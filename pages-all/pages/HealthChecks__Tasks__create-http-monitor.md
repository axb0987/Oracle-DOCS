# Creating an HTTP Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Creating an HTTP Monitor

Create an HTTP monitor in Health Checks.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#)
- 

- On the Health checks list page, select Create health check . If you need help finding the list page, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top).
- In the Create health check dialog box, enter the following values:

- 

Health check name : Enter a name for the HTTP monitor. Avoid entering confidential information.
- 

Create in compartment : Select the compartment to run the health check in. A default value from the scope is provided.
- 

Targets : Select or enter the hosts that you want to monitor with this health check. For each host, specify either the IP address or the name (fully qualified domain name, or FQDN).
- 

Vantage points : (Optional) Select up to ten locations to use for monitoring the targets. We recommend selecting at least three vantage points across three different providers. For more information about vantage points, see[Listing Vantage Points](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#top).
- 

Request type : Select HTTP .
- 

Protocol : Select the network protocol to use: HTTP or HTTPS .
Important  
  
If you select HTTPS for an IP address target, you must specify a host header with the domain name associated with the TLS certificate for that target in the Headers section. If you don't add the host header, the TLS connection phase doesn't complete successfully and the target endpoint is declared unavailable. Note that this host header is required only with IP address targets and HTTPS monitors.
- 

Port : Select the port to use for the connection. Default values are 80 for HTTP protocol and 443 for HTTPS protocol.
- 

Target path (HTTP protocol): Optionally specify the path on the target that you want to monitor. For example, for the target`www.example.com`, to monitor`www.example.com/project/help.htm`, specify`/project/help.htm`.
- 

Header name : (Optional) Define a name to display in the request header as part of the health check. Avoid entering confidential information.
- 

Header value : (Optional) Specify data to request.
- 

Method : Select the HTTP method to use.
- 

Timeout : Define the maximum time to wait for a reply before marking the health check as failed.
- 

Interval : Specify the period of time between health checks of the target.
- 

Tags : (Optional) Add one or more tags to the health check.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create health check .
The HTTP monitor's details page opens. Results appear after a few moments.
- 

Use the[oci health-checks http-monitor create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-monitor/create.html)command and required parameters to create an HTTP monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[CreateHttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor/CreateHttpMonitor)operation to create an HTTP monitor.

[Example Request and Response](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#)

The following example request creates an HTTP monitor to check the health of`www.example.com`using`GET`requests over HTTPS protocol every 30 seconds.
```

```

Following is an example`200`response for successful creation of the previously defined HTTP monitor. The`resultsUrl`field indicates the URL for retrieving results.
```

```
