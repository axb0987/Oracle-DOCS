# Adding an Edge Policy IP Address Allowlist
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/create_IP_address_whitelist.htm
- Fetched: 2026-09-05 03:10 CDT

# Adding an Edge Policy IP Address Allowlist

Describes how to add access IP address allowlists to an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/create_IP_address_whitelist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/create_IP_address_whitelist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/create_IP_address_whitelist.htm#)
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
- Complete the following:

- 

Name : Enter the name for the IP addresses used in the list.
- 

IP Addresses : Enter the trusted IP addresses included in the allowlist. This field supports CIDR notation.
- 

+ Add IP List : (optional): Select to display the Address list in &lt;compartment&gt; list. Select an existing IP address allowlist contained in the compartment. Select Change Compartment to select an IP address allowlist contained in a different compartment.

You can add multiple IP lists. Select the X next to a list to remove it.
- Select Add .

The IP address allowlist is added to the list.

Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/../Bot/publishing_changes.htm#PublishChanges).
- 

Enter the following command and required parameters:

```

```

The`whitelists`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

Create an IP address allowlist by adding a new allowlist object to the list without a`key`property specified. A`key`is generated for the new allowlist upon update.

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas whitelists update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/whitelist/update.html)command.
- 

Use the[UpdateWhitelists](https://docs.oracle.com/iaas/api/#/en/waas/latest/Whitelist/UpdateWhitelists)operation to add an IP address allowlist using the API.

Create an IP address allowlist by adding a new allowlist object to the list without a`key`property specified. A`key`
