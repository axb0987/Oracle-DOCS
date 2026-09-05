# Configuring Widgets
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm
- Fetched: 2026-09-05 02:00 CDT

# Configuring Widgets

Configure Console Dashboards widgets so that they give you insight into your resource usage, billing, and system health. Each dashboard can contain multiple widgets.
Note  
  
A single dashboard can contain a maximum of 20 widgets. If you need more than 20 widgets, create additional dashboards.

## Types of Console Dashboards Widgets

Console Dashboards support the following types of widget ([Applications services](https://docs.oracle.com/iaas/Content/fusion-applications/overview.htm)support only Resource Explorer, Monitoring, and Markdown).
- 

[Infrastructure Billing Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#billing): This widget shows current billing cycle information. You can only include a single instance of the infrastructure billing widget in your dashboard.
- [Cost Management Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#cost-management): This widget helps you track and optimize your Oracle Cloud Infrastructure spending by generating charts with aggregated[Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)data. You can include multiple cost management widgets in your dashboard.
- 

[Logging Chart Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#loggingchart): This widget allows you to create visualizations with data from the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). You can include multiple logging chart widgets in your dashboard.
- 

[Logging Data Table Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#loggingtable): This widget allows you to display a table of the data stored in the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). You can include multiple logging data table widgets in your dashboard.
- 

[Markdown Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#markdownwidget): This widget lets you add and format text-based content. You can include multiple markdown widgets in your dashboard.
- 

[Monitoring Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#monitoringchart): This widget lets you view and compare metrics from the[Oracle Cloud Infrastructure Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). You can include multiple monitoring widgets in your dashboard.
- 

[Resource Explorer Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#resourceexplorer): This widget allows you to view resources by compartment. You can only include a single instance of the resource explorer widget in your dashboard.
- 

[Resource Query Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#resource-query): This widget allows you to use queries to get detailed information about specific resources. You can filter by region, compartment, resource type, or write an advanced query using[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).

The following sections describe the dashboard widgets and explain how to configure them. For general steps explaining how to add widgets to dashboards, see[Managing Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets).

## Infrastructure Billing

Administrators and users with[appropriate permissions](https://docs.oracle.com/iaas/Content/Billing/Concepts/costs.htm)can view the infrastructure billing widget. The infrastructure billing widget lets you quickly view your current charges or usage and the days elapsed in your billing cycle. Your view depends on your account type.
- Pay As You Go customers see the current charges and the number of days elapsed in the current billing cycle.
- Universal credit customers see the total credits used and number of days elapsed in the credit period.
- Trial customers see the total credits used and number of days elapsed in the trial period.

To get a more detailed view of your spending, select the Analyze costs link to go to the[Cost Analysis tool](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)where you can generate charts and reports of aggregated cost data for your Oracle Cloud Infrastructure consumption. If your account is a Free Tier or promotional trial account, you see an option to Upgrade your account . If you have a paid account, you see the option to Manage payment method to view or change your payment method.

[To add the infrastructure billing widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Infrastructure Billing .
- Select Save .

## Cost Management

Administrators and users with[appropriate permissions](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm#policy)can view the cost management widget. The cost management widget helps you track and optimize your Oracle Cloud Infrastructure spending by generating charts and reports of aggregated cost data.

The[Cost Analysis Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)includes more information about the Cost Analysis tool and detailed descriptions of the[Cost Analysis query fields](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Cost_Analysis_Query_Fields)used by this widget.

[To add the cost management widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Cost Management .

The default cost management chart displays.
- On the widget, select the Actions menu ( ) , and then select View and edit settings . The Cost Management chart widget configuration dialog opens.
- For Name , enter a name for the widget. Avoid entering confidential information.
- For Description , enter a description for the widget (optional).
- For Configure metric query , make the following selections:
- Time range: Select a predefined time range for data available in the usage store.
- Granularity: Select the granularity of the chart. Options are based on the selected time range.
- Chart type: Select the chart type.
- Filters: Select Add Filter to apply[filters](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm#Filters)to the chart data.
- Grouping dimensions: Select the[grouping](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm#groupingdimension)used to aggregate the chart data.
- Select Preview changes at any time to preview the chart.
- Select Submit , and then select Save .

[To export the chart as a PDF](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- On the widget, select the Actions menu ( ) , and then select Export as PDF .

The chart is exported as a PDF.

[To expand the chart](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- On the widget, select the Actions menu ( ) , and then select Expand chart .

The chart is expanded to a larger size.
- Optionally, change the Chart type .
- To return to your dashboard, close the window.

## Logging Chart

Use the logging chart widget to create visualizations with the data stored in the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).

To use the logging chart widget, you first need to enable logs for resources. After you enable a log, log entries begin to appear on the detail page for the log, and you can use this data to build charts with the logging chart widget. For instructions, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).

The Logging service contains three kinds of logs:
- Audit logs: Logs related to events emitted by the Oracle Cloud Infrastructure Audit service. These logs are available from the Logging Audit page, or are searchable on the Search page alongside the rest of your logs.
- Service logs: Emitted by OCI native services, such as API Gateway, Events, Functions, Load Balancer, Object Storage, and VCN Flow Logs. Each of these supported services has pre-defined logging categories that you can enable or disable on your respective resources.
- Custom logs: Logs that contain diagnostic information from custom applications, other cloud providers, or an on-premise environment. Custom logs can be ingested through the API, or by configuring the Unified Monitoring Agent. You can configure an OCI Compute instance/resource to directly upload Custom Logs through the Unified Monitoring Agent. Custom logs are supported in both a virtual machine and bare metal scenario.

[To add a logging chart widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Logging chart .
- In the widget, select Configure . The Logging Chart Widget Configuration dialog opens.
- For Name , enter a name for the widget. Avoid entering confidential information.
- For Description , enter a description for the widget (optional).
- For Region , select a region. The logging chart data that displays in the widget comes from the region that you select.
- For Set visualization parameters , make the following selections:
- Visualization Type: Select the chart type.
- Interval: Select the time interval between chart refreshes.
- Group By: Select the criteria to use for grouping the logging data in the visualization.
- Filter by time: Select the time intervals to use as a filter for the chart.
- For Select and filter the logs , make the following selections:
- For Custom filters , enter search filters, such as log fields, text search, or time intervals.
- For Select logs to search , enter compartments, log groups, or logs to filter by. You can filter by multiple compartments and log groups.

See[Basic Search Queries](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm#basic_search_queries)for more information about searching and filtering logs.
- Select Submit , and then select Save .

## Logging Data Table

Use the logging data table widget to add a table that displays the data stored in the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).

To use the logging data table widget, you first need to enable logs for resources. After you enable a log, log entries begin to appear on the detail page for the log. For instructions, see[Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).

The Logging service contains three kinds of logs:
- Audit logs: Logs related to events emitted by the Oracle Cloud Infrastructure Audit service. These logs are available from the Logging Audit page, or are searchable on the Search page alongside the rest of your logs.
- Service logs: Emitted by OCI native services, such as API Gateway, Events, Functions, Load Balancer, Object Storage, and VCN Flow Logs. Each of these supported services has pre-defined logging categories that you can enable or disable on your respective resources.
- Custom logs: Logs that contain diagnostic information from custom applications, other cloud providers, or an on-premise environment. Custom logs can be ingested through the API, or by configuring the Unified Monitoring Agent. You can configure an OCI Compute instance/resource to directly upload Custom Logs through the Unified Monitoring Agent. Custom logs are supported in both a virtual machine and bare metal scenario.

[To add a logging data table widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Logging data table .
- In the widget, select Configure . The Logging Data Table Widget Configuration dialog opens.
- For Name , enter a name for the widget. Avoid entering confidential information.
- For Description , enter a description for the widget (optional).
- For Region , select a region. The logging data that displays in the widget comes from the region that you select.
- For Select and filter the logs , make the following selections:
- For Custom filters , enter search filters, such as log fields, text search, or time intervals.
- For Select logs to search , enter compartments, log groups, or logs to filter by. You can filter by multiple compartments and log groups.
- Filter by time: Select the time intervals to use as a filter for the table.

See[Basic Search Queries](https://docs.oracle.com/iaas/Content/Logging/Concepts/searchinglogs.htm#basic_search_queries)for more information about searching and filtering logs.
- Select Submit , and then select Save .

## Markdown

Use the markdown widget to include and format text-based content in your dashboard.

[To add a markdown widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Markdown widget .
- In the widget, select Configure . The Markdown widget configuration dialog opens.
- In Name , enter a name for the widget. Avoid entering confidential information.
- In Description , enter a description for the widget (optional).
- In the Markdown content field, enter text formatted with Markdown. For information about using Markdown, see the[Markdown Guide](https://www.markdownguide.org/). You can preview the content in the Preview markdown field.
- Select Create widget , and then select Save .

## Monitoring

Use the monitoring widget to view metric data stored in the[Oracle Cloud Infrastructure Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm).

To configure the monitor chart widget, you first need to configure metric queries. See[Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm)for more information.

[To add a monitoring widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Monitoring .
- In the widget, select Configure . The Monitoring Widget Configuration dialog opens.
- For Name , enter a name for the widget. Avoid entering confidential information.
- For Description , enter a description for the widget (optional).
- For Set visualization parameters , make the following selections:
- Chart type: Select the chart type.
- Interval: Select the time interval between chart refreshes.
- Filter by time: Select the time interval to use as a filter for the chart.
- For Configure metric query , make the following selections:
- If you want to change the compartment, select Change Compartment and choose a different compartment.
- For Region , select a region.
- For Namespace , select the service or application emitting metrics for the resources that you want to monitor.
- For Metric Name , enter the name of the metric. You can only specify one metric. Metric selections depend on the selected compartment and metric namespace.
- For Statistic , select function to use to aggregate the data.
- Optionally, configure the Metric Settings .
- For Dimension Name , select a qualifier specified in the metric definition from the list. For example, the dimension`resourceId`is specified in the metric definition for`CpuUtilization`.
- For Dimension value , select the value you want to use for the specified dimension from the list. For example, the resource identifier for your instance.
- If required, select + Additional Dimension to add another name-value pair for a dimension.

To remove a dimension name-value pair, select the Remove (x) button.
- Select Submit , and then select Save .

## Resource Explorer

Use the resource explorer to get an overview of the number and types of resources that exist in a selected compartment and region.

[To add and use the resource explorer widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Resource explorer .
- Select Save .
- The resource explorer displays the list of services and count of resources in the selected compartment and region . By default, the root compartment is selected. To view another compartment, select the Actions menu ( ) , and then select View and edit settings , make changes, and select Update .
- Expand the entry for a service to see the count for each resource-type within the service.
- To see more information about a resource-type in the list, select the resource-type to open the detailed list. To navigate directly to a specific resource in the list, select the Display name .

## Resource Query

Use resource queries to get detailed resource information. You can filter by region, compartment, resource type, or write an advanced query using[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).

[To add and use the resource query widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#)

- Open the navigation menu. Under Home , select Dashboards .
- Follow the steps to[add a widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets__add-widgets)and choose Resource query .
- In the widget, select Configure . The Resource query widget configuration dialog opens.
- For Name , enter a name for the widget. Avoid entering confidential information.
- For Description , enter a description for the widget (optional).
- For Resources scope , make the following selections:
- Region : Select the region to query for resources (optional).
- Select compartments to search : Select one or more compartments containing the resources.
- Filter by resource types : Select one or more resource types to filter results (optional).
- Optionally, select Switch to advanced resource query , enter a resource query, and select Search . See[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm)for guidance on creating your query.
- 

The Resources preview table shows the results of your query.
-
