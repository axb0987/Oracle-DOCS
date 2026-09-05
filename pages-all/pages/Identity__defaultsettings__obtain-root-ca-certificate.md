# Getting the Root CA Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/obtain-root-ca-certificate.htm
- Fetched: 2026-09-05 02:20 CDT

# Getting the Root CA Certificate

When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.
cURL must be installed to perform this task. See
Follow this procedure to obtain the root certificate.

- On the Domain settings page, find the setting you want to change. If you need help finding the domain settings page, see[Listing Domain Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/list-domain-settings.htm).
- Under Access signing certificate , select Configure client access to enable clients to access the tenant signing certificate without logging in to IAM.
- Select Save changes and confirm the action to save the default settings.
- In the overview page for the identity domain overview, select Copy next to the Domain URL in Domain information.
- In a new browser tab, paste the URL you copied and add`/admin/v1/SigningCert/jwk`to the end of it. For example:

```

```

- Use the following URL as the endpoint and press Enter .
`https:// <yourtenancy> .identity.oraclecloud.com/admin/v1/SigningCert/jwk`
When you Enter , a block of code is returned.

[

The section of code you want for the key is the block marked with`1:`on the left, and immediately above`key_ops`.
- Open a text editor and paste the key in the following manner:
`-----BEGIN CERTIFICATE----- [Paste the key here] -----END CERTIFICATE-----`

For example, (abbreviated):

`-----BEGIN CERTIFICATE----- "MIIDdDCCAlygAwIBAgIGAVw4Ns68MA0GCS......./VaWgoMQ6J9t9CLarai" -----END CERTIFICATE-----`
- Save this file with the suffix`.pem`
