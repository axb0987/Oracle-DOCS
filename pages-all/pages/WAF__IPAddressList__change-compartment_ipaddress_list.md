# Moving an Edge Policy IP Address List Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/change-compartment_ipaddress_list.htm
- Fetched: 2026-09-05 03:10 CDT

# Moving an Edge Policy IP Address List Between Compartments

Move an IP address list for an edge policy in the Web Application Firewall service to another compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/change-compartment_ipaddress_list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/change-compartment_ipaddress_list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/change-compartment_ipaddress_list.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Under OCI Edge policy resources , select IP address lists .
- Select the compartment that contains the IP address list.
- Select the name of the IP address list that you want to move.
- In the IP Address lists details page, select Move resource .
- In the Move resource dialog box, select the compartment to which you want to move the IP address list.
- Select Move resource .
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas address-list change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/address-list/change-compartment.html)command.
- 

Use the[ChangeAddressListCompartment](https://docs.oracle.com/iaas/api/#/en/waas/latest/AddressList/ChangeAddressListCompartment)
