# Assigning a New Secondary Private IP to a VNIC
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm
- Fetched: 2026-09-05 02:46 CDT

# Assigning a New Secondary Private IP to a VNIC

Assign a new secondary private IP address to a VNIC.

Note  
  

Using the CLI or API, you can also assign more than one secondary private IP to a VNIC with a single command.

You can add a secondary private IP to an instance after it's created. You can add it to either the primary VNIC or a secondary VNIC on the instance. The secondary private IP address must come from the CIDR of the VNIC's subnet. You can move a secondary private IP from a VNIC on one instance to a VNIC on another instance if both VNICs belong to the same subnet.

For more information see[Private IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the compartment that contains the instance you want to add a private IP address to.
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- On the IP administration tab, select Assign secondary private IP address and then enter the private IP address information:

- 

IPv4 Address : (Optional) Select an IPv4 CIDR block to automatically assign the IPv4 address. The available choices depend on what you select in IPv4 address assignment .
- Automatically assign IPv4 addresses from prefix : Select this option to let the Console assign an available IPv4 address from an IPv4 CIDR assigned to this subnet. A subnet can have more than one IPv4 prefix.
- Manually assign IPv4 addresses : Select this option to use a specific address from an IPv4 CIDR block assigned to this subnet.
- 

Private IP address : (Optional) Enter an available private IP address from the subnet's CIDR block. If you leave this field blank, the Console assigns a private IP address automatically.
- 

CIDR prefix length : (Optional) Enter an IPv4 network mask length to assign an IP CIDR address. If you leave this field blank, the system creates a host IP address.
- Unassign if already assigned to another VNIC : Select this option to force reassignment of the IP address if it's already assigned to another VNIC in the subnet. Only relevant if you specify a private IP address in the preceding field.
- Hostname : (Optional) A hostname to use for DNS within the cloud network. This field is available only if both the VCN and subnet have DNS labels. See[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm). This field is unavailable if the CIDR prefix length is used in the range of 18-31.
- Public IP Type : (Optional) Only available if the VNIC is in a public subnet. See[Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm). This field is unavailable if CIDR prefix length is used in the range of 18-31.
- Route Table : (Optional) Assign a custom route table to handle traffic from this IP address. For more information, see[Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing).

If you assign a custom route table, traffic from this IP address doesn't use the default VCN or subnet route tables.
- To assign additional IPv4 objects to the instance VNIC, select Another IPv4 address , if you're attaching this VNIC to an existing instance after creation, ensure that the instance's operating system is configured to use IPv4 addressing.
- Select Assign .
- 

Use the[network vnic assign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/assign-private-ip.html)command and required parameters to assign a secondary private IP to a VNIC:

```

```

Optionally, use the[network private-ip bulk-create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/bulk-create.html)command and required parameters to assign more than one secondary private IPv4 address to a VNIC with a single command.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/CreatePrivateIp)operation to assign a new secondary private IP to a VNIC.

Optionally, run the[BulkCreatePrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/BulkCreatePrivateIps)operation to assign more than one secondary private IP to a VNIC within a single API call.

## Next Steps

After assigning a secondary private IP object to a VNIC, you must configure the OS to use it.
- For instances running a variant of Linux, see[Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm).
- For Windows instances, see[Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm)
