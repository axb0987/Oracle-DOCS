# Restoring a Deleted Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm
- Fetched: 2026-09-05 02:52 CDT

# Restoring a Deleted Object

Recover a deleted object to an Object Storage bucket.

When versioning is enabled, deleting an object without targeting a specific version creates a delete marker , and you can recover the previous version of the object. A deleted object only appears in the Objects list when the Show deleted object feature is selected. Any deleted objects listed have (Deleted Object) next to the object entry name. Expand the deleted object's version list and look for the version with (Delete marker) next to it. Restore a deleted object version by removing that delete marker. If a previous version exists, that version becomes the live object.
Note  
  
Versioning must be enabled for an Object Storage bucket at the time of the object's uploading. Objects deleted from a bucket with versioning disabled or suspended can't be recovered.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_recover_a_deleted_object.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu , select Show deleted objects .
Any deleted objects, including folders and subfolders, appear.
- Find the object that you want to recover.
- From the Actions menu (three dots) of the object, select View versions .
The list of versions of the object appears. The latest version appears at the top of the list and displays ( Latest version ).
- From the Actions menu (three dots) of the object, select Delete .
- When prompted, confirm the deletion.
The object version listed after the one whose delete marker you removed becomes the restored object.
- 

To restore a deleted object in a bucket using the CLI, you first need to know which object is marked for deletion. To obtain that information, list the objects in the bucket. See[Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)and select the CLI tab to run the appropriate command.

In the output, find the object version that has`"is-delete-marker": true`.

Use the[oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html)command and required parameters to restore a deleted object in a bucket. Include the`version-id`parameter and its value for that object.

```

```

When you run this command, you're prompted to confirm the deletion:
```

```

Answer with`y`.

For example:
```

```

The object's delete marker is deleted with no further information returned. The object is restored in its bucket. You can list the object to verify it has been restored after removing the delete marker.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Restoring Deleted Object in Bulk

To restore several objects in a bucket at the same time, use the available OCI CLI filters to query for the`"is-delete-marker": true`indicator. See "Using Queries" under[Managing CLI Input and Output](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)for more information.

For example, to restore a group of deleted objects, run the following command to get a list of objects with the delete marker and the version ID of each deleted object:
```

```

Next, pipe the output to another command or write a wrapper script to restore the deleted objects in the bucket. For example, to restore all objects in a bucket with the delete marker on a Linux host, run the following command:
```

```

You can use the`--force`parameter to avoid interactive mode. However, use this option with caution to avoid missing any important information.
- 

First, use the[ListObjectVersions](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjectVersions)operation to find objects with the`"is-delete-marker": true`. Then, use the[DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject)
