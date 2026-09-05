# Performing an Out-of-Place Virtual Node Update by Replacing an Existing Virtual Node Pool with a New Virtual Node Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodesupdatedprops_topic-Performing_an_OutofPlace_Virtual_Node_Update_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm
- Fetched: 2026-09-05 01:55 CDT

# Performing an Out-of-Place Virtual Node Update by Replacing an Existing Virtual Node Pool with a New Virtual Node Pool

Find out how to update the properties of virtual nodes in a virtual node pool by replacing the original node pool with a new node pool that has new virtual nodes with the required properties, using Kubernetes Engine (OKE).

You can update the properties of virtual nodes in a virtual node pool by replacing the original node pool with a new node pool that has new virtual nodes with the required properties.

Having created the new virtual node pool and specified the virtual node properties you require, you delete the original node pool. Kubernetes Engine cordons and drains existing virtual nodes in the original virtual node pool to prevent new pods from starting, and to delete existing pods. When new virtual nodes are started in the new virtual node pool, they have the properties you specified.

## Using the Console

To perform an 'out-of-place' update of a virtual node pool in a cluster, by creating a new virtual node pool:
- On the Clusters list page, select the name of the cluster where you want to update virtual node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select Add node pool to create a new virtual node pool and specify the required virtual node properties.
- If there are labels attached to worker nodes in the original node pool and those labels are used by selectors (for example, to determine the nodes on which to run pods), then use the virtual node pool's Kubernetes labels property to attach the same labels to the new worker nodes in the new node pool. See[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#step-one-attach-label-to-the-node)in the Kubernetes documentation.
- 

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there are enough replica pods running throughout the drain operation.
- 

Select the Node pools tab, and then select Delete node pool from the Actions menu (three dots) beside the original virtual node pool.

Kubernetes Engine cordons and drains existing virtual nodes in the original virtual node pool to prevent new pods from starting, and to delete existing pods.

The original node pool and all its worker nodes are then deleted.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'out-of-place' virtual node update

First create a new virtual node pool with the virtual node properties you require:
```

```

Then, delete the original virtual node pool:

```

```
