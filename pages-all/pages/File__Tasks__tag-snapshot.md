# Tagging a Snapshot
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-snapshot.htm
- Fetched: 2026-09-05 02:05 CDT

# Tagging a Snapshot

Manage tags for a File Storage snapshot.

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-snapshot.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-snapshot.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/tag-snapshot.htm#)
- 

- On the File Systems list page, select the file system that contains the snapshot that you want to work with. If you need help finding the list page or the file system, see[Listing File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-file-systems.htm).
- On the details page, select Snapshots .
- In the Snapshots list, select the snapshot that you're interested in.
- On the snapshot's details page, select Tags .
- Select Add tags to add new tags.
- 

Use the[`fs snapshot update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/update.html)command and include the optional parameters`--defined-tags`and`--freeform-tags`to manage a snapshot's tags:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/UpdateSnapshot)operation to manage a snapshot's tags.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
