# Editing a Dashboard Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard-group.htm
- Fetched: 2026-09-05 02:00 CDT

# Editing a Dashboard Group

Edit a dashboard group's name and description.

To move a dashboard from one dashboard group to another, see[Moving a Dashboard Between Groups and Compartments](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#top).
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/edit-dashboard-group.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards . Then select Dashboard groups .
- (Optional) If needed, under List Scope , change the compartment.
- Select the name of the dashboard group.
- On the dashboard group details page, select Edit .
- In the Edit dashboard group panel, change the name and description as needed.

- For the name, leading and trailing spaces and the following special characters aren't allowed:`<>()=/'"&\`.
- For the description, the following special characters aren't allowed:`<>()=/'"&\`. Avoid entering confidential information.
- Select Submit .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard-group/update.html)dashboard-group update`command and required parameters to update a dashboard group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[
