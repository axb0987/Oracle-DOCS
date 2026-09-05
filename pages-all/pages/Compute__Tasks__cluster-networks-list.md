# Listing Cluster Networks
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-list.htm
- Fetched: 2026-09-05 01:50 CDT

# Listing Cluster Networks

Get a list of the Compute cluster networks in an Oracle Cloud Infrastructure compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-list.htm#)
- 

- 

Open the navigation menu and select Compute . Under Compute , select Cluster Networks .

The Cluster Networks list page opens. All existing cluster networks in the selected compartment are displayed in a list table.
- 

To view the resources in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

Optionally, you can do the following from the list.
- Select a cluster network to view the details page.
- For a cluster network, from the Actions menu (three dots), edit the configuration, move the cluster to another compartment, or terminate the cluster network.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/list.html)cluster-network list`command and required parameters to list cluster networks:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to list cluster networks:
- [ListClusterNetworks](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/ListClusterNetworks)
