# Extending the Partition for a Block Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm
- Fetched: 2026-09-05 01:46 CDT

# Extending the Partition for a Block Volume

The Oracle Cloud Infrastructure Block Volume service lets you expand the size of block volumes with offline volume resizing. For more information, see[Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm). In order to take advantage of the larger volume size, you need to extend the partition for the block volume. For boot volumes, see[Extending the Partition for a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm).
Note  
  
After a volume has been resized, the first backup on the resized volume will be a full backup. See[Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backuptype)for more information about full versus incremental volume backups.

## Required IAM Policy

Extending a partition on an instance does not require a specific IAM policy. However, you may need permission to run the necessary commands on the instance's guest OS. Contact your system administrator for more information.

## Extending the Partition for a Block Volume on a Linux-Based Image

On Linux-based images, use the following steps to extend the partition for a block volume.

### Prerequisites

After you have resized a volume, you need to attach it to an instance before you can extend the partition and grow the file system. See[Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-volume-attachment.htm)and[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm)for more information.

### Extending the Linux Partition

### Extending a partition

- 

To identify the volume that you want to extend the partition for, run the following command to list the attached block volumes:

```

```

- 

Run the following command to edit the volume's partition table with`parted`:

```

```

&lt;volume_id&gt; is the volume identifier, for example`/dev/sdc`.
- 

When you run`parted`, you may encounter the following error message:
```

```

You are then prompted to fix the error or ignore the error and continue with the current setting. Specify the option to fix the error.
- 

Run the following command to change the display units to sectors so that you can see the precise start position for the volume:

```

```

- 

Run the following command to display the current partitions in the partition table:

```

```

Make note of the values in the Number , Start , and File system columns for the root partition.
- 

Run the following command to remove the existing root partition:

```

```

&lt;partition_number&gt; is the value from the Number column.
- 

Run the following command to recreate the partition:

```

```

At the`Start?`prompt, specify the value from the Start column. At the`File system type?`prompt, specify the value from the File system column. Specify`100%`for the`End?`prompt.
- 

Run the following command to exit`parted`:

```

```

This command forces a rewrite of the partition table with the new partition settings that you specified.
- 

To verify that the root partition was extended, run the following command to list the attached block volumes:

```

```

After you extend the root partition you need to grow the file system. Use the steps applicable to your file system in the following procedure.

### Growing the file system for a partition

- 

Before you grow the file system, repair any issues with the file system on the extended partition by running one of the following commands.

For XFS file systems:

```

```

For ext* file systems:

```

```

&lt;partition_id&gt; is the partition identifier, for example`/dev/sdc1`. See[Checking and Repairing an XFS File System](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_repair_xfs.html)for more information.
- 

After you have confirmed that there are no more issues to repair, you need to create a mount point to run the`xfs_growfs`against. To do this, create a directory and mount the partition to that directory by running the following commands:

```

```

&lt;partition_id&gt; is the partition identifier, for example`/dev/sdc1`, and &lt;directory_name&gt; is the directory name, for example`data`.
- 

After you have created the mount point run one of the following commands to grow the file system.

For XFS file systems:

```

```

&lt;directory_name&gt; is the name for the directory you created in the previous step, for example`data`.

For ext* file systems:

```

```

&lt;partition_id&gt; is the partition identifier.
- 

To verify that the file system size is correct, run the following command to display the file system details:

```

```

## Extending the Partition for a Block Volume on a Windows-Based Image

On Windows-based images, you can extend a partition using the Windows interface or from the command line using the DISKPART utility.

### Windows Server 2016 and Later Versions

The steps to extend a partition for a block volume attached to an instance running Windows Server 2016, Windows Server 2019, Windows Server 2022, or Windows Server 2025 are the same and are described in the following procedures.

### Extending a partition using the Windows interface

- 

Open the[Disk Management](https://docs.microsoft.com/windows-server/storage/disk-management/overview-of-disk-management)system utility on the instance.
- 

Right-select the expanded block volume and select Extend Volume .
- 

Follow the instructions in the Extend Volume Wizard :
- 

Select the disk that you want to extend, enter the size, and then select Next .
- 

Confirm that the disk and size settings are correct, and then select Finish .
- 

Verify that the block volume's disk has been extended in Disk Management.

### Extending a partition using the command line with DISKPART

- 

Open a command prompt as administrator on the instance.
- 

Run the following command to start the DISKPART utility:

```

```

- 

At the`DISKPART`prompt, run the following command to display the instance's volumes:

```

```

- 

Run the following command to select the expanded block volume:

```

```

&lt;volume_number&gt; is the number associated with the block volume that you want to extend the partition for.
- 

Run the following command to extend the partition:

```

```

&lt;increased_size_in_MB&gt; is the size in MB that you want to extend the partition to.
Caution  
  
When using the DISKPART utility, do not overextend the partition beyond the current available space. Overextending the partition could result in data loss.
- 

To confirm that the partition was extended, run the following command and verify that the block volume's partition has been extended:

```

```
