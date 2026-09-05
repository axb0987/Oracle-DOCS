# Performing an In-Place Worker Node Update by Manually Deleting and Replacing Nodes in an Existing Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-Performing_an_InPlace_Worker_Node_Update_By_Updating_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:56 CDT

# Performing an In-Place Worker Node Update by Manually Deleting and Replacing Nodes in an Existing Node Pool

Find out how to update the properties of worker nodes in a node pool by changing properties of the existing node pool, using Kubernetes Engine (OKE).
Note  
  
This section applies to managed nodes only.

You can update the properties of worker nodes in a node pool by changing properties of the existing node pool.

You delete each worker node in turn, selecting appropriate cordon and drain options to prevent new pods starting and to delete existing pods. You start a new worker node to take the place of each worker node you delete. When new worker nodes start in the existing node pool, they have the properties you specified.

## Using the Console

To perform an 'in-place' update of a node pool in a cluster:
- On the Clusters list page, select the name of the cluster where you want to update worker node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select the name of the node pool where you want to update worker node properties.
- 

From the Actions menu, select Edit and specify the required properties for worker nodes.

Note that if you change the Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See[Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutupgradingclusters.htm).
- 

Select Update to save the change.

You now have to delete existing worker nodes so that new worker nodes are started, with the properties you specified.

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there are enough replica pods running throughout the deletion operation. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.
- 

For the first worker node in the node pool:
- Select the Nodes tab ,and then select Delete node from the Actions menu (three dots) beside the node you want to delete.
- 

Specify when and how to cordon and drain worker nodes before terminating them:
- Eviction grace period (mins): The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.

Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.

De-select this option if you don't want worker nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that can't be terminated within the eviction grace period have the Needs attention status. The status of the work request that initiated the termination operation is set to Failed , and the termination operation is cancelled. For more information, see[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- Decrease node pool size: Do not select this option, so that a new worker node is started (rather than the node pool being scaled down).

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Delete to delete the worker node.

The worker node is deleted and a new worker node is started that has the properties you specified.
-
