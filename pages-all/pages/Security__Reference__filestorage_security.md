# Securing File Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing File Storage

This topic provides security information and recommendations for Oracle Cloud Infrastructure File Storage.

## Security Responsibilities

To use File Storage securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure File Storage in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#iam-policies)
Review and implement File Storage security layers[Access Control](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#access-control)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#data-encryption)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#network-security)

## Routine Security Tasks

After getting started with File Storage use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Take regular backups[Data Durability](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#durability)
Use resource locks to prevent tampering[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#iam-policies)
Perform a security audit and review logs[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#auditing)
If you're managing your own encryption keys, rotate them regularly[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#data-encryption)

## IAM Policies

Use policies to limit access to File Storage.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

To minimize the risk of accidental or intentional resource deletion, we strongly advise granting`DELETE`permissions only to a limited group of trusted IAM users and groups, specifically tenancy and compartment administrators. By restricting these privileges, you can significantly reduce the potential for resource loss because of unauthorized or mistaken actions.

[Prevent File System and Mount Target Deletion](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/filestorage_security.htm#)

The following example prevents group FileUsers from deleting file systems and mount targets.

```

```

Tip  
  
File Storage resources can also be locked to prevent updates, moves, and deletions of the resource. Locks help protect resources against tampering. Locks on a file system resource doesn't prevent authorized users from changing the contents of the file system. Users can still create, change, and delete files on a file system with a resource lock. For more information, see[Locking a File System](https://docs.oracle.com/iaas/Content/File/Tasks/lock-file-system.htm).

For more information about File Storage policies and to view more examples, see[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

## Access Control

In addition to creating IAM policies, lock down access to file systems using other available security layers.

The File Storage service uses five different layers of access control. Each layer has its own authorization entities and methods which are separate from the other layers.

For more information, see[About File Storage Security](https://docs.oracle.com/iaas/Content/File/Concepts/securitylayers.htm).

## Data Encryption

Create and rotate encryption keys in the Vault service to protect your resources in File Storage.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

While Oracle Cloud Infrastructure can generate default encryption keys for certain resources, we strongly advise taking a more secure approach by creating and managing your own custom encryption keys within the Vault service. This gives you greater control over key management and enhances the overall security posture of your cloud environment.

To encrypt the data in a file system using your own Vault encryption key, see[Encrypting a File System](https://docs.oracle.com/iaas/Content/File/Tasks/encrypt-file-system.htm).

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

For the best security, use IAM policies to enforce granular access controls over encryption key management activities, including key creation, rotation, and deletion. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

Encryption keys handle encryption at rest. For more information about in-transit encryption, see[About File Storage Security](https://docs.oracle.com/iaas/Content/File/Concepts/securitylayers.htm).

## Data Durability

Take regular backups of your data in File Storage.

Users sometimes inadvertently delete production data in a File Storage file system. You can't recover the data unless you have a copy of that data stored in a backup. For data durability, we recommend that you take periodic snapshots of the file system as required by business SLOs. Snapshots let you recover data from the snapshot in case of accidental data deletion.
Caution  
  
If an user delete a file system inadvertently, it also deletes the snapshots associated with the file system. You can't recover the snapshots and the data in the file system unless have a copy of that data stored in a backup.

Use[policy-based snapshots](https://docs.oracle.com/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm)to schedule recurring, automatic backups or[manually create backups](https://docs.oracle.com/iaas/Content/File/Tasks/create-snapshot.htm)using the Console, CLI, or API.

### Data Location

Depending on your disaster recovery policy, you may decide to store file system data in different locations. Those locations could be within OCI or outside of OCI, including on-premises environments.

With File Storage, you can leverage built-in[file system replication](https://docs.oracle.com/iaas/Content/File/Tasks/FSreplication.htm)capabilities to seamlessly replicate your data across various OCI destinations, including:
- Another file system in the same availability domain
- A file system in a different availability domain
- A file system in another region

As alternatives to storing data within OCI File Storage, you can transfer data to the following locations:
- Other OCI services such as Block Volume or Object Storage
- Outside of OCI, such as within your on-premises environment
Note  
  
Copying data from File Storage to an on-premises server or directly mounting a File Storage file system to an on-premises server can have performance implications.

For more information on the preceding options, see[Transferring Data To and From File Storage](https://docs.oracle.com/iaas/Content/File/Tasks/transferring-data-to-and-from-file-storage.htm)and[Better backups with policy-based snapshots and replication in OCI File Storage Service](https://blogs.oracle.com/cloud-infrastructure/post/policybased-snapshots-replication-oci-file-storage).

## Network Security

Secure network access to your resources in File Storage.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. Use private subnets to host resources that do not require internet access. You can also configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

For more information, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/iaas/Content/File/Tasks/securitylistsfilestorage.htm).

## Auditing

Locate access logs and other security data for File Storage.

The logging feature records operations such as creation, deletion, and updates to File Storage resources for your internal review. For more information, see[File Storage Logging](https://docs.oracle.com/iaas/Content/File/Concepts/logging.htm).

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
