# Changing Snapshot Expiration Time
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm
- Fetched: 2026-09-05 02:04 CDT

# Changing Snapshot Expiration Time

If you need to keep a policy-based snapshot beyond its retention period, you can change or remove its expiration time. You can also add expiration times to user-created snapshots and change them as needed.

Note  
  
A snapshot without an expiration time persists unless it's manually deleted by a user or a new expiration time is set.

You can delete a snapshot manually at any time before it expires. Changes to the expiration time on a policy-based snapshot only apply to that snapshot, not the corresponding schedule or policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- In the Snapshots list, select the snapshot that you want to edit.
- On the snapshot's details page, change the expiration time of a snapshot using one of the following methods:

- To change the snapshot's expiration time, select Actions menu (three dots), and then select Edit . After editing, select Update .
- To remove the snapshot's expiration time, select Actions menu (three dots), and then select Remove .
- To add an expiration time to a snapshot, select Add next to Expiration time , select a time, and select Save changes .
- 

Use the[`oci fs snapshot update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/update.html)command and the`--expiration-time`parameter to change a snapshot's expiration time.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use[UpdateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/UpdateSnapshot)and`expirationTime`to change or remove a snapshot's expiration time.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
