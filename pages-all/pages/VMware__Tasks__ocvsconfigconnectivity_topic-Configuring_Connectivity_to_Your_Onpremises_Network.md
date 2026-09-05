# Connecting a VMware Solution SDDC to an On-premises Network
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_Your_Onpremises_Network.htm
- Fetched: 2026-09-05 03:08 CDT

# Connecting a VMware Solution SDDC to an On-premises Network

Use a quick action workflow in the Console to connect your SDDC to an on-premises network.

The workflow for configuring connectivity between your SDDC and an on-premises network does the following:
- Determines whether the VCN has an attached dynamic routing gateway (DRG), and if not, helps you create one.
- Adds the route table, rules, or network security groups needed to enable routing between the DRG and the SDDC's NSX Edge Uplink 1 VLAN.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

## Using the Console

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the details page, select Configure connectivity to your on-premises network
- Use the Networking wizard to set up the DRG, if needed. After the DRG setup is complete, you can continue with the workflow.
- Enter the SDDC workload CIDR. This CIDR block provides the IP addresses the VMware VMs use to run workloads. The minimum size is /30.
- Enter the CIDR of the on-premises network.
- Review the details of the planned updates to your networking resources. The workflow creates or updates route tables and rules that impact the NSX Edge Uplink1 VLAN, vSphere Replication Communication (v7.x only), and the DRG.

If you disallow an update, your SDDC might not have connectivity to your on-premises network. To complete the configuration, you can either return to the workflow later or make the required resource update manually outside of the workflow.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. To see the tagging options, select Show Advanced Options . The tags you specify are applied to all new resources created in this workflow.
- When you're satisfied with the configuration settings, select Apply Configuration .
