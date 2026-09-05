# Disabling (and Removing) a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm
- Fetched: 2026-09-05 01:57 CDT

# Disabling (and Removing) a Cluster Add-on

Find out how to disable (and remove) a cluster add-on using Kubernetes Engine (OKE).

You can disable a cluster add-on deployed on a cluster using the Console, the CLI, and the API. If you also want to remove the cluster add-on from the cluster, use the CLI or the API.

For specific instructions to disable (and remove):
- the Cluster Autoscaler add-on, see[Disabling (and Removing) the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Disabling_Removing_Cluster_Autoscaler_Add-on)
- the Istio add-on, see[Disabling (and Removing) the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Disabling_Removing_Istio_Add-on)
- the OCI native ingress controller add-on, see[Disabling (and Removing) the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Disabling_Removing)
- the Kubernetes Metrics Server add-on, see[Disabling (and Removing) the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_disabling-removing)

For more information about cluster add-ons, see[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#)
- 

- On the Clusters list page, select the name of the cluster on which the cluster add-on is deployed. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Add-ons tab, select Manage add-ons .
- Select the Edit option beside the cluster add-on that you want to disable.
- De-select the Enable &lt;add-on name&gt; option.

If you disable an essential cluster add-on, a warning indicates that you have taken responsibility for deploying and configuring an alternative add-on to provide equivalent functionality.
- Select Save changes .

The cluster add-on is disabled, but not removed from the cluster. To completely remove the add-on, use the CLI or the API.
- 

Use the[oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html)command and required parameters to disable (and optionally remove) a cluster-add-on deployed on a cluster:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DisableAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DisableAddon)
