# Security for Core Services
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_core_services.htm
- Fetched: 2026-09-05 03:03 CDT

# Security for Core Services

Learn about key security features in the core Oracle Cloud Infrastructure services.

## Compute

Oracle Cloud Infrastructure Compute lets you provision and manage Compute hosts, known as instances . You can launch instances as needed to meet your Compute and application requirements. After you launch an instance, you can access it securely from your computer, restart it, attach and detach volumes , and terminate it when you're done with it. Any changes made to the instance's local drives are lost when you terminate it. Any saved changes to volumes attached to the instance are retained.

Oracle Cloud Infrastructure offers both bare metal and virtual machine instances: Bare Metal A bare metal Compute instance gives you dedicated physical server access for highest performance and strong isolation. After a customer terminates their bare metal instance, the server undergoes an automated disk and firmware-level wipe process to ensure isolation between customers. Virtual Machine A virtual machine (VM) is an independent computing environment that runs on top of physical bare metal hardware. The virtualization makes it possible to run multiple VMs that are isolated from each other. VMs are ideal for running applications that do not require the performance and resources (CPU, memory, network bandwidth, storage) of an entire physical machine.

An Oracle Cloud Infrastructure VM Compute instance runs on the same hardware as a bare metal instance, using the same cloud-optimized hardware, firmware, software stack, and networking infrastructure.

All Oracle Cloud Infrastructure instances use key-based Secure Shell (SSH) by default. Customers provide the SSH public keys to Oracle Cloud Infrastructure and use the SSH private keys for accessing the instances. Oracle recommends using key-based SSH to access Oracle Cloud Infrastructure instances. Password-based SSH could be susceptible to brute-forcing attacks, and is not recommended.

Oracle Linux images hardened with the latest security updates are available for you to run on Oracle Cloud Infrastructure instances. Oracle Linux images run the Unbreakable Enterprise Kernel (UEK) and support advanced security features such as Ksplice to apply security patches without rebooting. In addition to Oracle Linux, Oracle Cloud Infrastructure makes available a list of other OS platform images, including CentOS, Ubuntu, and Windows Server. All platform images come with secure defaults including OS-level firewalls turned on by default.

You can also bring your own custom images. However, certain[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)only permit the use of platform images in compartments associated with a security zone.

Use the[Vulnerability Scanning](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#security_features_topic_Scanning)service to routinely check instances for potential security vulnerabilities like missing patches or open ports. The service generates reports with metrics and details about these vulnerabilities, and assigns each a risk level. Specialized Instances

Oracle Cloud Infrastructure offers features that let you customize instances for specialized workloads and security requirements.
- Shielded instances harden the firmware security on bare metal hosts and virtual machines to defend against malicious boot level software. For more information, see:[Shielded Instances](https://docs.oracle.com/iaas/Content/Compute/References/shielded-instances.htm#shielded).
- Confidential computing encrypts and isolates in-use data and the applications processing that data. For more information, see:[Confidential Computing](https://docs.oracle.com/iaas/Content/Compute/References/confidential_compute.htm).
- Dedicated virtual machine hosts let you run OCI Compute virtual machine instances on dedicated servers that are a single tenant and not shared with other customers. For more information, see:[Dedicated Virtual Machine Hosts](https://docs.oracle.com/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm).

For more information, see:
- [Overview of Compute](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm)
- [Securing Compute](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/compute_security.htm)

## Networking

The Oracle Cloud Infrastructure Networking service allows you to define a customizable private network (a VCN, or virtual cloud network), which enforces logical isolation of your Oracle Cloud Infrastructure resources. As with your on-premises network in your data centers, you can set up a VCN with subnets, route tables, gateways, and firewall rules.

The following are key networking concepts associated with a VCN: Subnet The primary subdivision of a VCN. Subnets can be public or private. A private subnet prevents resources launched in that subnet from having public IP addresses. Internet gateway A virtual router that provides public internet connectivity from a VCN. By default, a newly created VCN has no internet connectivity. Dynamic routing gateway (DRG) A virtual router that provides a path for private traffic between a VCN and a data center's network. A DRG is used with an IPSec VPN or Oracle Cloud Infrastructure FastConnect. Network address translation (NAT) gateway A virtual router that gives cloud resources without public IP addresses access to the internet without exposing those resources to incoming internet connections. Service gateway A virtual router that gives cloud resources private access to Oracle services such as Object Storage without using an internet gateway or NAT gateway. Route table Virtual route tables that have rules to route traffic from subnets to destinations outside the VCN by way of gateways or specially configured Compute instances. Security list Virtual firewall rules that specify the types of traffic (protocol and port) allowed in and out of resources. Individual rules can be defined to be stateful or stateless and affect all resources in the target subnet. Network security group Virtual firewall rules that define allowed ingress and egress to resources that are members of the group. Individual rules can be defined to be stateful or stateless.

Use security lists, network security groups, or a combination of both to control packet-level traffic in and out of the resources in your VCN. For example, you can allow incoming SSH traffic from anywhere to a subnet or group of instances by setting up a stateful ingress rule with source CIDR 0.0.0.0/0, and destination TCP port 22. Every VCN has a default security list that allows only SSH and certain types of important ICMP ingress traffic, and allows all egress traffic.

Create private subnets to ensure that resources in the subnet have no internet access, even if the VCN has a working internet gateway, and even if security rules and firewall rules allow the traffic. Certain[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)only permit the use of private subnets. You can use the[Bastion](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#security_features_topic_Bastion)service to create secure, temporary SSH sessions from the internet to resources in a private subnet.

A VCN can be configured for internet connectivity, or connected to your private data center through a Site-to-Site VPNor FastConnect. FastConnect offers a private connection between an existing network's edge router and DRGs. Traffic does not traverse the internet.

For more information, see:
- [Ways to Secure Your Network](https://docs.oracle.com/iaas/Content/Network/Concepts/waystosecure.htm)
- [Access Control](https://docs.oracle.com/iaas/Content/Network/Concepts/accesscontrol.htm)
- [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)
- [Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/networking_security.htm)

## Storage

Oracle Cloud Infrastructure offers multiple storage solutions to meet your performance and durability requirements: Local Storage NVMe-backed storage on compute instances, offering high IOPS. Block Volume Network-attached storage volumes, attachable to compute instances. Object Storage Regional service for storing large amounts of data as objects, providing strong consistency and durability. Objects are organized using buckets. File Storage

Durable network file system that supports the Network File System version 3.0 (NFSv3) protocol.

The Oracle Cloud Infrastructure Block Volume service provides persistent storage that can be attached to compute instances using the iSCSI protocol. The volumes are stored in high-performance network storage and support automated backup and snapshot capabilities. Volumes and their backups are accessible only from within a customer's VCN and are encrypted at rest using unique keys. For more security, iSCSI CHAP authentication can be required on a per-volume basis.

The Oracle Cloud Infrastructure Object Storage service provides highly scalable, consistent, and durable storage for objects. API calls over HTTPS provide high-throughput access to data. All objects are encrypted at rest using unique keys and, by default, access to buckets and objects within them requires authentication.

[Security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)require you to encrypt volumes, objects, and file systems using customer-managed keys in the[Vault](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Vault_Service)service. You can also use[Security Advisor](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Advisor)to quickly create storage resources and the required keys in a single interface.

Use IAM security policies to grant users and groups access privileges to Object Storage buckets. To allow access to buckets by users who do not have IAM credentials, the bucket owner (or a user with necessary privileges) can create pre-authenticated requests. Pre-authenticated requests allow authorized actions on buckets or objects for a specified duration.

Alternately, buckets can be made public, which allows unauthenticated and anonymous access. Object Storage enables you to verify that an object was not unintentionally corrupted by allowing an MD5 checksum to be sent with the object and returned upon successful upload. This checksum can be used to validate the integrity of the object. Given the security risk of inadvertent information disclosure, Oracle recommends that you carefully consider the business case before making a bucket public. Certain[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)forbid the creation of public buckets.

The Oracle Cloud Infrastructure File Storage service allows you to manage resources like file systems, mount targets, and export sets. You use IAM policies to define access to these resources. The`AUTH_UNIX`style of authentication and permission checking is supported for remote NFS client requests to a file system.

For more information, see:
- [Securing Block Volume](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/blockstorage_security.htm)
- [Securing Object Storage](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/objectstorage_security.htm)
- [Securing File Storage](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/filestorage_security.htm)

## Database

The Oracle Cloud Infrastructure Database service offers autonomous and co-managed Oracle Database cloud solutions. For both types of database solutions, you have full access to the features and operations available with the database, but Oracle owns and manages the infrastructure.
- Autonomous databases are preconfigured, fully managed environments that are suitable for either transaction processing or for data warehouse workloads.
- Co-managed solutions are bare metal, virtual machine, and Exadata DB systems that you can customize with the resources and settings that meet your needs.

DB systems are accessible only from your VCN, and you can configure network security groups or security lists to control network access to your databases. The Database service is integrated with IAM for controlling which users can launch and manage DB systems. By default, data is encrypted at rest using Oracle transparent data encryption (TDE) with master keys stored in an Oracle Wallet on each DB system.

RMAN backups of DB systems are encrypted and stored in customer-owned buckets in the Object Storage service. Certain[security zone policies](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security_features.htm#Security_Zones_Service)require the configuration of database backups.

Applying Oracle database security patches (Oracle Critical Patch Updates) is imperative to mitigate known security issues, and Oracle recommends that you keep patches up to date. Patchsets and Patch Set Updates (PSUs) are released on a quarterly basis. These patch releases contain security fixes and other high-impact/low-risk critical bug fixes.

For more information, see[Securing Database](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/dbaas_security.htm).

## Load Balancing

Oracle Cloud Infrastructure Load Balancer provides automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network (VCN). The service offers a load balancer with your choice of a public or private IP address, and provisioned bandwidth. A private load balancer has an IP address from the hosting subnet, which is visible only within your VCN.

You can apply the following SSL configurations to your load balancer: SSL TERMINATION The load balancer handles incoming SSL traffic and passes the unencrypted request to a backend server. POINT-TO-POINT SSL The load balancer terminates the SSL connection with an incoming traffic client, and then initiates an SSL connection to a backend server. SSL TUNNELING If you configure the load balancer's listener for TCP traffic, the load balancer tunnels incoming SSL connections to your application servers.

The Load Balancer service supports TLS 1.2 by default, and prioritizes the following forward-secrecy ciphers in the TLS cipher-suite:
- ECDHE-RSA-AES256-GCM-SHA384
- ECDHE-RSA-AES256-SHA384
- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-RSA-AES128-SHA256
- DHE-RSA-AES256-GCM-SHA384
- DHE-RSA-AES256-SHA256
- DHE-RSA-AES128-GCM-SHA256
- DHE-RSA-AES128-SHA256

You can configure network access to load balancers by using VCN network security groups or security lists.

For more information, see[Securing Networking: VCN, Load Balancers, and DNS](https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/../Reference/networking_security.htm)
