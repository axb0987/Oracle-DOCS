# Getting an Object Storage Object's ETag
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-head_objects.htm
- Fetched: 2026-09-05 02:51 CDT

# Getting an Object Storage Object's ETag

Get the user-defined metadata and entity tag (ETag) for an object.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-head_objects.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-head_objects.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-head_objects.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- Select the Actions menu next to the object name, and select View object details .
The Object details panel opens. Object details include basic information, response headers, metadata, and a preview of object contents, if applicable.
- Find the ETag attribute.
The ETag for the object is displayed.
- 

Use the[oci os object head](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/head.html)command and required parameters to get the details of an object in a bucket.

```

```

Find the`etag`attribute. For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject)operation to get the details of an object in a bucket. Find the`etag`
