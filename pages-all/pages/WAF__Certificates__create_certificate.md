# Creating a Web Application Firewall Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/create_certificate.htm
- Fetched: 2026-09-05 03:10 CDT

# Creating a Web Application Firewall Certificate

Describes how to create a web application firewall policy certificate.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/create_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/create_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Certificates/create_certificate.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.

The WAF Certificates page appears.
- Select Certificate under Resources .

All the certificates in that compartment are listed in tabular form.
- Select Create certificate .

The Create certificate dialog box appears.
- Complete the following:

- Name : Enter the name for the certificate.
- 

SSL certificate : Drag and drop, select, or paste a valid SSL certificate in PEM format. Also include intermediate certificates (the website certificate must be first). The following is an example:
```

```

- 

Private key : Drag and drop, select, or paste a valid private key in PEM format in this field. The passphrase can't protect the private key. The following is an example:
```

```

- Self signed certificate : Check this box when using a self-signed certificate to show an SSL warning in the browser.
- Show advanced options : Select this link to display options for tagging. See[Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
- 
Select one of the following:
- To create the certificate, select Create .
- To create the certificate later using Resource Manager see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm)
- 

Enter the following command and required parameters:

```

```

See the CLI online help for a list of optional parameters:

```

```

See[oci waas certificate create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/certificate/create.html)for a complete description of the command.
- 

Run the[CreateCertificate](https://docs.oracle.com/iaas/api/#/en/waas/latest/Certificate/CreateCertificate)
