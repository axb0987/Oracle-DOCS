# Working with the Kubernetes Metrics Server as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_standalone.htm
- Fetched: 2026-09-05 01:57 CDT

# Working with the Kubernetes Metrics Server as a Standalone Program

Find out how to use kubectl to deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools and virtual node pools that you've created using Kubernetes Engine (OKE).

Using the Kubernetes Metrics Server as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
- Installing a version of the Kubernetes Metrics Server that is compatible with the version of Kubernetes running on the cluster.
- Specifying configuration arguments correctly.
- Manually upgrading the Kubernetes Metrics Server when you upgrade a cluster to a new version of Kubernetes, to ensure the Kubernetes Metrics Server is compatible with the cluster's new Kubernetes version.

To deploy the Kubernetes Metrics Server as a standalone program on clusters with managed node pools or virtual node pools that you've created with Kubernetes Engine:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- If your Oracle Cloud Infrastructure user is a tenancy administrator or cluster administrator, skip the next step and go straight to the following step.
- If your Oracle Cloud Infrastructure user is not a tenancy administrator or cluster administrator, ask a tenancy administrator or cluster administrator to grant your user the Kubernetes RBAC cluster-admin clusterrole on the cluster by entering:

```

```

For more information, see[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengaboutaccesscontrol.htm).
- 

Deploy the Kubernetes Metrics Server by entering the following command in a terminal window:

```

```

where`<version-number>`is the Kubernetes Metrics Server version that you want to deploy. For example,`v0.6.1`.

Note that the Kubernetes Metrics Server is being actively developed, so the version number to specify will change over time. To find out the currently available versions, see the[Kubernetes Metrics Server documentation](https://github.com/kubernetes-sigs/metrics-server/releases).
Tip  
  
If the command fails to connect to`https://github.com/kubernetes-sigs/metrics-server/releases/download/<version-number>/components.yaml`, go to the url in a browser and download the manifest file`components.yaml`to a local directory. Repeat the`kubectl apply`command and specify the local location of the`components.yaml`file.
- 

Confirm that the Kubernetes Metrics Server has been deployed successfully and is available by entering:

```

```
