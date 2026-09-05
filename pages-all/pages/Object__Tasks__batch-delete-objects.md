# Batch Deleting Objects
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/batch-delete-objects.htm
- Fetched: 2026-09-05 02:50 CDT

# Batch Deleting Objects

Delete a specified list of objects in the same bucket with a single request.

Use the`BatchDeleteObjects`operation to delete up to 1,000 objects from a single bucket in one request. You provide the exact object names to delete. If versioning is enabled for the bucket, this operation deletes only the latest version of each listed object. If versioning isn't enabled, it deletes the object. You can't perform this task in the OCI Console. Instead, use the API or CLI.

## API and CLI references
- API: See[BatchDeleteObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/BatchDeleteObjects)in the Object Storage API Reference.
- CLI: See[batch-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/batch-delete.html)in the Object Storage CLI Command Reference.

## How Bulk Delete and Batch Delete Differ
- Use`BatchDeleteObjects`when you know the exact object names to delete and want to delete up to 1,000 objects from a bucket in a single request.
- Use the[bulk-delete](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bulk-delete-object.htm#top)command when you want to delete objects based on selection criteria such as a bucket and prefix, rather than providing an explicit list of object names. The CLI submits a separate delete request for each object that matches your criteria.

## IAM policies

To use`batchDeleteObjects`, you need the`OBJECT_DELETE`
