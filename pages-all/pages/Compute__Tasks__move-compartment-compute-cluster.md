# Moving a Compute Cluster to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm
- Fetched: 2026-09-05 01:52 CDT

# Moving a Compute Cluster to a Different Compartment

After you create a compute cluster, you can move it to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm#)
- 

- Navigate to the Compute Clusters list page. If you need help finding the list page, see[Listing Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/compute-clusters-list.htm).
- Select a compute cluster.
- Select the option you see:
- Actions then Move resource .
- Move resource .
- Choose the destination compartment from the list.
- Select Move resource .
- Optionally, move the instances and other resources that are associated with the compute cluster to the new compartment.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/change-compartment.html)compute-cluster change-compartment`command to move a compute cluster to another compartment:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move a compute cluster to a different compartment:
- [ChangeComputeClusterCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/ChangeComputeClusterCompartment)
