# Testing Your Custom SCIM Gateway Sample Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/scim/test-your-custom-scim-gateway-sample-application.htm
- Fetched: 2026-09-05 02:28 CDT

# Testing Your Custom SCIM Gateway Sample Application

Test your custom SCIM gateway sample application in an OCI IAM identity domain by provisioning users in an identity domain with it.

- In the Applications page, select your application, and then select it to open the Users tab.
- In the Users tab, select Assign .
- In the Assign Users window, choose a user, and then select Assign .
- In the Assign Application window, populate the Username , Full Name , Family Name , Given Name , Display Name , and Primary Email form fields with values, and then select Save .
- In the Assign Users window, select OK .
IAM creates a user account in the`userdb.json`file of your application.
- Open the`userdb.json`file and verify that a user account has been created. Then, close the file.
- In the Users tab, select the Actions menu (three dots) for the user, and then select Deactivate .
- After one minute, open the`userdb.json`file and verify that the corresponding user account has a`false`value for the`active`attribute. Then, close the file.
- In the Users tab, select the Actions menu (three dots) for the user, then select Activate .
- After one minute, open the`userdb.json`file and verify that the corresponding user account has a`true`value for the`active`attribute. Then, close the file.
- In the Users tab, select the user, and then select Revoke .
- In the Confirmation window, select OK .
- After the Confirmation window closes, open the`userdb.json`
