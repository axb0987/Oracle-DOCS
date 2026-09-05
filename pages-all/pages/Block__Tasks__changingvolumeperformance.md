# Changing the Performance of a Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm
- Fetched: 2026-09-05 01:45 CDT

# Changing the Performance of a Volume

The Block Volume service enables you to dynamically configure the performance level for block volumes and boot volumes.

For more information, see[Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumeperformance.htm).

If you configure performance level for a block volume to the ultra high performance level the volume attachment should be multipath-enabled. You may need to take additional steps to optmize the volume's performance, for more information, see[Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm#multipath). This does not apply to boot volumes configured for the ultra high performance level.
Note  
  
When you change a block volume's performance to ultra high performance from any other performance level you need to detach and then reattach the volume. See[Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)and[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).

## Tasks

- [Changing the Performance of an Existing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/update-performance-block-bv-volume.htm)
- [Changing the Performance of an Existing Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/update-performance-boot-bv-volume.htm)

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Limitations

- 

When you adjust the VPUs/GB setting for a volume, the volume's lifecycle state transitions to Provisioning while service updates the settings. During this process, you can't attach the volume to an instance or perform other volume operations. After this process is complete, the volume lifecycle state transitions back to Available . At this point, you can attach the volume to an instance.
-
