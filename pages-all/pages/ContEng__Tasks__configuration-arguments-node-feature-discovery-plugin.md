# Node Feature Discovery
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-node-feature-discovery-plugin.htm
- Fetched: 2026-09-05 01:53 CDT

# Node Feature Discovery

When you enable the Node Feature Discovery cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-node-feature-discovery-plugin.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-node-feature-discovery-plugin.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`master.tolerations`tolerations for nfd master Custom tolerations to apply to NFD master pods. Optional
```

```

`master.affinity`affinity for nfd master Node affinity rules for scheduling NFD pods. Optional
```

```

`master.config`config for nfd master

Additional master configuration to merge into`nfd-master.conf`.

YAML or JSON format in plain text. Optional`null`
`master.resources`resources for nfd master Resource requests and limits for the NFD master container. JSON format in plain text. Optional`null`
`master.replicaCount`replicaCount for nfd master Replica count for the NFD master deployment. Optional`null`
`master.extraArgs`extraArgs for nfd master

Additional command-line arguments for the NFD master container.

JSON array format in plain text. Optional`null`
`master.annotations`annotations for nfd master pods Annotations to merge into the NFD master pod template. Optional`null`
`priorityClassName`priorityClassName for nfd deployments PriorityClassName for the NFD master and gc deployments. Optional`null`
`worker.config`config for nfd worker

Additional worker configuration to merge into`nfd-worker.conf`.

YAML or JSON format in plain text. Optional`null`
`worker.resources`resources for nfd worker Resource requests and limits for the NFD worker container. JSON format in plain text. Optional`null`
`worker.tolerations`tolerations for nfd worker Additional tolerations to append to the NFD worker pods. Optional`null`
`worker.nodeSelector`nodeSelector for nfd worker Node selector labels to merge into the NFD worker DaemonSet. Optional`null`
`worker.priorityClassName`priorityClassName for nfd worker PriorityClassName for the NFD worker DaemonSet. Optional`null`
`worker.extraArgs`extraArgs for nfd worker

Additional command-line arguments for the NFD worker container.

JSON array format in plain text. Optional`null`
`worker.annotations`annotations for nfd worker pods Annotations to merge into the NFD worker pod template. Optional`null`
`master.customConfigData`Custom NFD master configuration data

Provide content for the`node-feature-discovery-master-custom-conf`ConfigMap.

If provided, it will be mounted automatically. Optional`""`
`worker.customConfigData`Custom NFD worker configuration data

Provide content for the`node-feature-discovery-worker-custom-conf`ConfigMap.

If provided, it will be mounted automatically. Optional`""`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-node-feature-discovery-plugin.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`master.tolerations`Y

Controls whether Node Feature Discovery master pods can run on tainted control-plane or infrastructure nodes.
- Ensures that the Node Feature Discovery master runs on stable control-plane or infrastructure nodes.
- Prevents the master from running on worker nodes with high workload activity.
- Improves the reliability of node labeling across the cluster.

If this argument is misconfigured:
- The master pod might remain in the`Pending`state because it cannot tolerate the node taints.
- The master pod might run on worker nodes and become unstable.
- Label updates across the cluster might be delayed or inconsistent.
- Always include tolerations for control-plane taints.
- Ensure that the master runs on stable nodes.
- Combine tolerations with affinity rules to control pod placement.
`master.affinity`Y

Defines preferred node placement for Node Feature Discovery master pods.
- Keeps the master on dedicated control-plane or infrastructure nodes.
- Reduces interference from application workloads.
- Improves the consistency of node-labeling operations.

If this argument is misconfigured:
- The master might run on worker nodes.
- Multiple replicas might run on the same node, reducing high availability.
- Node labeling might be slower or inconsistent.
- Use affinity rules to prefer control-plane or infrastructure nodes.
- Add anti-affinity rules when using multiple replicas.
- Treat master placement as part of the cluster control-plane design.
`master.customConfigData`N

Enables custom configuration for the Node Feature Discovery master.

The configuration controls how node features are processed and labeled. It affects:
- The number of labels generated
- The frequency of label updates

If this argument is misconfigured:
- Excessive or incorrect labels might be generated.
- Frequent label changes might increase the load on the Kubernetes API server.
- Feature detection might be inconsistent across nodes.
- Keep the configuration minimal.
- Configure only the required features.
- Validate the configuration on a small subset of nodes before applying it throughout the cluster.
`worker.customConfigData`N

Controls custom feature-detection logic on each node.

The Node Feature Discovery worker runs on every node as a DaemonSet. Any additional detection logic therefore runs on every node.

Custom detection logic can affect:
- Node CPU usage
- Labeling frequency
- Cluster-wide labeling consistency

If this argument is misconfigured:
- CPU usage might increase on nodes.
- Labels might be incorrect or inconsistent.
- Frequent label updates might increase pressure on the Kubernetes API server.
- Workload scheduling might be affected.
- Keep the worker configuration lightweight.
- Avoid resource-intensive detection logic.
- Validate labels before enabling the configuration throughout the cluster.
-
