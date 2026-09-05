# Detaching a Boot Volume Attachment from a Compute Instance on a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm
- Fetched: 2026-09-05 02:57 CDT

# Detaching a Boot Volume Attachment from a Compute Instance on a Roving Edge Infrastructure Device

Describes how to detach a boot volume from a compute instance on your Roving Edge Infrastructure device.
Note  
  

You can detach a boot volume only from a stopped compute instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/detach_boot-volume-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance from which you want to detach the boot volume. The instance's Details page appears.
- 

Select Boot Volume under Resources . The Boot Volumes page appears, displaying the boot volumes in tabular form.
- 

Select the Actions menu ( ) for the boot volume, and then select Detach Boot Volume . Confirm when prompted.
- 

Use the[oci compute boot-volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/detach.html)command and required parameters to detach a boot volume from a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLI)
- 

Run the[
