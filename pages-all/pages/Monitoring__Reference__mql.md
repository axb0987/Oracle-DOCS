# Monitoring Query Language (MQL) Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm
- Fetched: 2026-09-05 02:38 CDT

# Monitoring Query Language (MQL) Reference

Understand the syntax of Monitoring Query Language (MQL) expressions and review valid values for interval, statistic, and predicate operators in MQL expressions.

For information about editing MQL , see[Editing the MQL Expression for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-mql.htm). To retrieve a specific time range, such as the last hour, see[Selecting a Nondefault Time Range for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-time-range.htm).

## MQL Syntax

MQL syntax governs expressions for querying metrics that are published to the Monitoring service. MQL expressions define[queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric.htm)(including[alarm queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/create-alarm.htm)). MQL acts on[aggregated data](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Concepts/monitoringoverview.htm#concepts__aggregateddatadefinition2).

The following diagram depicts required components and common optional components.
Note  
  

Some components can appear in an MQL expression multiple times. For example, you can use two grouping functions (as in[`groupBy()`](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-groupby.htm), followed by a[statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-statistic.htm), followed by[`grouping()`](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-grouping.htm)). You can also[nest queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-nested.htm).

You can also[join multiple queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#join)into a single query.

For alarms in the Console, the`absent()`statistic is listed under Operator . See[Creating an Absence Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/create-alarm-absence.htm).

[More information about absent() in the Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#)

To select the`absent()`statistic in the Console, see the following page-specific instructions.
- Create Alarm or Edit alarm page: In Basic mode, select absent from Operator under Trigger rule . In Advanced mode (select Switch to Advanced Mode ),[update the MQL expression](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm).
- Metrics Explorer page: Select Advanced mode to use[MQL](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
- Service Metrics page:[Open the query in Metrics Explorer , then select Advanced mode to use[MQL](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).
[

For information about reading railroad diagrams, see[Reading Railroad Diagrams](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm#railroad-diagrams).

## Valid Values for MQL Expressions

Review valid values for interval, statistic, and predicate operators in MQL expressions.

### Interval

Note  
  

Along with[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Concepts/monitoringoverview.htm#concepts__intervaldefinition), consider the[resolution](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Concepts/monitoringoverview.htm#concepts__resolutiondefinition)and[time range](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Concepts/monitoringoverview.htm#concepts__time-range-definition).

Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported.

Select an alarm interval based on the frequency at which the metric is emitted. For example, a metric emitted every five minutes requires a 5-minute alarm interval or greater. Most metrics are emitted every minute, which means most metrics support any alarm interval. To determine valid alarm intervals for a specific metric, check the[relevant service's metric reference](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices). Example: One-Minute Interval (`1m`)
```

```

Following are valid intervals for MQL expressions:`1m`-`60m`,`1h`-`24h`,`1d`

For instructions, see[Selecting the Interval for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-interval.htm).
Note  
  
For metric queries, the interval you select drives the default resolution of the request, which determines the maximum time range of data returned.

For alarm queries, the specified interval has no effect on the resolution of the request. The only valid value of the resolution for an alarm query request is`1m`. For more information about the resolution parameter as used in alarm queries, see[Alarm](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Alarm).

[Maximum time range returned for a query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#)

The maximum time range returned for a metric query depends on the resolution. By default, for metric queries, the resolution is the same as the query interval.

The maximum time range is calculated using the current time, regardless of any specified end time. Following are the maximum time ranges returned for each interval selection available in the Console (Basic mode).

Interval Default resolution (metric queries) Maximum time range returned

1 minute

Auto ( Service Metrics page)*, when the selected period of time is 6 hours or less 1 minute 7 days

5 minutes

Auto ( Service Metrics page)*, when the selected period of time is more than 6 hours and less than 36 hours 5 minutes 30 days

1 hour

Auto ( Service Metrics page)*, when the selected period of time is more than 36 hours 1 hour 90 days

1 day 1 day 90 days

* The maximum time range returned when you select Auto for Interval ( Service Metrics page only) is determined by the automatic interval selection. The automatic interval selection is based on the selected period of time.

To specify a nondefault resolution that differs from the interval, see[Selecting a Nondefault Resolution for a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-resolution.htm). Example 1 for Returned Data One-minute interval and resolution up to the current time, sent at 10:00 on January 8. No resolution or end time is specified, so the resolution defaults to the interval value of`1m`, and the end time defaults to the current time (`2023-01-08T10:00:00.789Z`). This request returns a maximum of 7 days of metric data points. The earliest data point possible within this seven-day period would be 10:00 on January 1 (`2023-01-01T10:00:00.789Z`). Example 2 for Returned Data Five-minute interval with one-minute resolution up to two days ago, sent at 10:00 on January 8. Because the resolution drives the maximum time range, a maximum of 7 days of metric data points is returned. While the end time specified was 10:00 on January 6 (`2023-01-06T10:00:00.789Z`), the earliest data point possible within this seven-day period would be 10:00 on January 1 (`2023-01-01T10:00:00.789Z`). Therefore, only 5 days of metric data points can be returned in this example.

### Statistic

The statistic is the aggregation function applied to the set of raw data points at the specified interval . Example: Mean Statistic
```

```

For instructions, see[Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-statistic.htm).

Following are valid statistics.

Statistic (MQL expression) Statistic option (Basic Mode in the Console) Description
`absent()`(see[absent](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#predicate__absentoption)operator)

Absence predicate.

Returns true (1) if the metric is absent for the entire[interval](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).

Returns false (0) if the metric is present during the interval.

Is ignored after the[absence detection period](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset__absent), not generating any values.

The default absence detection period is two hours. You can customize this period when creating or updating an absence alarm. See[Customizing the Absence Detection Period for an Alarm Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm).

Valid values range from one minute (`1m`) to three days (`3d`or`72h`). Specify the amount of time in the absence detection period using a number and unit (`m`,`h`, or`d`for minute, hour, or day).

Use this statistic in basic queries as well as[absence alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm). See[Specifying a Predicate in a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm).
`avg()`(not available) Returns the value of Sum divided by Count during the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval). Identical to`mean()`.
`count()`Count Returns the number of observations received in the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`first()`(not available) For each interval, returns the value with the earliest timestamp in the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`increment()`(not available) Returns the per-[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval)change.
`last()`(not available) For each interval, returns the value with the latest timestamp in the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`max()`Max Returns the highest value observed during the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`mean()`Mean Returns the value of Sum divided by Count during the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`min()`Min Returns the lowest value observed during the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).
`percentile(p)`

P50

P90

P95

P99

P99.9 ( Service Metrics page only)

Returns the estimated value of the specified percentile (`p`when using SDK, CLI, or API) during the specified[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval). Valid values are greater than 0.0 and less than 1.0.

For example,`percentile(0.8)`returns the value of the 80th percentile.
`rate()`Rate Returns the per-[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval)average rate of change. The unit is per-second.
`sum()`Sum Returns all values added together, per[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#Interval).

### Predicate Operators

The predicate component keeps only specified values from the metric streams. Use a predicate operator to define a threshold or absence.
Example 1: Greater than 80 Percent for Mean CPU Utilization
```

```
Example 2: Between 60 and 80 Percent for Mean CPU Utilization
```

```
Example 3: Greater than 1 for Errors
```

```
Example 4: Greater than 85 for 90th Percentile CPU Utilization (Selecting an Availability Domain and Grouping by Pool)
```

```
Example 5: At Least 20 for Minimum CPU Utilization (Selecting Either "ol8" or "ol7")
```

```
Example 6: At Least 30 for Minimum CPU Utilization (Selecting Instance Names Beginning with "instance-2023-")
```

```
Example 7: Absence of CPU Utilization Metrics for Specified Resource, set to 20 hours for absence detection period
```

```
`absent()`description: Returns true (1) if the metric is absent for the entire[interval](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval). Returns false (0) if the metric is present during the interval. Is ignored after the[absence detection period](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset__absent), not generating any values.

For instructions, see[Specifying a Predicate in a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-predicate.htm).

Following are valid operators.

Operator (MQL expression) Operator option (Basic Mode in the Console) Comments
`>`greater than
`>=`greater than or equal to
`==`equal to
`=~`(not available)[Fuzzy Matching](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#fuzzy-mql).
`!=`(not available) Not equal to.
`<`less than
`<=`less than or equal to
`in`between (inclusive of specified values) Inclusive of the two specified values.
`not in`outside (inclusive of specified values) Inclusive of the two specified values.
(see[absent()](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/mql.htm#statistic__absent)statistic) absent

Absence predicate.

Returns true (1) if the metric is absent for the entire[interval](https://docs.oracle.com/iaas/Content/Monitoring/Reference/mql.htm#Interval).

Returns false (0) if the metric is present during the interval.

Is ignored after the[absence detection period](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#reset__absent), not generating any values.

The default absence detection period is two hours. You can customize this period when creating or updating an absence alarm. See[Customizing the Absence Detection Period for an Alarm Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-query-absence-detection-period.htm).

Valid values range from one minute (`1m`) to three days (`3d`or`72h`). Specify the amount of time in the absence detection period using a number and unit (`m`,`h`, or`d`for minute, hour, or day).

Use this statistic in basic queries as well as[absence alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-absence.htm). See[Specifying a Predicate in a Query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm).

For alarm instructions, see[Creating a Threshold Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/create-alarm-threshold.htm)and[Creating an Absence Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/create-alarm-absence.htm).

## Arithmetic Operators

The following arithmetic operators are supported in MQL expressions.

Operator Description
`+`Add
`-`Subtract
`*`Multiply
`/`Divide
`%`Modulo (divide and return remainder)

Example 1: Calculate the available percentage of CPU utilization (`CPUUtilization`metric in the[`oci_computeagent`namespace](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm#Availabl)).
```

```

Example 2: Calculate value in seconds, instead of the metric's default unit of milliseconds (`TotalRequestLatency`metric in the[`oci_objectstorage`namespace](https://docs.oracle.com/iaas/Content/Object/Reference/objectstoragemetrics.htm))
```

```

## Join Queries

Use the`&&`(AND) and`||`(OR) operators to join queries. Multiple joined queries act as a single query.
Note  
  
The`&&`(AND) and`||`(OR) operators can only be used between queries. Don't use them between dimension sets. For example, the following query is invalid:`CpuUtilization[1m]{faultDomain =~ "FAULT-DOMAIN-1|FAULT-DOMAIN-2" || resourceDisplayName = "test"}.mean()`

Join operator Description
`&&`AND: Join queries. Returns true if both operands are true. Returns false otherwise.
`||`OR: Join queries. Returns true if either operand is true, or if both operands are true. Returns false otherwise.

Example 1: Join queries with OR. Return true if CPU utilization data point is in fault domain 1 or 2 OR memory utilization data point is in fault domain 1 or 2.
```

```

Example 2: Join alarm queries with AND. Trigger the alarm (transition to firing state) only when both queries are true: At least one error exists AND the mean error is greater than half.
```

```

Example 3: Join alarm queries with AND. Trigger the alarm (transition to firing state) only when both queries are true: For smaller reads (0 to 8 Kilobytes), the 50th percentile of requests exceeds 100 AND the mean latency is less than 0.01.
```

```

## Fuzzy Matching

Specify approximate ("fuzzy") matches to dimension values in an MQL expression.

Use fuzzy matching when specifying multiple values for a[dimension](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Reference/../Tasks/query-metric-dimension.htm)name.

In place of the equals sign (`=`) before the set of values, use the following comparison operator.

Comparison operator Description
`=~`(equals sign followed by tilde) Approximately equal to. Use for fuzzy matches

For fuzzy matching, surround the set of values with quotes:`name = "val*"`or`name = "value1|value2"`

Update the set of values using one or more of the following characters.

Value Fuzzy Match Character Description
`*`(asterisk) Wildcard, indicating zero to many characters.
`|`(pipe) OR operand for dimension values.

Example showing fuzzy matching for two possible resource names ("ol8" or "ol7"):
```

```

Example showing fuzzy matching for resource names containing the phrase "instance-2023-":
```

```

Example showing fuzzy matching for three dimension value sets (test compute instances in fault domain 1 that use the`myshape`shape):

```

```
