# Access to Oracle Services: Private Service Access Endpoints
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/private-service-access.htm
- Fetched: 2026-09-05 02:42 CDT

# Access to Oracle Services: Private Service Access Endpoints

This topic describes using Private Service Access (PSA) endpoints to give cloud resources without public IP addresses private access to Oracle Cloud Infrastructure services.

## About PSA Endpoints

You can use Oracle Cloud Infrastructure Private Service Access to create Private Service Access (PSA) endpoints that provide private IP access to a single OCI service. The PSA endpoint uses a dedicated private IP address and FQDN in a specified VCN and subnet. A PSA endpoint is available in IPv4-only or dual stack IPv4-IPv6 networks.

You set up the PSA endpoint in a subnet within the VCN. You can think of the PSA endpoint as another VNIC in the VCN. You can control access to it how you would for any other VNIC: by using[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)in a security list, an NSG, or using Zero-trust Packet Routing (ZPR) security attributes and policies that you define and implement.

The following diagram illustrates the concept.
[

The PSA endpoint gives hosts within a VCN or an on-premises network access to the Oracle service of interest (for example, Autonomous AI Database Serverless). The private access model is similar to a service gateway: If you created five Autonomous AI Databases for a specific VCN, all five would be accessible through a single PSA endpoint by sending requests to the PSA endpoint for the service. With the private endpoint model, there would be five separate private endpoints: one for each Autonomous AI Database, and each with its own private IP address.
Note  
  
When you set up the PSA endpoint in the VCN, a DNS name (fully qualified domain name, or FQDN) is assigned to the PSA endpoint, or the private IP address itself. If you configured the network setup for DNS, hosts can access the PSA endpoint using the FQDN. If the service supports the use of[network security groups (NSGs)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm)with its resources, you can request that the service set up the private endpoint in an NSG within the VCN. NSGs let you write[security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)to control access to the private endpoint without knowing the private IP address assigned to the private endpoint. A[ZPR security attribute](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)that has associated policies that mention the PSA endpoint can also be used to control access.

To enable on-premises hosts to use the private endpoint's FQDN instead of its private IP address, you have two options:
- Set up a DNS listening endpoint. For an example of an implementation of this scenario with the Oracle Terraform provider, see[Hybrid DNS Configuration](https://github.com/oracle/terraform-provider-oci/blob/255817f83956f1f9a3ab903e11465e8b4dde1957/docs/examples/networking/hybrid_dns/Hybrid-DNS-configuration-using-DNS-VM-in-VCN.md).
- Manage hostname resolution yourself manually.

You might have several VCNs with hosts that need access to the specific resource of interest. You can[peer the VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/VCNpeering.htm)so that hosts in the other VCNs can also use the private endpoint (the preceding diagram doesn't show any peered VCNs).

## Service Specific ConsiderationsObject Storage
- The PSA endpoint for Object Storage blocks cross-tenancy preauthenticated requests, foreign credentials, and anonymous access to Object Storage.
- The PSA endpoint for Object Storage provides throughput up to 25 Gbps. When to use a PSA endpoint for Object Storage instead of a private endpoint PSA is recommended for most Object Storage use cases as it creates seamless, region-wide private access without code changes or reliance on public endpoints, and includes enhanced security features (for example, blocks cross-tenancy credentials/preauthenticated requests, offers traffic metrics, and zero trust attributes). Private Endpoints are best when you need to restrict access to specific namespaces, compartments, or buckets for certain clients—ideal for fine-grained control and scenarios needing dedicated FQDNs. Service Gateway remains an option when requiring higher bandwidth or when you want easy, broad access to all OCI services, albeit with less granularity and security controls.

## PSA Endpoint Management

The following basic management actions are available for PSA endpoints:
- [Listing PSA Endpoints](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-list.htm)
- [Creating a PSA Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-create.htm)
- [Getting PSA Endpoint Details](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-get_details.htm)
- [Editing a PSA Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-edit.htm)
- [Moving a PSA Endpoint to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-move.htm)
- [Deleting a PSA Endpoint](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/psa-delete.htm)
