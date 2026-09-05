# Moving a Secondary Private IP Address to a Different VNIC
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm
- Fetched: 2026-09-05 02:46 CDT

# Moving a Secondary Private IP Address to a Different VNIC

Move a secondary private IP address to another VNIC in the same subnet.

Note  
  
Using the CLI or API, you can also move more than one secondary private IP to a VNIC in the same subnet with a single command.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#)
- 

- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the name of the instance to open its details page.
- On the Networking tab, go to the Attached VNICs section and select the VNIC that you're interested in.
- On the IP administration tab, select Assign secondary private IP address and then enter the private IP address information:

- IPv4 Address : Select an IPv4 CIDR block to automatically assign the IPv4 address. The available choices depend on what you select in IPv4 address assignment .
- IPv4 address assignment : Manually assign IPv4 addresses to enter a specific IPv4 address from a CIDR block assigned to this subnet.
- Private IP address : Enter the secondary private IP address to move.
- CIDR prefix length : (Optional) Enter a netmask value if you want to assign an IP CIDR address. If you leave this field blank, the system uses 32 to assign a single private IP address. You can't reassign a private IP address if it's part of an IP CIDR address, but you can reassign an IP CIDR address itself.
- Unassign if already assigned to another VNIC : Select this option to move the secondary IP address from the current VNIC.
- Hostname : (Optional) Enter the hostname to use for DNS in the cloud network. This field is available only if the VCN and subnet both have DNS labels. For more information, see[DNS in a Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns.htm). This field isn't available if the CIDR prefix length used is in the range of 18-31.
- Public IP type : (Optional) This field is available only if the VNIC is in a public subnet. For more information, see[Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm). This field isn't available if the CIDR prefix length is used is in the range of 18-31.
- 

Route Table : (Optional) Assign a custom route table to handle traffic from this IP address. For more information, see[Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing). If you assign a custom route table, traffic from this IP address doesn't use the default VCN or subnet route tables.
- To assign more IPv4 objects to the instance VNIC, select + Another IPv4 address . However, the objects must come from the same subnet.
- Select Assign .
- 

Use the[network vnic assign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/assign-private-ip.html)command and required parameters to move a secondary private IP address from one VNIC to another:

```

```

Optionally, use the[network private-ip bulk-update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/bulk-update.html)command and required parameters to move more than one secondary private IP address from one VNIC to another:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp)operation to move a private IP address from one VNIC to another.

Optionally, run the[BulkUpdatePrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/BulkUpdatePrivateIps)
