# Applying Tags to Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm
- Fetched: 2026-09-05 01:56 CDT

# Applying Tags to Load Balancers

Find out how to apply tags to load balancer resources, and how to override initial load balancer tags, when using Kubernetes Engine (OKE).
Note  
  
References to load balancer in this section apply to both OCI load balancer resources and OCI network load balancer resources, unless explicitly stated otherwise.

When you create a cluster, you can optionally define tags to apply to load balancer resources created when Kubernetes services of type LoadBalancer are defined. These tags are referred to as initial load balancer tags. You can specify both defined tags and free-form tags as initial load balancer tags.

You can override initial load balancer tags using annotations on the Kubernetes service (see[Overriding Initial Load Balancer Tags](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm#contengtaggingclusterresources_tagging_oke_resources_load_balancer_tags__load-balancer-tag-override-annotations)). If you specify the annotations when defining the Kubernetes service, none of the initial load balancer tags specified in the cluster definition are applied to the load balancer resource. Instead, the tags specified by the annotations are applied to the load balancer resource.

Tag defaults with default values that are specified for the compartment are automatically applied to the load balancer resource as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.

Note the following:
- Tags are only applied to load balancers when the load balancers are first created. If you update the initial load balancer tags, the changes only apply to new load balancers (assuming the tags are not overridden by annotations on the Kubernetes service). Tags applied to existing load balancers are unaffected.
- If you apply a cost-tracking defined tag to a load balancer resource, you can include load balancer usage in budgets (see[Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm)).
- To apply defined tags from a tag namespace belonging to one compartment to a load balancer resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See[Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm).

## Using the Console to Specify Initial Load Balancer Tags

To specify an initial load balancer tag to apply to load balancer resources created for a new cluster:
- Follow the instructions in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm)to create a new cluster.
- In the Tagging - Initial load balancer section of the Create Cluster page, select Add tag .
- To add a defined tag to load balancer resources:
- Namespace: Select the tag namespace to which the tag belongs.
- Key: Select the name of the defined tag to apply to load balancer resources.
- Value: Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
- To add a free-form tag to load balancer resources:
- Namespace: Set to None (free-form tags do not belong to a tag namespace).
- Key: Enter a name for the free-form tag to apply to load balancer resources.
- Value: Enter a value for the tag to apply to load balancer resources.

To update initial load balancer tags to apply to new load balancer resources created for a cluster:
- Follow the instructions in[Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm)to update an existing cluster.
- Select the Tags tab of the cluster details page.
- In the Initial load balancer tags section:
- Select Add to apply additional defined tags and free-form tags to new load balancer resources.
- Select Edit from the the Actions menu (three dots) to change the value of defined tags and free-form tags applied to new load balancer resources.
- Select Delete from the the Actions menu (three dots) to remove defined tags and free-form tags previously applied to new load balancer resources.

Note that tags are only applied to load balancers when the load balancers are first created. So if you update initial load balancer tags, the changes only apply to new load balancer resources. Tags already applied to existing load balancer resources are unaffected.

## Using the CLI to Specify Initial Load Balancer Tags

```

```

For example:

```

```

## Using the API to Specify Initial Load Balancer Tags

Use the`freeformTags`and`definedTags`attributes of the`ServiceLbConfigDetails`object used by the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)and[Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)operations to add and update initial load balancer tags.

## Overriding Initial Load Balancer Tags

You can override initial load balancer tags specified for a cluster using annotations in the definition of a Kubernetes service of type LoadBalancer, as follows:
- For load balancer resources:
- 

To override defined initial load balancer tags for load balancer resources, add the following annotation in the metadata section of the manifest file:

```

```

- 

To override free-form initial load balancer tags for load balancer resources, add the following annotation in the metadata section of the manifest file:

```

```

- For network load balancer resources:
- 

To override defined initial load balancer tags for network load balancer resources, add the following annotation in the metadata section of the manifest file:

```

```

- 

To override free-form initial load balancer tags for network load balancer resources, add the following annotation in the metadata section of the manifest file:

```

```

For example:

```

```

Note the following:
- If you specify the above annotations, none of the initial load balancer tags set for the cluster are applied to the load balancer resource. Only the tags specified by the annotations, along with tag defaults, are applied to the load balancer resource.
- If you change the annotations in the manifest file, the changes only apply to new load balancer resources. Tags already applied to existing load balancer resources are unaffected. You cannot change the tags applied to an existing load balancer resource by changing the annotations. Instead, you have to create a new Kubernetes service of type LoadBalancer with the annotations for the tags you require.

## Which Tags Are Applied to Load Balancers?

[
