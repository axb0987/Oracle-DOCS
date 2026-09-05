# Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/recover_key.htm
- Fetched: 2026-09-05 03:02 CDT

# Recovering Your Roving Edge Infrastructure Device After Shredding the Master Key

Describes how to recover a device on which you have shredded the master key.

If you have rendered your Roving Edge Infrastructure device inoperable because you shredded the master key as described in[Shredding the Master Key for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/shred_master_key.htm#ShredMasterKey), you can recover the device and return it to service by recovering the key.

Finding the Device Recovery Key
- 

If the recovery key is stored in an OCI Vault secret in your tenancy (described in[Self-Provision the Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Provisioning/provisioning-a-roving-edge-device.htm#provisioning-a-roving-edge-device)), you can retrieve the recovery from the Vault service. See[Getting a Secret's Contents](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/concepts_concepts_concepts_secretrules_view_secret_content.htm). While getting the secret contents, enable Show decoded Based64 digit to view the recovery key.
- 

If the recovery key is secured using your own KMS-based master key (described in[Using Your Own Master Key with Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/user_master_key.htm#UserMasterKey)), get the recovery key using your own master key.

Recovering the Device

Your device must be running and connected to your controlling host running terminal emulation software such as PuTTY to unlock the device. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

In the terminal emulator, select the Recover Key menu option and follow the prompts to enter a new passphrase.
