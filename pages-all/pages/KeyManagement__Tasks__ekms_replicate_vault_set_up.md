# Setting up IDCS Domains
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault_set_up.htm
- Fetched: 2026-09-05 02:35 CDT

# Setting up IDCS Domains

Configure Identity Cloud Service (IDCS) domains in both source and destination regions to enable cross-regional replication for External KMS vaults. OCI.

## Prerequisites
Before you begin, ensure that you have:
- An existing OCI tenancy with active subscriptions to both source and destination regions.
- A basic understanding of IDCS and OAuth 2.0 concepts.

## Setting Up IDCS in the Source Region

- Create an IDCS domain in the source region. See[Creating an Identity Domain](https://docs.oracle.com/iaas/Content/Identity/domains/to-create-new-identity-domain.htm).
Note  
  
By default, an IDCS domain is created in the tenancy subscribed home region. In this case, the domain must be explicitly created in the source region by selecting the same from the region selector in the OCI Console
- Create the following applications in the source region:
- [Confidential Resource Server Application](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms_creating_confidential_resource_app.htm): To represent your external key manager hosted outside of OCI.
- [Confidential Client Application](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/ekms_creating_associate_client_app.htm): To represent your external vault in OCI.
External KMS supports both IP and FQDN based connectivity model to your external key manager.
- IP-based connectivity: Uses the IP address of your external key manager.
- FQDN-based connectivity: Uses the IP address of your OCI API Gateway.
- For IP based connectivity,[Replicate the IDCS domain](https://docs.oracle.com/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)in the source region to the destination region.
- For FQDN based connectivity, create a new OCI API Gateway in the destination region.
- [Replicate the IDCS domain](https://docs.oracle.com/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)in source region to destination region.
- Create a new Confidential Resource Server Application in the destination region which is same as the Confidential Resource Server Application in the source region but with the Primary audience as the destination region OCI API Gateway IP address https://destination_region_apigw_ip_address
- Associate this new application's scope in the original replicated Confidential Client Application .
Note
