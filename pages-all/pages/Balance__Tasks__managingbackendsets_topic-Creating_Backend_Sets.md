# Creating a Load Balancer Backend Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer Backend Set

Create logical entities consisting of a load balancing policy, health check policy, and a list of backend servers for a load balancer.

For prerequisite information, see[Backend Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Creating_Backend_Sets.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Backend sets .
The Backend sets tab opens. All backend sets in the selected load balancer are displayed in a table.
- Select Create backend set .
- Enter the following information:

- Name : Enter a friendly name for the backend set. It must be unique within the load balancer, and it can't be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names can't contain spaces.
- Traffic distribution policy : Choose the load balancer policy for the backend set. The available options are:
- IP hash
- Least connections
- Weighted round robin

You can't add a backend server marked as Backup to a backend set that uses the IP Hash policy. For more information on these policies, see[Load Balancer Policies](https://docs.oracle.com/iaas/Content/Balance/Reference/lbpolicies.htm).
- Use SSL
Enable to associate an SSL certificate resource with the backend set.

The load balancer automatically detects changes and consumes the current version of the Certificates service entities (certificates, certificate authorities, and CA Bundles) for use in SSL configuration. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on automated certificate rotations.

If no certificate resources attached to the load balancer exist, this option is disabled.
Note  
  
If you check Use SSL , the SSL Policies fields appear at the bottom of the page under Show advanced SSL options .

Enter the following information:
- Certificate resource : Select the certificate resource type from the list:

The method of importing the certificate varies depending on the certificate resource type you select. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for information on how load balancers use SSL certificates.

See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for general information on using SSL with your web application firewall policy.
- Certificate service managed certificate

Select the CA bundle or Certificate authority option, and then select your choice from the associated list.

Advanced options are available with this selection. Select Show advanced options and select the Advanced SSL tab. This option is described later in this topic.
- Load balancer managed certificate : Select one of these options to import the certificate:

Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field. You can also select the Paste SSL certificate option to paste a certificate directly into this field.

If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.

Specify private key : (Required for SSL termination.) Select to provide a private key for the certificate.

Choose private key file : Drag the private key, in PEM format, into the Private key field.

Enter private key passphrase : Specify the private key passphrase. Alternatively, you can choose the Paste private key option to paste a private key directly into this field.

Verify peer certificate : Select to enable peer certificate verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.

Verify depth : Specify the maximum depth for certificate chain verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.
- Session persistence
Specify how the load balancer manages session persistence. See[Load Balancer Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm)for information on configuring these settings.

Enter the following information:
- Disable session persistence : Select to disable cookie-based session persistence.
- Enable application cookie persistence : Select to enable persistent sessions from a single logical client when the response from a backend application server includes a`Set-cookie`header with the cookie name you specify.
- Cookie name : The cookie name used to enable session persistence. Specify * to match any cookie name.
- Disable fallback : Select to disable fallback when the original server is unavailable.
- Enable load balancer cookie persistence : Select to enable persistent sessions based on a cookie inserted by the load balancer.
- Cookie name : Specify the name of the cookie used to enable session persistence. If blank, the default cookie name is`X-Oracle-BMC-LBS-Route`.

Ensure that any cookie names used at the backend application servers are different from the cookie name used at the load balancer.
- Disable fallback : Select to disable fallback when the original server is unavailable.
- Domain name : Specify the domain in which the cookie is valid.

This attribute has no default value. If you don't specify a value, the load balancer doesn't insert the domain attribute into the`Set-cookie`header.
- Path : Specify the path in which the cookie is valid. The default value is`/`.
- Expiration period in seconds : Specify the amount of time the cookie remains valid. If blank, the cookie expires at the end of the client session.
- Attributes

Secure : Specify whether the`Set-cookie`header contains the`Secure`attribute. If selected, the client sends the cookie only using a secure protocol.

If you enable this setting, you can't associate the corresponding backend set with an HTTP listener.

HTTP only : Specify whether the`Set-cookie`header contains the`HttpOnly`attribute. If selected, the cookie is limited to HTTP requests. The client omits the cookie when providing access to cookies through non-HTTP APIs such as JavaScript channels.
- Health check
Specify the test parameters to confirm the health of backend servers.

Enter the following information:
- Protocol : Specify the protocol to use, either HTTP or TCP. Configure your health check protocol to match your application or service. See[Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm)for more information.
- Port : (Optional) Specify the backend server port against which to run the health check. You can enter the value 0 to have the health check use the backend server's traffic port.
- Force plaintext health checks : (HTTP only) (Optional) Check to send the health check to the backend server without SSL. This option is only available when the backend server has its protocol is set to HTTP. It has no effect when the backend server doesn't have SSL enabled. When SSL is disabled, health checks are always plaintext.
- Interval in milliseconds : (Optional) Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in milliseconds : (Optional) Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : (Optional) Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is '3.'
- Status code : (HTTP only) (Optional) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP only) Specify a URL endpoint against which to run the health check.
- Response body regex : (HTTP only) (Optional) Provide a regular expression for parsing the response body from the backend server.
- Max backend connections
Specify a value within the range of 256–65535 connections.

Setting a limit on the maximum number of backend server connections for this backend set specifies the default maximum connections value for all backend servers in the backend set. Individual backend servers in the backend set can have their own maximum connections value which overrides this default value.
- Advanced SSL options
You can select Show advanced SSL options at the bottom of the page if you previously enabled Use SSL to associate an SSL certificate resource with the backend set.
- Advanced SSL : (HTTP and TCP only) Select a CA bundle or Certificate Authority for use with the listener. Then select CA bundle or Certificate Authority from the corresponding list. Change compartments if you can't find the item you want in your current compartment.

See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for information on how load balancers use SSL certificates.
- TLS version: : (Optional) Specify the Transport Layer Security (TLS) versions: 1.0 , 1.1 , 1.2 (recommended), and 1.3

You can select any combination of versions. Select the ones you want from the list. If you don't specify the TLS versions, the default TLS is version 1.2 only.

Select cipher suite : Select a set of cipher suites from the list. All choices present in the list have at least one cipher associated with each TLS version you selected.
- Show cipher suite details : Select to display what ciphers the selected cipher suite contains.
- Select Create backend set .
- 

Use the[oci lb backend-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/create.html)command and required parameters to create a load balancer's backend set:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/CreateBackendSet)
