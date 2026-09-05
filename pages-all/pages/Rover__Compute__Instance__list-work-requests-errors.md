# Listing an Instance's Work Request Errors for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-errors.htm
- Fetched: 2026-09-05 02:58 CDT

# Listing an Instance's Work Request Errors for Roving Edge Infrastructure

View a list of errors for an instance's work request for a Roving Edge Infrastructure device.

A work request is an activity log that tracks each step in an asynchronous operation. Use work requests to monitor the progress of long-running operations.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-errors.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-errors.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests-errors.htm#)
- 

- Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- (optional) Select a State from the list to limit the instances displayed to that state.
- Select the instance whose work request details you want to get. The Details page for that instance appears.
- Select Work Requests under Resources . The Work Requests page appears. All the work requests are listed in tabular form.
- Select the work request whose details you want to get. The Details page for that work request appears. The Details page contains information on the work request, including the time the job was accepted, started, and completed.
- Select Error Messages under Resources . The Error Messages page appears.

The Error Messages page displays error entries in the log and their timestamps.
- 

Use the[oci work-requests work-request-error list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/work-requests/work-request-error/list.html)command and required parameters to view a list of errors for an instance's work request for a Roving Edge Infrastructure device:
```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ListWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequestError/ListWorkRequestErrors)
