# Editing the MQL Expression for a Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm
- Fetched: 2026-09-05 02:39 CDT

# Editing the MQL Expression for a Query

Directly edit the MQL expression used to query metric data in Monitoring.

For an example MQL expression, see[Example Query and Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-landing.htm#example). For information about all query elements, including compartment and metric namespace, see[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm). For troubleshooting, see[Troubleshooting Monitoring](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../troubleshooting.htm)or[Troubleshooting Queries](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../troubleshooting-queries.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm#)
- 

This section describes how to edit the MQL expression on the Metrics Explorer page. The MQL expression is available in Advanced mode only. For alarm query edits, see[Creating a Basic Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm).

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- Select Advanced mode .
- Edit the text in the Query code editor box.
- Select Update Chart .
- 

Use the[oci monitoring metric-data summarize-metrics-data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric-data/summarize-metrics-data.html)command and required parameters to query metric data. Use the`--query-text`parameter to specify the MQL expression.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[SummarizeMetricsData](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)operation to query metric data. Use the`query`attribute to specify the MQL expression. For an example, see[SummarizeMetricsDataDetails](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)
