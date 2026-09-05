# Securing Cloud Advisor
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloudadvisor-security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Cloud Advisor

This topic provides security information and recommendations for Oracle Cloud Infrastructure's Cloud Advisor service.

## Security Responsibilities

To use Cloud Advisor securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all of the services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security reponsibility includes the following area:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Cloud Advisor in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloudadvisor-security.htm#iam-policies)

## Routine Security Tasks

Cloud Advisor does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Cloud Advisor.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Create this policy to allow group`CloudAdvisorUsers`to perform all actions in Cloud Advisor except deleting profiles.

```

```

For more information about Cloud Advisor policies and to view more examples, see[Creating Cloud Advisor Policies](https://docs.oracle.com/iaas/Content/CloudAdvisor/Reference/cloudadvisorpolicyreference.htm).

## Data Encryption

Cloud Advisor uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in the service. No configuration is necessary.

Cloud Advisor does not use Vault keys. Internally, Cloud Advisor stores data in an Autonomous AI Database that uses Vault keys. Oracle manages and secures these resources.

## Data Durability
