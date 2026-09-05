# Creating a DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm
- Fetched: 2026-09-05 02:43 CDT

# Creating a DRG

Create a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

A DRG acts as a virtual router that provides a path for traffic between on-premises networks and virtual cloud networks (VCNs), and can also be used to route traffic between VCNs. Using different types of attachments, custom network topologies can be constructed using components in different regions and tenancies. Each DRG attachment has an associated route table used to route packets entering the DRG to their next hop. In addition to static routes, routes from the attached networks are dynamically imported into DRG route tables using optional import route distributions.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.
Note  
  
A DRG created before April 2021 can't perform transit routing between on-premises networks and several VCNs, or provide peering between VCNs. If you require that functionality and you see an Upgrade DRG button, select it. Upgrading the DRG resets all existing Border Gateway Protocol (BGP) sessions and temporarily interrupts traffic from the on-premises network. After the upgrade starts, you can't roll it back. See[Upgrading a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm).

For more information about DRGs, read[Working with DRGs and DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__drg_attach).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#)
- 

- On the Dynamic Routing Gateways list page, select Create dynamic routing gateway . If you need help finding the list page, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- Enter the following values:

- Name: A descriptive name for the DRG. It doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
- Create in compartment: The compartment in which you want to create the DRG, which could be different from the compartment you're working in.
- (Optional) Expand and enter information for Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create dynamic routing gateway .

The new DRG is created and then displayed on the Dynamic routing gateways list page of the compartment you chose. The new DRG is in the Provisioning state for a short period. You can connect it to one or more VCNs or DRGs after provisioning is complete.
Note  
  
When you create a DRG, as part of provisioning two default route tables are created for you: one for VCN attachments and one for all other attachments (such as virtual circuits and IPSec tunnels). This matches the default routing behavior used by legacy DRGs created before May 2021. See[Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt)for more about route tables.
- 

Use the[network drg create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/create.html)command and required parameters to create a DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/CreateDrg)
