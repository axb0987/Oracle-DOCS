# Creating a Subnet for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm
- Fetched: 2026-09-05 03:00 CDT

# Creating a Subnet for a Roving Edge Infrastructure Device

Describes how to create a subnet under the VCN on your Roving Edge Infrastructure device.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/create_subnet.htm#)
- 

- 

Open the navigation menu and select Networking &gt; Virtual Cloud Networks . The Virtual Cloud Networks page appears. The single virtual cloud network (VCN) is listed in tabular form.
- 

Select the VCN. The VCN's Details page appears.
- 

Select Create Subnet . The Create Subnet dialog box appears.
- 

Specify the resources to associate with the subnet. By default, the subnet is created in the root compartment, where you can also choose your resources.

Enter the following:
- 

Name : A friendly name for the subnet. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
- 

CIDR Block : A single, contiguous CIDR block for the subnet (for example, 172.16.0.0/24). Ensure that the CIDR block is within the cloud network's CIDR block and does not overlap with any other subnets. You cannot change this value later.
- 

Use DNS Hostnames in this SUBNET : This option is available only if you provided a DNS label for the VCN during creation. The option is required for assignment of DNS hostnames to hosts in the subnet. Enabling this option is required if you plan to use the VCN's default DNS feature (called the Internet and VCN Resolver ).

If the check box is selected, you can specify a DNS label for the subnet, otherwise the Device Console generates one for you. The dialog box automatically displays the corresponding DNS Label for the subnet (`<subnet_DNS_label>.<VCN_DNS_label>.oraclevcn.com`).
- 

DHCP Options : The set of DHCP options to associate with the subnet.
- 

Select Create Subnet . The subnet is then created and displayed on the Subnets page in the root compartment.
- 

Use the[oci network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html)command and required parameters to create a subnet under a VCN on your Roving Edge Infrastructure devices:

```

```

To determine your Roving Edge Infrastructure device compartment OCID, see[Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../compartments.htm#comparments).

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See[Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLIAccessHelp).

For CLI setup information on your Roving Edge Infrastructure device, see[Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/../../Access/cli_install.htm#CLI)
- 

Run the[CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet)
