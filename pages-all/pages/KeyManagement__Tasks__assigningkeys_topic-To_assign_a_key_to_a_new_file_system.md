# Assigning a key to a File System
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_file_system.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning a key to a File System

Assign a key to a file system using the OCI Console and CLI interface.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_file_system.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_file_system.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_file_system.htm#)
- 

- Open the navigation menu and select Storage . Under File Storage , select File Systems .
- Under List Scope , in the Compartment list, select the compartment where you want to create a file system that's encrypted with a Vault service master encryption key.
- 

Select Create File System , and then follow the instructions in[Creating File Systems](https://docs.oracle.com/iaas/Content/File/Tasks/creatingfilesystems.htm).
- 

Use the[fs file-system update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html)command and required parameters to encrypt the file system using the specified key:

```

```

Leave the`--kms-key-id`value unspecified to use Oracle-managed keys for encryption:

```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Run the[CreateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateFileSystem)and[Update File System](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem)to create and assign a key to a file system.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
