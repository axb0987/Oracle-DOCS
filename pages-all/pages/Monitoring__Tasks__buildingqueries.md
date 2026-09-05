# Building Metric Queries
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/buildingqueries.htm
- Fetched: 2026-09-05 02:38 CDT

# Building Metric Queries

View custom metric charts, list metric definitions, and query metric data for resources of interest.

For background information on metrics in Oracle Cloud Infrastructure, see[Metrics Feature Overview](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#metrics). For default metrics by service, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#SupportedServices)and[Listing Metric Definitions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm).

The following pages describe tasks you can perform with metric charts, metric definitions, and queries of metric data.
- [Viewing a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-view-chart.htm)
- [Creating a Basic Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-basic-query.htm)
- [Changing the Time Range for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-time-range.htm)
- [Switching Table and Graph Views for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-toggle-view.htm)
- [Customizing Y-Axis Labels in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-customize-y-axis.htm)
- [Viewing Queries for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-view-queries.htm)
- [Adding and Deleting Queries in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-add-delete-query.htm)
- [Editing a Query in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-edit-query.htm)
- [Hiding and Showing Queries in a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-hide-show-query.htm)
- [Creating an Alarm from a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-create-alarm.htm)
- [Listing Metric Definitions](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/list-metric.htm)
- [Querying Metric Data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-landing.htm)
- [Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric.htm)
- [Creating a Query for a Custom Metric](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-custom.htm)
- [Editing the MQL Expression for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-mql.htm)
- [Selecting the Metric Namespace for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-namespace.htm)
- [Selecting the Metric Name for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-metric.htm)
- [Selecting a Resource Group in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resource-group.htm)
- [Selecting the Interval for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-interval.htm)
- [Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-statistic.htm)
- [Selecting a Nondefault Time Range for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-time-range.htm)
- [Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-dimension.htm)
- [Selecting a Resource for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resource.htm)
- [Using filter(x) in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-filter.htm)
- [Using groupBy(x) in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-groupby.htm)
- [Aggregating Metric Streams in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-grouping.htm)
- [Specifying a Predicate in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-predicate.htm)
- [Selecting a Nondefault Resolution for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-resolution.htm)
- [Nesting Queries in an MQL Expression](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/query-metric-nested.htm)
- [Creating an Alarm from a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Tasks/metrics-explorer-create-alarm.htm)

## Before You Begin

- IAM policies: Querying metrics is part of monitoring. To monitor resources, you must be granted the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which compartment you need to work in. For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). Administrators: For common policies that give groups access to metrics, see[Metric Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups).
- Metrics exist in Monitoring: The resources that you want to monitor must emit metrics to the Monitoring service.
- Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm)
