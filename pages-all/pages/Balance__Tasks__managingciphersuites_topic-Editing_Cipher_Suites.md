# Editing a Load Balancer Cipher Suite
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm
- Fetched: 2026-09-05 01:41 CDT

# Editing a Load Balancer Cipher Suite

Update a cipher suite's configuration for a load balancer.
Note  
  
You can't edit a predefined ( Predefined=Yes ) cipher suite. You can only edit a custom ( Predefined=No ) cipher suite.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Cipher suites section.
- From the Actions menu for the cipher suite, select Edit .
- From the Manage ciphers panel, select or clear those ciphers you want to add or remove from the cipher. You can select the TLS versions of the ciphers you include from the TLS verion list.

Note  
  
You can't delete all ciphers from a cipher suite. The cipher suite must contain at least one cipher after editing.
- Select Save changes .
- 

Use the[oci lb ssl-cipher-suite update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/update.html)command and required parameters to update a cipher suite's configuration for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/UpdateSSLCipherSuite)
