# Securing Vulnerability Scanning
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Vulnerability Scanning

This topic provides security information and recommendations for Oracle Cloud Infrastructure Vulnerability Scanning Service.

[Vulnerability Scanning](https://docs.oracle.com/iaas/Content/scanning/home.htm)helps improve your security posture in Oracle Cloud by routinely checking hosts for potential vulnerabilities.

## Security Responsibilities

To use Vulnerability Scanning securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Database Security: Oracle is responsible for securing and patching the database used to store Vulnerability Scanning resources, including scan recipes, scan targets, and scan results.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Vulnerability Scanning in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to control who can configure Vulnerability Scanning and who can view the scanning results.[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#iam-policies)
Configure a service gateway to scan Compute instances that don't have public IP addresses.[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#network-security)

## Routine Security Tasks

After getting started with Vulnerability Scanning use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Respond to vulnerabilities detected in scan reports
- [Host Vulnerabilities Reports](https://docs.oracle.com/iaas/Content/scanning/using/host-vulnerabilities-reports.htm)
- [Scanning with Cloud Guard](https://docs.oracle.com/iaas/Content/scanning/using/scanning-with-cloud-guard.htm#scanning_with_cloud_guard)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#auditing)

## IAM Policies

Use policies to limit access to Vulnerability Scanning.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Consider the following organizational questions when creating policies for Vulnerability Scanning.
- Is there a dedicated group that's responsible for configuring Vulnerability Scanning across resources in all compartments?
- Are compartment administrators responsible for configuring Vulnerability Scanning for resources in their individual compartments?
- Is there a dedicated group that monitors the scanning results for resources in all compartments, and then communicates these results to compartment owners or resource owners?
- Do compartment administrators monitor the scanning results for resources in their individual compartments, and then communicate these results to resource owners?
- Do resource owners require access to the scanning results?

To use agent-based scanning for Compute instances (hosts), you must also give the Vulnerability Scanning service permission to deploy the Oracle Cloud Agent to the target instances.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

[Allow users in the group SecurityAdmins to scan resources in the entire tenancy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#)

A dedicated group is responsible for configuring Vulnerability Scanning across resources in all compartments.
```

```

[Allow users in the group SalesAdmins to scan resources in the compartment SalesApps](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#)

Compartment administrators are responsible for configuring Vulnerability Scanning for resources in their individual compartments.
```

```

[Allow users in the group SecurityAuditors to view the scan results for the entire tenancy](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#)

A dedicated group monitors the Vulnerability Scanning results for resources in all compartments.
```

```

[Allow users in the group SalesAuditors to view the scan results in the compartment SalesApps](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#)

Compartment administrators monitor the scanning results for resources in their individual compartments.
```

```

For more information about Vulnerability Scanning policies and to view more examples, see[Scanning IAM Policies](https://docs.oracle.com/iaas/Content/scanning/using/iam-policies.htm).

## Network Security

Use Vulnerability Scanning to scan resources that are on private subnets or don't have public IP addresses.

A Compute instance is associated with a VCN (virtual cloud network) and a subnet . When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. If an instance you want to scan is on a private subnet or has no public IP address, the VCN must include a service gateway and a route rule for the service gateway. See[Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).

## Auditing

Locate access logs and other security data for Vulnerability Scanning.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

For example, you might routinely audit all API activity related to creating, updating, and deleting scan targets. You can search the Audit service for these events:
- `CreateHostScanTarget`
- `UpdateHostScanTarget`
- `DeleteHostScanTarget`

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/scanning_security.htm#)

An excerpt from a`CreateHostScanTarget`event in the Audit service.
```

```

For a list of all Vulnerability Scanning events, see[Scanning Events](https://docs.oracle.com/iaas/Content/scanning/using/events.htm)
