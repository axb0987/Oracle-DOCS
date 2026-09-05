# Adding a Private View to a Resolver
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm
- Fetched: 2026-09-05 02:47 CDT

# Adding a Private View to a Resolver

You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN.
Each VCN's dedicated resolver has a protected default view. You can add custom zones to the default view, within restrictions on zone names to avoid collisions with protected zones. If a resolver is deleted, and its default view contains nonprotected zones, then the default view is converted to a nonprotected view instead of being deleted. You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN.

See[Private DNS Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/dns-topic-Private-resolver.htm)for more information and a feature overview.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- Look in the VCN details tab and select the name of the DNS resolver for the VCN. The Private Resolver Details screen appears.
- From the Private Resolver Details screen, select the Associated private views tab, then select Manage Private Views . The Manage Private Views screen appears.
- Select an already created private view from the drop down menu in the numbered Private view list.
- To associate another view, select Additional Private View select another view.
- When you're finished, select Save Changes .
Views created automatically by Oracle are available in addition to views you create.
- 

Use the[resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html)command and required parameters to add a private view to a resolver:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver)operation to add a private view to a resolver. Include the`AttachedViews`
