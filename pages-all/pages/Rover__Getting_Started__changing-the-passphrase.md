# Changing the Passphrase
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/changing-the-passphrase.htm
- Fetched: 2026-09-05 02:59 CDT

# Changing the Passphrase

Learn how to change the Roving Edge device serial console passphrase.

Every time a Roving Edge Device is booted, it boots into a locked state. You must unlock the device using an unlock passphrase to use the device.

You must have a controlling host connected to the serial port. The host must be running terminal emulation software such as PuTTY to display the serial console menu. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole)for more information.
- 

Using terminal emulation to display the serial console, select Change Passphrase .

You're prompted to enter a new passphrase:
```

```

- 

Enter a passphrase.

Passphrase requirements:
- 

Minimum Length: 15 characters
- 

Maximum Length: 64 characters
- 

Must Include the following characters:
- One lowercase character
- One uppercase character
- One digit
- One special char from this list:
```

```

- Must differ by at least four characters when changing to a new passphrase
-
