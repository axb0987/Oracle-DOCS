# Configuring Authentication Factors
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-auth-factors.htm
- Fetched: 2026-09-05 02:25 CDT

# Configuring Authentication Factors

Configure the authentication factors to use for passwordless authentication.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Security and then MFA .
- In the Factors section, select one or more factors that you want users to use.
If authentication factors were enabled before passwordless authentication has been enabled, then you have to disable the authentication factors and save, then enable the authentication factors again and save otherwise they will not appear when you are setting up the IdP policy rule in the next step.
- Select Save changes .
