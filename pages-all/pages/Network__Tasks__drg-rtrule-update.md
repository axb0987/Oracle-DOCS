# Updating a Route Rule in a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm
- Fetched: 2026-09-05 02:44 CDT

# Updating a Route Rule in a DRG Route Table

Update one or more route rules in the specified DRG route table.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-update.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- Select the name of the DRG route table whose static rules you want to update.
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Static route rules tab.
- Under Resources , select Static route rules .
- Check the box next to the Destination CIDR block for the rule or rules you want to update.
- Perform one of the following actions depending on the option that you see:

- Select Actions , then Edit , and make the changes you want.
- Select Edit and make the changes you want.
- When finished, select Save changes .
- 

Use the[network drg-route-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/update.html)command and required parameters to update one or more route rules in the specified DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/UpdateDrgRouteRules)
