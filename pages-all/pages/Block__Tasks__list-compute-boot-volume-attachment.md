# Listing Attachments for a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-boot-volume-attachment.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Attachments for a Boot Volume

Learn how to list attachments for a boot volume.

When a boot volume has no attached instances, then either the boot volume was detached from the associated instance or the instance was terminated (while the boot volume was preserved).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to list volume attachments. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-boot-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-boot-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-boot-volume-attachment.htm#)
- 

- On the Boot Volumes list page, select the boot volume that you want. If you need help finding the list page or the boot volumes, see[Listing Boot Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-bv-boot-volume.htm).
- Select Attached instances .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/list.html)oci compute boot-volume-attachment list`command and specify the`--availabilty-domain`and`--compartment-id`parameters to view the boot volumes in that availability domain and compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/ListBootVolumeAttachments)ListBootVolumeAttachments`operation and specify the`availabilityDomain`and`compartmentId`
