# Working with the Cluster Autoscaler as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with the Cluster Autoscaler as a Standalone Program

Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a standalone program to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine (OKE).

Using the Kubernetes Cluster Autoscaler as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
- Installing a version of the Kubernetes Cluster Autoscaler that is compatible with the version of Kubernetes running on the cluster.
- Specifying configuration arguments correctly.
- Manually upgrading the Kubernetes Cluster Autoscaler when you upgrade a cluster to a new version of Kubernetes, to ensure the Kubernetes Cluster Autoscaler is compatible with the cluster's new Kubernetes version.

The instructions below describe how to run the Kubernetes Cluster Autoscaler as a standalone program to manage node pools:
- [Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable Cluster Autoscaler Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-setup-access)
- [Step 2: Copy and customize the Cluster Autoscaler configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-copy-CA-config-file)
- [Step 3: Deploy the Kubernetes Cluster Autoscaler in the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-deploy-CA)
- [Step 4: View the Scaling Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-view-scaling)
- [Step 5: Clean Up](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-clean-up)

## Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable Cluster Autoscaler Access to Node Pools

To manage node pools, the Kubernetes Cluster Autoscaler performs actions on other Oracle Cloud Infrastructure service resources. To perform those actions on OCI service resources, the Kubernetes Cluster Autoscaler uses the credentials of an authorized actor (or principal). You can currently set up the following types of principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources:
- Instance principal: The Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running.
- Workload identity principal: The Kubernetes Cluster Autoscaler uses the identity of a workload resource running on a Kubernetes cluster.

Note the use of workload identity principals to enable the Kubernetes Cluster Autoscaler to access OCI services and resources:
- is supported with enhanced clusters, but not with basic clusters.
- is only supported with Cluster Autoscaler version 1.26 (or later)

### Using instance principals to enable access to node pools

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

### Using workload identity principals to enable access to node pools

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

## Step 2: Copy and customize the Cluster Autoscaler configuration file

### Step 2a: Copy the configuration file
- 

In a text editor, create a file called`cluster-autoscaler.yaml`with the following content:

```

```

- Save the`cluster-autoscaler.yaml`file you created.

### Step 2b: Specify the node pools to manage

In the`cluster-autoscaler.yaml`file you created, specify the cluster's node pools that you want the Kubernetes Cluster Autoscaler to manage.

You can specify that you want the Kubernetes Cluster Autoscaler to manage a single node pool, or multiple node pools. The recommendation is to always have at least one node pool that is not managed by the Kubernetes Cluster Autoscaler to run critcal cluster add-ons, and to ensure the Kubernetes Cluster Autoscaler does not scale down the nodes on which it is running. Also note that it is your responsibility to manually scale any node pools you do not specify in the configuration file.

You specify the node pools that you want the Kubernetes Cluster Autoscaler to manage in one of two ways:
- You can explicitly specify each node pool to manage, using the`--nodes`parameter to specify each node pool's OCID.
- You can specify that the Kubernetes Cluster Autoscaler is to discover which node pool (or node pools) to manage, using the`--node-group-auto-discovery`parameter to specify the tags to match. You can specify both defined tags and freeform tags. For more information about adding tags to node pools, see[Applying Tags to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-pool-tags.htm). The Kubernetes Cluster Autoscaler manages node pools with tags that match the tags you specify. Note that the`node-group-auto-discovery`parameter is supported with Cluster Autoscaler version 1.30.3, version 1.31.1, version 1.32.0, and later.

Note that you cannot specify both the`--nodes`parameter and the`--node-group-auto-discovery`parameter in the same`cluster-autoscaler.yaml`file. The two parameters are mutually exclusive alternatives.

To use the`--nodes`parameter to explicitly specify which node pools to manage:
- 

In the`cluster-autoscaler.yaml`file you created, locate the following template line:

```

```

The`--nodes`parameter has the following format:
```

```

where:
- `<min-nodes>`is the minimum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number.
- `<max-nodes>`is the maximum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool.
- `<nodepool-ocid>`is the OCID of the node pool to manage.
- 

Change the value of the`--nodes`parameter to specify:
- The minimum number of nodes allowed in the node pool. For example, 1.
- The maximum number of nodes allowed in the node pool. For example, 5.
- The OCID of the node pool you want the Kubernetes Cluster Autoscaler to manage.

For example:
```

```

- If you only want the Kubernetes Cluster Autoscaler to manage one node pool in the cluster, locate the following line in the`cluster-autoscaler.yaml`file and remove it:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage a second node pool in the cluster, locate the following line in the`cluster-autoscaler.yaml`file and set appropriate values for the`--nodes`parameter:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage more node pools, insert additional`--nodes`parameters in the`cluster-autoscaler.yaml`file and set appropriate values for them.
- Save the`cluster-autoscaler.yaml`file.

To use the`--node-group-auto-discovery`parameter to specify that the Kubernetes Cluster Autoscaler is to discover which node pools to manage, based on matching tags:
- 

In the`cluster-autoscaler.yaml`file you created, locate the following template line:

```

```

- Delete the entire line specifying the`--nodes`parameter, and replace it with the following line:
```

```

The`--node-group-auto-discovery`parameter has the following format:
```

```

where:
- `<cluster-ocid>`is the cluster in which to run the Kubernetes Cluster Autoscaler.
- `<compartment-ocid>`is the OCID of the compartment in which the node pool, or node pools, are located.
- `{{<tagKey1>}}={{<tagValue1>}}`specifies the name of the first tag to match, and the value of that tag to match.
- `{{<tagKey2>}}={{<tagValue2>}}`optionally specifies the name of a second tag to match, and the value of that tag to match. You can specify as many tags as required (you are not limited to two). If you specify multiple tags, then all tags have to match.
- `min:{{<min-nodes>}}`specifies the minimum number of nodes allowed in all matching node pools. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number. Note that at any time, you can override the value of`min:{{<min-nodes>}}`for a particular node pool by applying the`minSize`node pool tag to that node pool. The`minSize`node pool tag always takes precedence over`min:{{<min-nodes>}}`.
- `max:{{<max-nodes>}}`specifies the maximum number of nodes allowed in all matching node pools. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool. Note that at any time, you can override the value of`max:{{<max-nodes>}}`for a particular node pool by applying the`maxSize`node pool tag to that node pool. The`maxSize`node pool tag always takes precedence over`max:{{<max-nodes>}}`.
- 

Change the value of the`--node-group-auto-discovery`parameter to specify:
- The cluster in which to run the Kubernetes Cluster Autoscaler.
- The OCID of the compartment in which the node pool is located.
- One or more tag names and tag values to match.
- The minimum number of nodes allowed in matching node pools. For example, 1.
- The maximum number of nodes allowed in matching node pools. For example, 5.

For example:
```

```

- Locate the following line in the`cluster-autoscaler.yaml`file and remove it:

```

```

- If you want the Kubernetes Cluster Autoscaler to manage more node pools, in different compartments, or with different tag names and tag values, or with different minimum and maximum numbers of allowed nodes, insert additional`--node-group-auto-discovery`parameters in the`cluster-autoscaler.yaml`file and set appropriate values for them.

For example:
```

```

- Save the`cluster-autoscaler.yaml`file.

### Step 2c: Include additional configuration settings
- In the`cluster-autoscaler.yaml`file you created, add environment variables to specify how you have set up the Kubernetes Cluster Autoscaler to access OCI services and resources:
- If you have set up an instance principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, after the line`imagePullPolicy: "Always"`at the end of the file, add the following:

```

```

For example:

```

```

- If you have set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, after the line`imagePullPolicy: "Always"`at the end of the file, add the following:

```

```

where`<cluster-region>`is the region in which the cluster is located.

For example:

```

```

- In the`cluster-autoscaler.yaml`file you created, confirm that the`--cloud-provider`parameter is set correctly for the version of Kubernetes running on the cluster. By default, the parameter assumes the cluster is running Kubernetes version 1.27 or later (or 1.23 or earlier) and is set to`oci`. If the cluster is running Kubernetes version 1.26, 1.25, or 1.24, change the value of the`--cloud-provider`parameter to`oci-oke`:
- 

In the`cluster-autoscaler.yaml`file, locate the following line:

```

```

- 
If the cluster is running Kubernetes version 1.26, 1.25, or 1.24, change the value of the`--cloud-provider`parameter to`oci-oke`:

```

```

- Save the`cluster-autoscaler.yaml`file.
- In the`cluster-autoscaler.yaml`file you created, change the image path of the Kubernetes Cluster Autoscaler image to download from Oracle Cloud Infrastructure Registry. Images are available in a number of regions. For the best performance, choose the region closest to the one where the cluster is deployed:
- 

In the`cluster-autoscaler.yaml`file, locate the following template line:

```

```

- 

Change the image path to one of the following, according to the location and Kubernetes version of the cluster in which to run the Kubernetes Cluster Autoscaler:

Image Location Kubernetes Version Image Path
Germany Central (Frankfurt) Kubernetes 1.34 fra.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
Germany Central (Frankfurt) Kubernetes 1.35 fra.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
Germany Central (Frankfurt) Kubernetes 1.36 fra.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
UK South (London) Kubernetes 1.34 lhr.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
UK South (London) Kubernetes 1.35 lhr.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
UK South (London) Kubernetes 1.36 lhr.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US East (Ashburn) Kubernetes 1.34 iad.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US East (Ashburn) Kubernetes 1.35 iad.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US East (Ashburn) Kubernetes 1.36 iad.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US West (Phoenix) Kubernetes 1.34 phx.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US West (Phoenix) Kubernetes 1.35 phx.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323
US West (Phoenix) Kubernetes 1.36 phx.ocir.io/oracle/oci-cluster-autoscaler:1.34.3-323

For example, if you want to run the Kubernetes Cluster Autoscaler in a Kubernetes 1.34 cluster located in the UK South region, specify the following image:

```

```

Tip  
  

If you want to deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster that is not in the same region as any of the Oracle repositories containing Cluster Autoscaler images, we recommend you push the image to a repository that is in the same region as the cluster, as follows:

i. Pull the image from an Oracle repository using the`docker pull`command. See[Pulling Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm).

ii. Tag the image (using the`docker tag`command), and then push the image to a repository in Oracle Cloud Infrastructure Registry that is in the same region as the cluster in which you want to run the Kubernetes Cluster Autoscaler (using the`docker push`command). See[Pushing Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm).

iii. Specify the location of the image in the`cluster-autoscaler.yaml`file.
Note  
  

If you want to deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster where you have enabled image verification, do not simply specify an image path from one of the Oracle repositories in the`cluster-autoscaler.yaml`file. Instead, do the following:

i. Pull the image from an Oracle repository using the`docker pull`command. See[Pulling Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm).

ii. Tag the image (using the`docker tag`command), and then push the image to a repository in Oracle Cloud Infrastructure Registry that is in the same region as the cluster in which you want to run the Kubernetes Cluster Autoscaler (using the`docker push`command). See[Pushing Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm).

iii. Sign the image using a master key and key version in the Vault service, creating an image signature. See[Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).

iv. Specify the location of the signed image in the`cluster-autoscaler.yaml`file. Reference the image using the image digest rather than the image tag (see[Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengenforcingsignedimagesfromocir.htm)).
- Save the`cluster-autoscaler.yaml`file.
- 

In the`cluster-autoscaler.yaml`file you created, confirm that the default values of the CPU and memory limit parameters are sufficient for the number of node pools that you want the Kubernetes Cluster Autoscaler to manage. The default limits are relatively low, so consider increasing the limits if you want the Kubernetes Cluster Autoscaler to manage a large number of node pools. Note that it is your responsibility to set the limits to suitable values.
- 

In the`cluster-autoscaler.yaml`file, locate the following lines:

```

```

- 
Set the CPU and memory limits to values that are appropriate for the number of node pools that you want the the Kubernetes Cluster Autoscaler to manage. For example:

```

```

- Save the`cluster-autoscaler.yaml`file.
- 

In the`cluster-autoscaler.yaml`file you created, specify other parameters for the Kubernetes Cluster Autoscaler. For information about the parameters you can set, see[Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).
- Save and close the`cluster-autoscaler.yaml`file.

## Step 3: Deploy the Kubernetes Cluster Autoscaler in the cluster and confirm successful deployment

- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Deploy the Kubernetes Cluster Autoscaler on the cluster by entering:
```

```

- View the Kubernetes Cluster Autoscaler logs to confirm that it was successfully deployed and is currently monitoring the workload of node pools in the cluster, by entering:
```

```

- Identify which one of the three Kubernetes Cluster Autoscaler pods defined in the`cluster-autoscaler.yaml`file is currently performing actions, by entering:
```

```

- Obtain a high-level view of the Kubernetes Cluster Autoscaler's state from the configmap in the kube-system namespace, by entering:
```

```

## Step 4: View the Scaling Operation

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

## Step 5: Clean Up

- Delete the sample Nginx application by entering:
```

```

- After ten minutes, confirm that the worker nodes have reduced to the original number, by entering:
```

```

Note that after deleting the sample Nginx application and waiting, you might see fewer worker nodes but still more than the original number. This is probably because kube-system pods have been scheduled to run on those nodes. kube-system pods can prevent the Kubernetes Cluster Autoscaler from removing nodes because the Autoscaler's`skip-nodes-with-system-pods`parameter is set to`true`
