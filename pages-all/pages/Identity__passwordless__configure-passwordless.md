# Configuring Passwordless Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-passwordless.htm
- Fetched: 2026-09-05 02:25 CDT

# Configuring Passwordless Authentication

Configure passwordless authentication settings and compliance policies that define which authentication factors that you want to allow, and then configure the passwordless factors.

There are three steps to setting up password authentication:
- First, change the session settings for a domain so that users sign in using their username followed by an additional factor, instead of signing in using their username and password.
- Then, select the authentication factors you want users to use. For example, one or more of:
- Email
- A TOTP (Time-Based One Time Password) from a mobile app passcode generator such as Oracle Mobile Authenticator (OMA) or Google Authenticator.
- A text message (SMS) or phone call.

To find out about the different authentication factors, see[Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/../mfa/configure-authentication-factors.htm).
- Finally, update the IdP policy to allow the authentication factors you have selected.

See[Creating an Identity Provider Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/../idppolicies/add-identity-provider-policy.htm)to see how you can configure login options for users.
- [Configuring Username Only Sign In](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-username-first.htm)
- [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-auth-factors.htm)
- [Configuring the IdP Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-idp-policy.htm)
