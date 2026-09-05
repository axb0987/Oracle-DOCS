# kube-proxy
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-kube-proxy.htm
- Fetched: 2026-09-05 01:53 CDT

# kube-proxy

When you enable the kube-proxy cluster add-on, you can pass the following key/value pairs as arguments.

Note that for large clusters, we recommend that you review kube-proxy configuration before deploying the add-on:
- Review`kube-proxy.ContainerResources`. kube-proxy runs on every worker node, and resource requirements can increase as the number of Services, EndpointSlices, endpoint IPs, and update events increases. Increase CPU and memory requests and limits if kube-proxy pods show sustained CPU or memory pressure.
- Be careful when setting nodeSelectors, affinity, or tolerations. kube-proxy must run on every worker node that requires Kubernetes Service networking. Scheduling constraints that exclude nodes can leave those nodes without functional Service networking.
- Use`rollingUpdate`settings that allow kube-proxy updates to make progress across large numbers of nodes. Avoid settings that update too many nodes at once or prevent updates from rolling through the cluster.
- If you set`customizeKubeProxyConfigMap`to true, review kube-proxy sync settings for the cluster's Kubernetes version and proxy mode. The Kubernetes documentation notes that in iptables mode, very large clusters might need a larger`minSyncPeriod`if kube-proxy rule sync duration is much larger than one second (see[Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)in the Kubernetes documentation).
- If the cluster's Kubernetes version, operating system, and network plugin support nftables mode, evaluate whether nftables is appropriate for your workload. The Kubernetes documentation notes that nftables mode is designed to provide better performance and scalability than iptables mode, but also notes that it might not be compatible with all network plugins (see[Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/)in the Kubernetes documentation).

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-kube-proxy.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-kube-proxy.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`customizeKubeProxyConfigMap`customize kube-proxy configMap

If you want Oracle to manage Kube-proxy for you automatically, set`customizeKubeProxyConfigMap`to`false`(the default).

If you want to customize Kube-proxy behavior, set`customizeKubeProxyConfigMap`to`true`and create a kube-proxy configMap in the kube-system namespace. Required`false``true`
`kube-proxy.ContainerResources`kube-proxy container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`
