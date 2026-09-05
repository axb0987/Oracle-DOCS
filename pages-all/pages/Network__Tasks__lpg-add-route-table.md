# Associating a Route Table with an Existing LPG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm
- Fetched: 2026-09-05 02:45 CDT

# Associating a Route Table with an Existing LPG

To use transit routing, you must associate a route table to an LPG after you create the LPG.

Prerequisite: The route table must exist and belong to the VCN that the LPG belongs to.

This task is related to an advanced routing scenario called[transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm). Associating a route table to an LPG influences the behavior of traffic entering the VCN through the LPG.

An LPG can exist without having an associated route table. After you associate a route table with an LPG there must always be a route table associated with it, but you can associate a different route table. You can also edit the table's rules, or delete some or all rules.
Note  
  
The route rules in a route table associated with an LPG can point to a DRG or a private IP address in the same VCN as the LPG.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the requestor LPG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section.
- Under Resources , select Local Peering Gateways .
- For the LPG you're interested in, select the Actions menu (three dots) , and then select either:

- Associate With Route Table: If the LPG has no route table associated with it yet.
- Replace Route Table Association: If you're changing which route table is associated with the LPG.
- Select the compartment where the route table resides.
- Select the route table itself.
- Select Associate .
- 

Use the[network local-peering-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/update.html)command and required parameters to change the name and associated route table of a local peering gateway (LPG):

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/UpdateLocalPeeringGateway)operation to set the`routeTableId`
