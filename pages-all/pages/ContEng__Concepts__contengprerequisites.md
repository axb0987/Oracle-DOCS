# Preparing for Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengprerequisites.htm
- Fetched: 2026-09-05 01:53 CDT

# Preparing for Kubernetes Engine (OKE)

Find out about the prerequisites you have to meet before you can use Kubernetes Engine (OKE).

Before you can use Kubernetes Engine to create a Kubernetes cluster:
- You must have access to an Oracle Cloud Infrastructure tenancy. The tenancy must be subscribed to one or more of the regions in which Kubernetes Engine is available (see[Availability by Region](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengprerequisites.htm#regional-availability)).
- 

Your tenancy must have sufficient quota on different types of resource (see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)). More specifically:
- Compute instance quota: The compute instance quota depends on the shape you select. Compute instance quota is determined by the number of compute cores, and the amount of memory required for a particular shape. When creating a Kubernetes cluster with managed nodes and managed node pools, at least one compute instance (node) must be available in the tenancy. However, you'll probably want more than this minimum. For example, to create a highly available cluster in a region with three availability domains (ADs), at least three compute instances must be available (one in each availability domain). Note that when creating a Kubernetes cluster with virtual nodes, the[Compute Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#computelimits)for compute cores and memory apply to pods running on virtual nodes.
- Block volume quota: If you intend to create Kubernetes persistent volumes, sufficient block volume quota must be available in each availability domain to meet the persistent volume claim. Persistent volume claims must request a minimum of 50 gigabytes. See[Setting Up Storage for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingpersistentvolumeclaim.htm).
- Load balancer quota: If you intend to create a load balancer to distribute traffic between the nodes running a service in a Kubernetes cluster, sufficient load balancer quota must be available in the region. See[Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingloadbalancer.htm).
- Within your tenancy, there must already be a compartment to contain the necessary network resources (such as a VCN, subnets, internet gateway, route table, security lists). If such a compartment does not exist already, you will have to create it. Note that the network resources can reside in the root compartment. However, if you expect multiple teams to create clusters, best practice is to create a separate compartment for each team.
- 

Within the compartment, network resources (such as a VCN, subnets, internet gateway, route table, security lists) must be appropriately configured in each region in which you want to create and deploy clusters. For example, to create a highly available cluster in a region with three availability domains, the VCN must include:
- For worker nodes: a regional subnet (recommended), or three AD-specific subnets (one in each of the availability domains).
- For load balancers: optionally (but usually) an additional regional subnet (recommended), or an additional two AD-specific subnets (each in a different availability domain).

Best practice is to use regional subnets to make failover across availability domains simpler to implement.

When creating a new cluster, you can have Kubernetes Engine automatically create and configure new network resources for the new cluster, or you can specify existing network resources. If you specify existing network resources, you or somebody else must have already configured those resources appropriately. See[Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm).
- 

To create and/or manage clusters, you must belong to one of the following:
- The tenancy's Administrators group
- 

A group to which a policy grants the appropriate Kubernetes Engine permissions. See[Create Required Policy for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroupsrequired).
- 

To perform Kubernetes operations on a cluster:
- You must be able to run the Kubernetes command line tool kubectl. You can use the kubectl installation included in Cloud Shell, or you can use a local installation of kubectl (see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengaccessingclusterkubectl.htm)).
- You must have set up your own copy of the cluster's kubeconfig configuration file (see[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengdownloadkubeconfigfile.htm)). Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up.
- You must have appropriate permissions to access the cluster (see[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)).

## Availability by Region

Kubernetes Engine is available in all the Oracle Cloud Infrastructure regions listed at[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Refer to that topic to see region identifiers, region keys, and availability domain names.

In some cases, you might have to use shortened versions of availability domain names. For example, when defining a persistent volume claim (PVC), to request storage in a particular availability domain by specifying the value of the`topology.kubernetes.io/zone`Kubernetes label. To find out how to construct shortened versions of availability domain names, see[topology.kubernetes.io/zone](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Reference/contengsupportedlabelsusecases.htm#failure-domain)
