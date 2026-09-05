# Using Compute Host Groups to Provision Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghostgroups.htm
- Fetched: 2026-09-05 01:57 CDT

# Using Compute Host Groups to Provision Managed Nodes

Find out how to use compute host groups to control where Kubernetes Engine creates managed worker node instances, including using compute host groups configured for quick recycle.

A compute host group is a Compute service resource that groups hosts in a compartment and availability domain. In Kubernetes Engine, you can select a compute host group as the capacity type for a managed node pool placement configuration. When Kubernetes Engine creates worker node instances for that placement configuration, the Compute service places the instances on hosts in the selected compute host group.

Use compute host groups to control where Kubernetes Engine creates worker node instances for a managed node pool. This is useful for node pools that use bare metal shapes and require dedicated host placement or quick recycle behavior.

Quick recycle is a compute host group capability that can make a host available for reuse more quickly after the worker node instance on the host is terminated. Quick recycle is available only with supported shapes. For Kubernetes Engine, this means that when a worker node instance is terminated, the host can become available sooner for a replacement worker node instance, depending on the compute host group configuration.

Kubernetes Engine does not create compute host groups, attach hosts to compute host groups, or configure host group recycle levels. Create and configure the compute host group in the Compute service API or CLI before selecting it in Kubernetes Engine. For more information about creating and configuring compute host groups, see[ComputeHostGroup API Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeHostGroup/)and[compute-host-group CLI reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-host-group.html)in the Compute service documentation.

Changing the compute host group for a placement configuration affects new worker node instances. Existing worker node instances are not moved automatically. To use the updated compute host group for existing nodes, terminate and replace the existing worker node instances so that the Compute service places the replacement instances on hosts in the updated compute host group. For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm).

Before you use a compute host group with a managed node pool, note the following:
- Create and configure the compute host group in the Compute service.
- Make sure the compute host group lifecycle state is`ACTIVE`.
- Make sure the compute host group is in the same availability domain as the node pool placement configuration.
- Make sure the node pool shape matches the compute host group shape.
- For quick recycle, use a shape that supports quick recycle and configure the compute host group recycle level in the Compute service before selecting the compute host group in Kubernetes Engine.
- Add the required IAM policy so Kubernetes Engine can use the compute host group when launching worker node instances.

## Required IAM policy

To enable a node pool to use a compute host group, a policy must exist that allows the node pool resource principal to use the compute host group. For example:
```

```

where:
- `<compartment_name>`is the name of the compartment that contains the compute host group.
- `<host_group_OCID>`is the OCID of the compute host group.

## Using the Console

You can specify a compute host group when you create a cluster with a managed node pool, create a managed node pool, or update an existing managed node pool.

### Creating a cluster and specifying a compute host group for a managed node pool
- Follow the instructions to create a cluster using the 'Custom Create' workflow. See[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).
- When specifying the Node placement configuration for a managed node pool in the cluster:
- Specify the first availability domain and subnet:
- Availability domain: Select the availability domain in which to create worker nodes. When you select a compute host group, the compute host group must be in the same availability domain.
- Worker node subnet compartment: Select the compartment in which the worker node subnet resides.
- Worker node subnet: Select a regional subnet (recommended) or AD-specific subnet configured to host worker nodes, from the list of subnets in the specified compartment.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.
- 

Select Advanced options and specify the compute host group to use:
- Capacity type: Select Host group .
- Compartment: Select the compartment that contains the compute host group.
- 

Host group: Select the compute host group to use from the list. The compute host group must be in the same availability domain as the placement configuration.
- Optionally select Add row to add additional availability domains, subnets, and compute host groups to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different compute host group for each availability domain.
- Create the cluster.

Kubernetes Engine creates the cluster and managed node pool. For each placement configuration that specifies a compute host group, the Compute service places worker node instances on hosts in the selected compute host group.

### Creating a managed node pool and specifying a compute host group
- On the Clusters list page, select the name of the cluster where you want to create a new node pool. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Node pools tab of the cluster details page, select Add node pool to create a new managed node pool and specify the required properties for its worker nodes.
- When specifying the Node placement configuration for a managed node pool in the cluster:
- Specify the first availability domain and subnet:
- Availability domain: Select the availability domain in which to create worker nodes. When you select a compute host group, the compute host group must be in the same availability domain.
- Worker node subnet compartment: Select the compartment in which the worker node subnet resides.
- Worker node subnet: Select a regional subnet (recommended) or AD-specific subnet configured to host worker nodes, from the list of subnets in the specified compartment.
- Fault domains: (Optional) One or more fault domains in the availability domain in which to place worker nodes.
- 

Select Advanced options and specify the compute host group to use:
- Capacity type: Select Host group .
- Compartment: Select the compartment that contains the compute host group.
- 

Host group: Select the compute host group to use from the list. The compute host group must be in the same availability domain as the placement configuration.
- Optionally select Add row to add additional availability domains, subnets, and compute host groups to the placement configuration. If you specify multiple availability domains in a node pool's placement configuration, you can specify a different compute host group for each availability domain.
- Create the node pool.

Kubernetes Engine creates the managed node pool. For each placement configuration that specifies a compute host group, the Compute service places worker node instances on hosts in the selected compute host group.

### Updating the compute host group for a managed node pool
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Node pools tab of the cluster details page, select the name of the managed node pool you want to modify.
- Select Edit from the Actions menu.
- In Node placement configuration , select Advanced options and update the capacity type or selected compute host group as required.
- Save the changes.

The updated compute host group is used for new worker node instances. Existing worker node instances are not moved automatically.

To use the updated compute host group for existing nodes, terminate and replace the existing worker node instances so that the Compute service places the replacement instances on hosts in the updated compute host group. For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm).

## Using the CLI

### Creating a managed node pool that uses a compute host group

To use the CLI to create a managed node pool that uses a compute host group to provision managed nodes, include the`hostGroupId`key/value pair in the`placementConfigs`array in the`--node-config-details`parameter in the format:
```

```

The compute host group must be in the same availability domain as the placement configuration, and the node pool shape must match the compute host group shape.

### Updating the compute host group for a managed node pool

To use the CLI to update a managed node pool that uses a compute host group to provision managed nodes, include the`hostGroupId`key/value pair in the`placementConfigs`array in the`--node-config-details`parameter in the format:
```

```

Updating`hostGroupId`affects new worker node instances. Existing worker node instances are not moved automatically. To use the updated compute host group for existing nodes, terminate and replace the existing worker node instances so that the Compute service places the replacement instances on hosts in the updated compute host group. For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm).

## Using the API

When creating or updating a managed node pool, specify`hostGroupId`in each placement configuration that uses a compute host group.

For create node pool requests, specify:
```

```

For update node pool requests, specify:
```

```

## Troubleshooting

Use the following information to troubleshoot issues with compute host groups in managed node pools.

### The compute host group is not available in the list

Check the following:
- You selected the correct compartment.
- The compute host group is in the same availability domain as the placement configuration.
- The compute host group is active.
- You have permission to view or use the compute host group.

### Node pool creation or update fails

Check the following:
- The node pool shape matches the compute host group shape.
- The required IAM policy exists.
- The selected compute host group is not deleted or inactive.
- The selected compute host group is in the same availability domain as the placement configuration.

### Existing nodes did not move to the updated compute host group

Changing the compute host group affects new worker node instances. Existing worker node instances are not moved automatically.

To use the updated compute host group for existing nodes, terminate and replace the existing worker node instances so that the Compute service places the replacement instances on hosts in the updated compute host group. For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm)
