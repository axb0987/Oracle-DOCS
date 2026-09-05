# Bulk Uploading Object Storage Objects to a Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bulk-upload-object.htm
- Fetched: 2026-09-05 02:50 CDT

# Bulk Uploading Object Storage Objects to a Bucket

Upload a group of objects from a file system to an Object Storage bucket or folder.

To upload objects larger than 64 MiB, the Console uses multipart uploads. You need OBJECT_CREATE and OBJECT_OVERWRITE permissions to perform multipart uploads. For details, see[Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm)and[Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).

## Using the CLI

Use the[oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html)command and required parameters to upload a group of files in a directory and its sub-directories to a bucket:

```

```

where`source_directory_location`is the upload file system directory path, such as`C:\workspace\Upload\`or`/home/user/Documents/Upload`.

If your source directory has subdirectories, the subdirectory names are prepended to the names of the files stored in those subdirectories, delimited with a forward slash (/) character. For example, if a file named`maple.jpg`is stored in the subdirectory`trees`, when the file is uploaded, Object Storage assigns the name`trees/maple.jpg`to the resulting object.

By default, all objects in the bucket are uploaded. Use the Optional Parameters listed in the[oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html)page to specify what files in bulk to upload.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### Specifying the Storage Tier of the Uploaded Bulk Objects

Include the`storage-tier`parameter to assign a storage tier to the objects you're uploading in bulk.

```

```

For example, if you're uploading to a Standard tier-configured bucket and you wan to upload objects to the Infrequent Access storage tier, include`--storage-tier InfrequentAccess`in the command:
```

```

See[Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/../Concepts/understandingstoragetiers.htm)for more information on how storage tiers work.

If you don't specify`--storage-tier`, the object is automatically assigned and uploaded to the default storage tier of the bucket (Standard or Archive).

### Appending a Prefix String to the Uploaded Bulk Objects

To append a[prefix string](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix)to the object names created by your bulk upload, include the`object-prefix`parameter. For example:

```

```
