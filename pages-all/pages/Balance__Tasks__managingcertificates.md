# Load Balancer- Managed SSL Certificates
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm
- Fetched: 2026-09-05 01:41 CDT

# Load Balancer- Managed SSL Certificates

Use secure socket layer (SSL) certificates with your load balancer through the Load Balancer service.
Note  
  
This topic describes how to create and manage SSL certificates within the Load Balancer service. We recommend you use the Certificates service for creating and managing certificates. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information.

You can view those Certificate service-managed certificates used by a load balancer through the Console. See[Listing Certificates Service-Managed Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm#listing-service-managed-certificates)for more information.

To use standard SSL with a load balancer and its resources, you must supply a certificate.

To use mutual TLS (mTLS) with your load balancer, you must add one or more certificate authorities (CA) or certificate authority bundles (CA bundles) to your system.
- Certificate Authority : A private certificate authority capable of issuing leaf certificates. For a load balancer and its associated resources, the CA is a trust store created inside certificates service and isn't user uploaded.
- CA Bundle : A collection of CA public certificates that you can upload as an aggregated group. CA bundles don't include private key or leaf certificates.
Tip  
  
We recommend you upload the certificate bundles you want to use before you create the listeners or backend sets you want to associate them with.

You can perform the following SSL certificate tasks:

[Configure SSL handling for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm#configuringSSLhandling)

[List the certaificates for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm)

[Create a new certificate for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/create_certificate.htm)

[Get a certificate's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/get_certificate.htm)

[Update a expiring certificate.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_certificate.htm)

[Delete a certificate from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm)

Load balancers commonly use single domain certificates. However, load balancers with listeners that include request routing configuration (see[Request Routing](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrequest.htm)) might require a subject alternative name (SAN) certificate (also called multi-domain certificate) or a wildcard certificate. The Load Balancer service supports each of these certificate types.
Note  
  

- The Load Balancer service doesn't generate SSL certificates. It can only import an existing certificate that you already own. The certificate can be one issued by a vendor, such as Verisign or GoDaddy. You can also use a self-signed certificate that you generate with an open source tool, such as[OpenSSL](https://openssl.org/)or[Let's Encrypt](https://letsencrypt.org/). See the corresponding tool's documentation for instructions on how to generate a self-signed certificate.
- If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.

Oracle Cloud Infrastructure accepts x.509 type certificates in PEM format only. The following is an example PEM encoded certificate:
```

```

## Converting to PEM Format

If you receive your certificates and keys in formats other than PEM, you must convert them before you can upload them to the system. You can use OpenSSL to convert certificates and keys to PEM format. The following example commands provide guidance.

## Certificate or Certificate Chain from DER to PEM

```

```

## Private Key from DER to PEM

```

```

## Certificate Bundle from PKCS#12 (PFX) to PEM

```

```

## Certificate bundle from PKCS#7 to PEM

```

```

## Configuring Peer Certificate Verification

Peer certificate verification is used for client authentication. Peer certificate verification depth is the number of certificates in the chain that need to be verified for client authentication.

The following are expected values to be set:
- One intermediate certificate, client certificate, root certificate - 2
- Client certificate, root certificate - 1s

To decide if your peer certificate verification is configured incorrectly, note the following:
- The client indicates that it's unable to verify the certificate and results in a client SSL handshake failure. This error message varies based on the client type.
- In the load balancer logs, the following error appears:`Client %s has SSL certificate verify error`
- Use the OpenSSL utility to run the following command:`openssl verify -verbose -CAfile RootCert.pem Intermediate.pem`

An error occurs that shows at what depth the validation failure is occurring:`error 20 at 0 depth lookup:unable to get local issuer certificate`

To resolve this situation, provide the correct certificate depth and confirm that the client certificate and certificate authority certificate match and are in the correct order.

## Uploading Certificate Chains

If you have multiple certificates that form a single certification chain (for example, any intermediate certificate authority certificates), then include all relevant certificates in one file in the correct order before you upload them to the system. The correct order begins with the certificate directly signed by the trusted root certificate authority at the bottom of the list. Any additional certificates are pasted above the signed certificate.

Combine the server certificate (`SSL_Certificate.crt`) and the intermediate certificate authority certificate (`intermediateCA.crt`) files into a single, concatenated file.

To get a single, concatenated file from the SSL certificate and the intermediate certificate authority certificate, open a command prompt and run the following command:

```

```

The following example of a concatenated certificate chain file includes four certificates:
```

```

## Submitting Private Keys

Note  
  
We recommend a minimum length of 2048 bits for your RSA private key.

If your private key submission returns an error, the three most common reasons are:
- 

You provided an incorrect passphrase.
- 

Your private key is malformed.
- 

The system doesn't recognize the encryption method used for your key.

## Key Pair Mismatch

If you receive an error related to the private key and public key being mismatched, then before uploading, use the following OpenSSL commands to confirm that they're part of the same pair:

```

```

Confirm that the returned`sha1`hash values match exactly. If they're different, then the private key provided isn't used to sign the public certificate and can't be used.

## Private Key Consistency

If you receive an error related to the private key, then you can use OpenSSL to check its consistency:

```

```

This command verifies that the key is intact, the passphrase is correct, and the file contains a valid RSA private key.

## Decrypting a Private Key

If the system doesn't recognize the encryption technology used for your private key, decrypt the key. Upload the unencrypted version of the key with your certificate bundle. You can use OpenSSL to decrypt a private key:

```

```

## Configuring SSL Handling

Learn about configuring SSL handling for a Load Balancer resource.

You can perform the following SSL handling tasks for a load balancer:
- Terminate SSL at the load balancer. This configuration is frontend SSL . Your load balancer can accept encrypted traffic from a client. No encryption of traffic exists between the load balancer and the backend servers.
- Implement SSL between the load balancer and your backend servers. This configuration is backend SSL . Your load balancer does not accept encrypted traffic from client servers. Traffic between the load balancer and the backend servers is encrypted.
- Implement point-to-point SSL. Your load balancer can accept SSL encrypted traffic from clients and encrypts traffic to the backend servers.

### Terminating SSL at the Load Balancer

To terminate SSL at the load balancer, you must create a listener at a port such as 443, and then associate an uploaded certificate bundle with the listener. See[Creating a Load Balancer Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm)for more information.

### Implementing Backend SSL

To implement SSL between the load balancer and your backend servers, you must associate an uploaded certificate bundle with the backend set. See[Creating a Load Balancer Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)for more information.
Note  
  

- To have more than one backend server in the backend set, sign your backend servers with an intermediate CA certificate. The intermediate CA certificate must be included as part of the certificate bundle.
- Your backend services must be able to accept and terminate SSL.

### Implementing Point-to-Point SSL

To implement point-to-point SSL, you must associate uploaded certificate bundles with both the listener and the backend set. See[Creating a Load Balancer Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm)and[Creating a Load Balancer Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm)for more information.

## Listing Certificates Service-Managed Certificates

View a list of the Certificates service-managed certificates for a load balancer.

Load balancer certificates that are managed by the Certificates service can only be listed within the Load Balancer Console. To perform other Certificates service tasks, such as creating, editing, and deleting a certificate, see[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm).

To view SSL certificates created using the Load Balancer service, see[Listing Load Balancer Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-certificate.htm)

### Using the Console

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Certificate service certificates section.
The Certificate service managed certificates list opens. All Certificates service-managed in the selected load balancer are displayed in a table. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on how the Certificates service works.
The Certificate service managed certificates list opens. All Certificates service managed-certificates in the selected load balancer are displayed in a table. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on how the Certificates service works.

#### Filtering List Results

Use filters to limit the Certificates service-managed certificates in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

#### Actions
