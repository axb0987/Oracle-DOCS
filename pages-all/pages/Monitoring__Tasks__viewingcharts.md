# Viewing Default Metric Charts
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/viewingcharts.htm
- Fetched: 2026-09-05 02:40 CDT

# Viewing Default Metric Charts

View metric charts that use predefined service queries. Default metric charts are available on the Service Metrics page and resource details pages in the Console.

For background information on metrics in Oracle Cloud Infrastructure, see[Metrics Feature Overview](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#metrics). For default metrics by service, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#SupportedServices)and[Listing Metric Definitions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm).

The following pages describe tasks you can perform with default metric charts:
- [Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-namespace.htm)
- [Viewing Default Metric Charts for a Single Resource](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-resource.htm)
- [Switching Table and Chart Views for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-toggle-view.htm)
- [Viewing the Query for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-query.htm)
- [Copying the Query from a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-query-copy.htm)
- [Listing Resources in a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-list-resources.htm)
- [Sharing a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-share.htm)
- [Viewing and Updating the Query for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-explore.htm)
- [Changing the Time Range for Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-time-range.htm)
- [Changing the Interval for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-interval.htm)
- [Changing the Statistic for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-statistic.htm)
- [Aggregating Metric Streams in a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-aggregate-metric-streams.htm)
- [Selecting Dimensions to Filter Metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-dimensions.htm)
- [Creating an Alarm from a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-create-alarm.htm)
- [Resetting Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/view-chart-reset.htm)

## Before You Begin

Following are prerequisites for viewing metric charts:
- IAM policies: Viewing metric charts is part of monitoring. To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). Administrators: For common policies that give groups access to metrics, see[Metric Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups).
- Metrics exist in Monitoring: The resources that you want to monitor must emit metrics to the Monitoring service.
- Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).

## Example Metric Chart

The following image shows several metric streams in the graph view of a metric chart. Each metric stream corresponds to a compute instance.

The 85% value at 1:30 indicates that a compute instance used 85% of its CPU (averaged over the specified interval). Absent values are indicated for a metric stream toward the bottom of the graph, indicating that a compute instance didn't emit metric data until 1:30.
[

Very small or large values are indicated by International System of Units (SI units), such as M for mega (10 to the sixth power). Units correspond to the selected metric and don't change by statistic .

For more information about this example, see[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)
