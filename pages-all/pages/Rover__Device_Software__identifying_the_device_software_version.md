# Identifying the Device Software Version
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/identifying_the_device_software_version.htm
- Fetched: 2026-09-05 02:59 CDT

# Identifying the Device Software Version

You can identify the Roving Edge Device software version using the Device Console or the serial console.

## Using the Device Console
- 

Sign in to the Device Console.
- 

Perform one of the following actions:
- 

In the navigation menu, select Node Management , then select Nodes .

The version is displayed in the Version column.
- 

Select the System Status icon ( ) in the upper right corner.

The version is displayed under System Upgrades.

## Using the serial console

Prerequisites

You must have a controlling host, such as a laptop connected to the device serial port (see[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Setup-RED/cable-device.htm#install-the-device)) and have terminal emulation configured (see[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation)).

For information about the serial console menu, see[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

In your terminal emulation utility, with the main menu displayed, select 4) Show Status .

The version is listed in the device status output:
```

```
