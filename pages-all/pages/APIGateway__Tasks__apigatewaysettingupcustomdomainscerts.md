# Setting Up Custom Domains and TLS Certificates
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm
- Fetched: 2026-09-05 01:38 CDT

# Setting Up Custom Domains and TLS Certificates

Find out how to set up custom domains and TLS certificates with API Gateway.

The API gateways you create with the API Gateway service are TLS-enabled, and therefore require TLS certificates (formerly SSL certificates) issued by a Certificate Authority to secure them. You can direct the API Gateway service to obtain a default TLS certificate for you (if your tenancy exists in the OC1 realm), or you can obtain a custom TLS certificate from a Certificate Authority yourself. To specify a particular custom domain name for an API gateway, you must obtain a custom TLS certificate, rather than have the API Gateway service obtain a default TLS certificate.

When you create an API gateway, you specify that the API gateway uses one of the following:
- A default TLS certificate that the API Gateway service obtains for you (OC1 realm only). In this case, the API Gateway service requests a TLS certificate from an Oracle-designated Certificate Authority.
- A custom TLS certificate that you obtain from your chosen Certificate Authority yourself. Your request to the Certificate Authority includes the custom domain name. The Certificate Authority returns a file containing the custom TLS certificate, and typically one or more files containing intermediate certificates forming a certificate chain from the TLS certificate back to the Certificate Authority.

You can obtain a custom TLS certificate in multiple ways:
- You can obtain a custom TLS certificate from a third-party Certificate Authority, and then create an API Gateway certificate resource comprising the custom TLS certificate, any intermediate certificates, and the private key used to generate the TLS certificate. You can then select that API Gateway certificate resource when creating a new API gateway.
- You can obtain a custom TLS certificate using the[Certificates service](https://docs.oracle.com/iaas/Content/certificates/home.htm)to create a certificate resource. The Certificates service can issue a certificate directly, or you can import a certificate issued by a third-party Certificate Authority into the Certificates service. You can then select that Certificates service certificate resource when creating a new API gateway.

The way in which the TLS certificate is obtained determines how much control you have over the API gateway's domain name:
- If the API Gateway service obtains a default TLS certificate for you (OC1 realm only), the API Gateway service gives the API gateway an auto-generated default domain name. The auto-generated default domain name comprises a random string of characters followed by`.apigateway.<region-identifier>.oci.customer-oci.com`. For example,`laksjd.apigateway.us-phoenix-1.oci.customer-oci.com`.
- If you obtain a custom TLS certificate yourself, the API Gateway service gives the API gateway the custom domain name you specified in your request to the Certificate Authority.

The way in which the TLS certificate is obtained also determines responsibility for recording the mapping between the API gateway's domain name and its public IP address with a DNS provider:
- If the API Gateway service obtains a default TLS certificate for you (OC1 realm only), the API Gateway service takes responsibility for recording the mapping between the API gateway's auto-generated default domain name and its public IP address with the Oracle Cloud Infrastructure DNS service.
- If you obtain a custom TLS certificate yourself, you are responsible for recording the mapping between the API gateway's custom domain name and its public IP address with your chosen DNS provider as an A record.

Similarly, the handling of TLS certificate expiry and renewal is determined by how the TLS certificate is originally obtained:
- If the API Gateway service obtains a default TLS certificate for you (OC1 realm only), the API Gateway service automatically renews the TLS certificate with the Oracle-designated Certificate Authority before it expires.
- If you obtain a custom TLS certificate yourself, you are responsible for renewing the TLS certificate with your chosen Certificate Authority before it expires. See[Renewing Custom TLS Certificates Used by API Gateways](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#Renewing_Custom_TLS_Certificates_Used_by_API_Gateways).

For some customers, use of custom domains and custom TLS certificates is obligatory. For example, if you are using Oracle Cloud Infrastructure Government Cloud, you are required to:
- only obtain a TLS certificate from a particular, approved Certificate Authority
- only use a particular, approved DNS provider

For other customers, use of custom domains is likely to be driven by commercial requirements. For example, typically you'll want to include your company name in the API gateway's domain name, rather than using the auto-generated random string of characters followed by`.apigateway.<region-identifier>.oci.customer-oci.com`.

Note the following:
- You cannot delete an API Gateway certificate resource or Certificates service certificate resource that is currently being used by an API gateway. To delete the certificate resource, you must first remove it from any API gateway that is using it.
- You can only specify one API Gateway certificate resource or Certificates service certificate resource for an API gateway.
- You cannot update an API Gateway certificate resource after you have created it. However, you can update a Certificates service certificate resource.
- You can only direct the API Gateway service to obtain default TLS certificates for you if your tenancy exists in the OC1 realm.
Important  
  
For public or production systems, Oracle recommends using custom TLS certificates. Oracle recommends only using default TLS certificates obtained by the API Gateway service for private or non-production systems (for example, for development and testing).

## Obtaining a Custom TLS Certificate to Set Up a Custom Domain Name for an API Gateway

You can set up a custom domain name and custom TLS certificate in multiple ways:
- You can obtain a custom TLS certificate from a third-party Certificate Authority, and then create an API Gateway certificate resource comprising the custom TLS certificate, any intermediate certificates, and the private key used to generate the TLS certificate. You can then select that API Gateway certificate resource when creating a new API gateway. See[Using an API Gateway Certificate Resource to Set Up a Custom Domain Name for an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#apigatewaysettingupcustomdomainscerts_topic_using_an_apigw_certificate_resource).
- You can obtain a custom TLS certificate using the Certificates service to create a Certificates certificate resource (see[Certificates service](https://docs.oracle.com/iaas/Content/certificates/home.htm)). The Certificates service can issue a certificate directly, or you can import a certificate issued by a third-party Certificate Authority into the Certificates service. You can then select that Certificates service certificate resource when creating a new API gateway. See[Using a Certificates Service Certificate Resource to Set Up a Custom Domain Name for an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#apigatewaysettingupcustomdomainscerts_topic_using_a_certificates_service_certificate_resource).

## Using an API Gateway Certificate Resource to Set Up a Custom Domain Name for an API Gateway

To use an API Gateway certificate resource to set up a custom domain name for an API gateway:

[Step 1: Obtain a TLS Certificate from your chosen Certificate Authority](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

The precise steps to obtain a TLS certificate will be different, according to the Certificate Authority you choose to use. At a high level, the steps will probably be somewhat similar to the following, but always refer to the Certificate Authority documentation for more detailed information:
- 

Create a certificate signing request for your chosen Certificate Authority.

Typically, you'll include information like the organization name, locality, and country in the certificate signing request.

You'll also include a common name in the certificate signing request as the fully qualified domain name of the site you want to secure. The common name usually connects the TLS certificate with a particular domain. This domain name is used as the custom domain name for API gateways.

When you create a certificate signing request, a public key is added to the request, and a corresponding private key is also generated and stored in a local file. You'll use this private key when you set up an API Gateway certificate resource, so make a note of its location. The private key you use to obtain a TLS certificate:
- must be an RSA key
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN RSA PRIVATE KEY-----`
- must end with`-----END RSA PRIVATE KEY-----`
- must not be protected by a passphrase
- must have a minimum length of 2048 bits and must not exceed 4096 bits
- 

Submit the certificate signing request to the Certificate Authority.

The Certificate Authority returns:
- a file containing the custom TLS certificate for the API gateway itself (known as the 'leaf certificate' or 'end-entity certificate')
- typically one or more files containing intermediate certificates that form a certificate chain from the leaf certificate back to the Certificate Authority

You can now use these certificate files to create an API Gateway certificate resource.

[Step 2: Create an API Gateway certificate resource](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

An API Gateway certificate resource is a named definition of a TLS certificate that you can use when creating or updating an API gateway using the API Gateway service.

An API Gateway certificate resource comprises:
- a name of your choice for the certificate resource itself
- the custom TLS certificate for the API gateway (the 'leaf certificate' or 'end-entity certificate') returned by the Certificate Authority
- any intermediate certificates forming a certificate chain from the leaf certificate back to the Certificate Authority
- the private key paired with the public key that was included in the original certificate signing request

Note that you cannot update an API Gateway certificate resource after you have created it.

You can create an API Gateway certificate resource using the Console or the CLI.

#### Using the Console

To create an API Gateway certificate resource using the Console:
- On the Certificates list page, select Create Certificate . If you need help finding the list page, see[Listing API Gateway Certificate Resources](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-certificates.htm).
- 

Specify the following values for the API Gateway certificate resource:
- Name: The name of the new API Gateway certificate resource. Avoid entering confidential information.
- Compartment: The compartment in which to create the API Gateway certificate resource.
- Certificate: The custom TLS certificate returned by the Certificate Authority (the 'leaf certficate' or 'end-entity certificate'). Drag and drop, select, or paste a valid TLS certificate. Note that the TLS certificate you specify:
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN CERTIFICATE-----`
- must end with`-----END CERTIFICATE-----`
- must not exceed 4096 bits in length
- 

Intermediate Certificates: (Optional) If there is one or more intermediate certificates forming a certificate chain from the TLS certificate back to the Certificate Authority, include the contents of the intermediate certificate files in the correct order. The correct order begins with the certificate directly signed by the Trusted Root Certificate Authority at the bottom, with any additional certificate directly above the Certificate Authority that signed it. For example:
```

```

If you have concatenated the contents of intermediate certificate files into a single certificate chain file in the correct order, drag and drop that file, or select that file, or paste that file's content.

If you don't have a concatenated certificate chain file, paste the contents of the individual certificate files, in the correct order.

The combined length of any intermediate certificates you specify must not exceed 10240 bits.
- Private Key: The private key used to obtain the TLS certificate from the Certificate Authority. Drag and drop, select, or paste a valid private key in this field. Note that the key you specify:
- must be an RSA key
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN RSA PRIVATE KEY-----`
- must end with`-----END RSA PRIVATE KEY-----`
- must not be protected by a passphrase
- must have a minimum length of 2048 bits and must not exceed 4096 bits
- 

Tags: (Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the API Gateway certificate resource.

#### Using the CLI

To create an API Gateway certificate resource using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway certificate create`to create the API Gateway certificate resource:

```

```

where:
- `<certificate-name>`is the name of the new API Gateway certificate resource. Avoid entering confidential information.
- `<compartment-ocid>`is the OCID of the compartment to which the new API Gateway certificate resource will belong.
- 

`<certificate-file-path>`is the path and name of the file containing the leaf certificate returned by the Certificate Authority. For example,`~/.certs/cert.pem`. Note that the leaf certificate in the file you specify:
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN CERTIFICATE-----`
- must end with`-----END CERTIFICATE-----`
- must not exceed 4096 bits in length
- 

`<intermediate-certificates-file-path>`is optionally the path and name of a file containing one or more intermediate certificates forming a certificate chain from the leaf certificate back to the Certificate Authority. For example,`~/.certs/int_cert.pem`. If the file contains multiple intermediate certificates, the intermediate certificates must be in the correct order. The correct order ends with the certificate directly signed by the Trusted Root Certificate Authority, with any additional certificate directly preceding the Certificate Authority that signed it. For example:
```

```

The combined length of any intermediate certificates you specify must not exceed 10240 bits.
- 

`<private-key-file-path>`is the path and name of the file containing the private key used to obtain the TLS certificate from the Certificate Authority. For example,`~/.certs/key.pem`. Note that the private key in the file you specify:
- must be an RSA key
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN RSA PRIVATE KEY-----`
- must end with`-----END RSA PRIVATE KEY-----`
- must not be protected by a passphrase
- must have a minimum length of 2048 bits and must not exceed 4096 bits

For example:

```

```

The response to the command includes:
- The OCID of the new API Gateway certificate resource.
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to create the API Gateway certificate resource (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the API Gateway certificate resource is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

[Step 3: Specify the API Gateway certificate resource when creating an API gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

To specify the API Gateway certificate resource when creating an API gateway:
- Follow the instructions in[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)to create an API gateway using either the Console or the CLI.
- 

Specify the API Gateway certificate resource as described in the instructions:
- If using the Console: Use the Certificate field.
- If using the CLI: Set the`--certificate-id <certificate-ocid>`property.

The API Gateway service creates the new API gateway, and installs the custom TLS certificate and private key.
- Obtain the public IP address of the API gateway.

[Step 4: Record the mapping between the API Gateway's custom domain name and public IP address with your chosen DNS provider](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

The precise steps to record the mapping between an API gateway's custom domain name and its public IP address depend on the DNS provider you choose to use. Typically, you will create a new record (specifically a new A record) in the DNS provider's configuration. The record associates the domain name you configured when requesting the TLS certificate from your chosen Certificate Authority with the public IP address that the API Gateway service assigns to the new API gateway. Refer to your chosen DNS provider's documentation for more detailed information.

## Using a Certificates Service Certificate Resource to Set Up a Custom Domain Name for an API Gateway

To use a Certificates service certificate resource to set up a custom domain name for an API gateway:

[Step 1: Create a Certificates Service certificate resource](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

You can use the Certificates service in multiple ways to create a certificate resource when setting up a custom domain name for an API gateway:
- You can use the Certificates service to issue a TLS certificate that you plan to manage internally with the Certificates service. For more information about creating a Certificates service certificate resource in this way, see[Creating a Certificate](https://docs.oracle.com/iaas/Content/certificates/creating-certificate.htm).
- You can use the Certificates service to import a TLS certificate issued by a third-party Certificate Authority, that you plan to manage internally with the Certificates service. For more information about creating a Certificates service certificate resource in this way, see[Importing a Certificate](https://docs.oracle.com/iaas/Content/certificates/importing-certificate.htm).

Note that although you can use the Certificates service to issue a TLS certificate that you plan to manage externally with a third-party Certificate Authority, you cannot use such an externally-managed TLS certificate when setting up a custom domain name for an API gateway.

Also note the following:
- The TLS certificate:
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN CERTIFICATE-----`
- must end with`-----END CERTIFICATE-----`
- must not exceed 4096 bits in length
- The TLS certificate must have been created using one of the supported certificate profile types, as follows:
- Supported certificate profile types: TLS Server or Client ; TLS server .
- Unsupported certificate profile types: TLS Client ; TLS Code Sign .
- The private key used to obtain the TLS certificate:
- must be an RSA key
- must be in PEM-encoded X.509 format
- must start with`-----BEGIN RSA PRIVATE KEY-----`
- must end with`-----END RSA PRIVATE KEY-----`
- must not be protected by a passphrase
- must have a minimum length of 2048 bits and must not exceed 4096 bits

[Step 2: Specify the Certificates Service certificate resource when creating an API gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

To specify the Certificates service certificate resource when creating an API gateway:
- Follow the instructions in[Creating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm)to create an API gateway using either the Console or the CLI.
- 

Specify the Certificates service certificate resource as described in the instructions:
- If using the Console: Use the Certificate field.
- If using the CLI: Set the`--certificate-id <certificate-ocid>`property.

The API Gateway service creates the new API gateway, and installs the custom TLS certificate and private key.
- Obtain the public IP address of the API gateway.

[Step 3: Record the Mapping Between the API Gateway's Custom Domain Name and Public IP Address With Your Chosen DNS Provider](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#)

The precise steps to record the mapping between an API gateway's custom domain name and its public IP address depend on the DNS provider you choose to use. Typically, you will create a new record (specifically a new A record) in the DNS provider's configuration. The record associates the domain name you configured when requesting the TLS certificate from your chosen Certificate Authority with the public IP address that the API Gateway service assigns to the new API gateway. Refer to your chosen DNS provider's documentation for more detailed information.

## Renewing Custom TLS Certificates Used by API Gateways

TLS certificates are valid for a limited period of time (typically one or two years) before they expire. If the TLS certificate used by an API gateway expires, calls to an API deployed on the API gateway might be marked as insecure by the API client (for example, by a browser or by the curl command line tool) and blocked. To avoid blocked calls, you have to renew TLS certificates before they expire (sometimes referred to as 'rotating' certificates).

If the API Gateway service obtained the original TLS certificate for you, the API Gateway service automatically renews the TLS certificate with the Oracle-designated Certificate Authority before it expires. However, if you obtained a custom TLS certificate yourself, you are responsible for renewing the custom TLS certificate with your chosen Certificate Authority before it expires. When you request the renewal of a TLS certificate, the Certificate Authority returns a completely new TLS certificate.

The procedure for renewing a custom TLS certificate used by API gateways depends on whether you've created API Gateway certificate resources or Certificates service certificate resources.

### Renewing custom TLS certificates for API Gateway certificate resources

When you've created an API Gateway certificate resource used by an API gateway, you cannot simply update the existing API Gateway certificate resource with the new TLS certificate. Instead, you create a new API Gateway certificate resource, add the new TLS certificate to the new certificate resource, and then update any API gateways that used the previous certificate resource to use the new certificate resource.

To renew the custom TLS certificate used by an API gateway:
- 

Submit a TLS certificate renewal request to the Certificate Authority from which you originally obtained the TLS certificate. The exact steps to renew a TLS certificate depend on the Certificate Authority you use, so always refer to the Certificate Authority documentation for more detailed information.

When you create the certificate renewal request, a public key is added to the request, and a corresponding private key is also generated and stored in a local file. You'll use this private key when you set up the new API Gateway certificate resource, so make a note of its location.

The Certificate Authority returns a file containing the new custom TLS certificate, and typically one or more files containing intermediate certificates forming a certificate chain from the TLS certificate back to the Certificate Authority.
- Create a new API Gateway certificate resource and add to it the new TLS certificate, any intermediate certificates, and the new private key (see[Step 2: Create an API Gateway certificate resource](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomdomainscerts.htm#Step)).
- Update all the existing API gateways that used the original API Gateway certificate resource to use the new API Gateway certificate resource (see[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm)).
- When there are no API gateways still using the original API Gateway certificate resource, delete the original certificate resource:
- If using the Console: On the Certificates page, select the Actions menu (three dots) beside the original API Gateway certificate resource you want to delete, and then select Delete .
- If using the CLI: Use the following command to delete the original API Gateway certificate resource:

```

```

Note that you cannot delete an API Gateway certificate resource if there are API gateways still using it.

### Renewing custom TLS certificates for Certificates service certificate resources

When you've created a Certificates service certificate resource used by an API gateway, you can use the Certificates service to renew the TLS certificate by creating a new certificate version. The new certificate version has the same OCID as the original certificate, so you don't have to modify API gateways to use a new certificate resource. The API Gateway service automatically updates API gateways to use the new version. Note that there are some restrictions on the certificates that the Certificates service can renew. See[Renewing a Certificate](https://docs.oracle.com/iaas/Content/certificates/renewing-certificate.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the:
- [CreateCertificate](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/CreateCertificate)operation to create a new API Gateway certificate resource.
- [DeleteCertificate](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/DeleteCertificate)operation to delete an existing API Gateway certificate resource.
- [UpdateCertificate](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/UpdateCertificate)operation to change the details of an existing API Gateway certificate resource.
- [GetCertificate](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/GetCertificate)operation to see details of an existing API Gateway certificate resource.
- [ListCertificates](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/ListCertificates)operation to list all the certificates in a compartment.
- [ChangeCertificateCompartment](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Certificate/ChangeCertificateCompartment)
