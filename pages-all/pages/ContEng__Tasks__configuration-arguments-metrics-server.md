# Kubernetes Metrics Server
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm
- Fetched: 2026-09-05 01:53 CDT

# Kubernetes Metrics Server

When you enable the Kubernetes Metrics Server cluster add-on, you can pass the following key/value pairs as arguments

Note that to use the Kubernetes Metrics Server as a cluster add-on, you also have to deploy cert-manager (either as a standalone product, or as a cluster add-on). If you deploy cert-manager as a standalone product, set the`skipAddonDependenciesCheck`configuration argument to`true`.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`metrics-server.ContainerResources`metrics-server container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`skipAddonDependenciesCheck`skipAddonDependenciesCheck Whether to check that other required add-ons have been deployed (such as the cert-manager add-on). Optional null`true`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`metrics-server.ContainerResources`Y

Defines CPU and memory requests and limits for the Metrics Server pod.
- Scrape operations increase linearly because Metrics Server collects metrics from every node.
- CPU usage increases for metric collection and processing.
- Memory usage increases for holding aggregated metrics.
- Metrics might take longer to become available.

If the resources are undersized:
- The Metrics Server pod might be terminated because it exceeds its memory limit.
- CPU throttling might cause slow or missed scrapes.
- The Metrics API might provide stale data or become unavailable.
- Horizontal Pod Autoscaler decisions might be delayed or inaccurate.
- Increase CPU and memory resources in proportion to the number of nodes.
- Increase CPU to support scraping and metric processing.
- Increase memory to support metric aggregation.
- Validate resource sizing through load testing for clusters with more than 5,000 nodes.
`numOfReplicas`N

Controls the number of Metrics Server pods.

Each replica scrapes every node. Metrics Server does not divide the scraping workload between replicas, so additional replicas provide high availability rather than additional processing capacity.
- Additional replicas generate duplicate scrape traffic.
- Increasing the number of replicas does not improve scraping throughput.
- Use two or three replicas to provide high availability.
- Do not increase the number of replicas to improve performance.
`affinity`/`nodeSelectors`/`tolerations`N

Control the placement of Metrics Server pods.

Metrics Server is a control-plane-critical component. Its placement affects service stability and the availability of resource metrics.

If these arguments are not configured appropriately:
- Pods might run on unstable or resource-constrained nodes.
- Pods might restart.
- Performance might be reduced.
- Intermittent gaps might occur in metric availability.
- Run Metrics Server on stable nodes with low churn and sufficient resources.
- Prefer dedicated infrastructure or system node pools.
- Configure tolerations when the target nodes are tainted.
`rollingUpdate`N

Controls the deployment update strategy for Metrics Server.

Metrics Server downtime makes the Metrics API unavailable, prevents the Horizontal Pod Autoscaler from operating correctly, and causes`kubectl top`commands to fail.

If this argument is not configured appropriately:
- All replicas might restart at the same time.
- The metrics pipeline might become temporarily unavailable.
- Configure`maxUnavailable`carefully.
- Ensure that at least one Metrics Server replica remains active during an update.
- Use a gradual rollout strategy.
`topologySpreadConstraints`N

Controls how Metrics Server pods are distributed across nodes, availability domains, and other failure domains.
- Prevents all replicas from running on the same node or in the same availability domain.
- Improves resilience to node and availability-domain failures.
- Adds a small amount of scheduling complexity.

If topology spread constraints are not configured:
- All replicas might run on the same node or in the same availability domain.
- A single failure might cause a complete metrics outage.
- Distribute replicas across availability domains where possible.
- Run replicas on different nodes.
- Maintain an even distribution to provide high availability.
`skipAddonDependenciesCheck`N

Controls whether dependency validation is skipped during installation of the add-on.

This argument has no direct performance or scalability impact, but it affects deployment reliability. In OKE, Metrics Server depends on components such as Certificate Manager.

If dependency validation is skipped:
- The add-on might be installed without required dependencies.
- The metrics pipeline might not function.
- Runtime failures might occur.
- Troubleshooting might be more difficult in a large cluster.
- Keep dependency validation enabled.
-
