# Editing a Web Application Firewall Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/update_certificate.htm
- Fetched: 2026-09-05 03:10 CDT

# Editing a Web Application Firewall Certificate

Describes how to edit a certificate for a web application firewall policy.

Note  
  

You can only edit the name of a certificate.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/update_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/update_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/update_certificate.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

The WAF Certificates page appears.
- Select Certificate under Resources .

All the certificates in that compartment are listed in tabular form.
- Select the certificate you want to edit.

The WAF Certificate Details dialog box appears.
- Select Edit .
Alternatively, select the Actions menu (three dots) for the certificate and select Edit .
The Edit WAF Certificate dialog box appears.
- Update the Name of the certificate.
- Select Save Changes .

The Edit WAF Certificate dialog box closes. The updated name of the certificate appears in the Details page and the list of WAF certificates.
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

See[oci waas certificate update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/certificate/update.html)for a complete description of the command.
- 

Run the[UpdateCertificate](https://docs.oracle.com/iaas/api/#/en/waas/latest/Certificate/UpdateCertificate)
