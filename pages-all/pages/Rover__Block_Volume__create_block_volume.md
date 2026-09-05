# Creating a Block Volume for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm
- Fetched: 2026-09-05 02:57 CDT

# Creating a Block Volume for a Roving Edge Infrastructure Device

Describes how to create a block volume on your Roving Edge Infrastructure device.

Volumes can be created in sizes ranging from 50 GB (51200 MB) to 6 TB (6291456 MB), in 1 GB (1024 MB) increments. By default, volumes are 300 GB (307200 MB).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm#)
- 

- 

Open the navigation menu and select Block Storage &gt; Block Volumes . The Block Volumes page appears. All block volumes are listed in tabular form.
- 

Select a State from the list to limit the block volumes displayed to that state.
- 

Select Create Block Volume . The Create Block Volume dialog box appears.
- Complete the following:
- 

Name : A user-friendly name or description.
- 

Size : Must be between 50 GB and 6 TB . You can choose in 1 GB increments within this range. The default is 300 GB. If you choose a size outside of your service limit, you might be prompted to request an increase.
- 

Check View detail page after this block volume is created to display the block volume's Details page after you create it.
- 

Select Create Block Volume . The volume is ready to attach after its icon no longer lists it as Provisioning in the Volume list.
- 

Use the[oci bv volume create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/create.html)command and required parameters to create a block volume on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/../Access/cli_install.htm#CLI)
- 

Run the[CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)
