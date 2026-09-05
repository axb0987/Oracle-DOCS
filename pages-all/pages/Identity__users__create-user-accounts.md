# Creating a User
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/create-user-accounts.htm
- Fetched: 2026-09-05 02:30 CDT

# Creating a User

Create a user account for a user in an OCI IAM identity domain.

- On the Domains list page, select the domain for which you want to create a user. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- Under Users select Create .
- In the First name and Last name fields enter the user's name.
- To have the user sign in with their email address, follow these steps:
- Leave the Use the email address as the username checkbox selected.
- In the Username / Email field, enter the email address for the user account.
- To have the user sign in with their username, follow these steps:
- Clear the Use the email address as the username checkbox.
- In the Username field, enter the person's username.

The following characters are allowed:
- a-z
- A-Z
- 0-9
- Special characters ! @ # $ % ^ &amp; * ( ) _ + = - { } [ ] | \ : " ' ; &lt; &gt; ? / . ,
- Blank spaces
- In the Email field, enter the email address for the user account.

Note  
  

If the Primary email address required checkbox is selected on the Domain settings page, then you must provide an email address in the Email field to create the user account.

If the Primary email address required checkbox is not selected, then you can create the account without entering an email address in the Email field.
- To assign the user to a group, select the checkbox for each group that you want to assign to the user account.
-
