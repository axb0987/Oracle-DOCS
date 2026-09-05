# NVIDIA GPU Operator
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm
- Fetched: 2026-09-05 01:53 CDT

# NVIDIA GPU Operator

When you enable the NVIDIA GPU Operator cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`skipNodeFeatureDiscoveryDependencyCheck`skipNodeFeatureDiscoveryDependencyCheck Skip Node Feature Discovery dependency check. Optional`false`
`disableNvidiaGpuPlugin`disableNvidiaGpuPlugin Disable the existing NvidiaDevicePlugin add-on and related resources. Optional`false`
`cdi.enabled`Enable Container Device Interface Flag to enable Container Device Interface. Optional

`false`for version 25.3.x.

`true`for version 25.10.x and later.
`cdi.default`Enable CDI as default Flag to enable the container runtime to use CDI as the default option to perform device injection. Optional

`false`for version 25.3.x.

Deprecated in version 25.10.x and later.
`daemonsets.labels`DaemonSets Labels Labels for all GPU Operator DaemonSets. JSON text or Base64-encoded JSON map. Optional`null`
`daemonsets.annotations`DaemonSets Annotations Annotations for all GPU Operator DaemonSets. JSON text or Base64-encoded JSON map. Optional`null`
`daemonsets.tolerations`DaemonSets Tolerations Tolerations for all GPU Operator DaemonSets. JSON text or Base64-encoded JSON array. Optional`null`
`daemonsets.rollingUpdate.maxUnavailable`DaemonSets MaxUnavailable Maximum number of unavailable pods for rolling update on GPU Operator DaemonSets. Optional`1`
`dcgm.enabled`Enable DCGM Enable NVIDIA DCGM Hostengine as a separate pod. Optional`false`
`dcgm.args`DCGM Args Arguments for DCGM Hostengine. JSON plain text or Base64-encoded JSON array. Optional`null`
`dcgm.env`DCGM Env Environment variables for DCGM Hostengine. JSON plain text or Base64-encoded JSON. Optional`null`
`dcgm.containerResources`DCGM Resources Resource requests and limits for the DCGM Hostengine pod. JSON plain text or Base64-encoded JSON. Optional`null`
`dcgmExporter.enabled`Enable DCGM Exporter Enable the DCGM Exporter DaemonSet for metrics. Optional`true`
`dcgmExporter.env`DCGM Exporter Env Environment variables for DCGM Exporter. JSON plain text or Base64-encoded JSON. Optional`null`
`dcgmExporter.resources`DCGM Exporter Resources Resource requests and limits for the DCGM Exporter pod. JSON plain text or Base64-encoded JSON. Optional`null`
`dcgmExporter.service.internalTrafficPolicy`Exporter Service Traffic Policy InternalTrafficPolicy for the DCGM Exporter ClusterIP service. Optional`Cluster`
`dcgmExporter.serviceMonitor.enabled`Enable ServiceMonitor Enable a ServiceMonitor for NVIDIA DCGM Exporter. Optional`false`
`dcgmExporter.serviceMonitor.interval`ServiceMonitor Interval Scrape interval for NVIDIA DCGM Exporter. Supports`y`,`w`,`d`,`h`,`m`,`s`, and`ms`. Optional`15s`
`dcgmExporter.serviceMonitor.honorLabels`ServiceMonitor Honor Labels Prefer target metric labels on collisions. Optional`false`
`dcgmExporter.serviceMonitor.additionalLabels`ServiceMonitor Additional Labels Additional labels for the ServiceMonitor. JSON plain text or Base64-encoded JSON map. Optional`null`
`dcgmExporter.serviceMonitor.relabelings`ServiceMonitor Relabelings Relabeling rules for the ServiceMonitor. JSON plain text or Base64-encoded JSON. Optional`null`
`dcgmExporter.config.name`Exporter ConfigMap Name Name of the ConfigMap that provides custom metrics configuration for DCGM Exporter. Optional`null`
`migManager.enabled`Enable MIG Manager Enable deployment of NVIDIA MIG Manager. Optional`false`
`migManager.resources`MIG Manager Resources Resource requests and limits for each MIG Manager pod. JSON plain text or Base64-encoded JSON. Optional`null`
`migManager.env`MIG Manager Env Environment variables for MIG Manager. JSON plain text or Base64-encoded JSON. Optional`null`
`migManager.config.name`MIG ConfigMap Name ConfigMap name with`mig-parted`configuration for MIG Manager. Optional`null`
`migManager.gpuClientsConfig.name`MIG GPU Clients Config ConfigMap name with`gpu-clients`configuration for MIG Manager. Optional`null`
`devicePlugin.enabled`Enable Device Plugin Enable NVIDIA Kubernetes Device Plugin. Optional`true`
`devicePlugin.args`Device Plugin Args Arguments for the Device Plugin. JSON plain text or Base64-encoded JSON array. Optional`null`
`devicePlugin.env`Device Plugin Env Environment variables for the Device Plugin. JSON plain text or Base64-encoded JSON. Optional`null`
`devicePlugin.resources`Device Plugin Resources Resource requests and limits for each Device Plugin pod. JSON plain text or Base64-encoded JSON. Optional`null`
`devicePlugin.config.name`Device Plugin ConfigMap Name ConfigMap name that provides Device Plugin configuration, shared with GFD when applicable. Optional`null`
`devicePlugin.mps.root`MPS Root MPS root path on the host. Optional`/run/nvidia/mps`
`toolkit.enabled`Enable Toolkit Enable deployment of NVIDIA Container Toolkit. Optional`true`
`toolkit.env`Toolkit Env Environment variables for the Container Toolkit. JSON plain text or Base64-encoded JSON. Optional`null`
`toolkit.resources`Toolkit Resources Resource requests and limits for each Container Toolkit pod. JSON plain text or Base64-encoded JSON. Optional`null`
`toolkit.installDir`Toolkit Install Dir Install directory of Container Toolkit utilities on the host. Optional`/usr/local/nvidia`
`mig.strategy`MIG Strategy MIG strategy for GFD and Device Plugin. Valid values are`none`,`single`, and`mixed`. Optional`single`
`operator.logging.level`Operator Log Level Zap logging level:`debug`,`info`,`error`, or an integer &gt; 0 for custom verbosity. Optional`info`
`operator.resources`Operator Resources Resource requests and limits for the GPU Operator pod. JSON plain text or Base64-encoded JSON. Optional`null`
`hostPaths.rootFS`Host RootFS Host root filesystem path. The path must be chroot-able. Optional`/`
`hostPaths.driverInstallDir`Driver Install Dir Root directory for NVIDIA driver files on the host. Optional`/run/nvidia/driver`
`driver.rdma.enabled`Enable RDMA in Driver Enable RDMA support for the NVIDIA driver. Optional`false`
`driver.rdma.useHostMofed`Use Host MOFED Use host-provided Mellanox OFED instead of container-provided Mellanox OFED. Optional`false`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`devicePlugin.*`Y

Controls the NVIDIA device plugin that exposes GPUs to Kubernetes.

The device plugin runs on every GPU node and is responsible for:
- Advertising`nvidia.com/gpu`resources
- Enabling GPU scheduling

The configuration directly affects scheduler decisions and GPU workload placement.

If this argument is misconfigured:
- GPUs might not be visible to Kubernetes.
- Pods requesting GPUs might remain in the`Pending`state.
- GPU availability might be inconsistent across nodes.
- Scheduling failures might occur at scale.
- Set`devicePlugin.enabled`to`true`.
- Allocate sufficient resources by using`devicePlugin.resources`.
- Use a consistent configuration across all GPU nodes.
`toolkit.*`Y

Controls the NVIDIA Container Toolkit, which provides GPU access inside containers.

The toolkit runs on every GPU node and is required for GPU workloads to access GPUs inside containers.

If this argument is misconfigured, pods might be scheduled successfully but:
- GPU workloads might fail to start.
- Containers might not be able to access GPUs.
- Runtime failures might be difficult to diagnose.
- Set`toolkit.enabled`to`true`.
- Ensure that the toolkit is compatible with the container runtime.
- Allocate sufficient resources by using`toolkit.resources`.
`daemonsets.tolerations`Y

Controls whether GPU Operator components can run on GPU nodes.

GPU nodes are often tainted. All GPU Operator DaemonSets must tolerate those taints to run on the GPU nodes.

If the required tolerations are missing:
- GPU Operator components cannot run on GPU nodes.
- GPUs might become unusable throughout the cluster.
- Configure tolerations that match the taints applied to GPU nodes.
- Validate the tolerations for all GPU node pools.
`daemonsets.rollingUpdate.maxUnavailable`Y

Controls how many nodes are updated simultaneously.

The value affects the number of GPU nodes that are temporarily unavailable during an update.

In a large cluster, an update might affect many nodes.

If the value is too high:
- Too many GPU nodes might be unavailable at the same time.
- GPU workloads might be disrupted.

If the value is too low, rolling out the update across thousands of nodes might take a long time.

Use a balanced value that is not overly aggressive. Set the value based on the cluster size and the amount of disruption that workloads can tolerate.
`operator.resources`Y

Defines the CPU and memory resources for the GPU Operator controller.

The operator manages components including:
- The device plugin
- The NVIDIA Container Toolkit
- Multi-Instance GPU
- NVIDIA Data Center GPU Manager

As the number of nodes increases, the operator manages more objects and requires more resources.

If the resources are undersized:
- Reconciliation might be slow.
- The operator might become unstable.
- Configuration changes and component rollouts might be delayed.
- Increase CPU and memory resources for large clusters.
- Monitor operator logs and memory usage.
`cdi.enabled`Y

Enables the Container Device Interface.
- Simplifies injecting GPUs into containers.
- Improves runtime consistency across nodes.

If the Container Device Interface is disabled, the older runtime integration might:
- Cause inconsistencies.
- Make troubleshooting more complex.
- Set`cdi.enabled`to`true`.
- Use the default settings unless you have a specific requirement.
`mig.strategy`Y

Controls Multi-Instance GPU partitioning.

Multi-Instance GPU partitioning enables workloads to share GPUs and affects scheduler behavior.

If this argument is misconfigured:
- GPU resources might become fragmented.
- Pods might not find a matching GPU partition.
- Behavior might be inconsistent across nodes.
- Use a consistent Multi-Instance GPU strategy throughout the cluster.
- Avoid mixed configurations unless they are required.
`dcgmExporter.*`Y

Controls GPU metrics collection.

The exporter generates GPU metrics for each node, increasing Prometheus load and network traffic as the number of GPU nodes increases.

If this argument is misconfigured:
- Scraping metrics too frequently might cause high overhead.
- Scraping metrics too infrequently might provide insufficient visibility.
- Tune`serviceMonitor.interval`.
- Allocate sufficient resources by using`dcgmExporter.resources`.
`dcgm.*`Y

Controls the NVIDIA Data Center GPU Manager host engine.

The optional component tracks GPU health across the cluster.
- If the component is disabled, visibility into GPU health is limited.
- If the component is enabled with insufficient resources, it might become unstable.
- Enable the component only when it is required.
- Allocate sufficient resources.
`skipNodeFeatureDiscoveryDependencyCheck`N

Controls the dependency check for Node Feature Discovery.

The dependency check affects node labeling and GPU detection.

If Node Feature Discovery is missing:
- GPU nodes might not be labeled.
- The operator might fail to detect GPU nodes.
- Use this argument only when Node Feature Discovery is already installed.
- Ensure that the required node labels are present and correct.
`disableNvidiaGpuPlugin`Y

Disables the standalone NVIDIA GPU device plugin.

Disabling the standalone plugin prevents duplicate GPU device plugins from running in the cluster.

If this argument is configured incorrectly:
- Multiple GPU device plugins might run.
- The plugins might conflict.
- GPU resources might be reported incorrectly.
