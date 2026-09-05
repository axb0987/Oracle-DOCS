# Getting an Object Storage Data Retention Rule's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm
- Fetched: 2026-09-05 02:52 CDT

# Getting an Object Storage Data Retention Rule's Details

View a retention rule's details for an Object Storage bucket.

You can get the retention rule's ID by running the list command. See[Listing Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Retention rules section.
- From the Actions menu for the data retention rule you want, select View rule details .

The Retention rules details panel opens. You can view the details for the retention rule, such as its retention duration lock state, scheduled lock time, and when it was last changed.
- 

Use the[oci os retention-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/list.html)command and required parameters to get the details of a retention rule for a bucket:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/GetRetentionRule)
