# Configuring Duo Security
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-duo-security-settings.htm
- Fetched: 2026-09-05 02:23 CDT

# Configuring Duo Security

If you have implemented or want to implement Duo security as a third-party multifactor authentication (MFA) solution, and IAM manages your primary authentication and identity management, you can connect to and integrate with Duo to secure Oracle IaaS, PaaS, or SaaS applications or to secure applications already secured by an identity domain IAM.

- Download and install the Duo Mobile app from the Google Play Store or the Apple Store.
- Subscribe to Duo and create a Duo administrator account.

Go to[https://duo.com/](https://duo.com/)to set up your subscription and to set up your Duo administrative account. Refer to the[Duo documentation](https://duo.com/docs)for the latest instructions.
- Create and activate the Duo-protected Web SDK app.
See the[Duo documentation](https://duo.com/docs)for the latest instructions.
- Note the credentials and connecting host information.
These values were generated when you created and activated the Duo-protected Web SDK app. You need the values for Client ID , Client Secret , and API hostname . See the[Duo documentation](https://duo.com/docs)for the latest instructions.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Authentication .
- On the Authentication page, in the Duo security row, select Edit .
- Enter the credentials and connecting host information (client ID, client secret, and API hostname) that was generated from your Duo Administrative account, and then select a value for User identifier .
The User identifier that you select must map to the user identifier set in the Duo user account. For example, User name in the identity domain user account must map to Username in the Duo security user account.
- Enter a redirect URL in the Duo Security Authz Redirect Url field.
The redirect URL is used to start Duo security authentication, which receives a response from the Duo security server with the`duoSecurityAuthzState`and`duoSecurityAuthzCode`. The redirect URL must use https and specify the server by hostname, not by IP address, with a maximum length of 1024 characters.
- (Optional) Enable WebSDKv4 . Otherwise Duo Web SDK v2 is used by default.
- Select Save changes .
-
