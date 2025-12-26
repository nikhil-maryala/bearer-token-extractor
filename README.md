# Bearer Token Extractor

A Chrome extension that captures bearer tokens from API calls and displays them in an easy-to-use popup interface.

## Features

- 🔍 Automatically captures bearer tokens from all HTTP requests
- 🌐 Navigate to any URL directly from the extension
- 📋 One-click copy to clipboard
- 🕒 Timestamp tracking for each captured token
- 🗑️ Clear all tokens with a single click
- 🔄 Auto-refreshes token list every 2 seconds

## Installation

1. Clone this repository or download the files
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked"
5. Select the directory containing the extension files

## Usage

1. Click the extension icon in your Chrome toolbar
2. Enter a URL in the input field and click "Navigate" (or press Enter)
3. The extension will automatically capture any bearer tokens from API calls made on the page
4. Click "Copy Token" to copy a specific token to your clipboard
5. Click "Clear All" to remove all captured tokens

## How It Works

The extension uses Chrome's `webRequest` API to intercept HTTP requests and extract bearer tokens from the `Authorization` header. Tokens are stored per tab and automatically cleaned up when tabs are closed.

## Permissions

- `webRequest`: To intercept and analyze HTTP requests
- `activeTab`: To interact with the current tab
- `scripting`: To execute scripts in the context of web pages
- `<all_urls>`: To capture tokens from any website

## Files

- `manifest.json`: Extension configuration
- `background.js`: Service worker that captures tokens from requests
- `popup.html`: User interface
- `popup.css`: Styling
- `popup.js`: Popup logic and interaction handling

## Security Notice

This extension captures authentication tokens. Use it responsibly and only on websites you own or have permission to test. Do not share captured tokens with unauthorized parties.

## License

MIT
