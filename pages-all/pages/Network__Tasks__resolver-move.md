# Moving a Resolver Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm
- Fetched: 2026-09-05 02:47 CDT

# Moving a Resolver Between Compartments

You can move a resolver from one compartment to another.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)for more information and a feature overview.

See[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for information about compartments and access control.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm#)
- 

You can only edit the resolver name using the Console.

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Select the name of the DNS resolver for the VCN. The Private Resolver Details screen appears.
- Select Actions , then select Move resource .
- Select a destination compartment from the list.
- Select Move resource .
- 

Use the[resolver change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/change-compartment.html)command and required parameters to move a resolver from one compartment to another:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ChangeResolverCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ChangeResolverCompartment)
