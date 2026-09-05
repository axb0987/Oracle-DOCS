# Cluster Networks with Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm
- Fetched: 2026-09-05 01:52 CDT

# Cluster Networks with Instance Pools

Cluster networks use instance pools to manage groups of identical high performance computing (HPC), GPU, or optimized instances that are connected with a high-bandwidth, ultra low-latency network. Each node in the cluster is a bare metal machine located in close physical proximity to the other nodes. A remote direct memory access (RDMA) network between nodes provides latency as low as single-digit microseconds, comparable to on-premises HPC clusters.

Cluster networks are built on top of the[instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instance-pools.htm)feature. Most operations in the instance pool are managed directly by the cluster network, though you can resize the underlying instance pool, change the instance configuration that the pool uses to create new instances, monitor the pool, and add tags.
Tip  
  
If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, then use[compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/compute-clusters.htm)instead.

For steps to manage cluster networks with instance pools, see the following topics:
- [Listing Cluster Networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-list.htm)
- [Creating a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm)
- [Getting a Cluster Network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-get.htm)
- [Detaching Instances from a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)
- [Resizing a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm)
- [Updating the Instance Configuration for a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/update-cluster-network-instance-configuration.htm)
- [Renaming a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-cluster-network.htm)
- [Deleting a Cluster Network with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/delete-cluster-network.htm)

For more information about how to access and store the data that you want to process in cluster networks, see[FastConnect Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm),[Overview of File Storage](https://docs.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm),[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm), and[Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm).

## Supported Shapes

The following[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm)support cluster networks:

- BM.GPU.A100-v2.8
- BM.GPU.H100.8
- BM.GPU4.8
- BM.HPC2.36
- BM.Optimized3.36

Typically, to create multiple HPC, GPU, or optimized instances that are contained in a cluster network, you must[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).

## Supported Regions and Availability Domains

Cluster networks are supported in selected regions within the Oracle Cloud Infrastructure[commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)and[Government Cloud realms](https://docs.oracle.com/iaas/Content/General/Concepts/govlanding.htm).

### Supported regions in the commercial realm
- Australia East (Sydney)
- Australia Southeast (Melbourne)
- Brazil East (Sao Paulo)
- Brazil Southeast (Vinhedo)
- Canada Southeast (Montreal)
- Canada Southeast (Toronto)
- France Central (Paris)
- France South (Marseille)
- Germany Central (Frankfurt)
- India South (Hyderabad)
- India West (Mumbai)
- Israel Central (Jerusalem)
- Italy Northwest (Milan)
- Japan Central (Osaka)
- Japan East (Tokyo)
- Netherlands Northwest (Amsterdam)
- Saudi Arabia West (Jeddah)
- Singapore (Singapore)
- South Africa Central (Johannesburg)
- South Korea Central (Seoul)
- South Korea North (Chuncheon)
- Sweden Central (Stockholm)
- Switzerland North (Zurich)
- UAE East (Dubai)
- UK South (London)
- US East (Ashburn)
- US Midwest (Chicago)
- US West (Phoenix)
- US West (San Jose)

### Supported regions in the Government Cloud realms
- UK Gov South (London)
- UK Gov West (Newport)
- US Gov East (Ashburn)

The availability domain that you create the cluster network in must have hardware that supports cluster networks.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: For a typical policy that gives access to cluster networks, see[Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Before You Begin

[Create an instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)for the instance pool that is managed by the cluster network. Use the following settings:
- Image: Select Change image .
- Select Marketplace .
- Search for HPC .
- Select the Oracle Linux HPC cluster networking image .
- Shape: Select Change shape .
- Select Bare metal machine .
- Select a[shape that supports cluster networks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#cluster-networks-supported-shapes).

For more information about these shapes, see[Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm)
