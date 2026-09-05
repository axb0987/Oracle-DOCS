# Creating a Topic
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-topic.htm
- Fetched: 2026-09-05 02:49 CDT

# Creating a Topic

Create a topic in Notifications.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-topic.htm#)
- 

- On the Topics list page, select Create topic . If you need help finding the list page, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- In the Create topic panel, enter the following information.

- Name : A user-friendly name for the topic. Avoid entering confidential information.

The topic name is required and must be unique across the tenancy. Validation is case-sensitive.
Note  
  
The topic name appears in[confirmation messages for new subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/confirm-subscription.htm)and in messages published to some[subscription types](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/manage-subscription.htm), such as email.
- Description : (Optional) Description for the topic. Avoid entering confidential information.
- Tags (or Show Advanced Options ): Add one or more tags to the topic. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
The new topic is immediately available and in the active state.
- 

Use the[oci ons topic create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/create.html)command and required parameters to create a topic:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[CreateTopic](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/CreateTopic)operation to create a topic.

## What's Next

Add[subscriptions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/create-subscription.htm)
