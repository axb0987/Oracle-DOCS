# Traditional fstab Options
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm
- Fetched: 2026-09-05 01:45 CDT

# Traditional fstab Options

On Linux instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the`/etc/fstab`file, or the instance may fail to launch.
Note  
  
These steps are for block volumes that do not have[consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm)enabled. If consistent device paths are enabled for the block volume, use the[/etc/fstab options for block volumes using consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm)instead.

## Volume UUIDs

On Linux operating systems, the order in which volumes are attached is non-deterministic, so it can change with each reboot. If you refer to a volume using the device name, such as`/dev/sdb`, and you have more than one non-root volume, you can't guarantee that the volume you intend to mount for a specific device name will be the volume mounted.

To prevent this issue, specify the volume UUID in the`/etc/fstab`file instead of the device name. When you use the UUID, the mount process matches the UUID in the superblock with the mount point specified in the`/etc/fstab`file. This process guarantees that the same volume is always mounted to the same mount point.

### Determining the UUID for a Volume
- 

Follow the steps to[attach a volume](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Tasks/attach-compute-volume-attachment.htm)and[connect to the volume](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Tasks/connectingtoavolume.htm).
- 

After the volumes are connected, create the file system of your choice on each volume using standard Linux tools.

The remaining steps assume that three volumes were connected, and that an XFS file system was created on each volume.
- 

Run the following command to use the blkid utility to get the UUIDs for the volumes:

```

```

The output will look similar to the following:
```

```

The root volume in this output is`/dev/sda*`. The additional remote volumes are:
- `/dev/sdb`
- `/dev/sdc`
- `/dev/sdd`
- 

To automatically attach the volumes at`/mnt/vol1`,`/mnt/vol2`, and`/mnt/vol3`respectively, create the three directories using the following commands:

```

```

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
