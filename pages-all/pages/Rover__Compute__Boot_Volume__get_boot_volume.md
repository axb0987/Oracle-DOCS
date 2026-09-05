# Getting a Boot Volume's Details for a Compute Instance on a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm
- Fetched: 2026-09-05 02:57 CDT

# Getting a Boot Volume's Details for a Compute Instance on a Roving Edge Infrastructure Device

Describes how to get the details of a boot volume for a compute instance on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot_volume.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the instances displayed to that state.
- 

Select the instance on whose attached boot volume you want to get details. The instance's Details page appears.
- 

Select Boot Volume under Resources . The Boot Volumes page appears, displaying the boot volumes in tabular form.
- 

Select the boot volume on whose details you want to get. The boot volume's Details page appears. The instance associated with the boot volume is listed in the Attached Instance field. If the value for this field displays the following message, the boot volume has been detached from the associated instance, or the instance has been terminated while the boot volume was preserved.
```

```

- 

Use the[oci bv boot-volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/get.html)command and required parameters to get the details of a boot volume for a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLI)
- 

Run the[
