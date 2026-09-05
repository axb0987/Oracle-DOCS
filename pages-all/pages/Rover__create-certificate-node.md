# Creating a Certificate for a Roving Edge Infrastructure Device while Connected
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-node.htm
- Fetched: 2026-09-05 03:02 CDT

# Creating a Certificate for a Roving Edge Infrastructure Device while Connected

Describes how to create a new certificate for a Roving Edge Infrastructure device node while connected to the Oracle Cloud Infrastructure Cloud.

Note  
  

If you want to create a certificate for a disconnected device node, see[Creating a Certificate while Disconnected](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-offline.htm#top)

## Using the Device Console

- Access the Device Console for the device node for which you are creating the certificate.
- Open the navigation menu and select Node Management &gt; Certificates . The Certificates page appears. Each Roving Edge Infrastructure device node's certificate is listed.
- Select Create Certificates . You can also select Create under the Actions menu ( ) (at the right of each certificate entry). The Create Certificates dialog box appears.
- Select Not Valid After . The date and time calendar appears. Select the date and UTC time wanted as the expiration date for the certificate, and then select Submit . The date and time you specify cannot exceed the maximum validity period of the certificate authority that is used for the certificate.
- Select Submit .

The Device Console displays a message confirming that the request to create certificates for the device node have been successfully submitted.
- Select Certificate Actions under Node Management on the left side of the page to see the state of the request. The Certificate Actions page appears. Each device node certificate request is listed in tabular format. This page displays information regarding the certificate request, including the current action and lifecycle status.
- Select View under the Actions menu ( ) at the right of each certificate request entry to display the View Certificate Action dialog box. This dialog box displays a variety of information regarding the certificate request.
- If your attempt to create a certificate fails for a particular device node, you can select Retry under the Action menu to the right of the node.
