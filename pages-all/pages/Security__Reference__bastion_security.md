# Securing Bastion
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Bastion

This topic provides security information and recommendations for Bastion.

[Oracle Cloud Infrastructure Bastion](https://docs.oracle.com/iaas/Content/Bastion/home.htm)provides restricted and time-limited access to target resources that don't have public endpoints. Bastions let authorized users connect from specific IP addresses to target resources using Secure Shell (SSH) sessions. When connected, users can interact with the target resource by using any software or protocol supported by SSH. For example, you can use the Remote Desktop Protocol (RDP) to connect to a Windows host, or use Oracle Net Services to connect to a database.

## Security Responsibilities

To use Bastion securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Network Security: Limit the nodes in your cloud network that can access bastions.
- Host Security: Configure SSH on clients and target instances for maximum security.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Bastion in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#iam-policies)
When creating bastions, restrict network access[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#network-security)

## Routine Security Tasks

After getting started with Bastion, use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Integrate target instances with IAM[Access Control](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#access-control)
Secure communication between clients and bastions[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#data-encryption)
Configure the SSH server on target instances for maximum security[Hardening](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#hardening)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#auditing)

## IAM Policies

Use policies to limit access to Bastion.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Bastion supports policy variables to further restrict access to bastions, including:
- `target.bastion-session.username`- Restrict access to specific POSIX operating system user names when creating a session that connects to a compute instance.
- `target.resource.ocid`- Restrict access to specific compute instances when creating a session.
Note  
  
We recommend that you restrict access to the`opc`user (and`ubuntu`user in Ubuntu platform images) because by default, it has`sudoer`capabilities on Oracle Cloud Infrastructure platform images.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

[Allow a group to manage all bastions and bastion sessions](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

Allow users in the group`SecurityAdmins`to create, update, and delete all Bastion resources in the entire tenancy:

```

```

[Allow a group to create any bastion session](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

Allow users in the group`BastionUsers`to create, connect to, and terminate sessions in the entire tenancy:

```

```

[Allow a group to create bastion sessions in a specific compartment and only to a specific compute instance](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

Allow users in the group`SalesAdmins`to create, connect to, and terminate sessions for a specific target host in the compartment`SalesApps`:

```

```

[Allow a group to create bastion sessions in a specific compartment and with a specific user name](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

Allow users in the group`SalesAdmins`to create, connect to, and terminate sessions in the compartment`SalesApps`and with the user`opc`:

```

```

[Allow users to only create bastion sessions with their OCI user name](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

Allow any user to create, connect to, and terminate sessions in the compartment`HRProd`, but only if they specify a user name that exactly matches their IAM user name:

```

```

For more information about Bastion policies and to view more examples, see[Bastion Policies](https://docs.oracle.com/iaas/Content/Bastion/Reference/bastionpolicyreference.htm).

## Access Control

In addition to creating IAM policies, follow these additional best practices for securing access to the targets that you connect to with Bastion.

### Enable Multifactor Authentication (MFA)

The Pluggable Authentication Module (PAM) allows you to integrate target Linux instances with IAM to perform end-user authentication with first and second factor authentication.

End users can log in to a Linux server using SSH and authenticate with their IAM user credentials. In addition, you can use the multi-factor authentication capabilities of IAM. With MFA, end users are prompted to authenticate with a second factor such as a One Time Password code sent using Email, SMS, a Mobile Authenticator application, or authenticate using security questions.
- Before configuring PAM and MFA, verify that the instance's SSH configuration meets the minimum requirements for Bastion. Refer to the section SSH Server is Not Configured Properly on Target Instance in[Troubleshooting Bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/troubleshooting_bastion.htm#managed_ssh_session_creation_failed).
- Install and configure PAM on the instance, and then enable MFA. See[Enabling MFA to Authentication into Linux](https://docs.oracle.com/iaas/Content/Identity/linuxpam/overview.htm#enable-multi-factor-authentication-authenticate-linux).

## Data Encryption

Follow these best practices for using SSH to encrypt communication between clients and bastions.

### Use a FIPS Certified Module

We recommend that you use the OpenSSH 7.6 client with Federal Information Processing Standard (FIPS) protection for all client operating systems.

For more details, see the[OpenSSL FIPS documentation](https://www.openssl.org/docs/man3.0/man7/fips_module.html)and the[Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/Certificate/3582).
Note  
  
The Oracle Linux 7.8 OpenSSH Client Cryptographic Module has not received FIPS certification yet. See[Oracle FIPS Certifications](https://www.oracle.com/corporate/security-practices/assurance/development/external-security-evaluations/fips/certifications.html).

By default, RSA key pairs are not supported in the OpenSSH client version 8 and greater. To enable RSA key pairs, you must add the following stanza to your SSH configuration.
```

```

For more details, see the[OpenSSH release notes](https://www.openssh.com/releasenotes.html).

### Don't Reuse SSH Key Pairs for Sessions

Regenerate a new ephemeral SSH key pair for each new bastion session.

Do not reuse previously generated key pairs. Create new key pairs for both port forwarding and managed SSH session types.

## Network Security

Secure network access to the resources that you connect to using Bastion.

When[creating a bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingbastions.htm), use CIDR block allowlist to specify one or more address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.

A more limited address range offers better security. Do not specify an open CIDR range like`0.0.0.0/0`.

## Hardening

Configure the SSH server on target compute instances for maximum security.

We recommend that you update the default values for these settings in`/etc/ssh/sshd_config`.

Setting Description
`MaxAuthTries`Specifies the maximum number of authentication attempts permitted per connection. After the number of failures reaches half this value, failures are logged.
`ClientAliveCountMax`Sets the number of client alive messages which can be sent without receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, the server disconnects the client, terminating the session.
`ClientAliveInterval`Sets a timeout interval in seconds after which if no data has been received from the client, the server will send a message through the encrypted channel to request a response from the client.

## Auditing

Locate access logs and other security data for Bastion.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/bastion_security.htm#)

The following is an excerpt from a log entry for the creation of a new bastion session.
```

```

If you enabled Cloud Guard in your tenancy, then it reports any user activities that are potential security concerns. Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)and[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm)
