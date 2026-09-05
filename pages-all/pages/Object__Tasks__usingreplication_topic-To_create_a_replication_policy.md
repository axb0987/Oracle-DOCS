# Creating an Object Storage Replication Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm
- Fetched: 2026-09-05 02:52 CDT

# Creating an Object Storage Replication Policy

Create a replication policy for an Object Storage source bucket.
Note  
  
A source bucket can only have one replication policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm#)
- 

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, select Policies and find the Replication policy (Source) section.
The replication policy for the selected bucket is displayed in a table.
- Select Create policy .
- Enter the following information:

- Name : Accept the default name or enter your own. Object Storage generates a policy name that reflects the current year, month, day, and time, for example, replication-policy-20200129-2230 . If you change this name, use letters, numbers, dashes, underscores, and periods.
- 

Destination region : Select the OCI region that contain the destination bucket that you want to replicate to from the list. Your tenancy must be subscribed to a region for you to replicate to that region. See[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm)for more information.
- Destination bucket compartment : Select the compartment that contains the bucket you want to use.
- 

Destination bucket : Select the name destination bucket for replication that's available from the compartment you previously selected. Ensure you have the required policy access for the destination bucket.
- Select Create policy .
The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you have the required policies in place, create the replication policy.

After the policy is created, Replication: Enabled (Source) is added to the source bucket information. Objects uploaded to the source bucket after the policy is created are asynchronously replicated to the destination bucket.

The destination bucket's details page shows Replication: Enabled (Destination) and displays the settings for the source bucket's replication policy.
- 

Use the[oci os replication create-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/create-replication-policy.html)command and required parameters to create a replication policy for a bucket:

```

```

For example:
```

```

Objects uploaded to the source bucket after policy creation are asynchronously replicated to the destination bucket.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/CreateReplicationPolicy)
