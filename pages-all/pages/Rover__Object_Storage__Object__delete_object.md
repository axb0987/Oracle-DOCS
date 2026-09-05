# Deleting an Object from Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm
- Fetched: 2026-09-05 03:01 CDT

# Deleting an Object from Roving Edge Infrastructure

Describes how to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices.

To delete objects in bulk using the command line interface (CLI), see[Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/delete_object.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket containing the object you want to delete. The bucket's Details page appears. All objects are listed in tabular form.
- 

Check each object that you want to delete.
- 

Select Delete Objects . To delete a single object, select the Actions menu ( ) for that object in the Buckets page and select Delete .
- 

Confirm the deletion when prompted.
- 

Use the following command and required parameters to delete an object storage object contained within an object storage bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLI)
- 

Run the[DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject)
