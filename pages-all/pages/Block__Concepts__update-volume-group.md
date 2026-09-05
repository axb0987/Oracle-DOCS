# Updating a Volume Group
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm
- Fetched: 2026-09-05 01:44 CDT

# Updating a Volume Group

Update a volume group in the Block Volume service. For example, add or remove block volumes or boot volumes.
When you update a volume group, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm#)
- 

- On the Volume Groups list page, select the volume group you want to update. If you need help finding the list page or the volume group, see[Listing Volume Groups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/list-volume-group.htm).
- On the details page, select Edit .
- Select Next .
- To add a block volume or boot volume:
- Select Additional Volume .
- Select the compartment that contains the volume that you want to add.
- (Optional) Select the cluster placement group for the volume you want to add.
- Select the volume that you want to add.

Note  
  
For both block volumes and boot volumes:
- You can't add a volume with an existing backup policy assignment to a volume group with a backup policy assignment. Remove the backup policy assignment from the volume before you add it to the volume group.
- If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
- Select X for the volume that want to remove.

Note  
  
When you remove the last volume in a volume group, the volume group is terminated.
- Select Next .
- (Optional) Enable or disable cross-region replication.
- Select Next .
- (Optional) Add or update the backup policy for the group.
- Select Next .
- Review your changes in the Summary section.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html)oci bv volume-group update`command and required parameters to update a volume group:

```

```

You can update the volume group display name along with adding or removing volumes from the volume group. The volume group is updated to include only the volumes specified in the update operation. This means that you must specify the volume IDs for all of the volumes in the volume group each time you update the volume group.

The following example changes the volume group's display name for a volume group with two volumes:

```

```

If you specify volumes in the command that are not part of the volume group they are added to the group. Any volumes not specified in the command are removed from the volume group.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup)UpdateVolumeGroup`operation and specify the`volumeGroupId`attribute in the request body and optionally the`definedTags`,`displayName`,`freeformTags`,`volumeGroupReplicas`, and/or`volumeIds`attributes in the[`UpdateVolumeGroupDetails`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeGroupDetails)
