# Securing Batch
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/batch_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Batch

This topic provides security information and recommendations for Batch.

## Security Responsibilities

To use Batch securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Batch in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/batch_security.htm#iam-policies)
Add security lists where needed so that Batch can access resources.[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/batch_security.htm#network-security)

## Routine Security Tasks

Batch does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Batch.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Create this policy to allow`admin`user group to manage all Batch resources in a specific compartment.

```

```

For more information about policies and to view more examples, see[Batch Policies](https://docs.oracle.com/iaas/Content/oci-batch/iam-policies.htm).

## Network Security

Use Vulnerability Scanning to scan resources that are on private subnets or don't have public IP addresses.

A Compute instance is associated with a VCN (virtual cloud network) and a subnet . When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. If an instance you want to scan is on a private subnet or has no public IP address, the VCN must include a service gateway and a route rule for the service gateway. See[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)
