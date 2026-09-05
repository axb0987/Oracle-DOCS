# Private DNS Resolvers
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm
- Fetched: 2026-09-05 02:41 CDT

# Private DNS Resolvers

A private DNS resolver answers DNS queries for a VCN per a configuration you create.

When you create a VCN and select the[Use DNS hostnames in this VCN option, this choice creates a dedicated private DNS resolver and a default private view with system-managed zones. A private DNS resolver also handles internal DNS queries for the VCN based on private views and the private zones that you have created and the[rules you create for the resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm). A private DNS zone has capabilities similar to an internet DNS zone, but only provides responses for clients that can reach it through a VCN. The default view is only used if the resolver doesn't get a match from the other attached private views, if any. A private resolver can be configured to use views and zones and also conditional forwarding rules to define how to respond to DNS queries. To better understand views and zones, see[Private DNS](https://docs.oracle.com/iaas/Content/DNS/Tasks/privatedns.htm).

You can create custom domains to use in addition to the system-generated names based on VCNs and subnets, and you can do VCN to VCN and VCN to on-premises resolution.

## Private Resolver Tasks

- [Listing Resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-list.htm)
- [Adding a Private View to a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-add-view.htm)
- [Removing a Private View From a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-remove-view.htm)
- [Getting a Resolver's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-get.htm)
- [Editing a Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-update.htm)
- [Moving a Resolver Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-move.htm)

To manage DNS zones and views, See[Managing Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm)
