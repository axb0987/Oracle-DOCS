# Deleting a Subnet from a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/delete_subnet.htm
- Fetched: 2026-09-05 03:00 CDT

# Deleting a Subnet from a Roving Edge Infrastructure Device

Describes how to delete a subnet under a VCN on your Roving Edge Infrastructure device.

If the subnet is empty, its state changes to TERMINATING briefly and then TERMINATED. If the subnet is not empty, you get an error indicating that instances or other resources contained within that you must delete first.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/delete_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/delete_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/delete_subnet.htm#)
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

Select Terminate .
- 

Confirm the deletion when prompted.
- 

Use the[oci network subnet delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/delete.html)command and required parameters to delete a subnet under a VCN on your Roving Edge Infrastructure devices:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLI)
- 

Run the[DeleteSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/DeleteSubnet)
