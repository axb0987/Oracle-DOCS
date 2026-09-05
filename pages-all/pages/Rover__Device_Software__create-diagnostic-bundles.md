# Creating a Diagnostic Bundle for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm
- Fetched: 2026-09-05 02:58 CDT

# Creating a Diagnostic Bundle for a Roving Edge Infrastructure Device

Create a diagnostic bundle for a Roving Edge Infrastructure device that you can send to Oracle for further review and analysis.

You can use either the Device Console or the CLI to create a diagnostic bundle in normal mode.

You can only use the CLI to create a diagnostic bundle for both standard and minimum services modes. Select the CLI tab to see the CLI procedure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/create-diagnostic-bundles.htm#)
- 

- Open the navigation menu and select Node Management &gt; Diagnostic Bundles . The Diagnostic Bundles page appears.
- Select Create Bundle . The Create Diagnostic Bundle dialog box appears.
- Enter a Bundle Name for the diagnostic bundle.
- Select a specific device node from the Node list to create a diagnostic bundle for just that node.
- Select Include Core Files to include core files in the bundle.
- Select Create .
As the bundle is generated, the status progresses from Accepted to In Progress , then to Completed .

The diagnostic bundle you created appears in the list in the Diagnostic Bundles page.

What's Next?

Download the bundle to your computer so that you can submit the bundle to Oracle for analysis. See[Downloading a Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/download-diagnostic-bundles.htm#top).
- 

Use the[oci raw-request](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/raw-request.html)command and required parameters to send a request to the Roving Edge device to create a diagnostic bundle.

```

```

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Access/cli_install.htm#CLI)

Procedure
- 

Create a json file that includes a`displayName`and optionally a`nodeName`. Example:
```

```

- 

Send a request to create a diagnostic bundle.

Example:
```

```

What's Next?

Download the bundle to your computer so that you can submit the bundle to Oracle for analysis. See[Downloading a Diagnostic Bundle](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/download-diagnostic-bundles.htm#top).
-
