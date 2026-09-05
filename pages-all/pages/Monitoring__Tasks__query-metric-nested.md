# Nesting Queries in an MQL Expression
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-nested.htm
- Fetched: 2026-09-05 02:39 CDT

# Nesting Queries in an MQL Expression

Nest multiple queries in a single MQL expression for querying metric data in Monitoring.

In a nested query, the alarm portion appears at the beginning (surrounded with parentheses), followed by the optional group function and required statistic.

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm).

## Examples

Example 1: Sum of Hosts with CPU utilization Greater than 80 Percent
```

```
Example 2: Sum of Availability Domains with a Success Rate Lower than 0.99
```

```
Example 3: Count of Hosts with Up Time Greater than Zero
```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-nested.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-nested.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-nested.htm#)
- 

This section describes how to nest queries within a single MQL expression on the Metrics Explorer page. Nesting is available in Advanced mode (MQL) only. For alarm query edits, see[Editing the MQL Expression When Creating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select Advanced mode .
- Edit the text in the Query code editor box.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to nest multiple queries (within the MQL expression).

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`
