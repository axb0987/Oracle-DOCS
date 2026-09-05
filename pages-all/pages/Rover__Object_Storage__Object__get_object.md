# Downloading an Object
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm
- Fetched: 2026-09-05 03:01 CDT

# Downloading an Object

Learn how to download an Object Storage object from a Roving Edge Infrastructure device to your computer.

To download objects in bulk using the command line interface (CLI), see[Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket whose details you want to get. The bucket's Details page appears. All objects are listed in tabular form.
- 

Select the Actions menu ( ) for the object whose details you want to get and select View Object Details . The Object Details dialog box appears.
- 

Select Download .

Alternately, you can select the Actions menu ( ) for the object in the Objects page and select Download .

The object is downloaded to your local computer in the default download location.
- 

Use the[oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html)command and required parameters to download an object contained to a bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLI)
- 

Run the[GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject)
