# Accessing a Cluster Using the Kubernetes Dashboard
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengstartingk8sdashboard.htm
- Fetched: 2026-09-05 01:56 CDT

# Accessing a Cluster Using the Kubernetes Dashboard

Find out how to start the Kubernetes Dashboard to view the clusters you've created using Kubernetes Engine (OKE).
Important  
  

The Kubernetes Dashboard project has been archived and is no longer maintained. The upstream Kubernetes project recommends Headlamp as the replacement for Kubernetes Dashboard. Headlamp supports comparable cluster management workflows and adds multi-cluster support, extensibility, and both desktop and in-cluster deployment options. For more information, see[From Kubernetes Dashboard to Headlamp: Understanding the Transition](https://kubernetes.io/blog/2026/06/01/dashboard-to-headlamp/).

To use Headlamp to access clusters you've created using OKE see[Accessing a Cluster Using Headlamp](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterusingheadlamp.htm).
Note  
  
You cannot use the Kubernetes Dashboard with virtual node pools.

The Kubernetes Dashboard is a web-based management interface that enables you to:
- deploy and edit containerized applications
- assess the status of containerized applications
- troubleshoot containerized applications

The Kubernetes Dashboard is particularly useful for new Kubernetes users. For more information about the Kubernetes Dashboard (sometimes called the Web UI or the Dashboard UI), see the[Web UI (Dashboard) topic](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)in the Kubernetes documentation.

The Kubernetes Dashboard is not deployed in clusters by default. However, you can deploy the Kubernetes Dashboard in clusters you create with Kubernetes Engine in the following ways:
- 

To manually deploy the Kubernetes Dashboard on an existing cluster, see the[Kubernetes documentation](https://github.com/kubernetes/dashboard). When you follow the instructions to manually deploy the Kubernetes Dashboard, it is deployed in the`kubernetes-dashboard`namespace (not the`kube-system`namespace). The URL to display a manually deployed Kubernetes Dashboard is:

```

```

- To have Kubernetes Engine automatically deploy the Kubernetes Dashboard during enhanced cluster creation, you can:
- Create the enhanced cluster using the 'Custom Create' workflow in the Console, and configure the Kubernetes Dashboard cluster add-on.
- Create the cluster using the API and set the isKubernetesDashboardEnabled attribute to true.

When Kubernetes Engine automatically deploys the Kubernetes Dashboard, it is deployed in the`kube-system`namespace. The URL to display an automatically deployed Kubernetes Dashboard is:

```

```

Note the following:
- You cannot run the Kubernetes Dashboard in Cloud Shell.
- We do not recommend installing the Kubernetes Dashboard on production clusters due to the lack of extensible authentication support. If you do install the Kubernetes Dashboard, we recommend that you restrict access within the cluster, instead of exposing it externally via either a load balancer or an ingress controller. The Kubernetes Dashboard is a common attack vector used to gain access to Kubernetes clusters.
- The commands to use to delete the Kubernetes Dashboard from a cluster will depend on the version of Kubernetes running on the cluster. See[Notes about Deleting the Kubernetes Dashboard](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengstartingk8sdashboard.htm#Starting_the_Kubernetes_Dashboard__kubernetes_dashboard_deletion_notes).
- An Oracle Cloud Infrastructure CLI command in the kubeconfig file generates authentication tokens that are short-lived, cluster-scoped, and specific to individual users. As a result, you cannot share kubeconfig files between users to access Kubernetes clusters. The generated authentication tokens are also unsuitable if you want other processes and tools to access the cluster, such as continuous integration and continuous delivery (CI/CD) tools. In this case, consider creating a Kubernetes service account and adding its associated authentication token to the kubeconfig file. For more information, see[Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm).
- You can use the Kubernetes Dashboard with managed node pools but not with virtual node pools.

## Accessing a Cluster using the Kubernetes Dashboard

To access a cluster using the Kubernetes Dashboard:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

In a text editor, create a file (for example, called oke-admin-service-account.yaml) with the following content:

```

```

The file defines an administrator service account and a clusterrolebinding, both called oke-admin.
- 

Create the service account and the clusterrolebinding in the cluster by entering:

```

```

where`<filename>`is the name of the file you created earlier. For example:

```

```

The output from the above command confirms the creation of the service account and the clusterrolebinding:
```

```

You can now use the oke-admin service account to view and control the cluster, and to connect to the Kubernetes dashboard.
- Obtain an authentication token for the oke-admin service account as follows:
- In a text editor, create a file (for example, called oke-admin-sa-token.yaml) to create a secret (for example, named oke-admin-sa-token) with the following content.

```

```

- 

Create the service account token by entering:

```

```

where`<filename>`is the name of the file you created earlier. For example:

```

```

- 

View details of the secret by entering:

```

```

The output from the above command includes an authentication token (a long alphanumeric string) as the value of the`token:`element, as shown below:
```

```

In the example above,`eyJh______px1Q`(abbreviated for readability) is the authentication token.
- 

Copy the value of the`token:`element from the output. You will use this token to connect to the dashboard.
- In a terminal window, enter`kubectl proxy`to make the Kubernetes Dashboard available.
- Open a browser and go to the following URL to display the Kubernetes Dashboard that was deployed when the cluster was created:

```

```

Note that if you followed the instructions in the[Kubernetes documentation](https://github.com/kubernetes/dashboard)to manually deploy the Kubernetes Dashboard on an existing cluster, it is deployed in the`kubernetes-dashboard`namespace rather than the`kube-system`namespace. As a result, the URL to display the manually deployed Kubernetes Dashboard is:

```

```

- 

In the Kubernetes Dashboard, select Token and paste the value of the`token:`element you copied earlier into the Token field.
- In the Kubernetes Dashboard, select Sign In , and then select Overview to see the applications deployed on the cluster.

## Notes about Deleting the Kubernetes Dashboard

If you want to manually delete the Kubernetes Dashboard from a cluster, run the following kubectl commands:

```

```
