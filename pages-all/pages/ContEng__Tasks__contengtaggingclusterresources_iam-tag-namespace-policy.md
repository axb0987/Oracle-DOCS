# Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm
- Fetched: 2026-09-05 01:56 CDT

# Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments

Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine (OKE).

To apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, you must include a policy statement similar to the following in an IAM policy:

```

```

If you consider this policy statement to be too permissive, you can restrict the permissions to explicitly specify the compartment to which the tag namespace belongs, and/or to explicitly specify the cluster that belongs to a different compartment. For example:

```

```
