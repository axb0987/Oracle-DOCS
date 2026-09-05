# Adding External Access to a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-add-external-access.htm
- Fetched: 2026-09-05 03:09 CDT

# Adding External Access to a VMware Solution SDDC VLAN

Add external access to a VLAN. Assign a private IP address to use as a route target to the VLAN or assign a public IP address to allow internet access.

## Using the Console

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- Select Add external access .
- Specify the type of access to configure:

- Route target only : Select this option to assign a private IP address only for use as a route target for traffic that needs to reach the VMware overlay. The IP address must be within the VLAN gateway CIDR block. If you don't specify a name, a private IP address, or both, Oracle generates the needed values for you.
- Private IP address : (Optional) Specify a name and a private IP address within the VLAN gateway CIDR block. If you don't specify these values, Oracle generates them for you.
- Public access : Select this option to also provide a public IP address for internet access to the resources such as VNICs and VMs in the VLAN. The public IP address must be attached to a private IP address to enable internet access.
- Private IP address : (Optional) Specify a name and a private IP address within the VLAN gateway CIDR block. If you don't specify these values, Oracle generates them for you. Note that as with the route target only option, this private IP address can also be used as a route target for noninternet traffic.
- Reserved public IP address : Select whether to specify an existing reserved public IP address or have a new one created for this external access.
-
