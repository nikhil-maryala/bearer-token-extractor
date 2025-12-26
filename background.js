// Store captured tokens per tab
const tokens = new Map();

// Listen for web requests
chrome.webRequest.onBeforeSendHeaders.addListener(
  (details) => {
    if (details.requestHeaders) {
      for (const header of details.requestHeaders) {
        if (header.name.toLowerCase() === 'authorization') {
          const value = header.value || '';
          // Check if it's a bearer token
          if (value.toLowerCase().startsWith('bearer ')) {
            const token = value.substring(7); // Remove 'Bearer ' prefix

            // Store token for this tab
            if (!tokens.has(details.tabId)) {
              tokens.set(details.tabId, []);
            }

            const tabTokens = tokens.get(details.tabId);
            // Only add if not already present
            if (!tabTokens.some(t => t.token === token)) {
              tabTokens.push({
                token: token,
                url: details.url,
                timestamp: new Date().toISOString()
              });
            }
          }
        }
      }
    }
  },
  { urls: ["<all_urls>"] },
  ["requestHeaders"]
);

// Clean up tokens when tab is closed
chrome.tabs.onRemoved.addListener((tabId) => {
  tokens.delete(tabId);
});

// Handle messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getTokens') {
    const tabId = request.tabId;
    const tabTokens = tokens.get(tabId) || [];
    sendResponse({ tokens: tabTokens });
  } else if (request.action === 'clearTokens') {
    const tabId = request.tabId;
    tokens.delete(tabId);
    sendResponse({ success: true });
  } else if (request.action === 'navigateToUrl') {
    chrome.tabs.update(request.tabId, { url: request.url }, () => {
      sendResponse({ success: true });
    });
    return true; // Will respond asynchronously
  }
  return true;
});
