# Editing an Application
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Editing an Application

Change Oracle and custom applications in an identity domain in IAM. Assign users and groups, edit high-level information, import users and groups into the applications, export users and groups from applications, and perform specific configuration tasks for custom applications.
To modify applications:

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.

Tip  
  
To search for applications, enter all or part of the beginning of the application name that you want to find in the search field, and then press Enter . To fine-tune your search, select the search field again, and then select a status.
- Select the application to open a detailed view. The Applications page expands to open a sub page that displays high-level information about the application.

You can perform the following tasks in Oracle and custom applications:

- 

Oracle applications :
- 

Assign users and groups.
- 

Remove users and groups.

The Groups and Users tabs are used to display groups and users assigned to application roles of an Oracle application. Although you can filter and sort this list of users and groups, you can't change the list. You can't edit values in these tabs.
- 

Import and export users and groups for Oracle application roles.
Note  
  
If you assign users to Oracle application roles and then deactivate the accounts, IAM prevents the users from accessing the roles. To enable the users to access the Oracle application roles to which they're assigned, activate the users.
- 

View high-level information

See[Modify Oracle Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-oracle-applications.htm).
- 

Custom applications:
- 

Assign users and groups.
- 

Remove users and groups.
- 

Edit high-level information and configuration information.
- 

Edit Web Tier Policies for Trusted Applications.
- 

Regenerating a Client Secret and generating tokens for Trusted Applications
- 

Edit single sign-on (SSO) configuration for SAML Applications.

See[Modify Custom Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/modify-custom-applications.htm)
