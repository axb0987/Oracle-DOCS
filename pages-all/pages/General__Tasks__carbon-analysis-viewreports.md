# Viewing Carbon Emissions Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-viewreports.htm
- Fetched: 2026-09-05 02:11 CDT

# Viewing Carbon Emissions Reports

View carbon emissions reports using the Console or the API.

## Using the Console

To view Carbon Emissions Analysis reports in the Console:

- Open the navigation menu and select Governance &amp; Administration . Under Emissions Management , select Carbon Emissions Analysis .

The Carbon emissions analysis page opens and displays the Location-based Carbon Footprint by Service default report with applied filters on the Report details tab.

You can create and save your own reports, which appear on the User Reports page. To view other predefined reports included in Carbon Emissions Analysis , which you can use as a template to create new reports, select Default Reports . The following included reports are available on the Default Reports page:
- Location-based Carbon Footprint by Service
- Market-based Carbon Footprint by Service
- Carbon Footprint by Service and Description
- Carbon Footprint by Service and SKU
- Location-based Carbon Footprint by Region
- Market-based Carbon Footprint by Region
- Carbon Footprint by Region
- In Applied filters , you can adjust any of the following report filters settings from the defaults by selecting Apply filter . For any filter, you can also can type the name of the preferred filter value.

Power-based and spend-based reports have a different set of applied filters. Spend-based reports have access to all filters, while power-based reports have a subset of these filters.

Spend-based report filters are the following:
- Date Range :
- Custom range : Select the starting and ending year and month (YYYY-MM format in UTC) from the Start month and End month fields. The default date range is 3 months.
- Last 7 days
- Last 2 weeks
- Last month
- Last 3 months
- Last 6 months
- Last year
- Availability domains
- Compartment
Note  
  
Filtering by compartment displays carbon usage attributed to all resources in the selected compartments.
- Platform : Gen_1 are services which aren't OCI native. Gen_2 includes all OCI native services.
- Product description (the human-readable corresponding product name)
- Region
- Service
- Subscription ID
- Tag
- Tenant

Power-based report filters are the following:
- Date Range :
- Custom range : Select the starting and ending year and month (YYYY-MM format in UTC) from the Start date and End date fields. The default date range is 3 months.
- Last 7 days
- Last 2 weeks
- Last month
- Last 3 months
- Last 6 months
- Last year
- Compartment
Note  
  
Filtering by compartment displays carbon usage attributed to all resources in the selected compartments.
- Region
- Service
- Tag
- Tenant

Filters are ORed within each specific filter, and ANDed between filters. For example, a filter for Service = Compute, Block Storage, Object Storage, Database, and tag`MyTag`displays data that's for (Compute OR Block Storage OR Object Storage OR Database) AND tag`MyTag`.

The Tag filter, however, is a unique case. You can add multiple Tag filters, which function as a joined OR.

For the Location-based Carbon Footprint by Service report on the main Carbon Emissions Analysis page, after Applied filters , each report has a settings summary with the following fields:
- Report template : Each report is based on one of included Default Reports templates.
- Calculation method : Power-based or spend-based.
- Carbon emissions factor : Market-based or Location-based.
- Grouping dimension : How the data is visualized in terms of a particular grouping. A grouping dimension by Service is displayed by default for the Location-based Carbon Footprint by Service report. Grouping dimensions change the way data is aggregated, but don't change the sum. If a resource doesn't have data for a particular field, a`0`value is displayed, which reflects the sum of those resources. Products which are GEN_1 often don't have an Availability domain, compartment, or resource ID. You can view only one grouping dimension at a time.

Depending on the report template, the following grouping dimensions are available:
- Availability domain
- Compartment
- Platform : GEN_1 are services which aren't Oracle Cloud Infrastructure native, while GEN_2 includes all native Oracle Cloud Infrastructure services.
- Region
- Resource id
- Service
- Service and description
- Service and sku
- sku part Number
- Sku roduct Description
- Subscription id
- Tag
- Tenant id
- Tenant name
- After adjusting any of the applied filters, the chart is regenerated with your chosen settings.

Under Carbon emissions by date (UTC) , the chart displays the selected data. The chart is organized in terms of the date (UTC) on the X-axis, and the carbon emission MTCO2e (Metric Tons Carbon dioxide equivalent) amount on the Y-axis. When viewing a chart, you can hover the mouse over a data point in the chart to see more details. The tip shows the data point details for the particular Y-axis item at a particular time, whether you're viewing the chart as either a Bars (the default) or Lines chart, which you can select from Chart type .

Chart granularity lets you select either Monthly (the default) or Daily .

In Chart scope , you can select the Cumulative option to change the values so that they're cumulative for the selected time period. For example, consider if you were looking at 10 months of data, cumulatively, and the values for each month are 5. In such a case, selecting Cumulative displays values of 5, 10, 15, 20, 25, 30, 35, 40, 45, and 50 across the 10 months. In a non-cumulative chart, the values display as 5, 5, 5, 5, 5, 5, 5, 5, 5, 5.

On the right side of the chart, the legend shows all the data by default, and each item is color-coded. You can select any of the legend items to switch the chart data on or off for that item. For example, when viewing a chart with various services and their emissions, the legend includes all the impacted services related to the query. Toggling one or more of the services shows or hides them dynamically from the chart output, but doesn't change the data shown in tabular view, nor in the downloaded CSV version.
- (Optional) You can download your carbon emissions data or view a tabular version of the chart from the Actions menu:

- Download data as CSV : Download a CSV file of the data. After confirming, you can then download a CSV file with the current date included in the file name (for example,`carbon-emission- <date> _ <time> .csv)`.
- View chart data in a table : Opens the View chart data in a table panel, where you can view the emissions data. Select Download table as CSV to also download the data.
- After viewing and then applying different filter settings, you can save your reports for later viewing by selecting Create new user report . See[Creating User Reports](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm)for more information.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the following[Usage API](https://docs.oracle.com/iaas/api/#/en/usage/)operations to manage Carbon Emissions Analysis:
- [RequestAverageCarbonEmission](https://docs.oracle.com/iaas/api/#/en/usage/latest/AverageCarbonEmission/RequestAverageCarbonEmission)
- [RequestCleanEnergyUsage](https://docs.oracle.com/iaas/api/#/en/usage/latest/CleanEnergyUsage/RequestCleanEnergyUsage)
- [RequestUsageCarbonEmissionConfig](https://docs.oracle.com/iaas/api/#/en/usage/latest/Configuration/RequestUsageCarbonEmissionConfig)
- [CreateUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/CreateUsageCarbonEmissionsQuery)
- [DeleteUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/DeleteUsageCarbonEmissionsQuery)
- [GetUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/GetUsageCarbonEmissionsQuery)
- [ListUsageCarbonEmissionsQueries](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/ListUsageCarbonEmissionsQueries)
- [UpdateUsageCarbonEmissionsQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionsQuery/UpdateUsageCarbonEmissionsQuery)
- [RequestUsageCarbonEmissions](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageCarbonEmissionSummary/RequestUsageCarbonEmissions)
