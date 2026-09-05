# Resetting Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/reset_factory_device.htm
- Fetched: 2026-09-05 02:59 CDT

# Resetting Devices

You can reset your Roving Edge Infrastructure device to various levels. Use this feature if your device isn't functioning correctly and you can't recover it using regular troubleshooting operations such as rebooting.

Resetting your device affects its on-device services. If a service has been modified by a system upgrade, resetting the device reverts the service to its original version. All virtual machine (VM) instances, block and boot volumes, network configurations are deleted. The state of the IAM service is also removed. The system prompts you for a new root password, then IAM is reinitialized to the blank state with only the root user active.

Object storage contents aren't automatically deleted in the same manner as the other services. When you perform a factory reset, you're prompted to either preserve objects or not preserve objects.
Important  
  
Before resetting a device, we recommend backing up the device if it's healthy enough to do so. Regardless of selecting to preserve or not preserve objects, back up Object Storage prior to resetting a device. See[Roving Edge Infrastructure Data Synchronization](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Data_Sync/datasynctask_management.htm#DataSyncTaskManagement).

Your device must be running and connected to your controlling host running terminal emulation software such as PuTTY to reset the device. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole)and[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation)for more information.
- 

Using terminal emulation, select the Reset Device menu option. The following options are displayed:
- 

Factory Reset : This option deletes all instances, boot volumes and block volumes on the device. All system upgrades are rolled back. All user information is deleted and a single root user is created. All objects in the object storage are deleted, including instance images and audit logs.
- 

Service Reset : This option deletes all instances, boot volumes and block volumes on the device. All user information is deleted and a single root user is created. Objects in the object storage remain untouched.
- 

Network Reset : This option resets the network configuration values to the factory default for items such as DNS servers. User-configured values, such as IP addresses are removed. See[Configure Network Parameters for a Factory Provisioned Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/finish-the-set-up-for-preprovisioned-devices.htm#finish-the-set-up-for-preprovisioned-devices)after you reset the network to reestablish your networking.
- Select a reset option.
- 

Enter the device passphrase when prompted.
- 

Enter the new user root password when prompted.
- You're prompted to preserve or not preserve objects in Object Storage:
- 

Enter yes to Preserve objects : Deletes all instances, boot volumes and block volumes on this device. All system upgrades are rolled back. All user information is deleted and a single root user is created. All objects in object storage remain untouched.
-
