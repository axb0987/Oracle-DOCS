# Applying Tags to Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-tags.htm
- Fetched: 2026-09-05 01:56 CDT

# Applying Tags to Nodes

Find out how to apply tags to worker nodes in node pools you create using Kubernetes Engine (OKE).

When you define a node pool, you can optionally apply tags to the worker nodes in the node pool. These tags are referred to as node tags . You can specify both defined tags and free-form tags as node tags.

When you define a managed node pool, any node tags you apply are applied to the compute instances hosting the managed nodes.

Tag defaults with default values that are specified for the corresponding node pool's compartment are automatically applied to worker nodes. Tag defaults with user-applied values are only applied if the node pool is in a different compartment to the cluster. If that is the case, then you must specify a value for tag defaults with user-applied values by specifying node tags, as described in this section.

Note the following:
- If you use the 'Quick Create' workflow to create a new cluster, the free-form tags`"OKEclusterName": <cluster-name>`and`"OKEnodePoolName": <node-pool-name>`are also automatically added to worker nodes in the new cluster. The tags are not added to worker nodes if you use the 'Custom Create' workflow to create the cluster. Note that the tag values do not change if you subsequently change the name of the cluster or node pool.
- If you specify node tags when defining a node pool and the node pool is subsequently scaled out, the node tags are automatically applied to any new worker nodes that are created.
- Tags are only applied to worker nodes when the worker nodes are first created. If you update the tags to be applied to worker nodes, the changes only apply to new worker nodes. Tags applied to existing worker nodes are unaffected.
- To apply defined tags from a tag namespace belonging to one compartment to worker nodes in a node pool belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).
- If you apply a cost-tracking defined tag to worker nodes, you can include worker node compute instance usage in budgets (see[Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm)).

## Using the Console to Specify Managed Node Tags

To add a node tag to managed nodes in a new managed node pool when creating a new cluster:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- In the Node tags section of the Node pools page, select Add tag .
- To add a defined node tag to worker nodes in the new node pool:
- Namespace: Select the tag namespace to which the tag belongs.
- Key: Select the name of the defined tag to apply to worker nodes.
- Value: Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- To add a free-form node tag to worker nodes in the new node pool:
- Namespace: Set to None (free-form tags do not belong to a tag namespace).
- Key: Enter a name for the free-form tag to apply to worker nodes.
- Value: Enter a value for the tag to apply to worker nodes.

To update node tags applied to new managed nodes created in an existing managed node pool:
- Follow the instructions in[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm)to update an existing node pool.
- Select the Tags tab of the node pool details page.
- In the Node tags section:
- Select Add to apply additional defined tags and free-form tags to new nodes.
- Select Edit from the the Actions menu (three dots) to change the value of defined tags and free-form tags applied to new nodes.
- Select Delete from the the Actions menu (three dots) to prevent defined tags and free-form tags being applied to new nodes.

Note that tags are only applied to worker nodes when the worker nodes are first created. So if you update the tags applied to worker nodes, the changes only apply to new worker nodes. Tags already applied to existing worker nodes are unaffected.

## Using the CLI to Specify Managed Node Tags

```

```

For example:

```

```

## Using the CLI to Specify Virtual Node Tags
```

```

For example:
```

```

## Using the API

To add and update managed node tags, use the`freeformTags`and`definedTags`attributes of the`CreateNodePoolNodeConfigDetails`and`UpdateNodePoolNodeConfigDetails`objects used by the[CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)and[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)operations.

To add and update virtual node tags, use the`freeformTags`and`definedTags`attributes of the`CreateVirtualNodePoolDetails.virtualNodeTags`and`UpdateVirtualNodePoolDetails.virtualNodeTags`
