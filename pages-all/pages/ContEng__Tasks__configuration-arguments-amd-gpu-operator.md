# AMD GPU Operator
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-operator.htm
- Fetched: 2026-09-05 01:53 CDT

# AMD GPU Operator

When you enable the AMD GPU Operator cluster add-on, you can pass the following key/value pairs as arguments.

[Configuration Arguments Common to most Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-operator.htm#)

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

[Configuration Arguments Specific to this Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-operator.htm#)

Note the following points when setting configuration arguments for the AMD GPU Operator cluster add-on:
- The Test Runner and Device Config Manager ConfigMap names in the sample values refer to ConfigMaps that you have pre-created in the AMD GPU Operator namespace.
- To enable the DRA driver, set`draDriver.enable`to`true`and`devicePlugin.enableDevicePlugin`to`false`in the same add-on update.
- For`imagePullPolicy`,`devicePluginImagePullPolicy`, and`nodeLabellerImagePullPolicy`, supported values are`Always`,`IfNotPresent`, and`Never`.
- Toleration arrays supplied through these parameters are merged with the add-on defaults. A supplied toleration replaces a default toleration with the same key and effect; otherwise, it is appended.

Key (API and CLI) Key's Display Name (Console) Description Required/Optional Default Value Example Value
`skipNodeFeatureDiscoveryDependencyCheck`skipNodeFeatureDiscoveryDependencyCheck Controls whether the add-on skips the Node Feature Discovery dependency check. Optional`false``true`
`selector`selector Selects the Kubernetes nodes managed by AMD GPU Operator. Optional`{"feature.node.kubernetes.io/amd-gpu":"true"}``{"node.kubernetes.io/instance-type":"BM.GPU.MI300X.8"}`
`devicePlugin`devicePlugin Configures the AMD GPU device plugin and node labeller. Optional`{"enableDevicePlugin":true,"devicePluginImagePullPolicy":"IfNotPresent","devicePluginTolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"enableNodeLabeller":true,"nodeLabellerImagePullPolicy":"IfNotPresent","nodeLabellerTolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"kubeletSocketPath":"/var/lib/kubelet/device-plugins","hostNetwork":false,"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}``{"enableDevicePlugin":true,"devicePluginImagePullPolicy":"Always","devicePluginTolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"devicePluginArguments":{"resource_naming_strategy":"single"},"enableNodeLabeller":true,"nodeLabellerImagePullPolicy":"Always","nodeLabellerTolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"nodeLabellerArguments":["compute-memory-partition","compute-partitioning-supported","memory-partitioning-supported"],"kubeletSocketPath":"/var/lib/kubelet/device-plugins","hostNetwork":true,"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}`
`metricsExporter`metricsExporter Configures AMD GPU metrics collection and exposure. Optional`{"enable":true,"serviceType":"ClusterIP","port":5000,"nodePort":32500,"imagePullPolicy":"IfNotPresent","tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"hostNetwork":false,"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1},"rbacConfig":{"enable":false,"disableHttps":false,"staticAuthorization":{"clientName":"","enable":false}},"prometheus":{"serviceMonitor":{"enable":false,"interval":"30s","honorLabels":true,"honorTimestamps":false}}}``{"enable":true,"serviceType":"NodePort","port":5001,"nodePort":32501,"imagePullPolicy":"IfNotPresent","config":{},"tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"hostNetwork":true,"selector":{"feature.node.kubernetes.io/amd-gpu":"true"},"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1},"rbacConfig":{"enable":true,"disableHttps":false},"prometheus":{"serviceMonitor":{"enable":false,"interval":"30s","honorLabels":true,"honorTimestamps":false}},"resource":{"limits":{"cpu":"1","memory":"1Gi"},"requests":{"cpu":"100m","memory":"128Mi"}},"podAnnotations":{"prometheus.io/scrape":"true"},"podResourceAPISocketPath":"/var/lib/kubelet/pod-resources","serviceAnnotations":{"prometheus.io/scrape":"true"}}`
`testRunner`testRunner Configures AMD GPU health validation and diagnostic testing on selected nodes. Optional`{"enable":false,"imagePullPolicy":"IfNotPresent","tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"logsLocation":{"hostPath":"/var/log/amd-test-runner","logsExportSecrets":[],"mountPath":"/var/log/amd-test-runner"},"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}``{"enable":true,"imagePullPolicy":"IfNotPresent","config":{"name":"test-runner-config-map"},"logsLocation":{"hostPath":"/var/log/amd-test-runner","mountPath":"/var/log/amd-test-runner","logsExportSecrets":[]},"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1},"tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"selector":{"feature.node.kubernetes.io/amd-gpu":"true"}}`
`configManager`configManager Configures AMD GPU partitioning profiles through the Device Config Manager. Optional`{"enable":false,"imagePullPolicy":"IfNotPresent","configManagerTolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}``{"enable":true,"imagePullPolicy":"IfNotPresent","config":{"name":"config-manager-config"},"selector":{"feature.node.kubernetes.io/amd-gpu":"true"},"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1},"configManagerTolerations":[{"key":"amd-dcm","operator":"Equal","value":"up","effect":"NoExecute"}]}`
`draDriver`draDriver Configures Kubernetes Dynamic Resource Allocation for AMD GPUs. Optional`{"enable":false,"imagePullPolicy":"IfNotPresent","tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}``{"enable":true,"imagePullPolicy":"IfNotPresent","tolerations":[{"key":"amd.com/gpu","operator":"Equal","value":"present","effect":"NoSchedule"}],"cmdLineArguments":{},"selector":{"feature.node.kubernetes.io/amd-gpu":"true"},"upgradePolicy":{"upgradeStrategy":"RollingUpdate","maxUnavailable":1}}`
`controllerManager`controllerManager Configures the AMD GPU Operator controller deployment. Optional`{"replicas":1,"resources":{"limits":{"cpu":"1000m","memory":"1Gi"},"requests":{"cpu":"100m","memory":"256Mi"}},"imagePullPolicy":"Always","nodeSelector":{},"affinity":{"nodeAffinity":{"preferredDuringSchedulingIgnoredDuringExecution":[{"weight":1,"preference":{"matchExpressions":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists"}]}}]}},"tolerations":[{"key":"amd-gpu-unhealthy","operator":"Exists","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/control-plane","operator":"Equal","effect":"NoSchedule"}],"simEnable":false}``{"replicas":2,"resources":{"requests":{"cpu":"120m","memory":"192Mi"}},"imagePullPolicy":"IfNotPresent","nodeSelector":{"kubernetes.io/os":"linux"},"affinity":{"nodeAffinity":{"preferredDuringSchedulingIgnoredDuringExecution":[{"weight":10,"preference":{"matchExpressions":[{"key":"kubernetes.io/os","operator":"In","values":["linux"]}]}}]}},"tolerations":[{"key":"validation.amd.com/controller","operator":"Exists","effect":"NoSchedule"}],"simEnable":false}`
