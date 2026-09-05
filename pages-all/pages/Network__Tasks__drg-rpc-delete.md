# Deleting a Remote Peering Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm
- Fetched: 2026-09-05 02:44 CDT

# Deleting a Remote Peering Connection

Delete a remote peering connection (RPC).

Deleting an RPC also ends the peering connection. The RPC at the other side of the peering changes to the REVOKED state.

This is an asynchronous operation. The RPC's lifecycleState changes to Terminating temporarily until the RPC is removed.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the Remote peering connection attachments section.
- Under Resources , select Remote peering connection attachments .
- In the table, select the name of the RPC you're interested in.
- On the RPC details page, perform one of the following actions depending on the option that you see:

- Select Actions and then Terminate .
- Select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network remote-peering-connection delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/delete.html)command and required parameters to delete an RPC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteRemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/DeleteRemotePeeringConnection)
