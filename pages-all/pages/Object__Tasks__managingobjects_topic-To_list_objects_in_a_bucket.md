# Listing Object Storage Objects in a Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Listing Object Storage Objects in a Bucket

View a list of the objects in an Object Storage bucket.

When you list the objects in a bucket, they appear in a table in lexicological (numerical + alphabetical) order.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.

## Filtering List Results

Use filters to limit the objects in the list. Perform one of the following actions depending on the options that you see:
- From the Search object by name or prefix box above the list table, enter a name or prefix to filter the list of objects displayed.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

To perform an action on an object directly from the object list table, select any of the following options from the Actions menu in the row for that object:
- View object details :[Open the Object details panel for the object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm).
- View versions :[Display a list of the versions of the object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm).
- Download :[Download the object to your computer](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm).
- Copy :[Copy the object to another bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm).
- Update storage tier :[Change the storage tier assigned to the object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_update_the_storage_tier_of_an_object.htm).
- Create pre-authenticated request :[Create a pre-authenticated request for the object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm).
- Re-encrypt :[Re-encrypt an object's data encryption keys with a different master encryption key.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm)
- Rename :[Change the name of the object.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm)
- Delete :[Remove the object from the bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm)

To create a bucket, select Create bucket .
- 

Use the[oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html)command and required parameters to list the objects in a bucket:

```

```

By default, a minimal number of fields are returned for each object. For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)operation to list the objects in a bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
