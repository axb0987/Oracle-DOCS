# Checking an Object Storage Object's Restoration Status
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_check_the_status_of_an_Archive_Storage_object_restoration.htm
- Fetched: 2026-09-05 02:51 CDT

# Checking an Object Storage Object's Restoration Status

Check the status of an Archive Storage object restoration.

## Using the CLI

Use the[oci os object restore-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/restore-status.html)command and required parameters to get that status of an object being restored from Archive Storage to Object Storage in a bucket:

```

```

By default, you have 24 hours to download an object after restoration. However, you can include the optional`hours`parameter with an integer value of download time of from 1 to 240 hours. For example:

```

```
You need`OBJECT_RESTORE`permissions to restore Archive Storage objects.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/)
