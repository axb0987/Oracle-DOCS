# /etc/fstab Options for Block Volumes Using Consistent Device Paths
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm
- Fetched: 2026-09-05 01:45 CDT

# /etc/fstab Options for Block Volumes Using Consistent Device Paths

On Linux instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the`/etc/fstab`file, or the instance may fail to launch.
Note  
  
These steps are for block volumes that are attached with[consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm)enabled. If the block volume does not have consistent device paths enabled, use the[legacy etc/fstab options](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm)instead.

## Prerequisites

- Follow the steps to[attach a volume](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Tasks/attach-compute-volume-attachment.htm)and[connect to the volume](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Tasks/connectingtoavolume.htm).
- 

Create the file system of your choice on the volume using standard Linux tools. For example, run the following command to create an XFS file system:
```

```

If a file system already exists on the volume, you don't need to create another one.
- 

Confirm that the[instance supports consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#images)and is correctly configured. To verify that the volume is attached to a supported instance, connect to the instance and run the following command:

```

```

The output will look similar to the following:
```

```

If you don't see this output and instead see the following error message:
```

```

there may be a problem with the instance configuration for device paths. For assistance with this,[contact Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

## Use the _netdev and nofail Options

By default, the`/etc/fstab`file is processed before the initiator starts. Configure the mount process to initiate before the volumes are mounted by specifying the`_netdev`option on each line of the`/etc/fstab`file.

When you create a custom image of an instance where the volumes, excluding the root volume, are listed in the`/etc/fstab`file, instances will fail to launch from the custom image. To prevent this issue, specify the`nofail`option in the`/etc/fstab`file.

In the example scenario with three volumes, the`/etc/fstab`file entries for the volumes with the`_netdev`and`nofail`options are as follows:

```

```

After you have updated the`/etc/fstab`file, use the following command to mount the volumes:

```

```

Reboot the instance to confirm that the volumes are mounted properly on reboot with the following command:

```

```

## Troubleshooting Issues with the /etc/fstab File

If the instance fails to reboot after you update the`/etc/fstab`file, you may need to undo the changes to the`/etc/fstab`file. To update the file, first[connect to the serial console for the instance](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm). When you have access to the instance using the serial console connection, you can remove, comment out, or fix the changes that you made to the`/etc/fstab`
