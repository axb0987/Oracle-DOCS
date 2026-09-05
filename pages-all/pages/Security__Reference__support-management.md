# Securing Support Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/support-management.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Support Management

Review security information and recommendations for Support Management.

For more information about Support Management, see[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

## Security Responsibilities

To use Support Management securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Support Management in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/support-management.htm#iam-policies)
Configure Oracle support accounts, including My Oracle Cloud Support for access control[Configuring Your Oracle Support Account](https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm)

## Routine Security Tasks

After getting started with Support Management use this checklist to identify security tasks that we recommend you perform regularly.

Support Management does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Support Management.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about Support Management policies and to view more examples, see[Support Management IAM Policy Reference](https://docs.oracle.com/iaas/Content/GSG/support/policy-reference.htm).

### Get and List Support Requests

Create this policy to allow a group to[get support requests](https://docs.oracle.com/iaas/Content/GSG/support/get-incident.htm)and[list support requests](https://docs.oracle.com/iaas/Content/GSG/support/list-incidents.htm)in the tenancy.
```

```

### Create and Update Support Requests

Create this policy to allow a group to[create support requests](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm)and[update support requests](https://docs.oracle.com/iaas/Content/GSG/support/update-incident.htm)in the tenancy.
```

```

## Access Control

In addition to creating IAM policies, lock down access to support requests using My Oracle Cloud Support. For more information, see[Configuring Your Oracle Support Account](https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm)
