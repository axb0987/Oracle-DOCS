# Accessing a Cluster Using Headlamp
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterusingheadlamp.htm
- Fetched: 2026-09-05 01:54 CDT

# Accessing a Cluster Using Headlamp

Find out how to use Headlamp to view and manage clusters you've created using Kubernetes Engine (OKE).

Headlamp is an open source Kubernetes user interface that you can use to inspect workloads, view logs and events, edit resources, troubleshoot applications, and perform operations allowed by your Kubernetes RBAC permissions. You can run Headlamp as a desktop application or deploy it in a Kubernetes cluster.
Important  
  

The upstream Kubernetes project recommends Headlamp as the replacement for Kubernetes Dashboard. The Kubernetes Dashboard project has been archived and is no longer maintained. Headlamp provides similar cluster management workflows, as well as multi-cluster support, extensibility, and both desktop and in-cluster deployment options. For more information, see[From Kubernetes Dashboard to Headlamp: Understanding the Transition](https://kubernetes.io/blog/2026/06/01/dashboard-to-headlamp/).

Choose how to run Headlamp based on how you want to access clusters:
- For individual administrators and developers, use Headlamp Desktop. Headlamp Desktop runs on your workstation and connects to clusters using the Kubernetes kubeconfig file. You do not have to deploy Headlamp components in each cluster.
- For a shared browser-based interface, deploy Headlamp in a cluster. The Headlamp project provides a Helm chart for in-cluster deployments.

In both cases, Kubernetes authentication and RBAC determine which resources users can view and which operations they can perform.

## Using Headlamp Desktop

Use Headlamp Desktop when you want to access one or more clusters from a workstation without deploying Headlamp in the clusters.

To use Headlamp Desktop to access a cluster:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

Verify that the kubeconfig file contains the Kubernetes context for the cluster you want to access by entering:

```

```

- 

Install Headlamp Desktop by following the instructions for your operating system in the[Headlamp Desktop documentation](https://headlamp.dev/docs/latest/installation/desktop/).

For example, on macOS, you can install Headlamp Desktop using Homebrew by entering:

```

```

- Start Headlamp Desktop.
- Select the cluster or Kubernetes context you want to access.
- Complete authentication if prompted.

Headlamp displays the Kubernetes resources that the identity in the kubeconfig file is authorized to access. The operations available in Headlamp depend on the Kubernetes RBAC permissions granted to that identity.

Because Headlamp Desktop runs on your workstation, it does not consume worker node resources and is not itself subject to virtual node workload restrictions.

## Installing Headlamp In-Cluster

Deploy Headlamp in a cluster when you want to provide a shared browser-based interface.

Before you install Headlamp, ensure that:
- You have set up access to the cluster. You can verify access by entering`kubectl get nodes`. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm).
- Helm is installed and available in your environment. You can verify the installation by entering`helm version`.
- Your Kubernetes identity has sufficient permissions to create the resources in the Headlamp Helm chart.

To install Headlamp using Helm:
- 

Add the Headlamp Helm repository by entering:

```

```

```

```

- 

Create a namespace for Headlamp by entering:

```

```

- 

Install Headlamp by entering:

```

```

- 

Verify the installation:

```

```

Wait until the Headlamp pod is running and ready.

## Authenticate to an In-Cluster Headlamp Deployment

Headlamp uses Kubernetes authentication and RBAC to determine which cluster resources users can access.

To authenticate to the Headlamp deployment installed using the Helm chart:
- 

Verify the Headlamp service account by entering:

```

```

- 

Verify the ClusterRoleBinding by entering:

```

```

Important  
  

By default, the Headlamp Helm chart creates a`headlamp-admin`ClusterRoleBinding that grants the`cluster-admin`role to the`headlamp`service account. The`cluster-admin`role provides unrestricted access to the cluster. For production use, grant only the permissions required for your environment.
- 

Create a temporary token for the Headlamp service account by entering:

```

```

- 

Copy the token from the command output. You enter this token when you access Headlamp.

For shared deployments, consider configuring OpenID Connect (OIDC) authentication instead of distributing service account tokens. See the[Headlamp in-cluster documentation](https://headlamp.dev/docs/latest/installation/in-cluster/).

## Accessing an In-Cluster Headlamp Deployment

For local administrative access, you can use`kubectl port-forward`to access the Headlamp service.
- 

Forward local port 8080 to the Headlamp service by entering:

```

```

- 

Open a browser and go to:

```

```

- When prompted, enter the authentication token you created earlier.
Important  
  

The`kubectl port-forward`command is not supported for pods running on virtual nodes. If the Headlamp pod runs on a virtual node, expose Headlamp using an ingress or another access method supported by your environment instead.

For shared production access, configure ingress, TLS, and an appropriate authentication mechanism rather than relying on port forwarding. See the[Headlamp in-cluster documentation](https://headlamp.dev/docs/latest/installation/in-cluster/).

## Using Headlamp with Virtual Nodes

You can use Headlamp with clusters that contain virtual node pools.
- Headlamp Desktop runs outside the cluster and is not itself subject to virtual node workload restrictions. Workloads that you inspect or manage remain subject to the capabilities and limitations of the node type on which they run.
- An in-cluster Headlamp deployment runs as Kubernetes pods. If Headlamp pods are scheduled on virtual nodes, the pods are subject to the same Kubernetes feature, networking, storage, and resource constraints as other workloads running on virtual nodes.

In particular,`kubectl port-forward`is not supported for pods on virtual nodes. See[Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm)and[Resources Allocated to Pods Provisioned by Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengvirtualnodepodresourceallocation.htm).

## Verifying Headlamp Access

After connecting to the cluster using Headlamp:
- Select the cluster.
- Select a namespace.
- Open Workloads .
- Select Deployments or Pods .
- Select a resource to view its details, events, logs, and related resources.

The resources and operations that are shown depend on the Kubernetes RBAC permissions granted to the identity you used to access the cluster.

If the Kubernetes Metrics Server is installed in the cluster, Headlamp can also display resource usage information. For more information about the Kubernetes Metrics Server, see[Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm).

## Removing an In-Cluster Headlamp Deployment

To remove the Headlamp deployment created in this topic:
- 

Uninstall the Headlamp Helm release by entering:

```

```

- 

Delete the Headlamp namespace by entering:

```

```
