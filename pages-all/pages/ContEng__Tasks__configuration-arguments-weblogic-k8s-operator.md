# WebLogic Kubernetes Operator
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-weblogic-k8s-operator.htm
- Fetched: 2026-09-05 01:53 CDT

# WebLogic Kubernetes Operator

When you enable the WebLogic Kubernetes Operator cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-weblogic-k8s-operator.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-weblogic-k8s-operator.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`weblogic-operator.ContainerResources`weblogic-operator container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`weblogic-operator-webhook.ContainerResources`weblogic-operator-webhook container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-weblogic-k8s-operator.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`affinity`N

Controls pod-affinity rules for the operator deployment. Not applicable Not applicable Not applicable
`nodeSelectors`N

Controls the nodes on which the operator pods can run. Not applicable Not applicable Not applicable
`numOfReplicas`N

Controls the number of WebLogic Kubernetes Operator pods.

The number of cluster nodes does not directly affect the required number of replicas because the operator reconciles WebLogic resources rather than cluster nodes.

You might need more replicas if the number of WebLogic servers also increases.

If the count is low, a node failure, pod crash, or upgrade can temporarily stop reconciliation. This can delay WebLogic domain provisioning, scaling, rolling restarts, and status updates until a new operator instance becomes available.

Set`numOfReplicas`to`3`.
`rollingUpdate`N

Controls the update strategy for the operator deployment. Not applicable Not applicable Not applicable
`tolerations`N

Controls whether the operator pods can run on tainted nodes. Not applicable Not applicable Not applicable
`topologySpreadConstraints`N

Controls how operator pods are distributed across the cluster topology. Not applicable Not applicable Not applicable
`weblogic-operator.ContainerResources`Y

Defines CPU and memory requests and limits for the WebLogic Kubernetes Operator pod.

The number of cluster nodes does not directly affect resource requirements because the operator reconciles WebLogic resources in the WebLogic namespace.

If the number of WebLogic servers increases, the operator must observe and reconcile more server pods. This can result in:
- Higher CPU and memory usage
- Increased latency during scale-up and scale-down operations

If the resources are undersized:
- The operator pod might be terminated because it exceeds its memory limit.
- Reconciliation of the running server count with the expected state might be delayed.
- Pod churn might be processed more slowly, reducing responsiveness.
- A backlog of unschedulable pods might accumulate.

Increase CPU and memory resources as appropriate:
- Increase memory to handle a large number of WebLogic servers.
- Increase CPU to improve reconciliation performance.
`weblogic-operator-webhook.ContainerResources`Y

Defines CPU and memory requests and limits for the webhook container installed with the WebLogic Kubernetes Operator add-on.

The number of cluster nodes does not directly affect the webhook because it processes WebLogic resources rather than cluster nodes.

If the number of WebLogic servers and associated Domain operations increases, the webhook might need to process more requests.

If the resources are undersized:
- Webhook requests might be processed more slowly.
- Calls from the Kubernetes API server to the conversion webhook might have additional latency.
- Domain create and update operations that depend on webhook processing might be slower.
- Insufficient memory might cause memory pressure, container restarts, or out-of-memory terminations.
- Unstable webhook availability might cause webhook or conversion errors during Domain operations.
- Increase CPU when webhook requests are slow, Domain create or update operations have increased latency, or the webhook is CPU-throttled.
-
