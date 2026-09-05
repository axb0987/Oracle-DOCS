# Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_OutofPlace_Worker_Node_Upgrade_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm
- Fetched: 2026-09-05 01:57 CDT

# Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool

Find out how to upgrade the Kubernetes version on managed nodes in a node pool by replacing the original node pool with a new node pool that has managed nodes with a more recent Kubernetes version, using Kubernetes Engine (OKE).
Note  
  
This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

You can 'upgrade' the version of Kubernetes running on managed nodes in a node pool by replacing the original node pool with a new node pool that has new managed nodes running the appropriate Kubernetes version. Having drained existing managed nodes in the original node pool to prevent new pods starting and to delete existing pods, you can then delete the original node pool. When new managed nodes are started in the new node pool, they run the more recent Kubernetes version you specified.

## Using the Console

To perform an 'out-of-place' upgrade of a node pool in a cluster, by creating a new node pool to 'upgrade' the Kubernetes version on managed nodes:
- On the Clusters list page, select the name of the cluster where you want to change the Kubernetes version running on managed nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select Add node pool to create a new node pool and specify the required Kubernetes version for its managed nodes. We recommend that you select a version number that has the format`x.y`(see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm)).

The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- If there are labels attached to managed nodes in the original node pool and those labels are used by selectors (for example, to determine the nodes on which to run pods), then use the`kubectl label nodes`command to attach the same labels to the new managed nodes in the new node pool. See[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#step-one-attach-label-to-the-node)in the Kubernetes documentation.
- 

For the first managed node in the original node pool, prevent new pods from starting and delete existing pods by entering:

```

```

For more information:
- about using kubectl, see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm)
- about the drain command, see[drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain)in the Kubernetes documentation

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there are enough replica pods running throughout the drain operation.
- 

Repeat the previous step for each remaining managed node in the node pool, until all the managed nodes have been drained from the original node pool.

When you have drained all the managed nodes from the original node pool and pods are running on managed nodes in the new node pool, you can delete the original node pool.
- 

On the cluster details page, select the Node pools tab, and then select Delete node pool from the Actions menu (three dots) beside the original node pool.

The original node pool and all its managed nodes are deleted.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'out-of-place' managed node Kubernetes upgrade

First create a new node pool and specify the required Kubernetes version for its managed nodes:
```

```

Then, for each managed node in the original node pool, prevent new pods from starting and delete existing pods by draining each managed node in turn:
```

```

Finally, delete the original node pool:

```

```

For example:
```

```

```

```

```

```

```

```

```

```
