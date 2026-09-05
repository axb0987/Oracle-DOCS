# Getting a Cluster Add-on's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm
- Fetched: 2026-09-05 01:57 CDT

# Getting a Cluster Add-on's Details

Find out how to get details of a specific cluster add-on using Kubernetes Engine (OKE).

You can get details of a specific cluster add-on deployed on a cluster using the Console, the CLI, and the API.

For more information about cluster add-ons, see[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-add-on.htm#)
- 

To get details of a cluster add-on deployed on a cluster using the Console:
- On the Clusters list page, select the name of the cluster on which the cluster add-on is deployed. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Add-ons tab.

Detailed information about the enabled cluster add-ons deployed on the cluster are shown in tabular form.
- Select Manage add-ons , and then select the Edit option beside the cluster add-on that you want to get more detailed information about.
- 

Use the[oci ce cluster get-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/get-addon.html)command and required parameters to get details of a cluster add-on deployed on a cluster (for example, to verify successful deployment of a cluster add-on):

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/GetAddon)
