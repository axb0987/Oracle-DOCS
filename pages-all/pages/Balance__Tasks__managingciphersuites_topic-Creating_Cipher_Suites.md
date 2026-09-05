# Creating a Load Balancer Cipher Suite
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Creating_Cipher_Suites.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer Cipher Suite

Create a cipher suite to determine the security, compatibility, and speed of HTTPS traffic for a load balancer.

Assign at least one cipher to a cipher suite you create. You can't create a cipher suite that contains no ciphers. For prerequisite information, see[Cipher Suites](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites.htm).

After you create a hostname, the name becomes available for use with the associated load balance. You can apply the hostname to a listener. See[Listeners](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Creating_Cipher_Suites.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Creating_Cipher_Suites.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Creating_Cipher_Suites.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Certificates and ciphers and find the Cipher suites section.
- In the Cipher suites section, select Create cipher suite .
- From the Create cipher suite panel, enter the following information:

- Suite name : Enter a name for the cipher suite.
- TLS version : Select those TLS versions from which you want to select your ciphers. Ciphers associated with the TLS versions you checked (displaying which TLS versions they support) appear. Only select TLS versions that are supported in your environment.
- Cipher : Select those ciphers that you want to include in your cipher suite. The total number of ciphers available can span several pages. Use the Search ciphers field to find a specific cipher. Clear a cipher to remove it from the cipher suite.
- Select Create suite .
- 

Use the[oci lb ssl-cipher-suite create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/create.html)command and required parameters to create a cipher suite for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/CreateSSLCipherSuite)
