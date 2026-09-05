# Creating a Load Balancer Listener
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer Listener

Create a listener to check for incoming traffic on the load balancer's IP address.

For prerequisite information, see[Listeners for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm#)
- 

- On the Load balancers list page, select the load balancer that you want to work with. If you need help finding the list page or the load balancer, see[Listing Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/list_load_balancer.htm).
- On the load balancer's details page, select Listeners .
- In the Listeners section, select Create listener .
- From the Create listener panel, enter the following information:

- Name : Enter a friendly name for the listener. The name must be unique, and can't be changed.
- Hostname : (Optional) Select up to 16 virtual hostnames for this listener.
Note  
  
To apply a virtual hostname to a listener, the name must be part of the load balancer's configuration. If the load balancer has no associated hostnames, you can create one on the Hostnames page. See[Virtual Hostnames for Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/hostname_management.htm)for more information.
- Protocol : Specify the protocol to use:
- HTTPS
- HTTP
- HTTP/2
- gRPC
- TCP
- Port : Specify the port on which to listen for incoming traffic.
- Use SSL : (Required for HTTP/2, HTTPS, and gRPC. Optional for HTTP and TCP) Select to enable. The following settings are required to associate an SSL certificate bundle with the listener to enable SSL handling. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information on using SSL certificates with load balancers.

The load balancer automatically detects changes and consumes the current version of the Certificates service entities (certificates, certificate authorities, and CABundles) for use in SSL configuration. See[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm)for more information on automated certificate rotations.
- Certificate resource : Select the certificate resource type from the list:

The method of importing the certificate varies depending on the certificate resource type you select.
- Certificate service managed certificate : Select the certificate in the specified compartment from the Certificate list.

Advanced options are available with this selection. Select Show advanced options and select the Advanced SSL tab. This option is described later in this topic.
- Load balancer managed certificate : Select one of these options to import the certificate:

Choose SSL certificate file : Drag the certificate file, in PEM format, into the SSL certificate field. You can also select the Paste SSL certificate option to paste a certificate directly into this field. If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.

Specify private key : (Required for SSL termination, optional for all else) Select box to provide a private key for the certificate.

Choose private key file : Drag the private key, in PEM format, into the Private key field. You can also select the Paste private key option to paste a private key directly into this field.

Enter private key passphrase : (Optional) Specify the private key passphrase.

Verify peer certificate : (Optional) Select this option to enable peer certificate verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information. Mutual TLS (mTLS) isn't supported for communication between a load balancer and its backend servers. You can use mTLS for communication between load balancers and users.

Verify depth : (Optional) Specify the maximum depth for certificate chain verification. See[SSL Certificates for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information.
- Enable session resumption : Select to resume the previous encryption session rather than complete a new SSL connection before each request. Enabling session resumption improves performance but provides a lower level of security. Deselect the feature to force a new SSL connection before each request. Disabling session resumption improves security but reduces performance.
- Backend set : Specify the default backend set to which the listener routes traffic.
- Idle timeout in seconds : (Optional) Specify the maximum idle time in seconds. This setting applies to the time allowed between two successive receive or two successive send network input/output operations during the HTTP request-response phase. The maximum value is 7200 seconds. For more information, see[Load Balancer Timeout Connection Settings](https://docs.oracle.com/iaas/Content/Balance/Reference/connectionreuse.htm).
- (Optional) Select Proxy Protocol to enable and configure proxy protocol on the load balancer. See[Proxy Protocol](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer.htm#proxy-protocol)for more information on this feature. Select which proxy protocol version you want to use:
- Version 1 : Supports a human-readable header (text) format and is typically a single line of a log entry. Use this option for debugging during the early adoption stage when few implementations exist.
- Version 2 : Combines support for the human-readable header from Version 1 with a binary encoding of the header for greater efficiency in producing and parsing. Use this option for IPv6 addresses, which are difficult to generate and parse in ASCII form. Version 2 also better supports custom extensions. By default, PP2 Type Authority is selected as the only Version 2 option available.
- Select either a Routing policy or a Path route set .
- Routing policy : (Optional) Specify the name of the routing policy that applies to this listener's traffic.
- Path route set : (Optional) Specify the name of the set of path-based routing rules that applies to this listener's traffic.

To apply a[path route set](https://docs.oracle.com/iaas/Content/Balance/Tasks/path-route-set_management.htm)to a listener, the path route set must be part of the load balancer's configuration.

To remove a path route set from an existing listener, select None as the Path Route Set option. The path route set remains available for use by other listeners on this load balancer.
- Rule sets : (Optional) Select a[rule set](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm)to apply to this listener's traffic. To apply a rule set to a listener, the set must be part of the load balancer's configuration. To remove a rule set from the list, clear the corresponding box. The rule set remains available for use by other listeners on this load balancer.
- Select Create listener .
- 

Use the[oci lb listener create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/listener/create.html)command and required parameters to create a listener for a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateListener](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Listener/CreateListener)
