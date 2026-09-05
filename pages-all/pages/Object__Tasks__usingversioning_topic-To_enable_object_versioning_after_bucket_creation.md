# Managing Object Versioning for an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm
- Fetched: 2026-09-05 02:52 CDT

# Managing Object Versioning for an Object Storage Bucket

Enable or suspend object versioning on an Object Storage bucket.

By default, object versioning isn't enabled when you create a bucket. You can enable object versioning on an existing bucket. You can also suspend object versioning on a bucket where the feature is enabled. Versioning can't be disabled after it is enabled on a bucket. Versioning can only be suspended.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, find Object versioning under Features .
If object versioning is listed as Enabled , no further action is required. If object versioning is listed as Disabled or Suspended , select Enable .
- Select Enable versioning in the Enable object versioning confirmation box.
Object version is now enabled on the bucket. All later objects uploaded to the bucket are versioned.
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to enable or suspend object versioning in a bucket. Include the`versioning`parameter and a value of either`Enabled`or`Suspended`:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket)operation. Include the`versioning`attribute with either the`Enabled`or`Suspended`
