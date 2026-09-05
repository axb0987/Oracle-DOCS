# Troubleshooting Health Checks
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/troubleshooting.htm
- Fetched: 2026-09-05 02:14 CDT

# Troubleshooting Health Checks

Use troubleshooting information to identify and address common issues that can occur while working with Health Checks.

See also[Known Issues for Health Checks](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/known-issues.htm#top).

## Health Checks Continually Fail

Troubleshoot health checks that are continually returning non-healthy results.

Health checks continually return`"isHealthy": false`when you list results ([HTTP monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor-result.htm#top),[ping monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor-result.htm#top),[HTTP on-demand probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-probe-result.htm#top),[ping on-demand probe](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-probe-result.htm#top)).

### Cause: Insufficient Permissions

You might not have permissions to monitor the host.

### Remedy: Ensure Sufficient Permissions

Ensure that you have permissions to monitor the host.

### Cause: Incorrect Port Configuration on Host

The host ports might not be configured to receive traffic from Health Checks.

### Remedy: Configure Host Ports
