# Deleting a DRG Route Table
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm
- Fetched: 2026-09-05 02:44 CDT

# Deleting a DRG Route Table

Delete a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.

Before you try to delete a DRG route table, verify that no attachments in the DRG use that route table.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-delete.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to the DRG route tables section.
- Under Resources , select DRG route tables .
- From the Actions menu (three dots) for the DRG route table, select Delete .
- When prompted, confirm the deletion.
The route table is briefly in the Terminating state. When the process is complete it's removed from the list of route tables entirely.
- 

Use the[network drg-route-table delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/delete.html)command and required parameters to delete the specified DRG route table:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternalPublicIp/DeleteDrgRouteTable)
