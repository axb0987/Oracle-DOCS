# Sanitizing a Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/sanitizing-a-device.htm
- Fetched: 2026-09-05 02:59 CDT

# Sanitizing a Device

Some Roving Edge devices provide a sanitization feature that enables you to permanently and securely erase all data from the device in a way that the data can't be recovered. If your device has the sanitization feature, you must sanitize the device before you return the device to Oracle.
Note  
  
This feature is only available on devices that were self-provisioned on-site, as described in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device). The steps in this procedure help you find out if this feature is supported or not.

The sanitization feature offers the following wipe options:
- 

Simple Wipe : File storage is erased. This wipe takes less time than a deep wipe, and is suitable for situations where a deep wipe isn't needed, for example, if time is more important than the data on the device, or if you don't have any user data on the device.
- Deep Wipe : All user data on file storage is erased. Depending on the amount of data on the device, a deep wipe might run for 10 to 20 hours. Select the deep wipe option when you want to completely remove all user data from the device.

When the entire sanitization procedure is completed, the following actions happen:
- 

All user data is wiped clean on the device.
- The device is returned to an unprovisioned state (the same state in which the device was shipped to you).
- 

Billing stops for this device.
- 

You're presented with a sanitization certificate.
Note  
  
If you have trouble sanitizing a device, check the connectivity between the device and the OCI Object Storage service. See[Data sync, system upgrades, or sanitization operations not working](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../troubleshooting.htm#networking__object-storage-connectivity).

Prerequisites
- 

Back up your data : Ensure you have synced all your needed data to Oracle Cloud Infrastructure (OCI) using Data Sync before deleting it from your devices. See[Data Sync Tasks](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).
- 

Ensure connectivity to OCI : The device must have connectivity to the device's OCI home region during the entire procedure. You can test connectivity by running a ping or traceroute to the home region endpoint. See[Testing Network Connectivity](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/testing-network-connectivity.htm#testing-network-connectivity).
- 

If enabled, disable Ethernet Bonding : When you disable Ethernet bonding on the device, also disable LACP aggregation in your data center switch. See[Managing Ethernet Bonding](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing_network_bonding.htm#managing_network_bonding).

Procedure
- 

Access the serial console as described in[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).

Don't unlock the device. The device must be locked to sanitize it.

If the device is unlocked, take these actions:
- Ensure the device auto unlock feature is disabled. See[Managing Auto Unlock](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing-how-the-device-unlocks.htm#managing-how-the-device-unlocks).
- Select the Reboot Device option to reboot the device into a locked state.
- 

In the serial console, select Advanced Menu .
- 

Select Sanitize Device Management .
Note  
  

If you receive a message that you can't use the sanitize feature on this device, instead see[Returning Older Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/returning-older-devices.htm#returning-older-devices).

The Sanitize Device Management menu is displayed:
```

```

- 

Select Download Artifacts from OCI for Sanitization .

Files that are required for sanitization are downloaded from OCI to the device.
- 

Select one of the following sanitization programs:
- 

Sanitize Device with Simple Wipe
- Sanitize Device with Deep Wipe

After the sanitization completes, user data is wiped, the device reboots into a minimal OS and displays a new Sanitization Main Menu .
```

```

- 

Select Device Sanitization .

The following menu options are displayed:
```

```

- 

Select Wipe rover image .

Data on the boot drive is erased.
- 

Select Complete sanitization .

The following actions happen:
- The device is returned to an unprovisioned state (the same state in which the device was shipped to you).
- 

The device shuts down.
- 

The status of the device node in your OCI tenancy is set to CUSTOMER_SANITIZED.
- 

Oracle is notified that the device is restored to a factory state.
- 

A sanitization certificate is displayed.
- (Optional) Take a screen shot of the sanitization certificate and save it for your records.

What's next?

Return the device to Oracle : When sanitization is complete, Oracle sends you a shipping label that you can use to return the device to Oracle. After Oracle receives the device, the node status in your tenancy changes to ORACLE_RECEIVED. To see the status of a node, see[Listing Nodes for Compute, GPU, and Storage Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Node2/list_node2.htm#top)
