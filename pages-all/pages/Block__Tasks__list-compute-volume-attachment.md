# Listing Attachments for a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-volume-attachment.htm
- Fetched: 2026-09-05 01:46 CDT

# Listing Attachments for a Block Volume

Learn how to view a list all volume attachments in a specific compartment, as well as detailed information on a single volume attachment.

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances)includes the ability to list volume attachments. The policy in[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups)lets the specified group do everything with block volumes and backups, but not launch instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/list-compute-volume-attachment.htm#)
- 

- On the Block Volumes list page, select the volume that you want. If you need help finding the list page or the volumes, see[Listing Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/listingvolumes.htm).
- On the details page, select Attached Instances .

All of the block volume's attached instances in the selected compartment are displayed in the list.
Note  
  
To view volume attachments from Compute:
- On the Compute Instances list page, select the instance that you want to view. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/list-instances.htm).
- On the details page, perform one of the following actions depending on the option that you see:
- Select Storage and then scroll down to Attached block volumes .
- Select Attached Block Volumes .

All block volumes attached to the instance are displayed in the list, regardless of the compartment the block volumes are in.
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/list.html)oci compute volume-attachment list`command and specify the required parameters to list volume attachments.

To view volume attachments in a compartment:

```

```

Note  
  
This operation only returns the attached instances that are in the specified compartment. You must run this operation for every compartment that might contain instances that are attached to the specified volume.

To view volume attachments for an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/ListVolumeAttachments)ListVolumeAttachments`operation and specify the`compartmentId`attribute to view a list of a volume attachments in a compartment. To filter the list, also specify one or both of the following parameters:`instanceId`or`volumeId`.
Note  
  

- This operation returns attached instances in the compartment you specify. To return all attached instances for the volume, run this operation for every compartment that might contain instances.
- To get detailed information on a single attachment, use[GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)
