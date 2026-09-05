# Cluster Autoscaler
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-cluster-autoscaler.htm
- Fetched: 2026-09-05 01:53 CDT

# Cluster Autoscaler

When you enable the Cluster Autoscaler add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-cluster-autoscaler.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-cluster-autoscaler.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
annotations annotations

Annotations to pass to the Cluster Autoscaler deployment.

For example,`"{\"prometheus.io/scrape\":\"true\",\"prometheus.io/port\":\"8086\"}"`

JSON format in plain text or Base64 encoded. Optional ""
authType authType The authentication type the Cluster Autoscaler uses while making requests, as one of:
- `instance`specifies instance principal
- `workload`specifies workload identity Required`instance`
balanceSimilarNodeGroups balanceSimilarNodeGroups Detect similar node groups and balance the number of nodes between them. Optional`false`
balancingIgnoreLabel balancingIgnoreLabel Define a node label that should be ignored when considering node group similarity. One label per flag occurrence. The format is`label1, label2`. Optional ""
balancingLabel balancingLabel Define a node label to use when comparing node group similarity. If set, all other comparison logic is disabled, and only labels are considered when comparing groups. One label per flag occurrence. The format is`label1, label2`. Optional ""
cluster-autoscaler.ContainerResources cluster-autoscaler container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
cordonNodeBeforeTerminating (Not shown in Console) Should CA cordon nodes before terminating during downscale process. Optional`false`
coresTotal (Not shown in Console) Minimum and maximum number of cores in cluster, in the format`<min>:<max>`. Cluster autoscaler will not scale the cluster beyond these numbers. Optional`0:320000`
daemonsetEvictionForEmptyNodes (Not shown in Console) Whether DaemonSet pods will be gracefully terminated from empty nodes. Optional`false`
daemonsetEvictionForOccupiedNodes (Not shown in Console) Whether DaemonSet pods will be gracefully terminated from non-empty nodes. Optional`true`
debuggingSnapshotEnabled (Not shown in Console) Whether the debugging snapshot of cluster autoscaler feature is enabled. Optional`false`
emitPerNodegroupMetrics (Not shown in Console) If true, emit per node group metrics. Optional`false`
enforceNodeGroupMinSize (Not shown in Console) Should CA scale up the node group to the configured min size if needed. Optional`false`
estimator (Not shown in Console) Type of resource estimator to be used in scale up. Optional`binpacking`
expander expander Type of node group expander to be used in scale up.

Note that`expander=price`is not supported. Optional`random`
expendablePodsPriorityCutoff (Not shown in Console) Pods with priority below cutoff will be expendable. They can be killed without any consideration during scale down and they don't cause scale up. Pods with null priority (PodPriority disabled) are non-expendable. Optional`-10`
ignoreDaemonsetsUtilization (Not shown in Console) Whether DaemonSet pods will be ignored when calculating resource utilization for scaling down. Optional`false`
ignoreMirrorPodsUtilization (Not shown in Console) Whether Mirror pods will be ignored when calculating resource utilization for scaling down. Optional`false`
leaderElect (Not shown in Console) Start a leader election client and gain leadership before executing the main loop. Enable this when running replicated components for high availability. Optional`true`
leaderElectLeaseDuration (Not shown in Console) The duration that non-leader candidates will wait after observing a leadership renewal until attempting to acquire leadership of a led but un-renewed leader slot. This is effectively the maximum duration that a leader can be stopped before it is replaced by another candidate. This is only applicable if leader election is enabled. Optional`15s`
leaderElectRenewDeadline (Not shown in Console) The interval between attempts by the active cluster autoscaler to renew a leadership slot before it stops leading. This must be less than or equal to the lease duration. This is only applicable if leader election is enabled. Optional`10s`
leaderElectResourceLock (Not shown in Console) The type of resource object that is used for locking during leader election. Supported options are`leases`(default),`endpoints`,`endpointsleases`,`configmaps`, and`configmapsleases`. Optional`leases`
leaderElectRetryPeriod (Not shown in Console) The duration the clients should wait between attempting acquisition and renewal of a leadership. This is only applicable if leader election is enabled. Optional`2s`
maxAutoprovisionedNodeGroupCount (Not shown in Console) The maximum number of auto-provisioned groups in the cluster. Optional`15`
maxEmptyBulkDelete maxEmptyBulkDelete Maximum number of empty nodes that can be deleted at the same time. Optional`10`
maxFailingTime (Not shown in Console) Maximum time from last recorded successful autoscaler run before automatic restart. Optional`15m`
maxGracefulTerminationSec (Not shown in Console) Maximum number of seconds CA waits for pod termination when trying to scale down a node. Optional`600`
maxInactivity (Not shown in Console) Maximum time from last recorded autoscaler activity before automatic restart. Optional`10m`
maxNodeProvisionTime maxNodeProvisionTime Maximum time CA waits for node to be provisioned. Optional`15m`
maxNodesTotal (Not shown in Console) Maximum number of nodes in all node pools. Cluster autoscaler will not grow the cluster beyond this number. Optional`0`
maxTotalUnreadyPercentage (Not shown in Console) Maximum percentage of unready nodes in the cluster. After this is exceeded, CA halts operations. Optional`45`
memoryTotal (Not shown in Console) Minimum and maximum number of gigabytes of memory in cluster, in the format`<min>:<max>`. Cluster autoscaler will not scale the cluster beyond these numbers. Optional`0:6400000`
minReplicaCount (Not shown in Console) Minimum number or replicas that a replica set or replication controller should have to allow their pods deletion in scale down. Optional`0`
nodes nodes

A list of Minimum number of nodes, Maximum number of nodes, and the OCID of the nodepool to be managed by cluster autoscaler.

The format is`<min>:<max>:<node-pool1-ocid>, <min>:<max>:<node-pool2-ocid>`.

Use either`nodes`or`nodeGroupAutoDiscovery`, but not both.

JSON format in plain text or Base64 encoded. Required, if`nodeGroupAutoDiscovery`not set ""
nodeGroupAutoDiscovery (Not shown in Console)

A list of tag key/value pairs, Minimum number of nodes, Maximum number of nodes, and the OCID of the compartment in which the node pool to be managed by cluster autoscaler is located.

The format is`compartmentId:<compartment-ocid>,nodepoolTags:<tagKey1>=<tagValue1>&<tagKey2>=<tagValue2>,min:<min-nodes>,max:<max-nodes>`

Use either`nodeGroupAutoDiscovery`or`nodes`, but not both.

Note that the`minSize`and`maxSize`node pool tags always take precedence over`min:{{<min-nodes>}}`and`max:{{<max-nodes>}}`respectively.

Supported with Cluster Autoscaler version 1.30.3, version 1.31.1, version 1.32.0, and later.

JSON format in plain text or Base64 encoded. Required, if`nodes`not set
okTotalUnreadyCount (Not shown in Console) Number of allowed unready nodes, irrespective of`maxTotalUnreadyPercentage`. Optional`3`
recordDuplicatedEvents (Not shown in Console) Enable the autoscaler to print duplicated events within a 5 minute window. Optional`false`
scaleDownCandidatesPoolMinCount (Not shown in Console)

Minimum number of nodes that are considered as additional non empty candidates for scale down when some candidates from previous iteration are no longer valid. When calculating the pool size for additional candidates we take.
```

```
Required`50`
scaleDownCandidatesPoolRatio (Not shown in Console) A ratio of nodes that are considered as additional non-empty candidates for scale down when some candidates from previous iteration are no longer valid. Lower value means better CA responsiveness but possible slower scale down latency. Higher value can affect CA performance with big clusters (hundreds of nodes). Set to 1.0 to turn this heuristics off - CA will take all nodes as additional candidates. Required`0.1`
scaleDownDelayAfterAdd scaleDownDelayAfterAdd How long after scale up that scale down evaluation resumes. Required`10m`
scaleDownDelayAfterDelete (Not shown in Console) How long after node deletion that scale down evaluation resumes, defaults to scan-interval. Required`10s`
scaleDownDelayAfterFailure (Not shown in Console) How long after scale down failure that scale down evaluation resumes. Required`3m`
scaleDownEnabled scaleDownEnabled Should CA scale down the cluster. Optional`true`
scaleDownNonEmptyCandidatesCount (Not shown in Console) Maximum number of non empty nodes considered in one iteration as candidates for scale down with drain. Lower value means better CA responsiveness but possible slower scale down latency. Higher value can affect CA performance with big clusters (hundreds of nodes). Set to non positive value to turn this heuristic off - CA will not limit the number of nodes it considers. Required`30`
scaleDownUnneededTime scaleDownUnneededTime How long a node should be unneeded before it is eligible for scale down. Required`10m`
scaleDownUnreadyTime (Not shown in Console) How long an unready node should be unneeded before it is eligible for scale down. Required`20m`
scaleDownUtilizationThreshold (Not shown in Console) Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. Required`0.5`
scanInterval scanInterval How often cluster is re-evaluated for scale up or down. Optional`10s`
skipNodesWithCustomControllerPods (Not shown in Console) If`true`, cluster autoscaler will never delete nodes with pods owned by custom controllers. Optional`true`
skipNodesWithLocalStorage (Not shown in Console) If`true`, cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. Optional`true`
skipNodesWithSystemPods (Not shown in Console) If`true`, cluster autoscaler will never delete nodes with pods from kube-system (except for DaemonSet or mirror pods). Optional`true`
statusConfigMapName (Not shown in Console) The name of the status ConfigMap that CA writes. Optional`cluster-autoscaler-status`
stderrthreshold (Not shown in Console) The log severity threshold, beyond which logs are sent to stderr. For example, if you set this to`error`, all logs with a severity higher than`error`are sent to stderr. Optional`info`
unremovableNodeRecheckTimeout unremovableNodeRecheckTimeout The timeout before we check again a node that couldn't be removed before. Required`5m`
v (Not shown in Console) The number for the verbosity of logging. Optional`0`
writeStatusConfigmap (Not shown in Console) Should CA write status information to a configmap. Optional`true`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-cluster-autoscaler.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`cluster-autoscaler.ContainerResources`Y

Defines CPU and memory requests and limits for the Cluster Autoscaler pod.

As the cluster size increases, the Cluster Autoscaler experiences:
- Significant growth in cluster-state evaluation for nodes and pods
- More scheduling simulations
- Higher CPU and memory usage
- Increased decision-making latency for scale-up and scale-down operations

If the resources are undersized:
- The Cluster Autoscaler pod might be terminated because it exceeds its memory limit.
- Scaling decisions might be delayed, leaving pods in the`Pending`state.
- Cluster scan cycles might slow down, reducing responsiveness.
- A backlog of unschedulable pods might accumulate.

Increase CPU and memory resources as appropriate:
- Increase memory to process the state of a large cluster.
- Increase CPU to perform scheduling simulations and make scaling decisions more quickly.
`balanceSimilarNodeGroups`N

Controls whether the Cluster Autoscaler balances nodes across similar node pools.

Large clusters typically use multiple node pools, increasing the possibility of uneven scaling across pools.

Enabling this argument adds computation overhead and slightly increases the complexity of scaling decisions.

If this argument is disabled:
- Nodes might be distributed unevenly across similar node pools.
- Specific node pools might become hotspots.
- Fault tolerance might be reduced.

Enable this argument for environments with multiple node pools and for high-availability scenarios that require balanced scaling.
`numOfReplicas`N

Controls the number of Cluster Autoscaler pods.

The Cluster Autoscaler uses leader election. Only one active instance makes scaling decisions, while other replicas provide high availability.

If the count is too low, a node failure, pod crash, or upgrade can temporarily stop autoscaling decisions. This can delay node scale-up for pending workloads and scale-down of underutilized nodes until the Cluster Autoscaler becomes available again.

Use two or three replicas to provide high availability.
`affinity`/`nodeSelectors`/`tolerations`N

The Cluster Autoscaler is a critical control-plane component.

Pod placement affects the stability and reliability of the Cluster Autoscaler.

If these arguments are not configured appropriately:
- The Cluster Autoscaler might run on unstable nodes.
- The Cluster Autoscaler might run on resource-constrained nodes.
- Pods might restart.
- Performance might be reduced.
- Run the Cluster Autoscaler on dedicated system or infrastructure nodes with sufficient resources.
- Configure tolerations when the target system nodes are tainted.
`authType`N

Defines how the Cluster Autoscaler authenticates with OCI APIs.

The Cluster Autoscaler relies on OCI APIs to create nodes during scale-out operations and delete nodes during scale-in operations.
- Authentication failures prevent scaling operations.
- API latency or failures can delay node provisioning.
- Use a reliable authentication mechanism. Instance principals are preferred.
- Ensure that the required permissions and service limits are configured.
`rollingUpdate`N

Controls the deployment update strategy for the Cluster Autoscaler.

Cluster Autoscaler downtime stops scaling decisions and reduces cluster responsiveness during an upgrade.

If this argument is not configured appropriately:
- All replicas might restart at the same time.
- Scaling capability might be temporarily unavailable.
- Configure`maxUnavailable`carefully.
- Ensure that at least one Cluster Autoscaler instance remains active during an update.
`maxNodesTotal`Y

Defines the maximum number of nodes that the Cluster Autoscaler can manage.

This argument sets a hard upper limit for the cluster size and prevents uncontrolled scale-out.

If the value is too low, the Cluster Autoscaler stops scaling even when pods remain in the`Pending`state.

If the value is too high:
- The cluster might reach OCI tenancy or service limits.
- Costs might increase unexpectedly.

Set the value slightly higher than the expected maximum cluster size. For example, set it higher than`20000`for a cluster expected to contain up to 20,000 nodes.
`coresTotal`Y

Defines the minimum and maximum total number of CPU cores across the cluster.

This argument controls aggregate CPU-capacity scaling and helps prevent underprovisioning or overprovisioning.

If the maximum value is too low, the Cluster Autoscaler blocks scale-up operations.

If the maximum value is too high, excessive node provisioning can increase costs.

Set`coresTotal`based on your organization's planned maximum CPU capacity and cloud resource quotas. Ensure`coresTotal`is high enough to support peak workloads.
`memoryTotal`Y

Defines the minimum and maximum total memory across the cluster.

This argument controls total cluster memory provisioning and is particularly important for memory-intensive workloads.

If the maximum value is too low, the Cluster Autoscaler prevents scale-up operations, which can leave workloads without sufficient memory.

If the maximum value is too high, the cluster might be overprovisioned and costs might increase.

Align the minimum and maximum values with the node-pool sizing strategy.
`maxEmptyBulkDelete`Y

Defines the maximum number of empty nodes that can be deleted simultaneously.

This argument controls the speed of scale-down operations.

If the value is too low:
- Scale-down operations might be slow.
- Idle resources might remain in the cluster longer.

If the value is too high, a large number of nodes might be deleted at the same time.
- Increase the value moderately for large clusters.
- Avoid aggressive bulk deletion.
`nodes`Y

Defines the minimum and maximum number of nodes for each node pool.

This argument controls the scaling boundaries for each node pool.

If the boundaries are too restrictive, the node pool cannot scale sufficiently.

If the boundaries are too permissive, nodes might be distributed unevenly across node pools.
- Configure the boundaries for each node pool based on workload type and availability domain.
- Align the values with the`balanceSimilarNodeGroups`
