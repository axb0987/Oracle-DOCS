# Encrypting a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm
- Fetched: 2026-09-05 02:03 CDT

# Encrypting a File System

File Storage file systems use Oracle-managed keys to encrypt a file system by default, which leaves all encryption-related matters to Oracle. Optionally, you can encrypt the data in a file system using your own Vault encryption key.

To encrypt a file system with your own key, ensure that the following prerequisites are met:
- At least one key vault and key in the Vault service. For more information, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
Caution  
  
Be sure to back up vaults and keys. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. For more information, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm).
- 

[Set the permissions](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm#required-iam-policy)that allow the File Storage service to use keys.

Note  
  
Only symmetric Advanced Encryption Standard (AES) keys are supported for file system encryption.

## Required IAM Policy

File systems encrypted using your own key require the ability to read keys stored in Vault. File Storage uses resource principals to grant a specific set of file systems access to the Vault key. This is a two step process, first the file systems which need access must be put into a dynamic group, and then the dynamic group is granted access to read the keys.

- 

Create a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)for the file systems with a rule such as the following:
```

```

Note  
  
If you have more than one rule in the dynamic group, ensure that you use`Match any rules defined below`option.
- 

Create an IAM policy that gives the dynamic group of file systems access to Vault keys:
```

```

In addition to creating policies for resource principal access, grant the File Storage service user access to read the keys using a policy such as the following:
```

```

The name of the File Storage service user depends on your realm . For realms with realm key numbers of 10 or less, the pattern for the File Storage service user is`FssOc <n> Prod`, where n is the realm key number. Realms with a realm key number greater than 10 have a service user of`fssocprod`. For more information about realms, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, From the Actions menu, select Edit Master encryption key .
- In the Edit Master encryption key page, select Encrypt using customer-managed keys .
Note  
  
If you assign a Vault key to a file system, you can later return the file system to using Oracle-managed keys for encryption by selecting Encrypt using Oracle-managed keys .
- Select the Vault compartment , Vault , Master encryption key compartment , and Master encryption key .
- Select Update .
- 

Use the[`fs file-system update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command and required parameters to encrypt the file system using the specified key:

```

```

Leave the`--kms-key-id`value unspecified to use Oracle-managed keys for encryption:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)operation to manage file system encryption.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
