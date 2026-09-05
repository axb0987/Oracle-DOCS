# Upgrading Managed Nodes to Kubernetes version 1.35 (or later)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Upgrading_managed_nodes_to_k8s_135.htm
- Fetched: 2026-09-05 01:57 CDT

# Upgrading Managed Nodes to Kubernetes version 1.35 (or later)

Find out how to upgrade managed nodes that currently use an OKE OL7 image, an OL7 platform image, or a custom image based on an OL7 image, to run Kubernetes version 1.35 (or later) and OL8, using Kubernetes Engine (OKE).
Note  
  
This section applies to managed nodes only. For information about upgrading self-managed nodes, see[Upgrading Self-Managed Nodes to a Newer Kubernetes Version by Replacing an Existing Self-Managed Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm).

Starting with Kubernetes version 1.35, Kubernetes requires cgroups v2 for container resource management.

Control Groups (cgroups) is a Linux kernel feature that provides a mechanism for managing and controlling resource allocation for processes or groups of processes. Control groups version 2 (cgroups v2) groups provide a single control group hierarchy against which all resource controllers are mounted. In this hierarchy, you can coordinate resource use across different resource controllers.

Oracle Linux 7 (OL7) supports cgroups v1, but does not support cgroups v2. Oracle Linux 8 (OL8) and later versions support both cgroups v1 and cgroups v2, but cgroups v2 is not always enabled by default in OL8.

In summary, Kubernetes version 1.35 therefore requires OL8 (or later) with cgroups v2 enabled.

Cgroups v2 is enabled by default in OKE OL8 images that have a build number of 1367 or greater. However, in OKE OL8 images that have a build number lower than 1367 (and in OL8 platform images), cgroups v1 is enabled by default.

For worker nodes on clusters running Kubernetes version 1.35 (and later), Kubernetes Engine supports the following images:
- OKE OL8 images, and custom images based on OKE OL8 images, that have a build number of 1367 or greater.
- OKE OL8 images, and custom images based on OKE OL8 images, that have a build number lower than 1367, but only if you enable cgroups v2 (see[Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengcreatingcgroupv2enabledworkernodes.htm)).
- Custom images based on OL8 platform images, but only if you enable cgroups v2 (see[Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengcreatingcgroupv2enabledworkernodes.htm)).

In clusters running Kubernetes version 1.35 (and later), the use of platform images (both OL7 platform images and OL8 platform images) is not recommended. We strongly recommend the use of OKE images for all new deployments and upgrades. If you want to continue to use a platform image, create a custom image based on the platform image and specify the custom image's OCID when creating or updating a node pool (note that we do not recommend this approach).

When upgrading managed nodes that currently use an OL8 image to Kubernetes version 1.35 (and later), note the following:
- You can upgrade managed nodes that currently use an OKE OL8 image (or a custom image based on an OKE OL8 image) with a build number lower than 1367, by performing an in-place upgrade and specifying an OKE OL8 image with a build number of 1367 or greater.
- You can upgrade managed nodes that currently use an OL8 platform image by performing an in-place upgrade and specifying an OKE OL8 image with a build number of 1367 or greater.
- You can perform in-place upgrades of managed nodes that currently use an OL8 image, regardless of whether the Linux kernels of compute instances hosting the nodes already have cgroups v2 enabled.
- For instructions to perform in-place upgrades, see[Upgrading Managed Nodes to a Newer Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm).
- For more information about the introduction of support for Kubernetes version 1.35, see[OKE Welcomes Kubernetes 1.35: What’s new, what’s changing, and what to do next](https://blogs.oracle.com/cloud-infrastructure/oke-welcomes-kubernetes-1-35).

## Validate workloads for cgroups v2

Before upgrading production worker nodes, verify that applications and supporting agents are compatible with cgroups v2.

cgroups v2 can change how container memory is accounted for. An increase in reported container memory usage alone does not necessarily indicate memory saturation. Investigate an increase when it is accompanied by one or more of the following conditions:
- Container out-of-memory (OOM) terminations.
- Container or pod restarts.
- Pod evictions.
- The`MemoryPressure`node condition.

For information about cgroups v2 requirements, memory accounting, runtime compatibility, and determining the cgroups version used by a node, see[About cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/)in the Kubernetes documentation.

Older application runtimes might not correctly detect container resource limits on systems that use cgroups v2. For example, a Java application might calculate heap or other memory settings from the worker node's resources instead of the container's memory limit. As a result, the container might exceed its configured memory limit and be terminated by the Linux OOM killer.

For Java workloads, use one of the following JDK releases or a later release:
- JDK 15
- JDK 11.0.16
- JDK 8u381

JDK 8u372 introduced cgroups v2 awareness. JDK 8u381 includes further improvements to cgroups v1 and cgroups v2 resource-limit detection, container metrics, and application stability. For other JDK distributions and application runtimes, consult the vendor documentation to identify a release that supports cgroups v2.

Also verify the compatibility of monitoring, security, and other agents that directly access`/sys/fs/cgroup`. Update incompatible agents to versions that support cgroups v2.

Before upgrading production worker nodes, perform the following validation in a non-production environment:
- Test representative workloads and supporting agents on nodes that use cgroups v2.
- Compare the following information before and after enabling cgroups v2:
- Reported container memory usage
- Container OOM events
- Container and pod restarts
- Pod evictions
- The`MemoryPressure`node condition
- The memory limit detected by the application runtime
- 

For Java workloads:
- 

Record the JDK version by entering:
```

```

- 

Review the system and container settings detected by the JVM by entering:
```

```

- 

Configure explicit`-Xms`and`-Xmx`values when appropriate for the workload.

## Upgrade OL7 managed nodes to run Kubernetes version 1.35 (or later)

To upgrade managed nodes that currently use an OKE OL7 image, an OL7 platform image, or a custom image based on an OL7 image, to run Kubernetes version 1.35 (or later), perform an out-of-place upgrade to replace the existing node pool with a new node pool:
- 

Identify existing node pools that use OL7, using the Console or the CLI as follows:
- 

Using the Console:
- On the Clusters list page, select the name of the cluster containing the node pools you want to see. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Node pools tab.
- Use the Image name column to identify node pools that use`Oracle-Linux-7.9.x`images.
- 

Using the CLI: Identify existing node pools that use OL7 by entering a command similar to the following::
```

```

- 

Create a replacement node pool that uses an OL8 image, using the Console or the CLI as follows:
- 

Using the Console:
- On the Node pools tab, select Add node pool , and enter details for the new node pool.
- Select an OKE Worker Node Image based on an`Oracle Linux 8.x`image.
- Configure the new node pool with the same shape, size, and placement as the OL7 node pool.
- Select Create .
- 

Using the CLI: Create a replacement node pool that uses an OL8 image by entering a command similar to the following:
```

```

- 

Cordon the OL7 nodes:
- 

Get the names of OL7 nodes by entering:
```

```

- 

Cordon each node by entering:
```

```

- 

Drain the OL7 nodes to gracefully migrate workloads:
- Drain each OL7 node by entering:
```

```

- Verify that workloads have been rescheduled on the new nodes by entering:
```

```

- 

Delete the OL7 node pool using the Console or the CLI, as follows:
- 

Using the Console:
- On the Node pools tab, select Delete node pool from the Actions menu (three dots) beside the OL7 node pool.
- Click Delete .
- Confirm that you want to delete the node pool, and select Delete .
- 

Using the CLI: Delete the OL7 node pool:
```

```

- 

Upgrade the cluster (for example, to Kubernetes version 1.35):
```

```

For more information, see[Performing an Out-of-Place Managed Node Kubernetes Upgrade by Replacing an Existing Node Pool with a New Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode_topic-Performing_an_OutofPlace_Worker_Node_Upgrade_by_Replacing_an_Existing_Node_Pool_with_a_New_Node_Pool.htm)
