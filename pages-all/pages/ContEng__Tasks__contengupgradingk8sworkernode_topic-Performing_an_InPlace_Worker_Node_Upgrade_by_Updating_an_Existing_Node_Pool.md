# Performing an In-Place Managed Node Kubernetes Upgrade by Manually Deleting and Replacing Nodes in an Existing Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_InPlace_Worker_Node_Upgrade_by_Updating_an_Existing_Node_Pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Performing an In-Place Managed Node Kubernetes Upgrade by Manually Deleting and Replacing Nodes in an Existing Node Pool

Find out how to upgrade the Kubernetes version on managed nodes in a node pool by changing properties of the existing node pool, and then manually deleting and replacing each managed node in turn, using Kubernetes Engine (OKE).
Note  
  
This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

You can upgrade the version of Kubernetes running on managed nodes in a node pool by specifying a more recent Kubernetes version for the existing node pool.

You delete each managed node in turn, selecting appropriate cordon and drain options to prevent new pods starting and to delete existing pods. You start a new managed node to take the place of each managed node you delete. When new managed nodes start in the existing node pool, they run the more recent Kubernetes version you specified.

## Using the Console

To perform an 'in-place' upgrade of a node pool in a cluster, by specifying a more recent Kubernetes version for the existing node pool:
- On the Clusters list page, select the name of the cluster where you want to change the Kubernetes version running on managed nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select the name of the node pool where you want to upgrade the Kubernetes version running on the managed nodes.
- 

On the node pool details page, select Edit from the Actions menu.
- 

In the Version field of the Edit node pool dialog, specify the required Kubernetes version for managed nodes. We recommend that you select a version number that has the format`x.y`(see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm)).

The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Select Update to save the change.

You now have to delete existing managed nodes so that new managed nodes are started, running the Kubernetes version you specified.

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there are enough replica pods running throughout the deletion operation. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.
- 

For the first managed node in the node pool:
- On the node pool details page, select the Nodes tab, and then select Delete node from the Actions menu (three dots) beside the node you want to delete.
- 

Specify when and how to cordon and drain managed nodes before terminating them:
- Eviction grace period (mins): The length of time to allow to cordon and drain managed nodes before terminating them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon managed nodes and drain them of their workloads. To terminate managed nodes immediately, without cordoning and draining them, specify 0 minutes.
- Force terminate after grace period: Whether to terminate managed nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.

Select this option if you always want managed nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.

De-select this option if you don't want managed nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing managed nodes that can't be terminated within the eviction grace period have the Needs attention status. The status of the work request that initiated the termination operation is set to Failed , and the termination operation is cancelled. For more information, see[Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm).
- Decrease node pool size: Do not select this option, so that a new worker node is started (rather than the node pool being scaled down).

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Delete to delete the managed node.

The managed node is deleted and a new managed node is started, running the Kubernetes version you specified.
- Repeat the previous step for each remaining managed node in the node pool, until all managed nodes in the node pool are running the Kubernetes version you specified.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'in-place' managed node Kubernetes upgrade by manually terminating and replacing nodes

First, update the node pool's worker node Kubernetes version property, and specify the OCID of the corresponding image:

```

```

Then, delete each managed node in the node pool in turn, specifying that you want to start a new managed node to replace the managed node you have deleted

```

```
