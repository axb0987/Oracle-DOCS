# Moving a Web Application Firewall Certificate Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/change-compartment_certificate.htm
- Fetched: 2026-09-05 03:10 CDT

# Moving a Web Application Firewall Certificate Between Compartments

Describes how to move a certificate between compartments for a web application firewall policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/change-compartment_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/change-compartment_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/change-compartment_certificate.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

The WAF Certificates page appears.
- Select Certificate under Resources .

All the certificates in that compartment are listed in tabular form.
- Select the certificate you want to move.

The WAF Certificate Details dialog box appears.
- Select Move Resource .
Alternatively, select the Actions menu (three dots) for the certificate and select Move .

The Move Resource to a Different Compartment dialog box appears.
- Select the compartment to which you want to move your certificate from the Choose New Compartment list.
- Select Move Resource .

The certificate now appears in the compartment you moved it to.
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

See[oci waas certificate change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/certificate/change-compartment.html)for a complete description of the command.
- 

Run the[ChangeCertificateCompartment](https://docs.oracle.com/iaas/api/#/en/waas/latest/Certificate/ChangeCertificateCompartment)
