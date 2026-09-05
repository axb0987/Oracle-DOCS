# Deleting a Dashboard Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard-group.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting a Dashboard Group

Delete a dashboard group from a tenancy.

Note  
  
You can't delete a dashboard group that contains dashboards. Either[delete the dashboards](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard.htm#top)or[move them to another group](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard.htm#top)before you delete the group.
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/delete-dashboard-group.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards . Then select Dashboard groups .
- (Optional) If needed, under List Scope , change the compartment.
- Select the name of the dashboard group.
- On the dashboard group details page, select Delete .
- In the Delete dashboard group dialog box, select Delete .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard-group/delete.html)dashboard-group delete`command and required parameters to delete a dashboard group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[
