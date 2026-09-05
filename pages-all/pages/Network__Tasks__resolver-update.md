# Editing a Resolver
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm
- Fetched: 2026-09-05 02:47 CDT

# Editing a Resolver

You can update information such as the resolver name.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)for more information and a feature overview.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-update.htm#)
- 

When using the Console, you can only edit the resolver name.

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Select the name of the DNS resolver for the VCN. The Private Resolver Details screen appears.
- Select Actions , then select Edit .
- Update the resolver Name .
- Select Save changes .
- 

Use the[resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html)command and required parameters to edit a resolver:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver)
