# Connecting to Another LPG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm
- Fetched: 2026-09-05 02:43 CDT

# Connecting to Another LPG

Connect a local peering gateway (LPG) to another one in a different virtual cloud network (VCN) in the same region.

The[requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan)must perform this task, and if the acceptor is in another tenancy you must have the OCID of the acceptor's LPG.

After you peer an LPG to an LPG in another VCN, you can't peer it to a different LPG. For details, see[Repurposing an LPG fails](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#lpg-delete).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm#)
- 

Tip  
  
If you're using the Console and the peering is between two VCNs in the same tenancy: Instead of specifying the acceptor's LPG OCID, you can instead pick the acceptor's VCN and LPG from lists of resources in the tenancy. However, you need to know both the name and compartment of the acceptor's VCN and LPG instead of the LPG's OCID. For reference, see[Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info).

- On the Virtual Cloud Networks list page, select the VCN that contains the requestor LPG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section.
- Under Resources , select Local Peering Gateways .
- For the requestor LPG, select the Actions menu (three dots) , and then select Establish Peering Connection .
- Specify the LPG that you want to peer with:
- If the VCNs are in the same tenancy, perform one of the following actions:

- Select Browse Below , and then select the acceptor's VCN and LPG from the lists provided. Remember that the VCN and LPG each might be in a different compartment than the one you're working in.
- Select Enter Local Peering Gateway OCID , and enter the acceptor LPG's OCID.
- If the VCNs are in different tenancies, select Enter Local Peering Gateway OCID , and enter the acceptor LPG's OCID.
- Select Establish Peering Connection .

The connection is established, and the LPG's state changes to Peered.

At this point, the details of each LPG update to show the Peer VCN CIDR Block value for the other VCN. This is the CIDR of the other VCN across the peering from the LPG. Each administrator can use this information to update the route tables and security rules for their own VCN.
- 

Use the[network local-peering-gateway connect](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/connect.html)command and required parameters to connect this local peering gateway (LPG) to another one in the same region:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ConnectLocalPeeringGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ConnectLocalPeeringGateways)
