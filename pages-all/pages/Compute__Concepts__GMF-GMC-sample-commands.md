# Exploring Your GPU Memory Clusters and Memory Fabric
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/GMF-GMC-sample-commands.htm
- Fetched: 2026-09-05 01:48 CDT

# Exploring Your GPU Memory Clusters and Memory Fabric

Explore how your GPU memory fabric and memory clusters connect using the OCI[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).

This diagram shows how GPU memory clusters and memory fabric relate to compute clusters, hosts, and instances.  

  

To further explore these relationships, use these sample commands:
- 

To list all GPU memory fabrics in your regional dedicated capacity:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-fabric/list.html)compute-gpu-memory-fabric list`command and required parameters:

```

```

- 

To get more details about a specific GPU memory fabric:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-fabric/get.html)compute-gpu-memory-fabric get`command and required parameters:

```

```

- 

To find the GPU memory fabric and instance associated with a bare metal host:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-host/get.html)compute-host get`command and required parameters:

```

```

- 

To find all bare metal hosts on a given GPU memory fabric:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-host/list.html)compute-host list`command and required parameters:

```

```

- 

To find the GPU memory cluster an instance belongs to:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/get.html)instance get`command and required parameters:

```

```

- 

To find the compute cluster, GPU memory fabric, and instance configuration associated with a GPU memory cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-cluster/get.html)compute-gpu-memory-cluster get`command and required parameters:

```

```

- 

To list all instances in a GPU memory cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-gpu-memory-cluster-instance-summary/list-compute-gpu-memory-cluster-instances.html)compute-gpu-memory-cluster-instance-summary list-compute-gpu-memory-cluster-instances`command and required parameters:

```

```

- 

To see additional details about a compute cluster:
Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/get.html)compute-cluster get`command and required parameters:

```

```

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html)
