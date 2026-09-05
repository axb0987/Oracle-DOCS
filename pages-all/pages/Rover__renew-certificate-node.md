# Renewing a Certificate for a Roving Edge Infrastructure Device Node while Connected
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/renew-certificate-node.htm
- Fetched: 2026-09-05 03:02 CDT

# Renewing a Certificate for a Roving Edge Infrastructure Device Node while Connected

Describes how to renew an existing certificate for a device node while connected to the Oracle Cloud Infrastructure Cloud.

Renew the certificate for a device node if you want to extend its validity time, but do not want to change any of its details, such as the key algorithm. If you do want to change the details of the certificate, you must create a new one instead of renewing the existing certificate. See[Creating a certificate while connected](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-node.htm#top).
Note  
  

If you want to renew a certificate for a disconnected device node, see[Creating a Certificate while Disconnected](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-offline.htm#top)

## Using the Device Console

- Access the Device Console for the device node whose certificate you are renewing.
- Open the navigation menu and select Node Management &gt; Certificates . The Certificates page appears. Each Roving Edge Infrastructure device node's certificate is listed.
- select Renew certificates . You can also select Renew under the Action menu at the right of the certificate entry. The Renew certificates dialog box appears.
- Select Not Valid After . The date and time calendar appears. Select the date and UTC time wanted as the expiration date for the certificate, and then select Submit . The date and time you specify cannot exceed the maximum validity period of the certificate authority that is used for the certificate.
