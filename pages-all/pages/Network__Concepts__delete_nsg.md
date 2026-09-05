# Deleting an NSG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm
- Fetched: 2026-09-05 02:41 CDT

# Deleting an NSG

Delete a network security group (NSG) from a Virtual Cloud Network (VCN).

To delete an NSG, it must not contain any VNICs or parent resources. When a parent resource (or a compute instance VNIC) is deleted, it's automatically removed from the NSGs it was in. You might not have permission to delete a particular parent resource. Contact your administrator to determine who owns a given resource.

The Console displays a list of parent resources that are in an NSG, with a link to each parent resource. If the parent resource is a compute instance, the Console also displays the instance's VNIC or VNICs that are in the NSG.

To remove a parent resource from its NSGs without deleting the resource, first view the parent resource's details in the Console. There you can see a list of the NSGs that the resource belongs to. From there, you can click Edit and remove the resource from all NSGs. If you're instead working with a compute instance, view the details of the specific VNIC that you want to remove from the NSGs.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the NSG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Network Security Groups section.
- Under Resources , select Network Security Groups .
- From the Actions menu (three dots) for the NSG, select Terminate .
- When prompted, confirm the deletion.
- 

Use the[network nsg delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/delete.html)command and required parameters to delete an NSG:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

If you're using the REST API, the`ListNetworkSecurityGroupVnics`operation lists the parent resources and VNICs in an NSG. Use the resource's Update operation to remove the resource from the NSGs. For example, for a Compute instance, use the`UpdateVnic`operation . For a load balancer, use the`UpdateNetworkSecurityGroups`operation, and so on.

Run the[DeleteNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/DeleteNetworkSecurityGroup)
