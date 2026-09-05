# Editing a Reserved Public IP Address for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm
- Fetched: 2026-09-05 03:01 CDT

# Editing a Reserved Public IP Address for a Roving Edge Infrastructure Device

Describes how to edit a reserved public IP address for your Roving Edge Infrastructure device.

You can only rename the reserved public IP address using the Device Console. Use the CLI or API method to perform other edits on the IP address.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm#)
- 

- Open the navigation menu and select Networking &gt; IP Management . The IP Management page appears.
- Select Reserved Public IPs . The Reserved Public IP Addresses page appears. The reserved public IP addresses are listed in tabular form.
- Select the Actions menu ( ) to the right of the IP address, and select Rename . The Rename dialog box appears.
- Enter the updated name the IP address and select Save Changes .

The reserved public IP address list reappears displaying the updated IP address name.
- 

Use the[oci network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html)command and required parameters to edit a reserved public IP address for your Roving Edge Infrastructure device:

```

```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLI)
- 

Run the[UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp)
