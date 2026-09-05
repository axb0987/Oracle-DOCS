# Delete a Reserved Public IP Address for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm
- Fetched: 2026-09-05 03:00 CDT

# Delete a Reserved Public IP Address for a Roving Edge Infrastructure Device

Describes how to delete a reserved public IP address from your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm#)
- 

- Open the navigation menu and select Networking &gt; IP Management . The IP Management page appears.
- Select Reserved Public IPs . The Reserved Public IP Addresses page appears. The reserved public IP addresses are listed in tabular form.
- Select the Actions menu ( ) to the right of the IP address, and select Terminate .
- Confirm the termination when prompted.

The reserved public IP address list reappears without the IP address you terminated.
- 

Use the[oci network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html)command and required parameters to delete a reserved public IP address from your Roving Edge Infrastructure device:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLI)
- 

Run the[DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp)
