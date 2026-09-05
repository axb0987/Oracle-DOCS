# Creating OAuth 2.0 Client Credentials
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_create_an_Oauth20_client_credential.htm
- Fetched: 2026-09-05 02:16 CDT

# Creating OAuth 2.0 Client Credentials

Use the Console to create a OAuth 2.0 client credentials.
Note  
  
OAuth 2.0 client credentials are not available in the following realms :
- the commercial realm (OC1)
- the Oracle UK Sovereign Cloud (OC4)
- View the user's details:
- If you're creating an OAuth 2.0 client credential for yourself:

Open the Profile menu and then select My Profile .
- If you're an administrator creating an OAuth 2.0 client credential for another user: On the Domains list page, select the domain in which you want to work. If you need help finding the list page, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../domains/to-view-identity-domains.htm). Depending on the options you see, to one of the following:
- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users . Find the user in the list, and then select the user's name to view the details.
- 

Select OAuth 2.0 client credentials .
- Select Generate OAuth 2.0 client credential .
- 

Select Name , and then enter a name for this credential.
- 

Select Title , and then enter a description for this credential.
- 

Add the URI for the OAuth 2.0 services that this credential will provide access to.
To Select an audience-scope pair :
- In Audience , enter the URI for the OAuth 2.0 services.
- Next, select the Scope for this credential. Always select the minimum required privileges.
- To add more permissions to this credential, select + Another scope and follow the instructions in the previous step.
- Select Generate . The new secret string is generated.

Select Copy to copy the token string immediately, because you can't retrieve it again after closing the dialog box.

If you're an administrator creating OAuth 2.0 client credentials for another user, you need to securely deliver them to the user by providing them verbally, printing them out, or sending them through a secure email service.
- Select Close .

You will need the following information from the credential for the token request:
- The generated secret
- The OCID of the OAuth 2.0 client credential
-
