# Moving an Email Domain
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains_moving_domain.htm
- Fetched: 2026-09-05 02:00 CDT

# Moving an Email Domain

Move an email domain to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains_moving_domain.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains_moving_domain.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/configureemaildomains_moving_domain.htm#)
- 

- On the Email Domains list page, click the email domain that you want to move. If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/list-email-domains.htm).
- From the Actions menu for the email domain, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
The email domain is moved to a different compartment.
- 

Use the[change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/domain/change-compartment.html)command and required parameters to move an email domain into a different compartment.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To move an email domain to another compartment, use[ChangeEmailDomainCompartment](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailDomain/ChangeEmailDomainCompartment)
