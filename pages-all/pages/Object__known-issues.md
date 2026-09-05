# Known Issues for Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/known-issues.htm
- Fetched: 2026-09-05 02:52 CDT

# Known Issues for Object Storage

These known issues have been identified in Object Storage.

## PAR creation can fail when using long object names
Details Creating a pre-authenticated request (PAR) can fail when using long object names, resulting in a 500: Internal Server Error error. This failure is because of the size of the metadata associated with longer object names. Workaround Use shorter object names. The limit depends on implementation-specific details related to the user creating the PAR, so we can't currently give an exact limit. See[Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)for more information on that feature.

## Uncommitted or Failed Multipart Uploads in the Destination Bucket
Details Lingering uncommitted or failed multipart uploads might occur in replication destination buckets. You can't use the OCI Console or Object Lifecycle Management to delete the uncommitted or failed multipart upload parts on a destination bucket. Workaround

Use the OCI CLI, the bash script described in[Deleting a Multipart Upload from Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/To_delete_uncommitted_multipart_uploads.htm), or use a supported SDK using the[AbortMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/AbortMultipartUpload)API, such as[python](https://docs.oracle.com/iaas/tools/python-sdk-examples/2.159.0/objectstorage/abort_multipart_upload.py.html)
