# Creating a VCN for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create_vcn.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a VCN for a Roving Edge Infrastructure Device

Describes how to create a VCN on your Roving Edge Infrastructure device.

Only a single VCN is supported on each Roving Edge Infrastructure device.

These procedures create a VCN without any subnets or gateways for access. Manually create the subnets and other resources before using the VCN. Currently, Roving Edge Infrastructure supports only one VCN with only one CIDR Block.
Note  
  

The IPv6 option is not supported when creating a VCN. Including any reference to IPv6 in your creation of a VCN (is-ipv6-enabled=true|false) results in a failure.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create_vcn.htm#)
- 

- 

Open the navigation menu and select Networking &gt; Virtual Cloud Networks . The Virtual Cloud Networks page appears. The single virtual cloud network (VCN) is listed in tabular form.
- 

Select Create VCN . The Create a Virtual Cloud Network dialog box appears.
- Enter the following:
- 

Name : A descriptive name for the VCN. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- 

CIDR Block : The one valid IPv4 CIDR block for the VCN. For example: 172.16.0.0/16. You cannot change this value later.
- 

DNS Resolution : Check Use DNS Hostnames in this VCN if you want to enable this functionality. Checking this option is required for assignment of DNS hostnames to hosts in the VCN. Enabling this option is required if you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ).

If enabled, you can specify a DNS label for the VCN, otherwise, the Device Console generates one for you. The dialog box automatically displays the corresponding DNS Domain Name for the VCN (`<VCN DNS label>.oraclevcn.com`).
- 

Select Create VCN .

Next, create one or more subnets in the cloud network. See[Subnets for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../Subnet/subnet_management.htm#SubnetManagement).
- 

Use the[oci network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html)command and required parameters to create a VCN on your Roving Edge Infrastructure devices.:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../compartments.htm#comparments).

The`cidr_block`parameter lists the one valid IPv4 CIDR block for the VCN

For example:`--cidr-block 10.0.0.0/16`

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/../../Access/cli_install.htm#CLI)
- 

Run the[CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn)
