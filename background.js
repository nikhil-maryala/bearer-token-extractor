// Store captured tokens per tab (key is token, value is token info)
const tokens = new Map();

// Decode JWT token to get payload
function decodeJWT(token) {
  try {
    const parts = token.split('.');
    if (parts.length !== 3) return null;

    const payload = parts[1];
    const decoded = JSON.parse(atob(payload.replace(/-/g, '+').replace(/_/g, '/')));
    return decoded;
  } catch (e) {
    return null;
  }
}

// Determine token type based on URL and payload
function getTokenType(url, payload) {
  // Check if URL contains id-alpha.uipath.com
  if (url.includes('id-alpha.uipath.com') || url.includes('id.uipath.com') || url.includes('id-staging.uipath.com')) {
    return 'IdToken';
  }

  // Check client_id in payload
  if (payload && payload.client_id) {
    if (payload.client_id === '73ba6224-d591-4a4f-b3ab-508e646f2932') {
      return 'PortalPkceToken';
    } else if (payload.client_id === '1119a927-10ab-4543-bd1a-ad6bfbbc27f4') {
      return 'UserAccessToken';
    }
  }

  return 'Unknown';
}

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
              tokens.set(details.tabId, new Map());
            }

            const tabTokens = tokens.get(details.tabId);

            // Only add if not already present (using token as key for uniqueness)
            if (!tabTokens.has(token)) {
              const payload = decodeJWT(token);
              const tokenType = getTokenType(details.url, payload);

              tabTokens.set(token, {
                token: token,
                url: details.url,
                timestamp: new Date().toISOString(),
                type: tokenType,
                payload: payload
              });

              // Send notification to popup that a new token was captured
              chrome.runtime.sendMessage({
                action: 'tokenCaptured',
                tabId: details.tabId,
                tokenCount: tabTokens.size
              }).catch(() => {
                // Popup might not be open, ignore error
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
    const tabTokens = tokens.get(tabId) || new Map();
    // Convert Map to array for sending
    const tokensArray = Array.from(tabTokens.values());
    sendResponse({ tokens: tokensArray });
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
