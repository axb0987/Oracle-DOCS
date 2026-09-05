# Registering a Client Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm
- Fetched: 2026-09-05 02:24 CDT

# Registering a Client Application

Before you configure multifactor authentication (MFA) in an identity domain in IAM, register a client application so that you have the credentials (client ID and client secret) that are used for authentication in REST API calls. Oracle Support can use your client ID and client secret to help you troubleshoot if you have issues, for example, if you lock yourself out of an identity domain when configuring MFA.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Integrated applications .
- Select Add application.
- In the Add application dialog box, select Confidential Application , and then select Launch workflow .
- On the Add application details page, enter an application name and description, and then select Next .
- On the Configure OAuth page, under Client configuration , select Configure this application as a client now .
- Under Authorization , select only Client Credentials as the Allowed Grant Type .
- At the bottom of the page, select Add app roles and then select Add roles .
- In the Add app roles panel, select Identity Domain Administrator , and then select Add .
- Select Next and then select Finish .
- On the application detail page, scroll down to General Information . Copy the Client ID and the Client Secret and store it in a safe place.
-
