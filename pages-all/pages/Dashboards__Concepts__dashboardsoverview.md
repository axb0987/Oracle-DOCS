# Overview of the Console Dashboards Service
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/dashboardsoverview.htm
- Fetched: 2026-09-05 01:59 CDT

# Overview of the Console Dashboards Service

The Console Dashboards service allows you to create custom dashboards in the Oracle Cloud Infrastructure Console to monitor resources, diagnostics, and key metrics for your tenancy.

Dashboards gather data from Oracle Cloud Infrastructure (OCI) services to create charts and tables that give you a quick view into your resource utilization, billing, and system health.

A dashboard is a collection of[widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#top). Each widget presents one set of data. For example, a widget could be a graph showing CPU metrics from the Monitoring service or a bar chart displaying the prevalence of different types of errors. The collection of widgets in a dashboard gives you a centralized view of your infrastructure and system health.

## Concepts

Here's a list of basic concepts for the Console Dashboards service. Dashboard

A dashboard is a collection of visualizations that let you monitor resources, diagnostics, and key metrics for your tenancy. Dashboards are fully customizable: you define the widgets, behavior, and IAM policies. OCI treats dashboards as resources: dashboards have OCIDs, adhere to IAM policies, and reside in compartments. See[Managing Console Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/dashboards.htm#top)for more information. Dashboard Group

Dashboard groups let you share collections of dashboards with designated groups of people. For example, each team within an organization can have its own dashboard group. A dashboard group is an OCI resource with its own OCID. See[Working with Console Dashboards Groups](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/dashboardgroups.htm#top)for more information. Default Dashboard

The first time you visit the Dashboard tab, you are presented a default dashboard and sample widgets that contain instructions for getting started with widgets. This dashboard is used as an example and doesn't start with the full functionality of a regular dashboard. For example, it doesn't have a Dashboards actions menu, and you cannot delete it. You can personalize the dashboard by editing its layout or adding more widgets. Once you save your changes, or create a new dashboard, the initial settings are lost. For more detailed instructions, see[Managing Console Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/dashboards.htm#top)and[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#top).

After your tenancy has a saved dashboard, your most recently viewed dashboard becomes the default dashboard. The initial default dashboard with sample widgets is inaccessible unless all other dashboards have been deleted. Widget

A[widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/dashboardsoverview.htm#dashboardsoverview_widgettypes)is a single data visualization from one data source. Widgets can display information about inventory, usage, billing, alerts, outages, and more. You can create multiple widgets and use them to build dashboards. For more information, see[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#top). Dashboard Template When you create a new dashboard, you can choose from a selection of dashboard templates that are preconfigured with a set of widgets for specific use cases. For example, the Audit logs template includes widgets that show you active user count, user activity, activity trends, activity by compartment, and other activity logs. Other templates focus on costs, metrics, or logs for Compute, Object Storage, VCN, and other services.

## Types of Widgets

Dashboards support the following types of widget:
- 

[Infrastructure Billing Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#billing): This widget shows current billing cycle information. You can only include a single instance of the infrastructure billing widget in your dashboard.
- [Cost Management Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#cost-management): This widget helps you track and optimize your Oracle Cloud Infrastructure spending by generating charts with aggregated[Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm)data. You can include multiple cost management widgets in your dashboard.
- 

[Logging Chart Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#loggingchart): This widget allows you to create visualizations with data from the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). You can include multiple logging chart widgets in your dashboard.
- 

[Logging Data Table Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#loggingtable): This widget allows you to display a table of the data stored in the[Oracle Cloud Infrastructure Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm). You can include multiple logging data table widgets in your dashboard.
- 

[Markdown Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#markdownwidget): This widget lets you add and format text-based content. You can include multiple markdown widgets in your dashboard.
- 

[Monitoring Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#monitoringchart): This widget lets you view and compare metrics from the[Oracle Cloud Infrastructure Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). You can include multiple monitoring widgets in your dashboard.
- 

[Resource Explorer Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#resourceexplorer): This widget allows you to view resources by compartment. You can only include a single instance of the resource explorer widget in your dashboard.
- 

[Resource Query Widget](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#resource-query): This widget allows you to use queries to get detailed information about specific resources. You can filter by region, compartment, resource type, or write an advanced query using[Search Language Syntax](https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm).

For more information about widgets, see[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/widgetmanagement.htm#top). For general steps explaining how to add widgets to dashboards, see[Managing Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Concepts/../Tasks/dashboards-widgets.htm#widgets).

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Monitoring Resources

Use Monitoring to query metrics and manage alarms. Metrics and alarms help monitor the health, capacity, and performance of your cloud resources.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in your organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, launch instances, create buckets, download objects, and so on. For more information, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.

## Limits on Dashboards Resources

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm)
