# Creating an Announcement Subscription
- Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm
- Fetched: 2026-09-05 02:10 CDT

# Creating an Announcement Subscription

Create an announcement subscription to deliver specific announcements to a particular list of recipients.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_create_a_subscription.htm#)
- 

- On the Subscriptions list page, select Create announcement subscription . If you need help finding the list page, see[Viewing a List of All Announcement Subscriptions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/announcements_topic-To_view_a_list_of_all_subscriptions.htm).
- Select Name , and then enter a name for the subscription. Avoid entering confidential information.
- (Optional) Select Description , and then enter a description. Avoid entering confidential information.
- Select Compartment , and then select the compartment where you want to create the subscription.
- Under Subscription type , do one of the following:
- If you want the service to publish all announcements to the Notifications topic that you configure for this subscription, select All announcements . Then, skip to step 12 to configure the Notifications topic.
- If you want the service to publish only the announcements that meet the filter criteria that you specify, select Selected announcements only . Then, continue to the next step to configure a filter group and its filters.

Note  
  
To receive all announcements about the tenancy, including those for the root compartment and all subcompartments, we recommend creating a subscription of the type "All announcements."
- If you selected Selected announcements only in the previous step, configure a filter group with the filters that you want to apply to announcements for this subscription. Perform one of the following actions, depending on what's available:
- Under Filter group , select Name , and then enter a name for the filter group. Avoid entering confidential information.
- Under Filter group , select Filter group name , and then enter a name for the filter group. Avoid entering confidential information.

Note  
  
Include only alphanumeric, hyphen, underscore, or whitespace characters in the filter group name.
- Next, perform one of the following actions, depending on what's available:
- Select Add filter , and then select Type .
- Under Filters , select Type .
- Use the following table to configure a Value for what announcements you want to receive:

Note  
  

You can't have more than one of any particular filter type within a filter group.

When filtering announcements, the Announcements service evaluates announcements against all configured filters in a subscription. To be considered a match, an announcement must meet the criteria specified by all filters. When several possible values are configured for a particular filter, alignment with any one of the values is considered a match with that filter.

Option Description
Announcement type Specify an announcement type to include in the filter. Every announcement is assigned to a category that helps you understand the relative severity of the information in the announcement. For more information, see[Types of Announcements](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/../Concepts/announcements.htm#Types).
Compartment Specify a compartment to include in the filter. Not all announcements impact a specific compartment, but this filter lets you include announcements that do. The service performs an exact match and doesn't include announcements about child compartments of the specified compartment.

Note: If you specify the root compartment, then subscribers receive announcements about the root compartment. These announcements might pertain to resources in the root compartment. They can also describe events for which specific impacted resources haven't been identified. Announcements for the root compartment might also address impacts to the tenancy as a whole. However, if you want all announcements about the tenancy, then we recommend you create a subscription for all announcements instead of creating a subscription for selected announcements only.
Platform Specify whether you want to see announcements that impact the Oracle Cloud Infrastructure ( IaaS ) platform or announcements that impact Software as a Service ( SaaS ) applications.
Region Specify a region to include in the filter.
Resource OCID Specify up to 10 resources that you want to include in the filter by doing the following:
- Select Browse , select the checkbox next to the resource that you want to include, and then select Add to filter . (If needed, to list resources in a different compartment, select Compartment and select a compartment.)

Note: You can't combine this filter with any other type of filter in a particular filter group.
Service

Select the name of the service that you want to include. To narrow the list, you can type or otherwise enter the service name. Not all announcements impact a particular service, but this filter lets you include announcements that do.

If a filter specifies more than one service, then the Announcements service notifies subscribers of announcements impacting any of the specified services.

Note: When you create a subscription based on a service, you get all the announcements for that service. You don't need to separately create a subscription for each region where you use the service.
- If needed, select Save changes .
- (Optional) To add another filter to the filter group, perform one of the following actions, depending on what's available:
- Select Add filter , and then repeat step 8. (You can't do this if the filter you created in step 8 specified resource OCIDs. You can't combine that type of filter with any other filter in a particular filter group.)
- Select + Another filter , and then repeat step 8. (You can't do this if the filter you created in step 8 specified resource OCIDs. You can't combine that type of filter with any other filter in a particular filter group.)
- You can create more than one filter group to combine different filters to meet specific criteria. To add another filter group, perform one of the following actions, depending on what's available:
- Select Add filter group , and then repeat steps 6 through 9. (You can't do this if any filters you create specify the service Oracle Fusion Applications. You can't have that filter and have more than one filter group.)
- Select + Another filter group , and then repeat steps 6 through 9. (You can't do this if any filters you create specify the service Oracle Fusion Applications. You can't have that filter and have more than one filter group.)
- Under Display preferences , select Time zone , and then select the time zone that you prefer for announcement time stamps.
- Select Language , and then select the language that you prefer for displaying announcements delivered by email. By default, the language is set to whatever you configured in the Console language selector.
- Under Notifications topic , do one of the following:
- To use an existing Notifications topic, select Use existing topic , and then select a topic from the currently selected compartment. (If needed, to list resources in a different compartment, select Compartment and select a compartment.)
- To create a new Notifications topic, select Create new topic , and then provide the following:

Option Description
Compartment Select the compartment where you want to create the topic.
Name Enter a name for the topic. (Avoid entering confidential information.)
Description Enter a description for the topic. (Avoid entering confidential information.)
- If you chose to create a new Notifications topic, under Subscription , select Subscription protocol , and then select the protocol used by subscription endpoints. The information you must provide about the subscription endpoint depends on the protocol.
- Do one of the following:
- If you selected Email , then select Email address and enter a valid email address. For more information, see[Creating an Email Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-email.htm).
- If you selected Function , then specify the Oracle Cloud Infrastructure Functions application and function by selecting an Oracle Functions application and then Function . (If needed, select Function compartment to list resources in a different compartment.) For more information, see[Creating a Function Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-function.htm).
- If you selected HTTPS custom URL , then select URL and enter a valid HTTPS URL. For more information, see[Creating an HTTPS (Custom URL) Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-https.htm).
- If you selected PagerDuty , select URL and enter a valid PagerDuty URL. For more information, see[Creating a PagerDuty Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-pagerduty.htm).
- If you selected Slack , select URL and enter the URL of a valid Slack channel. For more information, see[Creating a Slack Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-slack.htm).
- If you selected SMS , specify a Country and Phone Number . For more information, see[Creating an SMS Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription-sms.htm).
Note  
  
SMS subscriptions are limited to the OC1 commercial realm only.
- (Optional) To add another subscription protocol to this topic, perform one of the following actions, depending on what's available:
- Select Add subscription , and then repeat the previous step.
- Select + Another subscription , and then repeat the previous step.
- When you're ready, select Create .
- 

Use the[oci announce announcement-subscription create](https://docs.oracle.com/iaas/tools/oci-cli/3.25.4/oci_cli_docs/cmdref/announce/announcement-subscription/create.html)command and required parameters to create a subscription for announcements:

```

```

For example:
```

```

Note  
  
You can't create a subscription with multiple filter groups when any filter group specifies Oracle Fusion Applications as the service.

For more information about filter group options, see[FilterGroupDetails](https://docs.oracle.com/iaas/api/#/en/announcements/latest/datatypes/FilterGroupDetails). For more information about Notifications topic options, see[CreateSubscriptionDetails](https://docs.oracle.com/iaas/api/#/en/notification/latest/datatypes/CreateSubscriptionDetails).

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateAnnouncementSubscription](https://docs.oracle.com/iaas/api/#/en/announcements/latest/AnnouncementSubscription/CreateAnnouncementSubscription)
