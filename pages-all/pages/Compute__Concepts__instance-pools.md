# Managing Instance Pools
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance-pools.htm
- Fetched: 2026-09-05 01:49 CDT

# Managing Instance Pools

An instance pool is a set of instances that is managed as a group.

Instance pools simplify the management of your compute instances.

## Instance Pools Overview

Instance pools let you create and manage multiple compute instances within the same region as a group. They also enable integration with other services, such as the Load Balancer service and IAM service.

You create an instance pool using an existing instance configuration.

After you have created an instance pool, you can update the size of the pool, add and remove existing instances from the pool, and attach or detach load balancers and network load balancers. You can also update the instance pool to use a different instance configuration, or to place instances in a different availability domain, fault domain, or subnet.

You can automatically adjust the number of instances in an instance pool based on performance metrics or a schedule. You can also stop and start instances in an instance pool based on a schedule. To do this, enable autoscaling for the instance pool.

A cluster network is a special kind of instance pool that is designed for massive, high-performance computing jobs.
For steps to manage instance pools, see the following topics:
- [Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/instance-pools-list.htm)
- [Creating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/creatinginstancepool.htm)
- [Getting Instance Pool Details](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/instance-pools-get.htm)
- [Updating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/updatinginstancepool.htm)
- [Stopping and Starting the Instances in an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/restartinginstancepool.htm)
- [Moving an Instance Pool to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/instance-pools-move.htm)
- [Deleting Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/deletinginstancepool.htm)

The following topics are related to Instance Pools.
- [Autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/autoscalinginstancepools.htm)
- [Cluster Networks with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/managingclusternetworks.htm)

### Instance Pool Lifecycle States

The following list describes the different lifecycle states for instance pools.
- Provisioning: When you create an instance pool, this is the first state the instance pool is in. Instances for the instance pool are being configured based on the specified instance configuration.
- Starting: The instances are being launched. At this point, the only action you can take is to terminate the instance pool.
- Running: The instances are created and running.
- Stopping: The instances are in the process of being shut down.
- Stopped: The instances are shut down.
- Scaling: After an instance pool has been created, if you update the instance pool size, it will go into this state while creating instances (for increases in pool size) or terminating instances (for decreases in pool size). At this point, the only action you can take is to terminate the instance pool.
- Terminating: The instances and associated resources are being terminated.
- Terminated: The instance pool, all its instances and associated resources are terminated.

## Distributing Instances Across Fault Domains for High Availability

By default, the instances in a pool are distributed across all[fault domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)in a best-effort manner based on capacity. If capacity isn't available in one fault domain, the instances are placed in other fault domains to allow the instance pool to launch successfully.

In a high availability scenario, you can require that the instances in a pool are evenly distributed across each of the fault domains that you specify. When sufficient capacity isn't available in one of the fault domains, the instance pool doesn't launch or scale successfully, and a work request for the instance pool returns an "out of capacity" error. To fix the capacity error, either wait for capacity to become available, or[update the placement configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/updatinginstancepool-updating-placement.htm)(the availability domain and fault domain) for the instance pool.

## Limitations and Considerations

When working with instance configurations and instance pools, keep the following things in mind:
- You cannot delete an instance configuration if it is associated with an instance pool.
- You can use the same instance configuration for multiple instance pools. However, an instance pool can have only one instance configuration associated with it.
- 

If an instance pool has been in the scaling or provisioning state for an extended period, the number of instances requested might exceed the number of instances available. In this scenario, after 24 hours, the instance pool transitions to Running with the available capacity, which might be less than the number of instances requested. The instance pool size updates to reflect the number of instances currently running.
- When this happens, one of the following errors might appear in the work request:`ServiceLimit`,`OutOfCapacity`,`PostLaunchFailure`, or`InvalidParameter`.
- If the number of instances exceeds your tenancy's service limits for that availability domain, you can[check your service limits](https://docs.oracle.com/iaas/Content/General/service-limits/view-tenancy.htm)and[request a service limit increase](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm).
- If you modify the instance configuration for an instance pool, existing instances that are part of that pool don't change. Any new instances that are created after you modify the instance configuration use the new instance configuration. New instances are not created unless you increase the size of the instance pool or terminate existing instances.
- If you decrease the size of an instance pool, to balance the instances across placements ([availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)and[fault domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)), instances are terminated first based on how many instances from the instance pool are in that availability domain and fault domain. Within a placement, the oldest instances are terminated first.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: For a typical policy that gives access to instance pools and instance configurations, see[Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### Propagation of Tagging on Resources

OCI services propagate all of a primary resource's freeform tags and defined tags to secondary resources when both resources support the type of tags. For example, when instance pools create instances, the tags from the instance pool and the instance configuration propagate to the resources created. Resources include instances created by the pool, primary VNICs, secondary VNICs, and boot volumes and block volumes created with the instance. Tags are not propagated to existing instances that are attached to the pool.
