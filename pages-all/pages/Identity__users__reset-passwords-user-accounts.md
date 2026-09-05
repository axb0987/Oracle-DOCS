# Resetting a User Password
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-passwords-user-accounts.htm
- Fetched: 2026-09-05 02:30 CDT

# Resetting a User Password

Reset the password for a single account, for multiple accounts, or for all accounts in an OCI IAM identity domain.

When you request a password change, a notification is sent to the user or users so that they can provide a new password for the account. The user clicks the link in the notification to open a form where they provide a new password. The new password must conform to the password policy as[defined by an administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../passwordpolicies/Managing-Password-Policies.htm).

You can't reset the passwords for deactivated user accounts. To activate one or more deactivated accounts, search for accounts with a status of Inactive . Then, select individual accounts to activate, or select them all.

- On the Domains list page, select the domain for which you want to reset passwords. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- Select the checkbox of each user account for which to reset the password.

Tip  
  
To reset the passwords for all user accounts, don't select any checkboxes, and skip to the next step.
- Depending on what options you see, select Actions or More actions , and then perform one of the following:
- If you selected one or more user accounts, select Reset password . Then, in the Reset password dialog box, select Reset password .
- To reset the passwords for all accounts, select Reset all passwords . Then, in the Reset all passwords dialog box, select Reset all passwords .

Note  
  
For information about managing users and passwords on Oracle Autonomous AI Database Serverless, see the section on creating users in[Using Oracle Autonomous AI Database Serverless](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/manage-users-create.html#GUID-B5846072-995B-4B81-BDCB-AF530BC42847)
