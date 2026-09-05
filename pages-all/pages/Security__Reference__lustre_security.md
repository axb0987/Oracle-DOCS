# Securing File Storage with Lustre
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing File Storage with Lustre

This topic provides security information and recommendations for Oracle Cloud Infrastructure File Storage with Lustre.

## Security Responsibilities

To use File Storage with Lustre securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure File Storage with Lustre in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#iam-policies)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#data-encryption)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#network-security)

## Routine Security Tasks

After getting started with File Storage with Lustre use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate encryption keys[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#data-encryption)
Take regular backups[Data Durability](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#durability)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#auditing)

## IAM Policies

Use policies to limit access to File Storage with Lustre.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

[Prevent file system deletion](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/lustre_security.htm#)

The following example prevents group LustreUsers from deleting file systems.
```

```

For more information about File Storage with Lustre policies and to view more examples, see[File Storage with Lustre Policies](https://docs.oracle.com/iaas/Content/lustre/policies.htm).

## Data Encryption

Create and rotate encryption keys in the Vault service to protect your resources in File Storage with Lustre.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

Although default encryption keys can be generated automatically when you create certain Oracle Cloud Infrastructure resources, we recommend that you create and manage your own custom encryption keys in the Vault service.

To encrypt the data in a file system using your own Vault encryption key, see[Encrypting a File System](https://docs.oracle.com/iaas/Content/lustre/file-system-encryption.htm).

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

We recommend that you use IAM policies to strictly limit the creation, rotation, and deletion of encryption keys. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

## Data Durability

Take regular backups of your data in File Storage with Lustre.

Users sometimes inadvertently delete production data in a file system. You can't recover the data unless you have a copy of that data stored in a backup.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

## Network Security

Secure network access to your resources in File Storage with Lustre.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

For more information, see[Required VCN Security Rules.](https://docs.oracle.com/iaas/Content/lustre/security-rules.htm)

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. File Storage with Lustre file systems require private subnets . You can configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

## Auditing

Locate access logs and other security data for File Storage with Lustre.

The logging feature records operations such as creation, deletion, and updates to File Storage with Lustre resources for your internal review.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
