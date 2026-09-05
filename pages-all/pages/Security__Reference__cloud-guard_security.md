# Securing Cloud Guard
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloud-guard_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Cloud Guard

This topic provides security information and recommendations for Cloud Guard.

## Security Responsibilities

To use Cloud Guard securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You're responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security : Oracle is responsible for protecting the global infrastructure that runs all the services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibility includes the following area:
- Access Control : Limit privileges as much as possible. Give users only the access necessary to perform their work.

## Initial Security Tasks

See[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloud-guard_security.htm#cloud_guard_security__IAM_Policies)and[Data Masking](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloud-guard_security.htm#cloud_guard_security__Data_Masking)below.

## Routine Security Tasks

Cloud Guard doesn't have any security tasks that you need to perform regularly.

## IAM Policies

Design IAM user groups to which you can:
- Assign policies providing different levels of access to Cloud Guard. Design groups so that you can assign each the least privileges that they require to perform their responsibilities (inspect, read, use, or manage).
- Enforce the same data masking restrictions on all members of the group. Data masking allows you to redact sensitive information from users who aren't authorized to view it.

Create the IAM user groups to control access to Cloud Guard. See[Creating the Cloud Guard User Group](https://docs.oracle.com/iaas/Content/cloud-guard/using/prerequisites.htm#prereq-user-group).

Assign privileges to each group . Ensure that you assign the least privileges that group members require to perform their responsibilities. From the lowest level of privileges to the highest, the policy verbs are:`inspect`,`read`,`use`, and`manage`. See[Policy Statements for Users](https://docs.oracle.com/iaas/Content/cloud-guard/using/prerequisites.htm#prereq-policies-users).

Assign IAM users to the appropriate IAM groups. See[Using the Console](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#three).

## Data Masking

Determine what information is sensitive . Scan all the pages in the Cloud Guard UI and note any information that shouldn't be viewable by all people who are able to access Cloud Guard.

Understand how data masking works . See[About Data Masking](https://docs.oracle.com/iaas/Content/cloud-guard/using/data-mask.htm#data-mask-about).

Create data masking rules that redact sensitive information for IAM groups that aren't authorized to view it. See[Creating Data Masking Rules](https://docs.oracle.com/iaas/Content/cloud-guard/using/data-mask.htm#data-mask-create).

## Data Encryption

Cloud Guard uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in the service. No configuration is necessary.

Cloud Guard doesn't use Vault keys. Internally, Cloud Guard stores data in an Autonomous AI Database that uses Vault keys. Oracle manages and secures these resources.

## Data Durability
