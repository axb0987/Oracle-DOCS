# Shredding the Master Key for Roving Edge Infrastructure Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/shred_master_key.htm
- Fetched: 2026-09-05 03:03 CDT

# Shredding the Master Key for Roving Edge Infrastructure Devices

Learn how to destroy the master key on Roving Edge Infrastructure devices.

You can destroy or "shred" the master key of your Roving Edge Infrastructure devices. Run this command if you believe the device's has been compromised or is unsafe and is likely to be compromised.
Caution  
  

Shredding the master key permanently deletes the key and shuts down the device.

Your device must be running and connected to your controlling host running terminal emulation software such as PuTTY to shred its master key. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).

Using terminal emulation, select the Shred Key menu option. Confirm your choice to shred your master key and enter your existing Unlock passphrase when prompted.
When the master key is shredded, the device is no longer operable. When the device is restarted, the following message is displayed:
```

```

You must reconfigure the master security key before the device will restart fully. See[Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/recover_key.htm#recover_key)
