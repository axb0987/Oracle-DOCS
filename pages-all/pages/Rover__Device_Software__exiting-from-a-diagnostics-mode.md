# Exiting From a Diagnostics Mode
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/exiting-from-a-diagnostics-mode.htm
- Fetched: 2026-09-05 02:59 CDT

# Exiting From a Diagnostics Mode

After you've submitted a diagnostics bundle that was created in standard or minimum services mode, exit the mode.
- 

From your computer, connect to the device serial console.

See[Cable the Roving Edge Device](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Setup-RED/cable-device.htm#install-the-device)and[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation).
- 

Enter your unlock passphrase.

The serial console main menu is displayed.
- 

Enter the menu number that corresponds to Diagnostics .

The Diagnostics Menu is displayed:
```

```

- 

Enter the number for Exit Diagnostics Data Collection Mode. .
- 

Enter the number for one of these options based on the diagnostic mode:
- Exit Diagnostics Data Collection Standard Mode
- Exit Diagnostics Data Collection Minimum Services Mode
- 

For standard mode: Press Enter again, then`CTRL+C`to go back to the main menu.
- 

For minimum services mode:
- Enter Y to confirm to reboot the device.
- After the reboot, unlock the device as usual. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole)
