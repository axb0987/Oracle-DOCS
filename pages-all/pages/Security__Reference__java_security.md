# Securing Java Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Java Management

This topic provides security information and recommendations for Java Management Service.

[Java Management Service](https://docs.oracle.com/iaas/jms/index.html)(JMS) monitors Java deployments on Oracle Cloud Infrastructure (OCI) instances and instances running in customer data centers. It enables you to observe and manage the use of Java in your enterprise.

## Security Responsibilities

To use JMS securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.
- Data Encryption: Oracle uses standard Oracle Cloud Infrastructure encryption for all data stored at rest in JMS. No additional configuration is necessary.

JMS users don't use encryption keys directly. Internally, JMS stores data in an autonomous database, which uses Oracle Cloud Infrastructure Vault to securely store encryption keys. Oracle manages and secures these resources.
- Data Durability: Oracle configures the JMS service for daily backups. No additional backup configuration by you is necessary.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.
- Agent Security:
- Install the agent to the instance with the minimal privilege. Do not install it as`root`.
- Obtain an installation key. Verify the key's expiration and the number of installation instances.
- Delete the key after the agent is successfully installed.
- Verify that ports or proxy are set up correctly to only allow for the agent connection to OCI.
- Configure the agent to only scan the wanted directories and with the wanted frequency.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure JMS in a new Oracle Cloud Infrastructure tenancy.

If you're new to JMS, see[Setting Up Oracle Cloud Infrastructure for Java Management Service](https://docs.oracle.com/iaas/jms/doc/getting-started-java-management-service.html#GUID-A2B4E402-108C-4510-A430-4F1B4CD90167).

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm#iam-policies)

## Routine Security Tasks

After getting started with JMS, use this checklist to identify security tasks that we recommend you perform regularly.

Task More Information
Keep the agent up to date[Patching](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm#patching)
Perform a security audit[Auditing](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm#auditing)

## IAM Policies

Use policies to limit access to JMS.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

[Allow a Group to Manage Fleets in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm#)

Create policies to allow group`FLEET_MANAGERS`to manage fleets in compartment`Fleet_Compartment`.

```

```

[Allow Instances in a Dynamic Group to Manage Agents in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/java_security.htm#)

Create policies to allow dynamic group`JMS_DYNAMIC_GROUP`to deploy and use agents in the Management Agent service in compartment`Fleet_Compartment`.

```

```

For more information about deploying management agents, see[Perform Prerequisites for Deploying Management Agents](https://docs.oracle.com/iaas/management-agents/doc/perform-prerequisites-deploying-management-agents.html).

For more information about JMS policies, see[Details for the Java Management Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/javamanagementreference.htm).

## Patching

Ensure that your JMS resources are running the latest security updates.

If you disabled the automatic upgrade feature of the Management Agent, then you must manually check for updates to the agent and the JMS plugin. See[Upgrade Management Agents](https://docs.oracle.com/iaas/management-agents/doc/management-agents-administration-tasks.html#GUID-ED7408A4-D3D7-4E4D-A25B-CB83C545B3A6).

## Auditing

Locate access logs and other security data for JMS.

The Audit service automatically records all API calls to Oracle Cloud Infrastructure resources. You can achieve your security and compliance goals by using the Audit service to monitor all user activity within your tenancy. Because all Console, SDK, and command line (CLI) calls go through our APIs, all activity from those sources is included. Audit records are available through an authenticated, filterable query API or they can be retrieved as batched files from Object Storage. Audit log contents include what activity occurred, the user that initiated it, the date and time of the request, as well as source IP, user agent, and HTTP headers of the request. See[Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm)
