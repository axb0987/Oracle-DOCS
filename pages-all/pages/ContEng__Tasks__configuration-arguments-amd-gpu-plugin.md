# AMD GPU Plugin
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-plugin.htm
- Fetched: 2026-09-05 01:53 CDT

# AMD GPU Plugin

When you enable the AMD GPU Plugin cluster add-on, you can pass the following key/value pairs as arguments.

Note that to ensure that workloads running on AMD GPU worker nodes are not interrupted unexpectedly, we recommend that you choose the version of the AMD GPU Plugin add-on to deploy, rather than specifying that you want Oracle to update the add-on automatically.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-plugin.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`affinity`affinity

A group of affinity scheduling rules.

JSON format in plain text or Base64 encoded.
Not used by:
- Nvidia GPU Operator
Possible equivalents:
- Node Feature Discovery, use`master.affinity`
- NVIDIA Network Operator, use`operator.affinity`
- CSI Driver SMB, use`contoller.affinity`
- AMD GPU Operator, use`controllerManager.affinity`Optional null null
`nodeSelectors`node selectors

You can use node selectors and node labels to control the worker nodes on which add-on pods run.

For a pod to run on a node, the pod's node selector must have the same key/value as the node's label.

Set`nodeSelectors`to a key/value pair that matches both the pod's node selector, and the worker node's label.

JSON format in plain text or Base64 encoded.
Not used by:
- NVIDIA GPU Operator
- CSI Driver SMB
Possible equivalents:
- Node Feature Discovery, use`worker.nodeSelector`
- NVIDIA Network Operator, use`operator.nodeSelectors`
- AMD GPU Operator, use`selector`or`controllerManager.nodeSelector`Optional null`{"foo":"bar", "foo2": "bar2"}`

The pod will only run on nodes that have the`foo=bar`or`foo2=bar2`label.
`numOfReplicas`numOfReplicas The number of replicas of the add-on deployment.
Not used by:
- AMD GPU Plugin
- NVIDIA GPU Operator
- NVIDIA Network Operator
- CSI Driver SMB
Possible equivalents:
- CoreDNS, use`nodesPerReplica`
- Node Feature Discovery, use`master.replicaCount`
- AMD GPU Operator, use`controllerManager.replicas`Required`1`

Creates one replica of the add-on deployment per cluster.`2`

Creates two replicas of the add-on deployment per cluster.
`rollingUpdate`rollingUpdate

Controls the desired behavior of rolling update by maxSurge and maxUnavailable.

JSON format in plain text or Base64 encoded.
Not used by:
- Node Feature Discovery
- NVIDIA Network Operator
- CSI Driver SMB
Possible equivalents:
- NVIDIA GPU Operator, use`daemonsets.rollingUpdate.maxUnavailable`
- AMD GPU Operator, use`upgradePolicy`in`devicePlugin`,`metricsExporter`,`testRunner`,`configManager`, or`draDriver`Optional null null
`tolerations`tolerations

You can use taints and tolerations to control the worker nodes on which add-on pods run.

For a pod to run on a node that has a taint, the pod must have a corresponding toleration.

Set`tolerations`to a key/value pair that matches both the pod's toleration, and the worker node's taint.

JSON format in plain text or Base64 encoded.
Possible equivalents:
- Node Feature Discovery, use`master.tolerations`and/or`worker.tolerations`
- NVIDIA GPU Operator, use`daemonsets.tolerations`
- NVIDIA Network Operator, use`operator.tolerations`
- CSI Driver SMB, use`controller.tolerations`
- AMD GPU Operator, use tolerations in`devicePlugin`,`metricsExporter`,`testRunner`,`configManager`,`draDriver`, or`controllerManager`Optional null`[{"key":"tolerationKeyFoo", "value":"tolerationValBar", "effect":"noSchedule", "operator":"exists"}]`

Only pods that have this toleration can run on worker nodes that have the`tolerationKeyFoo=tolerationValBar:noSchedule`taint.
`topologySpreadConstraints`topologySpreadConstraints

How to spread matching pods among the given topology.

JSON format in plain text or Base64 encoded.
Not used by:
- Node Feature Discovery
- NVIDIA GPU Operator
- NVIDIA Network Operator
- CSI Driver SMB
- AMD GPU Operator Optional null null

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-plugin.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`amd-gpu-device-plugin.ContainerResources`amd-gpu-device-plugin container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`pulse`Enable health checks

Time interval in seconds for the plugin to update the kubelet with device health status.

Set to`0`to disable the health check. Optional`0`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-plugin.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`amd-gpu-device-plugin.ContainerResources`Y

Defines CPU and memory requests and limits for the AMD GPU Plugin containers.

The plugin runs on every GPU node.

Total resource usage grows linearly with the number of GPU nodes.

The following activities increase:
- GPU health monitoring
- Device-state reporting to the kubelet
- Interactions with the container runtime

If the resources are undersized:
- The plugin might become unstable on nodes.
- GPUs might not be exposed correctly as`amd.com/gpu`resources.
- Pods requesting GPUs might remain in the`Pending`state.
- Resources might be reported incorrectly to the scheduler.

Increase the memory and CPU allocated on each node based on the following factors:
- The number of GPUs on the node
- Workload intensity

Monitor kubelet logs and the CPU and memory usage of the plugin.
`nodeSelectors/affinity`Y

Controls which nodes the plugin runs on by using labels.

Ensures that the plugin runs only on AMD GPU nodes.

Prevents unnecessary scheduling on CPU-only nodes.

If no selector is specified, the plugin runs on all nodes and wastes resources.

If the wrong selector is specified, the plugin does not run on GPU nodes and the GPUs are not visible to Kubernetes.

Even a small misconfiguration affecting 1–2% of nodes can result in hundreds of incorrectly configured nodes, inconsistent GPU availability, and unpredictable scheduling failures.

Use strict node labeling.
`tolerations`Y

Controls whether the plugin can run on tainted GPU nodes.

If not configured correctly, the AMD GPU Plugin DaemonSet might fail to schedule on GPU nodes with taints, preventing GPU resources from being discovered and making GPUs unavailable for workload scheduling.

If tolerations are misconfigured, the plugin cannot run on GPU nodes and the GPUs become unusable.

Ensure that tolerations match the taints applied to GPU nodes.
`pulse`Y

Controls how frequently the plugin reports GPU health information to the kubelet.

A higher reporting frequency provides better GPU health visibility but generates more kubelet and API traffic.

A lower reporting frequency reduces overhead but delays failure detection.

If updates are too frequent, CPU overhead on each node and kubelet load increase.

If updates are too infrequent or disabled, GPU health information can become stale and the scheduler might assign workloads to unhealthy GPUs.

Use a moderate interval that balances health visibility against overhead.

Avoid overly aggressive polling.
`rollingUpdate`N

Controls update behavior.

In large clusters, many nodes might be updated simultaneously, affecting GPU availability during upgrades.
- GPU workloads might be interrupted.
- GPUs might be temporarily unavailable.

Use controlled rolling updates to avoid widespread disruption.
`numOfReplicas`N
