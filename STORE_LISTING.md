# Chrome Web Store Listing Information

## Basic Information

### Extension Name
```
Bearer Token Extractor
```

### Summary (132 character limit)
```
UiPath token extractor - Captures bearer tokens from API calls for development and testing with UiPath Cloud Platform
```

### Description (Full)
```
A Chrome extension primarily designed for UiPath token extraction - captures bearer tokens (UserAccessToken, PortalPkceToken, IdToken) from API calls and displays them in an easy-to-use popup interface. Perfect for UiPath developers and testers working with UiPath Cloud Platform authentication.

⚠️ SECURITY WARNING: This extension captures authentication credentials. Only use for authorized testing, development, and debugging.

FEATURES

Core Features:
• Automatically captures unique bearer tokens from all HTTP requests
• Detects and labels token types (IdToken, PortalPkceToken, UserAccessToken)
• Quick-nav buttons for UiPath environments (Alpha, Staging, Prod)
• Navigate to any URL directly from the extension
• One-click copy to clipboard
• Timestamp tracking for each captured token
• Clear all tokens with a single click
• Auto-refreshes token list every 2 seconds
• Memory-only storage (no persistence to disk)

Security Features:
• Token expiration warnings - Visual indicators for expired and expiring tokens
• Token masking - Option to hide middle portion of tokens (show first/last 8 chars)
• Auto-cleanup timer - Automatically clear tokens after configurable time (default: 15 minutes)
• URL validation - Prevents navigation to dangerous protocols
• Sender validation - Only accepts messages from extension pages
• Minimal permissions - Removed unused scripting permission

TOKEN TYPES

The extension automatically detects and categorizes tokens:
• UserAccessToken (Orange badge) - Shown first
• PortalPkceToken (Purple badge) - Shown second
• IdToken (Blue badge) - Tokens from UiPath identity services
• Unknown (Gray badge) - Other bearer tokens

SETTINGS

Click the settings button (⚙️) to configure:
• Auto-cleanup tokens - Enable automatic clearing after specified time (1-120 minutes)
• Token masking - Show only first and last 8 characters of tokens

HOW IT WORKS

1. Request Interception: Monitors all HTTP/HTTPS requests using Chrome's webRequest API
2. Token Extraction: Captures bearer tokens from Authorization headers
3. JWT Decoding: Decodes tokens to extract payload information (client_id, expiration, etc.)
4. Type Detection: Categorizes tokens based on request URL and JWT payload
5. Memory Storage: Stores tokens in memory, isolated per browser tab
6. Automatic Cleanup: Deletes tokens when tabs close or auto-cleanup timer expires

PRIVACY & SECURITY

✓ 100% local processing - No external servers
✓ No data collection or telemetry
✓ Memory-only storage (not saved to disk)
✓ Open source - Review the code on GitHub
✓ Comprehensive security documentation included

PERMISSIONS REQUIRED

• webRequest - To capture bearer tokens from HTTP request headers
• activeTab - To identify which tab tokens belong to
• storage - To save user preferences (auto-cleanup, masking settings)
• <all_urls> - To capture tokens from any website (can be restricted)

INTENDED USE

This extension is designed for:
✓ UiPath developers and testers
✓ Debugging UiPath Cloud Platform authentication
✓ Development and testing environments
✓ Authorized security testing

NOT for:
✗ Production environments
✗ Unauthorized access or testing
✗ Malicious purposes

For complete documentation, security analysis, and source code, visit:
https://github.com/nikhil-maryala/bearer-token-extractor

This extension is not affiliated with, endorsed by, or associated with JWT.io, Auth0, Inc., or UiPath Inc.
```

### Category
```
Developer Tools
```

### Language
```
English (United States)
```

---

## Images Required

You'll need to create these images:

### 1. Screenshots (Required - at least 1, recommended 3-5)
**Dimensions**: 1280x800 or 640x400
**Format**: PNG or JPEG

Screenshots to create:
1. **Main popup showing tokens**
   - Show the extension popup with 2-3 captured tokens
   - Display different token types (UserAccessToken, PortalPkceToken, IdToken)
   - Show expiration indicators

2. **Environment quick-nav buttons**
   - Highlight the Alpha, Staging, Prod buttons
   - Show the URL input field

3. **Settings modal**
   - Show the settings dialog open
   - Display auto-cleanup and token masking options

4. **Token details**
   - Close-up of token metadata (type badge, URL, timestamp)
   - Show the copy button

5. **Token masking example**
   - Side-by-side comparison of masked vs unmasked tokens

### 2. Small Promotional Tile (Required)
**Dimensions**: 440x280 pixels
**Format**: PNG or JPEG

Content suggestions:
- Extension icon (JWT logo)
- Text: "UiPath Token Extractor"
- Subtitle: "Capture & Manage Bearer Tokens"
- Background: UiPath brand colors (orange/purple) or neutral

### 3. Large Promotional Tile (Optional but recommended)
**Dimensions**: 920x680 pixels
**Format**: PNG or JPEG

Content suggestions:
- Extension icon
- Title: "Bearer Token Extractor"
- Key features as bullet points
- UiPath logo or branding elements

### 4. Marquee Promotional Tile (Optional)
**Dimensions**: 1400x560 pixels
**Format**: PNG or JPEG

---

## Additional Information

### Official URL (Optional)
```
https://github.com/nikhil-maryala/bearer-token-extractor
```

### Homepage URL (Optional)
```
https://github.com/nikhil-maryala/bearer-token-extractor
```

### Support URL (Optional)
```
https://github.com/nikhil-maryala/bearer-token-extractor/issues
```

### Privacy Policy URL (Required for extensions with user data)
```
https://github.com/nikhil-maryala/bearer-token-extractor/blob/main/PRIVACY_POLICY.md
```

---

## Distribution Settings

### Visibility
- ✅ **Public** - Listed in Chrome Web Store (recommended)
- ⬜ **Unlisted** - Only accessible via direct link
- ⬜ **Private** - Only for specific users/groups

### Regions
- ✅ **All regions** (recommended)
- ⬜ **Specific regions only**

### Pricing
```
Free
```

---

## Single Purpose Description (Required)

This field explains the single purpose of your extension:

```
This extension captures bearer tokens from HTTP Authorization headers and displays them to developers for debugging and testing purposes, with a primary focus on UiPath Cloud Platform authentication tokens.
```

---

## Permission Justifications

Chrome may ask you to justify broad permissions. Here's what to say:

### webRequest Permission
```
Required to intercept HTTP request headers and extract bearer tokens from the Authorization header. This is the core functionality of the extension - developers use it to capture and inspect authentication tokens during development and testing.
```

### <all_urls> Host Permission
```
Required to capture tokens from any website during development and testing. Developers may need to test authentication flows across various environments (alpha, staging, production) and different domains. The extension only reads Authorization headers and does not modify requests or responses.
```

### activeTab Permission
```
Required to identify which browser tab tokens belong to, enabling proper token isolation and management per tab. This ensures tokens from different testing sessions don't mix.
```

### storage Permission
```
Required to persist user preferences (auto-cleanup timer settings, token masking preference) across browser sessions. No sensitive data is stored - only user configuration settings.
```

---

## Maturity Rating

Select: **Everyone** (appropriate for all ages)

Justification: This is a developer tool that does not contain mature content.

---

## Test Account (If required)

If Chrome asks for test credentials:
```
This extension does not require authentication. Reviewers can test by:
1. Installing the extension
2. Navigating to any website that uses bearer token authentication
3. Opening the extension popup to see captured tokens

For UiPath-specific testing, navigate to: https://alpha.uipath.com/portal_/home
(Note: Requires UiPath account - can also test on any site with bearer tokens)
```

---

## Publishing Checklist

Before submitting:
- [ ] Extension is tested and working
- [ ] All icons are properly sized (16x16, 48x48, 128x128)
- [ ] Screenshots are created (1280x800)
- [ ] Small promotional tile created (440x280)
- [ ] Privacy policy is accessible
- [ ] manifest.json version is correct (1.1.0)
- [ ] Store listing information is complete
- [ ] ZIP file excludes .git, .DS_Store, node_modules
- [ ] Extension description clearly states "for development/testing only"
- [ ] All permissions are justified
- [ ] README.md is up to date

---

## Post-Publication

After approval:
1. Update README.md with Chrome Web Store link
2. Add Chrome Web Store badge to repository
3. Monitor user reviews and feedback
4. Respond to support requests via GitHub Issues
5. Plan for future updates if needed

---

## Expected Review Time

- **Initial Review**: 1-3 business days (can be up to 7 days)
- **Updates**: Usually faster, 1-2 days

## Common Rejection Reasons

Be prepared to address:
1. **Broad permissions** - Justify why you need <all_urls>
2. **Privacy policy** - Must be accessible and comprehensive
3. **Single purpose** - Must clearly state one main purpose
4. **Misleading description** - Be clear about security implications
5. **Trademark issues** - Already addressed with disclaimer

---

Good luck with the submission! 🚀
