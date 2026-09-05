# Edge Policy Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Reference/metricsalarms.htm
- Fetched: 2026-09-05 03:11 CDT

# Edge Policy Metrics

You can monitor the health, capacity, and performance of your edge policies by using[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm),[alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm), and[notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).

This topic describes the metrics emitted by the metric namespace`oci_waf`(the WAF service).

## Overview of the WAF Service Metrics

Oracle Cloud Infrastructure Web Application Firewall (WAF) is a cloud-based global security service that protects applications from malicious and unwanted internet traffic. The WAF service metrics help you measure various levels of traffic encountering your WAF policies, including non-malicious traffic. For more information, see[Overview of the Web Application Firewall Service](https://docs.oracle.com/en-us/iaas/Content/WAF/Reference/../Concepts/overview.htm#Overview_of_the_Web_Application_Firewall_Service).

## Prerequisites

- IAM policies: To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
- 

Permissions are required to allow monitoring, alarm, and notification (ONS) definition for users in a group for all compartments. The following policies must be configured in the root compartment:
```

```

```

```

```

```

## Available Metrics: oci_waf

The metrics listed in the following table are automatically available for any policies you create. You do not need to enable monitoring on the resource to get these metrics. However, you must have the policy properly set up with web traffic passing through it to make the`oci_waf`metric space available in the Metrics Explorer feature. Policies with no web traffic emit no metric data.

Metric Metric Display Name Unit Description Dimensions
`NumberOfRequests`Requests count The total number of requests serviced by the WAF.

`resourceID`

`primaryDomain`

`module`

`action`

`countryCode`

`responseCode`

`responseCodeGroup`
`Traffic`Traffic bytes Data egress from the WAF (compressed by default) measured in one minute intervals.
`Bandwidth`Bandwidth B/s (bytes per second)

Bandwidth rate calculated by dividing total data egress in a minute by 60.
`NumberOfRequestsDetected`Detects count The number of requests that triggered a detect (alert) for a WAF policy.`resourceID`

`primaryDomain`

`module`

## Available Dimensions

The following dimensions are available for WAF metrics:

Dimension Description Sample Values
`Action`
- blocked
- passed
- redirected
`Country`Two-letter country code where the request originated.
- US
- BZ
- CN
`Module`The rule type that was triggered by the request.
- access_rules
- captcha
- threat (threat intelligence)
- modsecurity (protection rule)
- origin
- fp_challenge (device fingerprint)
`PrimaryDomain`Web domain of the WAF policy. www.mydomain.com
`ResponseCode`HTTP response.
- 200
- 403
- 404
`ResponseCodeGroup`HTTP response status code series.
- 2XX
- 4XX
- 5XX
`ResourceId`The OCID of the WAF policy.`ocid1.waaspolicy.oc1..aaaaaaaayan6dy54hpfxqc45tofjjr6sgzd36atchdlxubpqma5bkejkjv7r`

Multiple dimensions can be combined and aggregated to form ad-hoc subset reports of telemetry.

## Viewing Metrics

Describes the different methods to view metrics for an edge policy.

Use one of the following methods to view logs for an edge policy.

### Using the Console

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the WAF policies displayed:

- 

Name
- 

Policy Type
- 

Status
- Select the edge policy whose logs you want to view.
The Edge Policy Details dialog box appears.
- Select Metrics under Resources .

The Metrics list appears. The list consists of panels displaying metric information on areas such as blocked requests, detected requests, traffic, and response code groups.

For each panel, you can select commands from the Options list, such as viewing the query in the Metric Explorer, copying the chart URL, copying the query, and viewing the metric information in table view. You can also specify the Interval and Statistic for each chart.

See[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)for more information on monitoring and the Metric Explorer. Use the oci_waf namespace when prompted to provide a monitoring namespace.
- Specify the date-time group range covered by the metrics by completing the following:

- Start time
- End time

Alternatively, select one of the time spans from the Quick Selects list. The time spans available range from the previous hour to 90 days in the future from that moment.
The metrics for the edge policy are displayed according to your specifications.

## Metrics When Migrating Edge Policies
