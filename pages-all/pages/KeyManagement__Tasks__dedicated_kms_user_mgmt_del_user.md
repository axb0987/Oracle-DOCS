# Deleting a User
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_del_user.htm
- Fetched: 2026-09-05 02:33 CDT

# Deleting a User

Command to delete a user.

The`deleteUser`command deletes a user from a HSM partition. Only a Crypto Officer (CO) can run this command.

In the User Management utility, open a command prompt and run`deleteUser`command to delete a user of type specified in Usertype with given username from the HSM(s).

Syntax
```

```

Parameter Description
`Usertype`Role assigned to the user (such as CO and CU) to perform user management operations.
`Username`Name of luser to be deleted.

Example
```

```

Example: Server mode
```

```
