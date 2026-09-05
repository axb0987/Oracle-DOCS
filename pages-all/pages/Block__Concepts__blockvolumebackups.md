# Block Volume Backups
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm
- Fetched: 2026-09-05 01:44 CDT

# Block Volume Backups

The Oracle Cloud Infrastructure Block Volume service offers a secure, cost-effective, policy-based, fully-managed backup solution.

Block volumes, boot volumes, and volume groups can be backed up while attached to or detached from an instance, and are then encrypted and regionally stored in[Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm). Backups can be restored to existing or new volumes in any availability domain, irrespective of the availability of the source volume or volume group. This capability allows you to easily restore the volumes or volume groups in the event of a disaster. You can create up to 100,000 backups.
Note  
  
While a backup is in progress, the volume being backed up can't be deleted.

## Tasks

- [Listing Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/list-bv-backup.htm)
- [Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-backup.htm)
- [Updating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/bv-backup-edit.htm)
- [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-to-new-volume-bv-volume-backup.htm)
- [Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copy-bv-backup.htm)
- [Moving a Block Volume Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/change-volume-backup-compartment-bv-volume-backup.htm)
- [Deleting a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/delete-bv-backup-volume.htm)

See also[Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-backup.htm)and[Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm).

## Required IAM Policy for Volume Backups

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

To get started with the volume backups, an administrator needs to grant user access through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

Example policy to allow block volume administrators to manage block volumes, backups, and volume groups across regions:

```

```

Example policy to allow boot volume backup administrators to create and manage only boot volume backups:
```

```

Tip  
  
When users create a backup from a volume or restore a volume from a backup, the volume and backup don't have to be in the same compartment . However, users must have access to both compartments.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Required IAM Policies for Backup Retention Features

To use backup retention features including retention lock, deletion prevention, and indefinite hold, an administrator needs to grant user access through an IAM policy. Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

First, create groups to manage retention features. For details, see[Managing Groups](https://docs.oracle.com/iaas/Content/Identity/groups/managinggroups.htm). Example group names are provided in the following example.

The following example policy allows specific retention feature groups to manage backup retention features across a tenancy:

```

```

The following example policy allows specific retention feature groups to manage backup retention features in a compartment:

```

```

## Volume Backup Types

The following are backup types available in Block Volume:
- Incremental: This backup type includes only the changes since the last backup.
- Full: This backup type includes all changes since the volume was created.

### Volume Group Backups

A volume group is a consistent group of volumes. You can use volume group backups to create point-in-time snapshots for multiple block volumes such as large filesystems and databases. These snapshots are stored in Object Storage. For more information, see[Working with Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../blockvolumes.htm).

### Backup Details

For data recovery purposes, no functional difference exists between an incremental backup and a full backup. Because both backup types enable you to restore the full contents to the point-in-time snapshot, you don't need to retain the initial full backup or subsequent incremental backups. A volume backup retains all of that volume's contents, regardless of the time of its snapshot.
Important  
  

If you delete a full backup of a volume, (for example, because of retention policies), the size of the incremental backup for that volume increases to restore the volume successfully.

In cases where an incremental backup needs to get promoted to a full backup, the "promotion" process might take a little time. During this interim period, the incremental backup sizes remain small. After the "promotion" is complete, the size of that backup (and the resulting quantity billed) might go up.

### Example

You create a 50 GB block volume, write 25 GB to the volume, and then launch a full backup of the volume on Day 1 with a two-day retention period. Upon completion, the backup size is 25 GB.

On Day 2, you then modify 2 GB of existing data, write 3 GB of new data and create an incremental backup. The unique size of the incremental backup totals 5 GB.

On Day 3, another incremental backup is made with modified 3 GB of existing data and added 2 GB of new data, totaling 5 GB.

On Day 4, the full backup is deleted as the retention expires. The incremental backup size now totals 28 GB, the contents of which are required to restore the volume contents to the time the incremental backup was taken.

On Day 5, the first incremental backup retention expires. The backup size for this second incremental backup totals 30 GB, the actual size of the volume contents at the time the second incremental backup was made. Because the blocks are retained even after the full backup was deleted, the volume can still be restored from an incremental backup.

## Volume Backup Size

Volume backup size might be larger than the current volume usage. Possible reasons for a larger backup size could include:
- Any part of a volume that has been written to is considered initialized, and is always included in a volume backup.
- Many operating systems write or zero out the content, which marks these blocks as used. Block Volume service considers these blocks updated and includes them in the volume backup.
- Volume backups also include metadata, which can be up to 1 GB in other data. For example, in a full backup of a 256 GB Windows boot disk, you might see a backup size of 257 GB, which includes an extra 1 GB of metadata.
Note  
  
After a volume has been resized, the first backup on the resized volume will be a full backup. See[Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/resizingavolume.htm)for more information about volume resizing.

## Backup Methods

Backups can be initiated manually or by assigning a backup policy. The backups for a volume are created in the same compartment as the volume. If volumes in a volume group are stored in different compartments, then the volume backups are stored in the volume's compartment and not in volume group's compartment. Volume group backup resources are in the volume group's compartment.

### Manual Backups

You can perform single incremental or full backups for volumes or volume groups. See[Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype)for more information.

To manually back up a volume, see[Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-backup.htm).
Note  
  

Backups can take hours during peak times, and completion times can vary based on the time the backups are initiated and by region. Large full and incremental backups can take longer based on the amount of data that must be copied.

### Policy-Based Backups

You can also define backup policies to simplify and automate the snapshot management and scheduling for a volume or volume group without affecting application performance.

Following are the kinds of backup policies:
- [Oracle-defined](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm#Oracle): Predefined backup policies that have a set backup frequency and retention period. You can't change these policies.
Note  
  
As of November 23, 2021, Oracle-defined policies no longer include full backups. For more information, see[Full backups removed from Oracle defined backup policies](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic-BlockVolume).
- [User-defined](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm#custom): Custom backup policies that you create and configure schedules and retention periods for.

You can also enable scheduled cross-region automated backups with user-defined policies. For more information, see[Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm#CrossRegionCopy).

## Copying Block Volume Backups Across Regions

[Copying block volume backups between regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copy-bv-backup.htm)enhances the following scenarios:
- Disaster recovery and business continuity: By copying block volume backups to another region at regular intervals, you can easily rebuild applications and data in the destination region if a region-wide disaster occurs in the source region.
- Migration and expansion: You can easily migrate and expand your applications to another region.

You can also enable scheduled cross-region automated backups with user-defined policies. See[Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/schedulingvolumebackups.htm#CrossRegionCopy).

To copy volume backups between regions, you must have permission to read and copy volume backups in the source region, and permission to create volume backups in the destination region. For more information, see[Copying a Volume Backup Between Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/copy-bv-backup.htm).

After you copy the volume backup to the new region, you can restore from that backup by creating a new volume from the backup using the steps described in[Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-to-new-volume-bv-volume-backup.htm).

## Volume Backup Encryption

The Oracle Cloud Infrastructure Block Volume service always encrypts all block volumes, boot volumes, and volume backups at rest by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption.

The Oracle Cloud Infrastructure Vault service enables you to bring and manage your own keys to use for encrypting volumes and their backups. When you create a volume backup, the encryption key used for the volume is also used for the volume backup.

You can change the encryption key for the volume backup to another Vault encryption key, or to an Oracle-managed key. See[Changing the Assigned Master Encryption Key](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/assign-encryption-key.htm)for more information.

When you restore the backup to create a new volume you configure a new key, see[Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-to-new-volume-bv-volume-backup.htm). See also[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
Important  
  

By default, volumes restored from a volume backup or a volume group backup are configured to use Oracle-provided keys for encryption. For volumes restored from a volume backup, you can specify a customer-managed key for the new volume during the restore process. This option is not available for volumes restored from volume group backups, so the new volumes are restored with Oracle-provided keys. You can update the encryption keys for these volumes after they are restored, see[Editing a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm).

If you don't configure a volume to use the Vault service, the Block Volume service uses the Oracle-provided encryption key instead. This applies to both encryption at-rest and in-transit encryption.

## Monitoring Backups

You can monitor backups using backup events, which are generated on all successful or failed backups. For more information, see[Using Events to Notify When a Volume Backup Fails](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/backupstatusevents.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Best Practices When Creating Block Volume Backups

When creating and restoring from backups, keep in mind the following:
- 

Backup your critical application volumes multiple times daily . For mission-critical applications, we recommend that you take multiple backups per day to minimize the possible recovery point objective (RPO).
Note  
  
With policy-based backups you can only schedule one backup and copy per day. Users can use manual backups to initiate multiple backups in a day. For cross region copy, we recommend copying only one backup per day to the remote region. For even smaller RPO, review our replication support.
- Configure retention and expiry times for your backups. Backups are automatically purged after the set expiry time to free storage space and costs. Manual backups don't expire.
- 

Schedule or create your backups during off-peak hours. If you notice your backups aren't completing at the expected time, consider changing your scheduled or manual backup times to a different time of day. A daily backup still completes in less than 24 hours.
- 

Organize critical and non-critical data. To reduce the amount of backups needing to be managed, we recommend using separate creation, backup and recovery operations for critical and non-critical data. Critical data typically includes all the data that's required for application recovery and use. Best practice is to keep critical data in a secondary block volume instead of your boot volume. Non-critical data includes swap, temporary, cache or page files and non-critical logs, and tends to be larger in size.
- Use volume groups to create cross-volume, crash-consistent backups. When your data is spread across multiple volumes, you can create and back them up as a volume group. Because the volume group backups consistently capture all of the data synced to each volume, you no longer need to shut down your instances to take individual snapshots. This method is ideal for filesystems and applications that support journaling.
- Maximize data recoverability and recover time with app-consistent backups. You can achieve app-consistent backups by pausing or quiescing your service before initiating a backup. This can include stopping all I/O operations, syncing all memory buffers, and flushing in-flight transactions. You can then send an API call to back up a volume or volume group.
- Before creating a backup, ensure that the data is consistent: Sync the file system, unmount the file system if possible, and save your application data. Only the data on the disk is backed up. When creating a backup, after the backup state changes from REQUEST_RECEIVED to CREATING, you can return to writing data to the volume. While a backup is in progress, the volume that's being backed up can't be deleted.
- To attach a restored volume that has the original volume attached, you might need to change the partition IDs first. This requirement comes from operating systems that don't allow you to restore identical volumes. For instructions on changing partition IDs, see your operating system's documentation.

See[Creating a Block Volume Backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-bv-backup.htm)and[Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/create-restore-to-new-volume-bv-volume-backup.htm)for more information.

## Planning Your Backup

The primary use of backups is to support business continuity, disaster recovery, and long-term archiving requirements. When determining a backup schedule, consider the following aspects in your backup plan and goals:
- Frequency: How often you want to back up your data.
- Recovery time: How long you can wait for a backup to be restored and accessible to the applications that use it. While the time for a backup to complete varies on several factors, the time is typically a few minutes or longer, depending on the size of the data being backed up and the amount of data that has changed since your last backup.
- Number of stored backups: How many backups you need to keep available and the deletion schedule for those you no longer need. You can only create one backup at a time, so if a backup is underway, that backup needs to complete before you can create another one. For details about the number of backups you can store, see[Performance Details for Shapes](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details).

The common use cases for using backups are:
- 

Needing to create multiple copies of the same volume. Backups are highly useful in cases where you need to create many instances with many volumes that need to have the same data formation.
- Taking a snapshot of your work that you can restore to a new volume at a later time.
- Ensuring you have a spare copy of your volume in case something goes wrong with your primary copy.

## Reducing Volume Backup Sizes with SCSI UNMAP

Oracle Cloud Infrastructure Block Volume supports SCSI UNMAP commands for both boot volumes and block volumes to reclaim unused space. Use these commands to reduce your backup sizes, resulting in faster backup restore times. See[Support for SCSI UNMAP](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/reducingbackupsizewithtrim.htm)for more information.

## Differences Between Block Volume Backups and Clones

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
Volume groups Supported. You can back up a volume group. Supported. You can clone a volume group.

For background information and steps to clone a block volume, see[Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/../Tasks/cloningavolume.htm)
