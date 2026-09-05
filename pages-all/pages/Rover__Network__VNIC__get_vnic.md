# Getting VNIC Details for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic.htm
- Fetched: 2026-09-05 03:01 CDT

# Getting VNIC Details for Roving Edge Infrastructure

Describes how to get the details of a VNIC on your Roving Edge Infrastructure devices.

Use this command to get the VNIC private IP address, MAC address, optional public IP address, optional DNS hostname, and other properties.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/get_vnic.htm#)
- 

- 

Open the navigation menu and select Compute &gt; Instances . The Instances page appears. All instances are listed in tabular form.
- 

(optional) Select a State from the list to limit the VCNs displayed to that state.
- 

Select the instance associated with the VNIC to which you want to assign a secondary private ID. The instance's Details page appears.
- 

Select Attached VNICs under Resources . The primary VNIC is listed. If the instance has two[active physical NICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#overview), the VNICs are grouped by NIC 0 and NIC 1.
- 

Select the VNIC whose details you want to get. The VNIC Details page appears.
- 

Use the[oci network vnic get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/get.html)command and required parameters to get the details of a VNIC on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VNIC/../../Access/cli_install.htm#CLI)
- 

Run the[GetVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic)
