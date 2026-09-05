# Uploading an Object to an Object Storage Bucket on a Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/put_object.htm
- Fetched: 2026-09-05 03:02 CDT

# Uploading an Object to an Object Storage Bucket on a Device

Learn how to upload an object to a Object Storage bucket on your Roving Edge Infrastructure device.

To upload objects in bulk using the CLI, see[Bulk Object Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/bulk_object_management.htm#top).
Note  
  

A Device Console session expires after 4 hours. If you use the Device Console to upload a large object, and the upload duration exceeds the session window, the upload fails. For large objects, use the CLI to perform multipart uploads to the device Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/put_object.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/put_object.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/put_object.htm#)
- 

The Device Console uses multipart uploads to upload objects larger than 64 MiB.
- 

In the Device Console, open the navigation menu and select Storage &gt; Object Storage &amp; Archive Storage . The Buckets page is displayed. All buckets are listed in tabular form.
- 

Select the bucket to which you want to upload objects. The bucket's Details page appears. All objects are listed in tabular form.
- 

Select Upload . The Upload Objects dialog box appears.
Note  
  

Checking objects in the Objects list and then selecting Upload does not automatically upload those files. Select files you want to upload in the Upload Objects dialog box.
- 

Specify an Object Name Prefix value. This prefix value is prepended to each one of the files you upload. You can specify the following prefix strings:
- Prefix strings without a delimiter for matching purposes to perform allowed bulk operations
- 

Select the group of objects you want to upload using any combination of the following methods:
- 

Drag and drop one or more files from your computer.
- 

Select the select files link and select the files you want to upload.

The files you select to upload are displayed in a list. If you decide that you do not want to upload a particular file, select the X to the right of the file name.

If the files you select to upload are already stored in the bucket or folder with the same name, the Console displays messages warning you of an overwrite.
- 

Select Upload . The selected objects are uploaded and displayed in the list of objects in the bucket.
- 

Select Close to return to the bucket's Details page.
- 

Use the[oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html)command and required parameters to upload an Object Storage object to a bucket on your Roving Edge Infrastructure devices:

```

```

Example:
```

```

Multipart Uploads

Use the[oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html)command with the following parameters to perform a multipart upload:
- 

part-size part_size

Specify the part_size in MiB to use when the file is split into multiple parts and then combined. Part size must be greater than 10 MiB and defaults to 128 MiB.
- 

--parallel-upload-count number_of_parallel_operations

Specify the number_of_parallel_operations as an integer range for the number of parallel operations to perform. Decreasing this value makes the process less resource intensive but it might take longer. Increasing this value might decrease the time taken, but the process consumes more system resources and network bandwidth. The maximum is 1000.
```

```

Example:
```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/../../Access/cli_install.htm#CLI)
- 

Run the[
