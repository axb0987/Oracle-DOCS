# Updating the Instance Configuration for a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm
- Fetched: 2026-09-05 01:52 CDT

# Updating the Instance Configuration for a Cluster Network with Instance Pools

Update the instance configuration that a cluster network's underlying instance pool uses when creating instances.

To update the instance configuration for a cluster network, do either of the following:
- 

[Create a new instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)with the settings you want and then attach the new instance configuration to the cluster network.

If you want the instances in the cluster network to use the settings from the new instance configuration, such as a new shape, then[detach the existing instances from the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)and provision new instances.
Note  
  
When you detach instances from a cluster network, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the cluster network before detaching instances.
- If you only want to update the display name or tags of an existing instance configuration, you can[update the cluster network's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm). For any other updates, create and then attach the new instance configuration with the settings that you want to use.
Note  
  
For information about permissions and prerequisites, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-iam)and[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-prerequisites).

To update the instance configuration that a cluster network uses, first you[create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)with the settings that you want (if such a configuration doesn't already exist), and then you attach the new instance configuration to the cluster network, as described in the following steps.
If you want the instances in the cluster network to use the settings from the new instance configuration, such as a new shape, then[detach the existing instances from the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)and provision new instances.
Note  
  
When you detach instances from a cluster network, the existing instances are detached before new instances are provisioned. Depending on your requirements, you might want to increase the size of the cluster network before detaching instances.

If you only want to update the display name or tags of an existing instance configuration, then you can[update the cluster network's existing instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm). For any other updates, create and then attach the new instance configuration with the settings that you want to use.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm#)
- 

To attach a new instance configuration to a cluster network:
- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select a cluster network.
- Select Edit .
- Instance configuration: Select the instance configuration to use when creating instances in the cluster network's instance pool.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/update.html)cluster-network update`command to update the instance configuration used by a cluster network:
```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To update the instance configuration used by a cluster network, use the following API operation:
- [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork)
