# Creating a Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm
- Fetched: 2026-09-05 01:59 CDT

# Creating a Dashboard

Create a custom Console dashboard for a tenancy.

After you create a dashboard, you can[add widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets)and make adjustments. See[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#top)and[Using Dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-use-console.htm#top).
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
The default dashboard opens.
- Select New dashboard .
- Choose Start from a template to use a dashboard preconfigured with widgets addressing a specific use case, or choose Build from scratch to start with a blank dashboard. If you're starting from a template, select a value from the Template drop-down list.

Tip  
  
If Show dashboard format is selected, a preview of the template is displayed.
- In the Create new dashboard panel, enter the following values:
- Enter a name for the dashboard. You can change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the dashboard. Leading and trailing spaces and the following special characters aren't allowed:`<>()=/'"&\`. Avoid entering confidential information.
- (Optional) Enter a description for the dashboard. The following special characters aren't allowed:`<>()=/'"&\`.
- Select the compartment to create the dashboard in.
If the compartment contains one or more dashboard groups, you can either select an existing dashboard group or create new a dashboard group. If the compartment doesn't contain a dashboard group, you're prompted to create one. For more information, see[Working with Console Dashboards Groups](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboardgroups.htm#top).
- If you choose to use an existing dashboard group in the compartment, select one from the Dashboard group list.
- If you choose create a new dashboard group, enter a name for it. Avoid entering confidential information.
- (Optional) To add tags to the dashboard, select Show additional options and enter the required values.

If you have permission to create a resource, then you also have permission to apply free-form tags to that resource. To apply a defined tag, you must have permission to use the tag namespace. For more information about tagging, see[Tagging](https://docs.oracle.com/iaas/Content/Tagging/home.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator.
- Select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard/create-dashboard-v1.html)dashboard create-dashboard-v1`command and required parameters to create a dashboard:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Use the[
