# Securing Cluster Placement Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/clusterplacementgroups_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Cluster Placement Groups

Learn about security tasks and recommendations for Cluster Placement Groups.

[Oracle Cloud Infrastructure Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/home.htm)lets you create resources that have low-latency network needs in close proximity to one another. Collocating resources can help you achieve the lowest latency possible. Cluster Placement Groups supports the deployment of resources into the same logical grouping, known as a cluster placement group, to ensure that they're placed physically near one another in an Availability domain.

## Security Responsibilities

To use Cluster Placement Groups securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Cluster Placement Groups in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[Cluster Placement Groups Policies](https://docs.oracle.com/iaas/Content/cluster-placement-groups/policy-reference.htm)

## Routine Security Tasks

Cluster Placement Groups does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Cluster Placement Groups.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

Cluster Placement Groups supports policy variables to further restrict access to cluster placement groups, including:
- `target.cluster-placement-group.id`- Restrict access to specific cluster placement groups when getting cluster placement group details or listing cluster placement groups, when creating, updating, deleting, or moving cluster placement groups, or when deploying resources into a cluster placement group.
- `target.cluster-placement-group.name`- Restrict access to specific cluster placement groups when getting cluster placement group details or listing cluster placement groups, or when creating, updating, deleting, or moving cluster placement groups.

We recommend that you give`DELETE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`DELETE`permissions to tenancy and compartment administrators.

When granting access to cluster placement groups, we recommend that you scope permissions to specific compartments. For example, create the following policy to let users in the group`NetworkAdmins`create, update, and delete all Cluster Placement Groups resources in the compartment`compartmentABC`.

```

```

For more information about Cluster Placement Groups policies, see[Cluster Placement Groups Policies](https://docs.oracle.com/iaas/Content/cluster-placement-groups/policy-reference.htm)
