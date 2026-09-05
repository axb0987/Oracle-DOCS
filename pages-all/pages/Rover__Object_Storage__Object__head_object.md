# Getting an Object's Details for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm
- Fetched: 2026-09-05 03:01 CDT

# Getting an Object's Details for Roving Edge Infrastructure

Describes how to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/head_object.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket whose details you want to get. The bucket's Details page appears. All objects are listed in tabular form.
- 

Select the Actions menu ( ) for the object whose details you want to get and select View Object Details . The object's Details page appears. If object has versioning applied to it, the command is renamed View Object Versioning Details. The ObjecAll versions of the object are
- 

Use the[oci os object head](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/head.html)command and required parameters to get the details of an object contained within an Object Storage bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLI)
- 

Run the[HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject)
