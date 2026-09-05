# Rebooting Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/reboot-worker-node-top.htm
- Fetched: 2026-09-05 01:58 CDT

# Rebooting Worker Nodes

Find out how to reboot a worker node in a Kubernetes cluster that you've created using Kubernetes Engine (OKE).
Note  
  
You can only cycle nodes to reboot worker nodes when using enhanced clusters. See[Working with Enhanced Clusters and Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm).

You can cycle nodes to reboot nodes with both virtual machine shapes and bare metal shapes.

You can cycle nodes to reboot both managed nodes and self-managed nodes.

Sometimes, rebooting a worker node is the best way to resolve an issue with the compute instance hosting the worker node. Rebooting a worker node power cycles the compute instance, which would, for example, clear out all the rules in the compute instance's iptables. In the case of bare metal GPU compute instances, rebooting a worker node might resolve issues such as:
- Lowered job performance or thermal throttling, caused by high GPU memory temperatures.
- Reports of fewer than the expected number of GPUs.
- NVLink errors, indicated by the NVIDIA Fabric Manager failing to start, or by NCCL jobs failing to run.

Using Kubernetes Engine, you can:
- Reboot specific managed nodes.
- Reboot specific self-managed nodes.

When you cycle and reboot a worker node, Kubernetes Engine automatically cordons and drains the worker node before shutting it down. The compute instance hosting the worker node is then rebooted. The shutdown command that is sent to the compute instance hosting the worker node depends on the number of minutes you specify as the eviction grace period (the length of time to allow to cordon and drain worker nodes):
- If you specify an eviction grace period of zero minutes, a RESET command is sent to the compute instance. The instance is immediately powered off, and then powered back on.
- If you specify an eviction grace period greater than zero minutes, a SOFTRESET command is sent to the compute instance. After waiting 15 minutes for the operating system to shut down, the instance is powered off, and then powered back on.

Note that the instance itself is not terminated, and keeps the same OCID and network address.

Note the following considerations when cycling to reboot worker nodes:
- You have to cycle and reboot managed nodes individually. You cannot select a managed node pool and cycle and reboot all the managed nodes within it.
- You can use the Console, the CLI, or the API to cycle and reboot managed nodes.
- You have to use the CLI or the API to cycle and reboot self-managed nodes. You cannot use the Console to cycle and reboot self-managed nodes.

## Cordoning and draining when cycling and rebooting nodes

When you select an individual worker node (either a managed node or a self-managed node), and specify that you want to cycle and reboot that node, you can specify Cordon and drain options. In the case of managed nodes, the Cordon and drain options you specify for a managed node override the Cordon and drain options specified for the node pool.

For more information, see[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm)

## Rebooting Worker Nodes

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/reboot-worker-node-top.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/reboot-worker-node-top.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/reboot-worker-node-top.htm#)
- 

To reboot a specific managed node:
- On the Clusters list page, select the name of the cluster that contains the worker node that you want to reboot. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node Pools tab, and then select the name of the node pool that contains the worker node that you want to reboot.
- 

Select Cycle node from the Actions menu (three dots) beside the node that you want to reboot.
- In the Cycle node dialog:
- Select Reboot node from the Cycling options list.
- 

Specify when and how to cordon and drain the worker node before performing the reboot action, by specifying:

- Eviction grace period (mins): The length of time to allow to cordon and drain the worker node before performing the action. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon a worker node and drain it of its workloads. To perform the action immediately, without cordoning and draining the worker node, specify 0 minutes.
- Force action after grace period: Whether to perform the action at the end of the eviction grace period, even if the worker node hasn't been successfully cordoned and drained. By default, this option isn't selected.

See[Cordoning and Draining Managed Nodes Before Shut Down or Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdeletingworkernodes_topic-Notes_on_cordon_and_drain.htm).
- Select Cycle node to start the reboot operation.
- 

Monitor the progress of the operation by viewing the status of the associated work request on the Work requests tab (see[Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengviewingworkrequests.htm#get_work_requests)).
- 

To reboot a specific managed node or self-managed node

To reboot a specific managed node or self-managed node, use the[oci ce cluster reboot-cluster-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/reboot-cluster-node.html)command and required parameters:

```

```

For example:

```

```

- 

To reboot a specific managed node using the OCI API:

Run the[RebootClusterNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/RebootClusterNode)operation to reboot a specific managed node using the OCI API.

To reboot a managed node or self-managed node using the Kubernetes API:
Note  
  

To use the Kubernetes API to reboot a managed node or self-managed node that uses a custom image (rather than a platform image or an OKE image), an IAM policy must provide access to the custom image. If such a policy does not already exist, create a policy with the following policy statement:

```

```

See[Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm).
- Create a yaml file to define a`NodeOperationRule`custom resource, similar to the following:
```

```

where:
- `name: <rule-name>`specifies a name of your choosing for the`NodeOperationRule`custom resource. For example,`name: my-reboot-rule`
- `oke.oraclecloud.com/node_operation: "<value>"`specifies a value of your choosing for the`oke.oraclecloud.com/node_operation`label key. Nodes that you want to reboot must have this label key-value pair attached to them. For example:
```

```

Note that the value you specify for the`oke.oraclecloud.com/node_operation`label key must conform to the requirements in the[Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)topic in the Kubernetes documentation. Only[Kubernetes equality-based requirements](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#equality-based-requirement)are supported.
- `matchCustomLabels`optionally specifies a custom label with a key-value pair of your choosing in the format`<custom-key>: "<value>"`. You can optionally specify a custom label key-value pair to meet your own particular usecase. For example:
```

```

The custom label key-value pair you specify must conform to the requirements in the[Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set)topic in the Kubernetes documentation. Only[Kubernetes equality-based requirements](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#equality-based-requirement)are supported.

Note that if you do specify a custom label key-value pair in the manifest, then nodes are only rebooted if they have both this custom label and the`oke.oraclecloud.com/node_operation: "<value>"`label.
- `maxParallelism: <n>`specifies the number of worker nodes to reboot in parallel, up to a maximum of 20.
- `evictionGracePeriod: <number-of-minutes>`specifies the length of time to allow to cordon and drain worker nodes before rebooting them. Either accept the default (60 minutes, which is the maximum) or specify an alternative. For example, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To reboot worker nodes immediately, without cordoning and draining them, specify 0 minutes.
- `isForceActionAfterGraceDuration: <true|false>`specifies whether to reboot worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. Defaults to`false`if not specified.

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

(optional) You can view the node reboot action in progress by entering:
```

```
For example:
```

```
Example output:
```

```
