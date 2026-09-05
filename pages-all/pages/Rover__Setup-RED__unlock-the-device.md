# Unlock the Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/unlock-the-device.htm
- Fetched: 2026-09-05 03:02 CDT

# Unlock the Device

Every time a Roving Edge device is booted, it boots into a locked state. You must unlock the device using an unlock passphrase to use the device.

The passphrase was created in one of the following ways:
- 

When the device was self-provisioned on-site. See[Provision a Device: Set Up Credentials](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__set-up-credentials).
- 

On older Roving Edge Devices and Ultra Devices, the passphrase was created when the node was created in your tenancy. See[Creating a Roving Edge Device 1 Node (Deprecated)](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Node/create_node.htm#top)and[Creating a Roving Edge Ultra Node](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Ultra/create_ultra.htm#top).
Note  
  

Anytime you reboot the device, it reverts to a locked state. Receiving a`Device is locked`message after trying to connect to an API endpoint is indicative that the device is in a locked state. Unlock the device to proceed.
Note  
  

If your device is unexpectedly in a locked state, it might have accidentally rebooted. Check that your power connection is steady and not inadvertently causing device reboots.
- 

In the serial console, select Unlock Device .
- 

Enter the passphrase.

The device is unlocked, and the serial console menu is displayed.

What's next?

[Establishing the Certificate Authority for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Setup-RED/../Getting_Started/certificate_authority.htm#SettingPolicies)
