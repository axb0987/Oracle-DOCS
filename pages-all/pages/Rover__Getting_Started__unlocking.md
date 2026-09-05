# Unlocking a Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/unlocking.htm
- Fetched: 2026-09-05 03:00 CDT

# Unlocking a Device

By default, Roving Edge devices are automatically locked after every reboot. When a device is locked, you can't access any interfaces except the serial console, and you can't use resources, such as compute and storage. To enable the device to function, you must enter the unlock passphrase in the serial console.

The locking feature provides a level of security. However, you can disable the auto unlock feature if the device is located in a secure facility, and theft isn't a concern. See[Managing Auto Unlock](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing-how-the-device-unlocks.htm#managing-how-the-device-unlocks).

The passphrase was created in one of the following ways:
- 

When the device was self-provisioned on-site. See[Provision a Device: Set Up Credentials](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device__set-up-credentials).
- 

On older Roving Edge Devices and Ultra Devices, the passphrase was created when the node was created in your tenancy. See[Creating a Roving Edge Device 1 Node (Deprecated)](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Node/create_node.htm#top)or[Creating a Roving Edge Ultra Node](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Ultra/create_ultra.htm#top).

The passphrase can be changed, as described in[Changing the Passphrase](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/changing-the-passphrase.htm#changing-the-passphrase).
- 

Connect your local computer to the device serial port. See[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/cable-device.htm#install-the-device).
- 

Access the device serial console using terminal emulation on your local computer. See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).

You're prompted to provide the unlock passphrase.
- 

In the serial console, select Unlock Device .
- 

Enter the passphrase.

The device is unlocked, and the serial console menu is displayed.
Note  
  

Anytime you reboot the device, it reverts to a locked state. Receiving a`Device is locked`message after trying to connect to an API endpoint is indicative that the device is in a locked state. Unlock the device to proceed.
Note
