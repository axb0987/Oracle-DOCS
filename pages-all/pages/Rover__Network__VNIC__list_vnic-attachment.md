# Listing VNIC Attachments for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm
- Fetched: 2026-09-05 03:01 CDT

# Listing VNIC Attachments for Roving Edge Infrastructure

Describes how to list the VNIC attachments on your Roving Edge Infrastructure devices.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/list_vnic-attachment.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

(optional) Select a State from the list to limit the instances displayed to that state.
- 

Select the instance that you want to list VNIC attachments. The instance's Details page appears.
- 

Select Attached VNICs under Resources . The primary VNIC is listed. If the instance has two active physical NICs, the VNICs are grouped by NIC 0 and NIC 1.
- 

## Listing the VNIC attachments for a compartment

Use the[oci compute vnic-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/vnic-attachment/list.html)command and required parameters to list the VNIC attachments on your Roving Edge Infrastructure devices:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLI)

## Listing VNIC attachments for an instance

Use the[oci compute instance list-vnics](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/list-vnics.html)command and required parameters to list the VNIC attachments on your Roving Edge Infrastructure devices:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLI)
- 

Use the[
