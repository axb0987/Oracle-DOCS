# About User Capabilities
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/userfed/about-user-capabilities.htm
- Fetched: 2026-09-05 02:30 CDT

# About User Capabilities

About user capabilities.

To access Oracle Cloud Infrastructure, a user must have the required credentials. Users who need to use the Console must have a password. Users who need access through the API need API keys. Some service features require additional credentials, such as auth tokens, SMTP credentials, and customer secret keys (previously known as Amazon S3 Compatibility API keys). For a user to get these credentials, the user must be granted the capability to have the credential type.

User capabilities are managed by an Administrator in the user's details. Each user can see their capabilities, but only an Administrator can enable or disable them. The user capabilities available to federated users are:
- API keys
- auth tokens
- SMTP credentials
- customer secret keys
- OAuth 2.0 client credentials

By default, these capabilities are enabled when you provision new users, allowing users to create these credentials for themselves. For information about these user credentials, see[Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/userfed/../usercred/usercredentials.htm).
Important
