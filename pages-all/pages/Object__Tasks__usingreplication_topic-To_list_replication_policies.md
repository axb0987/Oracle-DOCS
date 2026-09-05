# Listing the Object Storage Replication Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm
- Fetched: 2026-09-05 02:52 CDT

# Listing the Object Storage Replication Policy

View a list the replication policy for an Object Storage bucket.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Replication policy (Source) section.
The replication policy for the selected bucket is displayed in a table.
- To view the Object Storage replication policy in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Actions

To perform an action on the Object Storage replication policy directly from the list table, select an available option from the Actions menu in the row for that Object Storage replication policy:
- Delete policy :[Delete the replication policy from the bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm).

To create a Object Storage replication policy, select Create policy .
Note  
  
A source bucket can only have one replication policy.
- 

Use the[oci os replication list-replication-sources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/list-replication-sources.html)command and required parameters to list the sources of a replication policy for an Object Storage replication destination bucket:

```

```

If you're replicating to a destination bucket in a different region, include the`region`parameter and the region identifier. For example:

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListReplicationPolicies](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/ListReplicationPolicies)
