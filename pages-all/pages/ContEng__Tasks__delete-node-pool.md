# Deleting a Managed Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-node-pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Deleting a Managed Node Pool

Find out how to delete a managed node pool using Kubernetes Engine (OKE).

You can delete a managed node pool from a cluster when you want to scale down the cluster. See[Removing Node Pools to Scale Down Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengremovingnodepools_topic.htm).

Note that deleting a node pool permanently deletes the node pool. You can't recover a deleted node pool.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-node-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-node-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-node-pool.htm#)
- 

- On the Clusters list page, select the name of the cluster that you want to modify. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/list-clusters.htm).
- Select the Node pools tab.
- 

Scale down the cluster by removing node pools as follows:
- 

Select Delete node pool from the Actions menu (three dots) beside the node pool that you want to remove.

Note that deleting a node pool permanently deletes the node pool. You can't recover a deleted node pool.
- Enter the name of the node pool to confirm that you want to delete it.
- 

Either accept the default values, or specify when and how to cordon and drain worker nodes before terminating them:
- Eviction grace period (mins): The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.

Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.

De-select this option if you don't want worker nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that can't be terminated within the eviction grace period have the Needs attention status. The status of the work request that initiated the termination operation is set to Failed , and the termination operation is cancelled. For more information, see[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengmonitoringclusters.htm).

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Delete to delete the node pool.
- 

Use the[oci ce node-pool delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete.html)command and required parameters to delete a managed node pool:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNodePool)
