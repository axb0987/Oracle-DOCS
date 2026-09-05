# Creating a Local Peering Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a Local Peering Gateway

Create a local peering gateway (LPG) that instances, load balancers, and other resources can use to connect to resources in other virtual cloud networks (VCNs) in the same Oracle Cloud Infrastructure (OCI) region.

LPGs require a specific IAM policy setting. After you create an LPG, you must establish a connection to another LPG, and configure routing rules and security settings before the VCN can connect to resources in another VCN.

The administrator of each VCN that you're trying to peer with creates an LPG for their own VCN. "You" in the following procedure means an administrator (either the[acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan)).

Required IAM Policy to Create LPGs

If both administrators already have broad network administrator permissions (see[Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete LPGs. Otherwise, here's an example policy giving the necessary permissions to a group called`LPGAdmins`. The second statement is required because creating an LPG affects the VCN that it belongs to, so the administrator must have permission to manage VCNs.

```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to create a local peering gateway in. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Gateways tab, go to the Local Peering Gateways section and select Create Local Peering Gateway .
- Under Resources , select Local Peering Gateways and then select Create Local Peering Gateway .
- Enter a friendly name for the gateway. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the gateway in. Select another compartment if needed.
- (Optional) In the Route Table Association section, you can associate a specific route table with this gateway. Specify this option only if you're setting up the advanced routing scenario called[transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm). Select the compartment that contains the route table that you want to associate with the LPG, and then select the route table. You can skip this part and associate the LPG with a route table later.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create Local Peering Gateway .

The LPG is then created and displayed on the Local Peering Gateways list. The next step in creating a local peering is to[share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info)with the administrator of the other VCN, because they also need to create an LPG for their VCN.
- 

Use the[network local-peering-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/create.html)command and required parameters to create an LPG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/CreateLocalPeeringGateway)
