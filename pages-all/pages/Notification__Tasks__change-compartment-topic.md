# Moving a Topic to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-topic.htm
- Fetched: 2026-09-05 02:49 CDT

# Moving a Topic to a Different Compartment

Move a topic in Notifications to another compartment. Its associated subscriptions remain in their existing compartment.
Important  
  
To move resources between compartments, resource users must have sufficient access permissions for the compartment that the resource is being moved to and the current compartment. For more information about permissions for Notifications resources, see[Securing Notifications](https://docs.oracle.com/iaas/Content/Security/Reference/notifications_security.htm).

The moved topic is subject to policies of the destination compartment. Inherent policies in the destination compartment apply immediately and affect access to the moved resource through the Console. For more information about moving resources, see[Moving a Resource Between Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/To_move_a_resource_to_a_different_compartment.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-topic.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-topic.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/change-compartment-topic.htm#)
- 

- On the Topics list page, find the topic that you want to work with. If you need help finding the list page or the topic, see[Listing Topics](https://docs.oracle.com/en-us/iaas/Content/Notification/Tasks/../Tasks/list-topic.htm).
- From the Actions menu (three dots) for the topic, select Move resource .
- In the Move resource panel, select the destination compartment from the list.
- Select Move resource .
- 

Use the[oci ons topic change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons/topic/change-compartment.html)command and required parameters to move a topic to another compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Notifications](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ons.html).
- 

Run the[ChangeTopicCompartment](https://docs.oracle.com/iaas/api/#/en/notification/latest/NotificationTopic/ChangeTopicCompartment)
