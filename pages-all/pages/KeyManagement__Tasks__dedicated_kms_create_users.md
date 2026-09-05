# Creating a User
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_create_users.htm
- Fetched: 2026-09-05 02:32 CDT

# Creating a User

Learn how to create a user with the Dedicated KMS user management utility.

Use the`createUser`command to create a Crypto User (CU) or Crypto Officer (CO) user. Only a Crypto Officer can run this command.
Important  
  
Ensure users are synchronized across all replicas before creating keys. Use the[listUsers](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/dedicated_kms_user_mgmt_listing_user.htm)command to verify user presence on all replicas. If users aren't synchronized, use the[syncUser](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/dedicated_kms_user_mgmt_sync_user.htm)command.

In the User Management utility, open a command prompt and run the`createUser`command to create a Crypto User (CU) or Crypto Officer (CO). Passwords must have a minimum of 12 characters and a maximum of 32 characters.

```

```

Parameter Description
Usertype The role assigned to the user. For Crypto Officer, use`CO`. For Crypto User, use`CU`.
Username The username for HSM sign in credentials. Username can be from 1 to 31 characters, and can use alphanumeric characters and the "_" (underscore) character.
Note
