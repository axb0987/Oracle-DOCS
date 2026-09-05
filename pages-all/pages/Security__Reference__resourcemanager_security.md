# Securing Resource Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/resourcemanager_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Resource Manager

This topic provides security information and recommendations for Resource Manager.

[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)allows you to automate the provisioning of Oracle Cloud Infrastructure resources by committing the instructions to configuration files. By doing so, you ensure that provisioned resources follow the security guidelines of your organization. These configuration files capture the step-by-step provisioning instructions using a declarative language that follows the "infrastructure-as-code" model. The provisioning instructions are run as jobs.

## Security Responsibilities

To use Resource Manager securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Confidentiality: Limit the use of sensitive data in configuration and output files

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Resource Manager in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies)

## Routine Security Tasks

After getting started with Resource Manager use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Limit the use of sensitive information in configuration and output files[Confidentiality](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/resourcemanager_security.htm#confidentiality)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/resourcemanager_security.htm#auditing)

## IAM Policies

Use policies to limit access to Resource Manager.
Important  
  
Policies for managing Oracle Cloud Infrastructure resources are also required for Resource Manager operations that access resources. For example,[running an apply job](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)on a stack that includes Compute instances and subnets requires policies that grant you permissions for those resource types, in the compartments where you want to provision the resources. To see examples of policies for managing Oracle Cloud Infrastructure resources, see[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about Resource Manager policies, see[Details for Resource Manager](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm).

### Manage Stacks and Jobs

Create this policy to allow a group to[managing stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm)and[jobs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/jobs.htm)in the tenancy, as well as manage Oracle Cloud Infrastructure resources on the tenancy stacks.

```

```

Create this policy to explicitly prevent a group from[running destroy jobs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm).
Note  
  
In this policy statement, you must include the new permission to`read orm-jobs`because the third statement includes a condition that uses variables that are not relevant to listing or getting jobs.

```

```

For more details about stack permissions, see[orm-stacks](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm#ormstacks). For more details about job permissions, see[orm-jobs](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm#ormjobs).

### Manage Configuration Source Providers

Create this policy to grant a group permission to create, update, move, and delete[configuration source providers](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts)in the tenancy.

```

```

Create this policy to grant a group permission to create stacks from configuration files in[source code control systems](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__sourcecode)(using existing[configuration source providers](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts)), in addition to managing stacks and jobs.

```

```

For more details about configuration source provider permissions, see[orm-config-source-providers](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm#ormconfigsourceproviders).

### Manage Private Templates

Create this policy to grant a group permission to create, update, move, and delete[private templates](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm)in the tenancy.

```

```

Create this policy to grant a group permission to create stacks from private templates, in addition to managing stacks and jobs.

```

```

For more details about private template permissions, see[orm-templates](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm#ormtemplate).

### Manage Private Endpoints

Create this policy to grant a group permission to create, update, move, and delete[private endpoints](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm)in the tenancy, including the ability to select VCNs and subnets when creating private endpoints.

```

```

For more details about private endpoint permissions, see[orm-private-endpoints](https://docs.oracle.com/iaas/Content/Identity/Reference/resourcemanagerpolicyreference.htm#ormprivateendpoints).

## Confidentiality

Manage and control access to sensitive information in Resource Manager.

### Terraform State Files

Terraform state (`.tfstate`) can contain sensitive data, including resource IDs, passwords, and SSH keys. Use the Vault service to manage and rotate secret credentials that you use with Resource Manager.

A vault includes the encryption keys and secrets that you use to protect your data and connect to secured resources. Secrets are encrypted using master encryption keys, and store credentials such as passwords, certificates, SSH keys, or authentication tokens. Before you create and use secrets, you must create a vault and a master encryption key if they don't exist.
- [Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)
- [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)
- [Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)

For example, you require an SSH key to run remote commands and scripts on a compute instance. See[Using Remote Exec](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/usingremoteexec.htm).

Each secret is automatically assigned a secret version. When you rotate a secret, you generate a new secret version by providing new secret contents to the Vault service. Periodically rotating secret contents reduces the impact in case a secret is exposed.

To control access to the Terraform state file, you can create a security policy that limits access to reading jobs, such as the following:

```

```

Any user with the[`ORM_JOB_READ`](https://docs.oracle.com/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm#ormjobs)permission can access Terraform states files.
Note  
  
Because the permission`read orm-jobs`also affects other operations such as getting logs and Terraform configurations, we recommend segregating state files in a compartment on which a restrictive policy does not limit the ability to perform other operations.

### Terraform Configurations

The Resource Manager workflow typically includes writing or generating a Terraform configuration that is then used to manage your stack. Because the Terraform configuration can be accessed using the Resource Manager API`GetJobTfConfig`, we recommend that you do not include sensitive information in your configuration files.

Any user with the[`ORM_JOB_READ`](https://docs.oracle.com/iaas/Content/Identity/policyreference/resourcemanagerpolicyreference.htm#ormjobs)permission can access Terraform configurations.

## Network Security

Secure network access to your resources in the Resource Manager service, including private Git servers and cloud resources that you access from Resource Manager.

Instead of exposing private resources and corresponding network traffic to the public, use[private endpoints](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm)for remote access to these resources.

Use security lists , network security groups , or a combination of both to control packet-level traffic in and out of the resources in your VCN (virtual cloud network) . See[Access and Security](https://docs.oracle.com/iaas/Content/Network/Concepts/permissions.htm).

When you set up a network security group (NSG) for use with a private endpoint, include the following rules.
- 

Egress rule allowing traffic to the nonpublic resource.

Examples for a nonpublic compute instance at the IP address`192.168.227.87`:
- Minimum access:`192.168.227.87/32`
- General access to VCN and subnet CIDR:`192.168.0.0/16`
- 

Ingress rule allowing traffic from the private endpoint.

Examples for a nonpublic compute instance at the IP address`192.168.227.87`:
- Minimum access:`192.168.198.204/32`(Source Type: CIDR)
- General access from subnet CIDR:`192.168.0.0/16`

When you create a subnet in a VCN, by default the subnet is considered public and internet communication is permitted. Use private subnets to host resources that do not require internet access. You can also configure a service gateway in your VCN to allow resources on a private subnet to access other cloud services. See[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity).

You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

## Auditing

Locate access logs and other security data for Resource Manager.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).

[Example Audit Log](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/resourcemanager_security.htm#)

An audit log for a`CreateJob`event
```

```
