# Deleting a DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting a DRG

Delete a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

Prerequisites:
- The DRG can't be attached to a VCN.
- The DRG can't be connected to another network by way of Site-to-Site VPN, FastConnect, or remote peering.
- The DRG can't be listed as a target in a[route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm#)
- 

To delete a DRG, follow these steps:

- On the Dynamic Routing Gateways list page, find the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- From the Actions menu (three dots) for the DRG you want to delete, select Terminate .
- When prompted, confirm the deletion.

The DRG is in the Terminating state for a short period while it's being deleted. The DRG route tables and DRG route distributions contained in the DRG are also deleted.
- 

Use the[network drg delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/delete.html)command and required parameters to delete a DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/DeleteDrg)
