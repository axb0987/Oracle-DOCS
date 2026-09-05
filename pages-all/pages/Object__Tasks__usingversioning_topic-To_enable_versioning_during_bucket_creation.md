# Enabling Object Versioning when Creating an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm
- Fetched: 2026-09-05 02:52 CDT

# Enabling Object Versioning when Creating an Object Storage Bucket

Enable object versioning when you create an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm#)
- 

- Create a bucket as described in[Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm).
- Select Enable object versioning to direct Object Storage to create an object version each time the content changes or the object is deleted.
- 

Create a bucket as described in[Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm). Include the`versioning`parameter with the value`enabled`:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Create a bucket using the[CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket)operation as described in[Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm). Include the`versioning`attribute with the value`enabled`
