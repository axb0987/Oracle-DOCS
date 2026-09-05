# Bulk Deleting Object Storage Objects
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bulk-delete-object.htm
- Fetched: 2026-09-05 02:50 CDT

# Bulk Deleting Object Storage Objects

Delete a group of objects in a bucket or folder.

Use the`bulk-delete`command to delete objects from a bucket based on selection criteria such as a prefix. The CLI submits a separate delete request for each object that matches your the criteria.
Note  
  
If you already know the exact object names to delete and want to delete up to 1,000 objects in a single request, use the`batchDeleteObjects`[API operation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/batch-delete-objects.htm#top).

## Using the CLI

Use the[oci os object bulk-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete.html)command and required parameters to delete a group of objects from a bucket:

```

```

For example:
```

```

By default, all objects in the bucket are deleted. Use the Optional Parameters listed in the[oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html)page to specify what files in bulk to delete.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/)
