# Moving a Cluster Network
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-move.htm
- Fetched: 2026-09-05 01:50 CDT

# Moving a Cluster Network

Move a Compute cluster network with instance pools into a different compartment within the same tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-move.htm#)
- 

- Navigate to the Compute Cluster networks list page. If you need help finding the list page, see[Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/cluster-networks-list.htm).
- To view the cluster networks in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- Select the cluster network.
- Select the option you see:
- Actions then Move resource .
- Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[cluster-network change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/change-compartment.html)command and required parameters to move a cluster network with instance pools to another compartment:

```

```

Or use a JSON file to set parameters:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to move a cluster network with instance pools to another compartment:
- [ChangeClusterNetworkCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/ChangeClusterNetworkCompartment)
