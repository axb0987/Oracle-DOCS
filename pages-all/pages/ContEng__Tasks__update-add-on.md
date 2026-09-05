# Updating a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm
- Fetched: 2026-09-05 01:58 CDT

# Updating a Cluster Add-on

Find out how to update a cluster add-on using Kubernetes Engine (OKE).

For specific instructions to update:
- the Cluster Autoscaler add-on, see[Updating the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Updating_Cluster_Autoscaler_Add-on)
- the Istio add-on, see[Updating the Istio Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on_topic-Updating_Cluster_Autoscaler_Add-on)
- the OCI native ingress controller add-on, see[Updating the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Updating)
- the Kubernetes Metrics Server add-on, see[Updating the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_updating)

You can use the API and the CLI to see a list of all versions of a particular cluster add-on (including version build numbers). Currently supported cluster add-on versions have a status of ACTIVE. Cluster add-on versions that are no longer supported have a status of DEPRECATED. Note that deprecated cluster add-on versions are only provided for exceptional circumstances (such as to perform a rollback). We recommend that you do not use a deprecated cluster add-on version, nor specify a particular build of a supported add-on version, for normal operations.

For more information about cluster add-ons, see[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#)
- 

To update the configuration of a cluster add-on deployed on an existing enhanced cluster using the Console:
- On the Clusters list page, select the name of the enhanced cluster on which the cluster add-on is deployed. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Add-ons tab, select Manage add-ons .
- Select the Edit option beside the deployed cluster add-on that you want to update.
- To update the configuration of the cluster add-on, specify the following details:
- Automatic updates: Choose this option when you want Oracle to automatically update the add-on when a new version becomes available.
- Choose a version: Choose this option when you want to control the version of the add-on that Oracle deploys on the cluster. A warning indicates that you have taken responsibility for updating the add-on. If you choose this option, select the version of the add-on to deploy on the cluster from the Version list. See[Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm).
- Option: and Value: (optional) Select Add configuration to specify one or more key/value pairs to pass as arguments to the cluster add-on. For example, for the Kubernetes Dashboard, you might select the`numOfReplicas`option, and specify a value of`3`. See[Cluster Add-on Configuration Arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm).
- Select Save changes .
- 

Use the[oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html)command and required parameters to update a cluster add-on deployed on a cluster:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateAddon)
