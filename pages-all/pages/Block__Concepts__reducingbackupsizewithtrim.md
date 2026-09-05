# Support for SCSI UNMAP
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/reducingbackupsizewithtrim.htm
- Fetched: 2026-09-05 01:44 CDT

# Support for SCSI UNMAP

Block Volume enables you to configure your applications to send SCSI UNMAP commands to both boot volumes and block volumes to reclaim unused space. Using SCSI UNMAP provides a significant reduction in your backup sizes and can also result in faster backup restore and volume clone times. The SCSI UNMAP commands are similar to the TRIM commands you can send to SSD drives to reclaim unused space.

You send an SCSI UNMAP command to tell the storage subsystem to discard and free up the blocks that are deleted or no longer in use by an application or by the file system. If you don't send this command, the storage subsystem does not know that the blocks are no longer in use, and it continues to include these blocks in all backups and clones to new volumes. After the storage subsystem receives the UNMAP command for the blocks, the corresponding blocks are discarded and freed, so they are excluded from future backups and clones.

The Block Volume UNMAP functionality is implemented using the SCSI UNMAP commands. UNMAP is supported for both ISCSI and paravirtualized volume attachment types.

UNMAP is a nondeterministic command, and it is not guaranteed that all the requested blocks are discarded immediately when you use the command. The time it takes to discard the blocks on a device depends on the following factors:
- 

The number of unused blocks on the file system. UNMAP on a device with more unused blocks will take longer to complete.
- 

The[performance level](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels)(VPU/GB setting) configured for the block volume.
- 

For file systems, it depends on the guest file system's implementation, which varies from file system to file system.

## Enabling UNMAP for Volumes Attached Prior to June 14, 2023

UNMAP is enabled by default for both boot volumes and block volumes for all new attachments. For volumes attached prior to June 14, 2023, use the commands below to check if UNMAP is already enabled or not and if not, take the recommended actions to enable it.

### Checking if UNMAP is Already Enabled

#### Linux

Use the`lsblk -D`command to check if UNMAP is enabled for a volume. If UNMAP is enabled, the`DISC-GRAN`and`DISC-MAX`columns in the output will have non-zero values. If the values for the`DISC-GRAN`and`DISC-MAX`columns in the output are zeros, the UNMAP functionality is not enabled. See for how to enable UNMAP.

The following screenshot contains sample output for the`lsblk -D`command on volumes that have UNMAP enabled.

[

#### Windows

SCSI UNMAP is enabled by default.

### Enabling UNMAP

To enable UNMAP functionality for a volume, perform one of the following actions, depending on the volume's attachment type. These actions apply to all operating systems.
- 

iSCSI attachments : Use the iSCSI commands to log out and then log in again.
- 

Paravirtualized attachments : Detach and then reattach the instance to the volume.

## Using UNMAP with the File System

You can configure the file system to issue UNMAP commands to discard deleted or unused blocks by the file system. This reduces your volume backup sizes.

### Linux

#### Commands to issue UNMAP manually

Run the`fstrim`command to issue UNMAP commands to the backend to discard and free up the deleted or unused blocks by the file system.

#### Commands to issue UNMAP periodically

You can enable the systemctl timer to periodically run the filesystem UNMAP command`fstrim`. The timer automatically runs the`fstrim`command on all mount points once a week.

To enable the timer:
```

```

To check the status of the timer:
```

```

#### Commands to enable Online Block Discard

You can specify file system mount options to issue the discard commands immediately when a block is deleted, or no longer used. This immediately sends the UNMAP commands to the backend storage system when a file is deleted or the file size is reduced. Use caution with this option as it is known to cause some performance issues with the file system even though there is no performance impact on the backend device by enabling UNMAP.

Mount command to specify online block discard:
```

```

You can update the`/etc/fstab`file to append`discard`to the mount options, for example:
```

```

### Windows

From a command window on the instance, run the following command to enable UNMAP, if it is not enabled already:
```

```

## No Performance Impact

When you use the UNMAP command, it does not impact a volume's performance. The guaranteed IOPS and throughput will not be impacted. However, the time it takes to process the UNMAP commands depends on the performance level configured for a volume.

For example,`fstrim`
