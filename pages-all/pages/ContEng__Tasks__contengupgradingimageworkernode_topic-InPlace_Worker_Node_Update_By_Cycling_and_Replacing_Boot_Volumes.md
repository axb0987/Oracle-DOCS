# Updating Worker Nodes in an Existing Node Pool by Replacing Boot Volumes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Boot_Volumes.htm
- Fetched: 2026-09-05 01:56 CDT

# Updating Worker Nodes in an Existing Node Pool by Replacing Boot Volumes

Find out how to update the properties of worker nodes in a node pool by changing properties of the existing node pool, and then cycling the nodes and replacing their boot volumes, using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to perform an in-place worker node update when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes with both virtual machine shapes and bare metal shapes.

This section applies to managed nodes only.

When you want to update one or more of the following node properties specified for the node pool, you can cycle all the nodes in a node pool to replace their boot volumes:
- `BootVolumeSizeInGBs`
- `ImageId`
- `KmsKeyId`
- `KubernetesVersion`
- `NodeMetadata`
- `SshPublicKey`

Note the following when cycling all the nodes in a node pool to replace their boot volumes:
- If you update one or more of the properties in the list, the property updates are applied to all the nodes in the node pool.
- If you do not update any of the properties in the list, the nodes in the node pool are not cycled and boot volumes are not replaced.
- If you update a property that is not in the list, the node cycling and boot volume replacement operation fails.

Note that if you cycle an individual managed node to replace its boot volume, the existing node configuration is preserved and changes to node pool properties are not applied. In particular, changing the Kubernetes version configured for the node pool does not change the Kubernetes version running on an individual node when you replace only that node's boot volume.

For more information, see[Replacing Boot Volumes of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm)

## Using the Console

To perform an 'in-place' update of a node pool in a cluster by cycling and replacing the boot volumes of nodes:
- On the Clusters list page, select the name of the cluster where you want to update worker node properties. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- 

Select the Node pools tab, and then select the name of the node pool where you want to update worker node properties.
- 

From the Actions menu, select Edit and change at least one of the supported properties listed in[Updating Worker Nodes in an Existing Node Pool by Replacing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Boot_Volumes.htm).

Note that if you change the Kubernetes version, the version you specify must be compatible with the version that is running on the control plane nodes. See[Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutupgradingclusters.htm).
- 

Select Update to save the change.

You now cycle nodes to automatically replace the boot volumes of the existing worker nodes, and re-start the worker nodes with the properties you specified.
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

### To perform an 'in-place' worker node update by cycling and replacing boot volumes

Use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command to specify the node pool's worker node property that you want to change.
```

```

where`--<property-to-update> <new-value>`is at least one of the supported properties listed in[Replacing the boot volumes of all nodes in a managed node pool to change node properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_BVR-node-pools), specified as follows:
- `--node-source-details "{\"sourceType\":\"IMAGE\", \"imageId\":\"<image-id-for-bvr>\", \"bootVolumeSizeInGBs\":50}"`
- `--node-metadata "{\"key1\":\"value1\"}"`
- `--ssh-public-key "<key>"`
- `--kms-key-id "<key-ocid>"`
- `--kubernetes-version <k8s-version>`

For example:
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
