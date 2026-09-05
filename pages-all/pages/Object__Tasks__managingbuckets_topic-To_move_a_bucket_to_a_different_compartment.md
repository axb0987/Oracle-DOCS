# Moving an Object Storage Bucket to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm
- Fetched: 2026-09-05 02:51 CDT

# Moving an Object Storage Bucket to a Different Compartment

Move an Object Storage bucket to a different compartment in your Oracle Cloud Infrastructure tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- To view the buckets in a different compartment, use the Compartment filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- From the Actions menu for the bucket, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to move the bucket to a different compartment:

```

```

where`destination_compartment_ocid`is the compartment OCID associated with the destination compartment for the bucket you're moving.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket)operation with the`compartmentID`of the destination compartment to move a bucket to a different compartment.

When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```

```
