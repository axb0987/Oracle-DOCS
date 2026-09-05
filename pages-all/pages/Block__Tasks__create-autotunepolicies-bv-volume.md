# Dynamic Performance Scaling
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/create-autotunepolicies-bv-volume.htm
- Fetched: 2026-09-05 01:45 CDT

# Dynamic Performance Scaling

Block Volume provides dynamic performance scaling with autotuning. This feature enables you to configure your volumes so that the service adjusts the performance level automatically to optimize performance.

There are two types of dynamic performance scaling with autotuning you can enable for volumes:
- 

[Performance Based Auto-tuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/perf-based.htm): When this option is enabled, Block Volume adjusts the volume's performance between the levels you specify, based on the monitored performance for the volume.
- 

[Detached Volume Auto-tuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detached-perf.htm): When this option is enabled, Block Volume adjusts the volume's performance level based on whether the volume is attached or detached from an instance.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)
