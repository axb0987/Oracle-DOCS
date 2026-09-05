# Moving an HTTP Monitor to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-http-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Moving an HTTP Monitor to a Different Compartment

Move an HTTP monitor in Health Checks to another compartment.
For general information about moving resources, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-http-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-http-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-http-monitor.htm#)
- 

- On the Health checks list page, find the HTTP monitor that you want to work with. If you need help finding the list page or the HTTP monitor, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top).
- From the the Actions menu (three dots) for the HTTP monitor, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci health-checks http-monitor change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/http-monitor/change-compartment.html)command and required parameters to move an HTTP monitor to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ChangeHttpMonitorCompartment](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor/ChangeHttpMonitorCompartment)
