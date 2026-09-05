# Cost Analysis
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm
- Fetched: 2026-09-05 01:43 CDT

# Cost Analysis

Cost Analysis is an easy-to-use visualization tool to help you track and optimize your Oracle Cloud Infrastructure spending. You can generate charts, and download accurate, reliable tabular reports of aggregated cost data on your Oracle Cloud Infrastructure consumption.

Use Cost Analysis for spot checks of spending trends and for generating reports. Common scenarios you might be interested in include:
- Viewing monthly costs for compartment X and its children, grouped by service or by tag.
- Viewing daily costs for tag key A and tag key B, values X, Y and Z, grouped by service and product description (SKU).
- Viewing hourly costs for service = compute or database, grouped by compartment name.

You can choose from one of the predefined, default reports from the Reports menu, and you can choose the dates you're interested in. By default, the Costs by Service report is shown when the Cost Analysis page first opens. Use the Filters menu to filter by the specific tags, compartments, services, or other filter you want, and pick how you want it grouped using the Grouping dimensions menu. As a result, a chart and corresponding data table are generated, and can also be downloaded as a CSV data table, PDF, or chart image. You can also save a custom set of dates, filters, and grouping dimensions into a[saved report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports). Up to 10 custom reports can be saved, and on each saved report, you can add up to five[custom tabs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#adding_custom_tabs), which allow you to create custom charts and tables of cost data using different combinations of grouping dimensions. See[Cost Analysis Query Fields](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields)and[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)for more information on the related Cost Analysis query settings. You can also[estimate](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#forecasting_costs)future usage and consumption information, based on past usage data.

If you want to re-create the breakdown provided by the former Classic Version of the Cost Analysis tool, apply the SKU (Part Number) grouping dimension in the current version of Cost Analysis. To explore your costs in new ways, we recommended viewing your costs based on Service , or Service and Product Description . If you are doing cost tracking, we recommended grouping by Compartment or Tag .
Note  
  
Costs for tags are based on the date at which the tag was associated with a resource. It does not work retroactively for resources on which these tags are applied.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

To use Cost Analysis, the following policy statement is required:
```

```

To use[Saved Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports), the following policy statement is required:
```

```

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Cost Analysis Query Fields

The following table describes the Cost Analysis query fields.

Field Description
Reports Select from one of the Default Reports :
- Costs by Service (shown by default when the Cost Analysis page first opens)
- Costs by Service and Description
- Costs by Service and Sku (Part Number)
- Costs by Service and Tag
- Compute Costs by Compartment
- Monthly Costs

After you have created some[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports), they are listed in this menu under Saved Reports .
Start/End Date (UTC)

Select the start and end date according to the UTC time zone.
After clicking either of the calendar icons, you can also query and select predefined time ranges for data available in the usage store:
- 7D
- 10D
- MTD
- 2M
- 3M
- All Data
- 6M
- YTD

These preset time ranges are crucial for[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports), because they will automatically change the time range every time a saved report is launched. For example, if the current date was March 18, and you created a saved report with 7D as the time period, the report shows data from March 11 to March 18. When you launch the same report the next day (March 19), the date range switches to March 12 to March 19. Lastly, when setting the time period, it is also indicated above the chart in Time Period .

Note: Historical data is currently being back-filled for tenancies and may not appear immediately. As the process completes, up to twelve months of past consumption data will become available.
Granularity

Granularity (hourly, daily, monthly) is based on the requested date range size. The logic is the following:
- Hourly: 24 hours or less (only shown when you select a Start Date and End Date with the same day). You can only query at daily granularity where today - start date &lt;= 31.
- Daily: &gt; 24 hours, &lt;= 3 months
- Monthly: You can only query for end date - start date &lt;= 12 months .
Show

Allows you to view the report in terms of Cost (the default) or Usage .

For a virtual machine cluster with pluggable databases, select Attributed cost or Attributed usage . Otherwise, for all other resources, use Cost or Usage . Also, selecting Attributed cost or Attributed usage for any non-VM cluster resource generates the same output as Cost or Usage . For more information, see[Viewing Cost and Usage from Virtual Machine Cluster Pluggable Databases](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#view_vmclusterpdb_costusage).
Show Forecast Allows estimating future usage and consumption information, based on past usage data. See[Forecasting Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#forecasting_costs)for prerequisites and usage information. When Show Forecast is selected, the End Date (UTC) field changes to End Forecast Date (UTC) .

Note: When viewing forecast data, you can choose dates from End Date (UTC) after the current day, but you can not do this when Show Forecast isn't selected.
Cumulative Select this option to change the values so that they're cumulative for the selected time period. For example, consider if you were looking at 10 days of data, cumulatively, and the values for each day are $5. In such a case, selecting Cumulative displays values of 5, 10, 15, 20, 25, 30, 35, 40, 45, and 50 across the 10 days, respectively. In a non-cumulative chart, the values display as 5, 5, 5, 5, 5, 5, 5, 5, 5, 5.
Filters

Allows filtering on the following:
- Availability Domain
- Compartment

Note: Filtering by compartment displays usage and costs attributed to all resources in the selected compartments.
- By name
- By OCID
- By Path (for example, root/compartmentname/compartmentname)
- Platform : GEN_1 are services which aren't OCI native. GEN_2 includes all OCI native services.
- Tag
- Tag Namespace
- Tag Key + Match any value or Match any of the following
- Region
- Service
- Subscription ID
- Resource OCID
- Product description (the human-readable corresponding name)
- SKU (Part Number) (for example, B91444)
- Tenant
- Unit

See[Filters](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Filters)for more information on adding, editing, and removing filters, and filter logic.
Grouping Dimensions

Allows visualizing the data in terms of the particular grouping. A grouping dimension by Service is displayed by default. You can view only one grouping dimension at a time.
- Availability Domain
- Compartment . When you group by compartment, you can pick the display name value, and a compartment depth. The compartment depth corresponds to the lowest level you want the compartments to be grouped by. All levels above that grouping level return what is directly in those compartments. The grouping level returns values for all resources in those compartments, plus all resources in compartments below it.
- Display as
- Compartment Name
- Compartment OCID
- Compartment Path

Note: If Compartment OCID is selected, you can't view Compartment Level .
- Compartment Level
- All (the default): Every compartment is displayed. Values would display usage/spend associated only with the resources in that specific compartment.
- Level 1 (root only): Only 1 column is returned (root), and values for resources contained in root and every child compartment are displayed.
- Level 2 (root/&lt;value&gt;): Displays root, with values for root equaling only those resources in root. All compartments that are direct children of root are also returned. The values for each of those compartments is the sum of all resources therein, or within any children of those compartments.
- Level 3 (root/&lt;value&gt;/&lt;value&gt;): Returns root, with values for root equaling only those resources in root. All Level 2 compartments are also returned, but with values only equal to the resources contained in each of those specific compartments. The first child level of the level 2 compartments are also returned. The values for the third level of compartment (root/child1/child2) would be equal to the resources in those compartments, plus all the resources in all the children of those compartments.
- Level 4 (root/&lt;value&gt;/&lt;value&gt;/&lt;value&gt;)
- Level 5 (root/&lt;value&gt;/&lt;value&gt;/&lt;value&gt;/&lt;value&gt;)
- Platform : GEN_1 are services which aren't Oracle Cloud Infrastructure native, while GEN_2 includes all native Oracle Cloud Infrastructure services.
- Region
- Resource OCID
- Service
- Service and Product Description
- Service and SKU (Part Number)
- SKU (Part Number)
- SKU (Product Description)
- Subscription ID
- Tag
- Tag Namespace
- Tag Key
- Tenant ID
- Tenant Name

See[Grouping Dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)for more information on viewing and changing grouping dimensions.

## Viewing and Working with the Chart Data

When the Cost Analysis page first opens, the default view is to show the Costs by Service report, grouped by Service and with Daily granularity. The default date range is from the first day of the month to the current day. The Cost Analysis chart is organized in terms of the date (UTC) on the X-axis, and the cost amount on the Y-axis. When viewing a chart, you can hover the mouse over a data point in the chart to see more details. The tooltip shows the cost value summary for the particular Y-axis item at a particular time, whether you're viewing the chart as either a Bars (the default), Lines , or Stacked Lines chart.
Note  
  
[Custom tabs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#adding_custom_tabs)can only display bar charts.

You can start by viewing the chart data in terms of the predefined reports, by selecting one from the Reports menu, and then adjust the date range, granularity, and then add or remove[filters](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Filters)and[grouping dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)(or both, that is, view the cost data according to one or more filters, or in terms of both filters and a single grouping dimension).

You can also save your adjustments as a saved report that you can view later, alongside the predefined reports. See[Saving Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)for more information on saving reports.

To the right of the chart, the Legend box shows all the data by default, and each item is color-coded. You can click any of the Legend items to switch the chart data on or off for that item. For example, when viewing a chart with various services and their costs, the Legend box includes all the impacted services related to the query. Toggling one or more of the services shows or hides them dynamically from the chart output. Toggling the Legend data, however, doesn't change the data shown in the table view, or what is downloaded.

A tabular view of the chart is also provided under the chart, which is updated as you apply different time period, filtering, and grouping dimension options. When viewing the table data, you can click any of the column headers to sort in ascending or descending order.

To help find out what is driving costs, see the following topics:
- [Using Multiple Filters to View Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#use_multifilters_view_costs)
- [Identifying a Resource that is Consuming Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#identifying_resource_consume_costs)
- [Grouping by Service and SKU, or Service and Product Description to Identify Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupby_service-sku_proddescrip_id_costs)
Note  
  
Data can take up to 48 hours to appear in Cost Analysis.

## Viewing Query History

You can view your Cost Analysis query history at any time by clicking the Query History link at the top of page. After clicking this link, the Oracle Cloud Infrastructure Logging[Audit](https://docs.oracle.com/iaas/Content/Logging/Concepts/audit_logs.htm)page opens.

The Audit page is pre-filtered to show the Cost Analysis-related audit events.

Under the Explore events tab, you can view the query parameters from any Cost Analysis query event, which are of the`com.oraclecloud.UsageApi.GetUsage`type. Expand the JSON view for an event entry to view the query parameters, which are available under the`"additionalDetails"`node.

The following are the query fields that are displayed:
- endTime
- granularity
- queryType
- startTime
- tenantId

For example:
```

```

## Filters

See the following for instructions on how to add, edit, and remove filters, as well filter logic.

[To add filters](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Start/End Date (UTC) , select a time period.
- From Show , select whether you want to view Cost or Usage .
- From Filters , select a filter. A dialog specific to the chosen filter is displayed. For example, if you chose Service , select a service from the list. You can add several services if preferred, or select the X icon to remove service filters. Select Select when you're finished selecting filtering criteria.
- Select Apply to apply the changes and reload the chart and table with the selected filters.

[To edit a filter](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- To edit the filter after it has already been applied to the chart, click the filter. The filter's dialog box is displayed.
- From the filter dialog menu, select one or more filters, and click Select .
- Click Apply to apply the changes and reload the chart and table with the selected filters.

[To remove a filter](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- To remove the filter after it has been applied to the chart, click Clear all filters , or click the filter's X icon next to Filters .
- Click Apply to apply the changes and reload the chart and table without the selected filters.

[To filter costs by dates](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Reports , select one of the predefined reports,[or create a new one](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports).
- In Start date (UTC) , select a start date.
- In End date (UTC) , select an ending date.
Note  
  
Historical data is currently being back-filled for tenancies and may not appear immediately. As the process completes, up to twelve months of past consumption data will become available.
- Click Apply .

[To filter costs by tags](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Reports , select one of the predefined reports,[or create a new one](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports).
- From Filters , select the Tag filter.
- In the Tag dialog box, complete the following. See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)for descriptions of these fields.
- 

Tag Namespace
- 

Tag Key
- 

Tag Value
- Click Select .
- Click Apply .

[To filter costs by compartments](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Filters , select the Compartment filter.
- In the Compartment dialog box, under Filter Compartments , select a compartment filtering option:
- By name
- By OCID
- By Path (for example, root/compartmentname/compartmentname)
Note  
  
Filtering by compartment displays usage and costs attributed to all resources in the selected compartments, and their child compartments.
- Click Apply .

[To remove a compartment or tag filter](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- When you filter costs, a label appears next to Filters with the name of the tag or compartment filter. To clear the filter, click the X icon, or click Clear all filters .

### Filter Logic

Filters are ORed within each specific filter, and ANDed between filters. For example, a filter for Service = Compute, Block Storage, Object Storage, Database, and Tag = Tag Key "MyKey" displays data that is for (Compute OR Block Storage OR Object Storage OR Database) AND Tag Key "MyKey".

The Tag filter, however, is a unique case. You can add multiple Tag filters, which function as a joined OR.
Note  
  
Only ten Tag Key values are retrieved and shown in the list when you try to select a possible Tag Key value. Or, you can manually type in the Tag Key value you want to filter on.

### Using Multiple Filters to View Costs

You can start by filtering the Cost Analysis chart data based on a single filter, and then add additional filters. For example:

- Set your[Grouping Dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)to Service , to view your costs by service.
- From Filters , add a filter by Tag .
- Select a Tag Namespace (this example uses "Financial" as the selected namespace).
- Select a Tag Key (this example uses "Owner" as the selected key).
- Specify whether to Match any value (AND condition), or Match any of the following (OR condition).

For example, assuming the value "alpha" is the value, and if Match any of the following is chosen, it means show all services that have "alpha" as the owner. Conversely, assuming multiple values "alpha" and "beta" are chosen, and if Match any of the following is selected, this corresponds to an OR condition (meaning, filter to show the costs from all the services from the "Financial" namespace, with the Tag Key "Owner", that matches either the "alpha" or "beta" values).
- Click Select , then Apply to reload the Cost Analysis chart with the filtered information.

You can also add another filter by tag, to break the data down further. For example:
- From Filters , add a filter by Tag .
- Select a Tag Namespace and Tag Key (for example, the "Cost Center" namespace).
- Select Match any of the following , and for example, filter for any "Cost Center" values of "1234" or "5678".

After clicking Select , then Apply , this filter shows the costs from all the services with the tag filter you just created, plus this second tag filter ("Financial" namespace, Tag Key "Owner", "alpha" or "beta" values + "Cost Center" namespace with the values of "1234" or "5678"). The two tag filters together amount to an AND with the previous filter (the two filters are shown adjacent to the Add Filter drop-down list).

Alternatively, instead of the second Tag filter ("Cost Center" namespace with the values of "1234" or "5678"), you could add a Service filter (NETWORK), and that would show the costs from all the services from the "Financial" namespace, with the Tag Key "Owner", that matches both the "alpha" or "beta" values, and is filtered by the NETWORK service type.

## Grouping Dimensions

Grouping dimensions change the way data is aggregated, but don't change the sum. If a resource doesn't have a value for a particular field, a "no value" column is displayed, which reflects the sum of those resources. Products which are GEN_1 often don't have an Availability domain, compartment, or resource ID.

[To view grouping dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Start/End Date (UTC) , select a time period.
- From Show , select whether you want to view Cost or Usage .
- From Grouping Dimensions , select the preferred grouping dimension. If Compartment or Tag is chosen, additional compartment or tag selection fields appear.
- Click Apply to apply the changes and reload the chart and table with the selected grouping dimension.

[To change a grouping dimension](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- To change the grouping dimension, select it from Grouping Dimensions .
- Click Apply to apply the changes and reload the chart and table with the new grouping dimension.

### Identifying a Resource that is Consuming Costs

If you have noticed a large amount of, for example, Database service usage that has appeared in a chart, and you wanted to identify which resource was responsible, you can group by Resource OCID from the Grouping Dimensions list. Next, from Filters , add a filter for the service type ( Database in this example), and click Apply to reload the chart.

The chart reloads to show which resource OCIDs were driving the Database cost, both when hovering over the data point in the chart, and in the Legend box. These resource OCIDs are also displayed in the data table below the chart. If desired, you can save this information by clicking Tab Actions , and then selecting Download Table as CSV or Download Chart .
Tip  
  
The Legend box is set to a default size when the charts first loads, but you can click and drag the box to more easily read lengthy items within the box (such as OCIDs).

To find more information about the resource, copy the OCID and enter it in the Console's[Search](https://docs.oracle.com/iaas/Content/Search/Tasks/queryingresources.htm)box, to pinpoint which resource is driving costs.

### Grouping by Service and SKU, or Service and Product Description to Identify Costs

In some instances you may see multiple SKU numbers for a service. When grouping by Service and SKU (Part Number) , multiple SKU numbers for the same service appear in the Legend box. For example, if you had multiple Compute entries in the Legend box but they have different SKUs, it means there is one resource using multiple underlying infrastructure components. This case is actually most common for Block Storage (where multiple Block Storage entries appear with different SKUs). Specifically, for the Block Storage case, you are charged for storage itself, but you are also charged for any data transfers out of Block Storage. As a result, you will see multiple "Block Storage" items listed with different SKU numbers in the Legend box. For example:
```

```

Another way of looking at this same type of data is to use the Service and Product Description grouping dimension. The Legend box is sorted in the same manner, but presents the data differently. That is, according to the actual product descriptions, versus the SKUs that these are associated with. For example:
```

```

Tip  
  
By default, these longer descriptions may not be visible, and so you should resize the Legend box to view them.

The Database service is also a useful example. There could be different instances of a database and you could also be charged for Block Storage within the Database service. For example, this entry could appear in the Legend for such a case:
```

```

You could also be charged in the Database service for network transfer. For example:
```

```

Charges for licensing of the application version can also occur:
```

```

[Cost and Usage reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm)are a good way to further slice such information you have noticed in the Cost Analysis charts. For example, in a cost report you might notice a SKU number that's associated with Compute, and also see the same SKU number that's associated with Block Storage. As a result, you may wonder if you were double-billed (though this is actually not the case). To investigate the actual cost, you can first filter the cost CSV spreadsheet by the SKU . Once you have applied a filter to the CSV using a particular SKU, you can see which services are consuming from the product/Description column. For example, a SKU could be using a lot of "Block Volume - Performance Units", but you also notice that "DBaaS - Attached Block Storage Volume" appears in this column.
A way to further segment the data would be to copy the resource ID from the product/resourceId column, of say the "DBaaS - Attached Block Storage Volume" entry you noticed amongst all the "Block Volume - Performance Units", and remove the SKU filter you applied previously. Next, filter the spreadsheet based on the resource ID instead. This then shows all the components (indicated in the product/Description column) that the particular resource ID is consuming.
Note  
  
When viewing a cost report, the cost/productSku and product/Description columns map to one another, and are adjacent columns in the CSV. For more information on these fields and other fields that appear in the reports, see[Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm). Similarly, you can use Cost Analysis to do a Resource OCID grouping dimension, with a Product description filter, to show all the resources that are using a particular product. For example, if you choose Block Volume Performance Units as the filter, the Cost Analysis chart shows which resources are using Block Volume Performance Units. See[Identifying a Resource that is Consuming Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#identifying_resource_consume_costs)for more information on identifying the particular resource(s).

## Downloading Your Cost Details Data

From the Tab Actions menu on any Cost details tab:
- Select the Download table as CSV option to download a CSV file of the data from the current Cost details tab. In the Export Confirmation that opens, click Confirm . You can then download a CSV file with the current date included in the file name.
- Select Download current tab as PDF option to export the chart and table data to PDF. In the Export Confirmation that opens, click Confirm . You can then save a PDF file with the Cost details by date tab name, along with the current timestamp included in the PDF file name.
- Select Download chart to download a PNG image of the chart from the current Cost details tab, with the current date included in the file name. The chart image includes the legend items, and reflects the selected time range, applied filters, and grouping dimensions.

## Saving Reports

Use the Report actions menu in Cost Analysis to create a saved report. You can later access the report after leaving the Console and returning to Cost Analysis, without needing to respecify your set of dates, filters, granularity, or grouping dimensions. After a report has been saved, it can later be renamed, updated, or deleted. A maximum of 10 reports can be saved.

You can create a saved report by modifying one of the predefined Cost Analysis reports, and then save your custom settings as a new report. Your new reports can have your own set of filters, grouping dimensions, granularity, and date range settings.

To save reports, ensure you also have the correct policy. See[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#policy)for more information.

To save a Cost Analysis report:

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Reports , select one of the predefined reports, or use the default Costs by Service report.
- Make your preferred query adjustments. See[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data),[Filters](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Filters), and[Grouping Dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)for more information on query settings. Also see[Cost Analysis Query Fields](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields)for an explanation of the Cost Analysis query interface and its fields and possible values.
- After you have made changes, the currently selected predefined report name from the Reports menu changes to (edited).
- If you're done making changes and want to save a new report, click Save as new report .
- In the Save as new report dialog, enter the report name in the Name field. Avoid entering confidential information..
- Click Save .

A notification is displayed that your report has been saved, and the report is also selected in the Reports menu.
- If you didn't already apply your custom report settings, click Apply to view your changes.

The new saved report is now available for future selection from the Reports menu under Saved Reports . You can also use the Scheduled Reports page to run a saved report based on a schedule. See[Scheduled Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/scheduledreportoverview.htm)for more information.
Note  
  
When the ten-report limit has been exceeded, you must select a pre-existing report from the Overwrite existing report box that you want to be overwritten with the new one.

After a report has been saved, you can rename it, reset in-progress changes, update it, or delete it.

[To rename a report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report from the Reports menu.
- From Report actions , select Rename . The Edit report name dialog is displayed.
- In Name , enter the new report name, and click Save . A notification is displayed that the report has been updated and renamed.

[To reset report changes](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report from the Reports menu.
- After making changes that you want to revert, from Report actions , select Reset . The (edited) text next to the report name disappears, to indicate that you have reset the report back to its original state.
- Click Apply to reload the chart and table data.

[To update a report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report from the Reports menu.
- Make the preferred changes to dates, filters, granularity, or grouping dimensions.
- From Report actions , select Update . A notification is displayed that the report has been successfully updated.
- Click Apply to reload the chart and table data.

[To delete a report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report from the Reports menu.
- From Report actions , select Delete . A delete confirmation is displayed.
- In the confirmation, click Delete to delete the report. A notification is displayed that the report has been deleted and the associated chart and table data disappears.
- Select another report from the Reports menu or create a new custom report.

### Adding Custom Tabs to Reports

By default, Cost Analysis displays time series-based charts and tabular output. With custom tabs, you can customize the reports by adding extra tabs with both chart and tabular output, based on your preferred combination of grouping dimensions.
For example, if you are interested in compartments and service type, you could create a custom query that shows the mapping of compartment to service in the same chart and tabular output format that Cost Analysis generates in all of its predefined reports. Any custom tabs you create can only be saved in one of your[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports). You can start by selecting one of the predefined Cost Analysis reports, add the custom tabs (up to a maximum of five custom tabs can be saved in a[saved report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)), and then save the report. Since you can save a maximum of 10 total reports, you could have up to 50 custom tabs in total (saved among 10[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)).
Note  
  
If you navigate away from the Cost Analysis section of the Console and don't save your custom tabs to a saved report, or if you sign out and don't save them, they will not be available when you return to Cost Analysis.
To add a custom tab:

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- From Reports , select one of the predefined reports, or use the default Costs by Service report.
- In the Cost details chart, next to the Cost details by date tab , click +Add Tab . The Add Custom Tab panel is displayed.
- In Name , enter a name for the custom tab. Avoid entering confidential information.
- In Table Rows , under Grouping dimension , select a grouping dimension that will correspond to the X-axis (row) data in the chart and table.
Select from the following grouping dimensions:
- Availability Domain
- Compartment
- Platform
- Region
- Resource OCID
- Service
- Service and Product Description
- Service and SKU (Part Number)
- SKU (Part Number)
- SKU (Product Description)
- Subscription ID
- Tag (allows entering the Tag Namespace and Tag Key when selected)
- Tenant ID
- Tenant Name
- In Table Columns , under Grouping dimension , select a grouping dimension that will correspond to the Y-axis (column) data in the chart and table. The grouping dimensions you can choose are the same as the grouping dimensions that can be chosen for Table Rows in the previous step (though you cannot, however, choose the identical grouping dimension to be the grouping dimension for both the row and column simultaneously).
- Click Add . A notification is displayed that your custom tab was created, and the new tab with its new chart and table, appear under Cost details . A notice is also displayed on the tab that states, "Tabs cannot be saved to a system report. Save as a new report to continue to be able to view this tab in future sessions." You can click the adjacent Save as New Report button embedded in the notice, or click the same button at the top of the Cost Analysis page under Reports .
- Click Save as New Report . The Save as New Report box is displayed.
- In Name , enter a saved report name, and click Save . For the name, avoid entering confidential information. A notification is displayed that your report has been saved, and the saved report is also selected in the Reports menu.

The custom tab and custom report are now saved. The new tab's chart and tabular data output is available for analysis (also see[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)).

For example, if you wanted to view which services were driving costs by region, select Region as the Table Rows , and Service in the Table Columns settings for the custom tab. Under Costs by Region , the X-axis of the chart would display the regions, in terms of the service usage, while the Y-axis displays the costs. Under Details , the tabular output lists each region in each row of the table, while each column displays each service's costs for the particular region.

After the custom tab is saved, you can add more tabs (up to five total per report), edit or delete the tab, or[download the data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Download_Your_Data)from the custom tab.

[To add more tabs to a report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

Follow the same steps for adding a new custom tab. When a new tab is created, it is added automatically to the saved report you are working with.

[To edit a tab](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report with your custom tabs from the Reports menu.
- Under Cost details , click the custom tab.
- If required, make any changes to dates, filters, or granularity. Grouping dimensions cannot be changed since they are determined by the custom tab settings.
- From Tab Actions , select Edit Tab . The Name , Table Rows , and Table Columns fields can be modified.
- Click Save . A notification is displayed and the custom tab data is refreshed to display your changes.

[To delete a tab](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

- Select the report with your custom tabs from the Reports menu.
- Under Cost details , click the custom tab.
- From Tab Actions , select Delete . A Delete Custom Tab delete confirmation is displayed.
- To delete the tab, click Delete . A notification is displayed that the tab has been deleted.

## Forecasting Costs

You can use Cost Analysis to estimate future usage and consumption information, based on past usage data.

Note  
  
Forecasted values are just estimates based on past usage trends, and likely to differ from actual usage.

See[Cost Analysis Query Fields](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields)for a description of the Cost Analysis search settings, and[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)for more information on performing searches.
Note  
  
Forecasting is currently not supported with[custom tabs](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#adding_custom_tabs). If a forecasted time range is used on the Cost details by date tab, it gets reverted to a query till &lt;date&gt; without forecasting.

Forecasting in Cost Analysis has the following characteristics:

- Exponential smoothing is used for forecasting.
- You need at least ten days of historical data to be able to do forecasting with Daily granularity. The date range fields ( Start/End Date (UTC) ) adjust accordingly to this.
- You need at least three months of historical data to do forecasting with Monthly granularity. As with Daily granularity, the date range fields ( Start/End Date (UTC) ) adjust accordingly.
- You can only forecast to the extent you have actual usage. For example, if you only have 15 days of historical data, you can only forecast for 15 days. If you have only four months of data, you can forecast only for four months in the future.
- The maximum limit for forecasting with Daily granularity is 93 days. The Monthly forecasting maximum limit is 12 months.
- Since there is a built-in 24-hour delay, the most recent 24 hours are always forecast. Similarly, in monthly forecasting mode, the current month is always forecast, irrespective of how far the current month has progressed.
- You can only do forecasting from continuous dates with actual usage. Namely, if today is March 26, your date range must start with at least March 24.

To view forecast costs:

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- Optionally, modify any search parameters, and then select Show Forecast . You can also select Show Forecast first, and then select search settings. In either case, you can view forecast data.
- Click Apply .

The chart reloads with the forecast data. For all chart types (whether Bars , Lines , or Stacked Lines ), a Forecast section is displayed (in a grayed out portion) in the right-most end of the chart. In addition, a Total (includes forecast) cost total field is added to the top of the chart, after the Time Period and Cost To Date fields. Lastly, the forecast data is also displayed in the tabular view of the chart (the forecast columns are added as grayed out rows).

You can choose to save your settings, including the forecast data, as a[saved report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports). You can also[download](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Download_Your_Data)a CSV file of the data, or a PNG file of the chart, which includes the forecast data.

## Viewing Subscription Details and Costs

Tenancies can view their subscription details, depending on the type of tenancy. You can also use the Subscription ID grouping dimension to view costs in terms of a tenancy's subscription.

You can view the details of your subscription, but only for certain types of tenancies:
- If a tenancy is a parent tenancy in an[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm), then a View subscription details link is available at the top of the Cost Analysis page, which allows you to view subscription details for the parent and any child tenancies.
- If a tenancy is a child tenancy in an[organization](https://docs.oracle.com/iaas/Content/General/Concepts/organization_management_overview.htm), then no such link is available, since child tenancies cannot view their subscription details in Cost Analysis.
- If a tenancy is a standalone tenancy that is not part of an organization, then the View subscription details link is available. You can view subscription details, similar to parent tenancies that are in an organization, with some minor differences.

After clicking View subscription details for an eligible tenancy, the Subscription Details panel is displayed, with the details listed in tabular format. The table has the following fields:
- Subscription ID
Note  
  
For parent tenancies in an organization only. This field is not present for a standalone tenancy.
- Type
- Start Date
- End Date
- Commitment ( &lt;currency&gt; )
- Consumption ( &lt;currency&gt; )
- Balance ( &lt;currency&gt; )
- Days elapsed in billing

When viewing the Subscription Details panel for a parent tenancy in an organization, the first row in the table corresponds to the parent tenancy's subscription, while subsequent rows correspond to child tenancy subscriptions. The Subscription Details panel, meanwhile, for a standalone tenancy only has a single row that displays the subscription detail information for the standalone tenancy.

### Viewing Costs by Subscription

You can use the Subscription ID[grouping dimension](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)to filter by a specific subscription and determine which subscription a tenancy's usage was attributed against. As a result, you can[view](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)the costs associated with a particular subscription (for the standalone tenancy case), or the costs for multiple subscriptions (for the parent tenancy with child tenancies case). The subscription IDs are indicated on the X-axis of the chart, and are also listed in the Legend box.

For example, using the default Costs by Service report, and ensuring to select Subscription ID as the[grouping dimension](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension), the Cost Analysis[chart and table](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)can display costs by one or more subscription IDs. Later you can[save a custom report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports)that focuses on such subscription ID usage.

For more information, see[Cost Analysis Query Fields](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields),[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data), and[Grouping Dimensions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension).

## Viewing Cost and Usage from Virtual Machine Cluster Pluggable Databases

You can use Cost Analysis and OCI proprietary[Cost Report Types](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports)to view the cost and usage for pluggable databases within a virtual machine cluster.
Note  
  
In Cost Analysis, querying a date range before the availability of this feature returns null values.

To view pluggable database costs in Cost Analysis:
- Complete the Prerequisites described for[Oracle Databases on Exadata Cloud Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/manage-databases.html#GUID-B7800AC7-8616-40CD-B0AC-7E28ECC56B55)and[Oracle Exadata Database Service on Cloud@Customer](https://docs.oracle.com/en/engineered-systems/exadata-cloud-at-customer/ecccm/ecc-manage-databases.html#GUID-AE3C2F04-1F94-487E-B15B-F05292CC7F24).
- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Analysis .
- See[Cost Analysis Query Fields](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields)and[Viewing and Working with the Chart Data](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Viewing_and_Working_with_the_Chart_Data)for an orientation to the query fields, the Cost Analysis interface, and information on creating reports.
- Select a preferred start and end date, and granularity.
- From Show , select Attributed cost .
- From Filters , select Tag .
- In the Tag window, select the orcl-cloud tag namespace, parent_resource_id_1 tag key, and after selecting Match any of the following , enter the virtual machine cluster OCID.
- Select Select .
- From Grouping dimensions , select Resource OCID .
- Select Apply .

The chart and table on the Cost details by date tab displays the pluggable database costs.

The chart Legend shows the parent virtual machine cluster and each pluggable database. In the chart, you can only visualize the cost data for each pluggable database returned by the report query (the parent virtual machine cluster itself doesn't appear, only the pluggable databases).

In the Details table, you can view the cost data for each pluggable database by date.

To view pluggable database costs in[Cost Report Types](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports):
- Follow the instructions in[Downloading a Cost Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/../Tasks/download-cost-usage-report.htm)to download the cost report.
Note  
  
Virtual machine cluster pluggable database costs aren't supported in FOCUS cost reports, and are only available in OCI proprietary cost reports. For more information, see[Cost Report Types](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costusagereportsoverview.htm#costreports).
- 

In the cost report CSV, you can filter the`tags/`column by the virtual machine cluster OCID, and the`lineItem/intervalUsageStart`column by a particular date.
The cost report indicates the total cost for the parent virtual machine cluster and its pluggable databases. For the parent virtual machine cluster, the total costs are shown in the`cost/myCost`column. The`cost/attributedCost`and`usage/attributedUsage`columns in the parent virtual machine cluster row indicate a value of zero, while the individual cost values for each pluggable database under the virtual machine cluster are split under the`cost/attributedCost`and`usage/attributedUsage`columns.
Note  
  
The`cost/attributedCost`and`usage/attributedUsage`columns aren't present in cost reports that were generated before the availability of this feature.

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations to manage usage:
- [UsageSummary](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageSummary)
- [RequestSummarizedUsages](https://docs.oracle.com/iaas/api/#/en/usage/latest/UsageSummary/RequestSummarizedUsages)

Use the following operations to manage[saved reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#saving_reports):
- [CreateQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/Query/CreateQuery)
- [DeleteQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/Query/DeleteQuery)
- [GetQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/Query/GetQuery)
- [ListQueries](https://docs.oracle.com/iaas/api/#/en/usage/latest/Query/ListQueries)
- [UpdateQuery](https://docs.oracle.com/iaas/api/#/en/usage/latest/Query/UpdateQuery)
The[Usage API](https://docs.oracle.com/iaas/api/#/en/usage/)allows retrieval of usage and cost data. You can:
- Query based on different granularity, for example, MONTHLY or DAILY.
- Specify`queryType`, for example, COST, USAGE.
- Filter and group by different dimension/tags, functioning like an SQL query.
- Use up to four`groupBy`parameters.

The following is a sample Usage endpoint URI that conforms to the schema:
- https://usageapi. &lt;region&gt; .oci.oraclecloud.com/20200107/usage

For more information about the API and to view the full list of endpoints, see the[Usage API](https://docs.oracle.com/iaas/api/#/en/usage/).

To use the Usage API, you must have one of these permissions:
- USAGE_REPORT_MANAGE
- USAGE_REPORT_READ
- USAGE_ANALYSIS_MANAGE
- USAGE_ANALYSIS_READ
Note  
  
Users with the USAGE_ANALYSIS_READ permission can select only`USAGE_ONLY`for`queryType`. For more information about the`queryType`parameter, see[Using queryType](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#cost_analysis_using_the_api__section_e1j_mtf_vmb).

[Using granularity](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

The Usage API supports: MONTLY, DAILY, and HOURLY granularity. All`startTime`are inclusive, and`endTime`are exclusive, the same as a Java substring.
- For HOURLY, only a maximum 36-hour time period is supported, with no more precision than an hour. This means no minutes or seconds in the input time.
- 

For MONTHLY, only the first date of the month to another first date of the month is supported. For example, 2020-06-01T00:00:00Z, a maximum 12-month period.
- 

For DAILY, no more precision than a day is supported, with a maximum 90-day period. You must enter this as 00:00:00. For example, 2020-06-01T00:00:00Z.

[Using groupBy](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

In an API response, dimension is only shown in terms of`groupBy`. For example, if "service" isn't in`groupBy`, the "service" field in the response will be empty.
Note  
  
Only four`groupBy`parameters can be used at a time.
In addition:
- If a`groupBy`list is empty, "currency" will be added into`groupBy`.
- If the`queryType`is "Usage", "unit" will be add into`groupBy`.
- If the`queryType`is "COST" or "empty", "currency" will be add into`groupBy`.
- `computedAmount`works as expected only when "currency" is in`groupBy`.
- `computedQuantity`works as expected only when "unit" is in`groupBy`.

[Using queryType](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

The API can query USAGE or COST for a specific account.`computedQuantity`represents usage and`computedAmount`represents cost. For getting the expected usage, you need to set`queryType`to USAGE or add "unit" in`groupByKey`. This is due to the fact that usage is aggregated/grouped correctly when grouping by unit.

See[RequestSummarizedUsagesDetails Reference](https://docs.oracle.com/iaas/api/#/en/usage/latest/datatypes/RequestSummarizedUsagesDetails)for a list of the values you can select for`queryType`.

[Using filtering](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

Nested filtering in API requests is supported. The list of filters are evaluated by the operator. In each filter, all dimensions and tags are evaluated by the operator. Simultaneous evaluation of the filter list and dimension/tags is not supported, which means dimensions or tags and the filter list can't be non-empty at the same time.

Supported operators are AND, OR. These two filters below are equal:
```

```
Invalid example because dimensions and filters are non-empty at the same time:
```

```

[Querying with tags](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

As mentioned previously, we only show the field in`groupBy`. So you need to add tag related fields in`groupBy`. For example:
```

```

If you add`tagKey`, all items in the response will have a`tagKey`.`tagKey`also can be empty even if you add a`tagKey`. This is because some of your resources don't have a`tagKey`. We suggested adding all three of these in`groupBy`, so you can see a complete tag in the response:
```

```

If you want to filter by tag, you need to add the tag in the filter object. This can be filtered by any tagKey/Namespace/value combination of any tagKey/Namespace/value.

[Valid groupBy example](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

```

```

Note  
  
Only up to four`groupBy`parameters can be used in an API call.

`"tenantId"`and`"tenantName"`are not currently supported.

[Valid filter dimension example](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

```

```
This is case-sensitive.`"tenantId"`and`"tenantName"`are not currently supported.

[How to groupBy compartment?](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

`groupBy`compartment-related keys (`"compartmentName"`,`"compartmentPath"`,`"compartmentId"`) are different than the other`groupBy`keys.

To get an expected result, you must request with`compartmentDepth`.`compartmentDepth`is &gt;=1 and &lt;=6.

`groupBy`compartment means all compartments usage or costs with a higher depth will be aggregated to the compartment with the given depth. For example:
```

```

If the depth is 1, it means all usage or costs are grouped to the root compartment.

If the depth is 2, it means all compartments with depth 2 will contain the usage or costs with all its children. In the response, the root will contain its own usage, B will aggregate (B, D, E, F), and C will contain C.

[Why are some fields in a response empty?](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

The fields will show up only when the fields are in`groupBy`. Not all fields in the response are currently available. Only the fields mentioned in[Valid groupBy example](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#cost_analysis_using_the_api__section_vnh_4cg_vmb)are supported.

[What is nextPageToken?](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

This can be set as null. Currently not supported.

[Example request body](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

The best way to understand how the API works is checking how the Console uses the API. You can find the request body in the web browser's debug mode.
```

```

After you make a request without any filter, you can see what the dimension/tags' value can be. Subequently, you can make a request with a filter and a correct dimension value.
```

```

[Using customized scripts, CLI, and SDK](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#)

If you write a customized script, Oracle does not support or assist with debugging your script. Only the CLI, SDK, and Terraform are supported. See[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)for more information. For example:
```

```
SimpleRequestSummarizedUsagesDetails.json:
```

```
clitest.conf:
```

```
Also see the Oracle Cloud Infrastructure SDK at[https://github.com/oracle/oci-java-sdk](https://github.com/oracle/oci-java-sdk),[https://github.com/oracle/oci-python-sdk](https://github.com/oracle/oci-python-sdk)
