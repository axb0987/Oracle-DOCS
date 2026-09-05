# Listing Cluster Add-ons
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm
- Fetched: 2026-09-05 01:58 CDT

# Listing Cluster Add-ons

Find out how to list the cluster add-ons deployed on a cluster using Kubernetes Engine (OKE).

You can list the cluster add-ons deployed on a cluster using the Console, the CLI, and the API.

For more information about cluster add-ons, see[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-add-ons.htm#)
- 

- On the Clusters list page, select the name of the cluster on which the cluster add-ons are deployed. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- Select the Add-ons tab.

The cluster add-ons deployed on the cluster are shown.
- 

Use the[oci ce cluster list-addons](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/list-addons.html)command and required parameters to list the cluster add-ons deployed on a cluster:

```

```

Use the[oci ce addon-option list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/addon-option/list.html)command to:
- 

List available versions of all cluster add-ons supported on a given Kubernetes version:

```

```

where`<k8s-version>`is a Kubernetes version number in the format`x.y`(recommended) or`x.y.z`, where`x`is a major version,`y`is a minor version, and`z`is a patch version.

For example:

```

```

- 

List available versions of a cluster add-on supported on a given Kubernetes version:

```

```

where`<k8s-version>`is a Kubernetes version number in the format`x.y`(recommended) or`x.y.z`, where`x`is a major version,`y`is a minor version, and`z`is a patch version.

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListAddons](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/ListAddons)operation to list the cluster add-ons deployed on a cluster.

Run the[ListAddonOptions](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/AddonOptionSummary/ListAddonOptions)
