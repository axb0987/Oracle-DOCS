# Creating a Snapshot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating a Snapshot

Create a snapshot of a File Storage file system. A snapshot is a point-in-time view of the file system.

After creation, snapshots are accessible under the root directory of the file system at`./snapshot/ <snapshot_name>`. If the snapshot is needed for only a limited time, you can[add an expiration time](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-expiration.htm). You can also create[policy-based snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm).

You can[use the snapshot to restore data](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/restore-from-snapshot.htm)or[clone a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/clone-file-system.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-snapshot.htm#)
- 

- On the File Systems list page, select the file system that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots and then Create Snapshot .
- 

In the Create Snapshot dialog box, provide the following information:
- Name : Enter a name for the snapshot. It must be unique among all other snapshots for this file system. The name can't be changed. Avoid entering confidential information.
- (Optional) Add expiration time : Select Add expiration time to add a date and time till which the snapshot is valid.
- (Optional) To tag the snapshot, select Add tag .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
- 

Use the[`fs snapshot create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/create.html)command and required parameters to create a snapshot:

```

```

Avoid entering confidential information.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/CreateSnapshot)operation to create a snapshot.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
