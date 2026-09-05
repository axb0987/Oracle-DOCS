# Listing Object Storage Data Retention Rules
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm
- Fetched: 2026-09-05 02:52 CDT

# Listing Object Storage Data Retention Rules

View a list of the retention rules for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Retention rules section.
The Retention rules list opens. All data retention rules in the selected bucket are displayed in a table.
- To view the Object Storage data retention rules in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Actions

In the list table, select the name of a data retention rule to open its details page, where you can view its status and perform other tasks.

To perform an action on a data retention rule directly from the list table, select an available option from the Actions menu in the row for that data retention rule:
- View rule details : Open the details page for the data retention rule.
- Edit rule :[Edit the settings of the data retention rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm).
- Delete rule :[Delete the data retention rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm).

To create a data retention rule, select Create rule .
- 

Use the[oci os retention-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/list.html)command and required parameters to list the retention rules for a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListRetentionRules](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/ListRetentionRules)
