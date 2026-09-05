# Moving a Ping Monitor to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Moving a Ping Monitor to a Different Compartment

Move a ping monitor in Health Checks to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm#)
- 

- On the Health checks list page, find the ping monitor that you want to work with. If you need help finding the list page or the ping monitor, see[Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top).
- From the the Actions menu (three dots) for the ping monitor, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci health-checks ping-monitor change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/ping-monitor/change-compartment.html)command and required parameters to move a ping monitor to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ChangePingMonitorCompartment](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor/ChangePingMonitorCompartment)
