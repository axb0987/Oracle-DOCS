# Detaching Instances from a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm
- Fetched: 2026-09-05 01:51 CDT

# Detaching Instances from a Cluster Network with Instance Pools

Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.

To remove instances from the cluster network by deleting instances, you can[resize the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm).

When you detach an instance, you can choose whether to delete or retain the instance. You can also choose whether to replace the detached instance by creating a new instance in the cluster network. If you don't replace the detached instance, then the size of the cluster network decreases.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#)
- 

- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select a cluster network.
- 

Navigate to attached instances using the option you see:
- Scroll down to Attached instances .
- Under Resources , select Attached instances.
- For the instance that you want to detach, from the Actions menu (three dots) select Detach instance .
- Permanently terminate (delete) this instance and its attached boot volume : To permanently delete the instance and its boot volume, select the checkbox.

By default, the size of the underlying instance pool is reduced. If you want the cluster network to remain the same size after you detach the instance, then you can provision a replacement instance.
- Replace the instance with a new instance, using the pool's instance configuration as a template for the instance : Select the checkbox to replace the detached instance with a new one.
- Select Detach (or Detach and terminate , if you're also deleting the instance).

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/detach.html)instance-pool-instance detach`command and required parameters to detach an instance from the underlying instance pool of a cluster network.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To detach instances from a cluster network's underlying instance pool, use the following API operation:
- [DetachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/DetachInstancePoolInstance)
