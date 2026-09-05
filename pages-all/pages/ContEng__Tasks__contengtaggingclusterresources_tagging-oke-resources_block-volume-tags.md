# Applying Tags to Block Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_block-volume-tags.htm
- Fetched: 2026-09-05 01:56 CDT

# Applying Tags to Block Volumes

Find out how to apply tags to block volume resources, and how to override initial block volume tags, when using Kubernetes Engine (OKE).

When you create a cluster, you can optionally define tags to apply to block volumes created when persistent volume claims (PVCs) are defined. These tags are referred to as initial block volume tags . You can specify both defined tags and free-form tags as initial block volume tags.

You can override the initial block volume tags by defining a new Kubernetes storage class that includes tag parameters, and then using this storage class to create PVCs (see[Overriding Initial Block Volume Tags](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_block-volume-tags.htm#contengtaggingclusterresources_tagging_oke_resources_block_volume_tags__block-volume-tag-override-parameters)). If you use a storage class that includes tag parameters, none of the initial block volume tags specified in the cluster definition are applied to block volumes. Instead, the tags set in the storage class are applied to the block volume resources.

Tag defaults with default values that are specified for the compartment are automatically applied to the block volume resources as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.

Note the following:
- Tags are only applied to block volumes when the block volumes are first created. If you update the initial block volume tags applied to block volume resources, the changes only apply to new block volumes (assuming the tags are not overridden by parameters in the storage class definition). Tags applied to existing block volumes are unaffected.
- If you apply a cost-tracking defined tag to block volumes, you can include block volume usage in budgets (see[Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm)).
- To apply defined tags from a tag namespace belonging to one compartment to a block volume resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).

## Using the Console to Specify Initial Block Volume Tags

To specify an initial block volume tag to apply to block volume resources created for a new cluster:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- In the Tagging - Initial block volume section of the Create Cluster page, select Add tag .
- To add a defined tag to block volume resources:
- Namespace: Select the tag namespace to which the tag belongs.
- Key: Select the name of the defined tag to apply to block volume resources.
- Value: Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- To add a free-form tag to block volume resources:
- Namespace: Set to None (free-form tags do not belong to a tag namespace).
- Key: Enter a name for the free-form tag to apply to block volume resources.
- Value: Enter a value for the tag to apply to block volume resources.

To update initial block volume tags to apply to new block volume resources created for a cluster::
- Follow the instructions in[Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)to update an existing cluster.
- Select the Tags tab of the cluster details page.
- In the Initial load balancer tags section:
- Display the Initial block volume tags section:
- Select Add to apply additional defined tags and free-form tags to new block volume resources.
- Select Edit from the the Actions menu (three dots) to change the value of defined tags and free-form tags applied to new block volume resources.
- Select Delete from the the Actions menu (three dots) to remove defined tags and free-form tags previously applied to new block volume resources.

Note that tags are only applied to block volume resources when the block volume resources are first created. So if you update initial block volume tags, the changes only apply to new block volume resources. Tags already applied to existing block volume resources are unaffected.

## Using the CLI to Specify Initial Block Volume Tags

```

```

For example:

```

```

## Using the API to Specify Initial Block Volume Tags

Use the`freeformTags`and`definedTags`attributes of the`PersistentVolumeConfigDetails`object used by the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)and[Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)operations to add and update initial block volume tags.

## Overriding Initial Block Volume Tags

You can override initial block volume tags applied to a block volume resource using parameters in a storage class manifest file as follows:
- 

To override defined initial block volume tags, include the following parameter in the parameters section of the StorageClass definition:

```

```

- 

To override free-form initial block volume tags, include the following parameter in the parameters section of the StorageClass definition:

```

```

For example:

```

```

Note the following:
- If you specify the above parameters, none of the initial block volume tags set for the cluster are applied to the block volume resource. Only the tags specified by the parameters, along with tag defaults, are applied to the block volume resource.
- Having applied a manifest file containing a StorageClass definition to create the storage class, you cannot subsequently change the tag parameter values by updating the definition and reapplying the manifest file. Once a storage class has been created, it is immutable. To specify different tag parameter values to the ones you previously specified, you have to create a new StorageClass definition that includes the new values for the tag parameters. Then specify the new storage class in the PVC definition.

## Which Tags Are Applied to Block Volumes?

[
