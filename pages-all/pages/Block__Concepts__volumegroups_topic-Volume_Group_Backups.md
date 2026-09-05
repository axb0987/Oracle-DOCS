# Volume Group Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Volume_Group_Backups.htm
- Fetched: 2026-09-05 01:44 CDT

# Volume Group Backups

Back up a volume group for automatic, point-in-time-consistent backups of all the volumes in the volume group.

## Tasks

- [Listing Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-volume-group-backup.htm)
- [Creating a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-volume-group-backup.htm)
- [Updating a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/update-bv-volume-group-backup.htm)
- [Retrieving a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/get-bv-volume-group-backup.htm)
- [Moving a Volume Group Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm)
- [Restoring a Volume Group from a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-bv-volume-group.htm)
- [Copying a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copy-bv-volume-group-backup.htm)
- [Deleting a Volume Group Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/delete-bv-volume-group-backup.htm)

See also[Managing Assigned Backup Policies for Volume Groups (Policy-Based Volume Group Backups)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups_topic-Scheduled_Backups.htm).

## About Backups for Volume Groups

You can perform most of the same backup operations and tasks with volume groups that you can perform with individual block volumes and boot volumes. You can restore a volume group backup to a volume group, or you can restore individual volumes in the volume group from volume backups. With volume group backups, you can manage the backup settings for several volumes in one place, consistently. This simplifies the process to create time-consistent backups of running enterprise applications that span multiple storage volumes across multiple instances.

For a general overview of the Block Volume's service backup functionality, see[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm).

## Source Region

Volume group backups include a Source Region field. This specifies the region for the volume group that the backup was created from. For volume group backups copied from another region, this field shows the region that the volume group backup was copied from.

## Manual Volume Group Backups

Manual backups are on-demand one-off backups that you can launch immediately for volume groups. See[Manual Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#manual).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
