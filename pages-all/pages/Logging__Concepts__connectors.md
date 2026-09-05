# Connectors
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/connectors.htm
- Fetched: 2026-09-05 02:36 CDT

# Connectors

Create a connector in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/connectors.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/connectors.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/connectors.htm#)
- 

Note  
  

When your configuration requires policies, default policies are offered. To accept a default policy, select the provided Create policy link.

[Default policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti__default-policies)are offered for any authorization required for this connector to access source, task, and target services.

You can get this authorization through these default policies or through group-based policies. The default policies are offered whenever you use the Console to create or edit a connector. The only exception is when the exact policy already exists in IAM, in which case the default policy isn't offered. For more information about this authorization requirement, see[Authentication and Authorization](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti).
- If you don't have permissions to accept default policies, contact your administrator.
- Automatically created policies remain when connectors are deleted. As a best practice, delete associated policies when deleting the connector.

To review a newly created policy, select the associated view link.

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Connectors .
- On the Connectors page, select a compartment.
- Select Create Connector .
The Create connector page opens.

## 1. Basic Connector Information

Enter identifying information and optional logs and tags.
- Connector name : Enter a user-friendly name for the new connector and an optional description. Avoid entering confidential information.
- Select a compartment : Select the compartment to store the new connector in.
- Description (Optional): Enter a description for the connector.
- Enable logs (Optional): Select to enable service logs for the new connector, and provide the following information.
- Category (default value: Run Log )
- Compartment : Select the compartment that you want for storing the service logs for the connector.
- Log group : Select the log group (by compartment) that you want for storing the service logs. To create a new log group, select Create new group and then enter a name.
- Log name (Optional): Enter a name for the log.
- Show advanced options :
- Enable legacy archival logs (Optional): Legacy log archival automatically creates a bucket in your compartment and archives a copy of the log.
- Log retention (Optional): Specify how long to keep the service logs (default: 30 days).
- Tags (Optional): To add tags to the connector, select the option that you see.
- Tags
- Add Tags (under Show Advanced Options )

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Next .

## 2. Configure Connector Source

Specify the source service for the connector to transfer data from.
- Select source : Select the service that contains the data that you want to transfer.

- Logging : Transfer log data from the Logging service. See[Logging](https://docs.oracle.com/iaas/Content/Logging/home.htm).
- Monitoring : Transfer metric data points from the Monitoring service. See[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm).
- Queue : Transfer messages from a queue in the service. See[Queue](https://docs.oracle.com/iaas/Content/queue/home.htm).
- Streaming : Transfer stream data from the Streaming service. See[Streaming](https://docs.oracle.com/iaas/Content/Streaming/home.htm).
- Configure source : Enter values for the selected source.[Logging

Note  
  
To enter this information using the query code editor, or to view entered information as query code, select Switch to Advanced Mode .
- Compartment name : The compartment that contains the log that you want.
- Log group : The log group that contains the log that you want.

For log input schema, see[LogEntry](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/LogEntry).
- Logs : The log that you want.
- Log filter task (Optional): Filter the logs that appear in the Logs field.

To specify attribute values for[audit logs ( _Audit ) :
- Filter type : Select Attribute .
- Attribute name : Select the audit log attribute that you want.
- Attribute values : Specify values for the selected audit log attribute.

To specify events for[audit logs ( _Audit ) :
- Filter type : Select Event type .
- Service name : Select the service that contains the event that you want.
- Event type : Select the event that you want.

To specify property values for[service logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm)or[custom logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs.htm)( not _Audit ):
- Property : Select the property that you want.
- Operator : Select the operator to use for filtering property values.
- Value : Specify the property value that you want.

To review supported queries for filtering source logs, see[Log Query Reference for Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/queryreference.htm).[Monitoring

- Metric compartment : Select the compartment that contains the[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricdefinitiondefinition2)that you want.
- Namespaces : Select one or more[metric namespaces](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricnamespacedefinition2)that include the[metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricdefinitiondefinition2)that you want. All metrics in the selected namespaces are retrieved.

The namespaces must begin with "`oci_`". Example:`oci_computeagent`.
- To add metric namespaces from another compartment, select + Another compartment .

The maximum number of metric compartments per Monitoring source is 5. The maximum number of namespaces per Monitoring source (across all metric compartments) is 50. Following are example sets of compartments in a single source that remain within this maximum:
- 5 metric compartments with 10 namespaces each
- 3 metric compartments with varying numbers of namespaces (20, 20, 10)
- 1 metric compartment with 50 namespaces[Queue

- Compartment : Select the compartment that contains the queue that you want.
- Queue : Select the queue that contains the messages that you want.
Note  
  
To select a queue for a connector, you must have authorization to read the queue. See[IAM Policies (Securing Connector Hub)](https://docs.oracle.com/iaas/Content/Security/Reference/sch_security.htm#iam-policies).
- 

Channel Filter (under Message filtering ) (optional): To filter messages from channels in the queue, enter a value.

For example, to filter messages by channel ID, enter the channel ID.

For supported values, see`channelFilter`at[GetMessages](https://docs.oracle.com/iaas/api/#/en/queue/latest/GetMessage/GetMessages)(Queue API).
Note  
  
A message that has been transferred to the connector's target is considered "consumed." To meet requirements of the Queue service, the connector deletes transferred messages from the source queue. For more information, see[Consuming Messages](https://docs.oracle.com/iaas/Content/queue/consume-messages.htm).[Streaming

Note  
  
[Private endpoint configuration](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamsecurity.htm#private_endpoints)is supported. To use a private endpoint, see[Private Endpoint Prerequisites for Streams](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-streaming-source.htm#stream-private).
- Compartment : Select the compartment that contains the stream that you want.
- Stream pool : Select the[stream pool](https://docs.oracle.com/iaas/Content/Streaming/Tasks/creating-stream-pools.htm)that contains the stream that you want.
Note  
  
To select a stream pool and stream for a connector, you must have authorization to read the stream pool and stream. See[IAM Policies (Securing Connector Hub)](https://docs.oracle.com/iaas/Content/Security/Reference/sch_security.htm#iam-policies).
- Stream : Select the name of the[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts)that you want to receive data from.
- Read position : Specify the cursor position from which to start reading the stream.
- Latest : Starts reading messages published after creating the connector.
- If the first run of a new connector with this configuration is successful, then it moves data from the connector's creation time. If the first run fails (such as with missing policies), then after resolution the connector either moves data from the connector's creation time or, if the creation time is outside the retention period, the oldest available data in the stream. For example, consider a connector created at 10 a.m. for a stream with a two-hour retention period. If failed runs are resolved at 11 a.m., then the connector moves data from 10 a.m. If failed runs are resolved at 1 p.m., then the connector moves the oldest available data in the stream.
- Later runs move data from the next position in the stream. If a later run fails, then after resolution the connector moves data from the next position in the stream or the oldest available data in the stream, depending on the stream's retention period.
- Trim Horizon : Starts reading from the oldest available message in the stream.
- If the first run of a new connector with this configuration is successful, then it moves data from the oldest available data in the stream. If the first run fails (such as with missing policies), then after resolution the connector moves the oldest available data in the stream, regardless of the stream's retention period.
- Later runs move data from the next position in the stream. If a later run fails, then after resolution the connector moves data from the next position in the stream or the oldest available data in the stream, depending on the stream's retention period.

Select Next .

## 3. Configure Connector Task

Optionally configure a function task to process data from the source using the[Functions service](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm).

- Compartment : Select the compartment that contains the function that you want.
- Function application : Select the name of the[function application](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#applications)that includes the function you want.
- Function : Select the name of the[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#functions)that you want to use to process the data received from the source.

For use by the connector as a task, the function must be configured to return one of the following responses:
- List of JSON entries (must set the response header`Content-Type=application/json`)
- Single JSON entry (must set the response header`Content-Type=application/json`)
- Single binary object (must set the response header`Content-Type=application/octet-stream`)
- Show additional options (Optional)
- Batch options (Optional): Specify limits for each batch of data sent to the function.
- Use automatic settings
- Use manual settings : Provide values for batch size limit (KBs) and batch time limit (seconds).

Considerations for function tasks:
- Connector Hub doesn't parse the output of the function task. The output of the function task is written as-is to the target. For example, when using a Notifications target with a function task, all messages are sent as raw JSON blobs.
- Functions are invoked synchronously with 6 MB of data per invocation. If data exceeds 6 MB, then the connector invokes the function again to move the data that's over the limit. Such invocations are handled sequentially.
- Functions can execute for up to five minutes. See[Delivery Details](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#delivery).
- Function tasks are limited to scalar functions.

Select Next .

## 4. Configure Connector Target

Specify the target service to send the data to.
- Target : Select the service that you want to transfer the data to.
- Functions : Send data to a[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#functions).
- Logging Analytics : Send data to a[log group](https://docs.oracle.com/iaas/log-analytics/doc/logging-analytics1.html#GUID-9B74BCD1-48BE-4A80-97E5-1C6CE9AA5EC2__GUID-19370356-C115-4904-95CF-3430A9510F49).
- Monitoring : Send[metric](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricdefinitiondefinition2)data points to the Monitoring service.
- Notifications : Send data to a[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts).
- Object Storage : Send data to a[bucket](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm#resources).
- Streaming : Send data to a[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts).
- Configure target : Enter values for the selected target. Functions

- Compartment : Select the compartment that contains the function that you want.
- Function application : Select the name of the[function application](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#applications)that contains the function that you want.
- Function : Select the name of the[function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsconcepts.htm#functions)that you want to send the data to.
- Show additional options (Optional): Select this link and specify limits for each batch of data sent to the function. To use manual settings, provide values for batch size limit (either KBs or number of messages) and batch time limit (seconds).

For example, limit batch size by selecting either 5,000 kilobytes or 10 messages. An example batch time limit is 5 seconds.

Considerations for Functions targets:
- The connector flushes source data as a JSON list in batches. Maximum batch, or payload, size is 6 MB.
- Functions are invoked synchronously with 6 MB of data per invocation. If data exceeds 6 MB, then the connector invokes the function again to move the data that's over the limit. Such invocations are handled sequentially.
- Functions can execute for up to five minutes. See[Delivery Details](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#delivery).
- Don't return data from Functions targets to connectors. Connector Hub doesn't read data returned from Functions targets. Logging Analytics

- Compartment : Select the compartment that contains the log group that you want.
- Log group : Select the[log group](https://docs.oracle.com/iaas/log-analytics/doc/logging-analytics1.html#GUID-9B74BCD1-48BE-4A80-97E5-1C6CE9AA5EC2__GUID-19370356-C115-4904-95CF-3430A9510F49)that you want.
- Log source identifier (for Streaming source only): Select the[log source](https://docs.oracle.com/iaas/log-analytics/doc/logging-analytics1.html#LOGAN-GUID-9B74BCD1-48BE-4A80-97E5-1C6CE9AA5EC2). Monitoring

- Compartment : Select the compartment that contains the metric that you want.
- Metric namespace : Select the[metric namespaces](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricnamespacedefinition2)that includes the metric that you want. You can select an existing namespace or enter a new namespace.

When typing a new namespace, press Enter to submit it.

For a new metric namespace, don't use the reserved`oci_`prefix. Metrics aren't ingested when reserved prefixes are used. See[Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)and[PostMetricData Reference (API)](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData).
- Metric : Select the name of the[metric](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__metricdefinitiondefinition2)that you want to send the data to. You can select an existing metric or enter a new metric.

When typing a new metric name, press Enter to submit it.

For a new metric, don't use the reserved`oci_`prefix. Metrics aren't ingested when reserved prefixes are used. See[Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)and[PostMetricData Reference (API)](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData).
- 

Add dimensions (Optional): Select to configure dimensions. The Add dimensions panel opens.

The six latest rows of log data are retrieved from the log specified under Configure source .

Specify a name-value key pair for each dimension that you want to send data to. The name can be custom and the value can be either static or a path to evaluate.[Use dimensions to filter the data after the log data is moved to a metric.](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm)For an example dimension use case, see[Scenario: Creating Dimensions for a Monitoring Target](https://docs.oracle.com/iaas/Content/connector-hub/dimensionlogs.htm).

To tag data (static value)
- Static path : Manually enter a custom name ( Dimension Name ) and path ( Dimension path ). For example, enter`traffic`and`customer`.

Note  
  
For new (custom) metrics, the specified metric namespace and metric are created the first time that the connector moves data from the source to the Monitoring service. To check for the existence of moved data, query the new metric by using the Console, CLI, or API. See[Creating a Query for a Custom Metric](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-custom.htm).

What's included with the metric
In addition to any dimension name-value key pairs that you specify under Configure dimensions , the following dimensions are included with the metric:
- `connectorId`: The OCID of the connector that the metrics apply to.
- `connectorName`: The name of the connector that the metrics apply to.
- `connectorSourceType`: The source service that the metrics apply to.

The timestamp of each metric data point is the timestamp of the corresponding log message. Notifications

- Compartment : Select the compartment that contains the topic that you want.
- Topic : Select the name of the[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts)that you want to send the data to.
- Message format : Select the option that you want:
Note  
  
Message format options are available for connectors with Logging source only. These options aren't available for connectors with function tasks. When Message format options aren't available, messages are sent as raw JSON blobs.

- Send formatted messages : Simplified, user-friendly layout.

To view supported subscription protocols and message types for formatted messages, see[Friendly Formatting](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__friendly-formatting).
- Send raw messages : Raw JSON blob.

Considerations for Notifications targets:
- The maximum message size for the Notifications target is 128 KB. Any message that exceeds the maximum size is dropped.
- SMS messages exhibit unexpected results for certain connector configurations. This issue is limited to topics that contain[SMS subscriptions](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts)for the indicated connector configurations. For more information, see[Multiple SMS messages for a single notification](https://docs.oracle.com/iaas/Content/connector-hub/known-issues.htm#multiple-sms). Object Storage

- Compartment : Select the compartment that contains the bucket that you want.
- Bucket : Select the name of the[bucket](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm#resources)that you want to send the data to.
- Object name prefix : Optionally enter a prefix value.
- Show batch options : Select this link and optionally enter values for batch size (in MBs) and batch time (in milliseconds). Fields are labeled Batch size and Batch time .

Considerations for Object Storage targets:
- 

Batch rollover details:
- Batch rollover size: 100 MB
- Batch rollover time: 7 minutes
- 

Files saved to Object Storage are compressed using gzip.
- 

Format of data moved from a Monitoring source: Objects. The connector partitions source data from Monitoring by metric namespace and writes the data for each group (namespace) to an object. Each object name includes the following elements.

`<object_name_prefix> / <service_connector_ocid> / <metric_compartment_ocid> / <metric_namespace> / <data_start_timestamp> _ <data_end_timestamp> . <sequence_number> . <file_type> .gz`

Within an object, each set of data points is appended to a new line. Streaming

Note  
  
To select a stream pool and stream for a connector, you must have authorization to read the stream pool and stream. See[IAM Policies (Securing Connector Hub)](https://docs.oracle.com/iaas/Content/Security/Reference/sch_security.htm#iam-policies).[Private endpoint configuration](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamsecurity.htm#private_endpoints)is supported. To use a private endpoint, see[Private Endpoint Prerequisites for Streams](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-streaming-source.htm#stream-private).
- Compartment : Select the compartment that contains the stream that you want.
- Stream : Select the name of the[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts)that you want to send the data to.

Considerations for Streaming targets:
- Format of data moved from a Monitoring source: Each object is written as a separate message.

Select Next .

## Connector Preview

Review the connector configuration and then select Create .

The creation process begins, and its progress is displayed. On completion, the connector's details page opens.
- 

Use the[oci sch service-connector create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/sch/service-connector/create.html)command and required parameters to create a connector:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateServiceConnector](https://docs.oracle.com/iaas/api/#/en/serviceconnectors/latest/ServiceConnector/CreateServiceConnector)
