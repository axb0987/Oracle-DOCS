# Creating an Edge Policy IP Address List
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/create_ipaddress_list.htm
- Fetched: 2026-09-05 03:10 CDT

# Creating an Edge Policy IP Address List

Create an IP address list for an edge policy in Web Application Firewall.

This task creates an address list in a specified compartment and allows it to be used in a Web Application Acceleration and Security (WAAS) policy and referenced by access rules. Addresses can be IP addresses and CIDR notations.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/create_ipaddress_list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/create_ipaddress_list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressList/create_ipaddress_list.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Under OCI Edge policy resources , select IP address lists .
- Select the compartment that you have permission to work in. The IP address list that you create resides in this compartment.
- Select Create IP address list .
- In the Create IP address list dialog box, complete the options as follows:

- Name : Enter a name for the IP address list.
- IP addresses : Enter IP addresses or CIDR notations.
- Show advanced options : Select this link to display options for tagging the IP address list. See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
- Choose one of the following:

- To create the IP address list, select Create .
- To create the IP address later using Resource Manager, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

Enter the following command and required parameters:

```

```

The`addresses`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas address-list create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/address-list/create.html)command.
- 

Use the[CreateAddressList](https://docs.oracle.com/iaas/api/#/en/waas/latest/AddressList/CreateAddressList)
