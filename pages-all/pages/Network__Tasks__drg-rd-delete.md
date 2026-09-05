# Deleting a Route Distribution
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm
- Fetched: 2026-09-05 02:44 CDT

# Deleting a Route Distribution

Delete a specified route distribution.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-delete.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to either the Import route distributions or Export route distributions sections.
- Under Resources , select either Import route distributions or Export route distributions .
- From the Actions menu (three dots) for the route distribution you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network drg-route-distribution delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/delete.html)command and required parameters to delete the specified route distribution:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/DeleteDrgRouteDistribution)
