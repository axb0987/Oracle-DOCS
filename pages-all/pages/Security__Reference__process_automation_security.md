# Securing Process Automation
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/process_automation_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Process Automation

This topic provides security information and recommendations for Process Automation.

## Security Responsibilities

To use Process Automation securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Process Automation in a new Oracle Cloud Infrastructure tenancy.

Task More Information

Use IAM policies to control and manage access to Process Automation resources.[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/process_automation_security.htm#iam-policies)

Use IDCS application roles to control access to the administration and Designer interface of Process Automation instance.[IDCS Application Roles](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/process_automation_security.htm#confidentiality)

## IAM Policies

Use policies to limit access to Process Automation.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to the tag administrators.

For more information about Process Automation policies and to view more examples, see[Details for Process Automation](https://docs.oracle.com/iaas/Content/Identity/Reference/processautomationpolicyreference.htm).

## IDCS Application Roles

Assign users IDCS application roles to control and manage access of users to the administration and Designer interface of Process Automation.

There are two predefined IDCS application roles in Process Automation.
- The ServiceAdministrator role grants full administrative privileges within the Oracle Cloud Infrastructure Process Automation instance, including administrative tasks in Workspace.
- The ServiceDeveloper role is appropriate for team members working with the instance to extend and customize it, such as creating process applications and configuring roles in Designer.
