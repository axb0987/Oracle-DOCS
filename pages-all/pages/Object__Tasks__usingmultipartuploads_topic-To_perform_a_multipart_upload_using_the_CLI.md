# Running an Multipart Upload in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm
- Fetched: 2026-09-05 02:51 CDT

# Running an Multipart Upload in Object Storage

Describes how to upload a large object using multipart upload in Object Storage.

For prerequisite information, see[Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm#)
- 

This task can't be performed using the OCI Console.
- 

Use the[oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html)command with the`part-size`parameter to upload an object to a bucket:

```

```

where`part_size`value represents the size of each part in mebibytes (MiBs). Object Storage waives the minimum part size restriction for the last uploaded part. The`--part-size`value must be an integer.

Optionally, you can use the`--parallel-upload-count`parameter to set the maximum number of parallel uploads allowed:

```

```

For example:
```

```

For more information on the`oci os object put`command, see[Uploading an Object to a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/CreateMultipartUpload)operation to create a multipart upload to a bucket.

See[Using the Multipart API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-Using_the_Multipart_Upload_API.htm)
