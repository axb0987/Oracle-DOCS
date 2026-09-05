# Listing Route Rules in a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm
- Fetched: 2026-09-05 02:44 CDT

# Listing Route Rules in a DRG Route Table

List the static and dynamic route rules in a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.

Listing route rules helps you validate and troubleshoot the next hop behavior of traffic entering the DRG. For example, you can confirm the behavior of traffic destined for an on-premises network by validating the routes received by way of a Site-to-Site VPN IPSec tunnel or FastConnect virtual circuit.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rtrule-list.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- Select the name of the route table whose rules you want to see.
- Select Get all route rules .

The list of routes includes static routes inserted into the table and all dynamic routes that have been imported from other attachments and inserted by using an import route distribution.
- (Optional) To download the route rule in this route table, select Download route rules .
The route table is downloaded as a JSON file.
- When you're finished, select Close .
- 

Use the[network drg-route-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-rule/list.html)command and required parameters to list the route rules in a specified DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListDrgRouteRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteRule/ListDrgRouteRules)
