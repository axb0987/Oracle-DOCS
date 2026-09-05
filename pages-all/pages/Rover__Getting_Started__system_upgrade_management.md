# Managing Your System Upgrades
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/system_upgrade_management.htm
- Fetched: 2026-09-05 03:00 CDT

# Managing Your System Upgrades

You can disable your Roving Edge Infrastructure device's ability to have its system upgraded in a disconnected environment using the serial console. Disable the disconnected upgrade by discarding the signing public key. You can also display the device's signing public key.
- 

Using terminal emulation, select the Advanced Menu &gt; System Upgrade Management menu option. The following options appear:
- 

Disable Disconnected Upgrade : Use to disable the disconnected upgrade feature by discarding the public signing key. See[Device Software Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Device_Software/device_software_management.htm#software_updates_0)for general information.
Note  
  

This is an irreversible action. You cannot perform a disconnected upgrade until the key is restored by connecting back to Oracle Cloud Infrastructure. Do not perform this operation unless advised by Oracle to discard the upgrade bundle signing public key.
- 

Display Signing Public Key : Use to display the public key corresponding to the private key that was used to sign the disconnected upgrade bundle.
-
