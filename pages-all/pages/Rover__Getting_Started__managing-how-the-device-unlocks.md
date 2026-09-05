# Managing Auto Unlock
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/managing-how-the-device-unlocks.htm
- Fetched: 2026-09-05 02:59 CDT

# Managing Auto Unlock

By default, Roving Edge devices are automatically locked after every reboot. To enable the device to function, you must enter the unlock passphrase in the serial console. The locking feature provides a level of security. However, you can disable the auto unlock feature if the device is located in a secure facility, and theft isn't a concern.

You must have a controlling host connected to the serial port. The host must be running terminal emulation software such as PuTTY to display the serial console menu. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole)and[Set Up Terminal Emulation](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../Setup-RED/setting-up-terminal-emulation.htm#setting-up-terminal-emulation)for more information.
- 

Using terminal emulation to display the serial console, select Advanced Menu , then select Auto Unlock Management .

The Auto Unlock menu is displayed:
```

```

- 

Depending on what you want to do, enter the number for one of the following options:
- Enable Auto Unlock : The device isn't locked after a reboot. No passphrase is required.
- Disable Auto Unlock : (default value) The device is automatically locked after every reboot, and you're prompted to enter a passphrase to unlock the device.
-
