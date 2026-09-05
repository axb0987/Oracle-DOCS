# Deleting an Email Address from Suppression List
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm
- Fetched: 2026-09-05 02:01 CDT

# Deleting an Email Address from Suppression List

Delete an email address from the suppression list.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/managingsuppressionlist_topic-delete_an_email_address_from_the_suppression_list.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Suppression List .
- From Actions menu for the suppressed email address, select Delete .
- When prompted, confirm the deletion.
The email address is removed from the suppression list.

Tip  
  
Use the search field to search for an email address.
- 

Use the[delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/suppression/delete.html)command and required parameters to remove a suppressed recipient email address from the suppression list.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To delete an email address from the suppression list, use the following operations:
- [GetSuppression](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/GetSuppression)
- [ListSuppressions](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/ListSuppressions)
- [DeleteSuppression](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Suppression/DeleteSuppression)
