# Creating a Remote Peering Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm
- Fetched: 2026-09-05 02:44 CDT

# Creating a Remote Peering Connection

Create a new remote peering connection (RPC) for a specified DRG.

To establish remote peering, each administrator creates an RPC object for a DRG, which includes a DRG attachment with the RPC type. "You" in the following procedure means an administrator (either the[acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)).
Note  
  

Required IAM Policy to Create RPCs

If the administrators already have broad network administrator permissions (see[Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete RPCs. Otherwise, here's an example policy giving the necessary permissions to a group called RPCAdmins. The second statement is required because creating an RPC affects the DRG it belongs to, so the administrator must have permission to manage DRGs.

```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Attachments tab, go to the Remote peering connection attachments section.
- Under Resources , select Remote peering connection attachments .
- Select Create Remote Peering Connection .
- Enter the following:

- Name: A friendly name for the RPC. It doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
- Create in compartment : The compartment where you want to create the RPC, if different from the compartment you're working in.
- Select Create Remote Peering Connection .
The RPC is then created and displayed on the Remote Peering Connections page in the compartment you chose.
- If you're the acceptor, record the RPC's region and OCID and give that information to the requestor.
- 

Use the[network remote-peering-connection create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/create.html)command and required parameters to create a new RPC for a specified DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateRemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/CreateRemotePeeringConnection)
