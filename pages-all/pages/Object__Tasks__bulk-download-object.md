# Bulk Downloading Object Storage Objects
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/bulk-download-object.htm
- Fetched: 2026-09-05 02:50 CDT

# Bulk Downloading Object Storage Objects

Download a group of objects from a bucket to a computer file system.

## Using the CLI

Use the[oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html)command and required parameters to download a group of objects from a bucket:

```

```

where`download_directory_location`is the destination path for the objects being downloaded, such as`C:\workspace\Downloads\`or`/home/user/Documents/Downloads/`. If the directory doesn't exist, Object Storage creates the directory when you run the command.

For example:
```

```

By default, all objects in the bucket are downloaded. Use the Optional Parameters listed in the[oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html)page to specify what files in bulk to download.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/)
