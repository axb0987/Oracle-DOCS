# Always Free Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
- Fetched: 2026-09-04 15:37 CDT

# Always Free Resources

Learn what Always Free resources are available to all Oracle Cloud Infrastructure users.

All Oracle Cloud Infrastructure accounts (whether free or paid) have a set of resources that are free of charge in the[home region](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm#Home)of the tenancy, for the life of the account. These resources display the Always Free-eligible label in the Console (for OCI Ampere A1 Compute shapes, see[Compute](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#compute)).

Using the Always Free resources, you can provision a[virtual machine (VM) instance](https://docs.oracle.com/iaas/Content/Compute/home.htm), an[Oracle Autonomous AI Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31), and the networking, load balancing, and storage resources needed to support the applications that you want to build. With these resources, you can do things like run small-scale applications or perform proof-of-concept testing.

The following sections summarize the Oracle Cloud Always Free-eligible resources that you can provision in your tenancy.

## Infrastructure

### Certificates

All tenancies get five certificate authorities (CAs) and 150 certificates included in the Always Free resources.

### Compute

All tenancies get a set of Always Free resources in the Compute service for creating[compute virtual machine (VM) instances](https://docs.oracle.com/iaas/Content/Compute/home.htm). You must create the Always Free compute instances in your[home region](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How).
Note  
  
If you receive an "out of host capacity" error when trying to create a Compute instance, this indicates a temporary lack of Always Free shapes in your home region. Try creating the instance in a different availability domain, or wait a while, then try to create the instance again. You can also choose to upgrade your account to Pay as You Go or another Paid account type, which gives you access to more types of Compute resources. Remember that Oracle doesn't charge for Always Free resources after you upgrade, and will only charge you for resource usage above the Always Free limits. You can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm)to control resource consumption within your account.

#### Available Shapes
- Micro instances (AMD processor): All tenancies get up to two Always Free VM instances using the VM.Standard.E2.1.Micro[shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm), which has an AMD processor.
- OCI Ampere A1 Compute instances (Arm processor): All tenancies get the first 1,500 OCPU hours and 9,000 GB hours per month for free for VM instances using the VM.Standard.A1.Flex[shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm), which has an[Arm processor](https://docs.oracle.com/iaas/Content/Compute/References/arm.htm). For Always Free tenancies, this is equivalent to 2 OCPUs and 12 GB of memory.

In regions with multiple availability domains:
- You can create OCI Ampere A1 Compute instances in any availability domain, except South Korea North (Chuncheon).
- Instances using the VM.Standard.E2.1.Micro shape can only be created in one availability domain.

#### Number of Compute Instances Available to Your Account

Depending on the size of the boot volume and the number of OCPUs that you allocate to each OCI Ampere A1 Compute instance, you can create one or two OCI Ampere A1 Compute instances, 2 OCPUs total. The minimum[boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm)size for each instance is 47 GB, regardless of shape. Your account comes with 200 GB of Always Free[block volume](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#blockvolume)storage which you use to create the boot volumes for your compute instances.

For example, using the default boot volume size of 47 GB, you could provision two instances using the VM.Standard.E2.1.Micro shape, and one OCI Ampere A1 Compute instance with 2 OCPUs or two OCI Ampere A1 Compute instances with 1 OCPU each, and zero instances using the VM.Standard.E2.1.Micro shape. Many combinations are possible, depending on how you allocate your block storage and OCI Ampere A1 Compute OCPUs. See[Details of the Always Free compute instances](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#Details_of_the_Always_Free_Compute_instance__a1_flex)for more information on allocating OCPU and memory resources when creating OCI Ampere A1 Compute instances.

#### IP Addresses for Compute Instances

You do not have to assign a public IPv4 address to every compute instance in your tenancy. You can create a compute instance in a public subnet without assigning the instance a public IP addresses, and create an instance in a private subnet.

#### Idle Compute Instances
Important  
  

Reclamation of Idle Compute Instances

Idle Always Free compute instances may be reclaimed by Oracle. Oracle will deem virtual machine and bare metal compute instances as idle if, during a 7-day period, the following are true:
- CPU utilization for the 95th percentile is less than 20%
- Network utilization is less than 20%
- Memory utilization is less than 20% (applies to[A1 shapes](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#Details_of_the_Always_Free_Compute_instance__a1_flex)only)

[Details of the Always Free compute instances](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

VM.Standard.E2.1.Micro shape (AMD):
- Processor: 1/8th of an OCPU with the ability to use additional CPU resources
- Memory: 1 GB
- Networking: Includes one VNIC with one public IP address and up to 50 Mbps network bandwidth via the internet. Traffic to private IPs, on-premise endpoints via a[Dynamic Routing Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm), or to endpoints within the same[Oracle Cloud region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)is up to 480 Mbps.
- 

Image: Your choice of one of the following Always Free-eligible[images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm):
- 

Oracle Linux Cloud Developer 8

[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm)provides the latest development tools, languages and Oracle Cloud Infrastructure software development kits (SDKs) to rapidly launch a comprehensive development environment. Due to the amount of memory allocated to the VM.Standard.E2.1.Micro shape, some programs are not installed.
- Oracle Linux
- Ubuntu
- CentOS

VM.Standard.A1.Flex shape (Arm-based OCI Ampere A1 Compute): Because the VM.Standard.A1.Flex shape is a[flexible shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#flexible), you can customize the number of OCPUs and amount of memory that are allocated when you create or resize an instance. You can use all of the Always Free OCPUs and memory to create a single instance, or create up to two instances of 1 OCPU each (2 OCPUs total) that each use a portion of the resources.
- Processor: 2 OCPUs total, which you can allocate flexibly
- Memory: 12 GB total, which you can allocate flexibly
- Networking: The network bandwidth and number of VNICs scale proportionately with the number of OCPUs. For details, see[Flexible Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm#flexible).
- 

Image: Your choice of one of the following Always Free-eligible[images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm):
- 

Oracle Linux Cloud Developer

[Oracle Linux Cloud Developer](https://docs.oracle.com/iaas/oracle-linux/oci/developer-image.htm)provides the latest development tools, languages and Oracle Cloud Infrastructure software development kits (SDKs) to rapidly launch a comprehensive development environment. The Oracle Linux Cloud Developer image requires at least 8 GB of memory.
- Oracle Linux
- Ubuntu

For steps to create an Always Free-eligible compute instance, see[Tutorial - Launching Your First Linux Instance](https://docs.oracle.com/iaas/Content/GSG/Reference/overviewworkflow.htm).
Tip  
  
The Linux images labeled "Always Free Eligible" in the Console are compatible with Always Free compute instances and incur no licensing fees. These images are also compatible with paid resources and are available to users of paid accounts. To provision a compute instance with an image that is not Always Free-eligible, you must have a paid account or a Free Trial account with available credits.

### Block Volume

All tenancies receive a total of 200 GB of[Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm)storage, and five volume backups included in the Always Free resources. These amounts apply to both boot volumes and block volumes combined. When you provision a compute instance, the instance automatically receives a 50 GB[boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm)for storage. You can also create and attach block volumes to expand the storage capacity of a compute instance. For more information, see[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)and[Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
Important  
  

- To create an Always Free block volume, the volume must be created in the[home region](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm#Home)of the tenancy. Volumes created outside of the home region incur regular block volume costs.
- For paid or free trial accounts that are eligible for Always Free resources, the same 200 GB of Always Free volume resources and five Always Free volume backup resources are available. When one of your Always Free resources is deleted, some of your Always Free resource capacity becomes available. When you have available Always Free capacity, Block Volume automatically tries to transition an existing paid resource to an Always Free resource. For example, if you have four 50 GB Always Free volumes and one 50 GB paid volume, and you delete one of the Always Free volumes, the service converts the paid volume to an Always Free volume.

[Details of the Always Free Block Volume resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

- 200 GB total of combined boot volume and block volume Always Free Block Volume storage in the[home region](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm#Home).
- Five total volume backups (boot volume and block volume combined) in home region.

When you create a compute instance, the default[boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm)size for the instance is 50 GB, which counts toward your allotment of 200 GB. You can customize the instance's boot volume size up to 200 GB; however, this will use up your full allotment of storage for Always Free Block Volume resources. Also, because the minimum boot volume size allowed for compute instances is 50 GB, launching four instances will use all your Always Free Block Volume resources. Alternatively, you can launch one instance with the default boot volume size of 50 GB, and then create and attach a 150 GB block volume to expand the storage capacity of the instance. For more information, see[Creating a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)and[Attaching a Block Volume to an Instance](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm). Although it is possible to mix paid and Always Free resources, Oracle does not recommend this. If you have used up your allotment of Always Free Block Volume resources, you can free up block storage resources by deleting an Always Free instance and deleting the boot volume, or deleting an Always Free block volume.

You can have a maximum of five Always Free volume backups at any time. This applies to both boot volume and block volume backups. For example, you could have three boot volume backups for your Always Free instance and two block volume backups for your Always Free block volumes. In this example, if you try to create new backups, the operation will fail with an error until you delete existing Always Free volume backups. For more information about volume backups, see[Overview of Block Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm)and[Overview of Boot Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm).

### Object and Archive Storage

All tenancies get a total of 20 GB of Always Free[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm).

[Details of the Always Free Object Storage resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

If your Free Trial has expired and your account is in an Always Free only state, Always Free includes the following:
- 20 GB of combined[Standard](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)tier,[Infrequent Access](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access)tier, and[Archive](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)tier data
- 50,000[Object Storage API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)requests per month

If you have a paid account or have free credits as part of a Free Trial, Always Free includes the following:
- 10 GB of[Standard](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Standard_Tier)tier data
- 10 GB of[Infrequent Access](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access)tier data
- 10 GB of[Archive](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive)tier data
- 50,000[Object Storage API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)requests per month
Important  
  
If you are participating in an Oracle Cloud Free Trial, you can store unlimited data and can use 20 GB for free (your usage of the first 20 GB incurs no deduction of your initial $300 trial credit balance). Upgrade to a paid account to continue access to unlimited storage. If you do not upgrade before your trial ends, your free account will be limited to 20 GB of combined Standard tier, Infrequent Access tier, and Archive tier data. If you are using more than the 20-GB limit when your Free Trial ends, all of your objects will be deleted. You can then upload objects until you reach your Always Free usage limits.

See[Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm)for instructions on using your Always Free storage resources.

### Vault

All master encryption keys protected by software are free. All tenancies get 20 key versions of master encryption keys protected by a hardware security module (HSM) and 150 Always Free[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)secrets. You can spread these keys or secrets across any number of vaults in the tenancy, although virtual private vaults are not included in the Always Free resources.

[Details of the Always Free Vault resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

- all key versions of a master encryption key protected by software (across any number of keys or vaults)
- 20 total key versions of a master encryption key protected by an HSM (across any number of keys or vaults)
- 

150 total Always Free secrets (across any number of vaults).
- 40 secret versions of any given secret (including up to 20 in some form of active use and 20 pending deletion).

If you have used up your allotment of Always Free secrets, you can release resources by scheduling a secret or secret version for deletion. At minimum, you do have to wait a day before the secret or secret version is deleted.

### Resource Manager

All tenancies get a set of Always Free resources in the[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)service that allow you to automate the process of provisioning infrastructure using Terraform. See[Quickly Launch Your Always Free Resources Using Resource Manager](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources_Launching.htm)for instructions on using Resource Manager to create your Always Free resources.

[Details of the Always Free Resource Manager resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

See the[Resource Manager documentation](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to learn more about the resources in the following table.

Resource Limit Name Always Free
[Configuration source providers](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm)

configuration-source-provider-count

100

[Jobs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/jobs.htm)(concurrent)

Job duration: 24 hours

concurrent-job-count

2
[Private endpoints](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm)

private-endpoint-count

1
[Private endpoint reachable IP addresses](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm)

private-endpoint-reachable-ip-count

100
[Private templates](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm)

template-count

100

[Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm)

Variables per stack: 250

Size per variable: 8192 bytes

Zip file per stack: 11 MB

stack-count

100

## Database

Oracle Autonomous AI Database: All tenancies get two Always Free[Oracle Autonomous AI Databases](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31). You can use these databases for transaction processing, data warehousing, Oracle APEX application development, or JSON-based application development. For current regional availability, see the Always Free Cloud Services table in[Cloud Regions—Infrastructure and Platform Services](https://www.oracle.com/cloud/data-regions.html).

Oracle NoSQL Database: All tenancies get an Oracle NoSQL Database with up to 133 million reads per month, 133 million writes per month, and 3 tables with 25 GB storage per table.[Learn more](https://docs.oracle.com/iaas/nosql-database/index.html)about Oracle NoSQL Database.

Oracle MySQL HeatWave: All tenancies get a standalone MySQL HeatWave DB system with a single node HeatWave cluster in the home region. The Always Free DB system has 50 GB of storage to store data and log files. An extra 50 GB of backup storage is available.[Learn more](https://docs.oracle.com/iaas/mysql-database/home.htm)about Oracle MySQL HeatWave.

[Details of the Always Free Oracle Autonomous AI Database instance](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

- Processor: 1 Oracle CPU processor (cannot be scaled)
- Database Storage: 20 GB storage (cannot be scaled)
- Workload Type: You choose from the following workload types: Autonomous AI Transaction Processing, Autonomous AI JSON Database, Oracle APEX Application Development, or Autonomous AI Lakehouse. See[About Autonomous AI Database Workload Types](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/about-autonomous-database-workloads.html#GUID-E1C8C5F2-22FB-4225-A3B9-9E78277A5834)for details about each workload type.
- Maximum Simultaneous Database Sessions: 20
- Exadata Infrastructure Type: Serverless
Tip  
  
Always Free Autonomous AI Databases can be upgraded to paid instances after provisioning if you need features like more storage or CPU scaling.
Note  
  

- Before creating an Always Free Autonomous AI Database, check your home region for Always Free Autonomous AI Database support. See[Data Regions for Platform and Infrastructure Services](https://www.oracle.com/cloud/data-regions.html).
- You cannot create an Always Free Autonomous AI Database in a home region where Always Free Autonomous AI Databases are not supported.
- Not all regions support the same database version. The supported version may be 19c-only or 21c-only, depending on the region.

See[Always Free Autonomous AI Database](https://docs.oracle.com/iaas/autonomous-database-shared/doc/autonomous-always-free.html)for additional product details.

## Networking

### Cluster Placement Groups

All tenancies get from 10 to 50 Always Free cluster placement groups in a region, depending on the service's pricing model.

### Load Balancing

All Oracle Cloud Infrastructure tenancies created December 15, 2020 or later get one Always Free Flexible Load Balancer with a minimum and maximum bandwidth set to 10 Mbps.

[Details of the Always Free Load Balancer](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

Tenancies created on December 15, 2020 or later
- Shape: Flexible (minimum and maximum: 10 Mbps)
- Listeners: 16
- Virtual Hostnames: 16
- Backend Sets: 16
- Backend Servers: 1024

Tenancies created before December 15, 2020
- Shape: Micro (10 Mbps)
- Listeners: 10
- Virtual Hostnames: 10
- Backend Sets: 10
- Backend Servers: 128

For information about provisioning an Always Free load balancer, see[Getting Started with Load Balancing](https://docs.oracle.com/iaas/Content/GSG/Tasks/loadbalancing.htm).

### Network Load Balancer

As part of your Always Free resources, you get one Network Load Balancer.

[Details of the Always Free Network Load Balancer](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

- 

Listeners: 50
- 

Backend sets: 50
- 

Backend servers per set: 512
- 

Backend servers total: 1024 (to be distributed among your backend sets)

### Virtual Cloud Networks (VCNs)

Free Tier tenancies (tenancies that are not paid and do not have Free Trial credits) can have up to 2 virtual cloud networks (VCNs). A VCN is a software-defined network that you set up in the Oracle Cloud Infrastructure data centers in a particular region. VCNs include IPv4 and IPv6 support.

Tenancies are by default not allowed to send e-mail through outbound TCP port 25 to the internet. If you require the ability to send email from your tenancy,[open a service limits request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)to obtain an exemption.

See the following topics for details on Networking service resources and service limits:
- [Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm)(service overview)
- [Overview of VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs_topic-Overview_of_VCNs_and_Subnets.htm)
- [Networking Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#network_limits)

### VCN Flow Logs

To help you audit the traffic in and out of the virtual network interface cards (VNICs) in your VCN, and to troubleshoot your[security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm), you can set up VCN flow logs . Flow logs record details about traffic that has been accepted or rejected based on the security list rules. Free Tier tenancies (tenancies that are not paid and do not have Free Trial credits) receive up to 10GB per month shared across OCI[Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).

See[VCN Flow Logs](https://docs.oracle.com/iaas/Content/Network/Concepts/vcn-flow-logs.htm)for more information on this feature.

### Site-to-Site VPN

Site-to-Site VPN provides a site-to-site IPSec connection between your on-premises network and your virtual cloud network (VCN). Use up to 50 IPSec connections with your Free Tier account.[Learn more](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm).

## Observability and Management

### Application Performance Monitoring

All tenancies get 1000 Application Performance Monitoring tracing events and 10 Synthetic Monitor runs per hour included in the Always Free resources.[Learn more](https://docs.oracle.com/iaas/application-performance-monitoring/index.html).

### Connector Hub

All tenancies get 2 Always Free connectors . Connector Hub helps cloud engineers manage and move data between Oracle Cloud Infrastructure (OCI) services and from OCI to third-party services.[Learn more](https://docs.oracle.com/iaas/Content/connector-hub/home.htm).

[Details of the Always Free Connector Hub resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm#)

If you have a free account (including trial accounts), Always Free Connector Hub includes 2 Always Free connectors .

If you have a paid account, see[Connector Hub Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#serviceconnectorhub-limits).

### Console Dashboards

All tenancies get 100 dashboards per tenancy included in the Always Free resources.[Learn more](https://docs.oracle.com/iaas/Content/Dashboards/Concepts/dashboardsoverview.htm).

### Email Delivery

As part of your Always Free resources, you can send 3000 emails for free per month. Learn more about OCI's[Email Delivery service](https://docs.oracle.com/iaas/Content/Email/home.htm).

### Fleet Application Management

All tenancies are entitled to manage the system lifecycle operation of the first 25 resources per month, which include Compute instances and databases, for free as a part of their Always Free resources.

### Monitoring

All tenancies get 500 million[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm)ingestion data points, and 1 billion retrieval data points included in the Always Free resources.

### Notifications

As part of your Always Free resources, you can send 1 million https notifications per month, and 1000 email notifications per month.[Learn more](https://docs.oracle.com/iaas/Content/Notification/home.htm)about OCI's Notifications service.

## Additional Services

### Outbound Data Transfer

As part of your Always Free resources, you get 10 TB per month of outbound data.

### Logging

Logging provides a highly scalable and fully managed single pane of glass for all the logs in your tenancy.[Learn more](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)about the Logging service.

### Bastion

OCI's Bastion service provides restricted and time-limited Secure Shell Protocol (SSH) access to target resources that don't have public endpoints. Bastion is free for both free and paid accounts. See[Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm)for more information.

## Service Usage and Limits
