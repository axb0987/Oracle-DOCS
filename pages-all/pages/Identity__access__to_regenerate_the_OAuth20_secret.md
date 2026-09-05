# Regenerating the OAuth 2.0 Client Credential Secret
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_regenerate_the_OAuth20_secret.htm
- Fetched: 2026-09-05 02:16 CDT

# Regenerating the OAuth 2.0 Client Credential Secret

Use the Console to regenerate an OAuth 2.0 client credential secret.

IMPORTANT: When you regenerate the secret for a credential, requests made with the previous secret will be denied access to target scopes.
- View the user's details:
- If you're regenerating an OAuth 2.0 client credential secret for yourself:

Open the Profile menu and then select My Profile .
- If you're an administrator regenerating an OAuth 2.0 client credential secret for another user, on the Domains list page, select the domain in which you want to work. If you need help finding the list page, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../domains/to-view-identity-domains.htm). Depending on the options you see, to one of the following:
- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users . Find the user in the list, and then select the user's name to view the details.
- 

Select OAuth 2.0 client credentials .
- Select the name of the credential that you want to regenerate the secret for.
- Select Regenerate secret .
- Acknowledge the warning dialog and select Regenerate secret .
- 

Copy the token string immediately, because you can't retrieve it again after closing the dialog box.

If you're an administrator creating OAuth 2.0 client credentials for another user, you need to securely deliver them to the user by providing them verbally, printing them out, or sending them through a secure email service.
- Select Close .
