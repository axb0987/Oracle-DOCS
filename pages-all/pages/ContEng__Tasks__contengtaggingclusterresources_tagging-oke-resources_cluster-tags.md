# Applying Tags to Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_cluster-tags.htm
- Fetched: 2026-09-05 01:56 CDT

# Applying Tags to Clusters

Find out how to apply tags to Kubernetes clusters you create using Kubernetes Engine (OKE).

When you create a cluster, you can optionally apply tags to the cluster resource. These tags are referred to as cluster tags . You can specify both defined tags and free-form tags as cluster tags.

Tag defaults with default values that are specified for the compartment are automatically applied to the cluster resource as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.

Note the following:
- If you use the 'Quick Create' workflow to create a new cluster, the free-form tag`"OKEclusterName": <cluster-name>`is automatically added to the cluster. The tag is not added to a cluster if you use the 'Custom Create' workflow to create the cluster. Note that the value of this tag does not change if you subsequently change the name of the cluster.
- Tags applied to a cluster resource are not applied to either the cluster's private IP address resource or to the optional public IP address resource.
- To apply defined tags from a tag namespace belonging to one compartment to a cluster resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).

## Using the Console to Specify Cluster Tags

To add a cluster tag to a new cluster:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- In the Tagging - Cluster section of the Create Cluster page, select Add tag .
- To add a defined tag to the cluster:
- Namespace: Select the tag namespace to which the tag belongs.
- Key: Select the name of the defined tag to apply to the cluster.
- Value: Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- To add a free-form tag to the cluster:
- Namespace: Set to None (free-form tags do not belong to a tag namespace).
- Key: Enter a name for the free-form tag to apply to the cluster.
- Value: Enter a value for the tag to apply to the cluster.

To update cluster tags applied to an existing cluster:
- Follow the instructions in[Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)to update an existing cluster.
- Select the Tags tab of the cluster details page.
- In the Cluster tags section:
- Select Add to apply additional defined tags and free-form tags to the cluster.
- Select Edit from the the Actions menu (three dots) to change the value of defined tags and free-form tags previously applied to the cluster.
- Select Delete from the the Actions menu (three dots) to remove defined tags and free-form tags previously applied to the cluster.

## Using the CLI to Specify Cluster Tags

```

```

For example:

```

```

## Using the API to Specify Cluster Tags

Use the`freeformTags`and`definedTags`attributes of the`CreateClusterDetails`and`UpdateClusterDetails`objects used by the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)and[Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)
