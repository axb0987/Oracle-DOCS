# Resizing a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm
- Fetched: 2026-09-05 01:52 CDT

# Resizing a Cluster Network with Instance Pools

Change the number of instances in a cluster network by resizing the underlying instance pool.

When you increase the size, instances are provisioned until the required number of instances in the instance pool are launched, subject to host capacity for nodes in the cluster's RDMA network.

When you decrease the size, instances are terminated (deleted) in the order that they were created, first-in, first-out. To remove a specific instance from the cluster network, you can[detach the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)from the cluster network.

To determine whether capacity is available for a specific shape before you resize a cluster network, use the[CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)operation.
Note  
  
The cluster network must be in the Running state to be resized.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm#)
- 

- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select a cluster network.
- Select Edit .
- Number of instances : Specify the updated number of instances for the instance pool.
- Select Save changes .

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

To resize a cluster network, you can use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html)instance-pool update`command to resize the underlying instance pool to increase or decrease the size of the instance pool. You can also detach or attach an instance to change the pool size.
```

```

```

```

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To resize a cluster network's underlying instance pool, use the following API operations:
- [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool)
- [DetachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/DetachInstancePoolInstance)
- [AttachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/AttachInstancePoolInstance)
