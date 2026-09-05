# Setting up Connectivity using a FQDN
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_tls_connectivity_using_fqdn.htm
- Fetched: 2026-09-05 02:35 CDT

# Setting up Connectivity using a FQDN

Learn how to configure TLS connectivity using a fully qualified domain name (FQDN).

To set up TLS connectivity using FQDN, you must create an OCI API Gateway instance and deploy it with the FQDN details.  

  

Overview: Two separate TLS trust chains (two CA bundles)

EKMS connectivity involves two different TLS connections, and each party must be able to validate the other party's server certificate:
- 

OCI KMS (External KMS private endpoint) to OCI API Gateway (ingress)

Purpose: OCI KMS connects to the API Gateway over TLS.

Requirement: OCI KMS must trust the certificate presented by API Gateway.
- 

OCI API Gateway (egress) to third-party KMS (external key manager)

Purpose: API Gateway forwards requests to the external KMS over TLS.

Requirement: API Gateway must trust the certificate presented by the third-party external key manager.

CA bundle best practices

For CA bundle uploads to OCI, the recommended default is to upload or install only the root CA certificate or certificates. This is the most stable approach and typically survives intermediate CA rotations without changes.

The server, such as API Gateway by default or a customer on-premises endpoint, must be configured to present the full chain during TLS. The full chain includes the server or leaf certificate and all required intermediate CA certificates.

Include intermediate CA certificates in the CA bundle only for one of these explicit reasons:
- Reliability: You have a requirement for resilience against on-premises servers that sometimes omit the intermediate certificate.
- Constrained trust: You have a requirement to accept only certificates issued under specific intermediate CAs.

Never include private keys in a CA bundle.

- CA bundle 1: Trust from OCI KMS (External KMS private endpoint) to OCI API Gateway

Description

A trusted CA bundle, consisting of PEM-encoded CA certificate or certificates, that OCI KMS uses to validate the TLS server certificate presented by API Gateway.

Purpose

OCI KMS connects to API Gateway over TLS. During the TLS handshake, OCI KMS must be able to build a valid certificate chain from the API Gateway server certificate to a trusted CA. If OCI KMS can't validate that certificate, the TLS connection fails.

Types and accepted certificate models for API Gateway

The API Gateway server certificate, uploaded to API Gateway along with its private key, can be one of the following types:
- 

Self-signed certificate

Common in controlled or private integrations where you explicitly pin trust.

CA bundle 1 must contain the same self-signed certificate as the trust anchor.
- 

Internal CA-signed certificate (enterprise PKI)

Preferred in many enterprise environments for manageability and rotation.

CA bundle 1 must contain the issuing internal CA chain, including intermediate CA certificates and the root CA as required.

Upload

Because these are two distinct TLS connections, you must upload two different trust bundles, CA bundle 1 and CA bundle 2, in the appropriate OCI services.
- In API Gateway, upload the server certificate and private key to API Gateway Certificates.
This is the certificate that API Gateway presents to OCI KMS.
- In the OCI KMS External KMS private endpoint, upload CA bundle 1 as the trusted CA bundle for the private endpoint.
This is what OCI KMS uses to validate API Gateway.
- CA bundle 2: Trust from OCI API Gateway to the third-party external key manager

Description

A trusted CA bundle, consisting of PEM-encoded CA certificate or certificates, that API Gateway uses to validate the TLS server certificate presented by the third-party KMS upstream endpoint.

Purpose

API Gateway forwards EKMS requests to the external or third-party KMS over TLS. API Gateway must validate the upstream server certificate to prevent man-in-the-middle attacks and to meet enterprise security requirements. If the upstream certificate can't be validated, calls from API Gateway to the third-party KMS fail.

Types and requirements for the third-party KMS certificate

The third-party KMS must present a TLS server certificate that meets the following requirements:
- Issued by a CA whose chain is included in CA bundle 2, such as an internal CA or public CA, depending on your design.
- Contains the FQDN in the Subject Alternative Name (SAN) that matches the hostname used by API Gateway in the upstream URL. The SAN must be a DNS SAN entry.
Important  
  
The SAN (DNS) is required for hostname verification. CN-only certificates may fail validation.

Upload
- Upload CA bundle 2 to Certificates &gt; CA Bundles in OCI.
-
