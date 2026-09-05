# Disabling an HTTP Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-http-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Disabling an HTTP Monitor

Disable an HTTP monitor in Health Checks.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-http-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-http-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-http-monitor.htm#)
- 

- On the Health checks list page, find the HTTP monitor that you want to work with. If you need help finding the list page or the HTTP monitor, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top).
- From the Actions menu (three dots) for the HTTP monitor, select Disable .
- In the Disable health check dialog box, select Disable .
- 

Use the[oci health-checks http-monitor update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-monitor/update.html)command and required parameters to disable an HTTP monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[UpdateHttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor/UpdateHttpMonitor)operation to disable an HTTP monitor by setting the`isEnabled`attribute to`false`
