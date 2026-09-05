# Managing Network Perimeters
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/overview.htm
- Fetched: 2026-09-05 02:25 CDT

# Managing Network Perimeters

Network perimeters in an identity domain in Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) restrict the IP addresses, countries, and VCNs that users can use to sign in.

You can perform the following tasks related to network perimeters:
- [IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/overview.htm#overview)
- [Listing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/listing_network_perimeters.htm)
- [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm)
- [Getting a Network Perimeter's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/view-details-network-perimeter.htm)
- [Updating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/modify-network-perimeter.htm)
- [Deleting a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/remove-network-perimeters.htm)

## IP Addresses

After you create a network perimeter, you can control who can sign in to an identity domain based on the user's IP address.
- Allow only the IP addresses you specify.
- Block specific IP addresses or ranges.

IAM supports both IPv4 and IPv6.

Allowlists and Blocklists Allowlist Only users signing in from the IP addresses you define are allowed to sign in to an identity domain. Blocklist Users signing in from IP addresses you define are denied access to an identity domain.

You can use an allowlist, a blocklist, or both, depending on your security policy.

IP Address Formats You Can Use Single IP Address
- Enter one or more exact IP addresses.
- Separate multiple IP addresses with commas.
- Examples:`10.11.12.13`(IPv4),`2001:db8::1`(IPv6). IP Range (two addresses separated by a hyphen)
- Specify a start and end IP address with a hyphen.
- Example: (IPv4):`10.10.10.1-10.10.10.10`. Any address from`10.10.10.1`through`10.10.10.10`is included. CIDR Block (masked range)
- Use a Classless Inter-Domain Routing (CIDR) notation to define a network.
- The number after the slash is the prefix length (number of network bits).
- Examples:`10.11.12.0/24`(all IPv4 addresses starting with`10.11.12`),`2001:db8::/32`(IPv6).

Note  
  
The examples listed use IP addresses with the IPv4 protocol. However, you can apply the same formats to IP addresses that use the IPv6 protocol (for example,`B138:C14:52:8000:0:0:4D8`).

After defining network perimeters, you can assign them to a sign-on policy, and configure the policy so that if you're trying to sign in to an identity domain using an IP address that's defined in the network perimeter, you can sign in to an identity domain or be prevented from accessing an identity domain. You can also use the network perimeter as a allowlist for OAuth token issuance for an OAuth client application. Token requests from outside the network perimeter will be denied.

You can also configure the your Enterprise or Confidential application by providing client configurations.

For more information about assigning network perimeters to a sign-on policy, see[Add a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../signonpolicies/add-sign-policy.htm).

For more information about restricting the Client IP address by a network perimeter (client configuration), see[Configuring OAuth](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../applications/to-configure-oauth.htm)
