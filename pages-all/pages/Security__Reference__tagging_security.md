# Securing Tagging
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Tagging

This topic provides security information and recommendations for Oracle Cloud Infrastructure Tagging.

## Security Responsibilities

To use Tagging securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Tagging in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm#iam-policies)
Manage credentials using secrets[Confidentiality](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm#confidentiality)

## IAM Policies

Use policies to limit access to Tagging.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

We recommend that you give`MANAGE`permissions to a minimum set of IAM users and groups. This practice minimizes loss of data from inadvertent deletes by authorized users or from malicious actors. Only give`MANAGE`permissions to the tag administrators.

[To manage tag namespaces and the tag definitions](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm#)

The following example allows a user in the group to manage a tag namespace in the tenancy.
```

```

[To grant access to a tag namespace](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm#)

A user in group A has the required permissions to manage instances in a compartment. For the user to be able to apply a tag to an instance in a compartment, you need to add the following statement to the group A policy. This statement grants the group the access to the said namespace.
```

```

[To grant access to add tag defaults](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/tagging_security.htm#)

To add tag defaults , you need the following permissions:
- `manage tag-defaults`to access the compartment where you want to add the tag default.
- `use tag-namespaces`to access the compartment where the tag namespace resides.
- `inspect tag-namespaces`to access the tenancy.

For a group called GroupA to be able to add a tag default to a compartment called CompartmentA where the set of tag namespaces reside, write a policy with the following statements.
```

```

For more information about Tagging policies and to view more examples, see[Details for IAM without Identity Domains](https://docs.oracle.com/iaas/Content/Identity/Reference/iampolicyreference.htm).

## Access Control

In addition to creating IAM policies, lock down access to the target resources or the requesting resource by using tag-based access control. Tag-based access control provides another layer of security by restricting and granting access to a particular group of users, or resources in a compartment. .

To learn more about this feature in Tagging, see[Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm)

## Confidentiality
