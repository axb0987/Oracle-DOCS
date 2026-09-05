# Getting a Private IP Address's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm
- Fetched: 2026-09-05 02:46 CDT

# Getting a Private IP Address's Details

View details about a private IP address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- Select the IP administration tab.
The IP addresses associated with the VNIC are listed in tabular form. Details such as associated FQDN and date assigned are displayed.
- To view tagging information for a private IP address, select its Actions menu (three dots) and then select Manage tags .
- 

Use the[private-ip get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/get.html)command and required parameters to view details about a private IP address:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetPrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp)
