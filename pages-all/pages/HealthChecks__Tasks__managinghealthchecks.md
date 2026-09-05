# Managing Health Checks
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm
- Fetched: 2026-09-05 02:13 CDT

# Managing Health Checks

Monitor the health of IP addresses and hosts using HTTP and ping monitors and on-demand probes.
Note  
  
Monitors, metrics, and probes that you create with the SDK, CLI, and API are associated with the region where you configure them. While using the API, you must perform monitor updates (including compartment changes), metrics retrieval, and probe results retrieval in the region where you configured them. However, you can list currently configured monitors and monitor details in every region, no matter where the monitors were configured.

- [HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-monitors.htm#top)
- [Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top)
- [Creating an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#top)
- [Getting an HTTP Monitor's Details](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/get-http-monitor.htm#top)
- [Listing Results for an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#top)
- [Updating an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/update-http-monitor.htm#top)
- [Duplicating an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/duplicate-http-monitor.htm#top)
- [Disabling an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-http-monitor.htm#top)
- [Enabling an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-http-monitor.htm#top)
- [Moving an HTTP Monitor to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-http-monitor.htm#top)
- [Deleting an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/delete-http-monitor.htm#top)
- [Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-monitors.htm#top)
- [Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top)
- [Creating a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#top)
- [Getting a Ping Monitor's Details](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/get-ping-monitor.htm#top)
- [Listing Results for a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor-result.htm#top)
- [Updating a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/update-ping-monitor.htm#top)
- [Duplicating a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/duplicate-ping-monitor.htm#top)
- [Disabling a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/disable-ping-monitor.htm#top)
- [Enabling a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/enable-ping-monitor.htm#top)
- [Moving a Ping Monitor to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/change-compartment-ping-monitor.htm#top)
- [Deleting a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/delete-ping-monitor.htm#top)
- [On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/probes.htm#top)
- [HTTP On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-probes.htm#top)
- [Creating an HTTP On-Demand Probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-probe.htm#top)
- [Listing Results for an HTTP On-Demand Probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#top)
- [Ping On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-probes.htm#top)
- [Creating a Ping On-Demand Probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-probe.htm#top)
- [Listing Results for a Ping On-Demand Probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-probe-result.htm#top)
- [Listing Vantage Points](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#top)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

Administrators: For common policies that give groups access to Health Checks resources, see[IAM Policies (on the Securing Health Checks page)](https://docs.oracle.com/iaas/Content/Security/Reference/healthchecks_security.htm#iam-policies).

## Available Protocols

Following are the protocols available to use with monitors and on-demand probes.
Note  
  
Configure the monitored endpoint to accept the specified protocol.
- HTTP - Configure a GET or HEAD request using HTTP/1.1 to test the target for availability. Results (JSON) include the HTTP Status Code and DNS lookup, connection, and response timings. See[HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-monitors.htm#top)and[HTTP On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-probes.htm#top).
- HTTPS - Configure an encrypted HTTPS GET or HEAD request to test the availability of any secure hosted target. Default port: 443. Results (JSON) include the HTTP Status Code and DNS lookup, connection, and response timings. See[HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-monitors.htm#top)and[HTTP On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/http-probes.htm#top).
- ICMP - Configure an ICMP echo request ping. Results include the round-trip time (RTT) latency. See[Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-monitors.htm#top)and[Ping On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-probes.htm#top).
- TCP - Configure a TCP handshake to the specified endpoint. Results include the round-trip time (RTT) latency. See[Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-monitors.htm#top)and[Ping On-Demand Probes](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/ping-probes.htm#top).
Note
