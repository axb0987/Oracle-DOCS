# Resource Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcemonitoring.htm
- Fetched: 2026-09-05 02:10 CDT

# Resource Monitoring

You can monitor the health, capacity, and performance of your Oracle Cloud Infrastructure resources when needed using queries or on a passive basis using alarms. Queries and alarms rely on metrics emitted by your resource to the Monitoring service.

## Prerequisites

- IAM policies: To monitor resources, you must have the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you have and which compartment you should work in. For more information about user authorizations for monitoring, see[IAM Policies (Monitoring)](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
- Metrics exist in Monitoring: The resources that you want to monitor must emit metrics to the Monitoring service.
- Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).

## Working with Resource Monitoring

Not all resources support monitoring. See[Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices)for the list of resources that support the Monitoring service, which is required for queries and alarms used in monitoring.

The following pages describe basic resource monitoring tasks:
- [Viewing Default Metric Charts for a Single Resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/view-chart-resource.htm)
- [Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/view-chart-namespace.htm)
- [Creating a Query](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/query-metric.htm)
- [Creating an Alarm from a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Tasks/view-chart-create-alarm.htm)
