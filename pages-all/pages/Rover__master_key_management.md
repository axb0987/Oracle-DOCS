# Managing Roving Edge Infrastructure Device Master Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/master_key_management.htm
- Fetched: 2026-09-05 03:02 CDT

# Managing Roving Edge Infrastructure Device Master Keys

Learn how to manage the master keys of Roving Edge Infrastructure devices.

The root access to a Roving Edge device is controlled by its master key. You need to know the master key passphrase to unlock the device. Until the serial console is unlocked, the device is nonfunctional.

On factory provisioned devices, Oracle creates and manages the master key for you. However, you can elect the use your own master key instead of the one provided by Oracle. You can also destroy the master key, rendering the device useless until it's recovered with another key.

On self-provisioned devices, Oracle doesn't manage the master key, passphrases, or passwords. You manage all master key, passphrases, or passwords. See[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device).

You can perform the following master key-based tasks:
- 

[Using Your Own Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/user_master_key.htm#UserMasterKey)
- 

[Shredding Your Device's Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/shred_master_key.htm#ShredMasterKey)
- 

[Recovering Your Device After Shredding its Master Key](https://docs.oracle.com/en-us/iaas/Content/Rover/recover_key.htm#recover_key)
