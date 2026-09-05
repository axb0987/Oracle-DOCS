# Deleting a DKIM Record
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-delete_dkim_record.htm
- Fetched: 2026-09-05 02:01 CDT

# Deleting a DKIM Record

Delete a DKIM record.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-delete_dkim_record.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-delete_dkim_record.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-delete_dkim_record.htm#)
- 

- On the Email Domains list page, select the email domain where you want to delete a DKIM record. If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/list-email-domains.htm).
- On the details page, select DKIM .
- From Actions menu for the DKIM, select Delete .
- When prompted, confirm the deletion.
The DKIM record is deleted from the email domain.
- 

Use the[delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/dkim/delete.html)command and required parameters to delete a DKIM.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[DeleteDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/DeleteDkim)operation to delete a DKIM record.

For more information about managing DKIMs, see[GetDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/GetDkim),[ListDkims](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/ListDkims), and[UpdateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/UpdateDkim)
