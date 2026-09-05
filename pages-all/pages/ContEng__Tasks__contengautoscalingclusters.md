# Autoscaling Kubernetes Node Pools and Pods
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengautoscalingclusters.htm
- Fetched: 2026-09-05 01:54 CDT

# Autoscaling Kubernetes Node Pools and Pods

Find out about autoscaling Kubernetes node pools and pods you've created using Kubernetes Engine (OKE).

You can automatically scale the node pools and pods of clusters you create using Kubernetes Engine to optimize resource usage.

To enable cluster autoscaling by autoscaling node pools, you can deploy the Kubernetes Cluster Autoscaler (see[Using the Kubernetes Cluster Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm)). You can deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster in two ways:
- as a standalone program (see[Working with the Cluster Autoscaler as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm))
- as a cluster add-on (see[Working with the Cluster Autoscaler as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm))

To enable autoscaling by autoscaling pods, you deploy the Kubernetes Metrics Server to collect resource metrics from each worker node in the cluster (see[Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm)). You can deploy the Kubernetes Metrics Server on a Kubernetes cluster in two ways:
- as a standalone program, on clusters with managed node pools or virtual node pools (see[Working with the Kubernetes Metrics Server as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_standalone.htm))
- as a cluster add-on, on clusters with managed node pools (see[Working with the Kubernetes Metrics Server as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmetricsserver_cluster-add-on.htm))

Having deployed the Kubernetes Metrics Server, you can then use:
- the Kubernetes Horizontal Pod Autoscaler to adjust the number of pods in a deployment (see[Using the Kubernetes Horizontal Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm))
- the Kubernetes Vertical Pod Autoscaler to adjust the resource requests and limits for containers running in a deployment's pods (see[Using the Kubernetes Vertical Pod Autoscaler](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingverticalpodautoscaler.htm))

You can use the Kubernetes Cluster Autoscaler in a cluster with both the Kubernetes Horizontal Pod Autoscaler and the Kubernetes Vertical Pod Autoscaler.
Note
