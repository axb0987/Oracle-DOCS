# Managing Instance Configurations
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm
- Fetched: 2026-09-05 01:49 CDT

# Managing Instance Configurations

An instance configuration is a template that defines the settings to use when creating Compute instances.

Instance configurations can simplify the management of your Compute instances. The following tasks are available for instance configurations.
- [Listing Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/list-instance-configurations.htm)
- [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/creatinginstanceconfig.htm)
- [Getting an Instance Configuration Details](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/get-instance-configuration.htm)
- [Updating Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/updatinginstanceconfig.htm)
- [Deleting Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/deletinginstanceconfig.htm)
- [Moving an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance_config_moving.htm)
Important  
  
Instance pools rely on instance configurations. For more information see:[Managing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instance-pools.htm)

## Instance Configurations Overview

An instance configuration defines the settings to use when creating compute instances, including details such as the base image, shape, and metadata. You can also specify the associated resources for the instance, such as block volume attachments and network configuration, and you can associate the instance with a[capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/reserve-capacity.htm).

For steps to create an instance configuration, see[Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/creatinginstanceconfig.htm).

To modify an existing instance configuration, create a new instance configuration with the desired settings.

For steps to delete an instance configuration, see[Deleting Instance Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/../Tasks/deletinginstanceconfig.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: For a typical policy that gives access to instance pools and instance configurations, see[Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

### Propagation of Tagging on Resources

OCI services propagate all of a primary resource's freeform tags and defined tags to secondary resources when both resources support the type of tags. For example, when instance pools create instances, the tags from the instance pool and the instance configuration propagate to the resources created. Resources include instances created by the pool, primary VNICs, secondary VNICs, and boot volumes and block volumes created with the instance. Tags are not propagated to existing instances that are attached to the pool.
