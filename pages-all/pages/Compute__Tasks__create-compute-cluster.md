# Creating a Compute Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm
- Fetched: 2026-09-05 01:50 CDT

# Creating a Compute Cluster

When you first create a compute cluster, you create an empty RDMA network group. After the compute cluster is created, you can create instances in the compute cluster.

For steps to create instances, See[Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm).

For information about required IAM policies, see[Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters-permissions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm#)
- 

- Navigate to the Compute Clusters list page. If you need help finding the list page, see[Listing Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/compute-clusters-list.htm).
- Select Create compute cluster .
- Fill out the cluster information:
- Name: Enter a name for the compute cluster. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
- Compartment: Select the compartment to create the compute cluster in.
- Availability Domain: Select the availability domain to run the compute cluster in. Only availability domains with hardware that supports compute clusters are listed.
- (Optional) Select Advanced options and navigate to Tags .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select the button you see:
- Submit
- Create

The cluster is created.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/create.html)compute-cluster create`command:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to create a compute cluster:
- [CreateComputeCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/CreateComputeCluster)
