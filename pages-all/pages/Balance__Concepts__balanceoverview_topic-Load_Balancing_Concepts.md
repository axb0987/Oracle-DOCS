# Load Balancer Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview_topic-Load_Balancing_Concepts.htm
- Fetched: 2026-09-05 01:40 CDT

# Load Balancer Concepts

Learn about concepts associated with load balancers and their resources.

The following concepts are essential to working with Load Balancer. BACKEND SERVER An application server responsible for generating content in reply to the incoming TCP or HTTP traffic. You typically identify application servers with a unique combination of overlay (private) IPv4 address and port, for example, 10.10.10.1:8080 and 10.10.10.2:8080. See[Backend Servers for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingbackendservers.htm)for more information. BACKEND SET A logical entity defined by a list of backend servers, a load balancing policy, and a health check policy. SSL configuration is optional. The backend set determines how the load balancer directs traffic to the collection of backend servers. See[Backend Sets for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingbackendsets.htm)for more information. CERTIFICATES If you use HTTPS or SSL for your listener, you must associate an SSL server certificate (X.509) with your load balancer. A certificate enables the load balancer to terminate the connection and decrypt incoming requests before passing them to the backend servers. See[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingcertificates.htm)for more information. CIPHER SUITE A cipher suite is a logical entity for a set of algorithms, or ciphers, using Transport Layer Security (TLS) to determine the security, compatibility, and speed of HTTPS traffic. All ciphers are associated with at least one version of TLS 1.0, 1.1, 1.2, and 1.3. You can use the provided preconfigured cipher suites, or create your own custom ones. You can only modify or delete custom cipher suites. health check

A health check is a test to confirm the availability of backend servers. A health check can be a request or a connection try. Based on a time interval you specify, the load balancer applies the health check policy to continuously monitor backend servers. If a server fails the health check, the load balancer takes the server temporarily out of rotation. If the server then passes the health check, the load balancer returns it to the rotation.

You configure your health check policy when you create a backend set. You can configure TCP-level or HTTP-level health checks for your backend servers.
- TCP-level health checks make a TCP connection with the backend servers and validate the response based on the connection status.
- HTTP-level health checks send requests to the backend servers at a specific URI and validate the response based on the status code or entity data (body) returned.

The service provides application-specific health check capabilities to help you increase availability and reduce your application maintenance window. See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/load_balancer_health_management.htm)for more information. HEALTH STATUS An indicator that reports the general health of your load balancers and their components. See[Health Check Policies for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/load_balancer_health_management.htm)for more information. HOSTNAME A virtual server name applied to a listener to enhance request routing. See[Virtual Hostnames for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/hostname_management.htm)for more information. LISTENER A logical entity that checks for incoming traffic on the load balancer's IP address. You configure a listener's protocol and port number, and the optional SSL settings. To handle TCP, HTTP, and HTTPS traffic, you must configure multiple listeners. Supported protocols include:
- 

HTTPS
- 

HTTP
- 

HTTP/2
- 

gRPC
- 

TCP See[Listeners for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managinglisteners.htm)for more information. LOAD BALANCING POLICY A load balancing policy tells the load balancer how to distribute incoming traffic to the backend servers. Common load balancer policies include:
- 

Round robin
- 

Least connections
- 

IP hash See[Load Balancer Policies](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/lbpolicies.htm)for more information. PATH ROUTE SET A set of path route rules to route traffic to the correct backend set without using multiple listeners or load balancers. See[Request Routing for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingrequest.htm)for more information. REGIONS AND availability domains The Load Balancer service manages application traffic across availability domains within a region . A region is a localized geographic area, and an availability domain is one or more data centers located within a region. A region is composed of several availability domains. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for more information. SESSION PERSISTENCE A method to direct all requests originating from a single logical client to a single backend web server. See[Load Balancer Session Persistence](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Reference/sessionpersistence.htm)for more information. SHAPE A template that determines the load balancer's total pre-provisioned maximum capacity (bandwidth) for ingress plus egress traffic. Specify minimum bandwidth and maximum bandwidth values to create an upper and lower size range for the load balancer's bandwidth shape. Possible sizes range from 10 Mbps to 8,000 Mbps. The Always Free option is incorporated into your paid account in your home region. The first 10 Mbps of your bandwidth is free, and is indicated as such on your bill. For more information about Always Free resources, including other capabilities and limitations, see[Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
Note  
  

Pre-provisioned maximum capacity applies to aggregated connections, not to a single client attempting to use the full bandwidth. SSL Secure Sockets Layer (SSL) is a security technology for establishing an encrypted link between a client and a server. You can apply the following SSL configurations to your load balancer: SSL TERMINATION The load balancer handles incoming SSL traffic and passes the unencrypted request to a backend server. POINT-TO-POINT SSL The load balancer terminates the SSL connection with an incoming traffic client, and then initiates an SSL connection to a backend server. SSL TUNNELING If you configure the load balancer's listener for TCP traffic, the load balancer tunnels incoming SSL connections to your application servers. Load Balancer supports the TLS 1.2 protocol with a default setting of strong cipher strength. The default supported ciphers include:
- 

ECDHE-RSA-AES256-GCM-SHA384
- 

ECDHE-RSA-AES256-SHA384
- 

ECDHE-RSA-AES128-GCM-SHA256
- 

ECDHE-RSA-AES128-SHA256
- 

DHE-RSA-AES256-GCM-SHA384
- 

DHE-RSA-AES256-SHA256
- 

DHE-RSA-AES128-GCM-SHA256
- 

DHE-RSA-AES128-SHA256 See[Load Balancer- Managed SSL Certificates](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingcertificates.htm)for more information. subnet A subdivision you define in a virtual cloud network (VCN), such as 10.0.0.0/24 and 10.0.1.0/24. A subnet can span a region or exist within in a single availability domain. A subnet consists of a contiguous range of IP addresses that do not overlap with other subnets in the VCN. For each subnet, you specify the routing and security rules that apply to it. See[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)and[Public IP Address Ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#oci-public-ips)for more information on subnets. TAGS

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). VIRTUAL CLOUD NETWORK (VCN) A private network that you set up in the Oracle data centers, with firewall rules and specific types of communication gateways that you can choose to use. A VCN covers a single, contiguous IPv4 CIDR block of your choice in the[allowed IP address ranges](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#Allowed). You need at least one virtual cloud network before you launch a load balancer. For information about setting up virtual cloud networks, see[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm). VISIBILITY Specifies whether your load balancer is public or private. PUBLIC A public load balancer has a public IP address that clients can access from the internet. PRIVATE A private load balancer has a private IP address from a VCN local subnet. Clients can access the private load balancer using methods and technology that can provide access to a private IP, such as:
- 

Cross-VCN (through LPG peering)
- 

From another region (through RPC)
- 

From on-prem (through FC private peering) For more information, see[Load Balancer Management](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/managingloadbalancer.htm). WORK REQUEST An object that reports on the current state of a Load Balancer request. The Load Balancer service handles requests asynchronously. Each request returns a work request ID (OCID) as the response. You can view the work request item to see the status of the request. For more information, see[Work Requests for Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/../Tasks/viewingworkrequest.htm)
