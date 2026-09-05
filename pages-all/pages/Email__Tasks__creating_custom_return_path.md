# Creating Custom Return Path
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm
- Fetched: 2026-09-05 02:01 CDT

# Creating Custom Return Path

Create a custom return path to improve your inbox placement and monitor email bounces when bulk emails are sent.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/creating_custom_return_path.htm#)
- 

- On the Email Domains list page, select the email domain where you want to configure custom return path. If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/list-email-domains.htm).
- On the details page, select Custom Return Path .
- Select Add custom return path .
- On the Add custom return path panel, enter the subdomain to be used as custom return path domain in the Custom return path field.
- In the Description field, provide a description for the custom return path domain.
- Select Generate CNAME Record to generate the CNAME record and value. The system generates a CNAME record and value that can be used in your DNS setup for your email domain.
- Copy the CNAME record and CNAME value and add it to the DNS zone of your email sending domain.
- Select Add custom return path .

Note  
  

Email Delivery supports one active custom return path per email domain.

To view the custom return path domain's status, navigate to the details page of the email domain. See[Viewing Custom Return Path](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/viewing_custom_return_path.htm).
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/email-return-path/create.html)command and required parameters to create a new email return path.

```

```

Use the[update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/email-return-path/update.html)command and required parameters to update an email return path.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateEmailReturnPath](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/EmailReturnPath/CreateEmailReturnPath)
