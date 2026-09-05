# Creating a Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm
- Fetched: 2026-09-05 01:41 CDT

# Creating a Load Balancer

Create a load balancer to provide automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network (VCN).

For prerequisite information, see[Load Balancer Management](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Creating_Load_Balancers.htm#)
- 

On the Load balancers list page, select Create load balancer . If you need help finding the list page, see[Listing Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/list-load-balancer.htm).

Creating a load balancer consists of the following pages:
- 1. Add details
- 2. Choose backends
- 3. Configure listener
- 4. Manage logging
- 5. Review and create

Run each of the following workflows in order. You can return to a previous page by selecting Previous .

## 1. Add details

The Add details page is where you provide the basic information for the load balancer.

Enter the following information:
- Load balancer name : Accept the default name or enter a friendly name for the load balancer. The name doesn't have to be unique, but it can't be changed in the Console. You can, however, change it with the API.
- Choose visibility type : Select one of the following options:
- Public : Create a public load balancer. You can use the assigned public IP address as a front end for incoming traffic and to balance that traffic across all backend servers. When you select the public IP address option, you're also prompted to select and complete the public IP address type.
- Private : Create a private load balancer. You can use the assigned private IP address as a front end for incoming internal VCN traffic and to balance that traffic across all backend servers.
- Assign a public IP address : (Public only) When you choose to create a public load balancer, select one of the following options. For more information, see[Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
- Ephemeral IP address : Let Oracle specify an ephemeral IP address for you from the Oracle IP pool. This option is the default.
- Reserved IP address : Specify an existing reserved IP address by name and compartment, or create a new reserved IP address by assigning a public IP name and selecting a source IP pool for the address. If you don't select a user-created pool, the default Oracle IP pool is used.
- Assign a private IP address : (Private only) When you choose to create a private load balancer, select one of the following options. For more information, see[Private IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm).
- Ephemeral private IP address : Let Oracle specify an ephemeral IP address for you from the Oracle IP pool. This option is the default.
- Reserved private IP address : Specify an existing reserved IP address by selecting it from the drop down menu, or create a new reserved IP address by assigning a private IP name and specifying the IP you want to reserve.

### Bandwidth

For the load balancer's bandwidth, select Flexible shapes . Dynamic shapes are deprecated and we don't recommend using them.
- Minimum bandwidth and Maximum bandwidth : Select values to create an upper and lower size range for the load balancer's bandwidth shape. Possible sizes range from 10 Mbps to 8,000 Mbps.
- The minimum bandwidth reflects the amount of bandwidth that's always available to provide instant readiness for the workloads.
- The maximum bandwidth is the upper amount of bandwidth the load balancer supports during time of peak workload.

To specify a fixed shape size, for example 500 Mbps, set the minimum and maximum sliders to the same value.

If you're creating the load balancer as a paid account user, you can create various shape options based on your limits and later adjust the bandwidth by changing the shape after the load balancer has been created. You can view your service limits and quotas in the Console by navigating to Governance &amp; Administration &gt; Limits, Quotas and Usage . Select "LbaaS" from the Service list. The bandwidth size options are listed. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).

Billing is per minute for your load balancer base instance, plus a bandwidth usage fee.
- If the actual usage is less than or equal to your specified minimum bandwidth, you're billed for the minimum bandwidth.
- If actual usage exceeds the minimum bandwidth, you're billed for the actual bandwidth used for that minute.

The Always Free option is incorporated into your paid account in your home region. The first 10 Mbps of your bandwidth is free, and is indicated as such on your bill.
Note  
  
Government accounts using prepaid dynamic (fixed) shape sizes run the risk of overage charges when flexible bandwidth shapes exceed the predetermined size. Update government accounts to the load balancer SKU, with the appropriate bandwidth quantity, in their contract before using the load balancer feature.

If you're using non-universal credit SKUs, ensure that your contract includes the shape you're updating to so you can prevent incurring overage charges.

You can adjust the bandwidth shape to a different size after you have completed creating the load balancer. See[Changing a Load Balancer's Bandwidth Shape](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm).
- Enable IPv6 address assignment : Select this checkbox if the load balancer supports IPv6 addresses for incoming requests. For more information about Oracle Cloud Infrastructure's IPv6 implementation, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).

When you create a load balancer, you can optionally choose to have an IPv4/IPv6 dual-stack configuration. When you choose the IPv6 option, the Load Balancing service assigns both an IPv4 and an IPv6 address to the load balancer. The load balancer receives client traffic sent to the assigned IPv6 address. The load balancer uses only IPv4 addresses to communicate with backend servers. The load balancer and the backend servers don't use IPv6 communication.
- Enable IPv6 address assignment : Select this checkbox if the load balancer supports IPv6 addresses for incoming requests. For more information about Oracle Cloud Infrastructure's IPv6 implementation, see[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).

When you create a load balancer, you can optionally choose to have an IPv4/IPv6 dual-stack configuration. When you choose the IPv6 option, the Load Balancing service assigns both an IPv4 and an IPv6 address to the load balancer. The load balancer receives client traffic sent to the assigned IPv6 address. The load balancer uses only IPv4 addresses to communicate with backend servers. The load balancer and the backend servers don't use IPv6 communication.

You can assign an IPv6 address for listener support when creating the load balancer. You can also update an IPv4-only load balancer to support dual stack listeners using the CLI. Run the[oci lb load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/update.html)command with the`ip-mode`parameter set to`IPV6`. You can also use run the[UpdateLoadBalancer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/update.html)operation with the`ipMode`parameter set to`IPV6`. For more information, see[Editing a Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Editing_Load_Balancers.htm).

### Choose networking

If the current compartment contains at least one VCN, the Console provides a list of VCNs from which to select. Change the compartment as needed to find the VCN that you want to use.
- Virtual cloud network compartment : Select the compartment that contains the VCN that you want to use for the load balancer.
- Virtual cloud network : Select the VCN that you want to use for the load balancer.
- Subnet compartment : Select an available subnet. For a public load balancer, it must be a public subnet. In addition to public or private , subnets can be either regional or AD-specific . We recommend using regional subnets. See[Overview of VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm).
- Subnet (2 of 2) : Required for a public load balancer when you specify an AD-specific subnet for Subnet and the region that you're working in contains more than one Availability domain. Select a second public subnet. The second subnet must reside in a separate Availability domain from the first subnet.
Note  
  
To create a VCN in a compartment that doesn't already contain on, the system offers to create a VCN for you. You can optionally enter a friendly name for the new VCN. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). If you don't specify a name for the new VCN, the system generates a name for you.
- Use network security groups to control traffic : Select to add your load balancer to a network security group (NSG). See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm). By default, the Console shows a list of NSGs in the compartment you're working in. Change compartments to select an NSG from a different compartment. Then, select the NSG. You can select more than one NSG. You can change the NSGs that your load balancer belongs to after you create it.

### Security

- Use a web application firewall policy to protect against layer 7 attacks : Select to apply web application firewall policies to the load balancer as a safeguard against attack.
- Assign in region web application firewall policy : Select a web application firewall policy available in the current compartment from the list. Change compartments to access the web application firewall policies in a different compartment.

For more information about web application firewall policies, see[Overview of Web Application Firewall](https://docs.oracle.com/iaas/Content/WAF/Concepts/overview.htm).

### Acceleration

- Use a web application acceleration policy to speed up your performance : Select to apply web application acceleration policies to speed up your performance.
- Assign a web application acceleration policy : Select a web application firewall policy available in the current compartment from the list. Change compartments to access the web application acceleration policies in a different compartment.

For more information about web application acceleration policies, see[Web Application Acceleration](https://docs.oracle.com/iaas/Content/web-app-acceleration/home.htm).

### Management

- Create in compartment : Select the compartment for the load balancer.
- Prevent deletion of the load balancer, listeners and backends when they are still active : Select this checkbox to avoid accidentally deleting a load balancer, or a listener or backend server contained in a load balancer, when they're configured to accept traffic.
- Load balancers are configured to accept traffic when they contain listeners that are configured to accept traffic.
- Listeners are configured to accept traffic when they reference a backend set with backend servers that are configured to accept traffic.
- Backend servers are configured to accept traffic when they're in a backend set referenced by a listener and the backend server is neither drained nor offline.

### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

### Security attributes

Select Show security attributes . Select the Add security attributes button.

Enter the following information:
- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. See[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm)for more information.
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.

Select the Add security attribute button to add another attribute (to a maximum of three).

### Dynamic shapes (deprecated)

The following describes the dynamic shapes feature, which is only available to certain legacy customer accounts:

Dynamic shapes : Select one of the following predefined shape sizes:
- 10 Mbps
- 100 Mbps
- 400 Mbps
- 8,000 Mbps

If you're creating the load balancer as a paid account user, you can create various shape options based on your limits and later adjust the bandwidth by changing the shape after the load balancer has been created. You can view your service limits and quotas in the Console by navigating to Governance &amp; Administration &gt; Limits, Quotas and Usage . Select LbaaS from the Service list. Your bandwidth size options are listed. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm).

You can adjust the bandwidth shape to a different size after you have completed creating the load balancer. See[Changing a Load Balancer's Bandwidth Shape](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Changing_the_Load_Balancer_Bandwidth.htm).

If you adjust a dynamic size value to a flexible size using the sliders, you can't revert to a dynamic shape of any size. You can achieve the effect of having a dynamic (fixed) size by setting the minimum and maximum sliders to the same size.

Select Next .

## 2. Choose backends

The Choose backends page is where you set up your backend servers and backend sets.

A load balancer distributes traffic to backend servers within a backend set. A backend set is a logical entity defined by a load balancing policy, a list of backend servers (compute instances), and a health check policy. The load balancer creation workflow creates one backend set for your load balancer. Optionally, you can add backend sets and backend servers after you create the load balancer. See[Backend Sets](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets.htm)and[Backend Servers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendservers.htm)for more information on these features.

Enter the following information:

### Load balancing policy

Select the load balancer policy to use for the backend set:
- Weighted round robin : (Default) Distributes incoming traffic sequentially to each server in a backend set list. After each server has received a connection, the load balancer repeats the list in the same order. Round robin is a basic load balancing algorithm. It works best when all the backend servers have similar capacity and the processing load required by each request doesn't vary much.
- IP hash : Ensures that requests from a particular client are always directed to the same backend server. The load balancer routes requests from the same client to the same backend server as long as that server is available. This policy honors server weight settings when establishing the initial connection. You can't add a backend server marked as Backup to a backend set that uses the IP hash policy.
- Least connections : Routes incoming request traffic to the backend server with the fewest active connections. This policy helps you maintain an equal distribution of active connections with backend servers. As with the round robin policy, you can assign a weight to each backend server and further control traffic distribution.

For more information on these policies, see[Load Balancer Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/lbpolicies.htm).

### Backend servers

Specify one or more backend servers to use for the load balancer. You can add more after you create the load balancer, if needed.

- Select the compartment that contains the compute instance that you want to use as a backend server. You can select instances from only one compartment at a time.
- Select Add instance .
- In the Add backends panel, select the instances that you want to include in the load balancer's backend set. You can't add a backend server marked as Backup to a backend set that uses the IP hash policy.
- Select Add instances .
- To add instances from another compartment, select that compartment and repeat the preceding steps.

After you add instances to the backend set, they appear in the Select backend servers table. You can perform the following actions:
- Specify the server port to which the load balancer must direct traffic. The default is port 80.
- From the Action menu for a backend server, select Delete to remove it from the backend set.

### Health check policy

Specify the test parameters that confirm the health of your backend servers:
- Protocol : Specify the protocol to use for health check queries, either HTTP or TCP. Configure your health check protocol to match your application or service. See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/load_balancer_health_management.htm).
- Port : Specify the backend server port against which to run the health check. You can enter the value "0" to have the health check use the backend server's traffic port.
- Force plaintext health checks : (HTTP only) Select to send the health check to the backend server without SSL. This option is only available when the backend server has its protocol is set to HTTP. It has no effect when the backend server doesn't have SSL enabled. When SSL is disabled, health checks are always plaintext.
- Interval in ms : Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in ms : Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : Specify the number of retries before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is 3.
- Status code : (HTTP only) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP only) Specify a URL endpoint against which to run the health check.
- Response body regex : (HTTP only) Provide a regular expression for parsing the response body from the backend server.

### SSL

Select to apply SSL to the load balancer backend. If you select this option, complete the following. If the best security is required, it's your responsibility to always use HTTPS for traffic between the load balancer and the backend set. Enter the following information:
- Certificate resource : Select one of these options from the list:
- Load balancer service managed certificate : Select the CA bundle or Certificate authority option, and then select your choice from the associated list. Select Change compartment to select a different compartment from which to select the CA bundle or certificate authority.
- Load balancer management certificate : Select one of the following:
- Choose SSL certificate file : Drag the certificate file into the SSL certificate field. You can also select Select Files and navigate your system to where you can select the certificate file for upload. Certificate files must be in PEM format and must have the`.pem`,`.cer`, or`.crt`file extensions.

If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
- Paste SSL certificate : Copy and paste a certificate directly into this field.
- Specify CA certificate: (Recommended for backend SSL termination configurations.) Select to provide a CA certificate. See[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm).
- Choose private key file : Drag the private key, in PEM format, into the Private key field. You can also select the Paste private key option to paste a private key directly into this field.
- Enter private key passphrase : Specify the private key passphrase.

### Backend set

Enter a name for the backend set. It must be unique within the load balancer, and it can't be changed. If you don't specify a name, the Load Balancer service creates one for you. Use only alphanumeric characters, dashes ("-"), and underscores ("_") for backend set names. Backend set names can't contain spaces.

### Max backend connections

- Set limit : Toggle to set a limit to the number of active backend connections at a time. Setting a limit on the maximum number of backend server connections for this backend set specifies the default maximum connections value for all backend servers in the backend set. Individual backend servers in the backend set can have their own maximum connections value which overrides this default value. See[Editing a Backend Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingbackendsets_topic-Editing_Backend_Sets.htm)for more information.
- Max backend connections : Specify the maximum number of connections in the box. You must specify value within the range of 256–65535 connections.

### Security list

Select whether to manually configure subnet security list rules to allow the intended traffic, or to allow the system to create security list rules for you. To learn more about these rules, see[Parts of a Security Rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).
- Manually configure security list rules after the backend servers are added : When you select this option, you must configure security list rules after you add the backend servers.
- Automatically add security list rules : When you select this option, the Load Balancer service creates security list rules for you. The system displays a table for the Egress security list and the Ingress security list . Each table lets you select the security list that applies to the relevant subnet. You can select whether to apply the proposed rules for each affected subnet.

### Session persistence

Specify how the load balancer manages session persistence. See[Load Balancer Session Persistence](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/sessionpersistence.htm)for important information on configuring these settings.
- Disable session persistence : Select this option to disable cookie-based session persistence.
- Enable application cookie persistence : Select this option to enable persistent sessions from a single logical client when the backend application server response includes a`Set-cookie`header with the cookie name you specify.
- Cookie name : The cookie name used to enable session persistence. Specify * to match any cookie name.
- Disable fallback : Select to disable fallback when the original server is unavailable.
- Enable load balancer cookie persistence : Select this option to enable persistent sessions based on a cookie inserted by the load balancer.
- Cookie name : Specify the name of the cookie used to enable session persistence. If blank, the default cookie name is`X-Oracle-BMC-LBS-Route`. Ensure that any cookie names used at the backend application servers are different from the cookie name used at the load balancer.
- Disable fallback : Select to disable fallback when the original server is unavailable.
- Domain name : Specify the domain in which the cookie is valid. This attribute has no default value. If you don't specify a value, the load balancer doesn't insert the domain attribute into the`Set-cookie`header.
- Path : Optional. Specify the path in which the cookie is valid. The default value is`/`.
- Expiration period in seconds : Specify the amount of time the cookie remains valid. If blank, the cookie expires at the end of the client session.
- Secure : Specify whether the`Set-cookie`header must contain the`Secure`attribute. If selected, the client sends the cookie only using a secure protocol. If you enable this setting, you can't associate the corresponding backend set with an HTTP listener.
- HTTP only : Specify whether the`Set-cookie`header must contain the`HttpOnly`attribute. If selected, the cookie is limited to HTTP requests. The client omits the cookie when providing access to cookies through non HTTP APIs such as JavaScript channels.

Select Next .

## 3. Configure listener

The Configure listener page is where you set up the listener for the load balancer.

A listener is a logical entity that checks for incoming traffic on the load balancer's IP address. To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type. When you create a listener, you must ensure that your VCN's[security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)allow the listener to accept traffic.

Enter the following information:
- Listener name : Enter a name for the listener. The name must be unique, and can't be changed. If you don't specify a name, the Load Balancer service creates one for you.
- Specify the type of traffic your listener handles : Select the type of traffic your listener handles from the list:
- HTTPS
- HTTP
- HTTP/2
- gRPC
- TCP
Note  
  
Listeners support HTTP 1.0, HTTP 1.1 and HTTP 1.2 traffic. However, communication between the load balancer and its listeners support only HTTP 1.1 and HTTP 1.2. Incoming HTTP 1.0 traffic is proxied to the backend servers as HTTP 1.1 traffic.
- Specify the port your listener monitors for ingress traffic : Specify the port your listener monitors for ingress traffic. Following are the default values:
- 443 for HTTPS
- 80 for HTTP
- 443 for HTTP/2
- 443 for gRPC
- 22 for TCP

### SSL certificate

If you chose the HTTPS, HTTP/2, or gRPC protocols, or if you chose the TCP protocol and selected Use SSL , specify certificate information. If best security is required, it's your responsibility to always use HTTPS for traffic between the load balancer and the backend set.

Select one of the following options for Certificate resource :
- Certificate service managed certificate : This option uses the Oracle Cloud Infrastructure Certificates service to manage the certificate used by the load balancer. See[Overview of Certificates](https://docs.oracle.com/iaas/Content/certificates/overview.htm)for more information.
Note  
  
We recommend you use the Certificates service for creating and managing certificates for use in load balancers.

Select the CA bundle or Certificate authority option, and then select your choice from the associated list.
- Load balancer management certificate : This option uses the SSL certificate feature that's part of the Load Balancer service. See[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingcertificates.htm)for more information. Select one of the following options:
- Certificate resource : Drag or upload the certificate file into the SSL certificate field. Certificate files must be in PEM format and must have the`.pem`,`.cer`, or`.crt`file extensions.

You can also copy and paste the certificate content directly into this box.

If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
- Specify CA certificate : (Recommended for backend SSL termination configurations.) Drag or upload the certificate authority file into the CA certificate field. CA certificate files must be in PEM format and must have the`.pem`,`.cer`, or`.crt`file extensions.

You can also copy and paste the CA certificate content directly into this box.
- Specify private key : Drag or upload the private key file, in PEM format, into the Private key box.

You can also copy and paste the private key contents directly into this box.

As an option, you can specify the private key passphrase in the Enter private key passphrase box:
- Enable session resumption : Select to resume the previous encryption session rather than complete a new SSL connection before each request. Enabling session resumption improves performance but provides a lower level of security.

Clear the feature to force a new SSL connection before each request. Disabling session resumption improves security but reduces performance.
- 
Use SSL : Select to apply SSL to the load balancer backend. If you select this option, complete the following. If optimal security is required, it's your responsibility to always use HTTPS for traffic between the load balancer and the backend set.

### SSL policy

(HTTPS, HTTP/2, and gRPC only) Configure the type of cipher suite to use:
- TLS version : Specify the Transport Layer Security (TLS) versions: 1.0 , 1.1 , 1.2 , 1.3

We recommend 1.2 . You can select any combination of versions. The HTTP/2 protocol only supports TLS 1.2 and TLS 1.3.
- Select cipher suite : To use a predefined set of cipher suites, select this option and then select the cipher suite to use. All listed cipher suites have at least one cipher from each of the TLS versions you selected. The HTTP/2 protocol only supports a default cipher. You can't change it.
- Create custom cipher suite : To add ciphers to a new suite, select this options and perform the following steps:
- Enter the name of the customer cipher suite in the Suite name field.
- Select the Select ciphers button.
- In the Select ciphers panel, select each cipher that you want to include in the suite. The TLS versions associated with each cipher are listed in the Version column. Ensure that any cipher you select is compatible with the TLS versions you previously chose. Assign at least one cipher to a cipher suite you create. You can't create a cipher suite that contains no ciphers.
- Clear any ciphers you want to exclude.
- Select the Select ciphers button.
- Show cipher suite details : Select to display what ciphers the selected cipher suite contains.
- Server order preference : Enable to give preference to the server ciphers over the client.

### Advanced SSL

(HTTP and TCP only) Select a CA bundle or Certificate Authority for use with the listener. Then select CA bundle or Certificate Authority from the corresponding list. Change compartments if you can't find the item you want in your current compartment.

### Timeout

Specify the maximum idle time in seconds. The maximum value is 7200 seconds. For more information, see[Load Balancer Timeout Connection Settings](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/connectionreuse.htm).

### Proxy protocol

Enable and configure proxy protocol on the load balancer. For more information, see[Proxy Protocol](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer.htm#proxy-protocol).

- Select Enable Proxy Protocol .
- Select which proxy protocol version you want to use:

- Version 1 : Supports a human-readable header (text) format and is typically a single line of a log entry. Use this option for debugging during the early adoption stage when few implementations exist.
- Version 2 : Combines support for the human-readable header from Version 1 with a binary encoding of the header for greater efficiency in producing and parsing. Use this option for IPv6 addresses, which are difficult to generate and parse in ASCII form. Version 2 also better supports custom extensions. By default, PP2 Type Authority is selected as the only Version 2 option available.

Select Next .

## 4. Manage logging

The Manage logging page is where you set up error and access logging.

Enabling error and access logs are optional, but recommended. Reviewing these logs can help you with diagnosing and fixing issues with your backend servers. Standard limits, restrictions, and rates apply when enabling the logging feature. See[Logging for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Logging.htm)for general information on how the Load Balancer service uses logging. For more information on log and log groups, including naming syntax guidelines, see[Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm).
Note  
  
Error logging is enabled by default. Disable this feature if you don't want to pay the associated fees.

Enter the following information:
- Error logs
- Enable : Toggle to enable logging. Logging is enabled by default.
- Compartment : Select the compartment within which the log file resides from the list.
- Log group : Select an existing log group from the list or select Create New Group where you can enter the name and description of a new logging group within which your log resides.
- Log name : Enter the name of the log.
- Log retention : Select the time period in months each error logging entry is to be retained from the list.
- Access logs
- Enable : Toggle to enable logging. Access logging is disabled by default.
- Compartment : Select the compartment within which the log file resides from the list.
- Log group : Select an existing log group from the list or select Create New Group where you can enter the name and description of a new logging group within which your log resides.
- Log name : Enter the name of the log.
- Log retention : Select the time period in months each error logging entry is to be retained from the list.
- Request ID

The Request ID can help you with tracking and managing a request by providing a unique request identifier exposed in HTTP request and response headers.

To use a request ID, switch the toggle to Enabled . The default header name`X-Request-Id`is included in the HTTP request header from the load balancer to the backend and HTTP header responses. If not enabled, the load balancer won't add this unique request ID header to the request passed through to the load balancer backend or to the response returned. You can enter a different header name instead of using the default. Any custom header name must start with "`X-`".

See[Load Balancer Headers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/../Reference/httpheaders.htm)for more information.

Select Next .

## 5. Review and create

Review the contents of the Review and create page. Edit settings or return to previous screens to add information. When the settings are fully verified, select Submit .

The load balancer you created appears in the Load balancer list page.
- 

Use the[oci lb load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/create.html)command and required parameters to create a load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/CreateLoadBalancer)
