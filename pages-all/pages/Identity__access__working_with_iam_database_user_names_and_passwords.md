# Working with IAM Database User Names and Passwords
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/access/working_with_iam_database_user_names_and_passwords.htm
- Fetched: 2026-09-05 02:16 CDT

# Working with IAM Database User Names and Passwords

Database end users can easily use IAM database passwords because they can continue to use a well-known authentication method to access the database. You can access database passwords that you manage through your OCI profile after you successfully authenticate to OCI.

Before users can access or manage their database password, IAM administrators can create an extra layer of protection by enforcing multifactor authentication using[Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../mfa/understand-multi-factor-authentication.htm). For example, this can be a FIDO authenticator, or by pushing notifications through authenticator applications.

## IAM Database Password Security

Using IAM database usernames and IAM database passwords to access databases improves security because they allow IAM administrators to centrally manage users and user access to database passwords within IAM instead of locally in each database. When a user leaves an organization, their IAM account is suspended and therefore, their access to all databases are automatically suspended. This method removes the possibility of unauthorized accounts being left on database servers after a user has left. For more information, see[IAM Database Passwords](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../Concepts/usercredentials_topic-iam_database_passwords.htm). See[Authenticating and Authorizing IAM Users for Oracle DBaaS Databases](https://docs.oracle.com/en/database/oracle/oracle-database/26/dbseg/authenticating-and-authorizing-iam-users-oracle-dbaas-databases.html#GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8)in the Oracle Database Security Guide for information about how IAM users authenticate and authorize to OCI databases.

## IAM Database User Names

If your OCI IAM database username is longer than 128 bytes, you must set a different database username and a database password that's less than 128 bytes. IAM enforces the uniqueness of database usernames within a tenancy. The database user name isn't case-sensitive and has the same allowable characters as an IAM user name (ASCII letters, numerals, hyphens, periods, underscores, +, and @)). This is more restrictive than local database usernames, which are governed by the character set of the database. See[Database Object Names and Qualifiers](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Database-Object-Names-and-Qualifiers.html)for more information.

To create, change, and delete IAM database user names, see[Working with IAM Database User Names](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../Concepts/usercredentials_topic-iam_database_user_names.htm).

## Alternate IAM Database User Names

You can create an alternate IAM database user name that contains only letters and numbers, doesn't include special characters, and can be shorter than regular IAM database user names.

You can create an alternate IAM database user name:
- If your user name is too long or hard to type
- To make signing in easier with a user name that doesn't include special characters

## IAM Database Password Specifications

The IAM database password complexity uses almost the same rules supported in IAM for Console passwords (no double quotes ["] in IAM passwords). For details, see[Creating an IAM database password](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../Concepts/usercredentials_topic-creating_a_database_password.htm).

## Failed Login Lockouts

For information about failed logins, see[IAM Database Password Lockouts](https://docs.oracle.com/en-us/iaas/Content/Identity/access/../Concepts/usercredentials_topic-password_lockouts.htm).

## Password Rollovers
