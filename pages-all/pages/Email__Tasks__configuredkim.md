# Managing DKIM
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/configuredkim.htm
- Fetched: 2026-09-05 02:01 CDT

# Managing DKIM

Manage email domains with Domain Keys Identified Mail (DKIM).

DKIM is an authentication framework that allows verification of the source and contents of messages by Mail Transfer Agents (MTAs). With DKIM, a signer can cryptographically sign an email message for a domain, claiming responsibility for its authenticity. The recipient verifies the signature by querying the signing domain for the public key to confirm that the signature was created with the matching private key.

DKIM-Signature is an email header field that contains all the signature and key-fetching data. This header value contains tags with specific details about the email message, such as the signing domain where the verifier can find the public key ("d") and the specific header fields as of signing ("h"). These tags protect the integrity of the email message, proving that it's from a legitimate source and that the signed contents haven't been tampered with. Thus, DKIM can protect a domain from being spoofed for the proliferation of spam or in a phishing attempt.
The following is an example of a DKIM-Signature:
```

```

One DKIM key can be active for your email domain at a time. You can[set up DKIM keys in the Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-setup_email_domain_with_dkim.htm)and denote one record to be the active DKIM key to sign your emails with.
For more information about DKIM, see:
- [DKIM.org](https://dkim.org/)
- [RFC 6376 – DomainKeys Identified Mail Signatures](https://datatracker.ietf.org/)

## Using the API
For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Note  
  
This procedure doesn't apply to OCI Classic services such as Fusion Apps, Cloud Notification Services, and classic IDCS. As these services don't use OCI Email Delivery, DKIM support for these services requires opening a support ticket to the service that generates the email. Note that if you set up a DKIM key for an OCI Classic service and a DKIM key for OCI Email Delivery in the same email domain, each of these keys must have a different selector. When opening a support ticket, mention the service that's generating the email so the support team can route your ticket correctly.
Note  
  

This procedure also doesn't apply to Oracle Integration Cloud Generation 2 (OIC) or Oracle Transportation and Global Trade Management (OTMGTM) services. Each of these services requires its own service-specific DKIM key that must have a different selector from other DKIM keys in your email domain. For the procedure for OIC, see[Configure Email Authentication Settings for SPF and DKIM](https://docs.oracle.com/en/cloud/paas/integration-cloud/oracle-integration-oci/configure-email-authentication-settings-spf-and-dkim.html). For the procedure for OTMGTM, see[Configure DKIM](https://docs.oracle.com/en/cloud/saas/transportation/24a/otmol/configuration/configure_dkim.htm?rhhlterm=otmgtm).

When opening a support ticket, mention the specific service (OIC or OTMGTM) so the support team can route your ticket correctly.

Use the following operations to manage email domains:
- [CreateEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/CreateEmailDomain)
- [GetEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/GetEmailDomain)
- [ListEmailDomains](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/ListEmailDomains)
- [UpdateEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/UpdateEmailDomain)
- [DeleteEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/DeleteEmailDomain)
- [ChangeEmailDomainCompartment](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/ChangeEmailDomainCompartment)
- [CreateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/CreateDkim)
- [GetDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/GetDkim)
- [ListDkims](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/ListDkims)
- [UpdateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/UpdateDkim)
- [DeleteDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/DeleteDkim)
