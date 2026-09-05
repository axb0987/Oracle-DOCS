# Securing Network Firewall
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/network-firewall_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Network Firewall

This topic provides security information and recommendations for Service_Name.

## Security Responsibilities

To use Network Firewall securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Service_Name in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[Network Firewall Policy Reference](https://docs.oracle.com/iaas/Content/network-firewall/policies.htm)
Secure network access to resources[Network Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm)

## Routine Security Tasks

After getting started with Service_Name use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate secret credentials[Confidentiality](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/network-firewall_security.htm#confidentiality)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/network-firewall_security.htm#auditing)

## IAM Policies

Use policies to limit access to Network Firewall.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

[Restrict Group Access to Specific Firewall Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/network-firewall_security.htm#)

You can restrict access by a group to a specific firewall policy by using the specific firewall policy name (`target.display-name`), regular expression matching (`/*name/`,`/name*/`,`/*name*/`), or defined tags (`target.tag.definition.name`).

The following example of restrict access to users in the`FirewallPolicyUsers`group to a specific bucket.

```

```

You can modify this policy to restrict access to users in the group`FirewallPolicyUsers`to all firewall policies whose names are prefixed with`ProjectA_`.

```

```

You can also match for post-fix (`/*_ProjectA/`) or substring (`/*ProjectA*/`).

For more information about Network Firewall policies and to view more examples, see[Network Policy Rules and Rule Components](https://docs.oracle.com/iaas/Content/network-firewall/policies.htm).

## Confidentiality

Use the Vault service to manage and rotate secret credentials that you use with Network Firewall.

A vault includes the encryption keys and secrets that you use to protect your data and connect to secured resources. Secrets are encrypted using master encryption keys, and store credentials such as passwords, certificates, SSH keys, or authentication tokens. Before you create and use secrets, you must create a vault and a master encryption key if they don't exist.
- [Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)
- [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)
- [Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)

Each secret is automatically assigned a secret version. When you rotate a secret, you generate a new secret version by providing new secret contents to the Vault service. Periodically rotating secret contents reduces the impact in case a secret is exposed.

## Auditing

Locate access logs and other security data for Network Firewall.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

Enable Logging on specific network firewalls to monitor traffic to the firewall. For more information, see[Network Firewall Logs](https://docs.oracle.com/iaas/Content/network-firewall/logs.htm)
