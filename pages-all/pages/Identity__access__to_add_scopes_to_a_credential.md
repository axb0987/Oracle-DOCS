# Adding Scopes to an Existing OAuth 2.0 Client Credential
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_add_scopes_to_a_credential.htm
- Fetched: 2026-09-05 02:16 CDT

# Adding Scopes to an Existing OAuth 2.0 Client Credential

Use the Console to add scopes to an existing OAuth 2.0 client credential.
- View the user's details:
- If you're adding scopes to an OAuth 2.0 client credential for yourself:

Open the Profile menu and then select My Profile .
- If you're an administrator adding scopes to an OAuth 2.0 client credential for another user: On the Domains list page, select the domain in which you want to work. If you need help finding the list page, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../domains/to-view-identity-domains.htm). Depending on the options you see, to one of the following:
- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users . Find the user in the list, and then select the user's name to view the details.
- 

Select OAuth 2.0 client credentials .
- Select the name of the credential that you want to add scopes to.
- Select Add scopes .
- 

Add the URI for the OAuth 2.0 services that you want to add access to.
To Select a resource-scope pair :
- Select the Select a resource-scope pair option.
- The Resource list displays the resources you have permission to view. Select the resource you want to add credentials for. After you select the resource, the Audience field is automatically populated.
- Next, select the Scope for this credential. Always select the minimum required privileges.
To Enter fully qualified Scope :
- Select the Enter fully qualified scope option.
- Enter the Audience and Scope for this credential.
- To add more permissions to this credential, select + Another scope and follow the instructions in the previous step.
-
