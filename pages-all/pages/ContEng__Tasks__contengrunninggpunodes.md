# Running Applications on GPU-based Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrunninggpunodes.htm
- Fetched: 2026-09-05 01:55 CDT

# Running Applications on GPU-based Nodes

Find out how to run applications on GPU-based worker nodes in clusters created using Kubernetes Engine (OKE).

To run applications on GPU-based worker nodes, you select a GPU shape and compatible GPU image either for the managed nodes in a managed node pool, or for self-managed nodes.

The shape determines the number of CPUs and the amount of memory allocated to each node. Among the shapes you can select are GPU (Graphics Processing Unit) shapes, with the GPUs themselves on NVIDIA graphics cards. Originally intended for manipulating images and graphics, GPUs are very efficient at processing large blocks of data in parallel. This capability makes GPUs a good option when deploying data intensive applications. For more information about the GPU shapes to select for worker nodes, see[GPU shapes supported by Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrunninggpunodes.htm#contengrunninggpunodes_topic-supportedgpushapes).

The massive parallel computing functionality of NVIDIA GPUs is accessed using CUDA (Compute Unified Device Architecture) libraries. Different GPUs (for example, NVIDIA® Tesla Volta™, NVIDIA® Tesla Pascal™) require specific versions of the CUDA libraries. When you select a GPU shape for a managed node pool or self-managed node, you must also select a compatible Oracle Linux GPU image that has the CUDA libraries pre-installed. The names of compatible images include 'GPU'.

You can select a GPU shape and compatible image for worker nodes in a cluster in the following ways:
- Managed nodes: By using Kubernetes Engine to create a managed node pool, and selecting a GPU shape (and compatible image) for the node pool. All the worker nodes in the managed node pool have the GPU shape. For more information, see[Creating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm).
- Self-managed nodes: By using the Compute service to create a compute instance (or instance pool) to host a self-managed node, selecting a GPU shape (and compatible image) for the instance, and specifying the Kubernetes cluster to which to add the instance. You can only add self-managed nodes to enhanced clusters. For more information, see[Working with Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm).

When you deploy an application on a cluster you've created with Kubernetes Engine, you have to specify in the pod spec the number of GPU resources that are required. To deploy the application, the kube-scheduler determines which node has the necessary resources. When an application pod is to run on a node with a GPU shape, the following are mounted into the pod:
- the requested number of GPU devices
- the node's CUDA library

The application is effectively isolated from the different types of GPU. As a result, CUDA libraries for different GPUs do not have to be included in the application container, ensuring the container remains portable.

Note the following:
- You can specify GPU shapes for managed node pools in clusters running Kubernetes version 1.19.7 or later. Do not specify a GPU shape for managed node pools in clusters running earlier versions of Kubernetes.
- You can use the Console, the API, or the CLI to specify a GPU image for use on a GPU shape. You can also use the API or the CLI to specify a non-GPU image for use on a GPU shape.
- Having created a managed node pool with a GPU shape, you cannot change the node pool to have a non-GPU shape. Likewise, you cannot change a managed node pool with a non-GPU shape to have a GPU shape.
- GPU shapes are not necessarily available in every availability domain.
- You can specify GPU shapes for managed node pools in clusters that are VCN-native (that is, clusters that have Kubernetes API endpoints hosted in a subnet of your VCN). Do not specify a GPU shape for managed node pools in a cluster if the cluster's Kubernetes API endpoint is not integrated into your VCN. See[Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm).
- You can run applications on GPU worker nodes in managed node pools, but not in virtual node pools.

## Defining a pod to run only on nodes that have a GPU

The following configuration file defines a pod to run on any node in the cluster that has one available GPU resource (regardless of the type of GPU):

```

```

## Defining a pod to run only on nodes that do not have a GPU

The following configuration file defines a pod to run only on nodes in the cluster that do not have a GPU:

```

```

## GPU shapes supported by Kubernetes Engine (OKE)

Kubernetes Engine supports different GPU shapes for managed node pools and nodes, and for self-managed nodes.

Note that due to service limits and compartment quotas, some of the supported GPU shapes might not be available in your particular tenancy.

### Supported GPU shapes for managed node pools and managed nodes

For managed node pools and managed nodes, Kubernetes Engine supports the available Virtual Machine (VM) GPU shapes and Bare Metal (BM) GPU shapes provided by Oracle Cloud Infrastructure (see[Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm)).

Note that due to service limits and compartment quotas, some of the supported GPU shapes might not be available in your particular tenancy.

### Supported GPU shapes for self-managed nodes

For self-managed nodes, Kubernetes Engine supports the GPU shapes available for the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) image you select when you create the compute instance to host the self-managed node.
