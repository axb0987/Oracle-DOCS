# Scaling Kubernetes Clusters and Node Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingkubernetesclustersnodepools.htm
- Fetched: 2026-09-05 01:56 CDT

# Scaling Kubernetes Clusters and Node Pools

Find out about scaling up and scaling down the Kubernetes node pools and clusters you've created using by Kubernetes Engine (OKE).

You can scale the clusters you create using Kubernetes Engine to optimize resource usage.

## Scaling Clusters with Managed Node Pools

In the case of managed node pools, you have responsibility for adjusting cluster capacity in response to changing requirements. You can:
- Change the number of managed node pools in a cluster to scale the cluster up and down (see[Adding and Removing Node Pools to Scale Clusters Up and Down](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm)).
- Change the number of managed nodes in a managed node pool to scale the node pool up and down (see[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm)).
- Enable autoscaling to automatically scale managed node pools and pods (see[Autoscaling Kubernetes Node Pools and Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengautoscalingclusters.htm)).

## Scaling Clusters with Virtual Node Pools

In the case of virtual node pools, much of the operational overhead of cluster capacity management is handled for you.

A virtual node pool scales automatically, and can support up to 1000 pods per virtual node.

If 1000 pods per virtual node is insufficient, you can:
- Increase the number of virtual node pools in a cluster to scale up the cluster (see[Adding and Removing Node Pools to Scale Clusters Up and Down](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm)).
- Increase the number of virtual nodes in the virtual node pool to scale up the node pool (see[Scaling Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm)). For the maximum number of virtual nodes, see[Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Container_Engine_for_Kubernetes_Limits).
