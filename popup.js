let currentTabId = null;
let lastTokenCount = 0;

// Get current tab ID
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  if (tabs[0]) {
    currentTabId = tabs[0].id;
    loadTokens();
  }
});

// Listen for token captured messages from background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'tokenCaptured' && message.tabId === currentTabId) {
    showNotification(`Bearer token captured! (${message.tokenCount} total)`, 'success');
    loadTokens();
  }
});

// Show notification function
function showNotification(message, type = 'info') {
  const notification = document.getElementById('notification');
  notification.textContent = message;
  notification.className = `notification ${type}`;

  // Auto-hide after 3 seconds
  setTimeout(() => {
    notification.className = 'notification';
  }, 3000);
}

// Function to navigate to URL
function navigateToUrl(url) {
  // Clear old tokens before navigating to new URL
  chrome.runtime.sendMessage({
    action: 'clearTokens',
    tabId: currentTabId
  }, () => {
    // Navigate to the new URL
    chrome.runtime.sendMessage({
      action: 'navigateToUrl',
      tabId: currentTabId,
      url: url
    }, (response) => {
      if (response && response.success) {
        // Reload tokens display
        loadTokens();
      }
    });
  });
}

// Environment buttons handler
document.querySelectorAll('.env-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    const url = e.target.dataset.url;
    navigateToUrl(url);
  });
});

// Navigate button handler
document.getElementById('navigateBtn').addEventListener('click', () => {
  const url = document.getElementById('urlInput').value.trim();
  if (!url) {
    alert('Please enter a URL');
    return;
  }

  // Add https:// if no protocol specified
  let finalUrl = url;
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    finalUrl = 'https://' + url;
  }

  document.getElementById('urlInput').value = '';
  navigateToUrl(finalUrl);
});

// Clear button handler
document.getElementById('clearBtn').addEventListener('click', () => {
  if (confirm('Clear all captured tokens?')) {
    chrome.runtime.sendMessage({
      action: 'clearTokens',
      tabId: currentTabId
    }, () => {
      loadTokens();
    });
  }
});

// Load and display tokens
function loadTokens() {
  if (!currentTabId) return;

  chrome.runtime.sendMessage({
    action: 'getTokens',
    tabId: currentTabId
  }, (response) => {
    const tokensList = document.getElementById('tokensList');
    const noTokens = document.getElementById('noTokens');

    if (!response || !response.tokens || response.tokens.length === 0) {
      tokensList.innerHTML = '';
      noTokens.classList.add('visible');
      return;
    }

    noTokens.classList.remove('visible');

    tokensList.innerHTML = response.tokens.map((item, index) => {
      const date = new Date(item.timestamp);
      const timeStr = date.toLocaleTimeString();

      return `
        <div class="token-item">
          <div class="token-header">
            <span class="timestamp">${timeStr}</span>
            <button class="copy-btn" data-index="${index}">Copy Token</button>
          </div>
          <div class="token-metadata">
            <span class="token-type ${item.type}">${item.type}</span>
            <span class="token-url">${item.url}</span>
          </div>
          <div class="token-value">${item.token}</div>
        </div>
      `;
    }).join('');

    // Add copy button handlers
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const index = parseInt(e.target.dataset.index);
        const token = response.tokens[index].token;

        navigator.clipboard.writeText(token).then(() => {
          e.target.textContent = 'Copied!';
          e.target.classList.add('copied');
          setTimeout(() => {
            e.target.textContent = 'Copy Token';
            e.target.classList.remove('copied');
          }, 2000);
        });
      });
    });
  });
}

// Reload tokens every 2 seconds
setInterval(loadTokens, 2000);

// Allow Enter key to navigate
document.getElementById('urlInput').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    document.getElementById('navigateBtn').click();
  }
});
