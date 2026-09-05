# Certificates Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-certificates.htm
- Fetched: 2026-09-05 02:59 CDT

# Certificates Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the Certificates service for a Roving Edge Infrastructure device.

## Resource-Types

`leaf-certificates`

`leaf-certificates-csr`

`leaf-certificate-family`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### leaf-certificates

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

CERTIFICATE_READ

ViewCertificate

ViewCertificateWorkRequest

None

read

CERTIFICATE_READ

ViewCertificate

ViewCertificateWorkRequest

None

manage

CERTIFICATE_READ

CERTIFICATE_RENEW

CERTIFICATE_IMPORT

CERTIFICATE_CREATE

ViewCertificate

ViewCertificateWorkRequest

RenewCertificate

ImportCertificate

CreateCertificate

None

### leaf-certificates-csr

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

CSR_READ

ViewCertificateSigningRequest

None

read

CSR_READ

ViewCertificateSigningRequest

None

manage

CSR_READ

CSR_CREATE

ViewCertificateSigningRequest

CreateCertificateSigningRequest

None

### leaf-certificate-family

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

CERTIFICATE_READ

CSR_READ

ViewCertificate

ViewCertificate

WorkRequest

ViewCertificate

SigningRequest

None

read

CERTIFICATE_READ

CSR_READ

ViewCertificate

ViewCertificate

WorkRequest

ViewCertificate

SigningRequest

None

manage

CERTIFICATE_READ

CERTIFICATE_RENEW

CERTIFICATE_IMPORT

CERTIFICATE_CREATE

CSR_READ

CSR_CREATE

ViewCertificate

ViewCertificateWorkRequest

RenewCertificate

ImportCertificate

CreateCertificate

ViewCertificateSigningRequest

CreateCertificateSigningRequest
