# Creating a Web Application Firewall Network Address List
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/create_network-address-list.htm
- Fetched: 2026-09-05 03:10 CDT

# Creating a Web Application Firewall Network Address List

Create a network address list for a web application firewall (WAF) policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/create_network-address-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/create_network-address-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/create_network-address-list.htm#)
- 

- On the Network address lists list page, select Create network address list . If you need help finding the list page or the policy, see[Listing Web Application Firewall Network Address Lists](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#top).
The Create network address list panel opens.
- Enter the following information:

- Name : Enter a name for the network address list, or use the default name.
- Create in compartment : Select the compartment to contain the network address list that you're creating.
- Address type : Specify the address type:
- Addresses : Use this type of network address list to match traffic coming from the internet or traffic coming from the same virtual cloud network (VCN) where the associated load balancer is hosted.
- VCN addresses : Use this type of network address list to match traffic coming from other VCNs through service gateways or private endpoints.
- IP addresses :
- If you selected Addresses for the address type, then enter each IP address and CIDR IP range on a separate line within the box.
- If you selected VCN addresses for the address type, then enter the following values:
- Select Use same tenancy VCN to populate the Virtual cloud network list with the VCNs that exist in the compartment selected for the network address list.
- Virtual cloud network : Select the VCN associated with your list of private IP addresses. Select Change Compartment to select a VCN in a different compartment.
- VCN IP addresses : Enter each IP address and CIDR IP range on a separate line within the box.

## Tags

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Create . The policy you created appears in the policy list.
- 

Use the[oci waf network-address-list create-addresses-list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/network-address-list/create-addresses-list.html)command and required parameters to create a network address list for a web application firewall policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[
