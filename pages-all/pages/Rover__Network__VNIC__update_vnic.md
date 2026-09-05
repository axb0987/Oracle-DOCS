# Editing a VNIC for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm
- Fetched: 2026-09-05 03:01 CDT

# Editing a VNIC for Roving Edge Infrastructure

Describes how to edit a VNIC on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/update_vnic.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

(optional) Select a State from the list to limit the VCNs displayed to that state.
- 

Select the instance associated with the VNIC you want to edit. The instance's Details page appears.
- 

Select Attached VNICs under Resources .
- 

Select the VNIC you want to edit. The VNIC Details page appears.
- 

Select the Actions menu ( ) to the right of the VNIC entry and select Edit . The Edit VNIC dialog box appears.
- 

Make your edits. See[Creating and Attaching VNICs](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/attach_vnic.htm#top)for descriptions of the settings
- 

Select Save Changes .
- 

Use the[oci network vnic update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/update.html)command and required parameters to edit a VNIC on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLI)
- 

Run the[UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic)
