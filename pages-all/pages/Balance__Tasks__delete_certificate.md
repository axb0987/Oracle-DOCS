# Deleting a Load Balancer Certificate
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm
- Fetched: 2026-09-05 01:40 CDT

# Deleting a Load Balancer Certificate

Remove an SSL certificate from a load balancer.
Note  
  

You cannot delete an SSL certificate that is associated with a listener or backend set. Remove the bundle from any listeners or backend sets before deleting.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/delete_certificate.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Load balancer certificates section.
The Load balancer managed certificates list opens. All Load Balancer service-managed certificates in the selected load balancer are displayed in a table.
- From the Actions menu for the certificate you want, select Delete .
- When prompted, confirm the deletion.
- 

Use the[oci lb certificate delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/delete.html)command and required parameters to delete a load balancer's certficate:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteCertificate](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/DeleteCertificate)
