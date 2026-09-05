# Creating an Email Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains-create-an-email-domain.htm
- Fetched: 2026-09-05 02:00 CDT

# Creating an Email Domain

Create an email domain to set up important authentication measures for sending emails.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains-create-an-email-domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains-create-an-email-domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains-create-an-email-domain.htm#)
- 

- On the Email Domains list page, select Create Email Domain . If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-email-domains.htm).
- In the Create Email Domain dialog box, provide the following information:

- Enter your email domain name.
- The domain must be one that you own or control in DNS, because the measures used to establish verification and authentication require a DNS record.
- The domain must be one that you plan to use for your email address while sending an email. It can't be a public mailbox provider domain, such as`gmail.com`or`hotmail.com`.
- (Optional) To change your compartment, select the one you require. By default, your current compartment is selected.
- (Optional) Add tags to organize your resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- Select Create Email Domain .
- On the Email Domains list page, view the email domain you created.

Note  
  
To register a domain with OCI, see[Managing Your Domains](https://docs.oracle.com/iaas/Content/General/domain/domains.htm).
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/domain/create.html)command and required parameters to create a new email domain.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To create an email domain, use[CreateEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/CreateEmailDomain)operation.

For more information about managing the email domains, see[GetEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/GetEmailDomain),[UpdateEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/UpdateEmailDomain),[ListEmailDomains](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/ListEmailDomains),[DeleteEmailDomain](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/DeleteEmailDomain), and[ChangeEmailDomainCompartment](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/ChangeEmailDomainCompartment)
