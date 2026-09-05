# Viewing SAML Certificate Metadata
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-access-signing-certificate.htm
- Fetched: 2026-09-05 02:20 CDT

# Viewing SAML Certificate Metadata

Allow clients to access the signing certificate for the identity domain in IAM without logging in to an identity domain.

- On the Domain settings page, find the setting you want to change. If you need help finding the domain settings page, see[Listing Domain Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/list-domain-settings.htm).
- Under Access signing certificate , select Configure client access to enable clients to access the tenant signing certificate without signing in to IAM.
If this option is cleared, clients can access the tenant signing certificate and the SAML metadata only after they authenticate by signing in to the identity domain.
- Select Save changes .
- In the overview page for the identity domain overview, select Copy next to the Domain URL in Domain information.
- In a new browser tab, paste the URL you copied and add`/fed/v1/metadata`to the end of it, and then press Enter . For example:

```

```
