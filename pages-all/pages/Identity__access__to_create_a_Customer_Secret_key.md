# Creating a Customer Secret Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_create_a_Customer_Secret_key.htm
- Fetched: 2026-09-05 02:16 CDT

# Creating a Customer Secret Key

Use the Console to create a customer secret key.
- View the user's details:
- If you're creating a customer secret key for yourself:

Open the Profile menu and then select My Profile .
- If you're an administrator deleting an auth token for another user : On the Domains list page, select the domain in which you want to work. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../domains/to-view-identity-domains.htm). On the domain details page, perform one of the following actions depending on the option that you see:
- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users . Find the user in the list, and then select the user's name to view the details.
- 

Select Customer secret keys .

A customer secret key consists of an access key/secret key pair. Oracle automatically generates the access key when you or your administrator generates the secret key to create the customer secret key.
- Select Generate secret key .
- 

Select Name to enter a friendly name for the key, and then select Generate secret key .

The generated secret key is displayed in the Generate secret key dialog box. At the same time, Oracle generates the access key that is paired with the secret key. The newly generated customer secret key is added to the list of Customer secret keys .
- 

Select Copy to copy the secret key immediately, because you can't retrieve the secret key again after closing the dialog box, for security reasons.

If you're an administrator creating a secret key for another user, you need to securely deliver it to the user by providing it verbally, printing it out, or sending it through a secure email service.
- When you are finished, select Close .
-
