# Attaching Instances to a Compute Cluster
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm
- Fetched: 2026-09-05 01:49 CDT

# Attaching Instances to a Compute Cluster

After you create a compute cluster, you can create instances within the cluster. The instances must be in the same compartment and availability domain as the cluster.

For steps to create a compute cluster, see[Creating a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm).

When you use the API, SDKs, or CLI to create instances in a compute cluster, provide the compute cluster's OCID with the`launch instance`operation. For steps to find the OCID of a compute cluster, see[Retrieving a Compute Cluster's OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-ocid-compute-cluster.htm).

If the placement ([Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)and[Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)) of the compute cluster doesn't have enough capacity for the instances that you create, you might get an out of capacity error. If that occurs, create a compute cluster in a different placement, and launch instances into the new compute cluster.

To remove instances from a compute cluster,[delete (terminate) the instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm).

For information about required IAM policies, see[Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters-permissions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm#)
- 

- Navigate to the Compute Clusters list page. If you need help finding the list page, see[Listing Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/compute-clusters-list.htm).
- Select a compute cluster.
- Select Attach instance .
- Follow the steps to[create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm), with the following specific choices for this instance.
- In the Placement section, select Show advanced options .
- For Capacity type , ensure Compute cluster is selected. In the Compute cluster list, confirm that your compute cluster is selected.
- In the Image and shape section, select Change shape . Select Bare metal machine , and then select a[shape that supports compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-cluster-shapes).
- Complete the steps to configure the instance.
- Select Create .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)instance launch`command and required parameters to create an instance in a compute cluster:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to get attach an instance to a compute cluster:
- [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance).
- Pass the OCID of the compute cluster in the`computeClusterId`parameter in[LaunchInstanceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LaunchInstanceDetails)
