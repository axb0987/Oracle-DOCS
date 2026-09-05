# OCI Native Ingress Controller
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm
- Fetched: 2026-09-05 01:53 CDT

# OCI Native Ingress Controller

When you enable the OCI native ingress controller cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`authSecretName`authSecretName The name of the Kubernetes secret to use for user authentication when`authType`is set to`user`. Optional`""``oci-config`
`authType`authType The authentication type that the OCI native ingress controller uses while making requests, as one of:
- `instance`specifies instance principal (managed nodes only)
- `user`specifies user principal (managed and virtual nodes)
- `workloadIdentity`specifies workload identity (managed and virtual nodes) Optional`instance``workloadIdentity`
`certDeletionGracePeriodInDays`certDeletionGracePeriodInDays

The number of days that the OCI native ingress controller waits before deleting unused OCI Certificates service resources. Applies when the[OCI Native Ingress Controller obtains a certificate from the Certificates service using a Kubernetes secret](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_certificate_using_secret).

Must be an integer value. If the value is less than or equal to zero, the OCI native ingress controller does not delete unused OCI Certificates service resources. Optional`0``1`
`compartmentId`compartmentId The OCID of the compartment in which the OCI native ingress controller is to create the OCI load balancer (and certificate, if the`useLbCompartmentForCertificates`add-on argument is set to`false`). Required`""``ocid1.compartment.oc1..aaaaaaaa______ddq`
`controllerClass`controllerClass The name of the controller specified in your ingressClass that is to be managed by the oci-native-ingress-controller. Optional`oci.oraclecloud.com/native-ingress-controller``oci.oraclecloud.com/native-ingress-controller`
`emitEvents`emitEvents

Whether to emit Kubernetes events for Ingress and IngressClass errors observed during reconciliation.

If set to`true`, events are emitted. Optional`false``false`
`leaseLockName`leaseLockName The name of the lease to use for leader election. Optional`oci-native-ingress-controller``oci-native-ingress-controller`
`leaseLockNamespace`leaseLockNamespace The namespace of the lease. Optional`native-ingress-controller-system``native-ingress-controller-system`
`loadBalancerSubnetId`loadBalancerSubnetId The OCID of the load balancer's subnet. Required`""``ocid1.subnet.oc1.iad.aaaaaaaa______dba`
`logVerbosity`logVerbosity The number for the verbosity of logging. Optional`4``2`
`metricsBackend`metricsBackend The name of the metrics backend. Optional`prometheus``prometheus`
`metricsPort`metricsPort The metrics port. Optional`2223``2223`
`oci-native-ingress-controller.ContainerResources`native-ingress-controller container resources

You can specify the resource quantities that the add-on containers request, and set resource usage limits that the add-on containers cannot exceed.

JSON format in plain text or Base64 encoded. Optional null`{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`

Create add-on containers that request 100 milllicores of CPU, and 100 mebibytes of memory. Limit add-on containers to 500 milllicores of CPU, and 200 mebibytes of memory.
`useLbCompartmentForCertificates`useLbCompartmentForCertificates

Whether to use the compartment specified for the OCI load balancer (in the related IngressClassParameters resource) to manage OCI Certificates service resources when using a Kubernetes secret to obtain a certificate and a CA bundle. See[Option 1: OCI Native Ingress Controller obtains certificate from the Certificates service using a Kubernetes secret](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_certificate_using_secret).

If set to`false`, the compartment specified by the`compartmentId`add-on argument is used. Optional`false``false`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`affinity`N

Controls the placement of Native Ingress Controller pods based on pod-affinity and pod-anti-affinity rules. Not applicable Not applicable Not applicable
`nodeSelectors`N

Controls the placement of Native Ingress Controller pods based on node labels. Not applicable Not applicable Not applicable
`numOfReplicas`N

Controls the number of replicas in the Native Ingress Controller deployment. Not applicable Not applicable Not applicable
`rollingUpdate`N

Controls the deployment update strategy, including settings such as`maxSurge`and`maxUnavailable`. Not applicable Not applicable Not applicable
`tolerations`N

Controls whether Native Ingress Controller pods can run on tainted nodes. Not applicable Not applicable Not applicable
`topologySpreadConstraints`N

Controls how matching Native Ingress Controller pods are distributed across the cluster topology by using settings such as`maxSkew`and`minDomains`. Not applicable Not applicable Not applicable
`oci-native-ingress-controller.ContainerResources`Y

Defines CPU and memory requests and limits for the Native Ingress Controller pod.

The controller examines nodes to identify available load balancer backends. CPU and memory usage therefore increase as the number of nodes increases.

When`externalTrafficPolicy`is set to`Cluster`, the node informer cache can contain backend information for every node. In a cluster with approximately 20,000 nodes, processing backend information during each synchronization cycle can become a resource bottleneck.

When`externalTrafficPolicy`is set to`Local`, the backend synchronization volume is substantially lower because only nodes with local backends are included.
- Backend reconciliation can cause significant CPU and memory pressure.
- Synchronization cycles might become slow when the controller processes backend information across thousands of nodes.
- If a backend request exceeds the load balancer limit of 512 backends, the load balancer control plane rejects the update.
- Repeatedly rejected updates can leave stale backends configured on the load balancer.

High cpu and limit is expected with`externalTrafficPolicy`set to`Cluster`. Moderate required if`externalTrafficPolicy`is set to`Local`. With`Local`external traffic policy health checks are constrained to nodes or pods with local backends, up to the load balancer backend limit.
`routingStrategies.hostBasedRouting`N

Routes requests to a service based on the domain name in the request. Not applicable Not applicable Not applicable
`routingStrategies.pathBasedRouting`N

Routes requests to a service based on the request path or API endpoint. Not applicable Not applicable Not applicable
`routingStrategies.defaultRouting`N

Routes requests that do not match another rule to the default backend service. Not applicable Not applicable Not applicable
`NIC annotations`Y

Configure Native Ingress Controller and load balancer behavior, including backend health-check settings.

Load balancer routing performance remains constrained by the maximum of 512 backends rather than by the total number of cluster nodes.

However, the selected external traffic policy affects controller resource usage:
- With`externalTrafficPolicy: Cluster`, health checks can fan out across all cluster nodes, creating significant overhead in a cluster with approximately 20,000 nodes.
- With`externalTrafficPolicy: Local`, health checks are constrained to nodes or pods with local backends, up to the load balancer backend limit.
- Cluster-wide health-check fan-out can substantially increase CPU and memory usage.
- Updating health-check configuration can cause the controller to reevaluate backend pods across the cluster.
- CPU and memory contention can occur even when`externalTrafficPolicy`is set to`Local`.
