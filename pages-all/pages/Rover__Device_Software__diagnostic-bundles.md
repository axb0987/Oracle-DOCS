# Collecting Roving Edge Device Diagnostic Information
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm
- Fetched: 2026-09-05 02:58 CDT

# Collecting Roving Edge Device Diagnostic Information

Use the diagnostic service to collect diagnostic information for Roving Edge devices and send the information to Oracle Support where the data can be further reviewed and recommendations made on how to fix problems and improve performance.

Start by[collecting a System Diagnostic Report](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__system-diag-mode). Include the report in all Support Requests that you submit.

If possible, to further aid the support resolution, also include another diagnostic report from one of the following collection modes:
- [Normal Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__normal-mode)
- [Standard Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__standard-mode)
- [Minimum Services Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__minimum-services-mode)

## Collecting a System Diagnostic Report

Always collect this data when you submit a Support Request.
- 

Connect your computer to the device serial console.

See[Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
- 

Enter your unlock passphrase.

The serial console main menu is displayed.
- Enter the number for Show System Diagnostics .

A diagnostic report is displayed.
- 

Save the diagnostic output in a file.
- 

If possible, collect additional diagnostic reports:
- [Normal Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__normal-mode)
- [Standard Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__standard-mode)
- [Minimum Services Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__minimum-services-mode)
- Open an Oracle Support Request and include the System Diagnostic file, and any additional diagnostic bundles as part of your Support Request ticket. See[Contacting Oracle Support](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../contacting_oracle_support.htm#ContactOracleSupport).

## Normal Mode

Use this mode when all Roving Edge services start and run as usual. The calling diagnostic API is authenticated through the on-device Identity service. This mode requires no special preparation of the device.

The following table lists the tasks you perform in this mode.

No. Task Description
1.[Create a Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#top)You can create the bundle using the Device Console or the CLI.
2.[Download the Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/download-diagnostic-bundles.htm#top)Use the Device Console to download a diagnostic bundle to your computer.
3.[Decrypt and submit the diagnostics bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/decrypting-and-submitting-a-diagnostic-bundle.htm#decrypting-and-submitting-a-diagnostic-bundle)

Decrypt the bundle on your computer. Then open an Oracle Support Request and upload the decrypted diagnostic bundle as part of your support request ticket.

## Standard Mode

Use this mode when all Roving Edge services run as usual. This mode differs from normal mode in the following ways:
- 

The calling diagnostic API is authenticated using basic user authentication instead of the local on-device Identity service. Basic user authentication is a temporary user and password that's issued to you when you put the device into standard mode. These credentials are required to submit the diagnostic bundle.
- 

You must use the CLI to create the diagnostic bundle. You can't use the Device Console.

The following table lists the tasks you perform in this mode.

No. Task Description
1.[Enabling Diagnostics Standard Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/enable_diagnostics_standard_mode.htm#enable_diagnostics_standard_mode)Use the serial console to put the device in standard mode.
2.[Create a Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#top)You create the bundle using the CLI.
3.[Download the Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/download-diagnostic-bundles.htm#top)Use the Device Console to download a diagnostic bundle to your computer.
4.[Decrypt and submit the diagnostics bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/decrypting-and-submitting-a-diagnostic-bundle.htm#decrypting-and-submitting-a-diagnostic-bundle)

Decrypt the bundle on your computer. Then open an Oracle Support Request and upload the decrypted diagnostic bundle as part of your support request ticket.
5.[Exit from the diagnostics mode.](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/exiting-from-a-diagnostics-mode.htm#exiting-from-a-diagnostics-mode)Exit the diagnostics mode.

## Minimum Services Mode

Use this mode when the device isn't running services as usual.

You use the serial console menu to put the device into Minimum data collection mode which results in rebooting the device with the minimum set of services. Basic user authentication is used in this mode (See[Standard Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/diagnostic-bundles.htm#software_updates_0__standard-mode)for a description of basic user authentication).

The following table lists the tasks you perform in this mode

No. Task Description
1.[Enabling Diagnostics Minimum Services Mode](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/enabling_diagnotics_in_services_mode.htm#enabling_diagnotics_in_services_mode)Use the serial console to put the device in standard mode.
2.[Create a Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#top)You create the bundle using the CLI.
3.[Download the Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/download-diagnostic-bundles.htm#top)Use the Device Console to download a diagnostic bundle to your computer.
4.[Decrypt and submit the diagnostics bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/decrypting-and-submitting-a-diagnostic-bundle.htm#decrypting-and-submitting-a-diagnostic-bundle)

Decrypt the bundle on your computer. Then open an Oracle Support Request and upload the decrypted diagnostic bundle as part of your support request ticket.
5.[Exit from the diagnostics mode.](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/exiting-from-a-diagnostics-mode.htm#exiting-from-a-diagnostics-mode)
