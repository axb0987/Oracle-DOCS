# Getting a Load Balancer Cipher Suite's Details
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Viewing_Cipher_Suite_Details.htm
- Fetched: 2026-09-05 01:41 CDT

# Getting a Load Balancer Cipher Suite's Details

View the details of a cipher suite for a load balancer.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Viewing_Cipher_Suite_Details.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Viewing_Cipher_Suite_Details.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Viewing_Cipher_Suite_Details.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Cipher suites section.
- On the cipher suite's list, select the cipher suite that you want to work with.
The cipher suite's details page opens and displays information about the cipher set, including the ciphers contained in it and whether the cipher suite is predefined or custom. You can also manage the ciphers contained in the cipher suite.
- 

Use the[oci lb ssl-cipher-suite get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/get.html)command and required parameters to view the details of a cipher suite for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/GetSSLCipherSuite)
