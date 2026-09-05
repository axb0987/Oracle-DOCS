# Creating a Cluster Network with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating a Cluster Network with Instance Pools

Create a cluster network with instance pools.

Cluster networks are built on top of the[instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instance-pools.htm)feature. Most operations in the instance pool are managed directly by the cluster network, though you can resize the underlying instance pool, change the instance configuration that the pool uses to create new instances, monitor the pool, and add tags. For background information, see[Cluster Networks with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm).
Tip  
  
If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, then use[compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/compute-clusters.htm)instead.
Note  
  
For information about permissions and prerequisites, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-iam)and[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/managingclusternetworks.htm#cluster-networks-prerequisites).

To determine whether capacity is available for a specific shape before you create a cluster network, use the[CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport)operation.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm#)
- 

- Navigate to the Compute Cluster Networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- Select Create cluster network .
- Name : Accept the default name or enter a name for the cluster network. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Compartment : Select the compartment in which to create the cluster network.
- (Optional) Select Show tagging options to add tags to the cluster network. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
Note  
  
This option might appear at the bottom of the page.
- Availability Domain : Select the availability domain in which to run the cluster network. You can select only the availability domains that have hardware that supports cluster networks.
- Configure networking : Specify the network that you want to use to administer the cluster network. This network is separate from the closed RDMA network between nodes within the cluster. Enter the following information:
- Virtual cloud network : Select the virtual cloud network (VCN) for the cluster network. Change the compartment if needed.
- Subnet : Select the subnet for the cluster network. Change the compartment if needed.
- Configure instance pool : Enter the following information:
- Instance pool name : A name for the instance pool that is managed by the cluster network. Change the compartment if needed. Avoid entering confidential information.
- Number of instances : Select the number of instances in the pool.
- Instance configuration : Select the instance configuration to use when creating instances in the cluster network's instance pool, as described in the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#cluster-networks-prerequisites). Change the compartment if needed.
- Select Create cluster network .

Instances are provisioned until the required number of instances in the pool are launched, subject to the host capacity for nodes in the cluster's RDMA network.

Tip  
  
To track the progress of the operation and[troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-work-requests)that occur during instance creation, use the associated[work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/create.html)cluster-network create`command and required parameters to create a cluster network.

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create a cluster network:
- [CreateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/CreateClusterNetwork)
