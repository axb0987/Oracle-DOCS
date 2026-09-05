# Getting a Boot Volume Attachment's Details for a Computer Instance on a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm
- Fetched: 2026-09-05 02:57 CDT

# Getting a Boot Volume Attachment's Details for a Computer Instance on a Roving Edge Infrastructure Device

Describes how to get the details of a boot volume attachment for a compute instance on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/get_boot-volume-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

Select a State from the list to limit the boot volumes displayed to that state.
- 

Select the instance whose attached boot volumes you want to list. The instance's Details page appears.
- 

Select Boot Volume under Resources . The Boot Volumes page appears, displaying the boot volumes in tabular form.
- 

Select the boot volume whose attachments you want to list. The boot volume's Details page appears.
- 

Select Attached Instances under Resources . The Attached Instances page appears. All attached instances are displayed in tabular form.
- 

Use the[oci compute boot-volume-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/get.html)command and required parameters to get the details of a boot volume attachment for a compute instance on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Boot_Volume/../../Access/cli_install.htm#CLI)
- 

Run the[
