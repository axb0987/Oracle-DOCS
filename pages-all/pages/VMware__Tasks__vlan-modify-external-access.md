# Changing External Access to a VMware Solution SDDC VLAN
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/vlan-modify-external-access.htm
- Fetched: 2026-09-05 03:09 CDT

# Changing External Access to a VMware Solution SDDC VLAN

Learn how to change external access to a VLAN. Change the access type or add or rename IP addresses.

## Using the Console

- On the Virtual Cloud Networks list page, select the VCN that contains the VLANs that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/iaas/Content/Network/Tasks/list-vcn.htm).
- Select VLANs .
- Select the VLAN that you want to work with.
- In the External Access list, find the external access that you want to change.
- From the Actions menu (three dots) for the external access, select Edit .

The settings you can change depend on the external access type. Consider the following:
- 

You can change the external access type from route target only to public access , or the other way around.

If you change the type from public access to route target only , the private IP address will no longer have an associated reserved IP address. Therefore, any host that uses the private IP address will not be accessible from the internet.

If you change the type from route target only to public access , you'll need to attach a reserved public IP address to it to enable access from the internet. You can select an existing public IP address or have a new one created for this purpose.
- For both route target only and public access types, you can rename the private IP address but you can't change the IP address value itself.
- For a public access type, you can rename the reserved public IP address but you cannot change the IP address value itself.
-
