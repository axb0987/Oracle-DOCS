# Deleting a Replication
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm
- Fetched: 2026-09-05 02:03 CDT

# Deleting a Replication

Delete a File Storage replication resource.

Important  
  
Deleting the replication resource also deletes its associated replication target. If the source file system and replication resource aren't available (such as in the case of an outage), then[delete the replication target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm)to make the target file system exportable for failover.

When you delete a replication resource, you can specify which delete mode you want to use. File Storage replication offers three modes to give you the most flexibility for your data recovery requirements. Delete modes aren't available when[deleting a replication target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication-target.htm). During a disaster recovery operation where the source availability domain isn't available, the replication resource isn't accessible, and the replication process stops. Graceful delete
- If the replication is`capturing`,`transferring`, or`applying`, finish and then delete the replication.
- If the replication is`idle`, delete the replication immediately. Best for data safety. This option is moderately fast depending on how much data is being replicated. This option is called`finish_cycle_if_capturing_or_applying`by the File Storage API. Replicate and delete
- If the replication is`capturing`,`transferring`, or`applying`, finish the current cycle, start and finish one more cycle, and then delete the replication.
- If the replication is`idle`, start and finish one more cycle, and then delete the replication. Best for testing failover. This option is slowest, depending on how much data is being replicated and whether a delta cycle is already in progress when you delete the replication. This option is called`one_more_cycle`by the File Storage API. Apply and delete
- If the replication is`applying`or`transferring`, finish and then delete the replication.
- If the replication is`capturing`or`idle`, delete the replication immediately. Best for data safety during[disaster recovery](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/replication-disaster-recovery.htm). This option is moderately fast depending on how much data is being replicated. This option is called`finish_cycle_if_applying`by the File Storage API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-replication.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the source file system's details page, select Replications .
- From the Actions menu (three dots) of the replication, select Delete .
- Select the Delete mode that you want to use.
- Select Delete .
Note  
  
The amount of time that the replication takes to finish deleting depends on the mode you choose and the amount of data in the replication.
- 

Use the[`fs replication delete`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/replication/delete.html)command and required parameters to delete a replication:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteReplication](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Replication/DeleteReplication)operation to delete a replication.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
