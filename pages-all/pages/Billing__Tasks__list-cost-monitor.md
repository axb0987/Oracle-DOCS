# Listing Cost Monitors
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Cost Monitors

Get a list of cost monitors in your compartment in Billing and Cost Management.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-monitor.htm#)
- 

- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost Anomaly Detection .

The Cost Anomalies page opens.
- Select Cost Monitors .

The Cost monitors list page opens. All default and custom cost monitors are displayed in a table.
Note  
  

- If you can't see the list of cost monitors, ensure that your user has the correct Identity and Access Management (IAM) policy.
- (Optional) Select the Manage Columns icon on top-right of the column to hide or rearrange the columns. The following columns are shown by default:

Column Name Description Default Visibility
Monitor name

Displays the service name (for default cost monitors) or the user-defined name (for custom cost monitors).

For OCI Default Cost Monitors there is a row for each unique combination of tenancy and region. Expand OCI default monitor to see the individual service monitors for the tenancy and region. Yes
Status

Indicates whether a cost monitor is active or inactive.

- Active : Cost monitors become active automatically when they're created, if a deactivated monitor is reactivated by a user, or if new cost appears for resource within inactive monitor for insufficient data.
- Inactive :Cost monitors become inactive when deactivated by the user or if there is no longer cost for a minimum of one resource within the cost monitor within the last 60 days. Yes
Resource Criteria Defines the cost monitor's filter criteria. When a resource meets the criteria, its daily cost is included in the cost forecast. Yes
Region Identifies the region where the resources are running. Yes
Tenancy name Identifies the tenancy where the resources are running. Yes
Last updated Shows when the cost monitor was created or updated. Yes

## Filtering List Results

Use filters to limit the cost monitors in the list. Perform one of the following actions depending on the options that you see:
- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list.

## Actions

In the list table, select the name of a cost monitor to open its details page, where you can view its status and perform other tasks.

To perform an action on a cost monitor directly from the list table, select an available option from the Actions menu in the row for that cost monitor:
- View details : Open the details page for the cost monitor.

To create a cost monitor, select Create task monitor .
- 

Use the[oci costad cost-anomaly-monitor-collection list-monitors](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/costad/cost-anomaly-monitor-collection/list-monitors.html)command and required parameters to get a list of cost monitors in a compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListCostAnomalyMonitors](https://docs.oracle.com/iaas/api/#/en/cost-anomaly/latest/CostAnomalyMonitorCollection/ListCostAnomalyMonitors)
