# Setting up Private DNS Resolver
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/external_kms_fqdn_setting_up_dns_resolver.htm
- Fetched: 2026-09-05 02:35 CDT

# Setting up Private DNS Resolver

Configure private DNS resolver to resolve FQDN queries.

A private DNS resolver provides responses to DNS queries from an on-premises environment and vise versa. It provides responses by checking each customer-referenced view in order, default view, each rule in order, and then finally by using internet DNS.
As part of FQDN based TLS connectivity configuration, you can optionally set up the private DNS resolver in your VCN to resolve FQDN queries to the private network.
Note  
  
If you own a public cloud, then this set up is not required for internet based DNS resolution. For more details to set up a private DNS resolver, see[OCI Private DNS](https://www.ateam-oracle.com/post/oci-private-dns---common-scenarios)
