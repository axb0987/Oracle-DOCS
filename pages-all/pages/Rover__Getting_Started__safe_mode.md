# Avoiding Storage Overages Using Safe Mode
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/safe_mode.htm
- Fetched: 2026-09-05 02:59 CDT

# Avoiding Storage Overages Using Safe Mode

We recommend keeping the object storage capacity on your Roving Edge Infrastructure devices at 80% or less.

When the storage is full, read and write errors can occur and storage operations cease. If this occurs, place your device in Safe Mode and remove items from object storage until the capacity is lower, preferably at 80% or less.

Your device must be running and connected to your controlling host running terminal emulation software such as PuTTY to place the device in Safe Mode. See[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation)and[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole)for more information.
- 

Using terminal emulation, select the Enter Safe-Mode menu option.
- 

Remove items from object storage. We recommend keeping object storage levels at 80% or less.
- 

Select Exit Safe-Mode . After the Roving Edge Infrastructure device determines that its object storage capacity is below the 95% level, it returns to normal operation.

See[Roving Edge Infrastructure Device Monitoring](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Device_Monitoring/device_monitoring.htm#NodeManagement)
