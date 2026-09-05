# Managing Console Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards.htm
- Fetched: 2026-09-05 01:59 CDT

# Managing Console Dashboards

Dashboards let you monitor resources, diagnostics, and key metrics for your tenancy in the Oracle Cloud Infrastructure Console.

Dashboards are fully customizable: you choose which widgets to use and how to display the data. The following topics explain how to create, edit, and manage your dashboards:
- [Creating a Dashboard](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#top)
- [Using Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-use-console.htm#top)
- [Listing the Dashboards in a Dashboard Group](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/listing-dashboards.htm#top)
- [Getting a Dashboard's Details](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/get-dashboard-details.htm#top)
- [Editing a Dashboard](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard.htm#top)
- [Deleting a Dashboard](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard.htm#top)
- [Moving a Dashboard Between Groups and Compartments](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#top)

For specifics on widgets, see[Managing Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets)and[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#top).

## Required IAM Policies

To use Oracle Cloud Infrastructure, you must be granted security access in a policy by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which compartment to work in.

To get started with the Console Dashboards service, an administrator needs to grant user access through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

The resource name for the Console Dashboards service is`dashboards-family`. The following is an example policy to grant users access to the Console Dashboards service resources:

```

```

The following is an example policy to grant users access to a dashboard group:
```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more information about Console Dashboards policies, see[Policy Details for Console Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/../Reference/dashboardspolicyreference.htm#policyreference).

### To share dashboards

Use IAM policies to control access to dashboards.

The following policy gives users in the specified group manage permissions for this dashboard group at the compartment level:

```

```

The following policy gives users in the specified group manage permissions for this dashboard group at the tenancy level:

```

```
