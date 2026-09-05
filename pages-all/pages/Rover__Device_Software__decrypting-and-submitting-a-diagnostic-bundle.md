# Decrypting and Submitting a Diagnostic Bundle
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/decrypting-and-submitting-a-diagnostic-bundle.htm
- Fetched: 2026-09-05 02:58 CDT

# Decrypting and Submitting a Diagnostic Bundle

After you've downloaded a diagnostic bundle from a Roving Edge Device to your local computer, decrypt the bundle before you submit the bundle to Oracle Support.
- 

Know the Roving Edge Device encryption key.

If you put the device into the[standard](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/enable_diagnostics_standard_mode.htm#enable_diagnostics_standard_mode)or[minimum services](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/enabling_diagnotics_in_services_mode.htm#enabling_diagnotics_in_services_mode)mode, you might already know the encryption key. If not, you can access the key from the device serial console. See[Displaying the Encryption Key for Diagnostic Bundles](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/serial-encryption-key.htm#serial-encryption-key).
- 

Open a command prompt window and navigate to where the diagnostic bundle was downloaded on your computer.
- 

Decrypt the diagnostic bundle by running the following command at the prompt:
```

```

- 

Open an Oracle Support Request and upload the decrypted diagnostic bundle as part of your support request ticket. See[Contacting Oracle Support](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../contacting_oracle_support.htm#ContactOracleSupport)
