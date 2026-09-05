# Displaying the Encryption Key for Diagnostic Bundles
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/serial-encryption-key.htm
- Fetched: 2026-09-05 02:59 CDT

# Displaying the Encryption Key for Diagnostic Bundles

All diagnostic bundles are encrypted by default. If you put the device into the[standard](https://docs.oracle.com/iaas/Content/Rover/Device_Software/enable_diagnostics_standard_mode.htm#enable_diagnostics_standard_mode)or[minimum services](https://docs.oracle.com/iaas/Content/Rover/Device_Software/enabling_diagnotics_in_services_mode.htm#enabling_diagnotics_in_services_mode)diagnostic mode, you might already know the encryption key. If not, you can get it here. To upload to MOS, the bundle must be decrypted.
You must be connected to the serial port. The host must be running terminal emulation software such as PuTTY to display the serial console menu. See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

Using terminal emulation, select the Diagnostics menu option. The Diagnostics Menu appears.
- 

Select Show Diagnostics Bundle Encryption Key . The encryption key is displayed.
-
