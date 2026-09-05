# Getting an Object Storage Object Lifecycle Policy's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm
- Fetched: 2026-09-05 02:51 CDT

# Getting an Object Storage Object Lifecycle Policy's Details

View the details of the object lifecycle policy for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the bucket's details page, select Policies and find the Lifecycle policy rules section.
All lifecycle policy rules are displayed in a table.
- From the Actions menu for the lifecycle policy rule you want, select View lifecycle rule details .

The Lifecycle rule details panel opens. Here you can view the lifecycle rule's details, such as the target type and lifecycle action.
- 

Use the[oci os object-lifecycle-policy get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/get.html)command and required parameters to get the object lifecycle policy configuration for a bucket.

```

```

For example:
```

```

For example, to get the lifecycle policy that archives objects after 30 days:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/GetObjectLifecyclePolicy)
