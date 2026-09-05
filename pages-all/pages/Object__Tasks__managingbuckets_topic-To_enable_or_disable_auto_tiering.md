# Managing Auto-Tiering for an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm
- Fetched: 2026-09-05 02:51 CDT

# Managing Auto-Tiering for an Object Storage Bucket

Enable or disable auto-tiering for any Standard storage-tier Object Storage bucket.

You can enable auto-tiering during the creation of a bucket. See[Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)for more information.

You can enable or disable auto-tiering for an existing bucket using the instructions in this topic.

For more information on this feature, see[Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm#auto_tiering).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, find Auto-tiering .
- Select Enable or Disable .
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to enable auto-tiering a bucket.

```

```

Include the`auto-tiering`parameter and the`InfrequentAccess`value to enable the feature.
For example:
```

```

You can also disable auto-tiering at any time using the update action. Include the`auto-tiering`parameter and the`Disabled`value to disable the feature. For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
-
