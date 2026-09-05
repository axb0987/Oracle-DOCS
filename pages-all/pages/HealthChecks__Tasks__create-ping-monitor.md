# Creating a Ping Monitor
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm
- Fetched: 2026-09-05 02:13 CDT

# Creating a Ping Monitor

Create a ping monitor in Health Checks.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#)
- 

- On the Health checks list page, select Create health check . If you need help finding the list page, see[Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top).
- In the Create health check dialog box, enter the following values:

- 

Health check name : Enter a name for the ping monitor. Avoid entering confidential information.
- 

Create in compartment : Select the compartment to run the health check in. A default value from the scope is provided.
- 

Targets : Select or enter the hosts that you want to monitor with this health check. For each host, specify either the IP address or the name (fully qualified domain name, or FQDN).
- 

Vantage points : (Optional) Select up to ten locations to use for monitoring the targets. We recommend selecting at least three vantage points across three different providers. For more information about vantage points, see[Listing Vantage Points](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#top).
- 

Request type : Select Ping .
- 

Protocol : Select the network protocol to use: ICMP or TCP .
- 

Port (TCP protocol): Select the port to use for the connection. A port is required for the TCP protocol. The default value is 80.
- 

Timeout : Define the maximum time to wait for a reply before marking the health check as failed.
- 

Interval : Specify the period of time between health checks of the target.
- 

Tags : (Optional) Add one or more tags to the health check.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create health check .
The new ping monitor's details page opens. Results appear after a few moments.
- 

Use the[oci health-checks ping-monitor create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/ping-monitor/create.html)command and required parameters to create a ping monitor:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[CreatePingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor/CreatePingMonitor)
