# Scaling Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm
- Fetched: 2026-09-05 01:56 CDT

# Scaling Node Pools

Find out how to scale up and scale down the node pools you've created using Kubernetes Engine (OKE).

To optimize resource usage, you can scale a node pool up and down to change the number of worker nodes in the node pool, and the availability domains and subnets in which to place them.

For general information about modifying node pools and worker nodes, see[Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm). In particular, note the following:
- Any changes you make to worker node properties will only apply to new worker nodes. You cannot change the properties of existing worker nodes.
- If you change a node pool's placement configuration (the availability domains, fault domains, and subnets in which worker nodes are placed, but not the node pool's capacity type), existing worker nodes are terminated and new worker nodes are created in the new locations.
- Changing the capacity type associated with a node pool placement configuration applies to new worker node instances. Existing worker node instances are not moved automatically. To update the capacity type for existing nodes, terminate and replace the existing worker node instances. For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm).
- If a capacity reservation is specified for a node pool, note that the node shape, availability domain, and fault domain in the node pool's placement configuration must always match the capacity reservation's instance type, availability domain, and fault domain respectively. See[Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm).
- If a compute host group is specified for a node pool placement configuration, the compute host group must be in the same availability domain as the placement configuration. The node pool shape must also match the compute host group shape. See[Using Compute Host Groups to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghostgroups.htm).
- If a compute cluster is specified for a node pool, the node pool shape must support RDMA and compute clusters, and the placement configuration must include only the availability domain that contains the compute cluster. Fault domains cannot be specified for node pools that use compute clusters. See[Using Compute Clusters to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm).
- If a compute cluster is specified for a node pool, new worker node instances are launched in the same compute cluster. You cannot change the compute cluster when scaling a node pool. To use a different compute cluster, create a new node pool.
- Do not use the`kubectl delete node`command to scale down or terminate worker nodes in a cluster that was created by Kubernetes Engine. Instead, reduce the number of worker nodes by changing the corresponding node pool properties using the Console or the API. The`kubectl delete node`command does not change a node pool's properties, which determine the desired state (including the number of worker nodes). Also, although the`kubectl delete node`command removes the worker node from the cluster's etcd key-value store, the command does not delete the underlying instance or virtual node.
- When scaling down a node pool, note that the node pool's Cordon and drain properties determine when and how worker nodes are terminated. See[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).

## Using the Console

To scale up or scale down an existing node pool by increasing or decreasing the number of worker nodes:
- On the Clusters list page, select the name of the cluster you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool you want to scale.
- 

On the details page, select Edit from the Actions menu and specify:
- the number of worker nodes you want in the node pool after the scale operation is complete
- the network security groups with security rules to control traffic into and out of the node pool
- the availability domains and fault domains in which to place the worker nodes
- the regional subnets (recommended) or AD-specific subnets to host the worker nodes
- a capacity type to use
- Save the changes.

If you subsequently decide to scale down a node pool that you have scaled up, always use the Console, or the API. Do not use the`kubectl delete node`command (see[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm)).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)operation to scale up and scale down an existing node pool.

If you subsequently decide to scale down a node pool that you have scaled up, always use the Console, or the API. Do not use the`kubectl delete node`command (see[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm)
