# Comparing Enhanced Clusters with Basic Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm
- Fetched: 2026-09-05 01:54 CDT

# Comparing Enhanced Clusters with Basic Clusters

Find out about the differences between the enhanced clusters and basic clusters you can create using Kubernetes Engine (OKE).

When creating a new cluster with Kubernetes Engine, you specify the type of cluster to create as one or other of the following:
- Enhanced cluster: Enhanced clusters support all available features. See[Enhanced Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-enhancedclusters).
- Basic cluster: Basic clusters support all the core functionality provided by Kubernetes and Kubernetes Engine, but none of the enhanced features that Kubernetes Engine provides. See[Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-basicclusters).

Note the following when creating clusters:
- When using the Console to create a cluster, if you don't select any enhanced features during cluster creation, you have the option to create the new cluster as a basic cluster. A new cluster is created as an enhanced cluster by default, unless you explicitly choose to create a basic cluster.
- When using the CLI or the API to create a cluster, you can specify whether to create a basic cluster or an enhanced cluster. If you don't explicitly specify the type of cluster to create, a new cluster is created as a basic cluster by default (until the date specified in the Service Change Announcement[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)).

Creating a new cluster as an enhanced cluster enables you to add enhanced features later, even if you didn't select any enhanced features initially. When you create an enhanced cluster, you must create it as a[VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters)cluster (that is, the cluster is fully integrated into your VCN, including the Kubernetes API endpoint). If you do choose to create a new cluster as a basic cluster, you can still choose to upgrade it to an enhanced cluster later on, provided it is[VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters)and meets the applicable upgrade prerequisites (note that basic clusters created with a Kubernetes API endpoint that is public and not integrated into your VCN aren’t eligible). However, you can't downgrade an enhanced cluster to a basic cluster.

All references to 'clusters' in the Kubernetes Engine documentation refer to both enhanced clusters and basic clusters, unless explicitly stated otherwise.

## Enhanced Clusters

Enhanced clusters support all available features, including features not supported by basic clusters (such as virtual nodes, cluster add-on management, workload identity, additional worker nodes per cluster, self-managed nodes, and node cycling when updating node pools, or when upgrading or rolling back the Kubernetes version running on managed nodes). Enhanced clusters come with a financially-backed service level agreement (SLA).

### Notable features supported differently by enhanced clusters

Depending on the enhanced features you select for an enhanced cluster, some features are supported differently in enhanced clusters when compared to basic clusters:
- Managed and virtual node pools: In an enhanced cluster, you can choose to create virtual node pools (as well as the managed node pools that you are restricted to creating in a basic cluster). If you choose to create virtual nodes and node pools, then load balancing, pod networking, autoscaling, and application log viewing are supported differently. See[Virtual Nodes and Virtual Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-virtualnodes).
- Cluster add-ons: In an enhanced cluster, you can use Kubernetes Engine to manage both essential add-ons and a growing portfolio of optional add-ons. You can enable or disable specific add-ons, select add-on versions, opt into and out of automatic updates by Oracle, and manage add-on specific customizations. See[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).
- Permissions: In an enhanced cluster, you can choose to define OCI IAM policies that authorize specific pods to make OCI API calls, and access OCI resources. See[Granting Workloads Access to OCI Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm).

In addition, you can[contact us](https://support.oracle.com/)to request an increase to the number of enhanced clusters you can create in a region (see[Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Container_Engine_for_Kubernetes_Limits)).

### Notable features not supported by enhanced clusters

Enhanced clusters support all the features supported by basic clusters. There are no features supported by basic clusters that are not supported by enhanced clusters.

## Basic Clusters

Basic clusters support all the core functionality provided by Kubernetes and Kubernetes Engine, but none of the enhanced features that Kubernetes Engine provides with enhanced clusters (such as virtual nodes, cluster add-on management, workload identity, node cycling, self-managed nodes, and additional worker nodes per cluster). Basic clusters come with a service level objective (SLO), but not a financially-backed service level agreement (SLA).

### Notable features supported differently by basic clusters

Some features are supported differently in basic clusters when compared to enhanced clusters:
- Managed and virtual node pools: In a basic cluster, you can only create managed node pools (rather than the managed and virtual node pools you can choose to create in an enhanced cluster). Load balancing, pod networking, autoscaling, and application log viewing are supported differently with managed nodes and node pools. See[Managed Nodes and Managed Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-managednodes).
- Cluster add-ons: In a basic cluster, you have more responsibility and less flexibility when managing cluster add-ons. You are responsible for upgrading essential add-ons, but you cannot install or disable specific add-ons, select add-on versions, opt into and out of automatic updates by Oracle, or manage add-on specific customizations. In addition, you are responsible for installing, managing, and maintaining any optional add-ons you want in the cluster. See[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm).
- Permissions: In a basic cluster, you have to define OCI IAM policies that authorize users and instances (rather than workload identity you can choose to implement in an enhanced cluster). Consequently, more privileges are granted than the absolute minimum required, which is not best practice. See[Granting Workloads Access to OCI Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm)

In addition, you cannot request an increase to the number of basic clusters you can create in a region (see[Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Container_Engine_for_Kubernetes_Limits)).

### Notable features not supported by basic clusters

Basic clusters do not support some of the features supported by enhanced clusters:
- Virtual node pools
- Fine-grained cluster add-on deployment and configuration
- Workload identity
- Increased numbers of worker nodes
- Self-managed nodes
- Financially-backed service level agreement (SLA)
- Node cycling when updating node pools, or when upgrading or rolling back the Kubernetes version running on managed nodes
- Cloud Guard Container Security Config
- Creation of managed node pools in compute clusters

## Comparison of Enhanced Clusters and Basic Clusters

The following table summarizes the similarities and differences between enhanced clusters and basic clusters:

Feature / Capability Enhanced Cluster Basic Cluster
Supports all core Kubernetes and OKE features Yes Yes
Managed node pools supported Yes Yes
Virtual node pools supported Yes No
Self-managed nodes supported Yes No
Node cycling (the automatic cordoning, draining, and replacement of nodes) for updates, and for Kubernetes version upgrades/rollbacks Yes No
Cloud Guard Container Security Config Yes No
Flexible and managed cluster add-ons Yes No
Fine-grained add-on deployment/configuration Yes No
Can manage essential and optional add-ons in Console and other interfaces Yes No
Add-on version selection and automatic updates Yes No
User-managed add-ons possible Yes Yes
Workload identity (fine-grained OCI IAM for pods/containers) Yes No
Creating managed node pools in compute clusters Yes No
User/instance policy-based permissions Yes Yes
Can request increase for number of clusters, or number of nodes per cluster Yes No
Higher worker node limits Yes No
Financially-backed SLA Yes No
Service Level Objective (SLO) only No Yes
Can upgrade to enhanced cluster N/A Yes (cluster must be VCN-native)
Default creation type (Console) Yes No (unless selected)
Default creation type (CLI/API) No, unless selected (until the date specified[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)) Yes (until the date specified[here](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_oke)
