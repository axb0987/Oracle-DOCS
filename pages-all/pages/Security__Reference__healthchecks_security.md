# Securing Health Checks
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Health Checks

This topic provides security information and recommendations for Health Checks.

## Security Responsibilities

To use Health Checks securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Health Checks in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm#iam-policies)
Add security lists where needed so that Health Checks can access resources.[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm#network-security)

## IAM Policies

Use policies to limit access to Health Checks.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about Health Checks policies, see[Details for Health Checks (IAM with identity domains)](https://docs.oracle.com/iaas/Content/Identity/Reference/healthcheckpolicyreference.htm)and[Details for Health Checks (IAM without identity domains)](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To).

[All Users in the Tenancy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm#)

Create this policy to allow all users in the tenancy to manage Health Checks resources.

```

```

[All Users in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm#)

Create this policy to allow all users in the`ABC`compartment to manage Health Checks resources.

```

```

[Group in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/healthchecks_security.htm#)

Create this policy to allow the`HCUsers`group in the`ABC`compartment to manage Health Checks resources.

```

```

For more information about Health Checks policies and to view more examples, see[Details for Health Checks](https://docs.oracle.com/iaas/Content/Identity/Reference/healthcheckpolicyreference.htm).

## Network Security

Secure network access to your resources in Health Checks.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

For monitoring by the Health Checks service, resources must be accessible from the public internet. You might need to set up[security lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm). See[Securing Networking](https://docs.oracle.com/iaas/Content/Security/Reference/networking_security.htm)
