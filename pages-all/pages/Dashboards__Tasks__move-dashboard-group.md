# Moving a Dashboard Group Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard-group.htm
- Fetched: 2026-09-05 02:00 CDT

# Moving a Dashboard Group Between Compartments

Move a dashboard group to a different compartment in the tenancy.
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/move-dashboard-group.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards . Then select Dashboard groups .
- (Optional) If needed, under List Scope , change the compartment.
- Select the the Actions menu ( ) on the right side of the dashboard group that you want to move, and select Move resource .
- In the Move resource to a different compartment dialog box, choose the destination compartment.
- Select Move resource .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard-group/change-compartment.html)dashboard-group change-compartment`command and required parameters to move a dashboard group to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Run the[
