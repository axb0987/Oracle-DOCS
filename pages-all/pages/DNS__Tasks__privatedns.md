# Private DNS
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm
- Fetched: 2026-09-05 01:59 CDT

# Private DNS

Create and manage private domain name system (DNS) zones .

Use private domain name service (DNS) zones to create private zones with domain names that you specify. You can fully manage the zones and records to provide hostname resolution for applications running within and between virtual cloud networks ( VCNs ), and on-premises or other private networks. Traffic Management is only available for public DNS, and isn't supported on private DNS.

Private DNS also provides DNS resolution across networks (for example, another VCN within the same region, cross region, or external network). Private DNS can be managed in the OCI DNS API and Console.

## Resources used in Private DNS

DNS Resources
- Private DNS Zones : Private DNS zones contain DNS data only accessible from within a Virtual Cloud Network (VCN) such as private IP addresses. A private DNS zone has similar capabilities to an internet DNS zone, but provides responses only for clients that can reach it through a VCN. Each zone belongs to a single view.
- Private DNS Zone Records : Different record types are supported for global and private DNS. See[Supported Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#privatedns_topic_supported_resource_records).
- Private DNS Views : A private DNS view is a collection of private zones. The same zone name can be used in many views, but zone names within a view must be unique.
- Private DNS Resolver : A VCN-dedicated private DNS resolver contains the configuration that serves responses to DNS queries within the VCN. Views on the resolver decide the zone and record data applicable for resolution. The resolver performs recursion to the internet and DNSSEC validation for DNSSEC-signed zones. Resolver endpoints on the resolver provide another ingress and egress besides the default ingress on 169.254.169.254. For more information, see[Private DNS Resolvers](https://docs.oracle.com/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm).
- Private DNS Resolver Endpoint : Use resolver endpoint resources to set up ingress and egress in the VCN. Resolver endpoints consume IP addresses in the subnet you create it in. A corresponding VNIC is created for each resolver endpoint.

VCN Resources:
- VCN : When you create a VCN, a dedicated resolver is also automatically created.
- Subnet : A subnet within a VCN is used when creating resolver endpoints. IP addresses from the subnet are consumed for listening and forwarding addresses.
- Network Security Group (NSG) : Optionally, you can configure a list of network security groups for resolver endpoints. NSGs control ingress and egress traffic to and from the resolver endpoint.

See[Private DNS resolvers](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm#Private_resolver)in the Networking documentation for more information about VCN resources.

## Protected Resources

Some private DNS resources, such as zones and views, are protected. Protected resources are managed automatically by Oracle. You can view protected resources, but editing is limited. Protected resources don't count toward service limits or quotas.
- All VCN-dedicated resolvers
- Default Views: Each VCN-dedicated resolver has a protected default view. You can add more zones to the default view, but restrictions apply to zone names to avoid collisions with protected zones. If a resolver is deleted, and its default view contains zones that aren't protected, then the default view is converted to a view that isn't protected instead of being deleted. You can create and attach a view to a resolver in addition to the default view so that their zones are resolvable in the VCN.

## Configuration and Resolution

### DNS

You can create a full or partial domain tree. A view can be used by any number of resolvers , and share private DNS data across VCNs within the same region. You can use these zones for split-horizon DNS because the same zone name can be used on a private zone and an internet zone. Different answers can be served for public queries and private queries from within a VCN.
The resolver listens on 169.254.169.254 by default. You can decide to define resolver endpoints for more ingress and egress. A listening resolver endpoint consumes one IP address for listening within the specified subnet . A forwarding resolver endpoint consumes two IP addresses, one address is unused and the second address is used for forwarding. Before you create a resolver endpoint, ensure that enough IP addresses are available in the subnet.
Important  
  
The subnet for private DNS endpoints must be IPv4 only. A request to create a private DNS endpoint in an IPv6 enabled subnet doesn't succeed.

Add rules to define the logic for answering queries. The only supported rule type is FORWARD. This rule conditionally forwards a query to a destination IP based on client IP or target QNAME . The destination IP address can be for an on-premises setup, private network, or listening resolver endpoint in a different VCN. Resolver rule qnameCoverConditions cover exact matches and also subdomains.

DNS responses in a VCN are evaluated using the configuration of the dedicated resolver in a specific order:
- Each attached view is evaluated in order. The default view is evaluated last, if not explicitly included in the list.
- [Resolver Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)are evaluated in order. The first resolver rule that matches the view is applied. Any rule farther down the list with duplicate conditions (including no conditions) to a previous is never evaluated. An example of an unreachable rule is a more specific qnameCoverCondition or clientAddressConditions after a more general one; if the more general rule is a match the more specific rule is never evaluated.
- The query is resolved to the internet.

The first item in sequence able to provide an answer does so. After an answer is provided, no further items are evaluated, even if the answer is negative.

For example, if a query name is included by a zone in a private view and the name doesn't exist in the zone, the zone returns an authoritative NXDOMAIN response.

### VCN

Ingress and egress between VCNs or between VCNs and on-premises networks require connectivity. Establishing a connection might require a local peering gateway ( LPG ), having both VCNs attached to the same DRG, or a remote peering connection ( RPC ) between VCNs. Connection between a VCN and on-premises networks require either FastConnect or an IPSec tunnel (Site-to-Site VPN).

VCN security lists and any referenced NSGs need to allow the required traffic. DHCP on the security list needs to be enabled for ingress and egress and include the corresponding resolver endpoint's IP address. Security rules for listening endpoints need to allow connectionless UDP ingress on destination port 53, connectionless UDP egress on source port 53, and TCP ingress on destination port 53. Security rules for forwarding endpoints need to allow connectionless UDP egress on destination port 53, connectionless UDP ingress on source port 53, and TCP egress on destination port 53.

For more information see the tutorial[Configure private DNS zones views and resolvers](https://docs.oracle.com/en/learn/oci_private_dns/).

## Use Cases

### Custom DNS Zones Within a VCN

Private DNS zones are grouped into views . All VCN dedicated resolvers have a default view which is created automatically. To create a custom DNS zone that resolves from within a VCN, either create the private zone in the dedicated resolver's default view, or create the zone in a new view and add it to the dedicated resolver's list of attached views. See[Help Center/Configure private DNS zones views and resolvers](https://docs.oracle.com/en/learn/oci_private_dns/)for a detailed guide on how to set this up.

### Split Horizon

Create private zones with the same names as public names on the Internet. Then, add the zones to one of the VCN resolver's views. Within the VCN, the names resolve based on the private DNS configuration. The same names serve different answers depending on where the request originates. See also[Private DNS Zone Transparency](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns-zone-transparency).

### Shared Private DNS Zones Within a Region

VCNs within the same region can resolve requests from each other's private views. For example, let's say you want to implement this solution with VCN A and VCN B. Add VCN A's dedicated resolver's default view to VCN B's dedicated resolver's attached views. Then, add VCN B's dedicated resolver's default view to VCN A's dedicated resolver's attached views.

The same private zone or collection of private zones can be reused across several VCNs. This solution can reduce DNS configuration duplication. Create a view and add one or more private zones to the view. For each VCN, add the new view to the VCN's dedicated resolver's list of attached views. See[Help Center/Configure private DNS zones views and resolvers](https://docs.oracle.com/en/learn/oci_private_dns/)for a detailed guide on how to set this up.

### Private DNS Zone Transparency

For private DNS zones, you can set the DNS resolution mode to change the behavior of the query resolution when a query name matches a zone name. A common use case for transparency is when a zone name exists in multiple locations, such as in OCI and on-premises. Transparency allows the same zone name to exist in both locations while having different zone records. Three modes are available:
- Static : This is the default behavior. If a private zone covers a query name, an NXDOMAIN is returned if the query name isn't present in the zone. A NoData response is returned if the name is present but there is no data for the specific query type requested.
- Transparent : If the queried domain is covered by the zone, but the domain doesn't exist in the zone or the queried domain matches the zone name but no records of the queried type exist, continue to the next evaluation for the resolver following the normal sequence for checking query resolution. This effectively bypasses NXDOMAIN responses at all domains and NoData responses specifically at the apex.
- RTypeTransparent : If the queried domain is covered by the zone, but the queried domain doesn't exist in the zone or the queried domain exists in the zone but not for the requested record type, continue to the next evaluation for the resolver following the normal sequence for checking query resolution. This effectively bypasses NXDOMAIN and NoData responses at all domains.
Note  
  
If transparency triggers a sequence to continue on, resolution evaluation begins at the next view in the sequence, if one exists. A maximum of 2 transparency continuations occur. If a third transparency match occurs, a SERVFAIL response is returned.

[Examples](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#)

To illustrate transparency behavior, the following tables provide a sample config and examples for how query resolution occurs with the different resolution modes.

Configuration for Private and Public Zones: example.us-ashburn-1.oraclecloud.com
Query Name Record Type RDATA
Private Zone
example.us-ashburn-1.oraclecloud.com A 1.2.3.4
bla.example.us-ashburn-1.oraclecloud.com A 5.6.7.8
api.example.us-ashburn-1.oraclecloud.com CNAME example.us-ashburn-1.oraclecloud.com
Public Zone
example.us-ashburn-1.oraclecloud.com A 100.100.100.100
example.us-ashburn-1.oraclecloud.com TXT "Hello!"
foo.example.us-ashburn-1.oraclecloud.com A 200.200.200.200
bla.example.us-ashburn-1.oraclecloud.com TXT "World!"
api.example.us-ashburn-1.oraclecloud.com CNAME example.us-ashburn-1.oraclecloud.com

Behaviors for Zone: example.us-ashburn-1.oraclecloud.com
Example Query name/type Static Transparent RTypeTransparent Notes
1 example.us-ashburn-1.oraclecloud.com/a 1.2.3.4 1.2.3.4 1.2.3.4 A match occurs on the exact name and query type, which gives the Private name (therefore 100.100.100.100 is never seen from this resolver).
2 example.us-ashburn-1.oraclecloud.com/txt NoData "Hello!" "Hello!" The override covers the name but not query type, so a Static zone indicates NoData (name exists, but not qtype) while RtypeTransparent continues to the Internet. Because this is the zone apex, Transparent also continues to the Internet.
3 bla.example.us-ashburn-1.oraclecloud.com/txt NoData NoData "World!" The override covers the name but not query type, so Static zones and Transparent zones indicate NoData (name exists, but not qtype) while RtypeTransparent continues to the Internet. Unlike #2, this isn't the Apex, hence the Transparent zone doesn't fall through.
4 foo.example.us-ashburn-1.oraclecloud.com/a NXDOMAIN 200.200.200.200 200.200.200.200 A matching private zone exists, so static indicates that "foo" doesn't exist, but as there isn't a name match, both Transparent and RtypeTransparent continue to the Internet.
5 api.example.us-ashburn-1.oraclecloud.com/a 1.2.3.4 1.2.3.4 1.2.3.4 Because the CNAME exists in both private and internet zones, all three modes— Static , Transparent , and RtypeTransparent resolve the A record to 1.2.3.4 from the private zone. Transparent mode only falls back to internet if the record type is missing in the private zone.
6 api.example.us-ashburn-1.oraclecloud.com/txt NoData NoData "Hello!" For a CNAME TXT query where the record exists only in the internet zone, Static and Transparent modes return NoData, since the private zone doesn't contain the record type. RtypeTransparent falls back to the internet zone and returns the TXT value.

### DNS Resolution Between VCNs

Send requests between VCNs using resolver endpoints. The VCNs can exist in different regions. This solution requires either a local or remote peering gateway ( LPG / RPG ). To send traffic from VCN A to VCN B, add a listening endpoint to VCN B's resolver. Then, add a forwarding endpoint to VCN A's dedicated resolver.

Create a rule on VCN A's dedicated resolver that forwards traffic through VCN A's forwarding endpoint to the address of VCN B's listening endpoint. To send traffic in both directions between the VCNs, add a forwarding and listening resolver endpoint to each dedicated resolver and add a rule on each dedicated resolver.

### Connectivity Between a VCN And On-Premises Name Servers

Requests can be sent between a VCN and on-premises name servers in either direction. This solution requires connectivity between the VCN and the on-premises network using either FastConnect or an IPSec tunnel (IPSec VPN). To send traffic to a VCN, add a listening endpoint to its dedicated resolver and send traffic to its address. To send traffic from a VCN, add a forwarding endpoint to its dedicated resolver and a rule that forwards traffic through the endpoint to the address of the on-premises name server.

### Advanced Use Cases

VCNs can be set up for more than one use case. A single VCN could be both peered with another VCN, and configured to connect to an on-premises name server. Forwarding can also be chained across many VCNs.

## Supported Resource Records

The Oracle Cloud Infrastructure DNS service supports many resource record types. The following list provides a brief explanation of the purpose of each supported record type for private DNS. For public DNS, see[Public DNS Supported Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm). Avoid entering confidential information when entering record data. The RFC links direct you to further information about the record types and data structure.

### Note About RDATA

OCI normalizes all RDATA into the most machine readable format. The returned presentation of RDATA can differ from its initial input.

Example:

The RDATA for the[CNAME](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns-resource-record-types__dlentry_cname-private),[DNAME](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns-resource-record-types__dlentry_dname-private), and[MX](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns-resource-record-types__dlentry_mx-private)record types can contain one or more absolute domain names. If the specified RDATA for one of these record types doesn't end in a dot or period to represent the root, the period is added.

`www.example.com --> www.example.com.`

You can use various DNS libraries to normalize RDATA before input.

Programming Language Library
Go[DNS Library in Go](https://github.com/miekg/dns)
Java[dnsjava](https://github.com/dnsjava/dnsjava)
Python[dnspython](http://www.dnspython.org/)

### Private DNS Resource Record Types
A An address record used to point a hostname to an IPv4 address. For more information about A records, see[RFC 1035](https://tools.ietf.org/html/rfc1035#page-21). AAAA An address record used point a hostname at an IPv6 address. For more information about AAAA records, see[RFC 3596](https://tools.ietf.org/html/rfc3596#section-2.1). CAA A Certification Authority Authorization record is used by a domain name holder to specify one or more Certification Authorities authorized to issue certificates for that domain. For more information about CAA records, see[RFC 6844](https://tools.ietf.org/html/rfc6844#section-3). CNAME A Canonical Name record identifies the canonical name for a domain. For more information about CNAME records, see[RFC 1035](https://tools.ietf.org/html/rfc1035#page-13). DNAME A Delegation Name record has similar behavior to a CNAME record, but maps an entire subtree beneath a label to another domain. For more information about DNAME records, see[RFC 6672](https://tools.ietf.org/html/rfc6672#section-2). MX A Mail Exchanger record defines the mail server accepting mail for a domain. MX records must point to a hostname. MX records must not point to a CNAME or IP address. For more information about MX records, see[RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). PTR A Pointer record reverse maps an IP address to a hostname. This behavior is the opposite of an A Record, which forward maps a hostname to an IP address. PTR records are commonly found in reverse DNS zones. For more information about PTR records, see[RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). SRV A Service Locator record is used by administrators to set up a single domain for several servers. For more information about SRV records, see[RFC 2782](http://tools.ietf.org/html/rfc2782). TXT A Text record holds descriptive, human readable text, and can also include non-human readable content for specific uses. This record type is commonly used for SPF records and DKIM records that require non-human readable text items. For more information about TXT records, see[RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).

## Required IAM Policies

To work with private DNS, a user needs enough authority (by way of an IAM policy). Users in the Administrators group have the required authority. If a user isn't in the Administrators group, then a policy such as this lets a specific group manage private DNS:
```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for private DNS, see[DNS Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).

## Private DNS Tasks

### Setting up Private DNS

Use these steps to set up private DNS:
- [Create a private zone with a private view](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm)
- [Create a private view](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-create.htm)
- [Add records to the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)

### Private DNS Tasks

See these sections for information on managing private DNS resources:
- [Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm)
- [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/views.htm)
- [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm)

### VCN Tasks

To create a VCN with a dedicated DNS resolver, see[Overview of VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm)and[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm)
