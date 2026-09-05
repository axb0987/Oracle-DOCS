# Reverse DNS (PTR)
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/reverse_dns.htm
- Fetched: 2026-09-05 02:42 CDT

# Reverse DNS (PTR)

A reverse DNS record, also known as a pointer record (PTR), resolves an IP address back to a fully qualified domain name (FQDN).

Reverse DNS records function in the opposite way of an A (IPv4) or AAAA (IPv6) forward record. For example:`192.0.2.5 → myhost.mydomain.com`.

You can only have a 1:1 connection between the PTR and the IP address. Associating multiple PTRs for the same IP address to multiple hostnames isn't supported.
You can request that a PTR record be established for cloud IP addresses:
- Create an A (IPv4) or AAAA (IPv6) forward record that points the fully qualified domain name to the IP before opening the request. You can create the record using the[Oracle Cloud Infrastructure DNS service](https://docs.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm), or a third-party DNS provider.
- [Open a service request](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)and include the following information:
- The IP address and fully qualified domain name (FQDN) you want in the PTR.
- The FQDN of the forward record that you created in step 1. After the service request is received, the forward (A or AAAA) record information is validated to be sure it can be successfully resolved and matches the specified IP address you provided for the PTR . After validation occurs, Oracle creates the PTR record for you.

## Using the API

Use the following operations to manage resolvers and resolver endpoints:
- [ListResolvers](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ListResolvers)
- [GetResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/GetResolver)
- [UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver)
- [ChangeResolverCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ChangeResolverCompartment)
- [ListResolverEndpoints](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/ListResolverEndpoints)
- [CreateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/CreateResolverEndpoint)
- [GetResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/GetResolverEndpoint)
- [UpdateResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/UpdateResolverEndpoint)
- [DeleteResolverEndpoint](https://docs.oracle.com/iaas/api/#/en/dns/latest/ResolverEndpoint/DeleteResolverEndpoint)
