# Access Metrics for Oracle Analytics Cloud Using the Console (Metrics Explorer)
- Source: https://docs.oracle.com/iaas/analytics-cloud/doc/access-metrics-oracle-analytics-cloud-using-console-metrics-explorer.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-cloud/doc/access-metrics-oracle-analytics-cloud-using-console-metrics-explorer.html#dcoc-content-body)

# Access Metrics for Oracle Analytics Cloud Using the Console (Metrics Explorer)

You can use the Metrics Explorer in Oracle Cloud Infrastructure Console to monitor metrics for Oracle Analytics Cloud, and other resource types such as Oracle Cloud Database, virtual cloud network, and so on.

For Oracle Analytics Cloud, you can view charts that report how many errors occur connecting to your data sources and how much available query capacity you're using. If you check these metrics regularly, you'll learn to recognize trends as they develop and prevent problems in the future.
- In Oracle Cloud Infrastructure Console, click in the top left corner.
- Click Observability &amp; Management . Under Monitoring , click Metrics Explorer .
- In Compartment , select the compartment that contains the Oracle Analytics Cloud instance you're looking for.
- In Metrics namespace , select oci_analytics .
- In Metric name , select the metric you want to monitor.

- Query Capacity Usage (%) (PercentQueryCapacityUsed)
- Data Source Connection Errors (DataSourceConnectionErrors)

If required, edit the Interval and Statistic fields to change the aggregation window and aggregation function.
- In Dimension name and Dimension value , select resourceName and then select the name of the instance you want to view metrics for.
- Click Update Chart .

- Optionally, change the Start time and End time to view the metrics over a specific time range.

For general information about monitoring in Oracle Cloud Infrastructure, see[Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
