# Bring Your Own Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/BringYourOwnCertificateAPI.htm
- Fetched: 2026-09-05 02:16 CDT

# Bring Your Own Certificate

Use custom certificates to configure SAML SSO in an identity domain.

A Certificate Signing Request (CSR) is a block of encoded text submitted to a Certificate Authority (CA) to apply for a new Certificate. A CSR contains information included in the Certificate. For example, Common Name, Organization, Organizational Unit, and Public Key are included in the Certificate.

## Before You Begin
Important  
  
You must create a Service Request (SR) with the Identity SAML team to enable the required feature flag for this functionality. See[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
- Provide the following details in the SR:
- The Identity Domain's GUID. For example,`ocid1.group.oc1..exampleuniqueID`.
- Provide your reason and use case for the request.
- Tenancy region.
- The component must be "`SAML`".

Perform the following actions before you start using your own CSR.
- Create an access token with an`Identity Domain Administrator`role to perform the following API commands. For more information on how to create an Access token, see[Generating an Access Token](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../usersettings/generate-personal-access-tokens.htm).
- Create a confidential application in the identity domain. For more information, see[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-confidential-application.htm).
- Configure the application as a client.
- On the page to configure OAuth, select Add app roles , and then select the application roles you want to apply to this application. Assign Identity Domain Administrator to the list of app roles.
- Use the client GUID and client secret to generate the Access token using a token endpoint.

## 1: Generating a Certificate Signing Request
Create a CSR for an identity domain (ID), make a POST request to the`CertificateSigningRequests`endpoint:
```

```

Sample request payload:
```

```

Property name Required? Data type Description
`certSubjectName`Optional Array

Certificate Subject Name or Certificate Name details. Common Name is required and all other parameters are optional.
For example,
- "CN=Sample Certificate,OU=Employees,O=Sample Corporation,C=US"
- "CN=[www.samplecertificate.com](http://www.samplecertificate.com)"
`certSubjectAltName`Required String Certificate Subject Alternate Name. For example, a certificate that lets several domain names to be protected by a single certificate has a SAN list defined in it.
`includeKeyUsage`Optional Boolean If true, key usages are included from the CSR. If false, key usages are omitted.
`signatureAlgorithm`Optional String By default, the signature algorithm is`SHA256WITHRSA`. Supported values are
- "SHA256WITHRSA"
- "SHA384WITHRSA"
- "SHA512WITHRSA"
Expected response:
```

```

Property name Data type Description
`csr`String Certificate Signing Request generated using the values defined in the API payload.

## 2: Getting a Certificate Issued by a Preferred Certificate Authority

Use the CSR you generated in step 1 to get a certificate issued from your preferred Certificate Authority (CA).

The expected outcome of this step is a certificate in`.pem`,`.cer`, or`.crt`format. Open this certificate in a text editor and copy the base64 encoded part of it, as required to create a SAML partner certificate.

## 3: Creating a SAML Partner Certificate

The expected certificate format is`.pem`,`.cer`, or`.crt`format from your preferred certificate provider.
To create a SAML partner certificate for an identity domain, open the certificate file, copy the base64-encoded portion, and paste it into a POST request to the API endpoint`SamlPartnerCertificates`:
```

```

Sample request payload:
```

```

Payload property details:

Property name Required? Data type Description
`x509Base64Certificate`Required String Certificate issued by a preferred CA which is generated using the CSR.
`displayName`Required String A unique user- friendly name for the certificate.
`includeKeyUsage`Optional Boolean If true, key usages are included from the CSR. If false, key usages are omitted.
Expected response:
```

```

Property name Data type Description
`Id`String Unique GUID for the SAML Partner Certificate resource.
`x509Base64Certificate`String Certificate issued by customer's preferred CA, which is generated using the CSR.
`displayName`String A customer defined, unique user-friendly name for the certificate.
`b64certificate`String Base64 encoded string of customer's signing certificate.
`description`String A short description about the certificate.
`certStartDate`Datetime Issued date of the certificate.
`certEndDate`Datetime Expiration date of the certificate.
`sha1Thumbprint`String SHA-1 thumbprint of the certificate.
`sha256Thumbprint`String SHA-256 thumbprint of the certificate.
`sha384Thumbprint`String SHA-384 thumbprint of the certificate.

## 4: Listing all SAML Partner Certificates for an Identity Domain
To list all SAML partner certificate for an identity domain, make a GET request to the endpoint`SamlPartnerCertificates`:
```

```

Expected response:
```

```

## 5: Generating the SAML Metadata with SAML Partner Certificate

To generate SAML metadata using SAML Partner Certificate, make a`GET`request to this API endpoint:`https://idcs-<identity-domain-url>/fed/v1/metadata?samlPartnerCertificateId=<guid-of-certificate-resource>`
Expected response:
```

```

## 6: Setting Up SAML SSO
Use the following to create a SAML application or a SAML Identity Provider:
- [Adding a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../applications/add-saml-application.htm)
- [Adding a SAML Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/../identityproviders/add-saml-identity-provider.htm#add-saml-identity-provider-console)
Note  
  

- While setting up the SAML SSO between SP and IdP, use the identity domain SAML metadata generated from earlier. Don't download the SAML metadata using the download button from the Console.
- Upload the partner application custom certificate issued by the preferred CA. Don't download the custom certificate from the Console.

## 7: PATCH the SAML Service Provider Application and Identity Provider (Optional)

If the identity domain is an IdP, then update the SAML application created in the Identity Domain. For more details on this, please see[Update an Application](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/op-admin-v1-apps-id-patch.html)from an API. To add a SAML Partner Certificate to a Service Provider Application in an Identity Domain, make the HTTP PATCH request to this API endpoint.

`https://idcs-<identity-domain-url>/admin/v1/Apps/<sp-application-guid>`
- Update "useSamlPartnerCertificate" and "samlPartnerCertificateId" properties.
Sample request:
```

```

Expected response:
```

```

- PATCH the Identity Provider

If IDCS is SP, then please update the SAML Identity Provider created in the IDCS Identity Domain.
To add a Saml Partner Certificate to an Identity Provider Application in an Identity Domain, make the HTTP PATCH request to this API endpoint.
```

```

Update`useSamlPartnerCertificate`and`samlPartnerCertificateId`properties:
```

```

Expected response:
```

```
