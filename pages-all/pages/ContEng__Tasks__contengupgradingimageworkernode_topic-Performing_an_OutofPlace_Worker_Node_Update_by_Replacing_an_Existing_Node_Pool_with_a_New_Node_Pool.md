# Performing an Out-of-Place Worker Node Update by Replacing an Existing Node Pool with a New Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-Performing_an_OutofPlace_Worker_Node_Update_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm
- Fetched: 2026-09-05 01:56 CDT

# Performing an Out-of-Place Worker Node Update by Replacing an Existing Node Pool with a New Node Pool

Find out how to update the properties of worker nodes in a node pool by replacing the original node pool with a new node pool that has new worker nodes with the required properties, using Kubernetes Engine (OKE).

You can update the properties of worker nodes in a node pool by replacing the original node pool with a new node pool that has new worker nodes with the required properties.

Having created the new node pool and specified the worker node properties you require, you drain existing worker nodes in the original node pool to prevent new pods starting and to delete existing pods. You can then delete the original node pool. When new worker nodes are started in the new node pool, they have the properties you specified.

## Using the Console

To perform an 'out-of-place' update of a node pool in a cluster, by creating a new node pool:
- On the Clusters list page, select the name of the cluster where you want to update worker node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select Add node pool to create a new node pool and specify the required worker node properties.

Note that if you specify a different Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See[Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutupgradingclusters.htm).
- If there are labels attached to worker nodes in the original node pool and those labels are used by selectors (for example, to determine the nodes on which to run pods), then use the`kubectl label nodes`command to attach the same labels to the new worker nodes in the new node pool. See[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#step-one-attach-label-to-the-node)in the Kubernetes documentation.
- 

For the first worker node in the original node pool, prevent new pods from starting and delete existing pods by entering:

```

```

For more information:
- about using kubectl, see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm)
- about the drain command, see[drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain)in the Kubernetes documentation

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there are enough replica pods running throughout the drain operation.
- 

Repeat the previous step for each remaining worker node in the node pool, until all the worker nodes have been drained from the original node pool.

When you have drained all the worker nodes from the original node pool and pods are running on worker nodes in the new node pool, you can delete the original node pool.
- 

Select the Node pools tab, and then select Delete node pool from the Actions menu (three dots) beside the original node pool.

The original node pool and all its worker nodes are deleted.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'out-of-place' worker node update

First create a new node pool with the worker node properties you require:
```

```

Then, for each worker node in the original node pool, prevent new pods from starting and delete existing pods by draining each worker node in turn:
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
