# Resolver Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_endpoints.htm
- Fetched: 2026-09-05 02:41 CDT

# Resolver Endpoints

Learn how to use resolver endpoints to listen for, or forward, queries.

Resolver endpoints are attached to a subnet within a VCN. The following types of endpoint are available:
- Listening : A listening resolver endpoint receives queries from these sources: within the VCN, other VCN resolvers, or an on-premises network's DNS. After it's created, no further configuration is needed for a listening endpoint. No listening endpoint is required for Compute instances sending queries to 169.254.169.254.
- Forwarding : A forwarding resolver endpoint forwards DNS queries to a listening resolver endpoint in other peered VCNs or an on-premises network's DNS. Decisions about where to forward queries are based on[resolver rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-resolver_rules.htm)that you define. A DNS forwarding resolver endpoint is required before you can create a corresponding resolver rule.
Note  
  

A resolver endpoint can only be configured to either forward or listen.

IPv6 isn't supported for listening or forwarding resolver endpoints.

Resolver endpoints are highly available and backed by availability domains and fault domains of virtual networking. Resolver endpoints are also backed by private endpoints which have a VNIC. Creating a resolver endpoint in your subnet results in a VNIC being created which consumes an IP address. The corresponding private endpoint and VNIC OCIDs are included on the resolver endpoint object so that you can track what resources in your subnet are related to another. The private endpoints with VNICs enable the ingress and egress between your VCN and other networks.
Note  
  
You can't delete a subnet while its contains a VNIC. You must delete a resolver endpoint in a subnet before being able to delete that subnet.

Network security groups (NSGs) act as a virtual firewall for the DNS resolver endpoints. An NSG consists of a set of ingress and egress[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)that apply only to the associated DNS resolver endpoints. Ultimately these are applied to the VNIC related to the resolver endpoint.

We recommend that you change the security list or NSG security rules to allow traffic bound for UDP Port 53 (and optionally TCP Port 53) on the DNS listener resolver endpoints.

You can perform the following resolver endpoint tasks:
- [Create a resolver endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-create.htm).
- [List the resolver endpoints in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-list.htm).
- [View the details of a resolver endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-get.htm).
- [Add and manage security attributes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-security-attributes.htm).
- [Add and remove Network Security Groups associated with a resolver endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-manage-nsg.htm).
- [Delete a resolver endpoint from a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/resolver-endpoint-delete.htm)
