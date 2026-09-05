# Deleting an Access Rule from an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/delete_access_rule.htm
- Fetched: 2026-09-05 03:09 CDT

# Deleting an Access Rule from an Edge Policy

Use Web Application Firewall to delete access rules from an Edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/delete_access_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/delete_access_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/delete_access_rule.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- On the Policies page, select the compartment that contains the policy.
- (Optional) Filter the listed policies by name, status (status), policy type ( Edge policy ), or creation date.
- Select the name of the Edge policy that you want to delete.
- On the policy details page, under Edge policy , select Access control .
- Select the Access rule tab.
- Select the checkbox for one or more access rules that you want to delete, and then select Delete .
- Confirm the deletion.

The Access rules list no longer includes the access rules that you deleted.

For changes to take effect, you must publish them. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/AccessRules/../Bot/publishing_changes.htm#PublishChanges).
- 

Enter the following command and required parameters:

```

```

The`access-rules`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

Any existing access rules that you do not specify with a key in the list of access rules are deleted upon update.

See the CLI online help for a list of optional parameters:

```

```

Refer to the Oracle Cloud Infrastructure documentation for a complete description of the[oci waas access-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/access-rule/update.html)command.
- 

Use the[UpdateAccessRules](https://docs.oracle.com/iaas/api/#/en/waas/latest/AccessRule/UpdateAccessRules)operation to edit an address rule using the API.
