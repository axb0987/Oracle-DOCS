# Connecting a VMware Solution SDDC to Other Resources in the VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_Other_Resources_in_the_VCN.htm
- Fetched: 2026-09-05 03:08 CDT

# Connecting a VMware Solution SDDC to Other Resources in the VCN

Use a quick action workflow in the Console to connect your SDDC to other resources in the VCN.

The workflow for configuring connectivity between your SDDC and other resources in the VCN does the following:
- Allows you to select subnets in the VCN that contain resources you want your SDDC to connect to. If the VCN has no subnets, you can use the Networking Wizard from the workflow to create them.
- Adds the route table, rules, or network security groups needed to enable routing between the SDDC's NSX Edge Uplink 1 VLAN and the resources in the selected subnets.
Note  
  
The workflow adds required route rules and security rules to the VCN resources. If you have reached your limits, you're prompted to check your existing rules and delete some to free up capacity.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

## Using the Console

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the details page, select Configure connectivity to VCN resources .
- Enter the SDDC workload CIDR. This CIDR block provides the IP addresses the VMware VMs use to run workloads. The minimum size is /30.
- Select Select Subnets .
- Check the check boxes of the subnets that contain resources your SDDC needs to connect to. You filter and sort the list to help you find the subnets you're interested in.
- Select Save Selection
- Select Next .
- Review the details of the planned updates to your networking resources. The workflow creates or updates route tables and rules that impact the NSX Edge Uplink1 VLAN and the selected subnets.

If you disallow an update, your SDDC might not have connectivity to the resources in a subnet. To complete the configuration, you can either return to the workflow later or make the required resource update manually outside of the workflow.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. To see the tagging options, select Show Advanced Options . The tags you specify are applied to all new resources created in this workflow.
- When you're satisfied with the configuration settings, select Apply Configuration .
