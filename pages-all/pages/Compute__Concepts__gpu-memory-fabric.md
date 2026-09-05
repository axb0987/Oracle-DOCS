# GPU Memory Cluster and Memory Fabric
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-fabric.htm
- Fetched: 2026-09-05 01:49 CDT

# GPU Memory Cluster and Memory Fabric

You can use GPU memory clusters to group, monitor, and manage high performance computing (HPC), GPU, or optimized instances together, and run high-performance clusters with more flexibility. Each GPU memory cluster is built on a single GPU memory fabric , the infrastructure that enables communication between GPUs. You use GPU memory clusters in conjunction with , not instead of, compute clusters.
Important  
  
You must be a[Dedicated Capacity customer](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm#capacity_types)to use GPU memory clusters and GPU memory fabric. To switch your host capacity, contact Oracle Support by opening a[Support Request (SR)](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
With GPU memory clusters, you can:
- Create a memory cluster from a set of GPUs.

For example, NVIDIA NVLink 72 supports up to 18 Compute hosts each.
- Combine many memory clusters into one large cluster that spans across a large network. GPU memory clusters are designed to scale at the rack level and let you scale up , whereas compute clusters let you scale out .
- GPU memory clusters facilitate host-to-host/GPU-to-GPU communication.
- Compute clusters facilitate communication, via RoCE or InfiniBand, between hosts/GPUs on different GPU memory fabrics.
- View all GPU memory clusters and see how they're connected.

See[ListComputeGpuMemoryClusters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryCluster/ListComputeGpuMemoryClusters)and[Exploring Your GPU Memory Clusters and Memory Fabric](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-GMC-sample-commands.htm#GMF-GMC-sample-commands).
- Track performance metrics for each memory cluster.
- Add or remove GPUs as needed.

Supported[Compute shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../References/computeshapes.htm#Compute_Shapes)
