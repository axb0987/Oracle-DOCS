# Connecting Two Remote Peering Connections
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm
- Fetched: 2026-09-05 02:44 CDT

# Connecting Two Remote Peering Connections

Connects an RPC object to an RPC object on another DRG.

Prerequisite: The requestor must have:
- The region the acceptor's VCN is in (the requestor's tenancy must be subscribed to the region).
- The OCID of the acceptor's RPC.

The requestor RPC must perform this task.

When the connection is no longer needed, the RPCs can be disconnected by deleting one of the RPCs.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the Remote peering connection attachments section.
- Under Resources , select Remote peering connection attachments .
- Select the name of the requestor RPC in the table.
- Select Establish Connection .

Enter the following:
- Region: The region that contains the acceptor's VCN. The list includes only those regions that both support remote VCN peering and that the requestor DRG's tenancy is subscribed to.
- Remote Peering Connection OCID: The OCID of the acceptor's RPC.
- Select Establish Connection .

The connection is established and the RPC's state changes to PEERED.
- 

Use the[network remote-peering-connection connect](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/connect.html)command and required parameters to connect an RPC to an RPC on another DRG:

```

```

The region names that could be used for`--peer-region-name`are listed in[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). For example:`us-ashburn-1`.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ConnectRemotePeeringConnections](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/ConnectRemotePeeringConnections)
