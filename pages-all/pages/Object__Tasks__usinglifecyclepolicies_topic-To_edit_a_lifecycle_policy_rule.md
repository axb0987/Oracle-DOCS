# Editing the Object Lifecycle Policy in Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm
- Fetched: 2026-09-05 02:51 CDT

# Editing the Object Lifecycle Policy in Object Storage

Update the object lifecycle policy for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_edit_a_lifecycle_policy_rule.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Policies and find the Lifecycle policy rules section.
All lifecycle policy rules are displayed in a table.
- From the Actions menu for the lifecycle policy rule you want, select Edit .
- Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see[Creating the Object Lifecycle Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)for descriptions of the settings.
- Select Update .
- 

Use the[oci os object-lifecycle-policy put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/put.html)command and required parameters to edit the object lifecycle policy for a bucket:

```

```

Running this command for an existing lifecycle policy replaces the existing policy rules with an updated version that includes whatever changes to the configuration you make. See[Creating an Object Storage Object Lifecycle Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)for more information on configuring a lifecycle policy for a bucket.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[PutObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/PutObjectLifecyclePolicy)operation to edit the object lifecycle policy for a bucket. Running this operation for an existing lifecycle policy replaces the existing policy rules with an updated version that includes whatever changes to the configuration you make.

See[Creating an Object Storage Object Lifecycle Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)
