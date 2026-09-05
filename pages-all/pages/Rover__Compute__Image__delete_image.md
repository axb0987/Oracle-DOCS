# Removing an Image from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/delete_image.htm
- Fetched: 2026-09-05 02:57 CDT

# Removing an Image from a Roving Edge Infrastructure Device

Describes how to remove a custom image for use in launching an instance from your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/delete_image.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/delete_image.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/delete_image.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Images . The Custom Images page appears. All custom images are listed in tabular form.
- 

Select a State from the list to limit the custom images displayed to that state.
- 

Select the custom image whose details you want to get. The custom image's Details page appears.
- 

Select Delete .
- 

Confirm the deletion when prompted.
- 

Use the[oci compute image delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/delete.html)command and required parameters to remove a custom image for use in launching an instance from your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLI)
- 

Run the[DeleteImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/DeleteImage)
