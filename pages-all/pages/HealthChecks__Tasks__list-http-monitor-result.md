# Listing Results for an HTTP Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Results for an HTTP Monitor

List results for an HTTP monitor in Health Checks.

Results are available a few moments after you create the monitor or on-demand probe. Each result includes the monitoring location (target), vantage points, endpoint availability, and test timestamp.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#)
- 

- On the Health checks list page, select the name of the HTTP monitor that you want to work with. If you need help finding the list page or the HTTP monitor, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top).
- On the HTTP monitor's details page, select Health check history
The past 90 days of results are available.
- To view details for a result, expand it.

## Filtering List Results

Use filters to limit the results in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).
- 

Use the[oci health-checks http-probe-result list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-probe-result/list.html)command and required parameters to list results for an HTTP monitor or on-demand probe:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ListHttpProbeResults](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbeResultSummary/ListHttpProbeResults)operation to list results for an HTTP monitor or on-demand probe.

[Example Responses](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#)

Following is an example healthy response.
```

```

Following is an example unhealthy response.
```

```

## Send an API Request to the Results URL

- On the Health checks list page, select the name of the HTTP monitor that you want to work with. If you need help finding the list page or the HTTP monitor, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top).
- Find the results URL from the details.
Example results URL for a ping monitor:
```

```

- Send a[signed API request](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm)to the results URL.
