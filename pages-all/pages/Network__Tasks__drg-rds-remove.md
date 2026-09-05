# Delete a Route Distribution Statement
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm
- Fetched: 2026-09-05 02:44 CDT

# Delete a Route Distribution Statement

Remove or delete one or more route distribution statements from a route distribution for a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-remove.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to either the Import route distributions or Export route distributions sections. Select the route distribution with a statement you want to delete, then select the Statements tab.
- Under Resources , select either Import route distributions or Export route distributions . Select the route distribution with a statement you want to delete.
-   

- Select the statement or statements you want to delete, then depending on the options that you see:

- Select Actions , then Remove .
- Select Remove .
- Confirm the removal.
- 

Use the[network drg-route-distribution-statement remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/remove.html)command and required parameters to delete one or more route distribution statements from the specified route distribution:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/RemoveDrgRouteDistributionStatements)
