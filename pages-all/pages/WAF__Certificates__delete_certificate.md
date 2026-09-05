# Deleting a Web Application Firewall Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/delete_certificate.htm
- Fetched: 2026-09-05 03:10 CDT

# Deleting a Web Application Firewall Certificate

Describes how to delete a certificate from a web application firewall policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/delete_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/delete_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/delete_certificate.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
- Select Certificate under Resources .

All the certificates in that compartment are listed in tabular form.
- Select the certificate you want to delete.

The WAF Certificate Details dialog box appears.
- Select Delete .
Alternatively, select the Actions menu (three dots) for the certificate and select Delete .
- Confirm the deletion when prompted.

The list of certificates reappears without the certificate you deleted.
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

See[oci waas certificate delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/certificate/delete.html)for a complete description of the command.
- 

Run the[DeleteCertificate](https://docs.oracle.com/iaas/api/#/en/waas/latest/Certificate/DeleteCertificate)
