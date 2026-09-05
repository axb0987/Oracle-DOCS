# Creating a Reserved Public IP Address for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create-public-ip.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a Reserved Public IP Address for a Roving Edge Infrastructure Device

Describes how to create a reserved public IP address for your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create-public-ip.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create-public-ip.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create-public-ip.htm#)
- 

- Open the navigation menu and select Networking &gt; IP Management . The IP Management page appears.
- Select Reserved Public IPs . The Reserved Public IP Addresses page appears. The reserved public IP addresses are listed in tabular form.
- Select Create Reserved Public IP . The Create Reserved Public IP dialog box appears.
- Complete the following:

- Reserved Public IP Address Name : Enter a name for the reserved public IP address.
- Create in Compartment : Accept the default value.
- IP Address Source in &lt;Compartment&gt; : (optional) The IP pool the reserved public IP is drawn from. If you do not select a pool you've created, the default Oracle pool is used.
- Select Reserved Public IP .

The reserved public IP address you created appears in the list of reserved public IP addresses.
- 

Use the[oci network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html)command and required parameters to create a reserved public IP address for your Roving Edge Infrastructure device:

```

```

where the possible values for`lifetime`are:
- 

EPHEMERAL: You must also specify a privateIpId with the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the primary private IP you want to assign the public IP to. The public IP is created in the same availability domain as the private IP. An ephemeral public IP must always be assigned to a private IP, and only to the primary private IP on a VNIC, not a secondary private IP. Exception: If you create a NatGateway, Oracle automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.
- 

RESERVED: You may also optionally assign the public IP to a private IP by specifying privateIpId . Or you can later assign the public IP with UpdatePublicIp.

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLI)
- 

Run the[CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp)
