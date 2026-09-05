# Deleting an Object Storage Data Retention Rule
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm
- Fetched: 2026-09-05 02:52 CDT

# Deleting an Object Storage Data Retention Rule

Delete a retention rule from an Object Storage bucket.

You can get the retention rule's ID by running the list command. See[Listing Object Storage Data Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Retention rules section.
- From the Actions menu for the data retention rule you want, select Delete rule .
- When prompted, confirm the deletion.
The retention rule you deleted to longer appears in the Retention rules list.
- 

Use the[oci os retention-rule delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/delete.html)command and required parameters to delete a retention rule from a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteRetentionRule](https://docs.oracle.com/iaas/api/#23/en/objectstorage/latest/RetentionRule/DeleteRetentionRule)
