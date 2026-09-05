# Securing Security Zones
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Security Zones

This topic provides security information and recommendations for Security Zones.

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)let you be confident that your resources in Oracle Cloud Infrastructure, including Compute, Networking, Object Storage, and Database resources, comply with your security policies.

## Security Responsibilities

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Security Policies: Oracle is responsible for defining[security zone policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm). These policies implement security controls and best practices for customer resources that require maximum security, such as production applications.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Security Policies: Enable security zone policies that align with your security requirements, and use caution when disabling policies in zones. Address any policy violations in your existing resources to maintain compliance.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Security Zones in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#iam-policies)
Create compartments and security zones[Security Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#security-policies)

## Routine Security Tasks

After getting started with Security Zones use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Evaluate and enable new security zone policies[Security Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#security-policies)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#auditing)

## IAM Policies

Use IAM policies to limit administrative access to Security Zones.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

A security zone policy differs from an IAM policy in the following ways:
- A security zone policy is validated regardless of which user is performing the operation.
- A security zone policy denies certain actions; it doesn't grant capabilities.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

The practice of limiting`DELETE`permission is especially critical for Security Zones. Deleting a zone disables all security zone policies on resources in the zone's compartments, and therefore dramatically changes your security posture.

Example IAM policies:

[Allow a Group to Manage All Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#)

Allow users in the group`SecurityAdmins`to create, update, and delete all security zones and recipes in the entire tenancy:

```

```

[Allow a Group to Manage Recipes in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#)

Allow users in the group`SecurityAdmins`to create, update, and delete all recipes in the compartment`SecurityApps`:

```

```

[Allow a Group to Audit Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/securityzone_security.htm#)

Allow users in the group`SecurityAuditors`to view the security zones and recipes in the compartment`SecurityArtifacts`:

```

```

The individual resource types for Security Zones are included in the aggregate type`cloud-guard-family`. A policy that grants permissions to`cloud-guard-family`also grants the same permissions to Security Zones. For more information, see[Cloud Guard Policies](https://docs.oracle.com/iaas/Content/cloud-guard/using/policies.htm).

## Security Policies

Evaluate and enable security zone policies to maintain a strong security posture in Oracle Cloud Infrastructure.

A recipe is a collection of[security zone policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm)that you can assign to a security zone. If you enable a policy in a recipe, any user action in the zones that use the recipe and that violate the policy is denied.

The Maximum Security Recipe enables all available security zone policies and can't be modified. Assign this recipe to new security zones so that they have the maximum security posture. If necessary, you can modify the zone at any time and choose a custom recipe that does not enable all policies.

To identify new security zone policies, periodically review the Maximum Security Recipe and the[Release Notes](https://docs.oracle.com/iaas/releasenotes/). To improve your security posture over time, evaluate each new policy and, if appropriate, enable the policy in custom recipes.

## Auditing

Monitor Security Zones for policy violations. Locate access logs and other security data for Security Zones.

After you create a security zone for a compartment, it automatically prevents operations, such as creating or modifying resources, that violate the security zone's policies. However, existing resources that were created before the security zone might also violate policies. Security Zones integrates with[Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/home.htm)to identify policy violations in existing resources. Routinely monitor your security zones to identity and resolve any policy violations in a zone. See[Managing Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/managing-security-zones.htm).

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
