# Deleting Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm
- Fetched: 2026-09-05 01:55 CDT

# Deleting Worker Nodes

Find out about deleting worker nodes with Kubernetes Engine (OKE).

You can delete specific worker nodes in node pools in clusters that you've created with Kubernetes Engine.

Note the following considerations:
- Deleting a worker node deletes that specific worker node from the node pool, and optionally scales down the node pool itself by subtracting 1 from the number of worker nodes specified for the node pool. If you delete a worker node without scaling down the node pool, a new worker node is created to replace it.
- When you delete managed nodes, the Cordon and drain options that you select determine when and how worker nodes are terminated. See[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- As well as being able to delete specific worker nodes, note that worker nodes are also deleted when you scale down node pools and change placement configurations.
- When you have marked a worker node for deletion (during a delete node operation, a scale down operation, or a change to placement configuration), you can't recover the node. Even if the delete node operation is initially unsuccessful, the next update node pool operation (including a scale up operation) attempts to terminate the node again.
- Kubernetes Engine creates the worker nodes in a cluster with automatically generated names. Managed node names have the following format:`oke-c<part-of-cluster-OCID>-n<part-of-node-pool-OCID>-s<part-of-subnet-OCID>-<slot>`. Virtual node names are the same as the node's private IP address. Do not change the automatically generated names of worker nodes. If you were to change the automatically generated name of a worker node and then delete the cluster, the renamed worker node would not be deleted. You would have to delete the renamed worker node manually.
- When deleting a worker node from a node pool, you set the Decrease node pool size property (`isDecrementSize`in the API) to indicate whether you want deletion of the worker node to scale down the node pool by 1. While the delete node operation is in progress, do not attempt to delete the same node and specify a different value for Decrease node pool size (`isDecrementSize`). If you want to delete the node and specify a different value for Decrease node pool size (`isDecrementSize`), wait until the first delete node operation is complete.

You can delete worker nodes using the Console, the CLI and the API. See[Deleting a Worker Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-worker-node.htm)
