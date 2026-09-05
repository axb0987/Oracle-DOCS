# Applying Tags to Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-pool-tags.htm
- Fetched: 2026-09-05 01:56 CDT

# Applying Tags to Node Pools

Find out how to apply tags to node pools you create using Kubernetes Engine (OKE).

When you create a managed node pool or a virtual node pool, you can optionally apply tags to the node pool resource. These tags are referred to as node pool tags . You can specify both defined tags and free-form tags as node pool tags.

Tag defaults with default values that are specified for the node pool's compartment are automatically applied to the node pool resource. Tag defaults with user-applied values are only applied to the node pool resource if the node pool is in a different compartment to the cluster. If that is the case, then you must specify a value for tag defaults with user-applied values by specifying node pool tags, as described in this section.

Note the following:
- If you use the 'Quick Create' workflow to create a new cluster, the free-form tags`"OKEclusterName": <cluster-name>`and`"OKEnodePoolName": <node-pool-name>`are also automatically added to node pools in the new cluster. The tags are not added to node pools if you use the 'Custom Create' workflow to create the cluster. Note that the values of these tags do not change if you subsequently change the name of the cluster or node pool.
- Node pool tags are not applied to worker nodes in the node pool. To apply tags to worker nodes, see[Applying Tags to Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-tags.htm).
- To apply defined tags from a tag namespace belonging to one compartment to a node pool belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).

## Using the Console to Specify Node Pool Tags

To add a node pool tag to a new node pool when creating a new cluster:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- In the Node pool tags section of the Node pools page, select Add tag .
- To add a defined tag to the node pool:
- Namespace: Select the tag namespace to which the tag belongs.
- Key: Select the name of the defined tag to apply to the node pool.
- Value: Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- To add a free-form tag to the node pool:
- Namespace: Set to None (free-form tags do not belong to a tag namespace).
- Key: Enter a name for the free-form tag to apply to the node pool.
- Value: Enter a value for the tag to apply to the node pool.

To update node pool tags applied to an existing node pool:
- Follow the instructions in[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm)to update an existing node pool.
- Select the Tags tab of the node pool details page.
- In the Node pool tags section:
- Select Add to apply additional defined tags and free-form tags to the node pool.
- Select Edit from the the Actions menu (three dots) to change the value of defined tags and free-form tags previously applied to the node pool.
- Select Delete from the the Actions menu (three dots) to remove defined tags and free-form tags previously applied to the node pool.

## Using the CLI to Specify Managed Node Pool Tags

```

```

For example:

```

```

## Using the CLI to Specify Virtual Node Pool Tags
```

```

For example:
```

```

## Using the API to Specify Node Pool Tags

To add and update managed node pool tags, use the`freeformTags`and`definedTags`attributes of the`CreateNodePoolDetails`and`UpdateNodePoolDetails`objects used by the[CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)and[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)operations.

To add and update virtual node pool tags, use the`freeformTags`and`definedTags`attributes of the`CreateVirtualNodePoolDetails`and`UpdateVirtualNodePoolDetails`
