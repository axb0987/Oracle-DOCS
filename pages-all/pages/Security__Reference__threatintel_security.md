# Securing Threat Intelligence
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/threatintel_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Threat Intelligence

This topic provides security information and recommendations for Threat Intelligence.

## Security Responsibilities

To use Threat Intelligence securely, learn about your security and compliance responsibilities.

Unlike most other services in Oracle Cloud Infrastructure, Threat Intelligence is a read-only database. You do not create and manage resources within Threat Intelligence. As a result, securing Threat Intelligence is relatively simple.
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Threat Intelligence in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/threatintel_security.htm#iam-policies)

## Routine Security Tasks

Threat Intelligence does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Threat Intelligence.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Because all resources in Threat Intelligence are read-only, only the`inspect`and`read`verbs are applicable.

[Limit threat intelligence data to security administrators](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/threatintel_security.htm#)

Allow users in the group`SecurityAdmins`to search for and view threat indicators:
```

```

For more information about Threat Intelligence policies and to view more examples, see[Threat Intelligence Policies](https://docs.oracle.com/iaas/Content/threat-intel/using/policies.htm)
