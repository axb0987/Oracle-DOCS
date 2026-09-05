# Detaching a Block Volume from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm
- Fetched: 2026-09-05 02:57 CDT

# Detaching a Block Volume from a Roving Edge Infrastructure Device

Describes how to detach a block volume from a compute instance on your Roving Edge Infrastructure device.

See[Detaching a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/detachingavolume.htm)in the Oracle Cloud Infrastructure documentation for more information on this feature.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/detach_volume-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance from which you want to detach the volume under Instances . The instance's Details page appears.
- 

Select Attached Block Volumes in the lower left corner. All attached block volumes are listed in tabular form.
- 

Select the Actions menu ( ) for the block volume you want to detach and select Detach .
- 

Confirm the detachment when prompted.
- 

Use the[oci compute volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/detach.html)command and required parameters to detach a block volume from a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/../../Access/cli_install.htm#CLI)
- 

Run the[
