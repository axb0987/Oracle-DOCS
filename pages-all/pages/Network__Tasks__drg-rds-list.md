# Listing Route Distribution Statements
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm
- Fetched: 2026-09-05 02:44 CDT

# Listing Route Distribution Statements

List the statements for an import or export route distribution for a dynamic routing gateway (DRG) in Oracle Cloud Infrastructure.

An import route distribution statement specifies how route advertisements entering the DRG through referenced attachments are inserted into the DRG route table. An export route distribution statement describes how routes are advertised to attachments from their assigned DRG route table.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-list.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to either the Import route distributions or Export route distributions sections. Select the route distribution for which you want to list statements, then select the Statements tab.
- Under Resources , select either Import route distributions or Export route distributions . Select the route distribution for which you want to list statements.

The statements are listed in the order in which they're evaluated.
- 

Use the[network drg-route-distribution-statement list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/list.html)command and required parameters to list the statements for a specified import or export route distribution:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/ListDrgRouteDistributionStatements)
