# Adding an Apple Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/integrating-apple-idp.htm
- Fetched: 2026-09-05 02:22 CDT

# Adding an Apple Identity Provider

Learn how to set up an Apple social identity provider in identity domains in IAM,

An Apple Developer Account is required for Apple IdP integration. You can enroll in the Apple Developer Program using this link:`https://developer.apple.com/programs/enroll/`.

To set up an Apple social identity provider in identity domains in IAM, the following 4 attributes are required:
- 

Client ID
- 

Apple Dev ID
- 

Apple Key ID
- 

Apple Private Key file

## 1. Creating a Dev ID

To integrate an Apple social identity provider, complete the following steps.

- Sign in to Apple Developer portal and select Certificates, Identifiers &amp; Profiles .
- Select Identifiers and select the plus symbol near Identifiers .
- Select App IDs and create a new App ID by providing the Explicit Bundle ID and description.
- Select Sign In with Apple .
- Record the Team ID. The Team ID will be the Apple Dev ID of the Apple IdP.

## 2. Getting Client ID and Allowlist an Identity Domain URL

- Getting a Client ID
- Once the App ID is available, navigate to the Identifiers page and select the plus symbol.
- Select Service IDs .
- Provide the identifier and record it. This identifier will be the Client ID of the Apple IdP.
- Allowlisting an Identity Domain URL.
- After registering, edit the Services ID .
- Check Sign in with Apple and select Configure .
- In the Configure page, enter the identity domain details and Return URLs.

Note  
  

The allowlist URL must be in the following format:`<identity-domain-url>/oauth2/v1/social/callback`

Example:`https://<IdentityDomainID>.identity.oraclecloud.com/oauth2/v1/social/callback`

## 3. Creating a New Key and Getting a Key ID

This is the key used to create the client secret for the Apple IdP. In the Apple Developer portal, select Certificates, Identifiers &amp; Profiles .

- Select Keys .
- Select the plus icon to create a new key.
- Select Sign in with Apple and select Configure .
- Select the App ID and select Save . A new Key Pair is generated, and the Download Key page is displayed.
-
