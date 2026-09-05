# Enabling Diagnostics Standard Mode
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/enable_diagnostics_standard_mode.htm
- Fetched: 2026-09-05 02:58 CDT

# Enabling Diagnostics Standard Mode

On a Roving Edge device, before you can create a diagnostics bundle in standard mode, you must enable standard mode on the device.
Note  
  
You don't need to enable standard mode if you plan to create the diagnostics bundle in normal mode. See[Collecting Roving Edge Device Diagnostic Information](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0).
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

In the Diagnostics Menu , enter the number for Show Diagnostics Bundle Encryption Key .

The encryption key is displayed. Example:
```

```

- 

Copy the key to a secure place. You need it later to decrypt the diagnostics bundle.
- 

Press Enter to return the Diagnostics Menu .
- 

Enter the number for Help .

The output shows you how to decrypt the diagnostic bundle file after you have downloaded it.
- 

Press Enter to return to the Diagnostics Menu .
- 

Enter the number for Enable Diagnostics Data Collection Mode .
- 

Enter the number for Enable Diagnostics Standard Mode .

Standard mode is enabled and the following credentials are displayed:
```

```

- 

Copy the user and password to a secure place. You might need these credentials if Oracle Support assists you with submitting the bundle.

What's Next?

[Create a diagnostic bundle using the CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#creating_a_diagnostic_bundle_using_the_cli)
