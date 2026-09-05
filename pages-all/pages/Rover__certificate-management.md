# Certificate Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/certificate-management.htm
- Fetched: 2026-09-05 03:02 CDT

# Certificate Management

Describes how to manage your Roving Edge Infrastructure devices' certificates.

You can view and manage your Roving Edge Infrastructure device nodes' certificates and certificate actions through the Node Management section in your node's Device Console. For each device node, only the latest version of the certificate and the latest action performed on that certificate is maintained. If you create a new certificate, that certificate will be the only one that is visible and the previous certificate is no longer maintained or usable.
Note  
  

Oracle recommends that you to use different Certificate Authorities (CAs) for each order. You can use the same root CA, but use different subordinate CAs. If you use the same CA for all your Roving Edge Infrastructure devices, a compromise in the common root/subordinate CA results in a compromise for all the devices using it.

You can perform the following device node certificate management tasks for your device node:
- 

[Getting a certificate's details](https://docs.oracle.com/en-us/iaas/Content/Rover/view-certificate.htm#top)
- 

[Getting a CA bundle's details](https://docs.oracle.com/en-us/iaas/Content/Rover/get-ca-bundle.htm#top)
- 

[Updating the certificate's details](https://docs.oracle.com/en-us/iaas/Content/Rover/update-certificate-details.htm#top)
- 

[Renewing an existing certificate for a connected device node](https://docs.oracle.com/en-us/iaas/Content/Rover/renew-certificate-node.htm#top)
- 

[Renewing a certificate for a disconnected device node](https://docs.oracle.com/en-us/iaas/Content/Rover/renew-certificate-offline.htm#top)
- 

[Creating a certificate for a connected device node](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-node.htm#top)
- 

[Creating a certificate for a disconnected device node](https://docs.oracle.com/en-us/iaas/Content/Rover/create-certificate-offline.htm#top)

Renew vs. Create Certificate
