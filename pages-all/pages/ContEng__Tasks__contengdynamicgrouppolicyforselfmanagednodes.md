# Creating a Dynamic Group and a Policy for Self-Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm
- Fetched: 2026-09-05 01:55 CDT

# Creating a Dynamic Group and a Policy for Self-Managed Nodes

Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine.

Before you can create self-managed nodes, you have to:
- create a new dynamic group to contain the compute instance that you want to add to the cluster as a self-managed node
- create a policy for the dynamic group, with a policy statement to allow compute instances in the dynamic group to join an existing Kubernetes cluster

To create a new dynamic group and a suitable policy using the Console:
- 

Create a new dynamic group to contain the compute instance that you want to add to the cluster as a self-managed node:
- Follow the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To)in the IAM documentation, and give the new dynamic group a name (for example,`acme-oke-self-managed-node-dyn-grp`).
- 

Enter a rule that includes the compute instances in the compartment, in the format:

```

```

where`<compartment-ocid>`is the OCID of the compartment to which the cluster belongs.

For example:

```

```

- Select Create .
- Create a policy for the dynamic group, with a policy statement to allow compute instances in the dynamic group to join an existing Kubernetes cluster:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-self-managed-node-policy`).
- 

Enter a policy statement to allow compute instances in the dynamic group to join the cluster, in the format:

```

```

where:
- `<dynamic-group-name>`is the name of the dynamic group you created earlier. For example,`acme-oke-self-managed-node-dyn-grp`. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format`dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format`dynamic-group id <dynamic-group-ocid>`.
- `<compartment-name>`is the name of the compartment to which the cluster belongs. For example,`acme-oke-cluster-compartment`

For example:

```

```

If you consider this policy statement to be too permissive, you can restrict the permissions to explicitly specify the cluster to which you want to add the managed node, by entering a policy statement in the format:

```

```

-
