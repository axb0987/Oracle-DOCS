# Selecting Dimensions for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm
- Fetched: 2026-09-05 02:39 CDT

# Selecting Dimensions for a Query

Limit returned metric data by selecting dimensions when querying metric data in Monitoring. A dimension is a qualifier provided in a metric definition. In MQL, the dimension selection component specifies name-value pairs for dimensions, surrounded by curly brackets.

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Considerations

Any text is accepted as a dimension name. If the dimension doesn't exist, then data isn't filtered.

To ensure that the dimension exists,[list dimensions for the metric name](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm)or see[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Concepts/monitoringoverview.htm#SupportedServices)

[Examples](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)

Note  
  
Quotes around the value (as in`"FAULT-DOMAIN-1"`) can be omitted unless the value contains spaces or is used in[Fuzzy Matching](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#dimension-fuzzy). Example 1: Fault Domain
```

```
Example 2: Compartment
```

```
Example 3: Shape (with Grouping)
```

```
Example 4: Multiple Dimension Name-Value Pairs: Fault Domain, Name, and Shape

```

```
The dimensions in this query are processed with an`AND`operator. Resulting data includes only those metric streams that match all dimensions. Example 5: Multiple Values for a Dimension: Fault Domain 1 or 2

```

```
The dimension values in this query are processed with an`OR`operator, using[fuzzy matching](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#dimension-fuzzy). (Fuzzy matching is available in MQL expressions only. In the Console, use Advanced mode.) Resulting data includes metric streams that match either value.

[Fuzzy Matching](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)

Specify approximate ("fuzzy") matches to dimension values in an MQL expression.

Note  
  
Fuzzy matching is available in MQL expressions only. In the Console, use Advanced mode.

In place of the equals sign (`=`) between the dimension name and set of values, use the following comparison operator.

Comparison operator Description
`=~`(equals sign followed by tilde) Approximately equal to. Use for fuzzy matches

For fuzzy matching, surround the set of values with quotes:`name = "val*"`or`name = "value1|value2"`

Update the set of values using one or more of the following characters.

Value Fuzzy Match Character Description
`*`(asterisk) Wildcard, indicating zero to many characters.
`|`(pipe) OR operand for dimension values.

Example showing fuzzy matching for three dimension value sets (test compute instances in fault domain 1 that use the`myshape`shape):

```

```

[Excluding Values](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)

Filter out (exclude) dimension values in an MQL expression.
Note  
  
Excluding values is available in MQL expressions only. In the Console, use Advanced mode.

In place of the equals sign (`=`) between the dimension name and set of values, use one of the following comparison operators.

Comparison operator Description
`!=`(exclamation point followed by equals sign) Not equal to. Use to filter out a single dimension value.
`!~`(exclamation point followed by tilde) Not equal to. Use to filter out multiple dimension values (when the expression uses wildcards or OR operands).

If using the`!~`comparison operator, then update the set of dimension values using one or more of the following characters.

Value Fuzzy Match Character Description
`*`(asterisk) Wildcard, indicating zero to many characters.
`|`(pipe) OR operand for dimension values.

Example 1 (Single Value): Basic query for CPU utilization, excluding fault domain 1.

```

```

Example 2 (Multiple Values): Basic query for CPU utilization, excluding fault domains 1 and 2.

```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-dimension.htm#)
- 

This section describes how to select dimensions on the Metrics Explorer page. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To select dimensions using Basic mode (default), provide values for the following fields:

Note  
  
Additional or other dimension fields appear for some metric namespaces. For example, a deployment type field appears for the`oci_autonomous_database`metric namespace. See the service-specific documentation for details.
- Dimension name : A qualifier specified in the metric definition. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.

To select a specific resource within the selected compartment, filter results by a resource-specific dimension, such as resourceDisplayName .
Note  
  

Long lists of dimensions are trimmed.
- To view dimensions by name, type one or more characters in the box. A refreshed (trimmed) list shows matching dimension names.
- To retrieve all dimensions for a metric, see[Listing Metric Definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm).
- Dimension value : The value that you want to use for the specified dimension, for example, the resource identifier for an instance.
- Additional dimension : Adds another name-value pair for a dimension.
- To select dimensions by updating the MQL expression, follow these steps:
- Select Advanced mode .
- Edit the text in the Query code editor box.

Dimension example in an MQL expression:
```

```

In this example, the query limits returned data to fault domain 1. The graph from[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example)now shows four metric streams. Each metric stream corresponds to an instance in fault domain 1.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to select dimensions (part of the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to select dimensions (part of the MQL expression). For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
