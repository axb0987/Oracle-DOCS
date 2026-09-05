# Getting an Object Storage Object Version's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm
- Fetched: 2026-09-05 02:52 CDT

# Getting an Object Storage Object Version's Details

View the details for an object version in an Object Storage bucket.

See[Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)for information on getting an object version's ID.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_get_the_contents_of_an_object_version.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- Find the object you want to work with. For more information, see[Listing Objects in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm).
- From the Actions menu (three dots) of the object, select View versions .
The Object versions panel opens.
- From the Actions menu for the object you want, select View object version details .
The Object version details panel opens. The latest version appears at the top of the list.
- From the Actions menu (three dots) for the object version, select View object version details .
The Object version details panel opens. All details of the object version are displayed. Select Download to copy the version details to your local computer.
- 

Get the details of an object as described in[Getting a Replication Policy's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm). Include the`version-id`parameter and the ID of the object version:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Get the details of an bucket using the[HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject)operation as described in[Getting a Replication Policy's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm). Include the`versionId`
