# Detaching and Deleting a VNIC from Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm
- Fetched: 2026-09-05 03:01 CDT

# Detaching and Deleting a VNIC from Roving Edge Infrastructure

Describes how to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/detach_vnic.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

(optional) Select a State from the list to limit the instances displayed to that state.
- 

Select the instance that you want to detach and delete a secondary VNIC. The instance's Details page appears.
- 

Select Attached VNICs under Resources .

The primary VNIC and any secondary VNICs attached to the instance are is displayed.
- 

Select the Actions menu ( ) to the right of the secondary VNIC you want to delete and select Delete VNIC .
- 

Confirm the detachment when prompted.

It takes typically a few seconds before the VNIC is deleted.
- 

Use the[oci compute instance detach-vnic](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/detach-vnic.html)command and required parameters to detach and delete a secondary VNIC from your Roving Edge Infrastructure devices:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLI)
- 

Run the[DetachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/DetachVnic)
