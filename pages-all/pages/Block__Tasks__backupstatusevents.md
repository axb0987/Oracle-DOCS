# Using Events to Notify When a Volume Backup Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm
- Fetched: 2026-09-05 01:45 CDT

# Using Events to Notify When a Volume Backup Fails

You can use Oracle Cloud Infrastructure Events to track the status of Block Volume backup operations. See[Block Volume Backup Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__blockvolume_backup)for a list of these event types. Block Volume event types include a status attribute you can use to trigger actions based on the result of the backup operation. The status attribute value is either operationFailed or operationSucceed .

This topic describes how to create a rule in the Console that triggers an action when the backup operation fails for a volume.
Note  
  
You need to manually type the operationFailed and operationSucceed attribute values into the text box when creating a rule in the Console.

For more information about Events, see the following topics:
- [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm)
- [Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm)
- [Events and IAM Policies](https://docs.oracle.com/iaas/Content/Events/Concepts/eventspolicy.htm)
- [Managing Rules for Events](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm)
- [Block Volume Events](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#blockevents__block_volume)

## Required IAM Policy

You can restore a backup of a volume as a new volume using Block Volume.

You can restore a volume from any of your incremental or full volume backups. Both backup types enable you to restore the full volume contents to the point-in-time snapshot of the volume when the backup was taken. You don't need to keep the initial full backup or subsequent incremental backups in the backup chain and restore them in sequence, you only need to keep the backups taken for the times you care about. See[Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/blockvolumebackups.htm#backuptype)for information about full and incremental backup types.

## Prerequisites

Before you can create a rule that triggers an action when a volume backup operation fails, you should ensure that you have the completed the prerequisites outlined in[Prerequisites for Creating Rules](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm#prereq).

You should also review the information in[Setting Up for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Setup), particularly:
- Create IAM Policy for Events
- Create Notifications Topic and Subscription

## Using the Console

- Open the navigation menu and select Observability &amp; Management . Under Events Service , select Rules .
- Choose a Compartment you have permission to work in, and then select Create Rule .

Events compares the rules you create in this compartment to event messages emitted from resources in this compartment and any child compartments.
- Enter the following.
- Display Name: Specify a friendly name for the rule. You can change this name later. Avoid entering confidential information.
- Description: Specify a description of what the rule does. You can change this description later.
- In Rule Conditions , create a filter that triggers when a volume backup operation completes with operationFailed for the status attribute.
To add the volume backup create ends event type
- Select Event Type from Condition .
- Select Service Name from Service Name .
- In Event Type , select Create Volume Backup End .

To add the status attribute
- After adding an event type, select + Another Condition .
- Select Attribute from Condition .
- Select status for Attribute Name .
- Type operationFailed for Attribute Values .

This filter matches Create Volume Backup End events where the status attribute is operationFailed , indicating that the backup operation did not complete successfully.
- In Actions , specify the actions resources to trigger when the filter finds a match. Select the action resource appropriate for what you configured for Events in[Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/backupstatusevents.htm#backupstatusevents_topic-Prerequisites). For more information, see[Prerequisites for Creating Rules](https://docs.oracle.com/iaas/Content/Events/Task/managingrules.htm#prereq)and[Setting Up for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Setup).

To select a topic
- Select Notifications .
- Select the Notifications Compartment .
- Select the Topic .
- Select + Another Action and select Notifications to add another topic.
To select a stream
- Select Streaming .
- Select the Stream Compartment .
- Select the Stream .
- Select + Another Action and select Streaming to add another stream.
To select a function
- Select Functions .
- Select the Function Compartment .
- Select a Function Application .
- Select the Function .
- Select + Another Action and select Functions to add another function.
- Select Create Rule .

## Next Steps

After you have configured the rule conditions as outlined in the preceeding procedure, you can continue creating the ruleBefore you can create the rule that triggers an action when a volume backup operation fails, you should ensure that you have the completed the following steps for Events:
- [Create IAM Policy for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Create_IAM_Policy_for_Events)
- [Create Notifications Topic and Subscription](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Create_Notifications_Topic_and_Subscription)

For more information, see[Setting Up for Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm#Setup)
