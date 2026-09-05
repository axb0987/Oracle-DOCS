# Creating a Bucket for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm
- Fetched: 2026-09-05 03:01 CDT

# Creating a Bucket for Roving Edge Infrastructure

Describes how to create a object storage bucket on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/create_bucket.htm#)
- 

- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select Create Bucket . The Create Bucket dialog box appears.
- 

Enter a name in the Bucket Name box. The system generates a default bucket name that reflects the current year, month, day, and time, for example bucket-20190306-1359 . If you change this default to any other bucket name, use letters, numbers, dashes, underscores, and periods. Avoid entering confidential information.
- 

Select Enable Object Versioning if you want to apply versioning to all objects that you upload. See[Object Versioning](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../Object/object_versions.htm#ObjectManagement).
- 

Select Create .

The bucket is created and you can start uploading objects.
- 

Use the[oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html)command and required parameters to create a object storage bucket on your Roving Edge Infrastructure devices:

```

```

For example:
```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/../../Access/cli_install.htm#CLI)
- 

Run the[CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket)
