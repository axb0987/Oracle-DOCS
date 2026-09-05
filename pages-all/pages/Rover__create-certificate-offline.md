# Creating a Certificate for a Roving Edge Infrastructure Device while Disconnected
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-offline.htm
- Fetched: 2026-09-05 03:02 CDT

# Creating a Certificate for a Roving Edge Infrastructure Device while Disconnected

Describes how to create a new certificate for a Roving Edge Infrastructure device node while disconnected from the Oracle Cloud Infrastructure Cloud.

## Using the Device Console and OCI Cloud Console

- Access the Device Console for the device node for which you are creating the certificate.
- Open the navigation menu and select Node Management &gt; Certificates . The Certificates page appears. Each Roving Edge Infrastructure device node's certificate is listed.
- Select the Create Certificate Signing Requests button above the list of certificates. You can also select Create Certificate Signing Request under the Action menu (three dots to the right of the node). The Create Certificate Signing Request dialog box appears.
- Select a Key Algorithm from the list to be used for the certificate signing request.
- Select Submit . The Device Console displays a message confirming that the certificate signing request for the device node has been successfully submitted.
- Monitor the status of your certificate signing request by performing the following steps:

- 

Select Certificate Actions under Node Management on the left side of the page to see the state of the request. The Certificate Actions page appears. The status of the certificate signing request is listed in tabular format. The page displays the last stage completed in the certificate signing request submission process.
- 

Select View under the Action menu (three dots at the right of the certificate signing request entry) to display the View Certificate Action dialog box. This dialog box displays a variety of information regarding the certificate request.
- 

If your attempt to create a certificate fails for a particular device node, you can select Retry under the Action menu (three dots to the right of the node).
- Select Certificate under Node Management to return to the Certificate page.
- Select View Certificate Signing Request under the Action menu (three dots to the right of the node). The View Certificate Signing Request dialog box appears.
- Download the certificate PEM file (`.csr`or`.pem`) or copy and paste the certificate PEM contents into a file. Transfer this file to a computer that has access to the Oracle Cloud Infrastructure Cloud.
-   

-   

- Select the device node for which you want to create a certificate. The device node's Details page appears.
- Select the Certificate information tab to view details on the device node's existing certificate. You can return to this tab later after you generate the new certificate to view the updated details.
- From the Actions menu at the top of the page, select Generate Certificate . The Generate Certificate dialog box appears.
- Upload the certificate PEM file (`.csr`or`.pem`) from your connected computer, or copy and paste the certificate PEM contents into the Certificate Signing Request box.
- Select Not Valid After . The date and time calendar appears. Select the date and UTC time wanted as the expiration date for the certificate, and then select Submit . The date and time you specify cannot exceed the maximum validity period of the certificate authority that is used for the certificate.
- Select Generate Certificate . The Details page displays a message indicating that a new certificate has been generated with an associated OCID on the Oracle Cloud Infrastructure Cloud. The contents of the Certificate Information tab are also updated to reflect the new certificate.
- Select View Certificate Content . The View Certificate Content dialog box appears.
- Copy or download the certificate PEM file or contents to the computer that has connected access to the Roving Edge Infrastructure environment
- Select View CA Bundle Content from the More Actions menu. The View CA Bundle Content dialog box appears.
- Copy or download the CA bundle file or contents to the computer that has network connectivity to the Roving Edge Infrastructure device.

You can also use the CLI to perform the following tasks:
- 

Creating a certificate for a Roving Edge Infrastructure device node. Run the following CLI command and parameters:
```

```

certificate_signing_request is the certificate signing request in`.PEM`format. The maximum size of the request is 10240 characters.

time_cert_validity_end is the time when the renewed certificate's validity ends. You can express this time in the following formats:
- 

UTC with microseconds
- 

Timezone with microseconds
- 

Viewing a certificate for a Roving Edge Infrastructure device. Run the following CLI command and parameters:
```

```

- 

View the CA bundle content of a Roving Edge Infrastructure. Run the following CLI command and parameters:
```

```

- Return to the Device Console on the device node for which you are creating the certificate and access the Certificates page.
- Select Import under the Action menu (three dots to the right of the node). The Import Certificate dialog box appears.
- Upload the certificate file (`.pem`) from your connected computer, or copy and paste the certificate contents into the Add Certificate box.
- Upload the CA bundle file (`.pem`) from your connected computer, or copy and paste the CA bundle contents into the Add Ca-bundle box.
- Select Import . The Certificates page displays a message indicating that your request to import the certificate has been successfully submitted.
- Monitor the status of your import by performing the following steps:

- 

Select Certificate Actions under Node Management on the left side of the page to see the state of the import. The Certificate Actions page appears. The status of the import is listed in tabular format. The page displays the last stage completed in the import process.
- 

Select View under the Action menu (three dots at the right of the import entry) to display the View Certificate Action dialog box. This dialog box displays a variety of information regarding the import.
- 

If your attempt to import fails for a particular device node, you can select Retry under the Action menu (three dots to the right of the device node).
