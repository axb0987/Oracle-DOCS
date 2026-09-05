# Upgrading Managed Nodes by Replacing Boot Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Upgrade_By_Cycling_and_Replacing_Boot_Volumes.htm
- Fetched: 2026-09-05 01:56 CDT

# Upgrading Managed Nodes by Replacing Boot Volumes

Find out how to upgrade the properties of worker nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes and replacing their boot volumes, using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to perform an in-place worker node upgrade when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes with both virtual machine shapes and bare metal shapes.

This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

You can upgrade the version of Kubernetes running on managed nodes in a node pool by specifying a more recent Kubernetes version for the existing node pool, and then cycling the nodes and selecting the Replace boot volume option.

When instances return to a Running state, they run the more recent Kubernetes version you specified. Note that if you cycle an individual managed node to replace its boot volume, the Kubernetes version is not changed.

For more information, see[Replacing Boot Volumes of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm)

## Using the Console

To perform an 'in-place' upgrade of a node pool in a cluster, by specifying a more recent Kubernetes version for the existing node pool and then cycling nodes to replace their boot volumes:
- On the Clusters list page, select the name of the cluster where you want to change the Kubernetes version running on managed nodes. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and select the name of the node pool where you want to upgrade the Kubernetes version running on the managed nodes.
- 

On the node pool details page, select Edit from the Actions menu.
- 

In the Version field of the Edit node pool dialog, specify the required Kubernetes version for managed nodes. We recommend that you select a version number that has the format`x.y`(see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm)).

The Kubernetes version you specify must be compatible with the version that is running on the control plane nodes.

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Select Update to save the change.

You now cycle nodes to automatically replace the boot volumes of the existing worker nodes, and re-start the worker nodes with the Kubernetes version you specified.
- 

From the Actions menu, select Cycle nodes .

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the operation. For more information, see[Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb)in the Kubernetes documentation.
- 

In the Cycle nodes dialog:
- Select Replace boot volume from the Cycling options list.
- Control the number of nodes to update in parallel, and balance service availability and cost, by specifying:
- Maximum unavailable (Maximum number or percentage of unavailable nodes): The maximum number of nodes to allow to be unavailable in the node pool during the boot volume replacement operation (expressed either as an integer or as a percentage). If you specify an integer for the number of unavailable nodes, do not specify a number greater than the value of Node count .

See[Balancing service availability and cost when cycling and replacing boot volumes of managed nodes in node pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_balancing-service-availability-and-cost-when-cycling-and-replacing-boot-volumes).
- Select Cycle nodes to start the boot volume replacement operation.

Kubernetes Engine uses the Cordon and drain options specified for the node pool to cordon and drain the worker nodes. For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).

## Using the CLI

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

### To perform an 'in-place' managed node upgrade by cycling and replacing boot volumes

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to change the node pool's worker node Kubernetes version property.
```

```

Monitor the progress of the operation by viewing the status of the associated work request:
```

```

```

```

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)
