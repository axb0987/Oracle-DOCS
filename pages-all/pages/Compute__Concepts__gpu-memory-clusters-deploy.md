# Creating GPU Memory Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-clusters-deploy.htm
- Fetched: 2026-09-05 01:49 CDT

# Creating GPU Memory Clusters

Create a memory cluster from a set of GPUs using the commands listed in this topic.

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

## Key Considerations
- A GPU memory cluster must be associated with a compute cluster.
- The hosts that are part of the GPU memory cluster are instantiated as part of the specified (and required) compute cluster.
- Many GPU memory clusters from different GPU memory fabrics can be associated with the same compute cluster.
- To launch multiple GPU memory clusters on a single GPU memory fabric, the GPU memory clusters must be associated with different compute clusters.
Note  
  
Compute shapes that support this "multiple GPU memory clusters" example are BM.GPU.GB200.4 and BM.GPU.GB300.4 .
- When you create one or more GPU memory clusters, instances are launched on the underlying hosts.
- You can't directly launch instances onto GPU memory fabric; instead, you create a GPU memory cluster.
- Instances of different shapes can be in the same compute cluster.
- Each GPU memory fabric requires the root tenancy OCID to be used for its`compartment-id`. This is true even if you create the associated GPU memory clusters in subcompartments.
- The GPU memory cluster OCID takes the form,`ocid1.computegpumemorycluster.oc1...`.
- The GPU memory fabric OCID takes the form,`ocid1.computegpumemoryfabric.oc1...`.
- The OCI HPC or OKE deployment stacks can be used to deploy Blackwell GPUs (for example, GB200/GB300 hosts) on multiple GPU memory fabrics. For details, see the readme associated with the version of the stack you're using.

## Get Started

Run these commands first, before creating the GPU memory cluster.
- 

Find your available GPU memory fabrics:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-fabric/list.html)compute-gpu-memory-fabric list`command and required parameters. Use the root compartment / tenancy OCID.

```

```

- 

Create a compute cluster in which to create the GPU memory cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/create.html)compute-cluster create`command and required parameters. Use the target compartment OCID.

```

```

- 

Create an instance configuration to use for instance launch in the GPU memory cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create.html)instance-configuration create`command and required parameters. Use the target compartment OCID.

```

```

Tip  
  
You might prefer to[create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration)via the OCI Cloud Console, rather than use a JSON input file.

You're now ready to create a GPU memory cluster.

## Create a GPU Memory Cluster

Important  
  
We recommend that you create the GPU memory cluster with all available hosts in the fabric. This is necessary to properly size the multicast limits for the NVLink partition, because after the partition is created, it can no longer be updated. The only way to update it after creation is to delete the GPU memory cluster and start over, or idle the workload on the rack and ask Oracle to update the partition in the background.

This means that you should launch with the maximum number of hosts available, rather than scaling up incrementally.
- The best practice is to set the`targetSize`specified in[CreateComputeGpuMemoryCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryCluster/CreateComputeGpuMemoryCluster)to the biggest you'll ever want your GPU memory cluster to be. See also[CreateComputeGpuMemoryClusterScaleConfig Reference](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateComputeGpuMemoryClusterScaleConfig).
- You can also use the count of instances specified in[CreateComputeGpuMemoryCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGpuMemoryCluster/CreateComputeGpuMemoryCluster).
- 

Create the GPU memory cluster:

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-cluster/create.html)compute-gpu-memory-cluster create`command and required parameters. Use the target compartment OCID.

When you create the GPU memory cluster, OCI attempts to instantiate`<size>`hosts; no additional instance launch command is needed.

(To set the`<size>`, use the`available-host-count`returned from the[`compute-gpu-memory-fabric list`step](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/gpu-memory-clusters-deploy.htm#deploy-GMC-get-started).)

```

```

## Configure a GPU Memory Cluster

Here are some additional commands you can use to further configure a GPU memory cluster, after creating it.
- 

Increase the number of instances in an existing GPU memory cluster:

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-cluster/update.html)compute-gpu-memory-cluster update`command and required parameters.
Set the`<size>`parameter to the total size you want (it's not an increment to the existing size):

```

```

- 

Reduce the number of instances in a GPU memory cluster:

To shrink the number of instances in a GPU memory cluster, normal/direct instance termination is used.

See[TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance).
- 

Terminate all instances and delete a GPU memory cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-cluster/delete.html)compute-gpu-memory-cluster delete`command and required parameters:

```

```
