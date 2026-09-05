# Getting an Object Storage Object's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm
- Fetched: 2026-09-05 02:51 CDT

# Getting an Object Storage Object's Details

View the details for an object in an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu for the object you want, select View object details .
- (Optional) Select Download to download the selected object.
Object details include basic information, response headers, metadata, and a preview of object contents, if applicable.
- 

Use the[oci os object head](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/head.html)command and required parameters to get the details of an object in a bucket:

```

```

For example:
```

```

If the object resides in an Archive tier bucket, the output also includes`archival-state`.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject)operation to get the details of an object in a bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
