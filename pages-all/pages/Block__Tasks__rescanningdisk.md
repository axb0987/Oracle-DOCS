# Rescanning the Disk for a Block Volume or Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm
- Fetched: 2026-09-05 01:47 CDT

# Rescanning the Disk for a Block Volume or Boot Volume

The Oracle Cloud Infrastructure Block Volume service lets you expand the size of block volumes and boot volumes while they are online and attached to instances. For more information, see[Online Resizing a Block or Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/update-online-resize-block-boot-volume.htm). After the volume is provisioned, you need to run commands to rescan the disk, so that the operating system identifies the expanded volume size. You will need to run different rescan commands depending on the operating system of the attached instance. This topic describes some procedures you can use to rescan the disk.

## Required IAM Policy

Rescanning the disk does not require a specific IAM policy. However, you may need permission to run the necessary commands on the instance's guest OS. Contact your system administrator for more information.

## Rescanning the Disk for Volumes Attached to Linux-Based Instances

For volumes attached to Linux-based instances, run the following commands rescan the disk for a block volume:

```

```

These commands are also displayed in the dialog that opens after you select Save Changes in the Edit Size or Performance dialog, and you can copy them from that dialog.

### Next Steps

After you've rescanned the disk, you need to extend the partition. See[Extending the Partition for a Block Volume on a Linux-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#exBlockLinux)for block volumes. For boot volumes, use the`[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)oci-growfs`operation from[OCI Utilities](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm).

## Rescanning the Disk for Volumes Attached to Windows Instances

### Using Disk Management or diskpart

For volumes formatted as FAT32 or NTFS, you can rescan the disk using the Windows interface, in Disk Management , or you can use the[diskpart utility](https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart)'s rescan command from the command line.

[Rescanning the disk using the command line with DISKPART](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#)

- 

Open a command prompt as administrator on the instance.
- 

Run the following command to start the[diskpart utility](https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart):

```

```

- 

At the`DISKPART`prompt, run the following command:

```

```

[Rescanning the disk using the Windows interface](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#)

- 

Open the[Disk Management](https://docs.microsoft.com/windows-server/storage/disk-management/overview-of-disk-management)system utility on the instance.
- 

Select Action , and then select Rescan Disks .

[Update disk information](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2003/cc786898(v=ws.10)).

#### Using Cygwin

For volumes formatted with a non-native Windows file system, such as volumes formatted using[Oracle Automatic Storage Management (Oracle ASM)](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmcon.htm), you can't use the Windows interface or the diskpart utitily. Instead, you can use the`dd`process from a Cygwin terminal to rescan the disk. You can also use this for native Windows file systems. For more information, see[Cygwin](https://cygwin.com/).

#### Next Steps

After you've rescanned the disk, you need to extend the partition. For block volumes, see[Extending the Partition for a Block Volume on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#exBlockWindows). For boot volumes, see[Extending the System Partition on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extendin)
