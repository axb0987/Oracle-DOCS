# Connecting to Volumes With Consistent Device Paths
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm
- Fetched: 2026-09-05 01:44 CDT

# Connecting to Volumes With Consistent Device Paths

Oracle Cloud Infrastructure supports consistent device paths for block volumes that are attached to compatible Linux-based instances. When you attach a block volume to an instance, you can select a device path that remains consistent between instance reboots. This enables you to use a consistent device path when you refer to the volume to perform tasks such as:
- 

Creating partitions.
- 

Creating file systems.
- 

Mounting file systems.
- 

Specifying options in the`/etc/fstab`file to ensure that volumes are mounted properly when automatically mounting volumes on instance boot. For more information, see[/etc/fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm).

When you use consistent device paths on compatible Linux-based instances, the boot volume's device path is:

```

```

Note  
  
Device paths are required when attaching a volume configured for the Ultra High Performance level.
Note  
  
Device paths are not available when you attach a boot volume as a data volume to a second instance.

## Images that Support Consistent Device Paths

Consistent device paths are supported and enabled by default on instances when all of the following things are true:
- The instance was created using a[platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm).
- The image is a Linux-based image.
- The image was released in November 2018 or later. For specific version numbers, see[Image Release Notes](https://docs.oracle.com/iaas/images/).
- The instance was launched after January 11, 2019.

For instances launched using the image OCID or an existing boot volume, if the source image supports consistent device paths, the instance supports device paths.

Consistent device paths are not enabled by default for Linux-based partner images and custom images created from other sources. You can enable consistent device paths for these images by[editing the image capabilities](https://docs.oracle.com/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm)for the custom image using the steps described below. This feature does not apply to Windows-based images.

[To enable consistent device paths for a custom image](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#)

- Open the navigation menu and select Compute . Under Compute , select Custom Images .
- 

Select the custom image that you want to enable consistent device paths for.
- 

Select Edit image capabilities .
- 

In the Consistent volume naming section select Enabled .
- 

Select Save changes .

## Device Paths in the Console

You select a device path when you[attach a block volume to an instance](https://docs.oracle.com/en-us/iaas/Content/Block/References/../Tasks/attach-compute-volume-attachment.htm).

If you specify a device path, the path appears in the Attached Block Volumes list for an instance, in the Device Path field.

## Device Paths on the Instance

Use the following sample commands to perform various configuration tasks on the attached volume. Commands are provided for volumes that use consistent device paths and for volumes that don't.

[Creating a partition with fdisk](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#)

- 

No device path specified:

```

```

- 

Device path specified:

```

```

[Creating an ext3 file system](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#)

- 

No device path specified:

```

```

- 

Device path specified:

```

```

[Updating the /etc/fstab file](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#)

- 

No device path specified:

```

```

- 

Device path specified:

```

```

[Mounting the file system](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#)

- 

No device path specified:

```

```

- 

Device path specified:

```

```
