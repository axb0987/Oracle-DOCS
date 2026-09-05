# Deleting a Bucket from Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm
- Fetched: 2026-09-05 03:01 CDT

# Deleting a Bucket from Roving Edge Infrastructure

Describes how to delete an object storage bucket on your Roving Edge Infrastructure devices.

The bucket must be empty before you can delete it. See[Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../Object/delete_object.htm#top). If your bucket has versioning enabled, you must delete each version of all the objects contained in the bucket before you can delete the bucket. See[Deleting an Object Version](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../Object/delete-object-versions.htm#top).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/delete_bucket.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket that you want to delete. The bucket's Details page appears.
- 

Select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci os bucket delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/delete.html)command and required parameters to delete an object storage bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLI)
- 

Run the[DeleteBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/DeleteBucket)
