# Removing a Private View From a Resolver
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm
- Fetched: 2026-09-05 02:47 CDT

# Removing a Private View From a Resolver

You can remove a nondefault private view from a resolver.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)for more information and a feature overview.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-remove-view.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Select the name of the DNS resolver for the VCN. The Private Resolver Details screen appears.
- Select the Associated private views tab.
- Select the checkbox next to the private view you want to remove from the resolver. Remove can now be selected. You can select other private views.
- Select Remove .

Note  
  
You can also remove a private view from the Manage Private Views screen by selecting the red button labeled - and then selecting Save Changes .
- 

Use the[resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html)command and required parameters to remove a private view from a resolver. In the`attached-views`parameter, don't include the view OCID value for the view you want to remove.

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver)
