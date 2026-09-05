# Overview of Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm
- Fetched: 2026-09-05 02:38 CDT

# Overview of Monitoring

Use the Oracle Cloud Infrastructure Monitoring service to actively and passively monitor cloud resources using the Metrics and Alarms features. Learn how Monitoring works.

[
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31981)to the service.

## How Monitoring Works

The Monitoring service uses metrics to monitor resources and alarms to notify you when these metrics meet alarm-specified triggers.

Metrics are emitted to the Monitoring service as raw data points , or timestamp-value pairs, along with dimensions and metadata. Metrics come from various sources:
- Resource metrics automatically posted by Oracle Cloud Infrastructure resources . For example, the Compute service posts metrics for monitoring-enabled compute instances through[the oci_computeagent namespace](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#Availabl). One such metric is`CpuUtilization`. See[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices)and[Viewing Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/viewingcharts.htm).
- [Custom metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/publishingcustommetrics.htm)published using the Monitoring API.
- Data sent to new or existing metrics using[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)(with Monitoring as the target service for a connector).

You can transfer metrics from the Monitoring service using[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm). For more information, see[Creating a Connector with a Monitoring Source](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-monitoring-source.htm).

Metric data posted to the Monitoring service is only presented to you or consumed by the Oracle Cloud Infrastructure features that you enable to use metric data.

When you query a metric, the Monitoring service returns aggregated data according to the specified parameters. You can specify a range (such as the last 24 hours), statistic , and interval . The Console displays one monitoring chart per metric for selected resources. The aggregated data in each chart reflects the selected statistic and interval. API requests can optionally filter by dimension and specify a resolution . API responses include the metric name along with its source compartment and metric namespace . You can feed the aggregated data into a visualization or graphing library.

Metric and alarm data is accessible from the Console, CLI, and API. For retention periods, see[Storage Limits](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Storage).

The Alarms feature of the Monitoring service publishes alarm messages to configured destinations, such as topics in[Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)and streams in[Streaming](https://docs.oracle.com/iaas/Content/Streaming/home.htm).

### Metrics Feature Overview

The Metrics feature relays metric data about the health, capacity, and performance of cloud resources.

A metric is a measurement related to health, capacity, or performance of a resource . Resources, services, and applications emit metrics to the Monitoring service. Common metrics reflect data related to:
- Availability and latency
- Application uptime and downtime
- Completed transactions
- Failed and successful operations
- Key performance indicators (KPIs), such as sales and engagement quantifiers

By querying Monitoring for this data, you can understand how well the systems and processes are working to achieve the service levels you commit to your customers. For example, you can monitor the CPU utilization and disk reads of compute instances . You can then use this data to decide when to provision more instances to handle increased load, troubleshoot issues with the instance, or better understand system behavior.

#### Example Metric: Failure Rate

For application health, one of the common KPIs is failure rate, for which a common definition is the number of failed transactions divided by total transactions. This KPI is typically delivered through application monitoring and management software.

As a developer, you can capture this KPI from applications using[custom metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/publishingcustommetrics.htm). Record observations every time an application transaction takes place and then post that data to the Monitoring service. In this case, set up metrics to capture failed transactions, successful transactions, and transaction latency (time spent per completed transaction).

### Alarms Feature Overview

Use alarms to monitor the health, capacity, and performance of cloud resources.
[

The Alarms feature of the Monitoring service works with the configured destination service to notify you when metrics meet alarm-specified triggers. The previous illustration depicts the flow, starting with resources emitting metric[data points](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__datapointdefinition)to Monitoring. When triggered, an alarm sends an[alarm message](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat)to the configured destination. For Notifications, messages are sent to subscriptions in the configured topic. For Streaming, messages are sent to the configured stream. (This illustration doesn't cover raw and aggregated metric data. For these details, see[the "Monitoring Overview" illustration at the top of this page](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#top__metrics-alarms-diagram).)

When configured, repeat notifications remind you of a continued firing state at the configured repeat interval. You're also notified when an alarm transitions back to the OK state, or when an alarm is reset.

#### Alarm Evaluations

Monitoring evaluates alarms once per minute to find alarm status.

When the alarm[splits notifications](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/split-messages.htm), Monitoring evaluates each tracked metric stream . If the evaluation of that metric stream indicates a new`FIRING`status or other[qualifying event](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes), then Monitoring sends an alarm message.

Monitoring tracks metric streams per alarm for[qualifying events](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes), but messages are subject to the[destination service limits](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#limits-alarm-messages).

##### Illustration of Alarm Evaluation

Consider an alarm that measures the 90th percentile of the metric`CpuUtilization`.
```

```

Notes about this example alarm:
- The percentile is specified in the query as the[statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-statistic.htm)( bold ):
```

```

- Each data point is the 90th percentile (`percentile(0.9)`) of a one-minute window, specified in the query as the[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-interval.htm)(bold):
```

```

- Data point values for this statistic could be anything from null (absent) to 100.
- Data point evaluations:
- For any data point value greater than 85, the evaluation is true (`1`). A true evaluation means that the trigger rule condition has been met.
- For any data point value that isn't greater than 85, the evaluation is false (`0`).
- The alarm doesn't fire until the[trigger rule](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-trigger-rule.htm)condition is met for three successive minutes. This configuration is the alarm's[trigger delay](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-trigger-delay.htm)(`pendingDuration`), set as`PT3M`.
- The alarm updates its state to OK when the breaching condition has been clear for the most recent minute.

The following image shows an aggregated metric stream for the example alarm. Each data point is indicated by a square.  
  

The following table shows consecutive alarm evaluations for the example alarm. The alarm is evaluated on a moving window of three one-minute intervals.

Evaluation period timestamp Minutes in period Data point evaluations* Status
3 [1, 2, 3] [0, 0, 0]`OK`
4 [2, 3, 4] [0, 0, 1]`OK`
5 [3, 4, 5] [0, 1, 1]`OK`
6 [4, 5, 6] [1, 1, 1]`FIRING`
7 [5, 6, 7] [1, 1, 1]`FIRING`
8 [6, 7, 8] [1, 1, 0]`OK`
9 [7, 8, 9] [1, 0, 0]`OK`
10 [8, 9, 10] [0, 0, 0]`OK`

*A value of one (1) means that the[trigger rule](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-trigger-rule.htm)condition is met.

#### How Data Points Are Counted

This section describes how to determine the number of data points (or datapoints ) retrieved by an alarm. This number can help you estimate[Monitoring pricing](https://www.oracle.com/cloud/cloud-native/monitoring/pricing/).

To find the number of data points retrieved by an alarm, first get the number of query streams and minutes analyzed .
- The number of query streams depends on the metric streams returned by the alarm query.
- The minutes analyzed depends on the alarm attributes`interval`,`resolution`, and`pendingDuration`. For alarm queries, the only valid value for`resolution`is`1m`. For more information about`interval`, see[Interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Reference/mql.htm#Interval). For more information about`resolution`and`pendingDuration`, see[Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/).

Each alarm gets evaluated once every minute, and thus each alarm is evaluated 1440 times per day. Each evaluation queries the data in the time window defined by`interval`and it checks the period of time that the alarm persists defined by`pendingDuration`. Therefore, minutes analyzed at every minute is calculated by the following expression:

minutes analyzed at every minute =`interval`* ceiling(`pendingDuration`/`resolution`)

#### About the Internal Reset Period

The internal reset period determines when an[alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/managingalarms.htm)stops checking for an absent metric that triggered the Firing state in the previous evaluation. When the metric is absent for the entire period, later alarm evaluations ignore the indicated metric stream. If no other metric streams are causing the Firing state for the alarm, then the alarm transitions to OK and sends a[RESET message](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes). By default, the RESET message arrives after 13 minutes (internal reset period plus the default slack period of 3 minutes). You can customize the[slack period](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-slack-period.htm).

The length of the internal reset period is globally configured at 10 minutes, which causes the[alarm history](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/get-alarm-history.htm)to show a 10-minute difference.

The beginning of an internal reset period depends on the alarm type. For[threshold alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-threshold.htm), the internal reset period starts when the first absence is detected. For[absence alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-absence.htm), the internal reset period starts after completion of the absence detection period (default of 2 hours, can be[customized](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-absence-detection-period.htm)).

##### Data Points Gathered During an Internal Reset Period

Each evaluation during the ten-minute internal reset period accounts for all data points in that period.

For example, consider a metric stream (`A`) that exceeds the threshold (dashed red line in following diagrams). The alarm fires (`F`). When a lack of emitted data points is detected, an internal reset period begins.

The following diagram shows a single internal reset period for metric stream`A`, from the times`t5`to`t15`. At time`t16`, metric stream`A`is no longer evaluated.
[

The following diagram shows two internal reset periods for metric stream`A`, from the times`t3`to`t5`, and from`t6`to`t16`.`A`emits a data point at`t6`, starting another internal reset period. At time`t17`, metric stream`A`is no longer evaluated.
[

##### Threshold Alarm Example

A[threshold alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-threshold.htm)reports on metric streams that occur outside the threshold. When a previously problematic metric stream is absent, the alarm starts the internal reset period for the metric stream.

In this example, four metric streams are evaluated by a threshold alarm. The Console shows the initial Firing (1:30) and Ok (1:51) transition states. The internal reset period occurs while the alarm is in Firing state.
[

The internal reset period and other significant events in this example are described in the following table.

Time State Transition Events Notifications (see[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes))
12:00`OK``OK`All emissions are within threshold.`FIRING_TO_OK`
1:30`FIRING``FIRING`Emission from resource1 exceeds threshold.`OK_TO_FIRING`
1:35`FIRING``--`No emission is detected for resource1. The alarm starts the internal reset period for resource1.`--`
1:38`FIRING``--`No emission is detected for resource2. The alarm starts the internal reset period for resource2.`--`
1:45`FIRING``--`The internal reset period ends for resource1, so the alarm no longer checks for emissions from resource1. However, the alarm is still Firing because resource2 is still in its own internal reset period.`--`
1:48`OK``OK`The internal reset period ends for resource2, so the alarm no longer checks for emissions from resource2. Emissions from the remaining resources (resource3 and resource4) are within threshold.`RESET`(sent after the three-minute slack period, at about 1:51)

##### Absence Alarm Example

An[absence alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-absence.htm)reports on absent metric streams. When a metric stream is absent, the alarm starts the[absence detection period for the metric stream (default of two hours, can be customized). After completion of the absence detection period, the alarm starts the internal reset period for the metric stream.

In this example, a metric stream is evaluated by an absence alarm that uses the default two-hour absence detection period and default three-minute slack period . The Console shows the initial Firing (2:00) and Ok (4:10) transition states. The internal reset period occurs while the alarm is in Firing state.
[

The internal reset period and other significant events in this example are described in the following table.

Time State Transition Events Notifications (see[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes))
1:00`OK`-- Emissions are detected.
2:00`FIRING``FIRING`No emission is detected for resource-z. The alarm starts the absence detection period for resource-z.`OK_TO_FIRING`
4:00`FIRING``--`The absence detection period for resource-z ends. The alarm starts the internal reset period for resource-z.`--`
4:10`OK``OK`The internal reset period ends for resource-z, so the alarm no longer checks for emissions from resource-z. No metric streams are monitored by the alarm any more, so the alarm transitions to Ok state.`RESET`(sent after the three-minute slack period, at about 4:13)

#### Time Needed to Reflect Alarm Updates

Updates to alarms take up to five minutes to be reflected everywhere.

For example, if you update an alarm to[split notifications](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/split-messages.htm), then it might take up to five minutes for[metric stream status](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/list-alarm-status-metric-stream.htm)to be populated in the Console.

#### Searching for Alarms

Search for alarms using supported attributes.

For more information about Search, see[Overview of Search](https://docs.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm). For attribute descriptions, see[Alarm Reference](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm).

[Search-Supported Attributes for Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#)

- 

`id`
- 

`displayName`
- 

`compartmentId`
- 

`metricCompartmentId`
- 

`namespace`
- 

`query`
- 

`severity`
- 

`destinations`
- 

`suppression`
- 

`isEnabled`
- 

`lifecycleState`
- 

`timeCreated`
- 

`timeUpdated`
- 

`tags`

[Message Types](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#)

The message type indicates the reason that the message was sent.
Note  
  

The specified message type is sent at the indicated time plus the alarm's configured trigger delay, if any.

Repeat messages are also sent if configured in the alarm.

The following table lists the alarm state and transition for each message type.

Message type State Transition Comments
`OK_TO_FIRING``FIRING`from`OK`to`FIRING`
`FIRING_TO_OK``OK`from`FIRING`to`OK`
`REPEAT``FIRING`-- This message type is sent when the alarm maintains the`FIRING`state, and the alarm is configured for repeat notifications.
`RESET``OK`from`FIRING`to`OK`

Important: When a`RESET`status change occurs, look at the health of the resource.

This message type is sent when the alarm transitions to the`OK`state after one or more internal resets . An internal reset occurs when a metric stream that caused the alarm to transition to the`FIRING`state is continuously absent for the full[internal reset period](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset). A metric stream that's internally reset is no longer tracked by the alarm.

Possible causes for an absent metric stream: The resource that was emitting the metric might have been moved or terminated, or the metric might be emitted only on failure. For more information about the internal reset period, see[About the Internal Reset Period](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset).

### Message Format and Examples

See[Example Alarm Messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../alarm-message-examples.htm)and[Alarm Message Format](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../alarm-message-format.htm).

## Monitoring Concepts

The following concepts are essential to working with Monitoring. aggregated data The result of applying a statistic and interval to a selection of raw data points for a metric . For example, you can apply the statistic`max`and interval`1h`(one hour) to the last 24 hours of raw data points for the metric`CpuUtilization`. Aggregated data is displayed in default metric charts in the Console. You can also build metric queries for specific sets of aggregated data. For instructions, see[Viewing Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/viewingcharts.htm)and[Building Metric Queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/buildingqueries.htm). alarm The alarm query to evaluate and the notification destination to use when the alarm is in the firing state, along with other alarm properties. To create an alarm, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-basic.htm). alarm query The Monitoring Query Language (MQL) expression to evaluate for the alarm . An alarm query must specify a metric , statistic , interval , and a trigger rule (threshold or absence). The Alarms feature of the Monitoring service interprets results for each returned time series as a Boolean value, where zero represents false and a nonzero value represents true. A true value means that the trigger rule condition has been met. To create a basic alarm query, see[Creating a Basic Query to Generate an Alarm Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-chart-basic-query.htm). To create an alarm, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-basic.htm). data point A timestamp-value pair for the specified metric . Example:`2022-05-10T22:19:00Z, 10.4`A data point is either raw or aggregated. Raw data points are posted by the metric namespace to the Monitoring service using the[PostMetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/PostMetricData)operation. The frequency of the data points posted varies by metric namespace . For example, a custom namespace might send data points for a metric at a 20-second frequency . Aggregated data points are the result of applying a statistic and interval to raw data points. The interval of the aggregated data points is specified in the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)request. For example, a request specifying the statistic`sum`and interval`1h`(one hour) returns a`sum`value for each hour of available raw data points for the metric . dimension A qualifier provided in a metric definition . Example: Resource identifier (`resourceId`), provided in the definitions of oci_computeagent metrics. Use dimensions to filter or group metric data. Example dimension name-value pair for filtering by availability domain:`availabilityDomain = "VeBZ:PHX-AD-1"`To select a dimension for a metric chart or query, see[Selecting Dimensions to Filter Metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-dimensions.htm)and[Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-dimension.htm). To select an interval for an alarm, see[Selecting the Interval for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-interval.htm). frequency The time period between each posted raw data point for a metric . (Raw data points are posted by the metric namespace to the Monitoring service.) While frequency varies by metric, default service metrics typically have a frequency of 60 seconds (one data point posted per minute). See also[resolution](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts__resolutiondefinition). interval The time window used to convert the set of raw data points . The timestamp of the aggregated data point corresponds to the end of the time window during which raw data points are assessed. For example, for a five-minute interval, the timestamp "2:05" corresponds to the five-minute time window from 2:00: n to 2:05:00.
[The following example query (MQL expression) specifies a 5-minute interval. For valid interval options in MQL expressions, see[Interval (Monitoring Query Language (MQL) Reference)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).
```

```

Note  
  
Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported. To select an interval for a metric chart or query, see[Changing the Interval for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-interval.htm)and[Selecting the Interval for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-interval.htm). To select an interval for an alarm, see[Selecting the Interval for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-interval.htm). See also resolution . message The content that the Alarms feature of the Monitoring service publishes to topics in the alarm's configured notification destinations . A message is sent when the alarm transitions to another state, such as from`OK`to`FIRING`. For more information about alarm messages, see[Message Format and Examples](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageFormat). metadata A reference provided in a metric definition . Example: unit (bytes), provided in the definition of the oci_computeagent metric`DiskBytesRead`. Use metadata to determine additional information about a metric. For metric definitions, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). metric A measurement related to health, capacity, or performance of a resource. Example: The`oci_computeagent`metric`CpuUtilization`, which measures usage of a compute instance. For metric definitions, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).
Note  
  
Metric resources don't have OCIDs . metric definition A set of references, qualifiers, and other information provided by a metric namespace for a metric . For example, the oci_computeagent metric`DiskBytesRead`is defined by dimensions (such as resource identifier) and metadata (specifying bytes for unit) as well as identification of its metric namespace (oci_computeagent). Each posted set of data points carries this information. Use the[ListMetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Metric/ListMetrics)API operation to get metric definitions. For metric definitions, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). To select a metric name for a query, see[Selecting the Metric Name for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-metric.htm). To select a metric name for an alarm, see[Creating a Basic Query to Generate an Alarm Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-chart-basic-query.htm)and[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-basic.htm). metric namespace Indicator of the resource , service, or application that emits the metric . Provided in the metric definition . For example, the`CpuUtilization`metric definition emitted by the Oracle Cloud Agent software on compute instances lists the metric namespace`oci_computeagent`as the source of the`CpuUtilization`metric . For metric definitions, see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). To select a metric namespace for a metric chart or query, see[Viewing Default Metric Charts for a Metric Namespace (Multiple Resources)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-namespace.htm)and[Selecting the Metric Namespace for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-namespace.htm). To select a metric namespace for an alarm, see[Creating a Basic Query to Generate an Alarm Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-chart-basic-query.htm)and[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-basic.htm). metric stream An individual set of aggregated data for a metric and zero or more dimension values . In[the Metric streams status page](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/list-alarm-status-metric-stream.htm), each metric stream corresponds to a set of dimension key-value pairs. In[metric charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/viewingcharts.htm)(in the Console), each metric stream is depicted as a line (unless you[aggregate all metric streams](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-aggregate-metric-streams.htm)). The following image depicts metric streams in a chart. Each line in the chart corresponds to a metric stream.
[For example, consider a compartment containing three compute instances in the`AD-1`availability domain (including two in the`ipexample`instance pool) and a fourth instance in the`AD-2`availability domain. In this example, the CPU Utilization metric chart shows four lines (one per instance). When[filtered](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-dimensions.htm)by the`AD-1`availability domain, the chart shows three lines. When further filtered by the`ipexample`instance pool, the chart shows two lines. To select metric streams in a query, see[Selecting Dimensions to Filter Metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-dimensions.htm),[Selecting Dimensions for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-dimension.htm), and[Selecting Dimensions for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-dimensions.htm). To set up an alarm for notifications per metric stream, see[Creating an Alarm That Splits Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-split.htm)and[Scenario: Split Messages by Metric Stream](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/split-messages.htm). notification destination Details for sending messages when the alarm transitions to another state, such as from`OK`to`FIRING`. The details and setup might vary by destination service. Available destination services include Notifications and Streaming. For the Notifications service, specify a[topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__topicdefinition). (If you're creating the topic for the alarm, also specify one or more[subscription](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts__subscriptiondefinition)protocols (such as PagerDuty). For the Streaming service, specify a[stream](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#concepts). For examples of alarm messages sent to topics and streams, see[Example Alarm Messages](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../alarm-message-examples.htm). To set up a notification destination in an alarm, see[Defining Notifications for an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-notification.htm). Oracle Cloud Agent software Software used by a compute instance to post raw data points to the Monitoring service. Automatically installed with the latest versions of supported images. See[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm). query The Monitoring Query Language (MQL) expression and associated information (such as metric namespace) to evaluate for returning aggregated data . The query must specify a metric , statistic , and interval . To create a metric query, see[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric.htm). To create an alarm query, see[Creating a Basic Query to Generate an Alarm Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-chart-basic-query.htm). resolution

The period between time windows, or the regularity at which time windows shift. For example, use a resolution of`1m`to retrieve aggregations every minute.
Note  
  
For metric queries, the interval you select drives the default resolution of the request, which determines the maximum time range of data returned.

For alarm queries, the specified interval has no effect on the resolution of the request. The only valid value of the resolution for an alarm query request is`1m`. For more information about the resolution parameter as used in alarm queries, see[Alarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm).

As shown in the following illustration, resolution controls the start time of each aggregation window relative to the previous window while interval controls the length of the windows. Both requests apply the statistic`max`to the data within each five-minute window (from the interval), resulting in a single aggregated data point representing the highest`CPUutilization`counter for that window. Only the resolution value differs. This resolution changes the regularity at which the aggregation windows shift, or the start times of successive aggregation windows. Request A doesn't specify a resolution and thus uses the default value equal to the interval (5 minutes). This request's five-minute aggregation windows are thus taken from the sets of data points emitted from 0: n to 5:00, 5: n to 10:00, and so forth. Request B specifies a 1-minute resolution, so its five-minute aggregation windows are taken from the set of data points emitted every minute from 0: n to 5:00, 1: n to 6:00, and so forth.
[

To specify a nondefault resolution that differs from the interval, see[Selecting a Nondefault Resolution for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-resolution.htm)and[Creating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm.htm). resource group A custom string provided with a custom metric that can be used as a filter or to aggregate results. The resource group must exist in the definition of the posted metric. Only one resource group can be applied per metric. To select a resource group in a query, see[Selecting a Resource Group in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-resource-group.htm). To select a resource group in an alarm query, see[Selecting a Resource Group in an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-resource-group.htm). statistic The aggregation function applied to the set of raw data points . To select the statistic for a metric chart or query, see[Changing the Statistic for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-statistic.htm)and[Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-statistic.htm). To select the statistic for an alarm query, see[Selecting the Statistic for an Alarm Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-statistic.htm). suppression A configuration to stop publishing messages during the specified time range. Useful for suspending alarm notifications during system maintenance. To suppress alarms, see[Suppressing a Single Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-suppression.htm)and[Suppressing Multiple Alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-alarm-suppression-multiple.htm). time range The bounds (timestamps) of the metric data that you want. For example, the past hour. To select the time range for a metric chart or query, see[Changing the Time Range for Default Metric Charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/view-chart-time-range.htm),[Changing the Time Range for a Custom Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/metrics-explorer-time-range.htm), and[Selecting a Nondefault Time Range for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/query-metric-time-range.htm). trigger rule The condition that must be met for the alarm to be in the firing state. A trigger rule can be based on a threshold or absence of a metric. To set up a trigger rule in an alarm, see[Adding Trigger Rules to an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/create-edit-alarm-query-trigger-rule.htm).

## Availability

The Monitoring service is available in all Oracle Cloud Infrastructure commercial regions. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the[list](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About__The)of available regions, along with associated locations, region identifiers, region keys, and availability domains.

## Supported Services

The following services have resources or components that can emit metrics to Monitoring:
- Analytics Cloud - see[Monitor Metrics](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoci/monitor-metrics.html)
- API Gateway - see[API Gateway Metrics](https://docs.oracle.com/iaas/Content/APIGateway/Reference/apigatewaymetrics.htm)
- Application Performance Monitoring - see[Application Performance Monitoring Metrics](https://docs.oracle.com/iaas/application-performance-monitoring/doc/application-performance-monitoring-metrics.html)
- Autonomous Recovery Service - see[Recovery Service Metrics](https://docs.oracle.com/iaas/recovery-service/doc/recovery-service-metrics.html)
- Bastion - see[Bastion Metrics](https://docs.oracle.com/iaas/Content/Bastion/Reference/metrics.htm)
- Batch - see[Batch Metrics](https://docs.oracle.com/iaas/Content/oci-batch/batchmetrics.htm)
- Big Data Service - see[Managing Cluster Metrics](https://docs.oracle.com/iaas/Content/bigdata/metrics-view.htm)
- Block Volume - see[Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm)
- Blockchain Platform - see[Monitor Metrics](https://docs.oracle.com/en/cloud/paas/blockchain-cloud/administeroci/monitor-metrics.html)
- 

Compute - see[Compute Metrics and Monitoring](https://docs.oracle.com/iaas/Content/Compute/References/computemetricsoverview.htm)
- 

Compute Cloud@Customer - see[Compute Cloud@Customer Metrics](https://docs.oracle.com/iaas/compute-cloud-at-customer/ccc/metrics.htm)
- Connector Hub - see[Connector Hub Metrics](https://docs.oracle.com/iaas/Content/connector-hub/metrics.htm)
- Container Instances - see[Container Instance Metrics](https://docs.oracle.com/iaas/Content/container-instances/container-instance-metrics.htm)
- Data Catalog - see[Data Catalog Metrics](https://docs.oracle.com/iaas/Content/data-catalog/using/metrics.htm)
- Data Flow - see[Data Flow Metrics](https://docs.oracle.com/iaas/Content/data-flow/using/dfs_manage_data_with_data_flow.htm#metrics)
- Data Integration - see[Data Integration Metrics](https://docs.oracle.com/iaas/Content/data-integration/using/metrics.htm)
- Data Science - see[Metrics](https://docs.oracle.com/iaas/Content/data-science/using/metrics.htm)
- Database - see these pages:
- [Monitor Performance with Autonomous AI Database Metrics](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-monitor-metrics.html)(Autonomous AI Database Serverless)
- [Database Observability with Autonomous AI Database Metrics](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/lbdmm/index.html)(Autonomous AI Database on Dedicated Exadata Infrastructure)
- [Metrics for Oracle Exadata Database Service on Dedicated Infrastructure in the Monitoring Service](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/metrics-for-exadata-database-service-on-dedicated-infrastructure-in-the-monitoring-service.html#GUID-B82F2A9D-56C4-459A-9EEE-A3330741F31F)(from[Reference Guides for Exadata Cloud Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/reference.html#GUID-B82F2A9D-56C4-459A-9EEE-A3330741F31F))
- Metrics for Base Database Service in the Database Management Service:[Monitor a Database Using Database Management Metrics](https://docs.oracle.com/en/cloud/paas/base-database/available-metrics/index.html)
- [Metrics for External Database](https://docs.oracle.com/iaas/external-database/doc/metrics-external-database.html)
- Database Management - see[Database Management Metrics for Oracle Databases](https://docs.oracle.com/en/cloud/paas/base-database/available-metrics/index.html)
- Database Migration - see[Database Migration Metrics](https://docs.oracle.com/iaas/database-migration/doc/database-migration-metrics.html)
- OCI Database with PostgreSQL - see[OCI Database with PostgreSQL Metrics](https://docs.oracle.com/iaas/Content/postgresql/metrics.htm)
- DevOps - see[DevOps Metrics](https://docs.oracle.com/iaas/Content/devops/using/devops_metrics.htm)
- Digital Assistant - see[Digital Assistant Metrics](https://docs.oracle.com/iaas/digital-assistant/doc/service-administration1.html#DACUA-GUID-6BF531B8-4F07-406C-8D04-53B63527B1A3)
- DNS - see[DNS Metrics](https://docs.oracle.com/iaas/Content/DNS/Reference/dnsmetrics.htm)
- Email Delivery - see[Email Delivery Metrics](https://docs.oracle.com/iaas/Content/Email/Reference/metricsalarms.htm)
- Events - see[Events Metrics](https://docs.oracle.com/iaas/Content/Events/Reference/eventsmetrics.htm)
- File Storage - see[File System Metrics](https://docs.oracle.com/iaas/Content/File/Reference/filemetrics.htm)
- Functions - see[Function Metrics](https://docs.oracle.com/iaas/Content/Functions/Reference/functionsmetrics.htm)
- Globally Distributed Autonomous AI Database - see[Monitor Performance with Autonomous AI Database Metrics](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-monitor-metrics.html)
- Globally Distributed Exadata Database on Exascale Infrastructure (See[Metrics for Oracle Exadata Database Service on Dedicated Infrastructure in the Monitoring Service](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/metrics-for-exadata-database-service-on-dedicated-infrastructure-in-the-monitoring-service.html#GUID-B82F2A9D-56C4-459A-9EEE-A3330741F31F))
- GoldenGate - see[Oracle Cloud Infrastructure GoldenGate Metrics](https://docs.oracle.com/iaas/goldengate/doc/goldengate-metrics.html)
- Health Checks - see[Health Checks Metrics](https://docs.oracle.com/iaas/Content/HealthChecks/Reference/metricsalarms.htm)
- Integration 3:[View Message Metrics and Billable Messages](https://docs.oracle.com/iaas/application-integration/doc/viewing-message-metrics.html)
- Java Management - see[Java Management Metrics](https://docs.oracle.com/iaas/jms/doc/java-management-metrics.html)
- Kubernetes Engine - see[Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/iaas/Content/ContEng/Reference/contengmetrics.htm)
- Load Balancer - see[Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm)
- Logging - see[Logging Metrics](https://docs.oracle.com/iaas/Content/Logging/metrics.htm)
- Log Analytics - see[Monitor Log Analytics Using Service Metrics](https://docs.oracle.com/iaas/log-analytics/doc/administer-other-actions.html#GUID-B7EA5A71-3887-49C4-9D8E-9D45E2CCEBF1)
- Media Streams (Media Services)- see[Media Streams Metrics](https://docs.oracle.com/iaas/Content/media-services/mediastreams/mediastreams_metrics.htm)
- Management Agent - see[Management Agent Metrics](https://docs.oracle.com/iaas/management-agents/doc/agent-metrics.html)
- MySQL HeatWave - see[Metrics](https://docs.oracle.com/iaas/mysql-database/doc/mysql-database-metrics.html)
- 

Networking - see[Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm)
- NoSQL Database Cloud - see[Service Metrics](https://docs.oracle.com/en/cloud/paas/nosql-cloud/fnsxl/#GUID-3D6B7AE0-EBE0-4E41-AC43-AA13DB419BF2)
- Notifications - see[Notifications Metrics](https://docs.oracle.com/iaas/Content/Notification/Reference/notificationmetrics.htm)
- Network Firewall - see[Monitoring Firewalls](https://docs.oracle.com/iaas/Content/network-firewall/metrics.htm)
- Object Storage - see[Object Storage Metrics](https://docs.oracle.com/iaas/Content/Object/Reference/objectstoragemetrics.htm)
- Ops Insights - see[Ops Insights Metrics](https://docs.oracle.com/iaas/operations-insights/doc/operations-insights-metrics.html)
- Oracle APEX Application Development - see[Monitor APEX Service Performance](https://docs.oracle.com/en/cloud/paas/apex/gsadd/monitor-apex-service-performance.html#GUID-4E640EB2-CACB-4994-BEE4-E40237AA5945)
- OS Management Hub - see[OS Management Hub Metrics](https://docs.oracle.com/iaas/osmh/doc/metrics.htm)
- Process Automation - see[Monitor Oracle Cloud Infrastructure Process Automation](https://docs.oracle.com/iaas/process-automation/oci-process-automation/monitor-oracle-cloud-infrastructure-process-automation.html)
- Queue - see[Queue Metrics](https://docs.oracle.com/iaas/Content/queue/metrics.htm)
- Secret Management Service - see[Secret Management Metrics](https://docs.oracle.com/iaas/Content/secret-management/Concepts/metrics.htm)
- Service Mesh - see[Service Mesh Metrics](https://docs.oracle.com/iaas/Content/service-mesh/sm-metrics.htm)
- Stack Monitoring - see[Metric Reference](https://docs.oracle.com/iaas/stack-monitoring/doc/metric-reference.html)
- Streaming - see[Streaming Metrics](https://docs.oracle.com/iaas/Content/Streaming/Reference/streamingmetrics.htm)
- Vulnerability Scanning - see[Scanning Metrics](https://docs.oracle.com/iaas/Content/scanning/using/metrics.htm)
- WAF - see[Edge Policy Metrics](https://docs.oracle.com/iaas/Content/WAF/Reference/metricsalarms.htm)

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)., see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
Note  
  
Metric resources don't have OCIDs .

## Ways to Access Monitoring

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Console: To access Monitoring using the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password. Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Service Metrics .

API: To access Monitoring through APIs, use[Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/)for metrics and alarms and[Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/)for notifications (used with alarms).

CLI: See[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html)and[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).

### Dual-Stack support and IPv6 endpoints

You can use dual-stack endpoints with Monitoring. A dual-stack endpoint resolves to both IPv4 and IPv6 addresses, so the same host name can be used by clients connecting over either address family.

To use dual-stack support, send requests to the dual-stack host name for the service.

IPv4-only endpoint Dual-stack endpoint
https://telemetry-ingestion. &lt;region&gt; . &lt;topleveldomainname&gt; telemetry-ingestion. &lt;region&gt; .ds.oci. &lt;topleveldomainname&gt;
https://telemetry. &lt;region&gt; . &lt;topleveldomainname&gt; telemetry. &lt;region&gt; .ds.oci. &lt;topleveldomainname&gt;

Use the dual-stack endpoint when clients might connect over either IPv4 or IPv6. Clients on IPv6 only networks must use the dual-stack endpoint.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

For more information about user authorizations for monitoring, see[IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).

Administrators: For common policies that give groups access to metrics, see[Metric Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups). For common alarm policies, see[Alarm Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#alarm-groups). To authorize resources, such as instances, to make API calls, add the resources to a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm). Use the dynamic group's matching rules to add the resources, and then create a policy that allows that dynamic group access to metrics. See[Metric Access for Resources](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-dynamic).

## Limits on Monitoring

See[Monitoring Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#MonitoringLimits)for a list of applicable limits and instructions for requesting a limit increase.

Other limits include the following.

### Storage Limits

Item Time range stored
Metric definitions 90 days
Alarm history entries 90 days

### Returned Data Limits (Metrics)

When you[query metrics](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/buildingqueries.htm)and[view metric charts](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/viewingcharts.htm), the returned data is subject to certain limits. Limits information for returned data includes the 100,000 data point maximum and[time range maximums (determined by resolution, which relates to interval)](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval). See[MetricData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData).

### Alarm Message Limits

The maximum number of messages per alarm evaluation depends on the alarm destination. Limits are associated with the Oracle Cloud Infrastructure service used for the destination.

Monitoring tracks 200,000 metric streams per alarm for[qualifying events](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MessageTypes). For more information about alarm evaluations, see[Alarm Evaluations](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarm-eval)on this page.

Alarm destination Delivery Maximum alarm messages per evaluation
topic (Notifications)[At least once](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts)60
stream (Streaming)[At least once](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm#benefits_of_streams)100,000

For example, consider the following evaluations of an alarm that[splits notifications](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../Tasks/split-messages.htm)among 200 metric streams, using a topic as its destination.

Alarm evaluation (time) Metric stream transition Generated messages Sent messages Dropped messages
00:01:00 110 metric streams transition from OK to FIRING. 110 60 50
00:02:00 90 metric streams transition from OK to FIRING. 90 60 30

When a topic or stream is overused, it can result in delayed alarm notifications. Overuse can occur when multiple resources are using that topic or stream.

#### Best Practices to Work Within Limits

When you expect a high volume of alarm notifications, follow these best practices to help prevent exceeding alarm message limits and associated delays.
- Reserve a single topic or stream for use with a high-volume alarm. Don't use one topic or stream for multiple high-volume alarms.
- If you expect more than 60 messages per minute, specify Streaming as the alarm destination.
- Streams:
- Create partitions based on expected load. See[Limits on Streaming Resources](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm).
- If alarm messages exceed the stream space, then update the alarm to use a different stream that has more partitions. For example, if the original stream contains five partitions, create a stream with ten partitions and then update the alarm to use the new stream.
Note  
  
To avoid missing messages, continue consuming the original stream until no more messages are received.
- Increase limits for the tenancy:
- Topics: See[Limits for publishing messages (PublishMessage operation)](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#limits__PublishMessageLimits).
- Streams: See[Limits on Streaming Resources](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm).

### Troubleshooting Limits

To troubleshoot a query error for too many metric streams, see[Error: Exceeded Maximum Metric Streams](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../troubleshooting-queries.htm#query-limits).

For troubleshooting information, see[Troubleshooting Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/../troubleshooting.htm).

## Security

This topic describes security for Monitoring.

For information about how to secure Monitoring, including security information and recommendations, see[Securing Monitoring](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm)
