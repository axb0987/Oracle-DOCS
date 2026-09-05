# Canceling a Diagnostic Bundle That's in Progress
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/cancel-diagnostic-bundles.htm
- Fetched: 2026-09-05 02:58 CDT

# Canceling a Diagnostic Bundle That's in Progress

Learn how to cancel a diagnostic bundle that's being generated on a Roving Edge device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/cancel-diagnostic-bundles.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/cancel-diagnostic-bundles.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/cancel-diagnostic-bundles.htm#)
- 

- Open the navigation menu and select Node Management &gt; Diagnostic Bundles . The Diagnostic Bundles page appears. All the diagnostic bundles are listed in tabular form.
- Select the diagnostic bundle that you want to cancel. The diagnostic bundle's Details page appears.
- Perform one of the following tasks depending on what you want to do:

- 

Cancel all diagnostic bundles for all nodes that are still in progress : Select Cancel at the top of the Details page.
- 

Cancel the diagnostic bundle associated with a particular node : Select the the Actions menu ( ) to the right of the diagnostic bundle and select Cancel Bundle .
- Select Confirm when the Cancel Diagnostic Bundle dialog box appears.

Those bundles display their canceled status in the Bundles page.
- 

Use the[oci raw-request](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/raw-request.html)command and required parameters to cancel a diagnostic bundle that's in the process of being created.

```

```

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Software/../Access/cli_install.htm#CLI)
-
