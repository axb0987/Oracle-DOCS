# Securing Document Understanding
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/document-understanding-security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Document Understanding

This topic provides security information and recommendations for the Oracle Cloud Infrastructure Document Understanding service.

## Security Responsibilities

To use Document Understanding securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You're responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all of the services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Security Patching: Oracle conducts security patching monthly to ensure that Oracle Cloud Infrastructure services have up-to-date security patches.

Your security responsibility includes the following area:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Document Understanding in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/document-understanding-security.htm#document_understanding-iam-policies)

## Routine Security Tasks

Document Understanding doesn't have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Document Understanding.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Create this policy to let the group,`DocumentUsers`, to perform all actions in Document Understanding, except deleting groups. Limit`DOCUMENT_DELETE`and`DOCUMENT_GROUP_DELETE`permissions to tenancy and compartment administrators.

```

```

For more information about Document Understanding policies and to view more examples, see[About Document Understanding Policies](https://docs.oracle.com/iaas/document-understanding/document-understanding/using/about_document-understanding_policies.htm).

## Data Encryption

Document Understanding uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in the service. No configuration is necessary.

## Data Durability

Document Understanding doesn't create back-ups. After data is deleted, the data cannot be restored. Use[policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/document-understanding-security.htm#document_understanding-iam-policies)to limit access to Document Understanding and to restrict users' ability to delete data.

## Data Security

Document Understanding uses the HTTPS protocol to secure data and[IAM policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/document-understanding-security.htm#document_understanding-iam-policies)to secure the API.

## Auditing

Document Understanding uses the[Oracle Cloud Infrastructure Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)to record the calls made to Document Understanding resources. The Audit service records the following log events:
- API calls made by the Console, CLI, or SDK
- Calls made by other Oracle Cloud Infrastructure services
-
