# Grafana Plug-in
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/grafana.htm
- Fetched: 2026-09-05 01:36 CDT

# Grafana Plug-in

This topic provides instructions for installing, configuring, and using the Oracle Cloud Infrastructure Data Source for Grafana.

This topic provides instructions for installing, configuring, and using the Oracle Cloud Infrastructure Data Source for Grafana, otherwise referenced as the Grafana Plug-in.

## Grafana Plug-in Overview

Grafana is an open-source visualization and alerting tool that you can use for analytics and monitoring of time-series data (metrics). While metrics from[Oracle Cloud Infrastructure Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)are visible in metrics charts through the Console, you can use Oracle Cloud Infrastructure Data Source for Grafana ("the Grafana Plug-in") to view metrics from resources across providers on a single Grafana dashboard.

## Prerequisites for Using the Grafana Plug-in

- An Oracle Cloud Infrastructure account.
- A user in that account, in a security group with an IAM policy that grants necessary permissions for working with resources in the account compartments. The policy must give you access to the metric namespaces emitting metrics (such as Compute) as well as the related resources (such as a set of compute instances). If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you've been granted and which compartment you should work in. Administrators: For common policies that give groups access to metrics, see[Metric Access for Groups](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups). To authorize resources, such as instances, to make API calls, add the resources to a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)through its matching rules, and then create a policy that allows that dynamic group access to metrics. To allow access across compartments, create the policy in the tenancy. Because of the concept of policy inheritance, instances in the indicated dynamic group can then access metrics in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. See[Metric Access for Resources](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-dynamic).
- Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see[Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).
- Required keys and Oracle Cloud Infrastructure IDs (OCIDs). For guidance, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).

## Download and Install the Grafana Plug-in

Note  
  

[Grafana](http://docs.grafana.org/installation/)must be installed before you can install the Grafana Plug-in. Version 3.0 or later required.

Authentication for metric access depends on where Grafana is running. If you are running Grafana on a local machine outside Oracle Cloud Infrastructure, you must call the Monitoring API using the[Command Line Interface (CLI)](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm). If you are running Grafana on an Oracle Cloud Infrastructure compute instance that you created, then you can add the instance to a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)by configuring a matching rule. In all scenarios, you have the option of calling the API using the[CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm).

For instructions on installing the Grafana Plug-in (Oracle Cloud Infrastructure Data Source for Grafana), see[https://github.com/oracle/oci-grafana-plugin](https://github.com/oracle/oci-grafana-plugin).

## Configure the Grafana Plug-in

This section describes how to add the Grafana Plug-in and set up a dashboard.

[To configure the Grafana Plug-in](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/grafana.htm#)

Note  
  
When installed locally, the Grafana plug-in accesses metrics using calls to the Monitoring API.
- 

Set up the[CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm)for accessing Oracle Cloud Infrastructure APIs.

You'll need to access the Monitoring API for authentication.
- 

Navigate to the Grafana homepage at the following URL.

[http://localhost:3000](http://localhost:3000/)
- 
Add the Grafana Plug-In (Oracle Cloud Infrastructure Data Source for Grafana).

In addition to the steps below, see the Grafana instructions for adding data sources at[https://grafana.com/docs/grafana/latest/getting-started/getting-started/](http://docs.grafana.org/guides/getting_started/).
- In Grafana, on the Home Dashboard, click the gear icon on the left.
- Click Add data source .
- In the Filter text box, type: oracle-oci-datasource
- In the filtered list, select oracle-oci-datasource .
- 

In the Settings page, fill in your Tenancy OCID , Default Region , and Environment . For Environment choose local .
- Set up a[dashboard](https://www.google.com/search?q=dashboard+site%3Adocs.grafana.org)of the type "Graph."
- 

(Optional) To confirm access to metrics from Oracle Cloud Infrastructure, update your dashboard query ("Metrics") with a specific region, compartment, namespace, metric. You can also add one or more dimensions.

Congratulations. You can now view your Oracle Cloud Infrastructure metrics in Grafana!

[Environment options](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/grafana.htm#)

local is for Grafana deployments outside Oracle Cloud Infrastructure.

OCI Instance is for Grafana deployments on Oracle Cloud Infrastructure resources.

The data source is now added, enabling you to set up a dashboard showing metrics from Oracle Cloud Infrastructure.

## Troubleshoot the Plug-In

If the dashboard query ("Metrics") fails to populate with options, or if you have other issues accessing metrics, then the IAM policy used to access metrics may be malformed, or it may not include all required matching rules for your dynamic group (for running Grafana on an Oracle Cloud Infrastructure compute instance that you created).

To resolve this issue, do the following.
- Review your IAM policy to ensure that it matches prerequisites.
-
