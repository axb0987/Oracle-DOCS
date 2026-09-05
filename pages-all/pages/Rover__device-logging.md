# Device Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/device-logging.htm
- Fetched: 2026-09-05 03:02 CDT

# Device Logging

Roving Edge device logs are collected and uploaded to your tenancy. The logs are used by Oracle to troubleshoot problems that might arise. You can disable uploading of logs to your tenancy, for example, when your device isn't connected to your OCI tenancy.

By default, Roving Edge device logs are collected and stored every five minutes in two local Object Storage buckets:
- `orei-logs`– This bucket has application server logs, metrics logs, and OS logs.
- `orei-request-logs`– This bucket has audit logs.

The logs provide useful information:
- Records of user activity
- Device activity
- API metrics
- Error messages

You can view the logs by downloading them from the local buckets. See[Downloading an Object](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/get_object.htm#top).

By default, four preconfigured Data Sync tasks run hourly to upload the logs from the local buckets into Object Storage buckets in your OCI tenancy. The four Data Sync tasks are identified by OCIDs, that are referred to as task definition IDs:
```

```

## Disabling and Enabling Log Uploads

Prerequisite

The OCI CLI must be installed and configured to reach the Roving Edge device. See[Using the Command Line Interface with a Roving Edge Infrastructure Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI).
- 

Run the following command to disable log uploads.

```

```

Replace the following placeholders:
- 

&lt;device_hostname&gt; : The hostname of the device.
- 

&lt;task_definition_id&gt; : Specify one of the four predefined OCIDs. See[Getting a Data Sync Task's Details for Roving Edge Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/get_synchronization.htm#GetDataSyncTask).
- 

&lt;device-cert-bundle.pem_filepath&gt; : The file path to the CA bundle file.
- 

&lt;oci-config_filepath&gt; : The file path to the CLI`config`file.
- 

&lt;profile_name&gt; : The CLI profile that's configured to reach the device.
- 

&lt;true|false&gt; : Enter`false`to disable log uploads. Enter`true`to enable log uploads.

Example output of a successful command:
```

```

-
