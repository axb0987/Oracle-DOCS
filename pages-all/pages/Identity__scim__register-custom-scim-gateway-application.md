# Registering the Custom SCIM Gateway Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/scim/register-custom-scim-gateway-application.htm
- Fetched: 2026-09-05 02:28 CDT

# Registering the Custom SCIM Gateway Application

Register the custom SCIM gateway sample application with IAM.

- Open the navigation menu . Go to Identity , Domains , Settings , and select Applications .
- Select Add , and then select App Catalog .
- In the Type of Integration section, select Provisioning , locate the GenericScim - Basic template, and then select Add .
- In the Details pane of the GenericScim - Basic page, enter`SCIM Gateway Application`for both the name and description of your application, and then select Next .
- In the Provisioning pane, turn on the Enable Provisioning switch.
- In the Confirmation window, select OK .
- Use the following table to populate the fields of the Configure Connectivity section of the Provisioning tab.

Parameter Value
Host Name Enter the host name of your application.
Base URI`/scimgate`
Administrator Username`admin`
Administrator Password Enter the administrator's password you have set in the run script of the sample application.
HTTP Operation Types`__ACCOUNT__.Update=PUT`

For more information about the fields of the Configure Connectivity section, see the table in[Enable and Configure Connectivity for Provisioning for Your Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/enable-and-configure-connectivity-provisioning-your-application.htm).
- To save the application, select Finish .
If you deploy and run the sample application in a non-HTTPS server or a server which doesn't contain a valid certificate, then you might need to use a REST API to change the`SSLEnabled`parameter to`false`. If the server doesn't listen to the default HTTP port number, then change the`Port`
