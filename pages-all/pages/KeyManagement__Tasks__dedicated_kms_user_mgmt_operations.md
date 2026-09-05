# User Management Utility
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_operations.htm
- Fetched: 2026-09-05 02:33 CDT

# User Management Utility

Learn how to configure the user management CLI.

Using this utility, the Crypto User (CU) and the Crypto Officer (CO) can perform user and key management operations on an HSM cluster:
You can perform the following operations:
- Manage user accounts, including creating and deleting users, changing user passwords, and transferring ownership of CU keys.
- Manage keys, including find and transferring ownership of keys.
- Backup and restore a partition.
Note  
  
The CU user does not have permission to perform administrative tasks.

The User Management utility operates on two modes - Global and Server.

Global Mode : By default, the`User Management`utility is in global mode on restart. Any command that you run in global mode is applied on all HSM partitions in the cluster.
Global mode command prompt
```

```

Server mode: In this mode, the`User Management`utility enables you to execute commands on a specific HSM partition.
Server mode command prompt:
```

```

## To open the user management utility
- Open a Linux or Windows command line.
- 

Run one of the following commands, depending on your OS:

Windows:

```

```

Linux:

```

```
