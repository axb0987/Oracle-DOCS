# Deleting a Block Volume from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm
- Fetched: 2026-09-05 02:57 CDT

# Deleting a Block Volume from a Roving Edge Infrastructure Device

Describes how to delete a block volume from your Roving Edge Infrastructure device.

The volume can't have an active connection to an instance.
Caution  
  

All data on the volume is permanently lost when the volume is deleted.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/delete_block_volume.htm#)
- 

- 

Open the navigation menu and select Block Storage &gt; Block Volumes . The Block Volumes page appears. All block volumes are listed in tabular form.
- 

Select a State from the list to limit the block volumes displayed to that state.
- 

Select the block volume that you want to delete. The block volume's Details page appears.
- 

Select Terminate .
- 

Confirm the deletion when prompted.
- 

Use the[oci bv volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/delete.html)command and required parameters to delete a block volume from your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/../Access/cli_install.htm#CLI)
- 

Run the[
