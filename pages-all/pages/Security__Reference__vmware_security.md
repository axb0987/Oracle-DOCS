# Securing VMware Solution
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing VMware Solution

This topic provides security information and recommendations for VMware Solution

Oracle Cloud VMware Solution allows you to create and manage VMware enabled software-defined data centers (SDDCs) in Oracle Cloud Infrastructure. See the[VMware Solution](https://docs.oracle.com/iaas/Content/VMware/home.htm)product documentation for more information.

## Security Responsibilities

To use VMware Solution securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Confidentiality: Manage and control access to sensitive information in VMware SDDCs and ESXi hosts.
- Patching : Keep vSphere, NSX-T, vSAN, and HCX software up to date with the latest security patches to prevent vulnerabilities.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure VMware Solution in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm#iam-policies)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm#network-security)

## Routine Security Tasks

After getting started with VMware Solution use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Apply the latest security patches[Patching](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm#patching)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm#auditing)

## IAM Policies

Use policies to limit access to VMware Solution.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors.

[Create an SDDC](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/vmware_security.htm#)

To let a group of administrators create an SDDC.
```

```

For more information about VMware Solution policies and to view more examples, see[Details for Oracle Cloud VMware Solution](https://docs.oracle.com/iaas/Content/Identity/Reference/ocvspolicyreference.htm).

## Network Security

Secure network access to your resources in VMware Solution

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. Use private subnets to host resources that do not require internet access. You can also configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

Oracle recommends that you use the Create SDDC workflow to create the VLANs within your VCN that are used by the SDDC resources. The workflow automatically creates route tables and security groups to control access to each VLAN. After creating the SDDC, review route tables and security groups to ensure that only the desired traffic can access SDDC resources.

The Bastion service provides restricted and time-limited access to target resources that don't have public endpoints. Using a bastion, you can let authorized users connect to target resources on private endpoints by way of Secure Shell (SSH) sessions. When connected, users can interact with the target resource by using any software or protocol supported by SSH. See[Managing Bastions](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingbastions.htm).

Use Bastion to restrict access to EXSi hosts.

Use Web Application Firewall (WAF) to create and manage protection rules for internet threats including Cross-Site Scripting (XSS), SQL Injection, and other OWASP-defined vulnerabilities. Unwanted bots can be mitigated while desirable bots are allowed to enter. WAF observes traffic to your web application over time and recommends new rules for you to configure. See[Getting Started with Edge Policies](https://docs.oracle.com/iaas/Content/WAF/Concepts/gettingstarted.htm).

## Patching

Ensure that your VMware Solution resources are running the latest security updates.

[Subscribe](https://www.broadcom.com/support/vmware-security-advisories)to[Broadcom Security Advisories](https://support.broadcom.com/web/ecx/security-advisory?)to get notified of security patch releases for VMware software stack ( vSphere, NSX-T, vSAN, and HCX ). For more information, see[Oracle Cloud VMware Solution FAQs - Patching and upgrades](https://www.oracle.com/cloud/compute/vmware/faq/#category-patching).

## Auditing

Locate access logs and other security data for VMware Solution

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
