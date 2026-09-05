# Working with the Kubernetes Metrics Server as a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with the Kubernetes Metrics Server as a Cluster Add-on

Find out how to use the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine (OKE).

Using the Kubernetes Metrics Server as a cluster add-on rather than as a standalone program simplifies configuration and ongoing maintenance. You can more simply:
- Enable or disable the Kubernetes Metrics Server.
- Opt into, and out of, automatic updates by Oracle.
- Select Kubernetes Metrics Server add-on versions.
- Manage add-on specific customizations using approved key/value pair configuration arguments.

To use the Kubernetes Metrics Server as a cluster add-on, you also have to deploy cert-manager. You can deploy cert-manager in two ways:
- You can deploy cert-manager as an open-source standalone product. If you deploy cert-manager as a standalone product, set the`skipAddonDependenciesCheck`configuration argument to`true`. For more information about cert-manager, see the[cert-manager.io documentation](https://cert-manager.io/docs/).
- You can deploy cert-manager as a cluster add-on. For more information about deploying cert-manager as a cluster add-on, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).

These sections describe how to work with the Kubernetes Metrics Server add-on:
- [Deploying the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying)
- [Updating the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_updating)
- [Disabling (and Removing) the Kubernetes Metrics Server Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_disabling-removing)

## Deploying the Kubernetes Metrics Server as a Cluster Add-on

Find out how to use kubectl to deploy the Kubernetes Metrics Server as a cluster add-on on clusters with managed node pools that you've created using Kubernetes Engine (OKE).

These instructions describe how to deploy the Kubernetes Metrics Server as a cluster add-on:
- [Step 1: Create the Kubernetes Metrics Server add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying__section_create-config-file)
- [Step 2: Deploy the Kubernetes Metrics Server add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm#contengworkingwithmetricsserver_cluster-add-on_deploying__section_deploy)

### Step 1: Create the Kubernetes Metrics Server add-on configuration file
Note  
  

These instructions describe how to create a Kubernetes Metrics Server add-on configuration file to enable you to deploy the Kubernetes Metrics Server add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the Kubernetes Metrics Server add-on, in which case you specify configuration arguments in the UI. For more information about deploying the Kubernetes Metrics Server add-on using the Console, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).
- 

In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called`enablemetrics-server.json`) containing the following:
```

```

This content is sufficient to enable the Kubernetes Metrics Server add-on.
- 

(Optional) In the`enablemetrics-server.json`file you created, specify other configuration arguments to customize the Kubernetes Metrics Server add-on. For information about the configuration arguments you can set, see[Kubernetes Metrics Server](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm).
- Save and close the`enablemetrics-server.json`file.

### Step 2: Deploy the Kubernetes Metrics Server add-on on the cluster and confirm successful deployment
Note  
  

These instructions describe how to deploy the Kubernetes Metrics Server add-on on clusters with managed node pools, using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Confirm that the Kubernetes Metrics Server add-on has not already been installed on the cluster by entering:
```

```

where`<cluster-ocid>`is the OCID of the cluster on which you want to deploy the Kubernetes Metrics Server add-on.
- If your Oracle Cloud Infrastructure user is a tenancy administrator or cluster administrator, skip the next step and go straight to the following step.
- If your Oracle Cloud Infrastructure user is not a tenancy administrator or cluster administrator, ask a tenancy administrator or cluster administrator to grant your user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:

```

```

For more information, see[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutaccesscontrol.htm).
- 

Deploy the Kubernetes Metrics Server add-on on the cluster by entering:
```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to deploy the Kubernetes Metrics Server add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the Kubernetes Metrics Server add-on configuration file you created earlier. For example,`--from-json file://./enablemetrics-server.json`

For example:
```

```

A work request is created to deploy the Kubernetes Metrics Server add-on.
- 

Confirm that the Kubernetes Metrics Server has been deployed successfully and is available by entering:

```

```

## Updating the Kubernetes Metrics Server Add-on

Note  
  

These instructions describe how to update the Kubernetes Metrics Server add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm).
- 

Open the Kubernetes Metrics Server add-on configuration file in a suitable editor
- 

Add, remove, or change configuration parameters in the configuration file as required. For information about the parameters you can set, see[Kubernetes Metrics Server](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-metrics-server.htm).
- Update the Kubernetes Metrics Server add-on using the[oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to update the Kubernetes Metrics Server add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the Kubernetes Metrics Server add-on configuration file to use when updating the add-on. For example,`--from-json file://./ enablemetrics-server.json`

For example:

```

```

A work request is created to update the Kubernetes resources required by the Kubernetes Metrics Server.
- Optional: View the status of the Kubernetes Metrics Server pods to observe progress, by entering:
```

```

## Disabling (and Removing) the Kubernetes Metrics Server Add-on

Note  
  

These instructions describe how to disable and remove the Kubernetes Metrics Server add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm).
- 

Disable (and optionally remove) the Kubernetes Metrics Server add-on using the[oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to disable (and optionally remove) the Kubernetes Metrics Server add-on.
- `--is-remove-existing-add-on <true|false>`specifies either to completely remove the Kubernetes Metrics Server add-on (when set to`true`), or to not remove the add-on but simply disable it and not use it (when set to`false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available.

For example:

```

```

A work request is created to disable (and optionally remove) the Kubernetes Metrics Server.
- Optional: View the status of the Kubernetes Metrics Server pods to observe progress, by entering:
```

```
