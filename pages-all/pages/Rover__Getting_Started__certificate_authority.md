# Establishing the Certificate Authority for Roving Edge Infrastructure Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/certificate_authority.htm
- Fetched: 2026-09-05 02:59 CDT

# Establishing the Certificate Authority for Roving Edge Infrastructure Devices

Learn how certificate authorities are used with Roving Edge Infrastructure device certificates in Oracle Cloud Infrastructure (OCI).

Sign any certificates used by Roving Edge Infrastructure devices with RSA keys. All certificates in the chain (for example, root, subordinate and leaf certificates) should use SHA family signing algorithms and RSA family signing keys. Roving Edge Infrastructure doesn't support other signing keys such as ECDSA.

You can optionally use the OCI Certificate service. See[Managing Certificate Authorities](https://docs.oracle.com/iaas/Content/certificates/managing-certificate-authorities.htm)for information on establishing the certificate authority to use with Roving Edge Infrastructure when creating your device node certificates.

After you receive your device, you can manage device certificates. See[Certificate Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/../certificate-management.htm#certificate-management)
