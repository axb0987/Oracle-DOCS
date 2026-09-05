# Upgrading the Roving Edge Device Software while Connected
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/software_update.htm
- Fetched: 2026-09-05 02:59 CDT

# Upgrading the Roving Edge Device Software while Connected

Learn how to upgrade the Roving Edge device software while the device is connected to your Oracle Cloud Infrastructure (OCI) tenancy.

Software upgrade versions aren't cumulative to the preceding versions. If your Roving Edge Infrastructure device is more than one software version behind the latest version, you must upgrade to each subsequent version individually until you're current with the latest version.

The size of the upgrade is currently around 20 to 30 GB with potential to grow or shrink with time. Download time is determined by the upgrade size and your network bandwidth. For example, with a 10 MBPS download connection, it would take approximately 30 minutes.

When you begin the upgrade, the Roving Edge Infrastructure device waits 60 seconds for all running instances to shut down. If you have instances that take longer than 60 seconds to shut down, shut them down yourself before performing the upgrade.

After the upgrade, the device reboots, and you must use the serial console to unlock the device. To prepare to use the serial console, see[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
Note  
  
If you have trouble upgrading the software, check the connectivity between the device and the OCI Object Storage service. See[Data sync, system upgrades, or sanitization operations not working](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../troubleshooting.htm#networking__object-storage-connectivity).
- 

Sign in to the Device Console of the device you plan to upgrade.
- 

Select the System Status icon ( ) in the upper right corner of the Device Console.

The System Upgrades dialog box is displayed, indicating if there are any available software upgrades. It also displays your current software version and the version number of the software upgrade.
- 

Select Download Upgrade .

The software bundle for the upgrade is downloaded onto your device. The System Upgrade dialog box indicates when the download is complete and ready for installation.
- 

After the download is complete, open the navigation menu and select Node Management &gt; Nodes .

The Nodes page is displayed.
- 

In the Actions menu ( ), select Upgrade .

The System Upgrades dialog box indicates the progress of the upgrade. The device is automatically rebooted at the end of the upgrade process. You must unlock the rebooted device using the serial console. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole)
