# Deleting a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm
- Fetched: 2026-09-05 01:50 CDT

# Deleting a Cluster Network with Instance Pools

Delete (terminate) a cluster network that you no longer need.
Caution  
  
When you delete a cluster network, you permanently delete all resources within the cluster network, including associated instances and instance pools, attached boot volumes, and block volumes.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm#)
- 

- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select a cluster network.
- From the Actions menu (three dots) for the cluster network, select Terminate .
- Confirm when prompted.

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/terminate.html)cluster-network terminate`command to delete a cluster network.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To delete a cluster network and all its resources, use the following API operation:
- [TerminateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/TerminateClusterNetwork)
