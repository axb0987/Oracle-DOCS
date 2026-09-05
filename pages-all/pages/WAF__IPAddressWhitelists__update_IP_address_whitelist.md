# Editing an Edge Policy IP Address Allowlist
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/update_IP_address_whitelist.htm
- Fetched: 2026-09-05 03:10 CDT

# Editing an Edge Policy IP Address Allowlist

Describes how to edit IP address allowlists for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/update_IP_address_whitelist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/update_IP_address_whitelist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/update_IP_address_whitelist.htm#)
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
- Select the Actions menu (three dots) for the IP address allowlist you want to edit and select Edit .

The Edit IP Address Whitelist dialog box appears.
- Edit the IP address allowlist.

See[Adding an Edge Policy IP Address Allowlist](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/create_IP_address_whitelist.htm#top)for a description of the IP address allowlist settings.
- Select Save Changes .

The Edit IP Address Whitelist dialog box closes. The IP address allowlist you edited appears in the IP Address Whitelist list with the updates you made.

Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/IPAddressWhitelists/../Bot/publishing_changes.htm#PublishChanges).
- 

Enter the following command and required parameters:

```

```

The`whitelists`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

Update an IP address allowlist by changing the properties of the allowlist object with the rule's key specified in the`key`field. Reorder allowlists by changing the order of the allowlists in the list of objects when updating.

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas whitelists update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/whitelist/update.html)command.
- 

Use the[UpdateWhitelists operation to edit an IP address allowlist using the API.

Update an IP address allowlist by changing the properties of the allowlist object with the rule's key specified in the`key`
