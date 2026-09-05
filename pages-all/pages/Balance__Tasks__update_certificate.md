# Updating an Expiring Load Balancer Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/update_certificate.htm
- Fetched: 2026-09-05 01:42 CDT

# Updating an Expiring Load Balancer Certificate

Update an expiring SSL certificate for a load balancer.

To ensure consistent service, you must update (rotate) expiring certificates. This process consists of the performing the tasks:
- Uploading the new SSL certificate bundle to the load balancer.
- Editing the applicable listeners and backend sets so they use the new certificate bundle.
- Optionally remove the expiring SSL certificate bundle.

## Using the Console

- Upload the new SSL certificate bundle to the load balancer:

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Load balancer certificates section.

The Load balancer managed certificates list opens. All Load Balancer service-managed certificates in the selected load balancer are displayed in a table.
- Select Add certificate .

The Add certificate panel opens.
- Enter the following information:
- Certificate name : Enter a friendly name for the certificate bundle. It must be unique within the load balancer, and it can't be changed in the Console. (It can be changed using the API.)
- Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field.

You can also choose the Paste SSL certificate option to paste a certificate directly into this field.
Important  
  
If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
- Specify CA certificate : (Recommended for backend SSL termination configurations.) Select to provide a CA certificate.
- Choose CA certificate file : Drag the CA certificate file, in PEM format, into the CA certificate field.

You can also choose the Paste CA certificate option to paste a certificate directly into this field.
- Specify private key : (Required for SSL termination.) Select to provide a private key for the certificate.
- Choose private key file : Drag the private key, in PEM format, into the Private key field.

You can also choose the Paste private key option to paste a private key directly into this field.
- Enter private key passphrase : (Optional) Specify the private key passphrase.
- Select Add certificate . Next, edit each applicable listeners or backend sets (as needed) so they use the new certificate bundle:
- Edit the listener:

- On the load balancer's details page, select Listeners .
- From the Actions menu for the listener, select Edit .

The Edit listener panel opens.
- In the Certificate name list, select the new certificate bundle.
- Select Save changes .
- Edit the backend set:

Important  
  
Updating the backend set temporarily interrupts traffic and can drop active connections.
- On the load balancer's details page, select Backend sets .
- From the Actions menu for the backend set, select Edit .

The Edit backend set panel opens.
- On the backend set's details page, enable Use SSL .
- In the Certificate name list, select the new certificate bundle.
- Select Save changes .
- (Optional) Remove the expiring SSL certificate bundle.

Note  
  
You can't delete an SSL certificate bundle that's associated with a listener or backend set. Remove the bundle from any other listeners or backend sets before deleting.
- On the load balancer's details page, select Certificates and ciphers and find the Load balancer certificates section.
- From the Actions menu for the certificate you want, select Delete .
-
