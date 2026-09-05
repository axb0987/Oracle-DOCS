# Configuring HTTPS Connection
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/email-submission-configure-https-connection.htm
- Fetched: 2026-09-05 02:00 CDT

# Configuring HTTPS Connection

Review the HTTPS information to configure the HTTPS connection in your system.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/email-submission-configure-https-connection.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/email-submission-configure-https-connection.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/email-submission-configure-https-connection.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery .
- Under Email Delivery , select Configuration . The HTTPS sending information panel displays the following information:

- Public Endpoint: The public endpoint used to send an email to, for this region.
- HTTPS ports: The HTTPS ports used to accept an email.
- 

Use the[oci email-data-plane email-submitted-response submit-email](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email-data-plane/email-submitted-response/submit-email.html)command and required parameters to send email using HTTPS submission.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[SubmitEmail](https://docs.oracle.com/iaas/api/#/en/emaildeliverysubmission/latest/EmailSubmittedResponse/SubmitEmail)operation to send emails using HTTPS submission.

Use the[SubmitRawEmail](https://docs.oracle.com/iaas/api/#/en/emaildeliverysubmission/latest/EmailRawSubmittedResponse/SubmitRawEmail)
