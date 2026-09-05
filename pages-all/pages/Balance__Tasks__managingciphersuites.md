# Cipher Suites for Load Balancers
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites.htm
- Fetched: 2026-09-05 01:41 CDT

# Cipher Suites for Load Balancers

Use cipher suites with a load balancer to determine the security, compatibility, and speed of HTTPS traffic.

A cipher suite is a logical entity for a set of algorithms, or ciphers , using Transport Layer Security (TLS) to determine the security, compatibility, and speed of HTTPS traffic. All ciphers are associated with at least one version of TLS 1.0, 1.1, 1.2, and 1.3.
Note  
  
Any cipher suite you use or create must contain individual ciphers that match the TLS version supported in your environment. Some ciphers can work with several TLS versions. If your environment supports at least one of the TLS versions associated with a specific cipher, you can use it.

Assign at least one cipher to a cipher suite you create. You can't create a cipher suite that contains no ciphers.

When you create or edit a listener, you add or can change the associated cipher suite. There can only be one cipher suite attached to a listener at a time, which controls all allowable ciphers. The cipher suite attached to the listener must have all ciphers for which you require support. See[Listeners for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm)for more information.

Select Cipher Suites under Resources in the load balancer's Details page to display the Cipher suites page. This page contains a button for creating cipher suites.

This page also contains a list of all the available cipher suites, both ones that came originally preconfigured from Oracle Cloud Infrastructure ( Predefined=Yes ), and ones that you created yourself ( Predefined=No ). You can change or delete those cipher suites you created yourself . You can't change or delete predefined cipher suites.

Here is reference information for ciphers and cipher suites:

[Predefined cipher suites.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm)

[Deprecated cipher suites.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm#predefinedciphersuites)

[Supported ciphers.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Supported_Ciphers.htm)

[Deprecated ciphers.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Supported_Ciphers.htm#deprecated-ciphers)

You can perform the following cipher suite management tasks:

[List the cipher suites under a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list_ssl-cipher-suite.htm)

[Create a cipher suite for a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Creating_Cipher_Suites.htm)

[Get a cipher suite's details.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Viewing_Cipher_Suite_Details.htm)

[Edit a cipher suite's settings.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Editing_Cipher_Suites.htm)

[Delete a cipher suite from a load balancer.](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingciphersuites_topic-Deleting_Cipher_Suites.htm)

Note the following items related to cipher suites:
- Ensure compatibility between specified SSL protocols and configured ciphers in the cipher suite, or else the SSL handshake isn't successful.
- Ensure compatibility between configured ciphers in the cipher suite and configured certificates (for example, RSA-based ciphers require an RSA certificate whereas ECDSA-based ciphers require ECDSA certificates).
- For all load balancer and listener resources that were created before the cipher suites feature was available, the following apply:
- When running a GET operation, the cipher suite value returned is by default "oci-default-ssl-cipher-suite-v1" inside the listener's SSL configuration. You can update this value by editing the load balancer or listener.
- When running a GET operation, the cipher suite value returned is displayed as "oci-customized-ssl-cipher-suite" inside the listener's SSL configuration if the cipher configuration customized after the load balancer creation through Oracle operations.
- For all existing load balancer backendsets that were created before the cipher suites feature was available, running a GET operation displays the cipher suite value as "oci-wider-compatible-ssl-cipher-suite-v1" inside the backendset's SSL configuration.
- If running a GET operation on a load balancer listener displays the cipher suite value as "oci-customized-ssl-cipher-suite," then select the appropriate cipher suite name (either pre-defined or custom defined cipher suites) when updating these load balancers.
- The cipher suite name "oci-customized-ssl-cipher-suite" is reserved for use by Oracle and isn't acceptable as an available name for a custom cipher suite.

## Cipher Suites in Listeners and Backend Sets

When you create a load balancer, specifying the cipher suite is part of configuring the listener and the backend set. See[Creating a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm)for more information.

If you plan to use TLS v1.3 protocol with either a backend set or a listener on the same load balancer, you can't use the predefined cipher suite`oci-wider-compatible-ssl-cipher-suite-v1`or any custom cipher suites that contains any of the following deprecated ciphers:
- DHE-DSS-AES128-GCM-SHA256
- DHE-DSS-AES128-SHA256
- DHE-DSS-AES256-GCM-SHA384
- DHE-DSS-AES256-SHA256
- ECDH-ECDSA-AES128-GCM-SHA256
- ECDH-ECDSA-AES128-SHA256
- ECDH-ECDSA-AES256-GCM-SHA384
- ECDH-ECDSA-AES256-SHA384
- ECDH-RSA-AES128-GCM-SHA256
- ECDH-RSA-AES128-SHA256
- ECDH-RSA-AES256-GCM-SHA384
- ECDH-RSA-AES256-SHA384
- IDEA-CBC-SHA
-
