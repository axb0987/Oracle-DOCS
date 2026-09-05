# Creating an Application User on Oracle E-Business Suite
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/create-app-user-ebs.htm
- Fetched: 2026-09-05 02:21 CDT

# Creating an Application User on Oracle E-Business Suite

You must create a specific application user that is authorized to connect to the Oracle E-Business Suite database. The Apps Schema Connect role determines the authorization to connect to the Oracle E-Business Suite database. A user that has this role is authorized to connect to the Oracle E-Business Suite database.

- Sign in to the Oracle E-Business Suite as an administrator. For example,`sysadmin`.
- In the Oracle E-Business Suite Home page, scroll down the Navigator , expand User Management , and then select Users .
- In the User Management page, select User Account from the Register menu, and then select Go .
- In the Create User Account page, enter the following details to create a user, and then select Submit .
- Username: Provide a username
- Password: Provide a password
- Description: E-Business Suite Asserter Service User
- Password Expire: None
Provide a temporary password for this user because the user needs to reset the password after first login.
- After the A new user account has been created. message appears, select Assign Roles , and then select Assign Roles in the Update User page.
- In the Search and Select: Assign Roles window, search for Code`UMX|APPS_SCHEMA_CONNECT`.
- Select Apps Schema Connect Role , and then select Select .
- In the Update User page, enter the justification as`EBS Asserter Service User`, and then select Save .

You can ignore the warning message regarding the Workflow Background Engine.
-
