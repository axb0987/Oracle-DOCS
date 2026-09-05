# Managing Specialized Hardware Devices on Worker Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmanagingspecializedhardwaredevices.htm
- Fetched: 2026-09-05 01:55 CDT

# Managing Specialized Hardware Devices on Worker Nodes

Find out how to make GPUs and other specialized hardware devices available to workloads deployed to clusters created with Kubernetes Engine (OKE).

For a containerized workload deployed to an OKE cluster to use a specialized hardware device, such as a graphical processing unit (GPU) accelerator or a high-performance network device, you must enable a mechanism for Kubernetes to advertise and allocate the device. For more information about devices, see[Device](https://kubernetes.io/docs/reference/glossary/?all=true#term-device)in the Kubernetes documentation.

Kubernetes supports the following mechanisms for making specialized hardware devices available to workloads:
- Device plugins: A device plugin discovers devices on a worker node and advertises them to Kubernetes as extended resources. For example, the NVIDIA Device Plugin for Kubernetes advertises GPUs using the`nvidia.com/gpu`extended resource.
- Dynamic Resource Allocation (DRA): A DRA driver publishes information about individual devices using`ResourceSlice`objects. Applications request devices using`ResourceClaim`or`ResourceClaimTemplate`objects that reference a`DeviceClass`.

## Device Plugins

Device plugins enable Kubernetes clusters to use hardware that requires vendor-specific initialization or configuration, including GPUs and high-performance network interfaces. The Kubernetes device plugin framework allows vendors to advertise hardware resources to the[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/).

Hardware vendors, such as AMD and NVIDIA, implement device plugins that cluster administrators can deploy to discover supported devices on each node, perform required vendor-specific setup, and make the devices available for allocation to Kubernetes workloads.

For more information, see[Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)in the Kubernetes documentation.

OKE simplifies the installation of GPU-related plugins by providing optional cluster software add-ons:
- AMD GPU Plugin: The optional AMD GPU Plugin add-on is a convenient way to manage the AMD Device Plugin for Kubernetes. The AMD Device Plugin for Kubernetes implements the Kubernetes device plugin framework to expose AMD GPUs as schedulable resources.
- AMD GPU Operator: The optional AMD GPU Operator add-on automates the deployment and management of AMD GPU software components. These components include the device plugin, node labeller, metrics exporter, test runner, and device configuration manager, which support AMD GPU workloads, monitoring, and GPU sharing in Kubernetes clusters.
- NVIDIA GPU Plugin: The optional NVIDIA GPU Plugin add-on is a convenient way to manage the NVIDIA Device Plugin for Kubernetes. The NVIDIA Device Plugin for Kubernetes implements the Kubernetes device plugin framework to expose the number of NVIDIA GPUs on each worker node and track the health of those GPUs.
- NVIDIA GPU Operator: The optional NVIDIA GPU Operator add-on automates the management of NVIDIA software components required to provision GPU nodes. The add-on works with NVIDIA GPU drivers installed on worker nodes and manages components such as the NVIDIA device plugin, NVIDIA Container Toolkit, MIG Manager, DCGM, and DCGM Exporter to enable GPU workloads, monitoring, and GPU sharing capabilities in Kubernetes clusters.

For more information, see[Overview of Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengintroducingclusteraddons.htm).

## Dynamic Resource Allocation

Dynamic Resource Allocation (DRA) is a Kubernetes feature that lets you request and share attached device resources among pods. These resources are typically attached devices, such as GPUs and other hardware accelerators.

Allocating resources with DRA is similar to Kubernetes[dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/), which enables applications to claim storage capacity from storage classes using PersistentVolumeClaims. With DRA, device drivers and cluster administrators define device classes that workloads can claim. Kubernetes then selects devices that match the claims and schedules pods that request those claims on nodes that can access the allocated devices.

For more information, see[Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)in the Kubernetes documentation.

### Deploying and Verifying DRA for GPUs

To deploy and verify Dynamic Resource Allocation for NVIDIA GPU devices, first[create an OKE cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm)running Kubernetes version 1.34 or later. DRA APIs are enabled by default on OKE clusters running Kubernetes version 1.34 or later.

Deploy a node pool that uses GPU shapes, for example`VM.GPU.A10.2`, and an OKE Oracle Linux GPU image (see[All OKE Worker Node Oracle Linux 9.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-9x/index.htm)) or a custom image with compatible GPU drivers.

For the current DRA Driver for NVIDIA GPUs installation requirements and instructions, see[Install the driver](https://dra-driver-nvidia-gpu.sigs.k8s.io/docs/install/).
- 

Install the DRA Driver for NVIDIA GPUs Helm chart, by entering:

```

```

Example output:
```

```

- 

Verify that the DRA driver pod is running, by entering:

```

```

Example output:
```

```

- 

Verify the devices and driver information that the DRA driver publishes in`ResourceSlice`objects, by entering:

```

```

`ResourceSlice`objects are the authoritative inventory published and maintained by the DRA driver. Kubernetes uses`ResourceSlice`objects to publish device attributes, versions, capacity, and node accessibility.

The output is similar to:
```

```
