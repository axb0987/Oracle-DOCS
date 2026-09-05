# Adding an Email Address to the Suppression List
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-add_an_email_address_to_the_suppression_list.htm
- Fetched: 2026-09-05 02:01 CDT

# Adding an Email Address to the Suppression List

Add an email address to the suppression list so that it isn't a part of your sending list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-add_an_email_address_to_the_suppression_list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-add_an_email_address_to_the_suppression_list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-add_an_email_address_to_the_suppression_list.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Suppression List .
- Select Add Suppression .
- In the Add Suppression dialog box, enter the email address to be listed in the suppression list.
- Select Add .
The email address is added to the suppression list.
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/suppression/create.html)command and required parameters to add recipient email addresses to the suppression list for a tenancy.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To add an email address to the suppression list, use the[CreateSuppression](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/CreateSuppression)operation.

The following example shows how to add an email address to the suppression list. For more information about managing the suppressions list, see[GetSuppression](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/GetSuppression)and[DeleteSuppression](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/DeleteSuppression).
```

```
