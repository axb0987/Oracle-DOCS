# Deleting a Load Balancer Cipher Suite
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm
- Fetched: 2026-09-05 01:41 CDT

# Deleting a Load Balancer Cipher Suite

Remove a cipher suite from a load balancer.

You can't delete a cipher suite that's in use. Ensure all listeners and backend sets using the cipher suite you want to delete are managed to a different suite first. You might not have access to all compartments containing associated resources.
Note  
  
You can't delete a predefined ( Predefined=Yes ) cipher suite. You can only delete a custom ( Predefined=No ) cipher suite.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Cipher suites section.
- From the Actions menu for the cipher suite, select Delete .
- When prompted, confirm the deletion.
The cipher suite you deleted no longer appears in the Cipher suites list.
- 

Use the[oci lb ssl-cipher-suite delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/delete.html)command and required parameters to remove a cipher suite from a load balancer

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/DeleteSSLCipherSuite)
