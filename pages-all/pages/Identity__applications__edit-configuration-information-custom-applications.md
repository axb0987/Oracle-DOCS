# Editing Configuration Information for Custom Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/edit-configuration-information-custom-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Editing Configuration Information for Custom Applications

You can edit configuration information for custom applications.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Integrated applications .
- Select the application that you want to modify.
- Select Configuration for the type of custom app.
- Select Edit configuration for the type of custom app.
- Expand the Client configuration area.
- Modify a configuration value for the custom application by:
- Entering the value in the attribute field (for example, in the Redirect URL field, entering the application URL where the user is redirected after authentication)
- Selecting a button (for example, adding a resource to the custom application by selecting Add or removing a scope for a trusted application by selecting Remove )
- Selecting or clearing the checkbox (for example, allowing the resource owner to be a grant type for the custom application by selecting Resource owner )
- Selecting the value from the menu (for example, selecting User administrator from the Grant the client access to Oracle Identity Cloud Service admin APIs. list to enable the custom application to access user administrator-related APIs)
- If your custom application is a confidential or a mobile application, then you can switch Bypass consent on or off.
- If your custom application is a confidential application, then expand the Resources node.
If your custom application is a mobile application, then the Resources node doesn't appear in the Configuration tab. This is because confidential applications run on a protected server, and mobile applications run on an unauthenticated web browser or a mobile device.
- Modify a configuration value for the protected resources of your confidential application. See step 3 for more information about how to edit configuration values.
- Select Save .

See[Add a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm),[Add a Mobile Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-mobile-application.htm), and[Add a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-saml-application.htm)
