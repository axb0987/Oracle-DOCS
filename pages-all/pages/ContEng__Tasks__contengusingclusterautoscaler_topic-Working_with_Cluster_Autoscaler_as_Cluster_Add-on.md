# Working with the Cluster Autoscaler as a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with the Cluster Autoscaler as a Cluster Add-on

Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a cluster add-on to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine (OKE).

Using the Kubernetes Cluster Autoscaler as a cluster add-on (the 'Cluster Autoscaler add-on') rather than as a standalone program simplifies configuration and ongoing maintenance. You can more simply:
- Enable or disable the Cluster Autoscaler.
- Opt into, and out of, automatic updates by Oracle.
- Select Cluster Autoscaler add-on versions.
- Manage add-on specific customizations using approved key/value pair configuration arguments.

These sections describe how to work with the Cluster Autoscaler add-on to manage node pools:
- [Deploying the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on)
- [Updating the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Updating_Cluster_Autoscaler_Add-on)
- [Disabling (and Removing) the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Disabling_Removing_Cluster_Autoscaler_Add-on)

## Deploying the Cluster Autoscaler Add-on

The instructions below describe how to deploy the Kubernetes Cluster Autoscaler as a cluster add-on (the 'Cluster Autoscaler add-on') to manage node pools:
- [Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-setup-access)
- [Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file)
- [Step 3: Deploy the Cluster Autoscaler add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-deploy-CA-addon)
- [Step 4: View the Scaling Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-view-scaling)
- [Step 5: Clean Up](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-clean-up)

### Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools

To manage node pools, the Kubernetes Cluster Autoscaler performs actions on other Oracle Cloud Infrastructure service resources. To perform those actions on OCI service resources, the Kubernetes Cluster Autoscaler uses the credentials of an authorized actor (or principal). You can currently set up the following types of principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources:
- Instance principal: The Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running.
- Workload identity principal: The Kubernetes Cluster Autoscaler uses the identity of a workload resource running on a Kubernetes cluster.

Note the use of workload identity principals to enable the Kubernetes Cluster Autoscaler to access OCI services and resources:
- is supported with enhanced clusters, but not with basic clusters.
- is only supported with Cluster Autoscaler version 1.26 (or later)

#### Using instance principals to enable the Cluster Autoscaler add-on to access node pools

You can set up an instance principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources.

To set up an instance principal:
- Log in to the Console.
- 

Create a new compartment-level dynamic group in the compartment to which the cluster belongs, containing the worker nodes (compute instances) in the cluster:
- Follow the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To)in the IAM documentation, and give the new dynamic group a name (for example,`acme-oke-cluster-autoscaler-dyn-grp`).
- 

Enter a rule that includes the worker nodes in the compartment, in the format:

```

```

where`<compartment-ocid>`is the OCID of the compartment to which the cluster belongs.

For example:

```

```

- 

Create a policy to allow worker nodes to manage node pools:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-cluster-autoscaler-dyn-grp-policy`).
- 

Enter a policy statement to allow worker nodes to manage node pools (along with other policy statements related to initializing worker nodes), in the format:

```

```

where:
- `<dynamic-group-name>`is the name of the dynamic group you created earlier. For example,`acme-oke-cluster-autoscaler-dyn-grp`. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format`dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format`dynamic-group id <dynamic-group-ocid>`.
- `<compartment-name>`is the name of the compartment to which the cluster belongs. For example,`acme-oke-cluster-autoscaler-compartment`

For example:

```

```

Note  
  

If a node pool belongs to one compartment, and the network resources used by the node pool belong to a different compartment, you have to create policies in both compartments as follows:
- 

In the node pool's compartment, create a policy with policy statements in the following format:

```

```

- 

In the network resources' compartment, create a policy with policy statements in the following format:

```

```

Note that before you deploy the Cluster Autoscaler add-on, you will indicate that you want the Cluster Autoscaler add-on to access node pools using instance principals by setting the`authType`parameter to`instance`in the configuration file. See[Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file).

#### Using workload identity principals to enable the Cluster Autoscaler add-on to access to node pools

You can set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources. Note that you can only use workload identity principals with enhanced clusters.

To set up a workload identity principal:
- Obtain the OCID of the cluster (for example, using the Cluster details tab in the Console).
- Follow the instructions in[Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm)in the IAM documentation, and give the new policy a name (for example,`acme-oke-cluster-autoscaler-policy`).
- 

Enter policy statements to allow node pool management, in the format:

```

```

where:
- `<compartment-name>`is the name of the compartment to which the cluster belongs. For example,`acme-oke-cluster-autoscaler-compartment`
- `<cluster-ocid>`is the cluster's OCID that you obtained previously.

For example:

```

```

Note  
  

If a node pool belongs to one compartment, and the network resources used by the node pool belong to a different compartment, you have to create policies in both compartments as follows:
- 

In the node pool's compartment, create a policy with policy statements in the following format:

```

```

- 

In the network resources' compartment, create a policy with policy statements in the following format:

```

```

Note that before you deploy the Cluster Autoscaler add-on, you will indicate that you want the Cluster Autoscaler add-on to access node pools using workload identity principals by setting the`authType`parameter to`workload`in the configuration file. See[Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file).

### Step 2: Create the Cluster Autoscaler Add-on configuration file

Note  
  

These instructions describe how to create a Cluster Autoscaler add-on configuration file to enable you to deploy the Cluster Autoscaler add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the Cluster Autoscaler add-on, in which case you specify configuration arguments in the UI. For more information about deploying the Cluster Autoscaler add-on using the Console, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).

#### Step 2a: Create the configuration file
- 

In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called`cluster-autoscaler-add-on.json`) containing the following:
```

```

- Save the`cluster-autoscaler-add-on.json`file you created.

#### Step 2b: Specify the node pools to manage

In the`cluster-autoscaler-add-on.json`file you created, specify the cluster's node pools that you want the Kubernetes Cluster Autoscaler to manage.

You can specify that you want the Kubernetes Cluster Autoscaler to manage a single node pool, or multiple node pools. The recommendation is to always have at least one node pool that is not managed by the Kubernetes Cluster Autoscaler to run critcal cluster add-ons, and to ensure the Kubernetes Cluster Autoscaler does not scale down the nodes on which it is running. Also note that it is your responsibility to manually scale any node pools you do not specify in the configuration file.

You specify the node pools that you want the Kubernetes Cluster Autoscaler to manage in one of two ways:
- You can explicitly specify each node pool to manage, using the`nodes`parameter to specify each node pool's OCID.
- You can specify that the Kubernetes Cluster Autoscaler is to discover which node pool (or node pools) to manage, using the`nodeGroupAutoDiscovery`parameter to specify the tags to match. You can specify both defined tags and freeform tags (for more information about adding tags to node pools, see[Applying Tags to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-pool-tags.htm)). The Kubernetes Cluster Autoscaler manages node pools with tags that match the tags you specify. Note that the`nodeGroupAutoDiscovery`parameter is supported with Cluster Autoscaler version 1.30.3, version 1.31.1, version 1.32.0, and later.

Note that you cannot specify both the`nodes`parameter and the`nodeGroupAutoDiscovery`parameter in the same`cluster-autoscaler-add-on.json`file. The two parameters are mutually exclusive alternatives.

To use the`nodes`parameter to explicitly specify which node pools to manage:
- 

In the`cluster-autoscaler-add-on.json`file, locate the following template lines:

```

```

The`nodes`parameter value has the following format:
```

```

where:
- `<min-nodes>`is the minimum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number.
- `<max-nodes>`is the maximum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool.
- `<nodepool-ocid>`is the OCID of the node pool to manage.
- 

Change the value of the`nodes`parameter to specify:
- The minimum number of nodes allowed in the node pool. For example, 1.
- The maximum number of nodes allowed in the node pool. For example, 5.
- The OCID of the node pool you want the Kubernetes Cluster Autoscaler to manage.

For example:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage a second node pool in the cluster, append appropriate details for the second node pool to the value of the`nodes`parameter. For example:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage more node pools, append appropriate details to the value of the`nodes`parameter.
- Save the`cluster-autoscaler-add-on.json`file.

To use the`nodeGroupAutoDiscovery`parameter to specify that the Kubernetes Cluster Autoscaler is to discover which node pools to manage, based on matching tags:
- 

In the`cluster-autoscaler-add-on.json`file you created, locate the following template lines:

```

```

- 

Delete the lines specifying the`nodes`parameter, and replace them with the following lines:

```

```

The`nodeGroupAutoDiscovery`parameter value has the following format:
```

```

where:
- `<compartment-ocid>`is the OCID of the compartment in which the node pool, or node pools, are located.
- `{{<tagKey1>}}={{<tagValue1>}}`specifies the name of the first tag to match, and the value of that tag to match.
- `{{<tagKey2>}}={{<tagValue2>}}`optionally specifies the name of a second tag to match, and the value of that tag to match. You can specify as many tags as required (you are not limited to two). If you specify multiple tags, then all tags have to match.
- `min:{{<min-nodes>}}`specifies the minimum number of nodes allowed in all matching node pools. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number. Note that at any time, you can override the value of`min:{{<min-nodes>}}`for a particular node pool by applying the`minSize`node pool tag to that node pool. The`minSize`node pool tag always takes precedence over`min:{{<min-nodes>}}`.
- `max:{{<max-nodes>}}`specifies the maximum number of nodes allowed in all matching node pools. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool. Note that at any time, you can override the value of`max:{{<max-nodes>}}`for a particular node pool by applying the`maxSize`node pool tag to that node pool. The`maxSize`node pool tag always takes precedence over`max:{{<max-nodes>}}`.
- 

Change the value of the`nodeGroupAutoDiscovery`parameter to specify:
- The OCID of the compartment in which the node pool is located.
- One or more tag names and tag values to match.
- The minimum number of nodes allowed in matching node pools. For example, 1.
- The maximum number of nodes allowed in matching node pools. For example, 5.

For example:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage more node pools, in different compartments, or with different tag names and tag values, or with different minimum and maximum numbers of allowed nodes, append appropriate details to the value of the`nodeGroupAutoDiscovery`parameter, separated by a semi-colon.

For example:

```

```

- Save the`cluster-autoscaler-add-on.json`file.

#### Step 2c: Include additional configuration settings

- 

In the`cluster-autoscaler-add-on.json`file you created, use the`authType`parameter to specify how you have set up Kubernetes Cluster Autoscaler to access OCI services and resources:
- If you have set up an instance principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, set the`authType`parameter to`instance`.
- If you have set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, set the`authType`parameter to`workload`.

For example:

```

```

Note that`instance`is the default value of the`authType`parameter, so if you do not explicitly specify a value for`authType`, the Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running to access OCI services and resources. For more information, see[Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-setup-access).
- 

In the`cluster-autoscaler-add-on.json`file you created, specify other parameters for the Kubernetes Cluster Autoscaler. For information about the parameters you can set, see[Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).

For example:
```

```

- Save and close the`cluster-autoscaler-add-on.json`file.

### Step 3: Deploy the Cluster Autoscaler add-on on the cluster and confirm successful deployment

Note  
  

These instructions describe how to deploy the Cluster Autoscaler add-on using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Confirm that the Cluster Autoscaler add-on has not already been installed on the cluster by entering:
```

```

where`<cluster-ocid>`is the OCID of the cluster on which you want to deploy the Cluster Autoscaler add-on.
- 

Deploy the Cluster Autoscaler add-on on the cluster by entering:
```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to deploy the Cluster Autoscaler add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the Cluster Autoscaler add-on configuration file to use when deploying the add-on. For example,`--from-json file://./cluster-autoscaler-add-on.json`

For example:
```

```

A work request is created to install the Kubernetes resources required by the Kubernetes Cluster Autoscaler on the cluster.
- Optional: View the status of the Kubernetes Cluster Autoscaler pods to observe progress of the deployment, by entering:
```

```

- View the Kubernetes Cluster Autoscaler logs to confirm that the add-on was successfully deployed and is currently monitoring the workload of node pools in the cluster, by entering:
```

```

### Step 4: View the Scaling Operation

You can watch the Kubernetes Cluster Autoscaler you have deployed as it automatically scales worker nodes in a node pool. To make the scaling operation more obvious, consider the following suggestions (note these are for observation purposes only, and might be contrary to recommendations shown in[Recommendations when using the Kubernetes Cluster Autoscaler in Production Environments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_recommendations)):
- Observe a cluster that has a single node pool (the node pool being managed by the Kubernetes Cluster Autoscaler).
- If the cluster you want to observe has more than one node pool, restrict pods to running on nodes on the single node pool being managed by the Kubernetes Cluster Autoscaler. See[Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)in the Kubernetes documentation.
- Start with one node in the node pool being managed by the Kubernetes Cluster Autoscaler.
- In the Kubernetes Cluster Autoscaler configuration file, you specify the maximum number of nodes allowed in the node pool. Make sure the maximum number of nodes you specify does not exceed the tenancy limit for the worker node shape defined for the node pool.

To view the Kubernetes Cluster Autoscaler automatically scaling worker nodes:
- Confirm the current total number of worker nodes in the cluster by entering:
```

```

- 

Define a sample Nginx application by creating a file called`nginx.yaml`in a text editor, with the following content:

```

```

Notice that a resource request limit has been set.
- Deploy the sample application by entering:
```

```

- Increase the number of pods in the deployment to 100 (from 2) by entering:
```

```

The Kubernetes Cluster Autoscaler now adds worker nodes to the node pool to meet the increased workload.
- Observe the status of the deployment by entering:
```

```

- After a few minutes, view the increased total number of worker nodes in the cluster by entering:
```

```

Note that the number of worker nodes that you see will depend on the worker node shape and the maximum number of nodes specified in the Kubernetes Cluster Autoscaler configuration file.

### Step 5: Clean Up

- Delete the sample Nginx application by entering:
```

```

- After ten minutes, confirm that the worker nodes have reduced to the original number, by entering:
```

```

Note that after deleting the sample Nginx application and waiting, you might see fewer worker nodes but still more than the original number. This is probably because kube-system pods have been scheduled to run on those nodes. kube-system pods can prevent the Kubernetes Cluster Autoscaler from removing nodes because the Autoscaler's`skip-nodes-with-system-pods`parameter is set to`true`by default.

## Updating the Cluster Autoscaler Add-on

Note  
  

These instructions describe how to update the Cluster Autoscaler add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm).
- 

Open the Cluster Autoscaler add-on configuration file in a suitable editor
- 

Add, remove, or change configuration parameters in the configuration file as required. For information about the parameters you can set, see[Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).
- Update the Cluster Autoscaler add-on using the[oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to update the Cluster Autoscaler add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the Cluster Autoscaler add-on configuration file to use when updating the add-on. For example,`--from-json file://./cluster-autoscaler-add-on.json`

For example:

```

```

A work request is created to update the Kubernetes resources required by the Kubernetes Cluster Autoscaler.
- Optional: View the status of the Kubernetes Cluster Autoscaler pods to observe progress, by entering:
```

```

## Disabling (and Removing) the Cluster Autoscaler Add-on

Note  
  

These instructions describe how to disable and remove the Cluster Autoscaler add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm).
- 

Disable (and optionally remove) the Cluster Autoscaler add-on using the[oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to disable (and optionally remove) the Cluster Autoscaler add-on.
- `--is-remove-existing-add-on <true|false>`specifies either to completely remove the Cluster Autoscaler add-on (when set to`true`), or to not remove the add-on but simply disable it and not use it (when set to`false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available.

For example:

```

```

A work request is created to disable (and optionally remove) the Kubernetes Cluster Autoscaler.
- Optional: View the status of the Kubernetes Cluster Autoscaler pods to observe progress, by entering:
```

```
