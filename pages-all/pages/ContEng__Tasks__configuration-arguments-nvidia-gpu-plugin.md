# NVIDIA GPU Plugin
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm
- Fetched: 2026-09-05 01:53 CDT

# NVIDIA GPU Plugin

When you enable the NVIDIA GPU Plugin cluster add-on, you can pass the following key/value pairs as arguments.

Note that to ensure that workloads running on NVIDIA GPU worker nodes are not interrupted unexpectedly, we recommend that you choose the version of the NVIDIA GPU Plugin add-on to deploy, rather than specifying that you want Oracle to update the add-on automatically.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`deviceIdStrategy`Device ID Strategy

Which strategy to use for passing device IDs to the underlying runtime.

One of:
- `uuid`
- `index`Optional`uuid`
`deviceListStrategy`Device List Strategy

Which strategy to use for passing the device list to the underlying runtime.

Supported values:
- `envvar`
- `volume-mounts`
- `cdi-annotations`
- `cdi-cri`

Multiple values are supported, in a comma-separated list. Optional`envvar`
`driverRoot`Driver Root The root path for the NVIDIA driver installation. Optional`/`
`failOnInitError`FailOnInitError

Whether to fail the plugin if an error is encountered during initialization.

When set to`false`, blocks the plugin indefinitely instead of failing. Optional`true`
`migStrategy`MIG Strategy

Which strategy to use for exposing MIG (Multi-Instance GPU) devices on GPUs that support it.

One of:
- `none`
- `single`
- `mixed`Optional`none`
`nvidia-gpu-device-plugin.ContainerResources`nvidia-gpu-device-plugin container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`passDeviceSpecs`Pass Device Specs Whether to pass the paths and desired device node permissions for any NVIDIA devices being allocated to the container. Optional`false`
`useConfigFile`Use Config File from ConfigMap

Whether to use a configuration file to configure the Nvidia Device Plugin for Kubernetes. The configuration file is derived from a ConfigMap.

If set to`true`, you have to create a ConfigMap in the cluster, name the ConfigMap`nvidia-device-plugin-config`, and specify values for configuration arguments. See[Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm#top__example-configmap).

The ConfigMap is referenced by the`nvidia-gpu-device-plugin`daemonset. Optional`false`

Example of`nvidia-device-plugin-config`ConfigMap:
```

```

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`nvidia-gpu-device-plugin.ContainerResources`Y

Defines CPU and memory requests and limits for NVIDIA GPU Plugin pods.

The plugin runs on every GPU node as a DaemonSet, so total resource usage increases with the number of GPU nodes.

Additional GPU nodes increase:
- GPU health-monitoring overhead
- Device-allocation tracking
- Node-level resource reporting

If the resources are undersized:
- The plugin might become unstable on nodes.
- GPU resources might not be advertised correctly.
- Pods might fail to schedule on GPU nodes.
- GPU availability might be inconsistent across nodes.
- Allocate sufficient memory on each GPU node.
- Adjust resources based on the number of GPUs on each node and the intensity of GPU workloads.
`affinity`/`nodeSelectors`/`tolerations`Y

Control the nodes on which NVIDIA GPU Plugin pods run.
- Ensures that the plugin runs only on GPU nodes.
- Prevents unnecessary deployment on CPU-only nodes.
- Avoids wasting resources on nodes that do not contain GPUs.

If these arguments are misconfigured:
- The plugin might run on CPU-only nodes and waste resources.
- The plugin might not run on GPU nodes, making the GPUs unusable by Kubernetes workloads.
- Use node selectors that match the labels applied to GPU nodes.
- Configure tolerations when GPU nodes are tainted.
`topologySpreadConstraints`N

Controls how NVIDIA GPU Plugin pods are distributed across nodes and availability domains.

Topology spread constraints help maintain an even distribution in multi-domain clusters and clusters with heterogeneous GPU node pools.

If topology spread constraints are not configured:
- Plugin pods might be distributed unevenly.
- Resilience during node or availability-domain failures might be reduced.

Use topology spread constraints for large GPU clusters that span multiple availability domains or contain heterogeneous GPU node pools.
`numOfReplicas`N

Controls the number of replicas for components that support replica-based scaling.

The NVIDIA GPU Plugin runs as a DaemonSet with one pod on each eligible GPU node. It is not scaled by changing a replica count. Not applicable Not applicable
`rollingUpdate`N

Controls how NVIDIA GPU Plugin pods are updated.

In large clusters, an update can affect many GPU nodes and temporarily reduce GPU availability.
- GPU workloads might be interrupted.
- GPUs might be temporarily unavailable while plugin pods are updated.
- Use a controlled rolling update strategy.
- Avoid updating a large number of GPU nodes simultaneously.
`failOnInitError`Y

Controls the plugin behavior when initialization fails.

Initialization failures become more likely to occur somewhere in the cluster as the number of GPU nodes increases.
- If the value is`true`, the plugin might terminate and the GPU on the affected node becomes unavailable.
- If the value is`false`, the plugin might remain running without becoming operational, making the failure less visible.
- Keep the value set to`true`so that initialization failures remain visible.
- Monitor plugin initialization failures across GPU nodes.
`deviceListStrategy`/`deviceIdStrategy`N

Control how GPU devices are identified and exposed to containers.

The selected strategies affect container-runtime integration and GPU-allocation efficiency across GPU nodes.

If configured incorrectly, GPU devices might not be identified or injected consistently into containers. This might result in GPU workload failures, incorrect device assignments, or scheduling issues across GPU nodes. Configure`deviceListStrategy`and`deviceIdStrategy`to match your container runtime and GPU environment, and use the default uuid device identification strategy unless a validated use case requires otherwise.
`migStrategy`N

Controls how NVIDIA Multi-Instance GPU resources are exposed to Kubernetes.

Multi-Instance GPU can improve GPU sharing and utilization as the number of GPU workloads increases.

If this argument is misconfigured:
- GPU resources might become fragmented.
- Workload scheduling might become more complex.
