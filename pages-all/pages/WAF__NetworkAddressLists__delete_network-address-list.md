# Deleting a Web Application Firewall Network Address List
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/delete_network-address-list.htm
- Fetched: 2026-09-05 03:10 CDT

# Deleting a Web Application Firewall Network Address List

Remove a network address list from a web application firewall (WAF) policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/delete_network-address-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/delete_network-address-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/delete_network-address-list.htm#)
- 

- On the Network address lists list page, select the network address list that you want to work with. If you need help finding the list page or the policy, see[Listing Web Application Firewall Network Address Lists](https://docs.oracle.com/en-us/iaas/Content/WAF/NetworkAddressLists/list_network-address-list.htm#top).
The network address list's details page opens.
- From the Actions menu (three dots) for the network address list, select Delete .
- When prompted, confirm the deletion.
The Network address lists list page refreshes. The status of the network address list that you deleted changes to Deleted .
- 

Use the[oci waf network-address-list delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waf/network-address-list/delete.html)command and required parameters to delete a network address list from a web application firewall policy:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[
