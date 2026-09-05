# Planning for Enhanced Clusters Up to 20,000 Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengplanningfor20knodes.htm
- Fetched: 2026-09-05 01:55 CDT

# Planning for Enhanced Clusters Up to 20,000 Nodes

Find out about prerequisites and planning considerations for Kubernetes clusters that need to scale above 5,000 nodes and up to 20,000 nodes when using Kubernetes Engine (OKE).

Kubernetes Engine supports large enhanced clusters up to 20,000 nodes. If you want to scale a cluster above 5,000 nodes and up to 20,000 nodes, contact your Oracle account team before creating or scaling the cluster.

We will confirm whether your tenancy, cluster configuration, and region are ready for clusters above 5,000 nodes and up to 20,000 nodes. We might ask you to validate or update cluster settings, add-ons, in-cluster components, or client behavior that could affect cluster scale, such as clients of the Kubernetes API server or clients that use Kubernetes-native or Kubernetes-facilitated OCI integrations.

## Requirements

To scale clusters above 5,000 nodes and up to 20,000 nodes:
- The cluster must be an enhanced cluster.
- The cluster must run Kubernetes version 1.36 or later.
- The cluster must be enabled by Oracle for the higher node limit. Contact your Oracle account team to enable the cluster.
- The cluster configuration must satisfy networking, IAM policy, and capacity requirements for very large clusters.

Only clusters running Kubernetes version 1.36 or later can scale above 5,000 nodes and up to 20,000 nodes. If a cluster is running an earlier Kubernetes version, upgrade the cluster to Kubernetes version 1.36 or later before contacting your Oracle account team to request the higher node limit.

## Networking and IAM Prerequisites

Before contacting your Oracle account team to request the higher node limit, review the following large-cluster networking and IAM prerequisites:
- Add the required service policy statements so that OKE can manage IP address resources used by the cluster endpoint and make sure the cluster endpoint subnet has sufficient capacity for additional endpoint addresses. See[Create Policy for Larger Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic-Create_Policies_for_Larger-Clusters).
- For clusters at this scale, Oracle recommends Cilium as the preferred CNI option. See[Pod Networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengpodnetworking.htm).
- If you choose to use the flannel CNI plugin for a cluster at this scale, carefully validate that the value of the Pods CIDR Block property is large enough for the intended node count, and validate performance and startup behavior at your target scale.

## Add-on Configuration

Review cluster add-on configuration before scaling above 5,000 nodes and up to 20,000 nodes. Some add-ons run on every node, or process cluster-wide objects such as Services and EndpointSlices, and might need configuration changes for very large clusters.

For example, review kube-proxy resource requests and limits, rolling update settings, and any custom kube-proxy configuration before scaling the cluster.

## Operational Planning

Before scaling above 5,000 nodes and up to 20,000 nodes, review[Large Cluster Best Practices](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengbestpractices_topic-Large-Scale-Clusters-best-practices.htm)and validate the cluster at the target scale before relying on it for production workloads.
