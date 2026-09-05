# Enabling a Ping Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Enabling a Ping Monitor

Enable a ping monitor in Health Checks.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm#)
- 

- On the Health checks list page, find the ping monitor that you want to work with. If you need help finding the list page or the ping monitor, see[Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top).
- From the Actions menu (three dots) for the ping monitor, select Enable .
- In the Enable health check dialog box, select Enable .
- 

Use the[oci health-checks ping-monitor update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/ping-monitor/update.html)command and required parameters to enable a ping monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[UpdatePingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor/UpdatePingMonitor)operation to enable a ping monitor by setting the`isEnabled`attribute to`true`
