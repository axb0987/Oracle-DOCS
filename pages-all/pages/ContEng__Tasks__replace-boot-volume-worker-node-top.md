# Replacing Boot Volumes of Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm
- Fetched: 2026-09-05 01:58 CDT

# Replacing Boot Volumes of Worker Nodes

Find out how to replace the boot volumes of worker nodes in a Kubernetes cluster that you've created using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to replace the boot volumes of worker nodes when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes to replace the boot volumes of worker nodes with both virtual machine shapes and bare metal shapes.

You can cycle nodes to replace the boot volumes of both managed nodes and self-managed nodes.

Sometimes, replacing the boot volumes of compute instances hosting worker nodes is the best way to resolve an issue with the worker nodes. For example:
- To address any configuration drift that might have occurred since the instance was originally launched.
- To address any underlying hardware faults.

Using Kubernetes Engine, you can:
- Replace the boot volumes of all the nodes in a managed node pool, when you want to update one or more supported node properties (see[Replacing the boot volumes of all nodes in a managed node pool to change node properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_BVR-node-pools)).
- Replace the boot volumes of specific managed nodes and self-managed nodes (see[Replacing the boot volumes of individual managed and self-managed nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_BVR-indvidual-nodes)).

When you cycle and replace the boot volume of a worker node, Kubernetes Engine automatically cordons and drains the worker node before shutting it down. The compute instance hosting the worker node is stopped, the boot volume is replaced, and the instance is restarted. Note that the instance itself is not terminated, and keeps the same OCID and network address.

## Replacing the boot volumes of all nodes in a managed node pool to change node properties

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

Replacing the boot volumes of all the nodes in a node pool can be useful when you want to:
- Update one or more of the properties in the list (see[Updating Worker Nodes in an Existing Node Pool by Replacing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Update_By_Cycling_and_Replacing_Boot_Volumes.htm)).
- Upgrade the Kubernetes version running on the nodes in the node pool (see[Upgrading Managed Nodes by Replacing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_topic-InPlace_Worker_Node_Upgrade_By_Cycling_and_Replacing_Boot_Volumes.htm)).
- Roll back the Kubernetes version running on managed nodes to an earlier available version (see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode_Rolling-Back.htm)).

## Replacing the boot volumes of individual managed and self-managed nodes

You can cycle individual managed nodes or self-managed nodes to replace their boot volumes when boot volume replacement is all that you require.

Note the following when cycling individual managed nodes or self-managed nodes to replace their boot volumes:
- For both managed nodes and self-managed nodes, existing node configuration is preserved when cycling nodes to replace boot volumes. In the case of managed nodes, any updates to node properties specified for the node pool are ignored (including changes to the Kubernetes version configured for the node pool.).
- You can use the Console, the CLI, or the API to cycle and replace the boot volumes of managed nodes.
- You have to use the CLI or the API to cycle and replace the boot volumes of self-managed nodes. You cannot use the Console to cycle and replace the boot volumes of self-managed nodes.

## Balancing service availability and cost when cycling and replacing boot volumes of managed nodes in node pools

When you cycle all the managed nodes in a node pool to replace their boot volumes, the greater the number of nodes that you allow to be unavailable during the replace boot volume operation, the more nodes Kubernetes Engine can update in parallel without increasing costs. However, the greater the number of nodes that you allow to be unavailable, the more service availability might be compromised.

To tailor Kubernetes Engine behavior to meet your own requirements for service availability and cost, you can specify a value for maxUnavailable . For more information, see[Balancing Service Availability and Cost When Cycling Managed Nodes in Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/balance-service-availability-cost.htm).

## Cordoning and draining when cycling and replacing boot volumes of nodes

When you select a node pool and specify that you want to cycle and replace the boot volumes of its worker nodes, Kubernetes Engine automatically cordons and drains the existing managed nodes. Kubernetes Engine uses the Cordon and drain options specified for the node pool.

When you select an individual worker node (either a managed node or a self-managed node), and specify that you want to cycle and replace the boot volume of that node, you can specify Cordon and drain options. In the case of managed nodes, the Cordon and drain options you specify for a managed node override the Cordon and drain options specified for the node pool.

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm)

## Replacing Boot Volumes of Worker Nodes

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#)
- 

To replace the boot volumes of all the worker nodes in a managed node pool:
- On the Clusters list page, select the name of the cluster that contains the worker nodes that you want to replace the boot volumes of. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool that contains the worker nodes that you want to replace the boot volumes of.
- From the Actions menu, select Edit , and change at least one of the supported properties listed in[Replacing the boot volumes of all nodes in a managed node pool to change node properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_BVR-node-pools).
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

To replace the boot volume of a specific managed node:
- On the Clusters list page, select the name of the cluster that contains the worker node that you want to replace the boot volume of. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab, and then select the name of the node pool that contains the worker node that you want to replace the boot volume of.
- 

On the Nodes tab, select Cycle node from the Actions menu (three dots) beside the node that you want to replace the boot volume of.
- In the Cycle node dialog:
- Select Replace boot volume from the Cycling options list.
- 

Specify when and how to cordon and drain the worker node before performing the boot volume replacement action, by specifying:

- Eviction grace period (mins): The length of time to allow to cordon and drain the worker node before performing the action. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon a worker node and drain it of its workloads. To perform the action immediately, without cordoning and draining the worker node, specify 0 minutes.
- Force action after grace period: Whether to perform the action at the end of the eviction grace period, even if the worker node hasn't been successfully cordoned and drained. By default, this option isn't selected.

See[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Cycle node to start the operation.
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).
- 

To replace the boot volumes of all the worker nodes in a managed node pool

To replace the boot volumes of all the worker nodes in a managed node pool, use the[oci ce node-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/update.html)command and required parameters:
```

```

where`--<property-to-update> <new-value>`is at least one of the supported properties listed in[Replacing the boot volumes of all nodes in a managed node pool to change node properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node_top__section_BVR-node-pools), specified as follows:
- `--node-source-details "{\"sourceType\":\"IMAGE\", \"imageId\":\"<image-id-for-bvr>\", \"bootVolumeSizeInGBs\":<boot-volume-size>}"`
- `--node-metadata "{\"key1\":\"value1\"}"`
- `--ssh-public-key "<key>"`
- `--kms-key-id "<key-ocid>"`
- `--kubernetes-version <k8s-version>`

For example:
```

```

To replace the boot volume of a specific managed node or self-managed node

To replace the boot volume of a specific managed node or self-managed node, use the[oci ce cluster replace-boot-volume-cluster-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/replace-boot-volume-cluster-node.html)command and required parameters:

```

```

For example:

```

```

- 

To replace the boot volumes of all the worker nodes in a managed node pool using the OCI API:

Run the[UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)operation to replace the boot volumes of all the worker nodes in a managed node pool.

To replace the boot volume of a specific managed node using the OCI API:

Run the[ReplaceBootVolumeClusterNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/ReplaceBootVolumeClusterNode)operation to replace the boot volume of a specific managed node using the OCI API.

To replace the boot volume of a managed node or self-managed node using the Kubernetes API:
Note  
  

To use the Kubernetes API to replace the boot volume of a managed node or self-managed node that uses a custom image (rather than a platform image or an OKE image), an IAM policy must provide access to the custom image. If such a policy does not already exist, create a policy with the following policy statement:

```

```

See[Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm).
- Create a yaml file to define a`NodeOperationRule`custom resource, similar to the following:
```

```

where:
- `name: <rule-name>`specifies a name of your choosing for the`NodeOperationRule`custom resource. For example,`name: my-bvr-rule`
- `oke.oraclecloud.com/node_operation: "<value>"`specifies a value of your choosing for the`oke.oraclecloud.com/node_operation`label key. Nodes for which you want to replace boot volumes must have this label key-value pair attached to them. For example:
```

```

Note that the value you specify for the`oke.oraclecloud.com/node_operation`label key must conform to the requirements in the[Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)topic in the Kubernetes documentation. Only[Kubernetes equality-based requirements](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#equality-based-requirement)are supported.
- `matchCustomLabels`optionally specifies a custom label with a key-value pair of your choosing in the format`<custom-key>: "<value>"`. You can optionally specify a custom label key-value pair to meet your own particular usecase. For example:
```

```

Note that the custom label key-value pair you specify must conform to the requirements in the[Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)topic in the Kubernetes documentation. Only[Kubernetes equality-based requirements](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#equality-based-requirement)are supported.

Note that if you do specify a custom label key-value pair in the manifest, then boot volumes are only replaced for nodes that have both this custom label and the`oke.oraclecloud.com/node_operation: "<value>"`label.
- `maxParallelism: <n>`specifies the number of worker nodes for which to replace boot volumes in parallel, up to a maximum of 20.
- `evictionGracePeriod: <number-of-minutes>`specifies the length of time to allow to cordon and drain worker nodes before replacing boot volumes. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To replace the boot volumes of worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- `isForceActionAfterGraceDuration: <true|false>`specifies whether to replace the boot volume of worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. Defaults to`false`if not specified.

For example:
```

```

- 

Use kubectl to apply the yaml file to the cluster by entering:
```

```

- 

Use kubectl to confirm that the NodeOperationRule custom resource has been created successfully by entering:
```

```

- 

Use kubectl to add a label to the node that specifies the value for the`oke.oraclecloud.com/node_operation`label key by entering:
```

```

For example:
```

```

- If you included a`matchCustomLabels`element in the manifest to specify a custom label key-value pair, use kubectl to add a label to the node that specifies the key-value pair by entering:
```

```

For example:
```

```

- 

(optional) You can view the boot volume replacement action in progress by entering:
```

```
For example:
```

```
Example output:
```

```

## Replacing Boot Volumes of Self-Managed Nodes After Cluster Credential Rotation

If you have added a self-managed node to a cluster and you subsequently rotate the cluster's credentials, replacing the self-managed node's boot volume requires extra steps (in addition to those described in[Replacing Boot Volumes of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm#replace_boot_volume_worker_node)).The extra steps are required because the cluster's CA certificate is referenced in the self-managed nodes cloud-init script.

Assume that you have already rotated the CA certificate of the cluster to which a self-managed node has been added, by following the instructions in[Rotating Cluster Credentials](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm). If you now want to replace the boot volume of the self-managed node, you have to first modify the self-managed node's cloud-init script. You have to replace the cluster's previous CA certificate referenced in the script with the cluster's current CA certificate. Follow these steps:
- Obtain details of the compute instance hosting the self-managed node, by entering:
```

```

For example:
```

```

Details about the compute instance are returned.
- 

Locate, and make a note of, the boot volume OCID (shown in`source-details`in the output of the`oci compute instance get`command), by entering:
```

```

For example:
```

```

Example output:
```

```

You use the boot volume OCID in a later step.
- 

Locate the`metadata`values shown in the output as follows:
```

```

Note that`ssh_authorized_keys`is present when SSH access to the node has been set up (which is usually, but not always, the case).

For example:
```

```
The value of`user_data`is the cloud-init script that was originally used to add the compute instance to the cluster as a self-managed node, in base64-encoded format. The cloud-init script specifies the cluster's Kubernetes API private endpoint, and the cluster's previous base64-encoded CA certificate.
- Copy the`ssh_authorized_keys`and`user_data`values and save them in a new file named`metadata.json`, by entering:
```

```

Example`metadata.json`file:
```

```

- Copy the value of`user_data`(the original base64-encoded cloud-init script), and decode it by entering:
```

```

For example:
```

```

The decoded output is the original cloud-init script. For example:
```

```

The value of`--kubelet-ca-cert`is the cluster's previous CA certificate, in base64-encoded format.
- Save the decoded output as a text file named`my-cloud-init-file`.
- Obtain the cluster's current CA certificate (that is, the cluster's CA certificate after rotation) by entering:
```

```

The cluster's current base64-encoded CA certificate is returned as a long alphanumeric string, starting with the characters`LS0t`. For example:
```

```

- In the cloud-init script that you saved in`my-cloud-init-file`, replace the original value of`--kubelet-ca-cert`with the current base64-encoded CA certificate, and save the file.

For example:
```

```

- Base64 encode the updated cloud-init script in`my-cloud-init-file`. For example, by entering:
```

```

The updated cloud-init script is base64-encoded and returned as a long alphanumeric string. For example:
```

```

- 

Update the`metadata.json`file you created earlier, as follows:
- If present, keep the value of`ssh_authorized_keys`unchanged.
- Change the value of`user_data`to the base64-encoded alphanumeric string you just created from the updated cloud-init script.

For example:
```

```

- Use the boot volume OCID that you made a note of earlier, to get details of the existing boot volume, by entering:
```

```

For example:
```

```

Example output:
```

```

- Use the output to specify the same values for the compute instance`source-details`properties in a new json file named`my-instance-source-details.json`, in the following format:
```

```

Note that you do not have to include boot volume properties in the`my-instance-source-details.json`that are shown as having a`null`value in the output of the`oci bv boot-volume get`command. For example, if the boot volume is not encrypted with a user-managed key, the value of`kms_key_id`is shown as`null`.

For example:
```

```

Note that you must provide a value for`image-id`in order to update`user_data`properties (specifically, to update the cloud-init script with the new CA certificate).
- 

Update the details of the compute instance hosting the self-managed node, by entering
```

```

- 

Verify that the compute instance hosting the self-managed node has the updated value for user_data, by entering:
```

```

For example:
```

```

Updated details about the compute instance hosting the self-managed node are returned.
```

```

Having updated the`user_data`value to the base64-encoded cloud-init file containing the new cluster CA certificate, you can now replace the boot volume of the self-managed node.
- Replace the boot volume of the self-managed node by entering:

```

```

For example:

```

```

For more information, see[Replacing Boot Volumes of Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/replace-boot-volume-worker-node-top.htm)
