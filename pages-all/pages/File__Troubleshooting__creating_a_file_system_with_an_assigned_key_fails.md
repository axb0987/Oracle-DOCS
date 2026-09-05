# Creating a File System With an Assigned Key Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/creating_a_file_system_with_an_assigned_key_fails.htm
- Fetched: 2026-09-05 02:05 CDT

# Creating a File System With an Assigned Key Fails

Creating a File Storage file system with an assigned Oracle Cloud Infrastructure Vault key fails.

The creation attempt fails with the following exception:
```

```

Cause: File Storage file systems require authorization to use keys on your behalf. Also, you must also authorize users to delegate key usage to the service in the first place. Authorization is provided to the service and users using specific IAM policies.

Solution:
- Create a policy in the tenancy to[let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id). For example:

```

```

- Assign the user who is creating the file system to the group.
- 

Create a dynamic group for file systems with a policy such as the following:
```

```

Note  
  
If you have more than one rule in the dynamic group, ensure that you use`Match any rules defined below`option.
- 

Create an IAM policy that gives the dynamic group of file systems read access to Vault secrets:
```

```

For more information, see[Encrypting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/encrypt-file-system.htm)and[Assigning Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys.htm)
