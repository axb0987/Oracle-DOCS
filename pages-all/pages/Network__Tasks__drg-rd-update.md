# Updating a Route Distribution
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm
- Fetched: 2026-09-05 02:44 CDT

# Updating a Route Distribution

Update a route distribution for a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

The following steps describe how to change the name of a route distribution. To add or update a statement for an import or export route distribution, see[Adding a Route Distribution Statement](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm)or[Updating a Route Distribution Statement](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-update.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-update.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to either the Import route distributions or Export route distributions sections.
- Under Resources , select either Import route distributions or Export route distributions .
- Select the name of the route distribution that you want to rename.
- Select Edit .
- Enter a new name, then select Save changes .
- 

Use the[network drg-route-distribution update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/update.html)command and required parameters to rename the specified route distribution:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateDrgRouteDistribution](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistribution/UpdateDrgRouteDistribution)
