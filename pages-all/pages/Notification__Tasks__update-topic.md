# Updating a Topic
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-topic.htm
- Fetched: 2026-09-05 02:50 CDT

# Updating a Topic

Update the description or tags for a topic in Notifications.

When you update a topic, you can also update its tags. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/update-topic.htm#)
- 

- On the Topics list page, select the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
The topic's details page opens.
- To update the topic's description:

- Select Edit next to Description .
- In the Edit panel, enter the value that you want.
- Select Save .
- To update the topic's tags, select Tags .
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- To add or delete a subscription in the topic, see[Actions](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/list-subscription-topic.htm#actions).
- 

Use the[oci ons topic update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/update.html)command and required parameters to update a topic:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[UpdateTopic](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/UpdateTopic)
