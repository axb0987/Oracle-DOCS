# Viewing Custom Return Path
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm
- Fetched: 2026-09-05 02:01 CDT

# Viewing Custom Return Path

View the details of a custom return path.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm#)
- 

- On the Email Domains list page, select the email domain where you want to view the custom return path status. If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/list-email-domains.htm).
- On the details page, select Custom return path .
- In the Custom return path section, view the added custom return path along with the following information:

- Custom return path: Displays the added custom return path.
- DNS status: Displays whether the DNS records for the added custom return path is active or not.
- Custom return path status: Displays whether the added custom return path is active or not.
- CNAME record: Displays the CNAME record of the custom return path.
- CNAME value: Displays the CNAME value of the custom return path.
- 

Use the[list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/email-return-path/list.html)command and required parameters to list the custom return path.

```

```

Use the[get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/email-return-path/get.html)command and required parameters to view the details of a custom return path.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[GetEmailReturnPath](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailReturnPath/GetEmailReturnPath)operation to view the details of a custom return path.

Use the[ListEmailReturnPath](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailReturnPath/ListEmailReturnPath)
