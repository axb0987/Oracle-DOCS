# Enabling Multiple IDCS Endpoints in Thales HMS
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_replicate_vault-thales-vendor-api.htm
- Fetched: 2026-09-05 02:35 CDT

# Enabling Multiple IDCS Endpoints in Thales HMS

Add more than one IDCS endpoints in the Thales HSM system using API approach.

This API-centric approach offers a programmatic way to manage and configure identity providers, ensuring a scalable and automated process. For more information, see[Create Issuer API Documentation](https://thalesdocs.com/ctp/cm/latest/reference/cckmapi/ora-ext-apis/ora-ext-issuers-apis/ora-create-issuer/index.html).

## Prerequisites

Before you begin, understand the following prerequisites:
- IDCS Domain Replication: Replicate IDCS Domain in Oracle Cloud Infrastructure (OCI). This replication ensures that the primary and secondary IDCS domains are synchronized, providing redundancy and high availability.
- Consistent URLs: Both the primary and secondary IDCS domain URLs need to be configured with the same values in the Thales system. This consistency is vital for seamless operation and ensures that Thales HMS can communicate with the correct IDCS endpoints.

## Implementing the API Integration

To add multiple IDCS endpoints, follow the steps outlined in the API documentation:
- Endpoint Creation: Use the provided API endpoint to create a new issuer (IDCS endpoint) in the Thales system. This process involves sending a POST request with the necessary configuration details, including the IDCS domain URL.
- Authentication Configuration: The API allows for setting up authentication details, such as client ID and secret, to ensure secure communication between Thales HMS and the IDCS domain.
-
