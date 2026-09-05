# Detaching a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detach-compute-boot-volume-attachment.htm
- Fetched: 2026-09-05 01:46 CDT

# Detaching a Boot Volume

If a boot volume issue is causing a compute instance issues, you can stop the instance and detach the boot volume, then attach it to another instance as a data volume to troubleshoot it.

You can only detach a boot volume from an instance when the instance is stopped. See[Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm)for information about managing an instance's state.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to attach and detach existing block volumes. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detach-compute-boot-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detach-compute-boot-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detach-compute-boot-volume-attachment.htm#)
- 

- On the Boot Volumes list page, select the boot volume you want to work with. If you need help finding the list page or the boot volume, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-bv-boot-volume.htm).
- On the details page, select Attached instances .
- Select the Actions menu (three dots) for the boot volume, and then select Detach Boot Volume .
- Select Continue Detachment .

You can now attach the boot volume to another instance. For more information, see[Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm).
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/detach.html)oci compute boot-volume-attachment detach`command and specify the`--boot-volume-id`parameter to attach the volume to the instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DetachBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/DetachBootVolume)operation and specify the`bootVolumeAttachmentId`
