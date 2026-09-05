# Creating a Basic Query
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm
- Fetched: 2026-09-05 02:39 CDT

# Creating a Basic Query

Select the minimum required query configuration on the Metrics Explorer page in the Console to view a custom metric chart.

Note  
  
To start with a predefined service query, see[Viewing and Updating the Query for a Default Metric Chart](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-explore.htm).

- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Metrics Explorer .
- In the navigation bar, select the region that contains the metric data that you want.
For more information about regions, see[Understand Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/applications-home-page.htm#apps-understand-regions)and[Working Across Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Working).
- In the query area under the chart, select values for Metric namespace and a Metric name , which are the minimum required values needed to view a metric chart.
If you don't see the query area, select Edit queries .
- Select Update Chart .
The chart shows metric data for the selected metric namespace and metric name, using default values for interval and statistic.
- To change the metric chart, update the query values and then select Update Chart again.
For reference, see[Creating a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric.htm).

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Editing the MQL Expression for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-mql.htm).

For query troubleshooting, see[Troubleshooting Queries](https://docs.oracle.com/iaas/Content/Monitoring/troubleshooting-queries.htm)
