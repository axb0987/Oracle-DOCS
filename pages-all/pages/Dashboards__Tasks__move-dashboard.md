# Moving a Dashboard Between Groups and Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm
- Fetched: 2026-09-05 02:00 CDT

# Moving a Dashboard Between Groups and Compartments

You can move a console dashboard to a new or existing dashboard group in the same compartment, or a different compartment.

To move a dashboard group, see[Moving a Dashboard Group Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard-group.htm#top). For more information about dashboard groups, see[Working with Console Dashboards Groups](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboardgroups.htm#top).
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
The default dashboard opens. If needed,[switch dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/dashboards-use-console.htm#top__switch).
- Select Dashboard actions , then select Move .
- In the Move dashboard panel, select the compartment that contains the group that you want to move the dashboard to, or the compartment where you want to create a group.
- If the compartment contains dashboard groups, select the one you want to move the dashboard to. You can also create a new group in the compartment by entering a name. Avoid entering confidential information.
- If the compartment doesn't contain any dashboard groups, create a new group in the compartment by entering a name. Avoid entering confidential information.
- Select Submit .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard/change-dashboard-group.html)dashboard change-dashboard-group`command and required parameters to move a dashboard to another group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Use the[
