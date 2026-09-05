# Cloning a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm
- Fetched: 2026-09-05 02:02 CDT

# Cloning a File System

Clone a File Storage file system.

Before you can clone a file system, at least one snapshot must exist for the file system. For more information, see[Creating a Snapshot](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm). The clone is a copy of the file system data as it exists at the date and time that the selected snapshot was taken.

When you clone a file system, you can decide whether to detach the clone from its parent to create an independent file system.

Hydration begins immediately upon instantiation of the clone. To view the clone's hydration status, source snapshot, parent file system, and other cloning information, visit the details page of the cloned file system. For more information, see[Getting a File System's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-file-system-details.htm).

You can export, mount, and use the clone immediately for READ or WRITE operations after you create it. See[Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)and[Mounting File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)for more information. Cloned file systems are[managed](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingfilesystems.htm)in the same way that any other file system is managed.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the file system's details page, select Snapshots .
- In the list, find the snapshot you want to use as the source of the clone, select the Actions menu (three dots) , and then select Clone .

The clone is a copy of the file system data as it exists at the date and time that the selected snapshot was taken.
- In the Create Clone page, you can to accept the provided system defaults, or change them by selecting Edit details . The details are as follows:
- Name : The File Storage service creates a default name using`FileSystem-YYMMDD-HHMM`. Optionally, change the default name for the file system. It doesn't have to be unique; an Oracle Cloud Identifier (OCID) uniquely identifies the file system. Avoid entering confidential information.
- Compartment : Specify the compartment in which you want to create the file system.
- 
Encryption : File systems use Oracle-managed keys by default, which leaves all encryption-related matters to Oracle. Optionally, you can encrypt the data in this file system using your own Vault encryption key.
Note  
  
Only symmetric Advanced Encryption Standard (AES) keys are supported for file system encryption. To use[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)for your encryption needs, select Encrypt using customer-managed keys and see the[required IAM policies](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm#Required_IAM_Service_Policy). Select the vault compartment and vault that contains the master encryption key that you want to use, and then select the master encryption key compartment and master encryption key.
Caution  
  
Be sure to back up your vaults and keys. Deleting a vault and key otherwise means losing the ability to decrypt any resource or data that the key was used to encrypt. For more information, see[Backing Up and Restoring Vaults and Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/backingupvaultsandkeys.htm).
- 

(Optional) To add tags to the file system, select Show tagging options . If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Resource locks section, select a lock level:
- No Lock : No restrictions.
- Delete : Prevents the file system from being deleted.
- Full : Prevents all modifications except reading.
- (Optional) To detach the file system from the parent file system by selecting Detach clone file system from the parent file system .
- Select Create .
- 

Use the[`fs file-system create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create.html)command and the`--source-snapshot-id`parameter to specify the snapshot that you want to use as the source for the clone:

```

```

Use the`--clone-attach-status`parameter to detach the clone from its parent.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateFileSystem)operation and include the`sourceSnapshotId`parameter to clone a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
