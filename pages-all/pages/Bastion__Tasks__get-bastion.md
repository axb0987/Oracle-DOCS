# Getting a Bastion's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm
- Fetched: 2026-09-05 01:42 CDT

# Getting a Bastion's Details

Get the details of a bastion in a compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/get-bastion.htm#)
- 

On the Bastions list page, find the bastion that you want to work with. If you need help finding the list page or the bastion, see[Listing Bastions](https://docs.oracle.com/en-us/iaas/Content/Bastion/Tasks/list-bastion.htm).
The details page opens and displays the following information about the bastion. Access the various resources associated with the bastion by selecting their links or tabs.
- OCID : The Oracle-assigned unique ID for the bastion.
- Created : The timestamp of bastion creation.
- Target virtual cloud network : The target VCN of the target resource that you intend to connect to by using sessions hosted on this bastion.
- Target subnet : The target subnet within the target VCN.
- Maximum session time-to-live (TTL) : The amount of time the session remains active before it ends.
- CIDR block allowlist : A list of IP address ranges in CIDR notation that are allowed to access the bastion .
- Compartment : A collection of related resources that can be accessed only by groups that have been given permission by an administrator in the organization.
- Private endpoint IP address : An internal IP address assigned to a private endpoint that allows communication between resources.
- Bastion type : Currently only a standard bastion type is supported.
- FQDN support : When enabled, FQDN support allows targets in the bastion to connect using FQDN.
- SOCKS5 support : When enabled, SOCKS5 support allows targets in the bastion to connect dynamically using SOCKS5 proxy.
- 

Use the[oci bastion bastion get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bastion/bastion/get.html)command and required parameters to get details about a bastion:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[GetBastion](https://docs.oracle.com/iaas/api/#/en/bastion/latest/Bastion/GetBastion)
