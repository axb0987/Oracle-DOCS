# Streaming Metrics Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Reference/metric-ref.htm
- Fetched: 2026-09-05 03:05 CDT

# Streaming Metrics Reference

Review details about the metrics emitted for the metric namespace`oci_streaming`(the Streaming service).

## Available Metrics

The following tables describe the available Streaming metrics.

You also can use the Monitoring service to create[custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).

### Dimensions

Each metric includes the following dimensions : REGION The REGION where the stream resides. RESOURCEID The OCID of the stream.

### Descriptions: Producers

Metric Metric Display Name Unit Description Dimensions
`PutMessagesLatency.Time`Put Messages Latency time (ms) Time taken for put messages operation measured over time range. region,resourceId
`PutMessagesThroughput.Bytes`Put Messages Total Throughput Bytes Bytes pushed to the stream measured over time.
`PutMessagesThroughput.Count`Put Messages Records/sec count Count of messages pushed to stream measured over time.
`PutMessagesThrottling.Count`Put Messages Throttled Records/sec count Number of put messages throttled either due to volume or requests measured over time.
`PutMessagesSuccess.Count`Put Messages Success/sec count Successful requests for put messages per stream measured over time.
`PutMessagesFault.Count`Put Messages Failure/sec count Total failed putMessage requests per stream measured over time.
`PutMessagesRecords.Count`Put Messages Requests/sec count Number of mesages published to a stream measured over time.

### Descriptions: Consumers

Metric Metric Display Name Unit Description Dimensions
`GetMessagesLatency.Time`Get Messages Latency time (s) Time taken for get messages operation measured over time range. region,resourceId
`GetMessagesThroughput.Bytes`Get Messages Total Throughput Bytes Bytes retrieved from stream measured over time.
`GetMessagesThroughput.Count`Get Messages Requests/sec count Count of messages read from stream measured over time.
`GetMessagesThrottling.Count`Get Messages Throttled Requests/sec count Number of get messages throttled either due to volume or requests measured over time.
`GetMessagesSuccess.Count`Get Messages Success/sec count Successful requests for get messages per stream measured over time.
`GetMessagesFault.Count`
