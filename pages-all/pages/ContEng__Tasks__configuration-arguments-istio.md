# Istio
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-istio.htm
- Fetched: 2026-09-05 01:53 CDT

# Istio

When you enable the Istio cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-istio.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-istio.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`customizeConfigMap`customizeConfigMap

If you want Oracle to manage Istio for you automatically, set`customizeConfigMap`to`false`(the default).

If you want to customize Istio using istioctl (or another tool supported by Istio) and you want to retain the customizations when Oracle updates the add-on, set`customizeConfigMap`to`true`. Required`false``true`
`discovery.ContainerResources`discovery.ContainerResources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`discovery.EnvVariables`discovery.EnvVariables

List of Istio control plane discovery container environment variables, in JSON format. Optional null`[{"name":"ISTIO_GPRC_MAXRECVMSGSIZE","value":"8388608"},{"name":"ISTIO_GPRC_MAXSTREAMS","value":"150000"}]`
`enableIngressGateway`enableIngressGateway Enable Istio ingress gateway Required`false``true`
`istio-ingressgateway.Annotations`istio-ingressgateway.Annotations

Annotations to pass to the Istio deployment.

For example, to specify the load balancer shape, or whether to create the load balancer as a network load balancer. For more annotations, see[Summary of Annotations for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer_topic-Summaryofannotations.htm).

JSON format in plain text or Base64 encoded. Optional`""`

`{"service.beta.kubernetes.io/oci-load-balancer-shape":"400Mbps"}`

`{"oci.oraclecloud.com/load-balancer-type": "nlb"}`
`istio-ingressgateway.HorizontalPodAutoscalerMinReplicas`istio-ingressgateway.HorizontalPodAutoscalerMinReplicas

Minimum number of replicas of the Istio ingress gateway horizontal pod autoscaler.

Must be an integer, with a value greater than zero. Optional null`1`
`istio-ingressgateway.HorizontalPodAutoscalerMaxReplicas`istio-ingressgateway.HorizontalPodAutoscalerMaxReplicas

Maximum number of replicas of the Istio ingress gateway horizontal pod autoscaler.

Must be an integer, with a value greater than zero. Optional null`3`
`istio-ingressgateway.PodDisruptionBudgetMinAvailable`istio-ingressgateway.PodDisruptionBudgetMinAvailable

Minimum number or percentage of Istio ingress gateway pods available. Optional null

`1`

`10%`
`istiod.HorizontalPodAutoscalerMinReplicas`istiod.HorizontalPodAutoscalerMinReplicas

Minimum number of replicas of the Istio controller.

Must be an integer, with a value greater than zero. Optional null`1`
`istiod.HorizontalPodAutoscalerMaxReplicas`istiod.HorizontalPodAutoscalerMaxReplicas

Maximum number of replicas of the Istio controller.

Must be an integer, with a value greater than zero. Optional null`3`
`istiod.PodDisruptionBudgetMinAvailable`istiod.PodDisruptionBudgetMinAvailable

Minimum number or percentage of Istio controller pods available. Optional null

`1`

`10%`
`profile`profile Istio installation profile Required`"oke-default"``"oke-default"`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-istio.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`affinity`N

Controls the placement of Istio pods on particular nodes. Not applicable Not applicable Not applicable
`nodeSelectors`N

Controls whether Istio pods run on nodes with particular labels. Not applicable Not applicable Not applicable
`tolerations`N

Controls whether Istio pods can run on tainted nodes. Not applicable Not applicable Not applicable
`topologySpreadConstraints`Y

Controls how matching Istio pods are distributed across the cluster topology.

You might need to adjust the topology spread constraints when the number of`istiod`replicas increases.

If not configured well, istiod or gateway replicas can end up co-located on the same node or in the same zone, so a node/zone failure takes out multiple replicas at once.

Configure`topologySpreadConstraints`to distribute istiod and ingress gateway replicas across different nodes and availability zones, improving resilience against node and zone failures.
`numOfReplicas`Y

Controls the number of Istio control-plane replicas.

More replicas might be required as the number of pods participating in the service mesh increases.

If set too low, istiod has a higher chance of becoming a single point of failure during node drains or upgrades.

Increase the number of replicas as the number of meshed pods increases.
`rollingUpdate`N

Controls the update strategy for the Istio deployment. Not applicable Not applicable Not applicable
`customizeConfigMap`N

Controls operator-level Istio configuration. Not applicable Not applicable Not applicable
`discovery.ContainerResources`Y

Defines CPU and memory resources for the`istiod`discovery container.

CPU and memory requirements can increase as the number of meshed proxies and the amount of Istio configuration increase.

If undersized, the Istio control plane can be CPU- or memory-starved, which risks slower config propagation, delayed sidecar updates, and instability under high mesh churn. Allocate sufficient CPU and memory for istiod based on mesh size and traffic, and monitor resource utilization regularly to prevent control-plane bottlenecks as the cluster grows.
`discovery.EnvVariables`N

Defines environment variables for the Istio control-plane discovery container. Not applicable Not applicable Not applicable
`enableIngressGateway`N

Controls whether the classic Istio ingress gateway is enabled. Not applicable Not applicable

Enable the ingress gateway only when the cluster requires the classic Istio ingress gateway.
`istio-ingressgateway.Annotations`Y

Defines annotations for the Istio ingress gateway, including annotations that control the load balancer type and shape.

The required load balancer configuration depends on the amount of traffic that the ingress gateway receives or is expected to receive, rather than directly on the number of cluster nodes.

If misconfigured, the ingress gateway can be provisioned with the wrong load balancer shape or type (for example, wrong OCI LB shape or NLB setting). This can lead to incorrect exposure, throughput limits, or traffic-routing issues. Configure OCI load balancer annotations to match your production traffic requirements and networking architecture, ensuring optimal load balancing, scalability, and high availability.
`istio-ingressgateway.HorizontalPodAutoscalerMinReplicas`Y

Defines the minimum number of Istio ingress gateway replicas maintained by the Horizontal Pod Autoscaler.

More ingress gateway replicas might be required as traffic increases.

If too low, the ingress gateway has less baseline capacity and is more likely to become a traffic bottleneck during spikes. If it is 1, there is also less resilience during disruptions.

Increase the minimum number of replicas as traffic increases to maintain availability and fault tolerance.
`istio-ingressgateway.HorizontalPodAutoscalerMaxReplicas`Y

Defines the maximum number of Istio ingress gateway replicas that the Horizontal Pod Autoscaler can create.

The ingress gateway might need to scale to more replicas as traffic increases.

If too low, the ingress gateway cannot scale enough during traffic surges, which can create latency or dropped connections.

Increase the maximum number of replicas as traffic increases to maintain availability and fault tolerance.
`istio-ingressgateway.PodDisruptionBudgetMinAvailable`Y

Defines the minimum number or percentage of Istio ingress gateway pods that must remain available during a voluntary disruption.

A higher minimum availability value might be required as ingress traffic increases.

If too low, upgrades or node drains can remove too many gateways at once and create an ingress outage.

Increase the minimum availability value as traffic increases to maintain high availability.
`istiod.HorizontalPodAutoscalerMinReplicas`Y

Defines the minimum number of`istiod`replicas maintained by the Horizontal Pod Autoscaler.

More`istiod`replicas might be required as the size of the service mesh increases.

If too low, the control plane starts from too little capacity and is more likely to fall behind during config bursts.

Increase the minimum number of replicas as the mesh size increases. Use at least three replicas to maintain availability.
`istiod.HorizontalPodAutoscalerMaxReplicas`Y

Defines the maximum number of`istiod`replicas that the Horizontal Pod Autoscaler can create.

More`istiod`replicas might be required when existing replicas reach or exceed their resource limits.

If too low, istiod cannot scale enough to handle mesh growth, config churn, or a large number of sidecars.

Increase the maximum number of replicas when`istiod`pods consistently approach or exceed their resource limits.
`istiod.PodDisruptionBudgetMinAvailable`Y

Defines the minimum number or percentage of`istiod`pods that must remain available during a voluntary disruption.

Maintaining available`istiod`replicas becomes increasingly important when the control plane manages a large service mesh.

If too low, a drain or upgrade can leave the control plane unavailable and sidecar injection can fail cluster-wide.

Configure the value so that some`istiod`pods remain available during restarts and configuration updates.
`profile`N
