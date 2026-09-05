# Creating a PSA Endpoint
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-create.htm
- Fetched: 2026-09-05 02:46 CDT

# Creating a PSA Endpoint

Create a PSA endpoint in a Virtual Cloud Network (VCN) to allow private access to the Oracle Services Network (OSN).
You can only create a PSA endpoint in an existing subnet in a VCN. You can't create the endpoint while creating a VCN or subnet.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-create.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-create.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/psa-create.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN or subnet that you want to create a PSA endpoint in. If you need help finding the list page for the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm)or[Listing Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-subnets.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Private service access tab, select Create .
- Enter a friendly name for the PSA endpoint. It doesn't have to be unique. Avoid entering confidential information.
- Verify the compartment that you want to create the PSA endpoint in. Select another compartment if needed.
- (Optional) In the Tags section, add one or more tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- In the Service section, select the Oracle Services Network (OSN) service you want the PSA endpoint to enable access to. You can only select one per endpoint.
- In the Network section, select the compartment for the PSA endpoint's subnet, and the subnet itself.
- Select whether the PSA endpoint's private IPv4 address is automatically or manually assigned.

If you select Automatically assign a private IPv4 address , you can decide between ephemeral (dynamically allocated from the available IP addresses in the subnet by Oracle) or persistent IPv4 addresses (selected from existing[reserved private IPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-ipv4-ipv6.htm)).

If you select Manually assign a private IPv4 address , you can either Provide private IPv4 address and enter the address in the field, or Select existing reserved IPv4 address from the list of available addresses.
- (Optional) Decide whether to add ZPR security attributes on the PSA endpoint.

If you select this option, you can add up to three security attributes to restrict access to resources. If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- (Optional) Decide whether to add the PSA endpoint to an[NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/networksecuritygroups.htm).

If you select this option, select the compartment that contains the NSG and then select the NSG you want.
- Select Create private service access endpoint .
- 

Use the[psa private-service-access create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/psa/private-service-access/create.html)command and required parameters to create a PSA endpoint:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreatePrivateServiceAccess](https://docs.oracle.com/iaas/api/#/en/psasvc/latest/PrivateServiceAccess/CreatePrivateServiceAccess)
