# Changing the Statistic for a Default Metric Chart
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-statistic.htm
- Fetched: 2026-09-05 02:40 CDT

# Changing the Statistic for a Default Metric Chart

Change the query's statistic used for aggregating data plotted on a default metric chart. Default metric charts are available on the Service Metrics page and resource details pages in the Console.

The statistic operates on the selected[interval](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/view-chart-interval.htm).

- View default metric charts in one of the following ways:
- [Open](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/view-chart-namespace.htm)the Service Metrics page.
- [Go to the Metrics area on the details page for a resource.
- For Statistic : Select the function to use to aggregate the data points.

- Mean - The value of Sum divided by Count during the specified time period.
- Rate - The per-interval average rate of change.
- Sum - All values added together.
- Max - The highest value observed during the specified time period.
- Min - The lowest value observed during the specified time period.
- Count - The number of observations received in the specified time period.
- P50 - The value of the 50th percentile.
- P90 - The value of the 90th percentile.
- P95 - The value of the 95th percentile.
- P99 - The value of the 99th percentile.

For information about directly editing MQL expressions or changing queries by using the CLI or API, see[Selecting the Statistic for a Query](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-statistic.htm). For more information about the statistic query component, see[Statistic](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../Reference/mql.htm#statistic)
