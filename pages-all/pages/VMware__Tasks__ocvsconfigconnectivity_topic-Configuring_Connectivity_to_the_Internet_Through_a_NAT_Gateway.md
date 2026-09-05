# Connecting a VMware Solution SDDC to the Internet
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsconfigconnectivity_topic-Configuring_Connectivity_to_the_Internet_Through_a_NAT_Gateway.htm
- Fetched: 2026-09-05 03:08 CDT

# Connecting a VMware Solution SDDC to the Internet

Use a quick action workflow in the Console to connect your SDDC to the internet through a NAT gateway.

The workflow for configuring connectivity between your SDDC and the internet through a NAT gateway does the following:
- Determines whether the VCN has a NAT gateway, and if not, helps you create one.
- Adds a default route rule to the SDDC's NSX Edge Uplink1 VLAN's route table to send traffic to the internet through the NAT gateway.
Note  
  
The workflow adds a required route rule to the VLAN's route table. If you have reached your route rule limits, you are prompted to check your existing rules and delete one to free up capacity.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

## Using the Console

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the details page, select Configure connectivity to the internet through NAT gateway .
- Review the details of the planned updates to your networking resources.

If you disallow an update, your SDDC might not have internet connectivity through the NAT gateway. To complete the configuration, you can either return to the workflow later or make the required resource update manually outside of the workflow.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. To see the tagging options, select Show Advanced Options . The tags you specify are applied to all of the new resources created in this workflow.
- When you are satisfied with the configuration settings, select Apply Configuration .
