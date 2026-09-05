# Securing Compute
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Compute

This topic provides security information and recommendations for Compute.

The[Compute](https://docs.oracle.com/iaas/Content/Compute/home.htm)service lets you provision and manage compute hosts, known as instances . You can create instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and terminate it when you're done with it. Any changes made to the instance's local drives are lost when you terminate it. Any saved changes to volumes attached to the instance are retained.

## Security Responsibilities

To use Compute securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Encryption and Confidentiality: Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.
- Patching : Keep software up to date with the latest security patches to prevent vulnerabilities.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Compute in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#iam-policies)
Encrypt resources using a custom key[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#data-encryption)
Secure network access to resources[Network Security](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#network-access)
Enable and configure Cloud Guard (optional)[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#cloud-guard)
Create a security zone (optional)[Security Zones](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#security-zones)

## Routine Security Tasks

After getting started with Compute use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Rotate encryption keys[Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#data-encryption)
Respond to problems detected in Cloud Guard[Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#cloud-guard)
Apply the latest security patches[Patching](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#patching)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#auditing)

## IAM Policies

Use policies to limit access to Compute.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

In all the following examples, the policies are scoped to a tenancy. However, by specifying a compartment name, they can be scoped down to specific compartment in a tenancy.

[Restrict Users Ability to Delete Instances](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#)

The following example allows the`InstanceUsers`group to launch instances, but not to delete them.

```

```

[Restrict Ability to Use Console Connections](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#)

For security compliance reasons, some customers do not want to expose the instance console to users in their tenancy. The following policy example restricts ability to create or read from consoles.

```

```

For more information about Compute policies and to view more examples, see[Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).

## Access Control

In addition to creating IAM policies, lock down access to compute instances.

### Instance Access to Other Services

You can use the Oracle Cloud Infrastructure instance principals feature to authorize instances to access other services on behalf of an IAM user.

For example, an instance might access Block Volume, Networking, Load Balancer, or Object Storage.

To use this feature, create[dynamic groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)and grant them access to service APIs. Dynamic groups allow you to group Oracle Cloud Infrastructure compute instances as "principal" actors (similar to user groups). You can then create policies to permit instances to[make API calls against Oracle Cloud Infrastructure services](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

When you create a dynamic group, rather than adding members explicitly to the group, you instead define a set of matching rules to define the group members. A short-lived private key to sign API calls is delivered through the instance metadata service (`http://169.254.169.254/opc/ <version> /identity/cert.pem`), and the key is rotated multiple times a day. For more information about accessing services from instances, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

### Access to Instance Metadata

We recommend that you limit instance metadata access to privileged users on the instance.

Instance metadata (`http://169.254.169.254`) provides predefined instance information, such as OCID and display name, and custom fields. The instance metadata can also provide short-lived credentials, such as dynamic group credentials. The following example shows how to use`iptables`to restrict instance metadata access to the`root`user.
```

```

Instances use link local addresses to access the instance metadata service (`169.254.169.254:80`), DNS (`169.254.169.254:53`), NTP (`169.254.169.254:123`), kernel updates (`169.254.0.3`), and iSCSI connections to boot volumes (`169.254.0.2:3260`,`169.254.2.0/24:3260`). You can use host-based firewalls, such as`iptables`, to ensure that only the`root`user is authorized to access these IPs. Ensure that these operating system firewall rules are not altered.

The instance metadata service is available in two versions, version 1 and version 2. IMDSv2 offers increased security compared to v1. We recommend you disable IMDSv1 and allow requests only to IMDSv2. See[Upgrading to the Instance Metadata Service v2](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2).

## Cloud Guard

Enable Cloud Guard and use it to detect and respond to security issues in Compute resources.

Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. Cloud Guard includes the following detector rules for Compute.
- Instance has a public IP address
- Instance is running an Oracle image
- Instance is not running an Oracle image
- Instance is publicly accessible
- Instance terminated
- Export image
- Import image
- Update image

For a list of all available detector rules in Cloud Guard, see[Detector Recipe Reference](https://docs.oracle.com/iaas/Content/cloud-guard/using/detect-recipes.htm).

If you haven't done so already, enable Cloud Guard and configure it to monitor the compartments that contain your resources. You can configure Cloud Guard targets to examine your entire tenancy (root compartment and all subcompartments), or to check only specific compartments. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm).

After enabling Cloud Guard, you can view and resolve detected security problems. See[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm).

## Security Zones

Using Security Zones ensures your resources in Compute comply with security best practices.

A security zone is associated with one or more compartments and a security zone recipe. When you create and update resources in a security zone's compartment, Oracle Cloud Infrastructure validates these operations against the list of security zone policies in the recipe. If any policy in the recipe is violated, then the operation is denied. The following security zone policies are available for resources in Compute.
- `deny instance_in_security_zone_​launch_from_boot_volume_​not_in_security_zone`
- `deny instance_in_security_zone_​in_subnet_not_in_security_​zone`
- `deny instance_without_​sanctioned_image`
- `deny boot_volume_not_in_security_​zone_attach_to_instance_​in_security_zone`
- `deny boot_volume_without_​vault_key`

For a list of all security zone policies, see[Security Zone Policies](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm).

To move existing resources to a compartment that is in a security zone, the resources must comply with all security zone policies in the zone's recipe. Similarly, resources in a security zone can't be moved to a compartment outside of the security zone because it might be less secure. See[Managing Security Zones](https://docs.oracle.com/iaas/Content/security-zone/using/managing-security-zones.htm).

## Data Encryption

Create and rotate encryption keys in the Vault service to protect your resources in Compute.

A vault is a logical entity that stores the encryption keys you use to protect your data. Depending on the protection mode, keys are either stored on the server, or they are stored on highly available and durable hardware security modules (HSMs). Our HSMs meet Federal Information Processing Standards (FIPS) 140-2 Security Level 3 security certification. See[Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

Although default encryption keys can be generated automatically when you create certain Oracle Cloud Infrastructure resources, we recommend that you create and manage your own custom encryption keys in the Vault service.

Instance boot volumes are encrypted by default. When you create an instance, you can use a custom encryption key to encrypt the data at rest in the boot volume. If you enable in-transit encryption for the instance, then the custom key is used for in-transit encryption as well. See[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).

Each master encryption key is automatically assigned a key version. When you rotate a key, the Vault service generates a new key version. Periodically rotating keys limits the amount of data encrypted or signed by one key version. If a key is ever comprised, key rotation reduces the risk to your data. See[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).

We recommend that you use IAM policies to strictly limit the creation, rotation, and deletion of encryption keys. See[Details for the Vault Service](https://docs.oracle.com/iaas/Content/Identity/Reference/keypolicyreference.htm).

## Network Security

Secure network access to your resources in the Compute service, including Secure Shell (SSH).

Harden SSH on all instances. The following table shows some SSH security recommendations. SSH configuration options can be set in the`sshd_config`file. On Linux, this file is at`/etc/ssh/sshd_config`.

Security Recommendation Configuration sshd_config Comments
Use public-key logins only`PubkeyAuthentication yes`Periodically review SSH public keys in the`~/.ssh/authorized_keys`file.
Disable password logins`PasswordAuthentication no`Mitigates brute-force password attacks.
Disable root logins`PermitRootLogin no`Prevents root privileges for remote logins.
Change SSH port to a non-standard port`Port <port_number>`Optional. Verify that this change does not break applications using port 22 for SSH.

Use secure SSH private keys to access instances and to prevent inadvertent disclosures. For more information about creating an SSH key pair and configuring an instance with the keys, see[Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

`Fail2ban`is an application that blocklists IP addresses involved in brute-force sign-in attempts (that is, too many failed attempts to sign in to an instance). By default,`Fail2ban`inspects SSH accesses, and you can configure it to inspect other protocols. For more information about`Fail2ban`, see[Fail2ban Main Page](http://www.fail2ban.org/wiki/index.php/Main_Page).

In addition to VCN network security groups and security lists, use host-based firewalls, such as`iptables`and`firewalld`, to restrict network access to instances by controlling ports, protocols, and packet types. Use these firewalls to prevent potential network security attack reconnaissance, such as port scanning and intrusion attempts. Custom firewall rules can be configured, saved, and initialized on every instance boot. The following example shows commands for`iptables`.

```

```

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. Use private subnets to host resources that do not require internet access. You can also configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

The Bastion service provides restricted and time-limited access to target resources that don't have public endpoints. Using a bastion, you can let authorized users connect to target resources on private endpoints by way of Secure Shell (SSH) sessions. When connected, users can interact with the target resource by using any software or protocol supported by SSH. See[Managing Bastions](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingbastions.htm).

Use Web Application Firewall (WAF) to create and manage protection rules for internet threats including Cross-Site Scripting (XSS), SQL Injection, and other OWASP-defined vulnerabilities. Unwanted bots can be mitigated while desirable bots are allowed to enter. WAF observes traffic to your web application over time and recommends new rules for you to configure. See[Getting Started with Edge Policies](https://docs.oracle.com/iaas/Content/WAF/Concepts/gettingstarted.htm).

## Patching

Ensure that your Compute resources are running the latest security updates.

Keep instance software up to date with security patches. We recommend that you periodically apply the latest available software updates to your instances. Oracle Autonomous Linux images are automatically updated with the latest patches. For Oracle Linux images, you can run the`sudo yum update`command (`sudo dnf update`on Oracle Linux 8). On Oracle Linux, you can get information about available and installed security patches using the`yum-security`plugin. The following example provides commands for`yum-security`.

```

```

Linux instances on Oracle Cloud Infrastructure can use Oracle Ksplice to apply critical kernel patches without rebooting. Ksplice can maintain specific kernel versions for Oracle Linux, CentOS, and Ubuntu. For more information, see[Oracle Ksplice](https://docs.oracle.com/iaas/oracle-linux/ksplice/index.htm).
Use Oracle Cloud Infrastructure Vulnerability Scanning Service to help improve your security posture by routinely checking hosts for potential vulnerabilities. The service generates reports with metrics and details about these vulnerabilities, and assigns each a risk level. For example:
- Ports that are unintentionally left open might be a potential attack vector to your cloud resources, or enable hackers to exploit other vulnerabilities.
- OS packages that require updates and patches to address vulnerabilities
- OS configurations that hackers might exploit See[Scanning Overview](https://docs.oracle.com/iaas/Content/scanning/using/overview.htm).

## Hardening

Configure your Compute resources for production deployments.

Establish a baseline for security hardening of Linux and Windows images running on instances. For more information about security hardening of Oracle Linux images, see[Tips for Hardening an Oracle Linux Server](http://www.oracle.com/technetwork/articles/servers-storage-admin/tips-harden-oracle-linux-1695888.html). The[Center for Internet Security Benchmarks](https://www.cisecurity.org/cis-benchmarks/)provides a comprehensive set of operating system security hardening benchmarks for various distributions of Linux and Windows Server.

### Instance Entropy

In Linux instances,`/dev/random`is non-blocking and should be used for security applications requiring random numbers.

Both bare metal and VM instances provide a high-quality and high-throughput entropy source. Instances have random number generators whose output is fed into the entropy pools used by the operating system to generate random numbers.

You can use the following commands to check the throughput and quality of the random numbers generated by`/dev/random`before using the output in applications.

```

```

## Auditing

Locate access logs and other security data for compute instances.

Various security-related events are captured in log files. We recommend that you periodically review these log files to detect any security issues. In Oracle Linux, the log files are in the folder`/var/log`. Some security-relevant log files are listed in the following table.

Log File or Directory Description
`/var/log/secure``Auth`log showing failed and successful sign-ins.
`/var/log/audit``Auditd`logs capturing system calls issued,`sudo`attempts, user sign-ins, and so on.`ausearch`and`aureport`are two tools used to query`auditd`logs.
`/var/log/yum.log`Lists packages installed or updated on instances with`yum`.
`/var/log/cloud-init.log`During instance boot,`cloud-init`can run user-provided scripts as a privileged user. For example,`cloud-init`can introduce SSH keys. We recommend that you review the`cloud-init`logs for any unrecognized commands.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/compute_security.htm#)

An audit log for a`LaunchInstance`event
```

```

If you enabled Cloud Guard in your tenancy, then it reports any user activities that are potential security concerns. Upon detecting a problem, Cloud Guard suggests corrective actions. You can also configure Cloud Guard to automatically take certain actions. See[Getting Started with Cloud Guard](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-start.htm)and[Processing Reported Problems](https://docs.oracle.com/iaas/Content/cloud-guard/using/part-problems.htm)
