# Extending the Partition for a Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm
- Fetched: 2026-09-05 01:46 CDT

# Extending the Partition for a Boot Volume

When you create a new virtual machine (VM) instance or bare metal instance based on a platform image or custom image, you have the option of specifying a custom boot volume size.

You can also expand the size of the boot volume for an existing instance. For more information, see[Resizing a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm). To take advantage of the larger size, you need to extend the partition for the boot volume. For block volumes, see[Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm).
Note  
  
After a boot volume has been resized, the first backup on the resized boot volume will be a full backup. For information about full and incremental boot volume backups, see[Boot Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/bootvolumebackups.htm#backuptypes).

## Required IAM Policy

Extending a partition on an instance does not require a specific IAM policy. However, you may need permission to run the necessary commands on the instance's guest OS. Contact your system administrator for more information.

## Extending the Root Partition on a Linux-Based Image

For instances running Linux-based images, you need to extend the root partition and then grow the file system using the`[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)oci-growfs`operation from[OCI Utilities](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm).

## Extending the System Partition on a Windows-Based Image

On Windows-based images, you can extend a partition using the Windows interface or from the command line using the DISKPART utility.

### Windows Server 2016 and Later Versions

The steps for extending a system partition on instances running Windows Server 2016, Windows Server 2019, Windows Server 2022, or Windows Server 2025 are the same and are described in the following procedures.

### Extending the system partition using the Windows interface

- 

Open the[Disk Management](https://docs.microsoft.com/windows-server/storage/disk-management/overview-of-disk-management)system utility on the instance.
- 

Right-select the boot volume and select Extend Volume .
- 

Follow the instructions in the Extend Volume Wizard :
- 

Select the disk that you want to extend, enter the size, and then select Next .
- 

Confirm that the disk and size settings are correct, and then select Finish .
- 

Verify that the boot volume's system disk has been extended in Disk Management.

### Extending the system partition using the command line with DISKPART

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

Run the following command to select the boot volume:

```

```

&lt;volume_number&gt; is the number associated with the boot volume that you want to extend the partition for.
- 

Run the following command to extend the partition:

```

```

&lt;increased_size_in_MB&gt; is the size in MB that you want to extend the partition to.
Caution  
  
When using the DISKPART utility, do not overextend the partition beyond the current available space. Overextending the partition could result in data loss.
- 

To confirm that the partition was extended, run the following command and verify that the boot volume's partition has been extended:

```

```
