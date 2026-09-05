# Cluster Add-on Configuration Arguments
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm
- Fetched: 2026-09-05 01:54 CDT

# Cluster Add-on Configuration Arguments

Find out about the configuration arguments that you can pass to cluster add-ons.

When you enable a cluster add-on, you can specify one or more key/value pairs to pass as arguments to the cluster add-on.

If the value of a key is required in JSON format, you can specify the value in plain text or Base64 encoded. For example, you could specify either of the following as the value of the`coreDnsContainerResources`key:
- `{"limits": {"cpu": "500m", "memory": "200Mi" }, "requests": {"cpu": "100m", "memory": "100Mi"}}`(plain text)
- `eyJsaW1pdHMiOiB7ImNwdSI6ICI1MDBtIiwgIm1lbW9yeSI6ICIyMDBNaSIgfSwgInJlcXVlc3RzIjogeyJjcHUiOiAiMTAwbSIsICJtZW1vcnkiOiAiMTAwTWkifX0=`(Base64 encoded)

If the value of a key is required in JSON form, depending on the OCI tool you are using, you might have to escape double quotation marks in the key value with single backslash characters, as follows:
- If you are specifying the value of a key when using the Console, do not escape double quotation marks in the key value. For example, when using the Console to specify the value of the`cluster-autoscaler container resources`key, enter the following:
```

```

- If you are specifying the value of a key when using the CLI or API, always escape double quotation marks in the key value with a single backslash. For example, when using the CLI to specify the value of the`cluster-autoscaler container resources`key, use the following notation:
```

```

Add-ons:
- [kube-proxy](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-kube-proxy.htm)
- [CoreDNS](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-coredns.htm)
- [OCI VCN-Native Pod Networking CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-vcn-native-podnetworking.htm)
- [flannel](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-flannel.htm)
- [ObservabilityAgent](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-observabilityagent.htm)
- [NodeProblemDetector](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nodeproblemdetector.htm)
- [Kubernetes Dashboard (not recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-k8s-dashboard.htm)
- [Tiller (not recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-tiller.htm)
- [Oracle Database Operator for Kubernetes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-db-operator-for-k8s.htm)
- [WebLogic Kubernetes Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-weblogic-k8s-operator.htm)
- [Certificate Manager](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-certificate-manager.htm)
- [Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-cluster-autoscaler.htm)
- [Istio](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-istio.htm)
- [OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm)
- [Kubernetes Metrics Server](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm)
- [NVIDIA GPU Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm)
- [AMD GPU Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-plugin.htm)
- [Node Feature Discovery](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-node-feature-discovery-plugin.htm)
- [NVIDIA GPU Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm)
- [NVIDIA Network Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-network-operator.htm)
- [CSI Driver SMB](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-csi-driver-smb.htm)
- [AMD GPU Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-amd-gpu-operator.htm)
