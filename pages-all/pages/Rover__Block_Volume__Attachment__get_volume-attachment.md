# Getting a Block Volume Attachment's Details within a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm
- Fetched: 2026-09-05 02:57 CDT

# Getting a Block Volume Attachment's Details within a Roving Edge Infrastructure Device

Describes how to get the details of a block volume attached to a compute instance on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/get_volume-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

(optional) Select a State from the list to limit the instances displayed to that state.
- 

Select the instance to which you want to attach a block volume.
- 

Select Attached Block Volumes in the lower left corner. All attached block volumes are listed in tabular form.
- 

Select the block volume whose details you want to get. The block volume's Details page appears.
- 

Use the[oci compute volume-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/get.html)command and required parameters to get the details of a block volume attached to a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLI)
- 

Run the[GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)
