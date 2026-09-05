# Listing Results for an HTTP On-Demand Probe
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Results for an HTTP On-Demand Probe

List results for an HTTP on-demand probe in Health Checks.

On-demand probes are available through SDK, CLI, and API. Results are available a few moments after you create the monitor or on-demand probe. Each result includes the monitoring location (target), vantage points, endpoint availability, and test timestamp.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#)
- 

This task can't be performed using the Console.
- 

Use the[oci health-checks http-probe-result list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-probe-result/list.html)command and required parameters to list results for an HTTP monitor or on-demand probe:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ListHttpProbeResults](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbeResultSummary/ListHttpProbeResults)operation to list results for an HTTP monitor or on-demand probe.

[Example Responses](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#)

Following is an example healthy response.
```

```

Following is an example unhealthy response.
```

```

## Send an API Request to the Results URL

- Get details for the HTTP on-demand probe.
Review the response on creation. See[Creating an HTTP On-Demand Probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#top).
- Find the results URL from the details.
Example results URL for a ping monitor:
```

```

- Send a[signed API request](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm)to the results URL.
