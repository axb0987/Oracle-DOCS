# Deleting a Boot Volume from a Compute Instance on a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm
- Fetched: 2026-09-05 02:57 CDT

# Deleting a Boot Volume from a Compute Instance on a Roving Edge Infrastructure Device

Describes how to delete a boot volume from a compute instance on your Roving Edge Infrastructure device.
Important  
  

You can't undo this operation. Any data on a volume is permanently deleted after the volume is deleted. You're not able to restart the associated instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/delete_boot_volume.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance whose attached boot volume you want to delete. The instance's Details page appears.
- 

Select Boot Volume under Resources . The Boot Volumes page appears, displaying the boot volumes in tabular form.
- 

Select the boot volume that you want to delete. The boot volume's Details page appears.
- 

Select Terminate .
- 

Confirm the deletion when prompted.
- 

Use the[oci bv boot-volume delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/delete.html)command and required parameters to delete a boot volume from a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLI)
- 

Run the[
