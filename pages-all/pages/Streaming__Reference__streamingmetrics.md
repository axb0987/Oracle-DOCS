# Streaming Metrics
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/streamingmetrics.htm
- Fetched: 2026-09-05 03:05 CDT

# Streaming Metrics

View metric charts, create queries, and review details about Streaming service metrics.

You can monitor the health and performance of your streams by using[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics)and[alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms). For more information, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm).

## Tasks

The following pages describe tasks you can perform with Streaming service metrics:
- [Viewing Default Metric Charts for All Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/view-chart-namespace.htm)
- [Viewing Default Metric Charts for a Stream](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/view-chart-resource.htm)
- [Creating a Query for Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/query-metric.htm)

For details about the Streaming service metrics, see[Streaming Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/metric-ref.htm).

## Overview

The Streaming service provides metrics showing how the service is performing. These metrics are automatically available.

You can use these metrics to:
- Understand the produce/consume latency for a real-time application.
- Calculate and validate the price of service usage.
- Monitor changes in throughput over time.
- Check the time that the last message was consumed.

For steps to view default metric charts in the Console, see[Viewing Default Metric Charts for Streams](https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/../Tasks/view-chart.htm).

## Stream Health

A healthy stream is a stream that is active: messages are received and consumed successfully.

Writes to the service are durable. If you can produce to your stream, and if you get a successful response, then the stream is healthy.

After data is ingested, it is accessible to consumers for the configured retention period. If GetMessages API calls return elevated levels of internal server errors, the service isn't healthy.

A healthy stream also has healthy metrics:
- Put Messages Latency is low.
- Put Messages Total Throughput is close to 1 MB per second per partition.
- Put Messages Throttled Records is close to 0.
- Put Messages Failure is close to 0.
- Get Messages Latency is low.
- Get Messages Total Throughput is close to 2 MB per second per partition.
- Get Messages Throttled Requests is close to 0.
- Get Messages Failure is close to 0.

## Suggested Alarms

### Producers

For producers, consider setting alarms on the following metrics:
- Put Messages Latency: An increase in latency means that the messages are taking longer to publish, which could indicate network issues.
- Put Messages Total Throughput:

- An increase in total throughput could indicate that the 1 MB per second per partition limit will be reached, and that event will trigger the throttling mechanism.
- A decrease could mean that the client producer is having an issue or is about to stop.
- Put Messages Throttled Records: It's important to get notified when messages are throttled.
- Put Messages Failure: It's important to get notified if put messages start failing.

### Consumers

For consumers, consider setting similar alarms based on the following metrics:
- Get Messages Latency
- Get Messages Total Throughput
- Get Messages Throttled Requests
- Get Messages Failure

For steps to create alarms, see[Creating an Alarm from a Default Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-create-alarm.htm)and[Creating an Alarm from a Custom Metric Chart](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-create-alarm.htm)
