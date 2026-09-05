# Renaming a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm
- Fetched: 2026-09-05 01:51 CDT

# Renaming a Cluster Network with Instance Pools

Edit a cluster network with instance pools to give it a new name.
Note  
  
For information about permissions and prerequisites, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-iam)and[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-prerequisites).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm#)
- 

- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select a cluster network.
- Select Edit .
- Enter a new name. Avoid entering confidential information.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/update.html)cluster-network update`command to rename a cluster network.
```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To rename a cluster network, use the following API operation:
- [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork)
