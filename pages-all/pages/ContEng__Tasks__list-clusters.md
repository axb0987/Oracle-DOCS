# Listing Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm
- Fetched: 2026-09-05 01:58 CDT

# Listing Clusters

Find out how to list clusters using Kubernetes Engine (OKE).

You can list clusters using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm#)
- 

- Open the navigation menu and select Developer Services . Under Containers &amp; Artifacts , select Kubernetes Clusters (OKE) .

The Clusters list page appears. All Kubernetes clusters in the selected compartment are displayed in a table.
- To view the Kubernetes clusters in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
- To see more detail about an individual cluster, select the name of the cluster on the Clusters list page to show the details page.
- 

Use the[oci ce cluster list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/list.html)command and required parameters to list clusters:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListClusters](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/ClusterSummary/ListClusters)
