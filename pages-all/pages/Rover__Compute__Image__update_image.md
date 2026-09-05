# Editing an Image for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm
- Fetched: 2026-09-05 02:58 CDT

# Editing an Image for a Roving Edge Infrastructure Device

Describes how to edit a custom image for use in launching an instance on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Images . The Custom Images page appears. All custom images are listed in tabular form.
- 

Select a State from the list to limit the images displayed to that state.
- 

Select the image whose details you want to get. The image's Details page appears.
- 

Select Edit Details .
- 

Make your edits. See[Importing a Custom Image](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image.htm#top)for descriptions of the settings.
- 

Select Save Changes .
Note  
  

After you add shape compatibility to an image, test the image on the shape to ensure that the image actually works on the shape. Some images (especially Windows) might never be cross-compatible with other shapes because of driver or hardware differences.
- 

Use the[oci compute image update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/update.html)command and required parameters to edit a custom image for use in launching an instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/../../Access/cli_install.htm#CLI)
- 

Run the[UpdateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/UpdateImage)
