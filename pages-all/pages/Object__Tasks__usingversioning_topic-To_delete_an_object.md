# Deleting an Object Storage Object Version
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm
- Fetched: 2026-09-05 02:52 CDT

# Deleting an Object Storage Object Version

Delete an object's version from an Object Storage bucket.

Deleting an object's version is permanent. You can't recover a deleted version. See[Object Version Deletion](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#Understa)for more information.

See[Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)for information on getting an object version's ID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- Find the object you want to work with. For more information, see[Listing Objects in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm).
- From the Actions menu (three dots) of the object, select View versions .
The Object version details panel opens. The latest version appears at the top of the list.
- From the Actions menu (three dots) for the object version, select Delete .
- When prompted, confirm the deletion.
The version you deleted no longer appears in the object's list of versions.
- 

Use the[oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html)command and required parameters as described in[Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm). Include the`version-id`parameter and version ID:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject)operation to delete an object from a bucket. Include the`versionId`attribute and the version ID.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
