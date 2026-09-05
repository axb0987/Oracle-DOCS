# Publishing Custom Metrics Using the API
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm
- Fetched: 2026-09-05 02:39 CDT

# Publishing Custom Metrics Using the API

Publish custom metrics to the Monitoring service.
Tip  
  
[Agent configurations](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/agent-configurations.htm)are another way to publish custom metrics to Monitoring. With agent configurations, the API isn't necessarily required to publish custom metrics. You can now use agent configurations to ingest metric data into custom metrics. For example, expose metrics from a virtual machine (VM) using an HTTP endpoint in Prometheus format.

A custom metric is a metric that you design to collect and analyze data.

For example, create a`productOrder`metric (in a metric namespace,`mymetricsnamespace`) to track product orders by country and division, with additional metadata for product categories and notes.

## Before You Begin

IAM policies: To publish custom metrics, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[Publish Custom Metrics (Securing Monitoring)](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups-publish).

## Considerations

When defining custom metrics, note the following:
- For the metric namespace, don't use a reserved prefix (`oci_`or`oracle_`).
- Ensure that custom metrics don't exceed limits. For example, note the valid range of dimensions and maximum number of streams for custom metrics. See[PostMetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData).
- Define metrics with aggregation in mind. While custom metrics can be posted as frequently as every second (minimum frequency of one second), the minimum aggregation interval is one minute.
- Define metrics with return limits in mind. Limits information for returned data includes the 100,000 data point maximum and[time range maximums (determined by resolution, which relates to interval)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval). See[MetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData). See also[Limits on Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#limits).
- Ensure that timestamp values are near current time. For a data point to be posted, its timestamp must be near current time (less than two hours in the past and less than 10 minutes in the future). See[PostMetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData).
- After publishing custom metrics, you can access them the same way you access any other metrics stored by the Monitoring service:[View charts in the Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm),[query metrics using the CLI or API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm), and[create alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm.htm).
- When retrieving custom metrics, you can[match to a resource group](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-resource-group.htm). Blank (null) for resource group returns metric data that doesn't have a resource group.

## Metric-Posting Clients

For information about developing a metric-posting client, see[Developer Guide](https://docs.oracle.com/iaas/Content/API/Concepts/devtoolslanding.htm). For an example client, see[MonitoringMetricPostExample.java](https://github.com/oracle/oci-java-sdk/blob/master/bmc-examples/src/main/java/MonitoringMetricPostExample.java).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)
- 

This task can't be performed in the Console.
- 

Note  
  
Unlike other Monitoring commands that use`telemetry`endpoints, this command requires a`telemetry-ingestion`endpoint.

Use the[oci monitoring metric-data post](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/post.html)command, the`--endpoint`parameter, and required parameters to publish custom metrics:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).

[Example JSON file for request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)

The example JSON file includes the following items.
- Metric namespace:`mymetricsnamespace`
- Metric name:`productOrder`
- Product dimension
- Country dimension
- Resource group (`DivisionX`,`DivisionY`)
- Additional metadata for category and note
```

```

[Example response](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)

```

```

- 

Note  
  
Unlike other Monitoring operations that use`telemetry`endpoints, this operation requires a`telemetry-ingestion`endpoint.

Run the[PostMetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData)operation to publish custom metrics.

[Example of a batched request](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm#)

This example shows a single request containing data points for metrics across two metric namespaces .
```

```

## More Information

To walk through common use cases with custom metrics, see[Custom Metrics Walkthrough](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/custom-metrics-walkthrough.htm). For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm)
