# Deleting an Object Version for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm
- Fetched: 2026-09-05 03:01 CDT

# Deleting an Object Version for Roving Edge Infrastructure

Describes how to delete a particular version of an object in an object storage bucket on your Roving Edge Infrastructure device.

Only those objects that were uploaded to an object storage bucket with versioning enabled will have their versions available for deleting.

To delete object versions in bulk using the command line interface (CLI), see[Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete-object-versions.htm#)
- 

- Open the navigation menu and select Object Storage &gt; Object Storage . The Buckets page appears. All buckets are listed in tabular form.
- Select the bucket containing the object whose version you want to delete. The bucket's Details page appears. All objects are listed in tabular form.
- (optional) Enable Show Deleted Objects to display those objects that were versioned, but subsequently deleted.
- Select the Down arrow at the right side of the object's entry to display the versions.
- Select the Actions menu ( ) of the version you want to delete and select Delete .
- Confirm the deletion.
The list of versions of the object no longer includes the version you deleted.
- 

Run the`oci os object delete`command to delete an object from a bucket using the CLI as described in[Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#top). Include the`--version-id`parameter in the command to specify the version being deleted. For example:

```

```

- 

Run the`DeleteObject`operation to delete the version of an object in the Roving Edge Infrastructure device's object storage bucket as described in[Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#top). Include the`versionId`
