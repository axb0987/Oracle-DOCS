# Managing Mount Targets
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm
- Fetched: 2026-09-05 02:04 CDT

# Managing Mount Targets

Learn the basics of managing File Storage mount targets.

## Overview

A mount target is an NFS endpoint that lives in a chosen VCN subnet and provides network access for file systems. The mount target provides the IP address or DNS name that's used together with a unique export path to mount the file system.

When you[use the Console to create your first file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm), the workflow also creates a mount target and export for it.
Caution  
  
Each mount target requires three IP addresses. Don't use /30 or smaller subnets for mount target creation because they don't have enough available IP addresses. As an example, a /28 subnet with 13 available IP addresses could support four mount targets. For more information, see[Mount Target Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#limitations).

You can reuse the same mount target to make as many file systems available on the network as you need. To reuse the same mount target for multiple file systems, create an export in the mount target for each file system.

You can perform the following mount target management tasks:
- [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm)
- [Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm)
- [Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm)
- [Editing a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm)
- [Moving a Mount Target Between Compartments](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm)
- [Getting Mount Command Samples](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm#get-mount-command-samples)
- [Creating an Export](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-export.htm)
- [Editing an Export and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-export.htm)
- [Setting a File System's Reported Size](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size-mt.htm)
- [Updating Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm)
- [Locking a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-mount-target.htm)
- [Deleting a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm)

### Exports

Exports control how NFS clients access file systems when they connect to a mount target. File systems are exported (made available) through mount targets. Each mount target maintains an export set which contains one or many exports. A file system may be exported through one or more mount targets. A file system must have at least one export in one mount target in order for instances to mount the file system. The information used by an export includes the file system OCID, mount target OCID, export set OCID,[export path](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filesystempaths.htm), and client[export options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm#Export). When you use the Console to create your first file system, the workflow also creates a mount target and export for it. Thereafter:
- You can create as many exports in a mount target for different file systems as you need.
- You can create as many exports in a mount target for a single file system as you need.
- You can delete and re-create exports in a mount target as often as you need to.
- You can add export options to an export to control access to the file system.

### NFS Export Options
NFS export options are a set of parameters within the export that specify the level of access granted to NFS clients when they connect to a mount target. An NFS export options entry within an export defines access for a single IP address or CIDR block range. You can have up to 100 options per export.

For more information, see[Working with NFS Exports and Export Options](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/exportoptions.htm).

## Mount Target Performance

When[changing a mount target's performance level](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm), you can select a level that corresponds to maximum throughput. You don't need to re-create the mount target if requirements change. The performance level of a mount target can be either a Standard type or a High Performance type.

Performance level maximum throughput is measured for reads where the block size is 1 MiB or greater with sufficient concurrency and queue depth. Maximum throughput isn't available to[hydrating clones](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/cloningFS.htm#Limitations_and_Considerations)until hydration is complete.

Read Throughput (Gigabits per Second) Capacity Entitlement Mount Target Type
1 Gbps None Standard
20 Gbps 20,000 GB High Performance
40 Gbps 40,000 GB High Performance
80 Gbps 80,000 GB High Performance

Standard mount targets have a maximum throughput, but no storage capacity entitlement. File systems exported through a standard mount target are billed based on usage. For more information, see[File System Usage and Metering](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/FSutilization.htm).

High Performance mount targets have a maximum throughput and a storage capacity entitlement. If the storage usage in the availability domain is equal to or greater than the total entitlement, there's no additional charge for high performance mount targets. To calculate the total billable storage usage, compare the total capacity entitlement for all high performance mount targets to the actual storage used in the availability domain. Whichever amount is larger is the billable usage.

A high performance mount target requires a 30-day billing commitment. After upgrading a mount target, the billing cycle begins. Because of this commitment, when you change a high performance mount target to a lower performance level, the mount target performance is downgraded when the billing cycle ends. To find mount target throughput and billing cycle, see[Getting a Mount Target's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-mount-target-details.htm).

For specific pricing details, see[Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html).

### Optimizing Throughput

The following settings and environment are required to take full advantage of an HPMT-80 mount target's 80 Gbps read throughput:
- One or more NFS clients capable of driving an aggregate 80 Gbps.
- 

Linux kernel version 5.3 or later using the`nconnect`mount option. For example:
```

```

- A dataset size of greater than 20 GB.
- 

A queue depth of 64.

If using`fio`, the following options are recommended:
```

```

## Details About a Mount Target

The mount target details page provides the following information about a mount target: MOUNT TARGET OCID Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). You need your mount target's OCID to use the Command Line Interface (CLI) or the API. You also need the OCID when contacting support. CREATED The date and time that the mount target was created. Availability Domain When you create a mount target, you specify the availability domain that it resides in. An availability domain is one or more data centers located within a region. You need your mount target's availability domain to use the Command Line Interface (CLI) or the API. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). COMPARTMENT When you create a mount target, you specify the compartment that it resides in. A compartment is a collection of related resources (such as cloud networks, compute instances, or file systems) that are accessible only to those groups that have been given permission by an administrator in your organization. You need your mount target's compartment to use the Command Line Interface (CLI) or the API. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). REPORTED SIZE (GIB) The maximum capacity in gibibytes reported by the file systems exported through this mount target. The File Storage service currently reports 8589934592 gibibytes (GiB) of available capacity by default. If you are installing an application that requires a specific reported size, you can change the reported size. Typically, setting the size to 1024 GiB is sufficient for most applications. This value is updated hourly. See[Setting a File System's Reported Size](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm)for more information. REPORTED INODES (GII) The maximum capacity in gibiinodes reported by the file systems exported through this mount target. The File Storage service currently reports gibiinodes (GiI) of available inodes by default. If you are installing an application that requires specific reported inodes, you can change the reported inodes. Typically, setting the inodes to 1024 GiI is sufficient for most applications. This value is updated hourly. See[Setting a File System's Reported Size](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-file-system-size.htm)for more information. NETWORK SECURITY GROUPS The[network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)that the mount target belongs to. Each mount target can belong to up to five (5) NSGs. See[Adding a Mount Target to a Network Security Group](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/add-mount-target-to-nsg.htm)for more information. MOUNT TARGET THROUGHPUT The requested read throughput for the mount target in gigabits per second (Gbps). This value only differs from Billed Throughput if there's been a request to downgrade the mount target's performance. This throughput will be available after the current billing cycle ends, unless the request is canceled or the mount target is deleted. The API calls this`requestedThroughput`. For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance). BILLED THROUGHPUT Current read throughput for the mount target in gigabits per second (Gbps). The API calls this`observedThroughput`. For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance). CAPACITY ENTITLEMENT The capacity entitlement for the mount target, if the mount target uses a high performance shape. For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance). BILLING CYCLE ENDS The date and time that the current billing cycle ends and the next billing cycle begins. High performance mount targets have a 30-day billing cycle. For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance). VIRTUAL CLOUD NETWORK The VCN that contains the subnet where the mount target VNIC resides. SUBNET The subnet within the VCN where the mount target VNIC resides. Subnets can be either AD-specific or regional (regional ones have " regional" after the name). For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

Tip  
  
We recommend using a subnet dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need. For more information, see[Choosing the Subnet for a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#subnet-selection). IP ADDRESS The IP address that was assigned to the mount target when it was created. You need your mount target's IP address to[mount associated file systems](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm). HOSTNAME The hostname that was assigned to the mount target, if any. For more information about hostnames, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). FULLY QUALIFIED DOMAIN NAME The hostname together with the subnet domain name. For more information, see[DNS in Your Virtual Cloud Network](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm). If you specify a hostname, you can use the FQDN to mount the file system. EXPORT SET OCID The OCID of the mount target's export set resource. Each mount target has one export set, which contains all of the exports for the mount target. You need your mount target's export set OCID when you perform export-related tasks in the Command Line Interface (CLI) or the API. EXPORTS All of the mount target's exports are listed here. The export path and name of each file system is also listed.[You need the export path to mount a file system.](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)

### NFS Tab

The NFS tab on the mount target details page provides the following information about your mount target: KERBEROS ENABLED Whether or not the mount target is configured to use Kerberos. KERBEROS REALM The Kerberos realm that this mount target has joined. KEYTAB SECRET OCID The Keytab secret used by the mount target. CURRENT KEYTAB SECRET VERSION The version of the Keytab secret used by the mount target. BACKUP KEYTAB SECRET VERSION The version of the backup Keytab secret. LDAP ENABLED Whether or not the mount target should use an LDAP server for[secondary group lookup](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap.htm#ldap-mapping). The file system's export must also have ID Mapping enabled. SCHEMA TYPE The schema type of the LDAP account. CACHE REFRESH INTERVAL IN SECONDS How often the mount target should contact the LDAP server for updates. CACHE LIFETIME IN SECONDS How long cached entries may be used. NEGATIVE CACHE LIFETIME IN SECONDS How long to cache if ID mapping information is missing. SEARCH BASE FOR USERS All LDAP searches are recursive starting at this user. SEARCH BASE FOR GROUPS All LDAP searches are recursive starting at this group. OUTBOUND CONNECTOR 1 OCID The first connector to use to communicate with the LDAP server. OUTBOUND CONNECTOR 2 OCID The second connector to use to communicate with the LDAP server.

## Limitations and Considerations

- 

Each availability domain is limited to two Standard mount targets, two 20 Gbps High Performance mount targets, one 40 Gbps High Performance mount target, and zero 80 Gbps High Performance mount targets by default.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.
- Each mount target can accept up to 100,000 NFS client connections. If you use in-transit encryption, each mount target can accept up to 4096 NFS/SSL client connections. See[Using In-transit TLS Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm)for more information.
- Each tenancy in a region can have one`CreateMountTarget`or`ChangeMountTargetCompartment`operation in progress at a time. See[409 error occurs when creating or moving a file system or mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Reference/known-issues-for-file-storage.htm#error-409)for more information.
- A mount target that's scheduled for a[performance downgrade](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm)can't be[edited](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-mount-target.htm),[moved](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-mount-target.htm), or have logging enabled until the downgrade is completed or canceled by a user.
- High performance mount targets can't be directly created or deleted. A standard mount target must be[created](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm)and[upgraded for high performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm). A high performance mount target must be[downgraded to a standard performance level](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm)before it can be deleted.
- 

Each mount target, during creation, requires three IP addresses in the subnet. Only the first IP address is for customer use. The second two addresses are used for an internal failover process. During a File Storage maintenance event, the failover process releases one of the two reserved addresses and uses a new IP address that's available in the subnet. The customer-facing IP address is unaffected.

If the mount target's subnet uses dual-stack IPv4/IPv6 addressing, two available IPv4 addresses are still required, even if an IPv6 address was assigned to the mount target for customer use.
Caution  
  
Don't use /30 or smaller subnets for mount target creation because they don't have enough available IP addresses. As an example, a /28 subnet with 13 available IP addresses could support four mount targets.

We recommend using a subnet dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need. You can use the CLI to search for used IP addresses, including those used by mount targets. To find the IP addresses in a subnet that are used by mount targets, use the following command:

```

```

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to manage mount targets. Because mount targets are network endpoints, users must also have "use" permissions for VNICs, private IPs, private DNS zones, and subnets to create or delete a mount target.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
