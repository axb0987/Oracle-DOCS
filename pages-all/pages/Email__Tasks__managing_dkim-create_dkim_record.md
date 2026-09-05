# Creating a DKIM Record
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-create_dkim_record.htm
- Fetched: 2026-09-05 02:01 CDT

# Creating a DKIM Record

Create a new DKIM resource and add the DKIM record to your DNS records.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-create_dkim_record.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-create_dkim_record.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-create_dkim_record.htm#)
- 

- On the Email Domains list page, select the email domain where you want to configure DKIM. If you need help finding the list page, see[Listing Email Domains](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/../Reference/list-email-domains.htm).
- On the details page, select DKIM .
- In the DKIM section, select Add DKIM .
- Select Add new DKIM and select Next .
(Optional) Add tags to organize your resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- In the DKIM selector field:

- Enter the prefix to be used in generating the DKIM selector for this particular DKIM key. Replacement keys each have their own unique selector and include a date component to easily identify when the key is rotated. The DKIM selector can contain only up to 63 lowercase alphanumeric characters (a-z, 0-9) with dashes.
- Select Next .
- Select Generate DKIM Record to generate the DKIM record. The system generates a CNAME record and value that can be used in your DNS setup for your email domain.

Note  
  
For non-commercial realms, add the DKIM Text Record Value to your DNS setup.
- Copy the CNAME and CNAME Record Value and add it to your DNS setup.

Note  
  
To add DNS records, the domain must be registered and available on the public Internet. DNS records must be added using the domain's registered DNS provider, which is the DNS system that the domain's name servers point to.
- Select Add DKIM .

Email Delivery supports a maximum of two DKIM keys per email domain. However, only one DKIM record can be active for your domain at a time. We recommend that you rotate your keys every six months.
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/dkim/create.html)command and required parameters to create a new DKIM for an email domain.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/CreateDkim)operation to create a DKIM record.

For more information about managing DKIMs, see[GetDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/GetDkim),[ListDkims](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/ListDkims), and[UpdateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/UpdateDkim)
