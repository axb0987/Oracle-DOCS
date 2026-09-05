# Editing an Object Storage Data Retention Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm
- Fetched: 2026-09-05 02:52 CDT

# Editing an Object Storage Data Retention Rule

Update a retention rule for an Object Storage bucket.

You can get the retention rule's ID by running the list command. See[Listing Object Storage Data Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Retention rules section.
- From the Actions menu for the data retention rule you want, select Edit rule .
The Edit retention rule panel opens.
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating a Retention Rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm).
- Select Update .
- 

Use the[oci os retention-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/update.html)command and required parameters to edit a retention rule for a bucket:

```

```

For example:
```

```

In this example, the retention rule has been updated to include values for`time-amount`,`time-unit`, and`time-rule-locked`.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/UpdateRetentionRule)
