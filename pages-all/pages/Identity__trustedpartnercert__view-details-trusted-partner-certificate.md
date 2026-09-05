# Viewing Details About a Trusted Partner Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/view-details-trusted-partner-certificate.htm
- Fetched: 2026-09-05 02:29 CDT

# Viewing Details About a Trusted Partner Certificate

View details of a trusted partner certificate for an identity domain in IAM.
You can see the alias, SHA-1 and SHA-256 thumbprints, start date, and end date for each certificate that you import into the identity domain. You can see either the abbreviated version of a certificate (the thumbprint ) or the entire certificate.

- On the Trusted Partner Certificates list page, verify that you see the following information about the imported trusted partner certificate. If you need help finding the list page, see[Listing Trusted Partner Certificates](https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/list-trusted-partner-certificate.htm).

- Alias : The alias for the trusted partner certificate.
- SHA-1 thumbprint : A hash value computed over the complete certificate, which contains all its fields, including the signature. If SHA-1 is used as the algorithm to encrypt the certificate, then the encrypted value appears in this column. Otherwise, the column is empty.
- SHA-256 thumbprint : If SHA-256 is used as the algorithm to encrypt the certificate, then the encrypted value appears in this column. Otherwise, the column is empty.
- Certificate start date : The date and time after which the identity domain can use the certificate to authenticate the trusted partner.
- Certificate end date : The date and time after which the identity domain can no longer use the certificate to authenticate the trusted partner.
-
