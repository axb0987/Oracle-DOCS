# NVIDIA Network Operator
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-network-operator.htm
- Fetched: 2026-09-05 01:53 CDT

# NVIDIA Network Operator

When you enable the NVIDIA Network Operator cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-network-operator.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-network-operator.htm#)

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`operator.nodeSelectors`nvidia-network-operator nodeSelectors Node selectors on the NVIDIA Network Operator pods. Optional`null`
`operator.tolerations`nvidia-network-operator tolerations Tolerations on the NVIDIA Network Operator pods. Optional`null`
`nicClusterPolicy.tolerations`nicClusterPolicy tolerations Tolerations for DaemonSets managed by NicClusterPolicy. Optional`null`
`nicClusterPolicy.deploymentTolerations`nicClusterPolicy deploymentTolerations Tolerations for Deployments managed by NicClusterPolicy. Optional`null`
`operator.affinity`nvidia-network-operator affinity Affinity scheduling rules for NVIDIA Network Operator. JSON format in plain text. Optional`null`
`operator.resources`nvidia-network-operator container resources NVIDIA Network Operator resources control the resource limits and requests for the`nvidia-network-operator`container. JSON format in plain text. Optional
```

```

`operator.cniBinDirectory`cniBinDirectory CNI binary directory for NVIDIA Network Operator. Optional`/opt/cni/bin`
`operator.cniNetworkDirectory`cniNetworkDirectory CNI network directory for NVIDIA Network Operator. Optional`/etc/cni/net.d`
`operator.admissionControllers.enabled`operator.admissionControllers.enabled Enable admission controllers for NVIDIA Network Operator. Optional`false`
`sriovNetworkOperator.enabled`sriovNetworkOperator.enabled Enable the SR-IOV NVIDIA Network Operator. Optional`false`
`sriov-network-operator.operator.resourcePrefix`sriov-network-operator.operator.resourcePrefix Resource prefix for resources created by SR-IOV Network Operator. Optional`nvidia.com`
`sriov-network-operator.operator.admissionControllers.enabled`sriov-network-operator.operator.admissionControllers.enabled Enable admission controllers for SR-IOV Network Operator. Optional`false`
`sriov-network-operator.operator.sriovOperatorConfig.configDaemonNodeSelectors`sriov-network-operator.operator.sriovOperatorConfig.configDaemonNodeSelectors Configure`configDaemonNodeSelector`for`sriovOperatorConfig`. Optional
```

```

`vfCreationMode`vfCreationMode Mode for VF creation. Valid values are`sriovNetworkOperator`and`custom`. Optional`custom`
`customizeVfCreationConfigMap`customizeVfCreationConfigMap Specify whether to skip creating the`vf-shape-config`ConfigMap. Optional`false`
`skipNodeFeatureDiscoveryDependencyCheck`skipNFDDependencyCheck Skip the Node Feature Discovery dependency check. Optional`false`

[Large Cluster Considerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-network-operator.htm#)

The following table describes considerations for configuring this cluster add-on in large clusters.

Argument Name Roles wrt number of Nodes Description As cluster size increases Risks Recommendation
`operator.nodeSelectors`Y

Controls where the NVIDIA Network Operator pods are scheduled.
- Keeps the operator on stable infrastructure or control-plane nodes.
- Prevents the operator from competing with workloads on busy worker nodes.
- Helps keep the networking control loop predictable when the cluster has many nodes and frequent node-state changes.

If this argument is misconfigured:
- The operator might run on overloaded worker nodes.
- The operator pod might remain in the`Pending`state if the selector is too restrictive or incorrect.
- Network-related reconciliation might become slow or inconsistent if the operator is unstable.
- Schedule the operator on dedicated infrastructure nodes.
- Use a simple and reliable selector.
- Keep the operator away from worker pools with frequent workload changes.
`operator.tolerations`Y

Controls tolerations for the NVIDIA Network Operator pods and related DaemonSets.
- Allows the operator and its DaemonSets to run on tainted infrastructure nodes.
- Prevents placement failures on control-plane or dedicated network nodes.
- Supports isolation when GPU or network nodes are tainted.

If this argument is misconfigured:
- The operator or its DaemonSets might remain in the`Pending`state on tainted nodes.
- SR-IOV, driver, or CNI components might not run on the required nodes.
- Some nodes might never receive the required networking features.
- Match tolerations to the taints used in the node pools.
- Use consistent tolerations across operator-managed DaemonSets.
- Retest the configuration after changing node-taint policies.
`operator.affinity`Y

Controls node-affinity rules for the NVIDIA Network Operator pods.
- Keeps the operator on the appropriate class of nodes.
- Reduces the likelihood that the operator is affected by worker-node churn.
- Allows the operator to run close to stable networking infrastructure.

If this argument is misconfigured:
- The operator might be scheduled on inappropriate nodes.
- If the rule is too restrictive, the operator might remain in the`Pending`state.
- If the rule is too broad, the placement might not provide the intended resilience.
- Use affinity rules to prefer stable nodes.
- Keep the rules simple unless multi-zone or multi-pool constraints are required.
- Combine affinity rules with tolerations when required.
`operator.resources`Y

Defines CPU and memory requests and limits for the NVIDIA Network Operator container.

The operator coordinates networking resources across the cluster. As the number of nodes increases, it must process more objects, node-state changes, and reconciliation operations.

The operator also relies on Node Feature Discovery labels to determine which nodes require networking components.

If the resources are undersized:
- Reconciliation might be slow.
- Networking software rollouts might be delayed.
- The operator might become unstable during frequent node changes or configuration updates.
- Increase CPU and memory resources for clusters with frequent node changes or many networking custom resources.
- Monitor operator CPU usage, memory usage, and reconciliation latency.
- Treat this argument as a control-plane sizing setting.
`operator.cniBinDirectory`N

Controls the directory on nodes where CNI binaries are deployed.

The CNI binaries must be deployed to the directory used by the container runtime. An incorrect path can affect many nodes at the same time.

If this argument is misconfigured:
- Pods might be created, but networking might not become available.
- CNI binaries might be deployed to the wrong host path.
- The cluster might appear configured even though networking is not working.
- Keep the value aligned with the node runtime default.
- Change the value only when the container runtime uses a different CNI binary directory.
- Validate the path on a single node pool before applying it broadly.
`operator.cniNetworkDirectory`N

Controls the host directory where CNI configuration files are deployed.

The CNI configuration files must be placed in the directory read by the kubelet or container runtime. An incorrect directory can affect every node that uses the configuration.

If this argument is misconfigured:
- CNI configuration files might be deployed to a directory that the kubelet or container runtime does not read.
- Nodes might appear configured even though secondary networking does not work.
- Troubleshooting might be difficult because the operator can appear healthy despite the path mismatch.
- Align the value with the CNI configuration directory used by the node runtime.
- Treat the argument as a host-runtime setting rather than a cluster policy setting.
- Validate file placement on a single GPU or network node before applying it broadly.
`operator.admissionControllers.enabled`N

Controls whether the NVIDIA Network Operator deploys its admission controller.

The admission controller helps prevent invalid configuration from entering the cluster. This becomes more important when many users or automation systems create networking custom resources.

If the admission controller is disabled:
- Invalid SR-IOV, network-policy, or NIC configuration might be accepted.
- Invalid settings might be applied to many nodes before the problem is detected.
- Operational risk increases in large clusters.
- Enable the admission controller in production environments.
- Ensure that Certificate Manager remains healthy if the webhook uses generated certificates.
`sriovNetworkOperator.enabled`N

Controls whether the SR-IOV Network Operator is deployed.

The SR-IOV Network Operator provides the SR-IOV components required for virtual-function-based, high-performance networking, including some RDMA and GPUDirect RDMA configurations.

If the SR-IOV Network Operator is disabled when required:
- SR-IOV capabilities are not deployed.
- Nodes might not provide the networking resources required by workloads.
- GPU and RDMA networking paths might remain incomplete.
- Enable the SR-IOV Network Operator only when the cluster requires SR-IOV.
- Leave it disabled in clusters that do not use virtual-function-based networking.
- When enabled, treat it as a foundational networking component.
`sriov-network-operator.operator.resourcePrefix`N

Sets the prefix used for resources created by the SR-IOV Network Operator.

The prefix determines the extended resource names that Kubernetes and workloads use. Changing the prefix requires all workload manifests to use the new resource names.

If this argument is misconfigured:
- Workloads might request an incorrect extended resource name.
- Pods might remain in the`Pending`state because the scheduler cannot match the requested resource.
- Old and new resource-naming conventions might be used inconsistently.
- Keep the default value unless an alternative naming policy is required.
- Do not change the prefix casually in a running cluster.
- Ensure that workload manifests use the same prefix.
`sriov-network-operator.operator.admissionControllers.enabled`Y

Controls the SR-IOV Network Operator admission controllers.

The admission controllers detect invalid SR-IOV configuration before it reaches nodes and help keep virtual-function and NIC settings consistent as the number of node groups and policies increases.

If the admission controllers are disabled:
- Invalid SR-IOV configuration might be applied.
- Misconfiguration might spread across many nodes.
- Recovery from configuration errors might be more difficult.
- Enable the admission controllers in production environments.
- Ensure that Certificate Manager and webhook certificate handling remain healthy.
- Disable the admission controllers only when there is a specific reason to avoid admission webhooks.
`sriov-network-operator.operator.sriovOperatorConfig.configDaemonNodeSelectors`Y

Selects the nodes that the SR-IOV configuration daemon configures.

The selector determines which nodes receive SR-IOV configuration. In a large cluster, an incorrect selector can affect hundreds or thousands of nodes.

If this argument is misconfigured:
- SR-IOV configuration might be applied to the wrong nodes.
- Intended nodes might not receive the configuration.
- Networking capabilities might become inconsistent across node pools.
- Align the selector closely with the node labels produced by Node Feature Discovery.
- Test the selector on a small node group before applying it broadly.
`vfCreationMode`N

Determines whether virtual-function creation is managed automatically by the operator or by custom logic.

An automated and consistent virtual-function creation process reduces configuration differences between nodes. Custom creation logic provides more flexibility but increases the likelihood of inconsistent node configuration.

If this argument is misconfigured:
- Virtual functions might not be created on the expected nodes.
- Node pools might behave differently.
- Networking configuration might drift over time.
- Use operator-managed virtual-function creation unless custom logic is required.
- Avoid mixing creation modes within the same operational domain.
- Validate virtual-function creation on a single node pool before applying it broadly.
`skipNodeFeatureDiscoveryDependencyCheck`Y

Determines whether the operator skips the Node Feature Discovery dependency check.

Skipping the check avoids redundant dependency validation when Node Feature Discovery is managed separately. However, the cluster administrator becomes responsible for ensuring that the required node labels are available and remain correct.

If this argument is misconfigured:
- The operator might depend on Node Feature Discovery even though it is not installed or healthy.
- Required labels might be missing.
- Incorrect node targeting for SR-IOV and related components might affect many nodes.
- Skip the dependency check only when Node Feature Discovery is already deployed and verified.
-
