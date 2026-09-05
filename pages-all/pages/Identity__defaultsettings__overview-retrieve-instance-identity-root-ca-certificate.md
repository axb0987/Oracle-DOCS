# Retrieving the Instance Identity Root CA Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/overview-retrieve-instance-identity-root-ca-certificate.htm
- Fetched: 2026-09-05 02:20 CDT

# Retrieving the Instance Identity Root CA Certificate

Oracle Cloud Infrastructure (OCI) issues each compute instance a unique x.509 identity certificate. This certificate is signed by an Oracle-operated Certificate Authority (CA). You can verify that an instance certificate was issued by Oracle by checking its signature against the Oracle Instance Identity Root CA certificate.

## Retrieving the Instance Identity Root CA Certificate

- Determine the OCI region for your instance.
- Retrieve the root CA certificates for that region by calling:`https://auth.{region}.oraclecloud.com/v1/instancePrincipalRootCACertificates`

Note  
  

Replace`{region}`with your specific OCI region.

This endpoint is authenticated. You must sign the request using the OCI standard API request signing process. See[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm)in the Oracle documentation.

Below is a sample using the OCI CLI. The API call requires the caller to be an authenticated principal in the region.

`Oci raw-request –http-method GET –target-uri ‘https://auth.us-phoenix-1.oraclecloud.com/v1/instancePrincipalRootCACertificates’`

The endpoint returns PEM-encoded x.509 root certificates. Any intermediates used to complete the instance certificate chain must be retrieved from the instance itself.

## Getting the Intermediate Certificate

OCI instances expose the intermediate certificate over the instance metadata endpoint:`curl -sSL http://169.254.169.254/opc/v2/identity/intermediate.pem`

## Verifying an Instance Certificate

- Obtain the instance public certificate:`curl -sSL http://169.254.169.254/opc/v2/identity/cert.pem -o cert.pem`
- Download the instance’s intermediate certificate:`curl -sSL http://169.254.169.254/opc/v2/identity/intermediate.pem -o intermediate.pem`
- Use a signed request or the OCI CLI above to download the root CA (save as`root.pem`).
- 4. Verify the full certificate chain with OpenSSL: Use any standard x.509 tool (like OpenSSL) to verify the instance certificate’s signature chain against the Oracle root CA:`openssl verify -CAfile root.pem -untrusted intermediate.pem cert.pem`
Where:
- `cert.pem`is the certificate from the instance metadata endpoint.
- `root.pem`and`intermediate.pem`are the files you downloaded from the Oracle Identity API.
