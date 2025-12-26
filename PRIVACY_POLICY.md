# Privacy Policy for Bearer Token Extractor

**Last Updated: December 26, 2025**

## Overview

Bearer Token Extractor ("the Extension") is a developer tool designed primarily for UiPath token extraction. This privacy policy explains what data the Extension collects, how it's used, and your privacy rights.

## Developer Information

- **Extension Name**: Bearer Token Extractor
- **Developer**: Nikhil Maryala
- **Contact**: https://github.com/nikhil-maryala/bearer-token-extractor/issues

## What Data We Collect

### Data Collected Locally (Not Transmitted)

The Extension collects the following data **locally on your device only**:

1. **Bearer Tokens**
   - Captured from `Authorization` headers in HTTP/HTTPS requests
   - Stored temporarily in browser memory only
   - Never persisted to disk or transmitted to external servers

2. **Request URLs**
   - URLs where bearer tokens are used
   - Stored temporarily in memory for display purposes only

3. **JWT Payload Data**
   - Token metadata (client_id, expiration times, etc.)
   - Decoded locally for display and categorization
   - Never transmitted externally

4. **User Preferences**
   - Settings (auto-cleanup enabled/duration, token masking preference)
   - Stored locally using Chrome's `chrome.storage.local` API
   - Never synchronized or transmitted

5. **Timestamps**
   - When tokens were captured
   - Used for display and auto-cleanup functionality

### Data NOT Collected

- ❌ Personal information (name, email, address, etc.)
- ❌ Browsing history beyond current session
- ❌ Form data or user input
- ❌ Passwords or credentials (other than bearer tokens)
- ❌ Cookies or session data
- ❌ Request/response bodies
- ❌ Analytics or telemetry

## How We Use Data

All data is used **exclusively** for the Extension's core functionality:

- **Display captured tokens** in the popup interface
- **Categorize tokens** by type (UserAccessToken, PortalPkceToken, IdToken, Unknown)
- **Show expiration warnings** for JWT tokens
- **Enable copy-to-clipboard** functionality
- **Auto-cleanup** tokens after user-configured time

## Data Storage and Retention

### Storage Location
- **Memory Only**: Tokens are stored in browser memory (JavaScript variables)
- **Local Storage**: User preferences stored in `chrome.storage.local`
- **No Remote Storage**: No cloud storage, databases, or external servers

### Data Retention
- **Tokens**: Deleted when:
  - Browser tab is closed
  - User clicks "Clear All" button
  - Auto-cleanup timer expires (if enabled)
  - Extension is uninstalled
- **Settings**: Persist until extension is uninstalled or user clears browser data

### Data Deletion
To delete all data:
1. Click "Clear All" in the extension popup (removes tokens)
2. Uninstall the extension (removes all data including settings)
3. Clear browser storage via `chrome://settings/clearBrowserData`

## Data Sharing and Transmission

### We Do NOT:
- ❌ Transmit any data to external servers
- ❌ Share data with third parties
- ❌ Use analytics or tracking services
- ❌ Collect telemetry or usage statistics
- ❌ Send data to advertisers or data brokers

### 100% Local Processing
- All token extraction and processing happens locally on your device
- No network requests are made by the Extension (except user-initiated navigation)
- Zero external communication

## Permissions Explained

The Extension requests the following Chrome permissions:

1. **`webRequest`** (Required)
   - Purpose: Intercept HTTP headers to extract bearer tokens
   - Data Access: Can read request headers from all websites
   - Usage: Only reads `Authorization` headers; ignores all other data

2. **`activeTab`** (Required)
   - Purpose: Identify current browser tab for token isolation
   - Data Access: Current tab URL and metadata
   - Usage: Tab identification only; no content access

3. **`storage`** (Required)
   - Purpose: Save user preferences (settings)
   - Data Access: Local storage on your device
   - Usage: Stores auto-cleanup and masking preferences only

4. **`host_permissions: <all_urls>`** (Required)
   - Purpose: Capture tokens from any website during development/testing
   - Data Access: Can monitor network traffic on all websites
   - Usage: Only reads `Authorization` headers; all other data ignored
   - **Note**: Can be manually restricted to specific domains

## Security Measures

- ✅ **Memory-only storage** - No disk persistence of sensitive tokens
- ✅ **Tab isolation** - Tokens isolated per browser tab
- ✅ **Sender validation** - Only accepts messages from extension pages
- ✅ **URL validation** - Prevents navigation to dangerous protocols
- ✅ **Auto-cleanup** - Optional automatic token deletion
- ✅ **Token masking** - Option to hide token values in UI
- ✅ **No external communication** - Zero network requests to third parties

## Intended Use

This Extension is intended **only for**:
- Authorized development and testing environments
- Debugging authentication flows
- UiPath Cloud Platform development
- Security research (with proper authorization)

This Extension is **NOT intended for**:
- Production environments
- Unauthorized access or testing
- Malicious purposes
- Data theft or credential harvesting

## Children's Privacy

This Extension is not directed at children under 13. We do not knowingly collect information from children. This is a developer tool for professional use.

## Changes to Privacy Policy

We may update this Privacy Policy from time to time. Changes will be posted to:
- This document in the Extension's GitHub repository
- Chrome Web Store listing (if material changes)

Continued use after changes constitutes acceptance of the updated policy.

## Compliance

### GDPR (European Union)
- **No personal data collected**: Extension does not process personal data as defined by GDPR
- **No cookies**: Extension does not use cookies
- **Local processing**: All data processing is local; no data controllers or processors involved
- **Right to deletion**: Users can delete all data by clearing tokens or uninstalling

### CCPA (California)
- **No sale of data**: We do not sell user data
- **No data sharing**: We do not share data with third parties
- **Data deletion**: Users can delete data at any time

## Data Protection Officer / Contact

For privacy questions or concerns:
- **GitHub Issues**: https://github.com/nikhil-maryala/bearer-token-extractor/issues
- **Email**: [Your email if you want to provide one]

## Third-Party Services

This Extension does **NOT** use:
- Analytics services (e.g., Google Analytics)
- Crash reporting services
- Advertising networks
- Social media integrations
- Cloud storage services
- Any third-party APIs or services

## User Rights

You have the right to:
- ✅ **Access**: View all captured tokens in the extension popup
- ✅ **Deletion**: Clear tokens at any time via "Clear All" button
- ✅ **Control**: Configure auto-cleanup and masking settings
- ✅ **Transparency**: Review source code at https://github.com/nikhil-maryala/bearer-token-extractor
- ✅ **Uninstall**: Remove extension and all associated data at any time

## Open Source

This Extension is open source under the MIT License:
- Source code: https://github.com/nikhil-maryala/bearer-token-extractor
- Security review: See SECURITY.md in repository
- Users can audit all code and data handling practices

## Disclaimer

This Extension handles authentication credentials. Users are responsible for:
- Ensuring proper authorization before use
- Protecting captured tokens from unauthorized access
- Compliance with applicable laws and regulations
- Proper handling of authentication credentials
- Using only in authorized testing environments

**The developer is not responsible for misuse, unauthorized access, or security incidents resulting from use of this Extension.**

## Agreement

By installing and using this Extension, you agree to this Privacy Policy and understand:
- The Extension captures bearer tokens from HTTP requests
- All data is stored locally and never transmitted externally
- The Extension is for authorized testing and development only
- You are responsible for proper use and token security

---

**This Privacy Policy is effective as of December 26, 2025.**
