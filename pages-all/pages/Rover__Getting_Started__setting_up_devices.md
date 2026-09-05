# Administering Devices Through the Serial Console
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm
- Fetched: 2026-09-05 03:00 CDT

# Administering Devices Through the Serial Console

Learn how to administer Roving Edge devices using the serial console.

## Operating the Serial Console

The Roving Edge device has a serial console that enables you to administer the device while directly connected to the device.

To use the serial console, perform these actions:
- Ensure that a USB serial port driver is installed on your local computer. See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).
- Set up terminal emulation on the local computer, See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).
- Connect a local computer, such as a laptop to the device serial port. See[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/cable-device.htm#install-the-device).
- 

Power on or reboot the device.

The serial console prompts you for the passphrase to unlock the device.
- 

Enter the passphrase.

The device is unlocked and the serial console main menu is displayed.

The device serial console provides the following menu options:
- 

Unlock Device : Use to unlock the device using an unlock passphrase obtained from the device's node resource in Oracle Cloud Infrastructure. See[Unlocking a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/unlocking.htm#UnlockingDevice).
- 

Change Passphrase : Use to update the device's unlocking passphrase. See[Changing the Passphrase](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/changing-the-passphrase.htm#changing-the-passphrase).
- 

Configure Networking : Use to manage the Roving Edge device network. See[Configuring the Network](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/configuring_devices.htm#ConfigureNetworking).

- 

Show Status : Use to display the device software version, lock or unlock status, and other device information.
- 

Show System Diagnostics : Use to display diagnostic information regarding the device system attributes. See[Collecting a System Diagnostic Report](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Device_Software/diagnostic-bundles.htm#software_updates_0__system-diag-mode).
- 

Shutdown Device : Use to shut down the device.
- 

Reboot Device : Use the reboot the device.
- 

Enter Safe-Mode : Contact Oracle before using Safe-Mode. Use when the storage is full resulting in write or read errors. At this storage capacity level, the Compute service and other device operations are suspended. While in safe mode, you can remove items from object storage until the capacity is lower, preferably at 80% or less. See[Avoiding Storage Overages Using Safe Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/safe_mode.htm#SafeMode).
- 

Exit Safe-Mode : Use to take the device out of safe mode after you have lowered the device's storage capacity level. See[Avoiding Storage Overages Using Safe Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/safe_mode.htm#SafeMode)
- 

Shred Key : Use to destroy or "shred" the master key of your device. Run this command if you believe the device's has been compromised or is unsafe and is likely to be compromised. See[Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../shred_master_key.htm#ShredMasterKey)
- 

Recover Key : Use to recover a device whose key has been shredded and return it to service. See[Recovering Your Device after Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../recover_key.htm#recover_key).
- 

Reset Device : Use to reset the device, either to factory level (objects in object storage are deleted) or service level (objects in the object storage retained.). See[Resetting Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/reset_factory_device.htm#ResetDevice).
- 

Advance Menu : Use to access additional menu commands:
- 

Banner Management : Use to run various banner tasks. The banner is the default message that appears when you attempt to log into the device. See[Managing the Banner](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/banner_management.htm#ManageBanner).
- 

Network Management : Use to display the status various network-related topics. See[Managing Advanced Network Settings](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/network_management.htm#ManageNetwork).
- 

Password Management : Use to specify the number of user login attempts allowed. See[Managing Serial Console Sign-In Attempts](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/password_management.htm#ManagePassword).
- 

System Upgrade Management : Use to disable the ability to have the device upgraded in a disconnected environment. See[Managing Your System Upgrades](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/system_upgrade_management.htm#system-upgrades).
- 

Auto Unlock Management : Use to enable or disable the auto unlock feature, and to see the auto unlock configuration. See[Managing Auto Unlock](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing-how-the-device-unlocks.htm#managing-how-the-device-unlocks).
- 

Identity Management : Use to reset a user's Device Console password. See[Resetting a Device Console Password](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/resetting-web-console-user-accounts.htm#managing-web-console-user-accounts).
- 

Sanitize Device Management : Use to wipe data from a Roving Edge device. See[Sanitizing a Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/sanitizing-a-device.htm#sanitizing-a-device).
- 

Node Health : Use to monitor the storage health in Roving Edge Infrastructure device nodes. Storage health covers following components:
- 

Block storage health
- 

Object storage health
- 

Storage backend services health
- 

Disk health

The health of a service on a device node is determined by the following classifications:
- 

AVAILABLE : The service is available, and all components are functional.
- 

WARNING : The service is still functional, but some minor issue is happening and we may need to pay attention.
- 

DEGRADED : The service is partially functional and some components have issues.
- 

UNAVAILABLE : The service is not responding or some components have critical issues which make the service not functional.
- 

Diagnostics : Use to run tasks related to collecting diagnostics data related to Roving Edge Infrastructure device performance. You can collect the diagnostics data and forward it to Oracle for analysis. See[Collecting Device Diagnosis Information](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Device_Software/diagnostic-bundles.htm#software_updates_0).
-
