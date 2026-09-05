# Installing the OCI Native Ingress Controller as a Cluster Add-on
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm
- Fetched: 2026-09-05 01:56 CDT

# Installing the OCI Native Ingress Controller as a Cluster Add-on

Find out how to install the OCI native ingress controller as a cluster add-on.

When you have completed the prerequisites, you can deploy the OCI native ingress controller as a cluster add-on. See[Deploying the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying).

Note that having installed the OCI native ingress controller cluster add-on, before you can use it you also have to create the necessary Kubernetes ingress-related resources. See[Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm)

## Deploying the OCI Native Ingress Controller Add-on

The instructions in the steps below describe how to deploy the OCI native ingress controller as a cluster add-on (the 'OCI native ingress controller add-on') to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
- [Step 1: Create the OCI native ingress controller add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying__section_create-config-file)
- [Step 2: Deploy the OCI native ingress controller add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-Deploying__section_deploy-native-ingress-controller)

### Step 1: Create the OCI native ingress controller add-on configuration file
Note  
  

These instructions describe how to create an OCI native ingress controller add-on configuration file to enable you to deploy the OCI native ingress controller add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the OCI native ingress controller add-on, in which case you specify configuration arguments in the UI. For more information about deploying the OCI native ingress controller add-on using the Console, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).
- 

In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called`native-ingress-controller-addon.json`) containing the following:
```

```

where:
- `<compartment-id>`is the OCID of the compartment in which the OCI native ingress controller is to create the OCI load balancer and certificate.
- `<load-balancer-subnet-ocid>`is the OCID of the load balancer's subnet.

For example:
```

```

- In the`native-ingress-controller-addon.json`file you just created, use the`authType`parameter to specify how you have set up the OCI native ingress controller to access OCI services and resources:
- If you have set up an instance principal to enable the OCI native ingress controller to access OCI services and resources, set the`authType`parameter to`instance`.
- If you have set up a workload identity principal to enable the OCI native ingress controller to access OCI services and resources, set the`authType`parameter to`workloadIdentity`.
- If you have set up a user principal to enable the OCI native ingress controller to access OCI services and resources, set the`authType`parameter to`user`.

For example:

```

```

Note that`instance`is the default value of the`authType`parameter, so if you do not explicitly specify a value for`authType`, the OCI native ingress controller uses the identity of the instance on which it is running to access OCI services and resources. For more information, see[Setting Up an Instance Principal, User Principal, or Workload Identity Principal to Enable Access to OCI Services and Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-auth).
- In the`native-ingress-controller-addon.json`file you created, specify other parameters for the OCI native ingress controller. For information about the parameters you can set, see[OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/configuration-arguments-nic.htm).

For example:
```

```

- Save and close the`native-ingress-controller-addon.json`file.

### Step 2: Deploy the OCI native ingress controller add-on on the cluster and confirm successful deployment
Note  
  

These instructions describe how to deploy the OCI native ingress controller add-on using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Confirm that the OCI native ingress controller add-on has not already been installed on the cluster by entering:
```

```

where`<cluster-ocid>`is the OCID of the cluster on which you want to deploy the OCI native ingress controller add-on.
- 

Deploy the OCI native ingress controller add-on on the cluster by entering:
```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to deploy the OCI native ingress controller add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the OCI native ingress controller add-on configuration file you created earlier. For example,`--from-json file://./native-ingress-controller-addon.json`

For example:
```

```

A work request is created to deploy the OCI native ingress controller add-on.
- 

Confirm successful deployment of the OCI native ingress controller add-on by entering:
```

```

Assuming successful deployment, the output shows the OCI native ingress controller add-on with a lifecycle-state of ACTIVE. For example:
```

```

## Updating the OCI Native Ingress Controller Add-on

Note  
  

These instructions describe how to update the OCI native ingress controller add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm).
- 

Open the OCI native ingress controller add-on configuration file in a suitable editor.
- 

Add, remove, or change configuration arguments in the configuration file as required. For information about the arguments you can set, see[Installing the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm).
- Update the OCI native ingress controller add-on using the[oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to update the OCI native ingress controller add-on.
- `--from-json file://<path-to-config-file>`specifies the location of the OCI native ingress controller add-on configuration file to use when updating the add-on. For example,`--from-json file://./native-ingress-controller-addon.json`

For example:

```

```

A work request is created to update the OCI native ingress controller add-on.

## Disabling (and Removing) the OCI Native Ingress Controller Add-on

Note  
  

These instructions describe how to disable and remove the OCI native ingress controller add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see[Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm).
- 

Disable (and optionally remove) the OCI native ingress controller add-on using the[oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html)command, by entering:

```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to disable (and optionally remove) the OCI native ingress controller add-on.
- `--is-remove-existing-add-on <true|false>`specifies either to completely remove the OCI native ingress controller add-on (when set to`true`), or to not remove the add-on but simply disable it and not use it (when set to`false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available.

For example:

```

```

A work request is created to disable (and optionally remove) the OCI native ingress controller add-on.
- (Optional) Remove Kubernetes ingress-related resources (such as the IngressClassParameters, IngressClass, and Ingress resources), which aren't managed by the OCI native ingress controller add-on, using the`kubectl delete`
