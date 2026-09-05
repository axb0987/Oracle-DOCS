# Known Issues for Roving Edge
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm
- Fetched: 2026-09-05 03:02 CDT

# Known Issues for Roving Edge

The following known issue is identified in Roving Edge Infrastructure.
- [Edge Installer showing "ERROR: Failed to get shape" or continuously printing its version number](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#enter-topic-id)
- [Can't recover passphrase if Auto Unlock is enabled](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#can-t-recover-passphrase-if-auto-unlock-is-enabled)
- [Edge Installer might experience a download failure](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#edge-installer-might-experience-a-download-failure)
- [Factory resetting and preserving objects results in a credential error](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#unique_1447020039)
- [During a reboot or power cycle, the device status might report "Unexpected Error!"](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#unique_1147946773)
- [The Roving Edge installer proxy URL isn't working](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#roving-edge-installer-proxy-url-not-working)
- [Shared block volumes get detached](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#shared-volume-gets-detached)
- [An Oracle Linux 9 instance takes a while to boot](https://docs.oracle.com/en-us/iaas/Content/Rover/known-issues.htm#ol9-instance-takes-a-while-to-boot)

## Edge Installer showing "ERROR: Failed to get shape" or continuously printing its version number
Details This issues applies to Edge Installer all versions 1.6.x or 1.6_classic.x. This issue is addressed in 2.0.59 version or above. When the device has been powered on for more than 10 days, a system file will be removed by the operating system. In some cases the file is recreated improperly causing the device to go into a corrupted state. Once it gets into this situation, there is no workaround or recovery. The device must be exchanged. Please contact Oracle Support. Workaround The self-provisioning procedure was updated to include a direction to power cycle the machine before performing self-provisioning to ensure the system file is created properly.

## Can't recover passphrase if Auto Unlock is enabled
Details This issue only applies when you're trying to recover the serial console passphrase with Auto Unlock enabled.

To lock a device, you must reboot it. With Auto Unlock enabled, the device automatically unlocks upon reboot. To disable auto unlock, you must enter the passphrase which was lost. Therefore, if a device has Auto Unlock enabled, it isn't possible to recover a passphrase. Workaround
- 

If you need to recover the passphrase, upgrade the Roving Edge device software to version 2.18.8 or higher. See[Roving Edge Device Software Version Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/device_software_management.htm#software_updates_0).
- 

Before the device reboots and locks the screen, use the serial console to disable Auto Unlock as described in[Managing Auto Unlock](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing-how-the-device-unlocks.htm#managing-how-the-device-unlocks).
- Recover the passphrase. See[Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/recover_key.htm#recover_key).
Note  
  
Roving Edge software to versions are released to realms at different times. If version 2.18.8 or later isn't available in your region, contact Oracle.

## Edge Installer might experience a download failure
Details This issue applies to Edge Installer versions 1.6.21 and 1.6.23. When you use the Edge Installer to[Download and Install Software](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__install-software)there's a small chance that excessive logs will fill up the disk space and cause the software download process to fail.

A factory reset doesn't free up the disk space. Workaround
- In the Edge Installer menu, select Advanced Operations , then select Check for Configuration Interface Software Updates .
- 

After the update is finished, reboot the device.

Note: Don't run Check for Configuration Interface Software Updates again. If you do, reboot the device again.
- Restart the self-provisioning process as described in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device).
Note  
  
Roving Edge software to versions are released to realms at different times. If version 2.18.8 or later isn't available in your region, contact Oracle.

## Factory resetting and preserving objects results in a credential error
Details In the 2.18.6 release, if you factory reset a device and choose to preserve objects, the reset might display a credential error. Workaround
- If possible, back up the device Object Storage data to your OCI Object Storage. See[Roving Edge Infrastructure Data Synchronization](https://docs.oracle.com/en-us/iaas/Content/Rover/Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).
- Factory reset the device again, and don't select to preserve objects. See[Resetting Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/reset_factory_device.htm#ResetDevice).

## During a reboot or power cycle, the device status might report "Unexpected Error!"
Details

As of version 2.18, the following error might be displayed when you reboot or power cycle a device:
```

```
Workaround Reboot the device until the error is no longer displayed. See[Rebooting a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/rebooting-a-device.htm#UnlockingDevice).

## The Roving Edge installer proxy URL isn't working
Details

The Proxy URL setting in the Roving Edge installer isn't working. If you set a proxy URL during self-provisioning, the Roving Edge installer must be reset to recover.

Depending on your situation, perform one of the following workarounds: Avoid the issue: Prior to self-provisioning a Roving Edge device, follow these guidelines:
- 

Ensure that the device isn't behind an HTTP proxy server and has internet connectivity.
- 

When you self-provision the device, don't specify a proxy URL. See[Configure Device Networking](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__device-networking). Workaround: If you started to self-provision a Roving Edge device and received an error similar to the following error:
```

```

Reset the device to factory defaults and repeat the self-provisioning process:
- 

In the self-provisioning menu, enter CTRL-C until you're back to the main menu:
```

```

- 

Enter`5`to select the`Advanced Operations`menu.
- 

Enter`3`to select the`Factory reset Configuration Interface`.
- 

Enter`factoryreset`, then enter the reset passphrase:`Oracle_Rover_Reset_1!`

The device resets to factory defaults then reboots.
- 

After the device reboots, ensure that the device isn't behind a HTTP proxy server and has internet connectivity.
- 

Self provision the device, and don't specify a proxy URL. See[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device).

## Shared block volumes get detached

On Roving Edge devices running version 2.16.2, when a block volume is shared with more than one instance, the shared block volume might get stuck in an ATTACHING state, then change to a DETACHED state. Details Any shared block volume attached to an instance that was created before version 2.16.2 remains attached and isn't affected by this issue. Any shared block volume attached to an instance that's created on version 2.16.2, will be stuck in an ATTACHING state and eventually reach a DETACHED state. Workaround We're working on a resolution.

## An Oracle Linux 9 instance takes a while to boot

An Oracle Linux 9 instance might take longer than 4 minutes to boot. Workaround
- 

In the instance, run the following command to check if the bootloader entry contains a`netroot`setting that's set to an iscsi target:
```

```

- 

If the command returns any result, remove the`netroot`option from the bootloader entries using this command:
```

```
