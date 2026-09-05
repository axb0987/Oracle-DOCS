# Adding Security Attributes to a VCN
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm
- Fetched: 2026-09-05 02:45 CDT

# Adding Security Attributes to a VCN

Use Zero Trust Packet Routing with an existing Virtual Cloud Network (VCN).

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- On the details page, go to the Security tab and perform one of the following actions depending on the option that you see:

- In the Security attributes section, select Add .
- Select Add security attributes
- In the panel that opens, select Add security attribute , and then enter the following information:

- Security attribute namespace : A security attribute namespace is a container for a set of security attributes in Zero Trust Packet Routing (ZPR).
- Security attribute key : The name for a specific security attribute.
- Security attribute value : The value for a specific security attribute.

These values must match an existing ZPR policy. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)
- When finished, select Add security attributes .
- 

Use the[network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html)command and parameters shown to add security attributes when you create a VCN:

```

```

Use the[network vcn update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/update.html)command and parameters shown to add security attributes to an existing VCN:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn)operation to add security attributes when you create a VCN, and use the securityAttributes attribute.

Run the[UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn)
