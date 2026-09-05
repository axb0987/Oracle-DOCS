# Deleting an Object Storage Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Deleting an Object Storage Object

Delete one or more objects from an Object Storage bucket

You can permanently delete an object from a bucket or folder. You can't, however, recover a deleted object unless you have object versioning enabled. See[Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm)for details.
Note  
  
You can't delete an object that has an active[retention rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu for the object you want, select Delete .
To delete several objects, select the check boxes next to the object names and select Delete from the Actions menu.
- When prompted, confirm the deletion.
- 

Use the[oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html)command and required parameters to delete an object from a bucket:

```

```

For example:
```

```

The object is deleted with no further information returned.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject)operation to delete an object from a bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
