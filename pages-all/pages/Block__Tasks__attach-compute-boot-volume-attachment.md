# Attaching a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm
- Fetched: 2026-09-05 01:45 CDT

# Attaching a Boot Volume

Learn how to reattach a volume after it's been detached from an associated instance.

Note  
  
An instance must be stopped before its respective boot volume can be detached, and a detached boot volume can only be reattached to replace an existing boot volume for a different instance. For more information, see[Replacing a boot volume](https://docs.oracle.com/iaas/Content/Compute/Tasks/replacingbootvolume.htm).

If a boot volume has been detached from the associated instance, you can reattach it to the instance. To restart an instance with a detached boot volume, you must reattach the boot volume using the steps described in this topic.

If a boot volume has been detached from the associated instance, or if the instance is stopped or terminated, you can attach the boot volume to another instance as a data volume. For steps, see[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to attach and detach existing block volumes. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect your ability to attach block volumes to compute instances.
- 

The boot volume for a compute instance in a security zone must also be in the same security zone.
- 

A compute instance that isn't in a security zone can't be attached to a boot volume that is in a security zone.

## Steps

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- Select Attached instances .
- Select the boot volume's attachment type.
- Select the boot volume's compartment.
- Select the boot volume.
- Select the instance you want to attach the both volume to in the drop-down menu, or by entering the instance OCID.
- (Optional) Select Require CHAP credentials to use iSCSI security protocol CHAP for authentication between the instance and volume.
- (Optional) Select Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes to run iSCSI commands automatically when connecting an iSCSI volume to Linux-based instances.
- 

Select You can[start the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm)when the boot volume's state is Attached .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/attach.html)oci compute boot-volume-attachment attach`command and specify the`--boot-volume-id`and`--instance-id`parameters to attach the volume to the instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/AttachBootVolume)AttachBootVolume`
