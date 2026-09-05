# Securing Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/notifications_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Notifications

This topic provides security information and recommendations for the Oracle Cloud Infrastructure Notifications service.

## Security Responsibilities

To use Notifications securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Notifications in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/notifications_security.htm#iam-policies)

## Routine Security Tasks

After getting started with Notifications, use this checklist to identify security tasks that we recommend you perform regularly.

Notifications does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Notifications.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about Notifications policies, see[Details for Notifications](https://docs.oracle.com/iaas/Content/Identity/policyreference/notificationpolicyreference.htm).

### Manage Topics and Subscriptions

Create this policy to allow group`TopicManagers`to create, update, and delete topics and subscriptions.

```

```

### Publish Messages and Manage Subscriptions

Create this policy to allow group`TopicUsers`to publish messages and to create, update, and delete subscriptions only (not topics).

```

```

### Manage Subscriptions

Create this policy to allow group`SubscriptionUsers`to create, update, and delete subscriptions only (not topics).

```

```

### Add a Function Subscription

You must have`FN_INVOCATION`permission against the function to be able to add the function as a subscription to a topic.
To authorize your function for access to other Oracle Cloud Infrastructure resources, such as compute instances, include the function in a dynamic group and create a policy to grant the dynamic group access to those resources. For more information, see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm)
