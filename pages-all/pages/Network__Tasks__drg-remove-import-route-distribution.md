# Removing an Import Route Distribution from a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm
- Fetched: 2026-09-05 02:44 CDT

# Removing an Import Route Distribution from a DRG Route Table

Remove the import route distribution from a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure so that no routes are imported into it.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-remove-import-route-distribution.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- Select the name of the DRG route table whose import route distribution you want to remove.
- Select Edit .
- Clear the Enable import route distribution checkbox.
- Select Save changes .
- 

Use the[network drg-route-table remove-import-route-distribution](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/remove-import-route-distribution.html)command and required parameters to remove an import route distribution from a DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[RemoveImportDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/RemoveImportDrgRouteDistribution)
