# Certificate Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-certificate-manager.htm
- Fetched: 2026-09-05 01:53 CDT

# Certificate Manager

When you enable the Certificate Manager cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-certificate-manager.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-certificate-manager.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`cert-manager-cainjector.ContainerResources`cert-manager-cainjector container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`cert-manager-controller.ContainerResources`cert-manager-controller container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`cert-manager-webhook.ContainerResources`cert-manager-webhook container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-certificate-manager.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`cert-manager-cainjector.ContainerResources`Y

Defines CPU and memory resources for the CA Injector.

The CA Injector adds CA data to webhooks, custom resource definitions, and API services.

As the cluster size increases:
- The number of custom resource definitions and webhook configurations can increase.
- The number of patch and update operations can increase.
- API server interactions increase.

The workload grows moderately and is generally lower than the workload of the Certificate Manager controller.

If the resources are undersized:
- CA bundle injection might be delayed.
- Webhooks might fail because CA data is missing.

Increase resources moderately as the cluster size increases. The CA Injector typically requires less aggressive resource scaling than the Certificate Manager controller.
`numOfReplicas`N

Controls the number of replicas for Certificate Manager components.

Additional replicas improve availability and fault tolerance.

The webhook can scale horizontally to handle a higher volume of admission requests.
- Controller throughput does not increase linearly with the number of replicas.
- Some components use leader election, so only the active leader performs certain operations.
- Use at least two or three replicas.
- Increase the number of webhook replicas when API request volume is high.
`affinity`/`nodeSelectors`/`tolerations`N

Control the placement of Certificate Manager components.

Certificate Manager is a control-plane-critical component and can be affected by node churn and resource contention.

If these arguments are not configured appropriately:
- Pods might run on unstable or overloaded nodes.
- Components might restart.
- Certificate operations might be delayed.
- Run Certificate Manager components on stable nodes or dedicated infrastructure or system node pools.
- Configure tolerations when the target nodes are tainted.
`rollingUpdate`N

Controls the deployment update strategy.

During an upgrade:
- Controller downtime stops certificate reconciliation.
- Webhook downtime can cause API requests to fail.
- All replicas might restart at the same time.
- Certificate operations might be temporarily paused.
- Set`maxUnavailable`to`0`or to the lowest practical value.
- Maintain continuous component availability during updates.
`topologySpreadConstraints`N

Controls how pods are distributed across nodes and availability domains.
- Prevents all replicas from running on the same node or in the same availability domain.
- Improves resilience to node and availability-domain failures.

If topology spread constraints are not configured:
- All pods might run on the same node or in the same availability domain.
- A single failure might make the webhook or controller unavailable.

Distribute replicas across different nodes and availability domains.
`cert-manager-controller.ContainerResources`Y

Defines CPU and memory resources for the Certificate Manager controller pod.

As the cluster size increases, the number of the following resources can increase:
- Certificates
- Certificate requests
- Secrets

The controller experiences:
- A larger informer cache
- More watch events
- More frequent reconciliation
- More API server interactions

If the resources are undersized:
- The controller might be terminated because it exceeds its memory limit.
- Certificate reconciliation might be slow.
- Certificate issuance and renewal might be delayed.
- An event-queue backlog might develop.
- Increase memory to support the larger informer cache.
- Increase CPU to support additional reconciliation activity.

This is the most important Certificate Manager resource-scaling argument.
`cert-manager-webhook.ContainerResources`Y

Defines CPU and memory resources for the Certificate Manager webhook.

The webhook validates and modifies Certificate Manager resources.

As the cluster size increases:
- The number of API requests can increase.
- The number of admission webhook calls can increase.
- The request load on this latency-sensitive component increases.

If the resources are undersized:
- Admission request latency might increase.
- Kubernetes API server operations might slow down.
- Resource creation might fail.
- Allocate sufficient CPU for request processing.
-
