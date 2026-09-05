# Removing External Access to a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-remove-external-access.htm
- Fetched: 2026-09-05 03:09 CDT

# Removing External Access to a VMware Solution SDDC VLAN

You can remove external access from a VLAN.

Important  
  

If an existing route rule targets the private IP address associated with the external access you're removing, the route rule drops traffic to that private IP address.

## Using the Console

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- In the External Access list, find the external access that you want to remove.
- From the Actions menu (three dots) for the external access, select Remove .
-
