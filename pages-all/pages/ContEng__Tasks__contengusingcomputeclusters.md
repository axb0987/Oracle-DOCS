# Using Compute Clusters to Provision Managed Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcomputeclusters.htm
- Fetched: 2026-09-05 01:57 CDT

# Using Compute Clusters to Provision Managed Nodes

Find out how to create managed node pools in compute clusters using Kubernetes Engine (OKE) to support workloads that use RDMA-capable bare metal shapes.

A compute cluster is a Compute service resource that provides high-bandwidth, low-latency networking between supported bare metal instances. In Kubernetes Engine, you can specify a compute cluster when you create a managed node pool. When Kubernetes Engine creates worker node instances for the node pool, the Compute service launches the instances in the selected compute cluster.

Use compute clusters for managed node pools that run workloads requiring RDMA-capable networking, such as distributed training workloads. Specifying a compute cluster for a managed node pool enables you to use RDMA-capable networking while retaining Kubernetes Engine managed node pool operations, such as scaling, upgrades, and node replacement.

Kubernetes Engine does not create compute clusters. Create and configure the compute cluster in the Compute service before selecting it in Kubernetes Engine. For more information about compute clusters, see[Compute Clusters](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm)in the Compute service documentation.

When you specify a compute cluster for a managed node pool, Kubernetes Engine automatically enables the Oracle Cloud Agent HPC plugins required for RDMA networking, including the Compute HPC RDMA Authentication plugin and the Compute HPC RDMA Auto-Configuration plugin. Note that you cannot customize this Oracle Cloud Agent plugin configuration using the Kubernetes Engine node pool APIs.

You can only specify a compute cluster when creating a managed node pool. You cannot add, remove, or change the compute cluster for an existing node pool. To use a different compute cluster, create a new managed node pool.

Before you create a managed node pool in a compute cluster, note the following:
- The Kubernetes Engine cluster must be an enhanced cluster.
- Create the compute cluster in the Compute service.
- Make sure the compute cluster lifecycle state is`ACTIVE`.
- Use a node pool shape that supports RDMA and compute clusters (see[Supported Shapes](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-cluster-shapes)in the Compute service documentation).
- The node pool placement configuration must include only the availability domain that contains the compute cluster.
- Do not specify fault domains in the placement configuration. When a compute cluster is specified, fault domain placement is managed by the Compute service.
- Add the required IAM policy so Kubernetes Engine can use the compute cluster when launching worker node instances.

## Required IAM policy

To enable a node pool to use a compute cluster, a policy must exist that allows the node pool resource principal to use the compute cluster. For example:
```

```

where:
- `<compartment_name>`is the name of the compartment that contains the compute cluster.
- `<compute_cluster_OCID>`is the OCID of the compute cluster.

## Using the Console

You can specify a compute cluster when you create a cluster with a managed node pool, or when you create a managed node pool in an existing enhanced cluster.

You cannot specify a compute cluster when updating an existing managed node pool.

### Creating a cluster and specifying a compute cluster for a managed node pool
- Follow the instructions to create a cluster using the Custom Create workflow. See[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).
- When specifying node pool details:
- For Node type , select Managed .
- Specify the Node placement configuration as follows:
- Availability domain: Select the availability domain that contains the compute cluster.
- Worker node subnet compartment: Select the compartment that contains the worker node subnet.
- Worker node subnet: Select a subnet in the compute cluster's availability domain.
- Fault domains: Do not specify fault domains. Fault domain placement is managed by the Compute service.
- For Node shape , select a node shape that supports RDMA and compute clusters.
- Select Advanced options and specify the compute cluster to use in the Add a compute cluster section:
- Compute cluster compartment: Select the compartment that contains the compute cluster.
- Compute cluster: Select the compute cluster.
- Create the cluster.

Kubernetes Engine creates the cluster and managed node pool. When Kubernetes Engine creates worker node instances for the managed node pool, the Compute service launches the instances in the selected compute cluster.

### Creating a managed node pool and specifying a compute cluster
- On the Clusters list page, select the name of the enhanced cluster where you want to create a new node pool. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Node pools tab of the cluster details page, select Add node pool to create a new managed node pool and specify the required properties for its worker nodes.
- When specifying node pool details:
- For Node type , select Managed .
- Select Advanced options and specify the compute cluster to use in the Add a compute cluster section:
- Compute cluster compartment: Select the compartment that contains the compute cluster.
- Compute cluster: Select the compute cluster.
- Specify the Node placement configuration as follows:
- Availability domain: Select the availability domain that contains the compute cluster.
- Worker node subnet compartment: Select the compartment that contains the worker node subnet.
- Worker node subnet: Select a subnet in the compute cluster's availability domain.
- Fault domains: Do not specify fault domains. Fault domain placement is managed by the Compute service.
- For Node shape , select a node shape that supports RDMA and compute clusters.
- Create the node pool.

Kubernetes Engine creates the managed node pool. When Kubernetes Engine creates worker node instances for the managed node pool, the Compute service launches the instances in the selected compute cluster.

## Using the CLI

To use the CLI to create a managed node pool in a compute cluster, include the`computeClusterId`key/value pair in the`--node-config-details`parameter in the format:
```

```

The placement configuration must include only the availability domain that contains the compute cluster. Do not specify fault domains.

## Using the API

When creating a managed node pool, specify`computeClusterId`in the node pool configuration details.

For create node pool requests, specify:
```

```

The`computeClusterId`property is immutable. You cannot specify`computeClusterId`in`UpdateNodePoolDetails`.

## Troubleshooting

Use the following information to troubleshoot issues with compute clusters in managed node pools.

### The compute cluster is not available in the list

Check the following:
- You selected the correct compartment.
- The compute cluster is active.
- You have permission to view or use the compute cluster.
- The Kubernetes Engine cluster is an enhanced cluster.

### Node pool creation fails

Check the following:
- The Kubernetes Engine cluster is an enhanced cluster.
- The node pool shape supports RDMA and compute clusters.
- The placement configuration includes only the availability domain that contains the compute cluster.
- Fault domains are not specified in the placement configuration.
- The required IAM policy exists.
- The selected compute cluster is not deleted or inactive.

### I cannot add or change the compute cluster for an existing node pool

You can specify a compute cluster only when creating a managed node pool. You cannot add, remove, or change the compute cluster for an existing node pool.
