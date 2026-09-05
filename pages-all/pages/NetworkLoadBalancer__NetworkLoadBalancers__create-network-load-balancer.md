# Creating a Network Load Balancer
- Source: https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm
- Fetched: 2026-09-05 02:48 CDT

# Creating a Network Load Balancer

Create a network load balancer to provide automated traffic distribution from one entry point to multiple servers in a backend set.

For prerequisite information, see[Network Load Balancer Management](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm#)
- 

On the Network load balancers list page, select Create network load balancer . If you need help finding the list page, see[Listing Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/list-network-load-balancer.htm).

Creating a network load balancer consists of the following pages:
- 1. Add details
- 2. Configure listener
- 3. Choose backends
- 4. Review and Create

Run each of the following workflows in order. You can return to a previous page by selecting Previous .

## 1. Add details

The Add details page is where you provide the basic information for the network load balancer.

Enter the following information:
- Network load balancer name : Enter a name for the network load balancer or accept the default name.
- Create in compartment : Select the compartment where the network load balancer you're creating resides.
- Choose visibility type : Select whether the network load balancer is public or private:
- Public : Select this option to create a public network load balancer. You can use the assigned public IP address as a front end for incoming traffic and to balance that traffic across all backend servers. The Public IP address can be either an ephemeral address assigned by Oracle or a reserved IP address you defined earlier.
- Private : Select this option to create a private network load balancer. You can use the assigned private IP address as a front end for incoming internal VCN traffic and to balance that traffic across all backend servers. Private network load balancers have the option of having header preservation enabled. For more information, see[Using the Console](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/create-network-load-balancer.htm#console).
- Allow IPv6 address assignment : Select to enable a dual-stack IPv4/IPv6 implementation for your network load balancer.
- Assign a public IP address : (Public only) Required if you selected the Public option for the network load balancer's visibility type. Select one of the following options:
- Ephemeral IPv4 address : Automatically assigns an IPv4 address from the Oracle pool. These IP addresses are temporary and only exist for the lifetime of the instance.
- Reserved IPv4 address : Select an existing reserved IP address or create a new one from one of your IP pools. These IP addresses are persistent and exist beyond the lifetime of the instance to which it's assigned. You can unassign the IP address and later reassign it to another instance at any point.
- Assign a private IP address : (Private only) Required if you selected the Private option for the network load balancer's visibility type. Select one of the following options:
- Ephemeral IPv4 address : Automatically assigns a private IPv4 address from the Oracle pool inside the VCN. These IP addresses are temporary and only exist for the lifetime of the instance.
- Reserved private IPv4 address : Select an existing reserved private IP address or create a new one. These IP addresses are persistent and exist beyond the lifetime of the instance to which it's assigned. You can unassign the IP address and later reassign it at any point.

### Header preservation

When you select the Private visibility type for your network load balancer, you have the option of enabling source/destination header preservation. This option lets you configure your private IP address network load balancer so that the original source and destination header (IP addresses and ports) of each incoming packet is preserved all the way to the backend server. For more information, see[Enabling Network Load Balancer Source/Destination Preservation](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm).

Source/destination header (IP, port) preservation affects all backend sets in the network load balancer. Update your route table to use this feature. For more information, see[VCN Route Tables](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

#### Symmetric hashing

When you enable source/destination header preservation, you have the option of enabling symmetric hashing. Network load balancers use symmetric hashing to calculate the same hash for packets belonging to the same flow in both forward and return directions. The hash doesn't change when the source IP address:port value is exchanged with the destination IP address: port value. Fore more information, see[Symmetric Hashing](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/preserve-source-id.htm#symmetric-hashing)for more information.

### Choose networking

If the current compartment contains one or more virtual cloud networks (VCNs) that you want to use with the network load balancer, skip to the next step.
- Virtual cloud network in &lt;compartment&gt; : Select a VCN from the list.

When the current compartment contains no virtual cloud networks, the list is disabled. The system offers to create a VCN for you. Enter a name for the new VCN in the Virtual cloud network name box. If you don't specify a name for the new VCN, the system generates a name for you.
- Subnet in &lt;compartment&gt; : Select a subnet from the list. For a public load balancer, you must select a public subnet.
- Use network security groups to control traffic : Select to add the network load balancer to a network security group (NSG). Complete the following steps:
- Network security groups in &lt;compartment&gt; : Select an NSG from the list.
- + Another network security group : Select to add the network load balancer to another NSG.

See[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).
Note  
  
You can change the NSGs that the network load balancer belongs to after you create it. On the Details page, select Edit beside the list of associated network security groups.

### Security

Apply security attributes to control access for your resources through the Zero Trust Packet Routing service. See[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm)for more information.
Note  
  
The number of security attributes you can configure for your network load balancer is limited. See[Limits](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/overview.htm#limits)for details.

Select Add security attribute to display the security attribute settings. Enter the following information for each security attribute:
- Namespace : Select a security attribute namespace from the list. This list contains those security attribute namespaces already configured. For more information, see[Creating a Security Attribute Namespace](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/create-security-attribute-namespace.htm).
- Key : Select a key from the list.
- Value : Select a value for the corresponding key from the list.
- Mode : You can apply security attributes to a network load balancer in the following modes:
- Enforce : Enforces security attribute policies and blocks any disallowed ingress or egress of traffic.

Select Add security attribute again to add another attribute.

### Tagging

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.

Select Next .

## 2. Configure Listener

The Configure listener page is where you set up the listener for the network load balancer.

A listener is a logical entity that checks for incoming traffic on the network load balancer's IP address. To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type. When you create a listener, you must ensure that your VCN's security rules allow the listener to accept traffic. For more information, see[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm).

Listener Name : Enter a unique name for the listener. If you don't specify a name, the Network Load Balancer service creates one for you. After the listener is created, you can't change its name.

Specify the type of traffic the listener handles : Specify the protocol to use from the following protocols:
- Public network load balancers:
- UDP
- TCP
- UDP/TCP
- L3 IP
- Private network load balancers
- UDP
- TCP
- TCP/UDP/ICMP : ICMP only supports network load balancers that have source/destination header preservation enabled.
- UDP/TCP
- L3 IP
Note  
  
When the L3 IP listener protocol is selected, the load balancer doesn't support 5-Tuple hash policies.

IP protocol version : Select from the following options:
- IPv4
- IPv6

This step is required if you enabled the IPv6 Address Assignment option earlier. The network load balancer listener and backend set must use the same IP protocol version.

Ingress traffic port : Specify the port the listener monitors for ingress traffic depending on the traffic type. Select one of the following options:
- Public network load balancers:
- Use any port: Enter 0 or an asterisk ("*") to indicate any port can be used.
- Select the Port: Enter the port number you want to use.
- Private network load balancers:
- Use any port: Enter 0 or an asterisk ("*") to indicate any port can be used.
- Select the Port: (UDP, TCP, and UDP/TCP only) Enter the port number you want to use.

### Timeout

Enter the timeout for each traffic type in seconds. If you don't enter a timeout value, the default values are used. The number of timeout values you must enter varies depending on the listener traffic type you selected earlier:
- UDP : One timeout. Default is 120 seconds.
- TCP : One timeout. Default is 360 seconds.
- UDP/TCP : Two timeouts, one for each protocol (UDP and TCP). Default is 120 and 360 seconds.
- L3IP : Three timeouts, for one for each protocol (L3IP, UDP, and TCP). Default is 120, 120, and 360 seconds.

Select Next .

### Proxy protocol

When you select TCP, UDP/TCP, TCP/UDP/ICMP, or L3 IP as the listener's traffic type, you have the option of enabling proxy protocol version 2. For more information on using proxy protocol with network load balancers, see[Proxy Protocol](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/network-load-balancer-management.htm#proxy-protocol)
Note  
  
You can't enable proxy protocol on your network load balancer if the source/destination header preservation feature in enabled.

## 2. Choose backends

The Choose backends page is where you set up your backend servers and backend sets.

A network load balancer distributes traffic to backend servers within a backend set. A backend set is a logical entity defined by a network load balancing policy, a list of backend servers (compute instances), and a health check policy.

The network load balancer creation workflow creates one backend set for the network load balancer. Optionally, you can add backend sets and backend servers after you create the network load balancer.

IP protocol version : Select from the following options:
- IPv4
- IPv6
Note  
  
This step is required if you enabled the IPv6 Address Assignment option. The network load balancer listener and backend set must use the same IP protocol version. You must select the option chosen for the listener.

Backend Set Name : Enter a name for the backend set or accept the default name.

Mode : Select the backend set mode:
- Default : A backend set defined by a load balancing policy, a health check policy, and an unlimited number of backend servers.
- Non-preemptive : A backend set limited to only two backend severs. You can specify one backend server as a backup for the other one. For more information, see[Non-Preemption Mode](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../BackendSets/backend-set-management.htm#non-preemption-mode).

### Select backends

The Backends list displays those backend servers that are configured and available for use with the network load balancer you're creating. The list displays details for each backend server, including its name (for compute instance-based servers), IP address, availability domain, compartment, port, and weight. You can add a backend server to the list by selecting Add Backends and configuring it as described in the later in this section.

The number of backends you can assign to a backend set depends on its type. A Default backend set can have an unlimited number of backend servers assigned. A Non-preemptive backend set can only have a maximum of two backend servers assigned. For Non-preemptive backend sets, you can specify one of the two backend servers as a backup for the other.

After you add instances to the backend set, they appear in the Select backend servers table. You can perform the following tasks:
- Update the server Port to which the network load balancer must direct traffic. The default is port 80.
- Update the server Weight that specifies the proportion of incoming traffic the backend handles. The higher the number, the more traffic that is received.
- Remove any instance by checking it and selecting Remove . You can also select Remove from the Action menu at the end of an instance entry.

Preserve Source IP : Select to preserve the original source and destination header (IP addresses and ports) of each incoming packet all the way to the backend server. You can't add IP address-based backend servers if the preserve source IP feature is enabled. For more information, see[Enabling Network Load Balancer Backend Set Source Preservation](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../BackendSets/preserve-backend-set-source-id.htm).
Note  
  
If you selected L3 IP for your listener traffic type, the Preserve Source IP option is automatically enabled. You can't disable it.

#### Adding Backend Servers to Default Backend Sets

Select Add Backends to open the Add backends panel.

Enter the following information:
- Backend type : Select one of the following options:
- Compute instances : Enter the following information under Backend :
- Instance compartment : Select the compartment containing the compute instance you want to use for the backend server from the list.
- Instance : Select the compute instance you want for the backend server from the list.
- IP address : Select the IP address for the backend server from the list.
- Availability domain : This value is automatically assigned based on the instance you selected.
- Port : Enter the communication port for the backend server. Sometimes the port value is fixed as "Any."
- Weight : (Optional) Enter the load balancing policy weight number assigned to the server. Backend servers with a greater weight receive a larger proportion of incoming traffic. Select Add another backend to configure another backend server of the same type (Compute instance).
- IP address : Enter the following information under Backend :
- IP address : Enter the IP address of the backend server.
- Port : Enter the communication port for the backend server. Sometimes the port value is fixed as "Any."
- Weight : (Optional) Enter the load balancing policy weight number assigned to the server. Backend servers with a greater weight receive a larger proportion of incoming traffic.
Note  
  
Preserve source IP must be disabled in the backend set to add an IP address-based backend server.

Select Add another backend to configure another backend server of the same type (Compute instance).

When have set up all the backends you want to add, select Add backends . The backend servers you added appear in the Backends list.

If you wanted to add another backend of the type opposite of what you had added before, you select Add backends and complete the process of adding more backends.

#### Adding Backend Servers to Non-Preemptive Backend Sets

Select Add Backends to open the Add backends panel. When you add backend servers to a non-preemptive backend set, the Add backends panel contains the settings for a pair of backend servers. You configure both backend server in the same way as for a default backend. Both backend servers are configured as either compute instance-based or IP address-based.

For non-preemptive backend sets, both backend servers include the Configure as backup option. Enabling this option assigns that backend server the role of the backup to the active backend server in the pair. Normally, you would configure your first backend server as the active server and the second backend server as the backup. You can only assign the backup role to one backend server in the pair at a time.

You can switch the active and backup roles of the two backend servers at any time. First, disable the Configure as backup option on the backup, then enable it on the current active backend server to reassign it as the backup. You can also switch the roles of the pair of backend servers after the network load balancer is creating by editing the backend server. For more information, see[Editing a Backend Server](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../BackendServers/update-backend-server.htm).
Note  
  
You can't edit the backend servers assigned to a non-preemptive backend set.

#### Deleting Backend Servers

You can delete an individual backend server from the Backends list by selecting Delete from its Actions menu (three dots). You can delete backend servers in bulk by selecting each one's box and then selecting the Delete button. Confirm the deletion when prompted.

### Specify health check policy

Specify the test parameters that confirm the health of the backend servers. For more information on this feature, see[Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../HealthCheckPolicies/health-check-policy-management.htm).

Enter the following information:
- Protocol : Specify the protocol to use for health check queries:
- HTTP
- HTTPS
- TCP
- UDP
- DNS : For more information on how to configure your health check policies for the DNS protocol, see[DNS Health Checking](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../HealthCheckPolicies/health-check-policy-management.htm#dns-health-checks).
Important  
  
Configure the health check protocol to match the application or service. For more information, see[Health Check Policies](https://docs.oracle.com/en-us/iaas/Content/NetworkLoadBalancer/NetworkLoadBalancers/../HealthCheckPolicies/health-check-policy-management.htm).

For both TCP and UDP, the provided data must be base64 encoded. Use any base64 encoding tool to convert the plain text strings to based64 encoded strings, and use the encoded strings for the health check configuration. For example, the following plain text string:

`this is the request data for my NLB backend health check`

is encoded as:

`dGhpcyBpcyB0aGUgcmVxdWVzdCBkYXRhIGZvciBteSBOTEIgYmFja2VuZCBoZWFsdGggY2hlY2s`

The encoded string is what undergoes the health check configuration.

The supported maximum length of the string before base64 encoding is 1024 bytes. If the string exceeds the limit, the configuration call fails with an HTTP status code 400.
- Transport protocol : (DNS only) Specify the transport protocol used to send traffic when DNS is selected as the protocol:
- UDP
- TCP
- Port : Specify the backend server port against which to run the health check. You can enter the value '0' to have the health check use the backend server's traffic port.
- Interval in MS : Specify how often to run the health check, in milliseconds. The default is 10000 (10 seconds).
- Timeout in MS : Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
- Number of retries : Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is 3.
- Request Data : (Required for UDP, and optional for TCP only) Enter the request message included in the request. This request data is included in the single request to the backend server. The request data is compared against the response data
- Response Data : (Required for UDP, and optional for TCP only) Enter the response message against which the health check feature sends a single request to the backend server is compared. If a match, the health check passes.
- Status code : (HTTP and HTTPS only) Specify the status code a healthy backend server must return.
- URL path (URI) : (HTTP and HTTPS only) Specify a URL endpoint against which to run the health check.
- Response body (regular expression) : Provide a regular expression for parsing the response body from the backend server.
- Query name : (DNS only) Provide a DNS domain name for the query.
- Query class : (DNS only) Select from the following options:
- IN : Internet (default)
- CH : Chaos
- Query type : (DNS only) Select from the following options:
- A : Indicates a hostname corresponding IPv4 address. (default)
- AAAA : Indicates a hostname corresponding IPv6 address.
- TXT : Indicates a text field.
- Acceptable response codes : Select one or more from the following options:
- RCODE:0 NOERROR DNS query completed successfully.
- RCODE:2 SERVFAIL Server failed to complete the DNS request.
- RCODE:3 NXDOMAIN Domain name doesn't exist.
- RCODE:5 REFUSED The server refused to answer for the query.
- Fail open : (Optional) Select to have the network load balancer continue to move traffic to the backend servers in this backend set using the current configuration, even if all the backend servers' states becomes unhealthy.
- Enable instant failover : (Required for DNS, optional for all other protocols) Select to redirect existing traffic to a healthy backend server if the current backend server becomes unhealthy. This feature doesn't work if Fail open is enabled and all backend servers become unhealthy.
- Send TCP reset : (L3 IP listeners only) Select to automatically reset the TCP connection to a failed backend server.

### Security list

Select to manually configure subnet security list rules to allow the intended traffic or allow the system to create security list rules for you. To learn more about these rules, see[Parts of a Security Rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).

Select one of the following options:
- Manually configure security list rules after the network load balancer is created : When you select this option, you must configure security list rules after the network load balancer creation.
- Automatically add security list rules : When you select this option, the Network Load Balancer service creates security list rules for you.

The system displays a table for egress rules and a table for ingress rules. Each table lets you select the security list that applies to the relevant subnet.

You can decide whether to apply the proposed rules for each affected subnet.

### Load balancing policy

Select one of the following load balancing policies:
- 5-Tuple hash : Routs incoming traffic based on 5-Tuple (source IP and port, destination IP and port, protocol) hash.
Note  
  
When the L3 IP listener protocol is selected, the load balancer doesn't support 5-Tuple hash policies.
- 3-Tuple hash : Routs incoming traffic based on 3-Tuple (source IP, destination IP, protocol) hash.
- 2-Tuple hash : Routs incoming traffic based on 2-Tuple (source IP Destination, destination IP) hash.

Select Next .

## 4. Review and create

Review the contents of the Review and create page. Edit settings or return to previous screens to add information. When the settings are fully verified, select Create network load balancer .

The network load balancer you created appears in the Network load balancer list page.
- 

Use the[oci nlb network-load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/create.html)command and required parameters to create a network load balancer:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/latest/NetworkLoadBalancer/CreateNetworkLoadBalancer)
