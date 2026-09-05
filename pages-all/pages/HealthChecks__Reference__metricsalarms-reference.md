# Health Checks Metrics Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/metricsalarms-reference.htm
- Fetched: 2026-09-05 02:13 CDT

# Health Checks Metrics Reference

Review details about the metrics emitted for the metric namespace`oci_healthchecks`(the Health Checks service).

## Available Metrics: oci_healthchecks

### Dimensions

Each metric includes a subset of the following dimensions:`errorMessage`The error messages encountered by the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top).`icmpCode`The ICMP code returned from the indicated ping[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top).`protocol`The[protocol](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#protocols)of the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top). See the`protocol`attribute of the related API object:[HttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor),[HttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe),[PingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor), or[PingProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingProbe).`resourceDisplayName`The display name of the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top). See the`displayName`attribute of the related API object:[HttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor),[HttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe),[PingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor), or[PingProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingProbe).`resourceId`The OCID of the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top). See the`id`attribute of the related API object:[HttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor),[HttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe),[PingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor), or[PingProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingProbe).`target`The endpoint for the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top). See the`targets`attribute of the related API object:[HttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor),[HttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe),[PingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor), or[PingProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingProbe).`vantagePoint`The name of the[vantage point](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/list-vantage-point.htm#top)for launching the indicated[health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Reference/../Tasks/managinghealthchecks.htm#top). See the`vantagePointNames`attribute of the related API object:[HttpMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpMonitor),[HttpProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HttpProbe),[PingMonitor](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingMonitor), or[PingProbe](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/PingProbe).

### Descriptions

The table lists metrics in alphabetical order.

Metric Metric Display Name Unit Description Dimensions
`BasicCount`Basic Count count The number of basic health checks.`resourceId`
`HTTP.DNSLookupTime`HTTP(S) DNS Lookup Time ms

The time taken for HTTP or HTTPS domain name lookup in milliseconds.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.isHealthy`HTTP(S) Test Success Rate percent The percentage of healthy, or successful, HTTP or HTTPS tests that were run during the selected interval. Each test returns either`0`(unhealthy or failed) or`1`(healthy or successful).

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.RequestTime`HTTP(S) Request Duration ms The total duration of the HTTP or HTTPS request in milliseconds.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.ResponseTime`HTTP(S) Response Duration ms The total duration of the HTTP or HTTPS response in milliseconds.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.StatusCode`HTTP(S) Response Status Code count The HTTP or HTTPS response code.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.TCPConnectTime.Full`HTTP(S) Connection Duration ms The total TCP connection duration for the HTTP or HTTPS test.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.TCPConnectTime.SSL`HTTPS Secure Connection Duration count The total duration in milliseconds from start of secure connection to end of the HTTPS connection.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`HTTP.TotalDuration`HTTP(S) Total Duration ms The total duration of the HTTP or HTTPS test run in milliseconds.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`PING.isHealthy`Ping Test Success Rate percent The percentage of healthy, or successful, ping tests that were run during the selected interval. Each test returns either`0`(unhealthy or failed) or`1`(healthy or successful).

`errorMessage`

`icmpCode`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`PING.Latency`Ping Latency Measurement ms Latency measurement for ping test in milliseconds.

`errorMessage`

`protocol`

`resourceDisplayName`

`resourceId`

`target`

`vantagePoint`
`PremiumCount`Premium Count count The number of premium health checks.`resourceId`
