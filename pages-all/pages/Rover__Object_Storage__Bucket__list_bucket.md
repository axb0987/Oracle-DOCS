# Listing Buckets for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm
- Fetched: 2026-09-05 03:01 CDT

# Listing Buckets for Roving Edge Infrastructure

Describes how to list the object storage buckets on your Roving Edge Infrastructure devices.
Note  
  

The list contains only summary fields for the bucket and does not contain fields like the user-defined metadata.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/list_bucket.htm#)
- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Use the[oci os bucket list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/list.html)command and required parameters to list the object storage buckets on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLI)
- 

Run the[ListBuckets](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ListBuckets)
