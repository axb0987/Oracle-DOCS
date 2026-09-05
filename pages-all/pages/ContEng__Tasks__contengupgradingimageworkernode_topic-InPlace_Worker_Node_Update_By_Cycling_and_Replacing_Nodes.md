# Updating Worker Nodes in an Existing Node Pool by Terminating and Replacing Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Nodes.htm
- Fetched: 2026-09-05 01:56 CDT

# Updating Worker Nodes in an Existing Node Pool by Terminating and Replacing Nodes

Find out how to update the properties of worker nodes in a node pool by changing properties of the existing node pool, and then terminating and replacing the nodes, using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to perform an in-place worker node update when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes with both virtual machine shapes and bare metal shapes.

This section applies to managed nodes only.

You can update the properties of worker nodes in a node pool by changing properties of the existing node pool, and then terminating and replacing the nodes by cycling the nodes and selecting the Replace nodes option.

If you cycle all the managed nodes in a node pool to terminate and replace them, when new instances have a Running state, any updates to node pool properties are applied to all of the worker nodes in the node pool. Note that if you cycle an individual managed node to terminate and replace it, any updates to node pool properties are applied to the replacement node. An exception applies to the Kubernetes version. Cycling an individual managed node to terminate and replace it does not change the Kubernetes version running on the node.

For more information, see[Terminating and Replacing Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-worker-node-top.htm#replace_worker_node)

## Using the Console

To perform an 'in-place' update of a node pool in a cluster by terminating and replacing nodes:
- On the Clusters list page, select the name of the cluster where you want to update worker node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select the name of the node pool where you want to update worker node properties.
- 

From the Actions menu, select Edit and specify the required properties for worker nodes.

Note that if you change the Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See[Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutupgradingclusters.htm).
- 

Select Update to save the change.

You now cycle nodes to automatically terminate existing worker nodes, and start new worker nodes with the properties you specified.
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

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'in-place' worker node update by terminating and replacing nodes

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to specify the node pool's worker node property that you want to change. Include the`--node-pool-cycling-details`parameter in the command to specify that you want to cycle the nodes to terminate and replace them, optionally specifying a maximum allowed number of new nodes that can be created during the update operation, and a maximum allowed number of nodes that can be unavailable:
```

```

where`--<property-to-update> <new-value>`is a new value for a node pool property. Note that the property you change is irrelevant, but you must change at least one property. Also note that including`\"cycleModes\":[\"INSTANCE_REPLACE\"]`in the`--node-pool-cycling-details`parameter is optional, since it is assumed if not explicitly included.

Monitor the progress of the operation by viewing the status of the associated work request:
```

```

```

```

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)
