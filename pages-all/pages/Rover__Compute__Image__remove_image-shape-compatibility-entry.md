# Removing an Image Shape Compatibility Entry from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm
- Fetched: 2026-09-05 02:58 CDT

# Removing an Image Shape Compatibility Entry from a Roving Edge Infrastructure Device

Describes how to remove an image shape compatibility entry on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Images . The Custom Images page appears. All custom images are listed in tabular form.
- 

Select a State from the list to limit the custom images displayed to that state.
- 

Select the image entry whose details you want to get. The image's Details page appears.
- 

Select Edit Details .
- 

Remove the compatible shape entry.
- 

Use the[oci compute image-shape-compatibility-entry remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/remove.html)command and required parameters to remove an image shape compatibility entry on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLI)
- 

Run the[RemoveImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/RemoveImageShapeCompatibilityEntry)
