# Securing Web Application Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/waf_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Web Application Firewall

This topic provides security information and recommendations for Web Application Firewall (WAF).

## Security Responsibilities

To use Web Application Firewall (WAF) securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Web Application Firewall (WAF) in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/waf_security.htm#iam-policies)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/waf_security.htm#network-security)

## IAM Policies

Use policies to limit access to Web Application Firewall (WAF).

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For information about WAF policies, see[Getting Started with Web Application Firewall Policies](https://docs.oracle.com/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#GetStartedPolicy).

## Network Security

Secure network access to your resources in Web Application Firewall (WAF).

For information about WAF network security, see see[Getting Started with Web Application Firewall Policies](https://docs.oracle.com/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm#GetStartedPolicy)
