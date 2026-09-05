# Changing a Password
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_changing_pwd.htm
- Fetched: 2026-09-05 02:33 CDT

# Changing a Password

Command to change password.

The`changePswd`command enables you to change the password of an existing user on the HSM partitions. You can change a password based on the following user role:
- Crypto Users (CU) can change only their password
- Crypto Officers (CO) can change theirs and CU's password

In the User Management utility, open a command prompt and run`changePswd`command to change the password of a user.

Syntax
```

```

Parameter Description
`Usertype`Role assigned to the user (such as CO and CU) to change a user password.
`Username`Name of the user.

Example
```

```
