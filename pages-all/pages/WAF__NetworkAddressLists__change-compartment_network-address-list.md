# Moving a Web Application Firewall Network Address List to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/change-compartment_network-address-list.htm
- Fetched: 2026-09-05 03:10 CDT

# Moving a Web Application Firewall Network Address List to a Different Compartment

Move a network address list contained within a web application firewall (WAF) policy to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/change-compartment_network-address-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/change-compartment_network-address-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/change-compartment_network-address-list.htm#)
- 

- On the Network address lists list page, select the network address list that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Network Address Lists](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#top).
The network address list's details page opens.
- From the Actions menu (three dots) for the network address list, select , Move resource .
- In the Move resource dialog box, select the destination compartment from the list.
The Move resource panel opens.
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci waf network-address-list change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/network-address-list/change-compartment.html)command and required parameters to move a network address list contained within a web application firewall policy between compartments:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[
