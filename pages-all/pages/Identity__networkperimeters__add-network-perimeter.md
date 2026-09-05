# Creating a Network Perimeter
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm
- Fetched: 2026-09-05 02:25 CDT

# Creating a Network Perimeter

Create a network perimeter in an identity domain in Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) and configure it to restrict the IP addresses, countries, and VCNs that users can use to sign in.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../domains/to-view-identity-domains.htm).
- Select Security and then Network perimeters .

A list of existing network perimeters is displayed.
- On the Network perimeters list page, select Create perimeter .
- Enter a unique name and an optional description.
- VCNs : Add a VCN.
- In the VCN section, select Add .
- Select a compartment and then a VCN. The default IP address appears. Edit the default IP address if needed.

Note  
  

Note the following about VCNs and IP addresses.
- IP addresses must be unique within the perimeter. If you add a duplicate IP, you will get an error. You can add the same VCN more than once if each entry has a different IP address.
- Search for added VCNs by name in the Search and filter field. You can only search for added VCNs.
- Remove a single VCN or use bulk delete by selecting multiple VCNs and removing them together.
- IP address or country :
- Enter the exact IP address or IP addresses, IP range, or CIDR block IP address range for the network perimeter. To learn about IP address formats, see[Managing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/overview.htm).
- Select countries from the country list.

Note  
  

Some Internet Protocol (IP) addresses can't be mapped to a country. These addresses are treated as Unknown locations . To include them in a Network Perimeter, add the Unknown locations to the Network Perimeter.
- Enter a comma-separated list of IP addresses or a CIDR block.

- IP range example for IPv4: 10.10.10.1-10.10.10.10. Any address from 10.10.10.1 through 10.10.10.10 is included.
- CIDR block examples for IPv4 and IPv6: 10.11.12.0/24 (all IPv4 addresses starting with 10.11.12 are included), 2001:db8::/32 (IPv6).
- Exclude IPs : Enter the IPs that you want IAM to exclude from the network perimeter. Excluded IP addresses aren't included in the perimeter, even if they're listed in the IP address field.

Note  
  
The Exclude IPs lists apply only to IP addresses and countries, not VCNs.
- Select Create .

Now, create a sign-on policy rule that includes the network perimeter. To learn about using this network perimeter in sign-on policy rules, see[Creating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../signonpolicies/add-sign-policy.htm).

To add a network perimeter to an application, see[Adding a Network Perimeter to an Application](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter-to-an-application.htm).

To configure the your Enterprise or Confidential application by providing client and resource server configurations, see[Configuring OAuth](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/../applications/to-configure-oauth.htm)
