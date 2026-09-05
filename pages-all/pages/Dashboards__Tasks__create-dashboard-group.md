# Creating a Dashboard Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard-group.htm
- Fetched: 2026-09-05 01:59 CDT

# Creating a Dashboard Group

Create a dashboard group to gather Console dashboards into a collection that can be shared.
- [Console](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Dashboards/Tasks/create-dashboard-group.htm#)
- 

- Open the navigation menu. Under Home , select Dashboards .
- In the dashboard banner, select Manage dashboards . Then select Dashboard groups .
- Select Create dashboard group .
- In the Create new dashboard group panel, enter the following values:
- Enter a name for the dashboard group. You can change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the dashboard group. Leading and trailing spaces and the following special characters aren't allowed:`<>()=/'"&\`. Avoid entering confidential information.
- (Optional) Enter a description for the dashboard group. The following special characters aren't allowed:`<>()=/'"&\`.
- Select the compartment to create the dashboard group in.
- (Optional) To add tags to the dashboard, select Show additional options and enter the required values.

If you have permission to create a resource, then you also have permission to apply free-form tags to that resource. To apply a defined tag, you must have permission to use the tag namespace. For more information about tagging, see[Tagging](https://docs.oracle.com/iaas/Content/Tagging/home.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator.
- Select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dashboard-service/dashboard-group/create.html)dashboard-group create`command and required parameters to create a dashboard group:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
- 

Use the[
