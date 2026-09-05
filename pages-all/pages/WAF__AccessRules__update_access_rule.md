# Editing an Access Rule for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/update_access_rule.htm
- Fetched: 2026-09-05 03:09 CDT

# Editing an Access Rule for an Edge Policy

Use Web Application Firewall to edit access rules for an Edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/update_access_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/update_access_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/update_access_rule.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- On the Policies page, select the compartment that contains the policy.
- (Optional) Filter the listed policies by name, state (status), policy type ( Edge policy ), or creation date.
- Select the name of the edge policy that you want to edit.
- On the policy details page, under Edge policy , select Access control .
- Select the Access rules tab.
- Select the checkbox for the access rule you want to edit, and then select Edit .
- In the Edit access rule dialog box, edit the access rule.

For a description of the access rule settings, see[Adding an Access Rule to an Edge Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/create_access_rule.htm#top).
- Select Save .

The access rule you that edited appears in the Access rules list with the updates that you made. For changes to take effect, you must publish them. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/../Bot/publishing_changes.htm#PublishChanges).
- 

Enter the following command and required parameters:

```

```

The`access-rules`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

Update an access rule by changing the properties of the access rule object with the rule's key specified in the`key`field. Reorder access rules by changing the order of the access rules in the list when updating.

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas access-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/access-rule/update.html)command.
- 

Use the[UpdateAccessRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/AccessRule/UpdateAccessRules)operation to edit an address rule using the API.

Update an access rule by changing the properties of the access rule object with the rule's key specified in the`key`
