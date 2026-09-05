# Boot Volume Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumebackups.htm
- Fetched: 2026-09-05 01:44 CDT

# Boot Volume Backups

The backups feature of the Oracle Cloud Infrastructure Block Volume service lets you make a crash-consistent backup, which is a point in time snapshot of a boot volume without application interruption or downtime.

You can make a backup of a boot volume while it's attached to a running instance, or you can make a backup of a boot volume while it's detached from the instance. Boot volume backup capabilities are the same as block volume backup capabilities. See[Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm)for more information.

There are two ways you can initiate a boot volume backup, the same as block volume backups. You can either manually start the backup, or assign a policy which defines a set backup schedule. See[Manual Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#manual)and[Policy-Based Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#policy)for more information.

## Tasks

- [Listing Boot Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-boot-volume-backup.htm)
- [Creating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-boot-volume-backup.htm)
- [Getting a Boot Volume Backup's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/get-bv-boot-volume-backup.htm)
- [Updating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/bootv-backup-edit.htm)
- [Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-bv-boot-volume-backup.htm)
- [Copying a Boot Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copyingbootvolumebackupcrossregion.htm)
- [Moving a Boot Volume Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm)
- [Deleting a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/delete-boot-volume-backup.htm)

See also[Creating a Boot Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-boot-volume-backup.htm)and[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm).

## Boot Volume Backup Types

The Block Volume service supports the same backups types for boot volumes as for block volumes:
- Incremental: This backup type includes only the changes since the last backup.
- Full: This backup type includes all changes since the volume was created.

You can restore a boot volume from any of your incremental or full boot volume backups. Both backup types enable you to restore the full boot volume contents to the point-in-time snapshot of the boot volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about.
Note  
  
After a boot volume has been resized, the first backup on the resized boot volume will be a full backup. See[Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/resizingavolume.htm)for more information about volume resizing.

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

When a boot volume backup is created, the source boot volume's tags are automatically included in the boot volume backup. This also includes boot volumes with custom backup policies applied to create backups on a schedule. Source boot volume tags are automatically assigned to all backups when they are created. You can also apply additional tags to volume backups as needed.

When you create an instance from the boot volume backup, the instance is created includes the source boot volume's tags.

## Copying Boot Volume Backups Across Regions

You can copy boot volume backups between regions using the Console, command line interface (CLI), SDKs, or REST APIs. For steps, see[Copying a Boot Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copyingbootvolumebackupcrossregion.htm). This capability enhances the following scenarios:
- Disaster recovery and business continuity: By copying boot volume backups to another region at regular intervals, it makes it easier for you to restore instances in the destination region if a region-wide disaster occurs in the source region.
- Migration and expansion: You can easily migrate and expand your instances to another region.

To copy boot volume backups between regions, you must have permission to read and copy boot volume backups in the source region, and permission to create boot volume backups in the destination region. For more information see[Copying a Boot Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copyingbootvolumebackupcrossregion.htm).

Once you have copied the boot volume backup to the new region you can then restore from that backup by creating a new volume from the backup using the steps described in[Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-bv-boot-volume-backup.htm).

## Differences Between Boot Volume Backups and Clones

Consider the following criteria when you decide whether to create a backup or a clone of a volume.

Criteria Volume Backup Volume Clone
Description Creates a point-in-time backup of data on a volume. You can restore multiple new volumes from the backup later. Creates a single point-in-time copy of a volume without having to go through the backup and restore process.
Use case

Retain a backup of the data in a volume, so that you can duplicate an environment later or preserve the data for future use.

Meet compliance and regulatory requirements, because the data in a backup remains unchanged over time.

Support business continuity requirements.

Reduce the risk of outages or data mutation over time.

Rapidly duplicate an existing environment. For example, you can use a clone to test configuration changes without impacting your production environment.
Speed Slower (minutes or hours) Faster (seconds)
Cost Lower cost Higher cost
Storage location Object Storage Block Volume
Retention policy Policy-based backups expire, manual backups do not expire No expiration
