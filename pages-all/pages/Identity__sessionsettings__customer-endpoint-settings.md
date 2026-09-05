# Changing Customer Endpoint Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/sessionsettings/customer-endpoint-settings.htm
- Fetched: 2026-09-05 02:28 CDT

# Changing Customer Endpoint Settings

Set customer endpoint settings in IAM.

- On the Session settings page, find the settings you want to change. If you need help finding the session settings page, see[Listing Session Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/sessionsettings/list-session-settings.htm).
- In Sign-in URL , enter the sign-in URL where you want the user redirected to sign in.
- To allow sign-in customization for the Admin Console, select Allow custom sign-in page .
- To show only the username field on the Sign In page, select Enable username first flow .
This allows the user to use[passwordless authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/sessionsettings/../passwordless/manage-passwordless.htm)by entering only their username.
- Choose whether users see a session picker or a domain picker when they sign in.

- The session pickers shows the user all active and historical sessions in different domains in the tenancy in the browser. To show the session picker, select Enable Session Picker for OCI console . This option is selected by default.
- The domain picker shows the user all domains available in the tenancy. To show the domain picker, unselect Enable Session Picker for OCI console .
- Enter a Sign-out URL . For example, to redirect the user to the My profile console, enter`/ui/v1/myconsole`.
- In the Error URL field, enter the tenant-specific error page URL to which a user is redirected after an error. This URL is used when the application-specific custom error URL isn't specified for an application.
- In Social linking callback URL , enter the URL to redirect to after linking a user between social providers and IAM is complete. This URL is used when the application-specific social linking callback URL isn't specified for an application.
-
