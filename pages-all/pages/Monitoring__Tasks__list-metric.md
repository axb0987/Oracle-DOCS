# Listing Metric Definitions
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm
- Fetched: 2026-09-05 02:39 CDT

# Listing Metric Definitions

List metric definitions in Monitoring.

## Before You Begin

IAM policies: To list metric definitions, you must be given the required type of access in a policy written by an administrator. This requirement applies whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, check with the administrator. You might not have the required type of access in the current compartment .

Administrators: For an example policy, see[List Metric Definitions](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#metric-groups-list).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/list-metric.htm#)
- 

- [Create a basic query](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/metrics-explorer-basic-query.htm)on the Metrics Explorer page.
- If the query isn't open, open it by selecting Edit queries .
- To list the metric information that you want, select the required configuration fields:

- To list metric namespaces, select Compartment .
- To list metric names, select Compartment and Metric namespace .
- To list dimensions, select Compartment , Metric namespace , and Metric name .
- 

Use the[oci monitoring metric list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring/metric/list.html)command and required parameters to list metric definitions:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Monitoring](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/monitoring.html).
- 

Run the[ListMetrics](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/Metric/ListMetrics)
