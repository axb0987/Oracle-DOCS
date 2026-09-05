# Securing Console Dashboards
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dashboards-security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Console Dashboards

This topic provides security information and recommendations for the Oracle Cloud Infrastructure Console Dashboards service.

## Security Responsibilities

To use the Console Dashboards service securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all of the services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Security Patching: Oracle conducts security patching monthly to ensure that Oracle Cloud Infrastructure services have up-to-date security patches.

Your security reponsibility includes the following area:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Console Dashboards in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dashboards-security.htm#iam-policies)

## Routine Security Tasks

The Console Dashboards service does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Console Dashboards.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Create this policy to allow group`DashboardUsers`to perform all actions in the Console Dashboards service except deleting dashboards and dashboard groups. Limit`DASHBOARD_DELETE`and`DASHBOARD_GROUP_DELETE`permissions to tenancy and compartment administrators.

```

```

For more information about Console Dashboards policies and to view more examples, see[Policy Details for Console Dashboards](https://docs.oracle.com/iaas/Content/Dashboards/Reference/dashboardspolicyreference.htm).

## Data Encryption

The Console Dashboards service uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in the service. No configuration is necessary.

## Data Durability

The Console Dashboards service does not create backups. After data is deleted, the data cannot be restored. Use[policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dashboards-security.htm#iam-policies)to limit access to Console Dashboards and to restrict users' ability to delete data.

## Data Security

The Console Dashboards service uses the HTTPS protocol to secure data and[IAM policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/dashboards-security.htm#iam-policies)to secure the API.

## Auditing

The Console Dashboards service uses the[Oracle Cloud Infrastructure Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)to record the calls made to Console Dashboards service resources. The Audit service records the following log events:
- API calls made by the Console, CLI, or SDK
- Calls made by other Oracle Cloud Infrastructure services
-
