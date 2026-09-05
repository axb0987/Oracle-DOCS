# Getting an NSG's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm
- Fetched: 2026-09-05 02:41 CDT

# Getting an NSG's Details

Get details for a network security group (NSG) in a virtual cloud network (VCN).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/get-nsg.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that contains the NSG you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/list-vcn.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Security tab, go to the Network Security Groups section.
- Under Resources , select Network Security Groups .
- Select the NSG you're interested in to view its details.

Depending on the options that you see, the NSG's security rules are displayed on the page or on the Security rules tab. From there you can add, edit, or remove rules.
- To see the parent resources that belong to the NSG, depending on the option that you see:

- Select the VNICs tab.
- Under Resources , select VNICs .

If the[parent resource](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison)is a Compute instance, the corresponding VNICs from that instance are also listed on the page.

For other types of parent resources, the relevant service manages the VNICs for you. Therefore, only the parent resource (and not its corresponding VNICs) is listed on the page.
- 

Use the[network nsg get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/get.html)command and required parameters to get an NSG's details:

```

```

Use the[network nsg vnics list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/vnics/list.html)command and required parameters to list the VNICs in the specified NSG:

```

```

Use the[network nsg rules list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/list.html)command and required parameters to list the security rules for the specified NSG:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/GetNetworkSecurityGroup)operation to get an NSG's details.

Run the[ListNetworkSecurityGroupVnics](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroupVnic/ListNetworkSecurityGroupVnics)operation to list the VNICs in the specified NSG.

Run the[ListNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/ListNetworkSecurityGroupSecurityRules)
