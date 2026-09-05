# Renaming a Subnet for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm
- Fetched: 2026-09-05 03:00 CDT

# Renaming a Subnet for a Roving Edge Infrastructure Device

Describes how to rename a subnet under a VCN on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm#)
- 

- 

Open the navigation menu and select Networking &gt; Virtual Cloud Networks . The Virtual Cloud Networks page appears. The single virtual cloud network (VCN) is listed in tabular form.
- 

Select the VCN. The VCN's Details page appears.
- 

Select Subnets . All subnets are listed in tabular form.
- 

Select the subnet whose details you want to get. The subnet's Details page appears.
- 

Select Edit . The Edit Subnet dialog box appears.
- 

Enter the new Name of the subnet.
- 

Select Save Changes .
- 

Use the[oci network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html)command and required parameters to rename a subnet under a VCN on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLI)
- 

Run the[UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet)
