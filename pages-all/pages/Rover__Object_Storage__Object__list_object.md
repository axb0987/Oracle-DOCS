# Listing Objects for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm
- Fetched: 2026-09-05 03:01 CDT

# Listing Objects for Roving Edge Infrastructure

Describes how to list the objects contained within an Object Storage bucket on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/list_object.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket whose details you want to get. The bucket's Details page appears. All objects are listed in tabular form.
- 

Enable Show Deleted Objects to display those objects that were versioned, but subsequently deleted. If an object listed has versioning applied to it, you can select the Down arrow at the right side of the object's entry to display the versions.
- 

Use the[oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html)command and required parameters how to list the objects contained within an Object Storage bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLI)
- 

Run the[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)
