# Listing an Instance's Work Request Log Entries for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-log-entry.htm
- Fetched: 2026-09-05 02:58 CDT

# Listing an Instance's Work Request Log Entries for Roving Edge Infrastructure

View a list of log entries for an instance's work request for a Roving Edge Infrastructure device.

A work request is an activity log that tracks each step in an asynchronous operation. Use work requests to monitor the progress of long-running operations.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-log-entry.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-log-entry.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-log-entry.htm#)
- 

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- (optional) Select a State from the list to limit the instances displayed to that state.
- Select the instance whose work request details you want to get. The Details page for that instance appears.
- Select Work Requests under Resources . The Work Requests page appears. All the work requests are listed in tabular form.
- Select the work request whose details you want to get. The Details page for that work request appears. The Details page contains information on the work request, including the time the job was accepted, started, and completed.
- Select Log Messages under Resources . The Log Message page appears.

The Log Messages page displays general entries in the log and their timestamps.
- 

Use the[oci work-requests work-request-log-entry list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/work-requests/work-request-log-entry/list.html)command and required parameters to view a list of log entries for an instance's work request for a Roving Edge Infrastructure device:
```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListWorkRequestLogs](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequestLogEntry/ListWorkRequestLogs)
