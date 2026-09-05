# Rolling Back Managed Nodes to an Earlier Kubernetes Version
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm
- Fetched: 2026-09-05 01:56 CDT

# Rolling Back Managed Nodes to an Earlier Kubernetes Version

Find out how to roll back the Kubernetes version running on managed nodes in an existing node pool using Kubernetes Engine (OKE).
Note  
  

This section applies to managed nodes only. You can roll back managed nodes in both enhanced clusters and basic clusters.

You cannot use this procedure to roll back the Kubernetes version running on control plane nodes or virtual nodes.

You can roll back the version of Kubernetes running on managed nodes in a node pool by specifying an earlier available Kubernetes version for the existing node pool, and then replacing the existing managed nodes.

The Kubernetes version you specify must be available for the managed node pool and compatible with the version that is running on the control plane nodes. The Kubernetes versions available for a managed node pool can vary by tenancy. To see the available versions, view the Version list when editing the node pool in the Console, use the`oci ce node-pool-options get`command, or use the`GetNodePoolOptions`operation.
Important  
  

Changing the Kubernetes version configured for a managed node pool does not change the Kubernetes version running on existing managed nodes. To complete the rollback, replace the existing managed nodes.

If you use node cycling, cycle the entire managed node pool. Cycling an individual managed node does not change the Kubernetes version running on the node.

For more information about Kubernetes version selection and compatibility, see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).

## Using the Console

### To roll back managed nodes in an enhanced cluster

In an enhanced cluster, you can roll back managed nodes by specifying an earlier available Kubernetes version for the existing node pool, and then cycling all the nodes in the node pool. You can cycle the nodes by replacing their boot volumes or by terminating and replacing the nodes.
- On the Clusters list page, select the name of the cluster where you want to roll back the Kubernetes version running on managed nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and select the name of the node pool where you want to roll back the Kubernetes version running on the managed nodes.
- 

On the node pool details page, select Edit from the Actions menu.
- 

In the Version field of the Edit node pool dialog, select the required earlier Kubernetes version for managed nodes.

The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Select Update to save the change.

You now cycle all the nodes in the node pool to apply the Kubernetes version you specified.
- 

From the Actions menu, select Cycle nodes .

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the operation. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.
- 

In the Cycle nodes dialog, select one of the following options from the Cycling options list:
- 

Replace boot volume : Specify the maximum number or percentage of nodes that can be unavailable during the operation, and then select Cycle nodes .
- 

Replace nodes : Specify the maximum number or percentage of additional nodes and unavailable nodes to allow during the operation, and then select Cycle nodes .
Note  
  
Do not cycle an individual managed node to apply the rollback. Cycling an individual managed node does not change the Kubernetes version running on the node.
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).

### To roll back managed nodes in a basic cluster

Node cycling is not available in basic clusters. To roll back managed nodes in a basic cluster, specify the earlier Kubernetes version for the existing node pool, and then manually delete and replace each existing managed node in turn.
- On the Clusters list page, select the name of the cluster where you want to roll back the Kubernetes version running on managed nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and select the name of the node pool where you want to roll back the Kubernetes version running on the managed nodes.
- 

On the node pool details page, select Edit from the Actions menu.
- 

In the Version field of the Edit node pool dialog, select the required earlier Kubernetes version for managed nodes.

The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Select Update to save the change.

You now have to delete existing managed nodes so that new managed nodes are started, running the Kubernetes version you specified.
- 

For the first managed node in the node pool:
- On the node pool details page, select the Nodes tab, and then select Delete node from the Actions menu beside the node you want to delete.
- Specify when and how to cordon and drain the managed node before terminating it. Do not select Decrease node pool size , so that a new managed node is started rather than the node pool being scaled down.
- Select Delete to delete the managed node.

The managed node is deleted and a new managed node is started, running the Kubernetes version you specified.
- Repeat the previous step for each remaining managed node in the node pool, until all managed nodes in the node pool are running the Kubernetes version you specified.

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To obtain the Kubernetes versions available for a managed node pool

Use the[oci ce node-pool-options get --node-pool-option-id all](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool-options/get.html)command to obtain the Kubernetes versions available for the managed node pool.

### To roll back managed nodes in an enhanced cluster by replacing boot volumes

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to specify an earlier Kubernetes version for the node pool and to cycle all the nodes to replace their boot volumes.
```

```

Monitor the progress of the operation by viewing the status of the associated work request:
```

```

```

```

### To roll back managed nodes in an enhanced cluster by terminating and replacing nodes

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to specify an earlier Kubernetes version for the node pool and to cycle all the nodes to terminate and replace them. Specify the OCID of an image that corresponds to the Kubernetes version.
```

```

Monitor the progress of the operation by viewing the status of the associated work request:
```

```

```

```

### To roll back managed nodes in a basic cluster by manually deleting and replacing nodes

First, use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to specify the earlier Kubernetes version for the node pool and the OCID of the corresponding image:
```

```

Then, delete each managed node in the node pool in turn, specifying that you want to start a new managed node to replace the managed node you have deleted:
```

```

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[GetNodePoolOptions](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePoolOptions/GetNodePoolOptions)operation to obtain the Kubernetes versions available for a managed node pool.

Use the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)
