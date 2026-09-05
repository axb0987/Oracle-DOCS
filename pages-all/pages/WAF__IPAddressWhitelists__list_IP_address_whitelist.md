# Listing Edge Policy IP Address Allowlists
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/list_IP_address_whitelist.htm
- Fetched: 2026-09-05 03:10 CDT

# Listing Edge Policy IP Address Allowlists

Describes how to list the IP address allowlists for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/list_IP_address_whitelist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/list_IP_address_whitelist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/list_IP_address_whitelist.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- Select the name of the edge policy for which you want to add an IP address allowlist.

The Details page of the edge policy you selected appears.
- Select Access Control under WAF Policy .

The Access Control list appears.
- Select the IP Whitelist tab.
The IP Address Whitelist list appears.

All the IP address allowlists for the edge policy are listed in tabular form.
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas whitelists list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/whitelist/list.html)command.
- 

Use the[ListWhitelists](https://docs.oracle.com/iaas/api/#/en/waas/latest/Whitelist/ListWhitelists)
