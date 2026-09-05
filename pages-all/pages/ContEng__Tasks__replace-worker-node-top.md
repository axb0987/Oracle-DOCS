# Terminating and Replacing Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm
- Fetched: 2026-09-05 01:58 CDT

# Terminating and Replacing Worker Nodes

Find out how to terminate and replace a worker node in a Kubernetes cluster that you've created using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to terminate and replace worker nodes when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes to terminate and replace nodes with both virtual machine shapes and bare metal shapes.

You can cycle nodes to terminate and replace managed nodes.

Sometimes, terminating and replacing managed nodes is the best way to resolve an issue with the compute instances hosting the nodes. In particular, where an issue can be resolved simply by terminating an existing instance and replacing it with a new instance that has the same properties, or that has different properties derived from changed node pool properties (such as a changed host OS, or a changed compute shape). For example:
- To address any configuration drift that might have occurred since the instance was originally launched.
- To address any underlying hardware faults.

Using Kubernetes Engine, you can terminate and replace the compute instances hosting managed nodes in the following ways:
- You can cycle the node pool containing the managed nodes, and select the Replace nodes option, as described in this section.
- You can cycle and replace specific managed nodes, as described in this section.
- You can delete a specific managed node. Provided that you do not indicate that you want node deletion to scale down the node pool, the node that you delete is replaced with a new node (see[Deleting Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm)).

When you cycle and terminate and replace a managed node, Kubernetes Engine automatically cordons and drains the worker node before terminating it. The compute instance hosting the managed node is terminated and a new instance is created. Note that the new instance has a new OCID and network address.

If you cycle all the managed nodes in a node pool to terminate and replace them, when new instances have a Running state, any updates to node pool properties are applied to all of the worker nodes in the node pool. Note that if you cycle an individual managed node to terminate and replace it, any updates to node pool properties are applied to the replacement node. An exception applies to the Kubernetes version. Cycling an individual managed node to terminate and replace it does not change the Kubernetes version running on the node.

As well as enabling you to perform routine worker node maintenance, terminating and replacing managed nodes can also be useful when you want to:
- Update managed node properties (see[Updating Worker Nodes in an Existing Node Pool by Terminating and Replacing Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Nodes.htm)).
- Upgrade the Kubernetes version running on managed nodes (see[Upgrading Managed Nodes by Terminating and Replacing Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Upgrade_By_Cycling_and_Replacing_Nodes.htm)).
- Roll back the Kubernetes version running on managed nodes to an earlier available version (see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm)).

Note the following considerations when cycling to terminate and replace worker nodes:
- You can select a managed node pool to cycle, terminate, and replace all the managed nodes within it. You can also cycle, terminate, and replace individual managed nodes.
- You cannot cycle self-managed nodes to terminate and replace them.

## Balancing service availability and cost when terminating and replacing managed nodes in node pools

When you cycle all the managed nodes in a node pool to terminate and replace them, Kubernetes Engine uses the Cordon and drain settings specified for the node pool, and follows two strategies:
- Create new (additional) nodes, and then remove existing nodes: Kubernetes Engine adds an additional node (or nodes) to the node pool with updated properties. When the additional node is active, Kubernetes Engine cordons an existing node, drains the node, and removes the node from the node pool. This strategy maintains service availability, but costs more.
- Remove existing nodes, and then create new nodes: Kubernetes Engine cordons an existing node (or nodes) to make it unavailable, drains the node, and removes the node from the node pool. When the node has been removed, Kubernetes Engine adds a new node to the node pool to replace the node that has been removed. This strategy costs less, but might compromise service availability.

To tailor Kubernetes Engine behavior to meet your own requirements for service availability and cost, control and balance the two strategies by specifying values for maxSurge and maxUnavailable . For more information, see[Balancing Service Availability and Cost When Cycling Managed Nodes in Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/balance-service-availability-cost.htm).

## Cordoning and draining when terminating and replacing nodes

When you select a node pool and specify that you want to terminate and replace its worker nodes, Kubernetes Engine automatically cordons, drains, and terminates the existing managed nodes. Kubernetes Engine uses the Cordon and drain options specified for the node pool.

When you select an individual managed node and specify that you want to terminate and replace it, you can specify Cordon and drain options. The Cordon and drain options you specify for the managed node override the Cordon and drain options specified for the node pool.

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm)

## Terminating and Replacing Worker Nodes

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm#)
- 

To terminate and replace all the worker nodes in a managed node pool:
- On the Clusters list page, select the name of the cluster that contains the worker nodes that you want to terminate and replace. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node Pools tab, and then select the name of the node pool that contains the worker nodes that you want to terminate and replace.
- Select Edit from the Actions menu, and change an unused property of the node pool (for example, by specifying a Kubernetes label with a key of`foo`, and a value of`bar`).

Note that the property you change is irrelevant, but you must change at least one property.
- 

From the Actions menu, select Cycle nodes .

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the operation. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.
- 

In the Cycle nodes dialog:
- Select Replace nodes from the Cycling options list.
- Control the number of nodes to update in parallel, and balance service availability and cost, by specifying:
- Maximum surge (Maximum number or percentage of additional nodes): The maximum number of additional nodes to temporarily allow in the node pool during the operation (expressed either as an integer or as a percentage). Additional nodes are nodes over and above the number specified in the node pool's Node count property. If you specify an integer for the number of additional nodes, do not specify a number greater than the value of Node count .
- Maximum unavailable (Maximum number or percentage of unavailable nodes): The maximum number of nodes to allow to be unavailable in the node pool during the operation (expressed either as an integer or as a percentage). If you specify an integer for the number of unavailable nodes, do not specify a number greater than the value of Node count .

See[Balancing service availability and cost when terminating and replacing managed nodes in node pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/replace-worker-node-top.htm#replace_worker_node_top__section_balancing-service-availability-and-cost-when-cycling-replacing-nodes).
- Select Cycle nodes to start the operation.

Kubernetes Engine uses the Cordon and drain options specified for the node pool to cordon and drain the worker nodes. For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).

To terminate and replace a specific managed node:
- On the Clusters list page, select the name of the cluster that contains the worker node that you want to reboot. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node Pools tab, and then select the name of the node pool that contains the worker node that you want to terminate and replace.
- 

On the Nodes tab, select Cycle node from the Actions menu (three dots) beside the node that you want to terminate and replace.
- In the Cycle node dialog:
- Select Replace node from the Cycling options list.
- 

Specify when and how to cordon and drain the worker node before performing the terminate and replace action, by specifying:

- Eviction grace period (mins): The length of time to allow to cordon and drain the worker node before performing the action. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon a worker node and drain it of its workloads. To perform the action immediately, without cordoning and draining the worker node, specify 0 minutes.
- Force terminate after grace period: Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected.

See[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Cycle node to start the operation.
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).
- 

To terminate and replace all the worker nodes in a managed node pool

To terminate and replace all the worker nodes in a managed node pool, use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command and required parameters:

```

```

where`--<property-to-update> <new-value>`is a new value for a node pool property. Note that the property you change is irrelevant, but you must change at least one property. Also note that including`\"cycleModes\":[\"INSTANCE_REPLACE\"]`in the`--node-pool-cycling-details`parameter is optional, since it is assumed if not explicitly included.

For example:

```

```

To terminate and replace a specific managed node

To terminate and replace a specific managed node, use the[oci ce node-pool delete-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete-node.html)command and required parameters to delete a node, and include`--is-decrement-size false`to specify that you do not want to scale down the node pool:
```

```

- 

To terminate and replace all the worker nodes in a managed node pool using the OCI API:

Run the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)operation to terminate and replace all the worker nodes in a managed node pool.

To terminate and replace a specific managed node using the OCI API:

Run the[DeleteNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNode)
