# Listing Private IP Addresses
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm
- Fetched: 2026-09-05 02:46 CDT

# Listing Private IP Addresses

View a list of all private IP addresses for an instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab.
The IP addresses associated with the VNIC are listed in tabular form.
- 

Use the[private-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/list.html)command and required parameters to list private IP addresses for an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListPrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps)
