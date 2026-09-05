# Listing Multipart Uploads in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm
- Fetched: 2026-09-05 02:51 CDT

# Listing Multipart Uploads in Object Storage

View a list of the in-progress multipart uploads for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Management and find the Uncommitted multipart uploads section.
Default filter is applied to hide uploads newer than 7 days. Remove the applied filter to view the complete list.
- 

Use the[oci os multipart list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/multipart/list.html)command and required parameters to list the in-progress multipart uploads in a bucket:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListMultipartUploads](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/ListMultipartUploads)operation to list the in-progress multipart uploads in a bucket.

See[Using the Multipart API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-Using_the_Multipart_Upload_API.htm)
