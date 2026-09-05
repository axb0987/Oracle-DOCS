# Editing a User
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-user-account.htm
- Fetched: 2026-09-05 02:30 CDT

# Editing a User

Modify the details of a user account in an OCI IAM identity domain.
You can change all the information associated with the user except the Username.

User information is grouped under the following headings:
- User information
- User preferences
- Work information
- Other information

- On the Domains list page, select the domain for which you want to create a user. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the domain details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- Select the user account that you want to change.
- Select Edit user .
- Change an attribute value for the user account. If changing the identity provider used to authenticate a user:

- Federated : Turn on this option when the user signs in to the OCI Console using a federated IdP.
- Authenticated By : Select the application that the user is authenticated to. By default, the "Oracle Identity Domain" application is seeded in each identity domain.
-
