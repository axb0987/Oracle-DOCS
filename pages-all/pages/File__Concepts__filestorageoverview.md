# Overview of File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm
- Fetched: 2026-09-05 02:02 CDT

# Overview of File Storage

Oracle Cloud Infrastructure File Storage service provides a durable, scalable, secure, enterprise-grade network file system. You can connect to a File Storage service file system from any bare metal, virtual machine, or container instance in your Virtual Cloud Network (VCN). You can also access a file system from outside the VCN using VCN peering, Oracle Cloud Infrastructure FastConnect, and Internet Protocol security (IPSec) virtual private network (VPN).

Large Compute clusters of thousands of instances can use the File Storage service for high-performance shared storage. Storage provisioning is fully managed and automatic as your use scales from a single byte to exabytes without upfront provisioning.

The File Storage service supports the Network File System version 3.0 (NFSv3) protocol. The service supports the Network Lock Manager (NLM) protocol for file locking functionality.

Oracle Cloud Infrastructure File Storage employs 5-way replicated storage, located in different fault domains, to provide redundancy for resilient data protection. Data is protected with erasure encoding.

The File Storage service uses the "eventual overwrite" method of data eradication. Files are created in the file system with a unique encryption key. When you delete a single file, its associated encryption key is eradicated, making the file inaccessible. When you delete an entire file system, the file system is marked as inaccessible. The service systematically traverses deleted files and file systems, frees all the used space, and eradicates all residual files.

Use the File Storage service when your application or workload includes big data and analytics, media processing, or content management, and you require Portable Operating System Interface (POSIX)-compliant file system access semantics and concurrently accessible storage. The File Storage service is designed to meet the needs of applications and users that need an enterprise file system across a wide range of use cases, including the following:
- General Purpose File Storage: Access to an unlimited pool of file systems to manage growth of structured and unstructured data.
- Big Data and Analytics: Run analytic workloads and use shared file systems to store persistent data.
- Lift and Shift of Enterprise Applications: Migrate existing Oracle applications that need NFS storage, such as Oracle E-Business Suite and PeopleSoft.
- Databases and Transactional Applications: Run test and development workloads with Oracle, MySQL, or other databases.
- Backups, Business Continuity, and Disaster Recovery: Host a secondary copy of relevant file systems from on premises to the cloud for backup and disaster recovery purposes.
- MicroServices and Docker: Deliver stateful persistence for containers. Easily scale as your container-based environments grow.
Note  
  
File Storage is designed to be used with 64-bit applications. For more information, see[32-Bit Application Stops Reading or Writing to a File System](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Troubleshooting/32_bit_application.htm).
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31676)to the service and its capabilities.

## File Storage Concepts

Using the File Storage service requires an understanding of the following concepts, including some that pertain to Oracle Cloud Infrastructure Networking: MOUNT TARGET An NFS endpoint that lives in a subnet of your choice and is highly available. Mount targets use IPv4 or IPv6 addresses to communicate with file systems. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system. File systems are exported (made available) through mount targets. When you[use the console to create your first file system](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/create-file-system.htm), the workflow also creates a mount target and export for it. You can reuse the same mount target to make as many file systems available on the network as you want. To reuse the same mount target for multiple file systems, create an export in the mount target for each file system.

Mount target limitations:
- Each mount target can accept up to 100,000 NFS client connections.
- If you use in-transit encryption, each mount target can accept up to 4096 NFS/SSL client connections. See[Using In-transit TLS Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/intransitencryption.htm)for more information.
- By default, you can create two mount targets per account per availability domain. See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase. See[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingmounttargets.htm)for more information about working with this resource. EXPORT Exports control how NFS clients access file systems when they connect to a mount target. File systems are exported (made available) through mount targets. Each mount target maintains an export set which contains one or many exports. A file system must have at least one export in one mount target in order for instances to mount the file system. The information used by an export includes the file system OCID, mount target OCID, export set OCID,[export path](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filesystempaths.htm), and client[export options](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/exportoptions.htm#Export). When you[create a new file system](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/create-file-system.htm), the workflow also creates a mount target and export for it. Thereafter,
- You can create as many exports in a mount target for different file systems as you want.
- You can create as many exports in a mount target for a single file system as you want.
- You can delete and re-create exports in a mount target as often as you need to.
- You can add export options to an export to control access to the file system. For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingmounttargets.htm). and[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/exportoptions.htm). EXPORT SET Collection of one or more exports that control what file systems the mount target exports using NFSv3 protocol and how those file systems are found using the NFS mount protocol. Each mount target has an export set. Each file system associated with the mount target has at least one export in the export set. EXPORT PATH A path that's specified when an export is created. It uniquely identifies the file system within the mount target, letting you associate many file systems to a single mount target. This path is unrelated to any path within the file system itself, or the client mount point path. The File Storage service adds an export that pairs the file system's Oracle Cloud Identifier (OCID) and path. See[Paths in File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filesystempaths.htm)for more information. EXPORT OPTIONS NFS export options are a set of parameters within the export that specify the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range. You can have up to 100 options per export.For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/exportoptions.htm). VIRTUAL CLOUD NETWORK (VCN) A private network that you set up in the Oracle data centers, with firewall rules and specific types of communication gateways that you can choose to use. A VCN covers a single, contiguous IPv4 or IPv6 CIDR block of your choice. For more information about VCNs, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)in the Oracle Cloud Infrastructure Networking documentation. Traffic to a file system doesn't travel through the internet, but you can manage File Storage resources using the API or SDK over the internet. You can choose to set up a service gateway and give the VCN private access to the File Storage API to manage its resources. When creating the service gateway, enable the service label called All &lt;region&gt; Services in Oracle Services Network , which includes the File Storage service. Be sure to update route tables for any subnets that need File Storage API access through the service gateway. For more information and detailed instructions, see[Setting Up a Service Gateway in the Console](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm#setting_up_sgw). SUBNETS Subdivisions you define in a VCN (for example, 10.0.0.0/24 and 10.0.1.0/24). Subnets contain virtual network interface cards (VNICs), which attach to instances. A subnet can span a region or exist in a single availability domain . A subnet consists of a contiguous range of IP addresses that don't overlap with other subnets in the VCN. For each subnet, you specify the routing rules and security lists that apply to it. For more information about subnets, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)in the Oracle Cloud Infrastructure Networking documentation. SECURITY RULES Virtual firewall rules for a VCN. A VCN comes with a default security list, and you can add more. These security lists provide ingress and egress rules that specify the types of traffic allowed in and out of the instances. You can choose whether a particular rule is stateful or stateless. Security list rules must be set up so that clients can connect to file system mount targets. Network security groups (NSGs). Another method for applying security rules is to set them up in a network security group (NSG), and then add the mount target to the NSG. Unlike security list rules that apply to all VNICs in the subnet, NSGs apply only to resource VNICs you add to the NSG. See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm),[Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm), and[Network Security Groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)for more information, examples, and scenarios about how these features interact in your network.[Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm)provides general information about networking. See[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/securitylistsfilestorage.htm)for more specific information. SNAPSHOTS Snapshots provide a consistent, point-in-time view of a file system, and you can take as many snapshots as you need. You pay only for the storage used by your data and metadata, including storage capacity used by snapshots. Each snapshot reflects only data that changed from the previous snapshot. For more information, see[Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingsnapshots.htm).

## Data Transfers

FastConnect offers you the ability to accelerate data transfers. You can leverage the integration between FastConnect and the File Storage service to perform initial data migration, workflow data transfers for large files, and disaster recovery scenarios between two regions, among other things.

For more information, see[Transferring Data To and From File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/transferring-data-to-and-from-file-storage.htm).

## File Storage Space Allocation

The File Storage service allocates space in blocks of variable size in a way that is fine-tuned to minimize total customer cost and optimize performance for modern workloads. The minimum block size used is 8192 bytes. For example, if you create a 1-byte file, we allocate 8192 bytes. We use larger blocks to store larger files. To learn more about file system and snapshot usage, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/FSutilization.htm).

## How File Storage Permissions Work

File Storage service resources include file systems, mount targets, and export sets. The AUTH_SYS style of authentication and permission checking is supported for remote NFS client requests. You use Oracle Cloud Infrastructure Identity and Access Management (IAM) policy language to define access to Oracle Cloud Infrastructure resources. You can consider exports and snapshots subsidiary resources of export sets and file systems, respectively. As such, they do not need their own permissions. Related resources include Oracle Cloud Infrastructure Compute instances and Oracle Cloud Infrastructure Networking virtual cloud networks (VCNs).

Oracle Cloud Infrastructure users require resource permissions to create, delete, and manage resources. Without the appropriate IAM permissions, you cannot export a file system through a mount target. Until a file system has been exported, compute instances cannot mount it. For more information about creating an IAM policy, see[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management).

If you have successfully exported a file system on a subnet, then you use Networking security lists to control traffic to and from the subnet and, therefore, the mount target. Security lists act as a virtual firewall, allowing only the network traffic you specify to and from the IP addresses and port ranges configured in your ingress and egress rules. The security list you create for the subnet lets hosts send and receive packets and mount the file system. If you have firewalls on individual instances, use FastConnect, or use a virtual private network (VPN), the settings for those might also impact security at the networking layer. For more information about creating a security list for the File Storage service, see[Creating File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/creatingfilesystems.htm). See[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/securitylayers.htm)for more information on how different types of security work together in your file system.

## Regions and Availability Domains

You can use the File Storage service in all regions. For a list of supported regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

When you create file systems and mount targets, you specify the availability domain they are created in. All file system data is then stored entirely within the availability domain the file system resides in. Within an availability domain, the File Storage service uses synchronous replication and high availability failover to keep your data safe and available.

You cannot move a file system to a different availability domain or region. However, you can take a snapshot of your data and use a tool such as`rsync`to copy your data to a different availability domain or region. To maximize performance for data protection operations, you can use the[File Storage Parallel Tools](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/using_file_storage_parallel_tools.htm)suite. The Parallel File Tools suite provides parallel versions of`tar`,`rm`, and`cp`. See[Managing Snapshots](https://docs.oracle.com/en-us/iaas/Content/File/Concepts/../Tasks/managingsnapshots.htm)for more information on using snapshots to protect your data.

While it is possible to access mount targets from any availability domain in a region, for optimal performance, place File Storage resources in the same availability domain as the compute instances that access them.

Subnets can be either AD-specific or regional. You can create File Storage resources in either type of subnet. Regional subnets allow compute instances to connect to any mount target in the subnet regardless of AD, with no additional routing configuration. However, to minimize latency, place mount targets in the same AD as compute instances just as you would in an AD-specific subnet. For more information, see[Overview of VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm).

## Creating Automation with Events

You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

The following File Storage resources emit events:
- File systems
- Snapshots
- Mount targets
- Exports
- Export sets

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## Limits on Your File Storage Components

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

To set compartment-specific limits on file systems or mount targets, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas_topic-File_Storage_Quotas.htm).

## Additional Documentation Resources

The following Oracle Cloud Infrastructure File Storage service solution playbooks and white papers are available:
- [Sharing the Application Tier File System in Oracle E-Business Suite Release 12.2 or 12.1.3 Using the Oracle Cloud Infrastructure File Storage Service

Learn best practices for using a File Storage service shared application tier file system for Oracle E-Business Suite.
- [Learn about deploying Oracle E-Business Suite on Oracle Cloud Infrastructure

Learn how file storage is part of a multihost, secure, high-availability topology for Oracle E-Business Suite.
- [Design a pilot-light disaster recovery (DR) topology
