# Editing a Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard.htm
- Fetched: 2026-09-05 02:00 CDT

# Editing a Dashboard

Edit a Console dashboard's name and description.

Because dashboards are made up of collections of widgets, most edits to a dashboard are best completed by using the Console. For information about creating and editing a dashboard's layout and widgets, see[Managing Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-widgets.htm#widgets)and[Configuring Widgets](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/widgetmanagement.htm#top).
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
The default dashboard opens. If needed,[switch dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-use-console.htm#top__switch).
- Select Dashboard actions and select Change name and description .
- In the Edit name and description panel, change the name and description as needed.

- For the name, leading and trailing spaces and the following special characters aren't allowed:`<>()=/'"&\`.
- For the description, the following special characters aren't allowed:`<>()=/'"&\`. Avoid entering confidential information.
- Select Submit .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard/update-dashboard-v1.html)dashboard update-dashboard-v1`command and required parameters to edit a dashboard:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Use the[
