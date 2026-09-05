# Managing Layer 2 Networking Resources for a VMware Solution SDDC
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/ocvsmanagingl2net.htm
- Fetched: 2026-09-05 03:09 CDT

# Managing Layer 2 Networking Resources for a VMware Solution SDDC

Manage the layer 2 networking resources for SDDCs in VMware Solution.

An Oracle Cloud Infrastructure SDDC requires a management subnet and layer 2 networking resources. The layer 2 networking resources include seven virtual local area networks (VLANs) and their configured external access objects.

When you provision an SDDC by using the Create SDDC workflow in the Console, you can have the workflow create these required networking resources for you. We recommend that you select this option. If you prefer, you can create them yourself before you start the Create SDDC workflow, and then select the existing subnet and VLANs you created for this purpose. See[Creating a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm)for a list of VLANs required for SDDCs and instructions on how to create them.

You can enable external access to an SDDC's ESXi hosts by creating a private IP object for the VLAN that can be used as a route target. Also, you can enable internet access to hosts in the VLAN by assigning a public IP address to the VLAN's private IP address object. When you configure external access, you have the option to indicate that it be accessible as a route target only and, as such, have no associated public IP address. See[Adding External Access to a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-add-external-access.htm)for the steps to configure external access.

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For more information and examples of OCI IAM policies you can use to create, modify, and delete VMware Solution resources, see[VMware Solution Identity and Access Management (IAM) Policies](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Reference/iam-policy-reference.htm).

## VLAN Tasks
You can perform the following VLAN management tasks:
- [Listing a VMware Solution SDDC's VLANs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-list.htm)
- [Creating a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm)
- [Getting a VMware Solution SDDC VLAN's Details](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-get.htm)
- [Editing a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-update.htm)
- [Moving a VMware Solution SDDC VLAN Between Compartments](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-move.htm)
- [Adding External Access to a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-add-external-access.htm)
- [Changing External Access to a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-modify-external-access.htm)
- [Removing External Access to a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-remove-external-access.htm)
- [Deleting a VMware Solution SDDC VLAN](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-delete.htm)
