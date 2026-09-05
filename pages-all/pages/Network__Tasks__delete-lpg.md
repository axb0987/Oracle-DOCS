# Deleting an LPG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm
- Fetched: 2026-09-05 02:43 CDT

# Deleting an LPG

Delete a local peering gateway (LPG) from a Virtual Cloud Network (VCN) in Networking.

Prerequisite: Before you delete an LPG, delete all route rules in the VCN that specify the LPG as the target. Deleting those rules stops the routing in the VCN to the LPG. If a route rule refers to the LPG, it can't be deleted until the reference is removed.

See[Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm)and[Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm)for more about finding and updating route rules that reference a gateway.

After deletion, the LPG's state could still be PEERED if the other LPG still exists. Whenever an LPG is deleted, the LPG at the other side of the peering changes to the REVOKED state.
Note  
  

After deleting an LPG, ensure that the other LPG in the peering (in the other VCN) is removed. That LPG can't be peered again. See[Repurposing an LPG fails](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Troubleshoot/vcn_troubleshooting.htm#lpg-delete)for more detail.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the gateway that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section.
- Under Resources , select Local Peering Gateways .
- From the the Actions menu (three dots) for the gateway that you want to delete, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network local-peering-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/delete.html)command and required parameters to delete an LPG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/DeleteLocalPeeringGateway)
