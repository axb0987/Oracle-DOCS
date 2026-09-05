# Deploying a Sample Nginx App on a Cluster Using Kubectl
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingsamplenginx.htm
- Fetched: 2026-09-05 01:55 CDT

# Deploying a Sample Nginx App on a Cluster Using Kubectl

Find out how to use kubectl to deploy an Nginx app on a cluster you've created using Kubernetes Engine (OKE).

Having created a Kubernetes cluster using Kubernetes Engine, you'll typically want to try it out by deploying an application on the nodes in the cluster. For convenience, the Quick Start tab (available from the Cluster page) makes it easy to view and copy the commands to:
- set up access to the cluster
- download and deploy a sample Nginx application using the Kubernetes command line tool kubectl from the instructions in a manifest file

To deploy the sample nginx application:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

In a terminal window, deploy the sample Nginx application by entering:

```

```

Tip  
  
If the command fails to connect to`https://k8s.io/examples/application/deployment.yaml`, go to the url in a browser and download the manifest file`deployment.yaml`to a local directory. Repeat the`kubectl create`command and specify the local location of the`deployment.yaml`file.
- Confirm that the sample application has been deployed successfully by entering:

```

```
