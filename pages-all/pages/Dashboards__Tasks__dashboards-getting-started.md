# Getting Started with Console Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-getting-started.htm
- Fetched: 2026-09-05 01:59 CDT

# Getting Started with Console Dashboards

Learn how to start using the Console Dashboards service.

You can use dashboards to view:
- Infrastructure overviews
- Usage summaries for resources in a particular region or compartment
- System health
- Resource monitoring
- Billing information

The first time you visit the Dashboard tab, you're presented with a default dashboard and sample widgets that contain instructions for getting started with widgets. You can personalize the dashboard by editing its layout or adding more widgets. Or, you can[create a new dashboard](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#top). For more detailed instructions, see[Managing Console Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards.htm#top)and[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#top).

After a tenancy has a saved dashboard, your most recently viewed dashboard becomes the default dashboard. The initial default dashboard with sample widgets is inaccessible unless all other dashboards have been deleted.
Important  
  
Resources for the Console Dashboards service are created in the tenancy's home region. Although it's possible to create dashboard and dashboard group resources in regions other than the home region, you can't view those resources in the Console. Therefore, creating resources outside of the home region isn't recommended.

## Using the Console

To access dashboards in the Console:
- Open the navigation menu. Under Home , select Dashboards .

To access dashboard groups in the Console:
- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards . Then select Dashboard groups .

To create a dashboard from the overview page using a template:
- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards .
- Select the name of a template to learn more about the dashboard. To create a new dashboard from the template, select Create new dashboard . For more information, see[Creating a Dashboard](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#top)and[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#top).

To view recently updated dashboards:
- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards and view the list under Recently updated dashboards .

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
