# Importing Existing DKIM
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-import_dkim_record.htm
- Fetched: 2026-09-05 02:01 CDT

# Importing Existing DKIM

Import existing DKIM keys to OCI and effortlessly migrate your email infrastructure without disruption, ensuring consistent email delivery and authentication. Ensure that the DKIM keys satisfy Oracle Cloud security requirements.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-import_dkim_record.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-import_dkim_record.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Email/Tasks/managing_dkim-import_dkim_record.htm#)
- 

- Open the navigation menu and select Developer Services . Under Application Integration , select Email Delivery . Under Email Delivery , select Email Domains .
- Click the name of the email domain where you want to configure DKIM.
- Select Import an existing DKIM record into OCI and select Next .
(Optional) Add tags to organize your resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask the administrator.
- In the DKIM selector field, enter the DKIM selector name associated with the DKIM key you want to import. The DKIM selector can contain only up to 63 lowercase alphanumeric characters (a-z, 0-9) with dashes.
- In the Add existing DKIM field, select one of the following options:

- Copy paste the private key : Use this option to type or paste the private key.
- Upload PEM file : Use this option to upload the PEM file that contains the private key.
- Select Next .
- Click Generate DKIM Record to generate the DKIM record. The system generates a CNAME record and value that can be used in your DNS setup for your email domain.

Note  
  
For non-commercial realms, add the DKIM Text Record Value to your DNS setup.
- Copy the CNAME and CNAME Record Value and add it to your DNS setup.

Note  
  
To add DNS records, the domain must be registered and available on the public Internet. DNS records must be added using the domain's registered DNS provider, which is the DNS system that the domain's name servers point to.
- Select Add DKIM .

Email Delivery supports a maximum of two DKIM keys per email domain. However, only one DKIM record can be active for a domain at a time. We recommend that you rotate the keys every six months.
- 

Use the[create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/email/dkim/create.html)command and required parameters to import an existing DKIM for an email domain.

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/CreateDkim)operation with`privateKey`parameter to import an existing DKIM record.

For more information about managing DKIMs, see[GetDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/GetDkim),[ListDkims](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/ListDkims), and[UpdateDkim](https://docs.oracle.com/iaas/api/#/en/emaildelivery/latest/Dkim/UpdateDkim)
