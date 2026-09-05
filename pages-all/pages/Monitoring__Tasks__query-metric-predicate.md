# Specifying a Predicate in a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm
- Fetched: 2026-09-05 02:39 CDT

# Specifying a Predicate in a Query

Specify a predicate for querying metric data in Monitoring.

While typically used with[alarms](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm.htm), you can also use predicates in queries for custom metric charts.

For valid predicate operators in MQL expressions, see[Predicate Operators](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#predicate).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

[Examples](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm#)

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

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-predicate.htm#)
- 

This section describes how to specify a predicate in a query on the Metrics Explorer page. On this page, predicates are available in Advanced mode (MQL) only. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select Advanced mode .
- Edit the text in the Query code editor box.
Example 1: Threshold Predicate`> 80`is the threshold predicate in the following MQL expression.
```

```
The graph from[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)now shows a single value. The 85% value resolves to true (1) to indicate that it satisfies the MQL expression. (If no values exceeded 80, then the graph on the Metrics Explorer page would show "no data.") Example 2: Absence Predicate`absent()`is the absence predicate in the following MQL expression.
```

```
The graph from[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)now shows a "1" value for a metric stream. The "1" value in the graph indicates that the compute instance corresponding to this metric stream didn't emit`CpuUtilization`metric data until 1:30.

For valid predicate operators in MQL expressions, see[Predicate Operators](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#predicate).
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to specify a predicate (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to specify a predicate (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
