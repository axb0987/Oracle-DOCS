# Creating a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm
- Fetched: 2026-09-05 03:09 CDT

# Creating a VMware Solution SDDC VLAN

Learn how to create a VLANs that are required for a VMware Solution SDDC.

We recommend that you create a size /21 CIDR network segment in the VCN for the SDDC's networking resources. Divide the SDDC CIDR into ten segments of size /25 to use for the subnet and the nine required VLANs.

If you're enabling HCX, further divide the segment for the vSphere VLAN into two equal segments, one for vSphere and the other for HCX.

Configure the security rules for these networking resources as detailed in[VMware Solution SDDC Security Rules](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Reference/ocvssecurityrules.htm). Otherwise, provisioning the SDDC fails.
An SDDC requires VLANs for the following functions:

Function Description
NSX Edge Uplink 1 The first of two uplinks used for communication between the VMware SDDC and Oracle Cloud Infrastructure.
NSX Edge Uplink 2 Reserved for future use to deploy public-facing applications on the VMware SDDC.
NSX Edge VTEP Used for data plane traffic between the ESXi host and NSX Edge.
NSX VTEP Used for data plane traffic between ESXi hosts.
vMotion Used for vMotion (VMware migration tool) management and workload.
vSAN Used for vSAN (VMware storage) data traffic.
vSphere Used for management of the SDDC components (ESXi, vCenter, NSX-T, and NSX Edge).
Replication-Net Used for the vSphere Replication engine. (VMware version 7.x only)
Provisioning-Net Used for virtual machine cold migration, cloning, and snapshot migration.
HCX: (Optional) Used for HCX traffic. Create this VLAN if you plan to enable HCX when you provision the SDDC.

Note  
  
HCX requires that the vSphere VLAN has a route table rule that allows traffic to a NAT gateway attached to the VCN. See[Intra-VCN Routing](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__intra_vcn)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-create.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select Create VLAN .
- Enter the following information for the VLAN:

Field Description
Name (Optional) A descriptive name for the VLAN. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
Create in Compartment The compartment for the VLAN.
VLAN Type A VLAN can be either Regional or Availability Domain-specific . Regional VLANs are useful for high availablity. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for more information.
Availability Domain If you choose to create an Availability domain-specific VLAN, select the Availability domain. The ESXi hosts must be in the same Availability domain as the SDDC's VLANs.
IEEE 802.1Q VLAN Tag (Optional) The VLAN uses this unique value to identify a broadcast domain for layer 2 traffic. Enter a number from 1 to 4094. If you don't enter a value, Oracle assigns one. You can't change this value later.
VLAN Gateway CIDR

This CIDR provides IP addresses used by the VLAN for external layer 3 communication and routing. This CIDR block also provides the private IP addresses Oracle uses as attachment objects for public IP addresses when instances require access to internet hosts. You can't change this value later.

This CIDR must be within the VCN's CIDR and can't overlap with the CIDRs of the other subnets and VLANs in the VCN.
Route Table The route table contains rules that specifiy the next hop for traffic from the VLAN to external destinations.
Network Security Groups

Select the NSGs with the security rules to apply to all VNICs in this VLAN. You can select up to 5 NSGs for a VLAN.

You manage NSG membership for VNICs in a VLAN at the VLAN level. You can't add or remove individual VNICs in a VLAN from an NSG.

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. If you don't see the tagging option, select Show Advanced Options .
- Select Create VLAN .

The new VLAN displays in the list of VLANs for the VCN in the selected compartment.
- Repeat steps 5 through 7 for each VLAN you need for the SDDC.
- 

Use the[vlan create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vlan/create.html)command and required parameters to create a VLAN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVlan](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vlan/CreateVlan)
