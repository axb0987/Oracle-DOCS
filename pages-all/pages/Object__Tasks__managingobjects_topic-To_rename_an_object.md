# Renaming an Object Storage Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm
- Fetched: 2026-09-05 02:51 CDT

# Renaming an Object Storage Object

Rename an object in an Object Storage bucket.

For information about object naming, see[Object Names](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_rename_an_object.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Objects .
The Objects tab opens. All objects in the selected bucket are displayed in a table.
- From the Actions menu for the object you want, select Rename .
The Rename object panel opens.
- Enter the new name for the object in the Object name box.
You can include an optional delimited directory structure prefix. For example,`p_94.jpg`or`/marathon/participants/p_94.jpg`. Avoid entering confidential information.
Caution  
  
Buckets can't store two objects that use identical names (case-sensitive). If you rename an object using the name of another object in the same bucket, the object that originally used the name is overwritten.
- Select Update .
- 

Use the[oci os object rename](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/rename.html)command and required parameters to rename an object in a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Renaming an Object Having a Specific Entity Tag

To make the rename operation dependent on the object having a specific entity tag, use the`--src-obj-if-match-e-tag`option.

For example:
```

```

## Overwriting an Object

For rename operations where you intend to overwrite one object in a bucket with another, you can make the renaming dependent on having a specific entity tag. To do so, use the`--new-obj-if-match-e-tag`option.

For example:
```

```

## Preventing Overwriting an Object

When renaming an object, you can prevent the system from overwriting another object in the same bucket by using the`--new-obj-if-none-match-e-tag *`option. This option prevents the renaming operation from completing if an object exists with the`--new-name`value specified and the same entity tag of the source object.

For example:

```

```

- 

Run the[RenameObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/RenameObject)operation to rename an object in a bucket.

Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```

```

The object name is everything after the`/o/`
