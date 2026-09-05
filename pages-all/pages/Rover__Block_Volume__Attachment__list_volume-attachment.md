# Listing Block Volume Attachments within a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm
- Fetched: 2026-09-05 02:57 CDT

# Listing Block Volume Attachments within a Roving Edge Infrastructure Device

Describes how to list the block volumes attached to a compute instance on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/list_volume-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance to which you want to attach a block volume under Instances .
- 

Select Attached Block Volumes in the lower left corner. All attached block volumes are listed in tabular form.
- 

Use the[oci compute volume-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/list.html)command and required parameters to list the block volumes attached to a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLI)
- 

Run the[ListVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/ListVolumeAttachments)
