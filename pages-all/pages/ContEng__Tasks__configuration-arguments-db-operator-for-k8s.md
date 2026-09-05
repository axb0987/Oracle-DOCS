# Oracle Database Operator for Kubernetes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-db-operator-for-k8s.htm
- Fetched: 2026-09-05 01:53 CDT

# Oracle Database Operator for Kubernetes

When you enable the Oracle Database Operator for Kubernetes cluster add-on, you can pass the following key/value pairs as arguments.

Note that to use the Oracle Database Operator as a cluster add-on, you also have to deploy cert-manager (either as a standalone product, or as a cluster add-on). If you deploy cert-manager as a standalone product, set the`skipAddonDependenciesCheck`configuration argument to`true`.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-db-operator-for-k8s.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-db-operator-for-k8s.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`manager.ContainerResources`manager container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`skipAddonDependenciesCheck`skipAddonDependenciesCheck Whether to check that other required add-ons have been deployed (such as the cert-manager add-on). Optional null`true`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-db-operator-for-k8s.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`manager.ContainerResources`Y

Defines the CPU and memory requests and limits for the operator pods.

As the cluster size increases, the operator experiences:
- Significant growth in the informer cache
- More watch streams
- A larger memory footprint
- More reconciliation activity

If the resources are undersized:
- Operator pods might be terminated because they exceed their memory limits.
- Reconciliation latency might increase.
- An event-queue backlog might delay processing.

Allocate sufficient memory and CPU to handle the additional load in large clusters. Give particular attention to memory sizing because the informer cache grows as the cluster size increases.
`numOfReplicas`N

Controls the number of operator pods deployed.

Additional replicas improve fault tolerance and failover through leader election.

Only one pod acts as the active leader for a controller. Other replicas remain on standby and take over only if the leader fails.

Increasing the number of replicas does not provide linear scaling of reconciliation throughput because the standby replicas do not process reconciliation loops for the same controller.

A low replica count increases the risk of operator downtime and slower recovery after failures.

Use a moderate number of replicas, such as three to five, to provide high availability. Do not increase the number of replicas to improve reconciliation performance.
`affinity`/`nodeSelectors`/`tolerations`N

Control where the operator pods are scheduled in the cluster.

Appropriate pod placement:
- Reduces interference from resource-intensive workloads.
- Keeps the operator on stable nodes with less churn and fewer disruptions.
- Allows the operator to run on dedicated or high-memory nodes that are suitable for control-plane add-ons. If not set correctly, the Oracle Database Operator may land on the wrong nodes or fail to schedule at all, which can lead to delayed reconciliation, and unstable performance.

Use these arguments to schedule operator pods on dedicated infrastructure nodes. Apply pod anti-affinity rules where necessary to improve resilience.
`rollingUpdate`N

Controls the deployment update strategy for the operator.

During upgrades in large clusters, the rolling update strategy:
- Prevents operator downtime.
- Maintains the availability of at least some replicas.
- Prevents all replicas from being terminated at the same time.

If not configured well, an upgrade can briefly take down too many Oracle Database Operator pods at once, causing reconciliation delays, and loss of failover safety.

Configure rolling update settings, such as`maxUnavailable`and`maxSurge`, to allow upgrades to complete without interrupting cluster operations.
`topologySpreadConstraints`N

Controls how operator replicas are distributed across nodes and availability domains.

Distributing replicas prevents all operator pods from running on the same node or in the same availability domain and reduces the effect of node or availability-domain failures.

If not configured correctly, operator pods may be scheduled on the same node or in the same availability zone, increasing the risk of losing multiple replicas during a node or zone failure.
