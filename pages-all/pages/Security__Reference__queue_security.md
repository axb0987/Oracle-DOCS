# Securing Queue
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Queue

This topic provides security information and recommendations for Queue.

## Security Responsibilities

To use Queue securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Queue in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#iam-policies)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#data-encryption)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#network-security)

## Routine Security Tasks

After getting started with Queue use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate encryption keys[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#data-encryption)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#auditing)

## IAM Policies

Use policies to limit access to Queue.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

[Queue Management](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#)

For administrators, the following policy lets the specified group do everything with queues and related Queue service resources:
```

```

[Producers and Consumers](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/queue_security.htm#)

Use the following policies to let a specified group produce to or consume from a queue:
```

```

```

```

For more information about Queue policies and to view more examples, see[Queue Policies](https://docs.oracle.com/iaas/Content/queue/policy-reference.htm).

## Data Encryption

Create and rotate encryption keys in the Vault service to protect your resources in Queue.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

Although default encryption keys can be generated automatically when you create certain Oracle Cloud Infrastructure resources, we recommend that you create and manage your own custom encryption keys in the Vault service.

Each queue uses a key to encrypt and decrypt all messages.

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

We recommend that you use IAM policies to strictly limit the creation, rotation, and deletion of encryption keys. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

## Data Durability

Queue messages are ephemeral and deleted when they expire.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

## Network Security

Secure network access to your resources in Queue.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. Use private subnets to host resources that do not require internet access. You can also configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

## Auditing

Locate access logs and other security data for Queue.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

If you enabled Cloud Guard in your tenancy, then it reports any user activities that are potential security concerns. Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)and[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm)
