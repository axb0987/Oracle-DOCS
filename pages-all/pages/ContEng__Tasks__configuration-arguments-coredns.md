# CoreDNS
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-coredns.htm
- Fetched: 2026-09-05 01:53 CDT

# CoreDNS

When you enable the CoreDNS cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-coredns.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-coredns.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`coreDnsContainerResources`CoreDNS container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`coreDnsEnhancedMetrics`CoreDNS enhanced metrics

The granularity of CoreDNS metrics to generate.

If you want CoreDNS to generate default metrics, set`coreDnsEnhancedMetrics`to`false`. If you want CoreDNS to generate more granular metrics for Kubernetes and OCI internal network traffic, set`coreDnsEnhancedMetrics`to`true`.

Note that the default value of`coreDnsEnhancedMetrics`depends on the version of Kubernetes that the cluster is running. Optional`true`for clusters running Kubernetes version 1.34.1 and later.

`false`for clusters running Kubernetes version 1.34.0 and earlier.`true`
`customizeCoreDNSConfigMap`customize CoreDNS configMap

If you want Oracle to manage CoreDNS for you automatically, set`customizeCoreDNSConfigMap`to`false`(the default).

If you want to customize CoreDNS behavior, set`customizeCoreDNSConfigMap`to`true`and create a coredns configMap in the kube-system namespace. Required`false``true`
`minReplica`min replica

The minimum number of replicas of the CoreDNS deployment. Required`1`

Creates a total of one pod in the cluster.`2`

Creates a total of two pods in the cluster.
`nodesPerReplica`nodes per replica

The number of CoreDNS replicas per cluster node. Required`1`

Creates a replica on every node.`2`
