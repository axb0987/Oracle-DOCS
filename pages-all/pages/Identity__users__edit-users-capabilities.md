# Editing a User's Capabilities
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-users-capabilities.htm
- Fetched: 2026-09-05 02:30 CDT

# Editing a User's Capabilities

Change the capabilities that decide which user credentials users can create for themselves, such as local password, API keys, Auth token, SMTP credentials, customer secret keys, OAuth 2.0 client credentials, database passwords, in an OCI IAM identity domain.
The user capabilities you can select or clear are:
- Local password
- API keys
- Auth token
- SMTP credentials
- Customer secret keys
- OAuth 2.0 client credentials
- Database passwords

See[Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../usercred/usercredentials.htm)for details of each option.

- On the Domains list page, select the domain for which you want to edit a user's capabilities. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- Select a user to see the user details.
- Depending on the options you see, do one of the following:

- select Edit user capabilities
- select Actions and then select Edit user capabilities
- Select or clear the checkbox to add or remove a capability.

Note  
  
The Local password option is disabled for federated users.
-
