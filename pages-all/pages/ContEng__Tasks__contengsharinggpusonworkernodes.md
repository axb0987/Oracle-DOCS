# Sharing GPUs on Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsharinggpusonworkernodes.htm
- Fetched: 2026-09-05 01:56 CDT

# Sharing GPUs on Worker Nodes

Find out how to improve GPU utilization by sharing GPUs between workloads running on worker nodes in clusters created with Kubernetes Engine (OKE).

Kubernetes represents GPUs and other accelerators as schedulable resources that are advertised by a device plugin. By default, a workload requests an integer number of GPU resources. For example, a workload that requests one standard NVIDIA GPU resource is allocated one GPU device.

If a workload does not require exclusive access to an entire physical GPU, you can improve GPU utilization by sharing a GPU between multiple workloads.

OKE supports the following NVIDIA GPU-sharing mechanisms:
- [NVIDIA Multi-Instance GPU (MIG)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/index.html): Provides hardware-level GPU partitioning. MIG partitions a supported physical GPU into hardware-isolated GPU instances. Each instance is exposed to Kubernetes as a schedulable resource.
- [NVIDIA Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/mps/latest/index.html): Enables compatible CUDA workloads to use the same physical GPU concurrently. MPS divides available GPU memory and compute capacity between clients.
- [NVIDIA Time-slicing](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html): Enables GPU oversubscription by allowing multiple workloads to take turns using the same physical GPU or supported MIG resource.

The sharing mechanism to use depends on the GPU hardware, workload requirements, and the level of isolation that the workloads require.

For information about running applications on GPU-based worker nodes, see[Running Applications on GPU-based Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrunninggpunodes.htm).

## Sharing GPUs Using Multi-Instance GPU (MIG)

NVIDIA Multi-Instance GPU (MIG) enables you to partition a supported physical GPU into multiple hardware-isolated GPU instances. Each instance has dedicated compute, memory, memory bandwidth, and cache resources.

Use MIG when multiple workloads need to share a physical GPU but require stronger resource and fault isolation than MPS or time-slicing provides.

For information about MIG architecture, see[NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html).

To configure MIG on compatible OKE GPU worker nodes, use the NVIDIA GPU Operator cluster add-on.

The NVIDIA GPU Operator manages components used to configure and expose MIG resources, including:
- MIG Manager, which enables MIG mode and applies the requested MIG configuration.
- NVIDIA Device Plugin for Kubernetes, which exposes MIG instances as schedulable Kubernetes resources.
- GPU Feature Discovery, which labels nodes with information about available GPUs and MIG resources.

When configuring the NVIDIA GPU Operator add-on for MIG, use the following configuration arguments as appropriate:
- Set`migManager.enabled`to enable MIG Manager.
- Set`devicePlugin.enabled`to enable NVIDIA Device Plugin for Kubernetes.
- Set`mig.strategy`to specify how MIG resources are exposed.
- Set`migManager.config.name`to specify a ConfigMap containing a custom`mig-parted`configuration, if required.
- Set`migManager.gpuClientsConfig.name`to specify a custom GPU clients ConfigMap, if required.
- Set`migManager.env`to specify supported MIG Manager environment variables, if required.

For the currently supported arguments and default values, see[NVIDIA GPU Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm).

OKE does not determine which MIG profiles are available on a GPU. The supported profiles and profile combinations depend on the GPU model and installed NVIDIA software.

For more information, see:
- [NVIDIA GPUs that support MIG](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html)
- [Supported MIG profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)
- [Using MIG with NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html)

## Sharing GPUs Using Multi-Process Service (MPS)

NVIDIA Multi-Process Service (MPS) enables multiple compatible CUDA workloads to use a single physical GPU concurrently.

NVIDIA Device Plugin for Kubernetes uses a CUDA MPS control daemon to manage access to the shared GPU. The control daemon divides the available GPU memory and compute capacity between the configured clients.

You specify the number of shared containers that can use a physical GPU. This value determines the share of the physical GPU resources available to each container through MPS.

For information about the MPS configuration format and restrictions, see[Sharing GPUs with CUDA MPS](https://github.com/NVIDIA/k8s-device-plugin#with-cuda-mps)in the NVIDIA Device Plugin for Kubernetes documentation.

OKE supports configuring MPS through NVIDIA Device Plugin for Kubernetes. You can use either of the following OKE cluster add-ons:
- NVIDIA GPU Plugin: Use this add-on if you require the NVIDIA device plugin and its GPU-sharing capabilities.
- NVIDIA GPU Operator: Use this add-on if you also require other NVIDIA components managed by the operator.

### Using the NVIDIA GPU Plugin Add-on

To configure MPS using the NVIDIA GPU Plugin add-on:
- Set the`useConfigFile`add-on configuration argument to`true`.
- Create a ConfigMap named`nvidia-device-plugin-config`.
- Create the ConfigMap in the`kube-system`namespace.
- In the ConfigMap, specify the MPS sharing configuration using the configuration schema defined by NVIDIA.

For information about the OKE-specific configuration arguments, see[NVIDIA GPU Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm).

### Using the NVIDIA GPU Operator Add-on

To configure MPS using the NVIDIA GPU Operator add-on:
- Enable NVIDIA Device Plugin for Kubernetes.
- Set`devicePlugin.config.name`to the name of the ConfigMap containing the NVIDIA device-plugin configuration.
- If the MPS host path must differ from the add-on default, set`devicePlugin.mps.root`.
- If the NVIDIA GPU Plugin add-on is already installed, set`disableNvidiaGpuPlugin`as appropriate to prevent multiple add-ons from managing the same device-plugin resources.

For information about the supported arguments and default values, see[NVIDIA GPU Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm).

OKE provides the add-on integration through which NVIDIA Device Plugin for Kubernetes receives the MPS configuration. NVIDIA defines the MPS configuration schema and behavior, including:
- Supported resource types.
- Resource naming.
- Replica behavior.
- Node labels used to identify MPS sharing.
- Application and CUDA compatibility requirements.
- Support and maturity of MPS in individual NVIDIA device-plugin releases.

For current behavior and restrictions, see:
- [Shared access to GPUs](https://github.com/NVIDIA/k8s-device-plugin#shared-access-to-gpus)
- [Sharing GPUs with CUDA MPS](https://github.com/NVIDIA/k8s-device-plugin#with-cuda-mps)
- [Catalog of Labels](https://github.com/NVIDIA/k8s-device-plugin#catalog-of-labels)

## Sharing GPUs Using Time-Slicing

NVIDIA GPU time-slicing enables multiple workloads to share a physical GPU through interleaved execution.

A time-slicing configuration specifies a number of replicas for an underlying GPU resource. NVIDIA Device Plugin for Kubernetes advertises the configured number of shared accesses for the device. Kubernetes can therefore schedule more GPU workloads than there are physical GPU devices.

Unlike MIG, time-slicing does not provide memory or fault isolation between replicas.

OKE supports configuring time-slicing through NVIDIA Device Plugin for Kubernetes. You can use either of the following OKE cluster add-ons:
- NVIDIA GPU Plugin: Use this add-on if you require the NVIDIA device plugin and its GPU-sharing capabilities.
- NVIDIA GPU Operator: Use this add-on if you also require other NVIDIA components managed by the operator.

### Using the NVIDIA GPU Plugin Add-on

To configure time-slicing using the NVIDIA GPU Plugin add-on:
- Set the`useConfigFile`add-on configuration argument to`true`.
- Create a ConfigMap named`nvidia-device-plugin-config`.
- Create the ConfigMap in the`kube-system`namespace.
- In the ConfigMap, specify the time-slicing configuration using the configuration schema defined by NVIDIA.

For information about the OKE-specific configuration arguments, see[NVIDIA GPU Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-plugin.htm).

### Using the NVIDIA GPU Operator Add-on

To configure time-slicing using the NVIDIA GPU Operator add-on:
- Enable NVIDIA Device Plugin for Kubernetes.
- Set`devicePlugin.config.name`to the name of the ConfigMap containing the NVIDIA device-plugin configuration.
- If the NVIDIA GPU Plugin add-on is already installed, set`disableNvidiaGpuPlugin`as appropriate to prevent multiple add-ons from managing the same device-plugin resources.

For information about the supported arguments and default values, see[NVIDIA GPU Operator](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nvidia-gpu-operator.htm).

OKE provides the add-on integration through which NVIDIA Device Plugin for Kubernetes receives the time-slicing configuration. NVIDIA defines time-slicing behavior, including:
- The time-slicing configuration schema.
- Resources that can be time-sliced.
- The number and meaning of advertised replicas.
- Shared-resource naming.
- Controls for rejecting requests for multiple shared replicas.
- Node labels used to identify time-sliced resources.
- Supported combinations of time-slicing and MIG.

For current behavior and restrictions, see:
- [Shared access to GPUs](https://github.com/NVIDIA/k8s-device-plugin#shared-access-to-gpus)
- [Sharing GPUs with CUDA time-slicing](https://github.com/NVIDIA/k8s-device-plugin#with-cuda-time-slicing)
- [Catalog of Labels](https://github.com/NVIDIA/k8s-device-plugin#catalog-of-labels)

Time-slicing can be configured for full GPU resources and, when supported by the installed NVIDIA device-plugin version, for resource types exposed using the`mixed`MIG strategy.

## Using Different GPU-Sharing Configurations on Different Nodes

An NVIDIA device-plugin ConfigMap can contain multiple named configurations. You can select a configuration for an individual node by applying the`nvidia.com/device-plugin.config`node label.

For example, you can configure a cluster to use:
- Different time-slicing replica counts on different groups of GPU nodes.
- Time-slicing on selected GPU nodes.
- MPS on other compatible GPU nodes.
- Exclusive GPU allocation on nodes that do not select a sharing configuration.

For the current procedure for selecting a device-plugin configuration on individual nodes, see[Updating per-node configuration with a node label](https://github.com/NVIDIA/k8s-device-plugin#updating-per-node-configuration-with-a-node-label)
