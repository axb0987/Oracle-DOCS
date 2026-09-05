# Linux: Recovering a Corrupted Boot Volume
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm
- Fetched: 2026-09-05 01:47 CDT

# Linux: Recovering a Corrupted Boot Volume

If your instance fails to boot successfully or boots with the boot volume set to read-only access, the instance's boot volume may be corrupted. While it is rare, boot volume corruption can occur in the following scenarios:
- 

When an instance experiences a forced shutdown using the API.
- 

When an instance experiences a system hang due to an operating system or software error and a graceful reboot or shutdown of the instance times out, and then a forced shutdown occurs.
- 

When an error or outage occurs in the underlying infrastructure and there were critical disk writes pending in the system.
Important  
  
In most cases a simple reboot will resolve boot volume corruption issues, so this is the first action you should take when troubleshooting this.

This topic describes how to determine if your Linux-based instance's boot volume is corrupted and what steps to take to troubleshoot and recover the corrupted boot volume. For Windows instances, see[Windows: Recovering a Corrupted Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringwindowsbootvolume.htm).

## Detecting Boot Volume Corruption

Boot volume corruption can prevent an instance from booting successfully, so you might not be able to connect to the instance using SSH. Instead, you can use the instance console connection feature to connect to the malfunctioning instance. For more information about using this feature, see[Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).

This section describes how to use a serial console connection to detect if boot volume corruption has occurred.
Tip  
  
If you have already confirmed your instance's boot volume is corrupted or if you are using an imported custom image, proceed to the[Recovering the Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm#recover)section, which describes how to use a second instance along with standard file system tools to both detect and repair boot volume corruption.
- [Create a serial console connection for the instance](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Creating).
- 

[Connect to the instance through serial console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti2).

At this point, it's normal for the serial console to appear to hang, as the system may have already crashed.
- [Reboot the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm)from the Console.
- 

Once the reboot process starts, switch back to the terminal window, and you should see system messages from the instance start to appear in the window.
- 

Monitor the messages that appear as the system is starting up. Most operating systems will set the boot volume to read-only as soon as disk corruption is detected to prevent writes from further corrupting the volume, so look for messages that indicate the boot volume is in read-only mode. Following are some examples:
- 

On an instance with iSCSI-attached boot volumes, the`iscsiadm`service will fail to attach a volume because the volume is in read-only mode. This will typically prevent instances from continuing to boot. The serial console may display a message similar to the following:
```

```

- 

On an instance with paravirtualized-attached boot volumes, the system may continue the boot process, but will be in a degraded state because nothing can be written to the boot drive.The serial console may display error messages similar to the following:
```

```

The error messages and system behavior described here are the most commonly seen for boot volume corruption, however depending on the operating system, you may see different error messages and system behavior. If you don't see the ones described here, consult the documentation for your operating system for additional troubleshooting information.

## Recovering the Boot Volume

To troubleshoot and recover the corrupted boot volume, you need to detach the boot volume from the instance and then attach the boot volume to a second instance as a data volume.

### Detaching the Boot Volume

If you have detected that your instance's boot volume is corrupted, you need to detach the boot volume from the instance before you can begin troubleshooting and recovery steps.
- [Stop the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).
- [Detach the boot volume from the instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detach-compute-boot-volume-attachment.htm).

### Attaching the Boot Volume as a Data Volume to a Second Instance

For the second instance, we recommend that you use an instance running an operating system that most closely matches the operating system for the boot volume's instance. You should only attach boot volumes for Linux-based instances to other Linux-based instances. The second instance must be in the same availability domain and region as the boot volume's instance. If no existing instance is available, create a new Linux instance using the steps described in[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). Once you have the second instance, make sure you can log into the instance and that it is functional before proceeding with the recovery steps. For steps to access the instance, see[Connecting to a Linux Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm). After you have confirmed that the instance is functional, perform the following steps.
- 

Run the`lsblk`command and make note of the drives that are currently on the instance, for example:
```

```

- Attach the boot volume to the second instance as a data volume. For more information, see[Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attach-compute-boot-volume-attachment.htm).

[To attach the boot volume as a data volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm#)

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the instance that you want to attach a volume to.
- Under Resources , select Attached Block Volumes .
- Select Attach Block Volume .
- 

Select the volume attachment type. If Paravirtualized attachments are available for this instance, we recommend that you select this attachment type for this procedure.

If you select iSCSI as the volume attachment type, you need to connect to the volume, see[Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm)for more information.
- In the Block Volume Compartment drop-down list, select the compartment.
- Choose the Select Volume option and then select the volume from the Boot Volume section of the Block Volume drop-down list.
- Select Read/Write as the access type.
- 

Select Attach .

When the volume's icon no longer lists it as Attaching , proceed with the next steps.
- Run the`lsblk`command again to confirm that the boot volume now shows up as a volume attached to the instance. In this sample output for the`lsblk`, the boot volume attached as a data volume shows up as`sdb`:
```

```

- 

Run the`fsck`command on the volume's root partition. The root partition is usually the largest partition on the volume.

The following sample for the`fsck`command shows the output when there are no errors or corruption present on the partitions for an Oracle 7.6 instance:
```

```

If errors are present on a partition, you will usually be prompted to repair the errors. Following is an example of an interactive repair session of a corrupt ext4 boot volume for an Ubuntu instance:
```

```

Note  
  

XFS file systems will usually auto-repair their contents when the system boots up, fixing any corruption during the boot process. You can use the`xfs_repair`command to force a repair for scenarios where boot volume corruption is preventing the auto-repair functionality from working, as shown in the following example:
```

```
