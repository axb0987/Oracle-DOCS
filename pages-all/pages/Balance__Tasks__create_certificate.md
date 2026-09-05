# Adding a Load Balancer Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_certificate.htm
- Fetched: 2026-09-05 01:40 CDT

# Adding a Load Balancer Certificate

Add an SSL certificate to a load balancer.

For prerequisite information, see[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_certificate.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Load balancer certificates section.
The Load balancer managed certificates list opens. All Load Balancer service-managed certificates in the selected load balancer are displayed in a table.
- Select Add certificate .
- Enter the following information:

- Certificate name : Enter a friendly name for the certificate bundle. It must be unique within the load balancer, and it can't be changed in the Console. (It can be changed using the API.)
- Choose SSL Certificate file : Drag the certificate file, in PEM format, into the SSL certificate field.

You can also select the Paste SSL certificate option to paste a certificate directly into this field.
Important  
  
If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
- Specify CA certificate : (Recommended for backend SSL termination configurations.) Select to provide a CA certificate.
- Choose CA certificate file : Drag the CA certificate file, in PEM format, into the CA certificate field.

You can also select the Paste CA certificate option to paste a certificate directly into this field.
- Specify private key : (Required for SSL termination.) Select to provide a private key for the certificate.
- Choose private key file : Drag the private key, in PEM format, into the Private key field.

You can also select the Paste private key option to paste a private key directly into this field.
- Enter private key passphrase : Enter the private key passphrase.
- Select Add certificate .
- 

Use the[oci lb certificate create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/create.html)command and required parameters to add a certificate to a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateCertificate](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/CreateCertificate)
