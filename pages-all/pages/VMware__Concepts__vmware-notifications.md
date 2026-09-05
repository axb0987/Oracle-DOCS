# Configuring VMware Solution SDDC Notifications
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/vmware-notifications.htm
- Fetched: 2026-09-05 03:07 CDT

# Configuring VMware Solution SDDC Notifications

Learn about configuring notifications for your Oracle Cloud Infrastructure VMware SDDC.

The Oracle Cloud Infrastructure Notifications service broadcasts messages to distributed components through a publish-subscribe pattern, delivering secure, highly reliable, low latency and durable messages for applications hosted on Oracle Cloud Infrastructure and externally.

[Use the Notifications service](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm)to send notifications whenever VMware Solution detects a problem for which you want to be notified. You can also create an alarm that is triggered for any health defect in your ESXi bare metal host instances.

VMware Solution integrates directly with the Notifications service so you can enable notifications from the Create or Edit SDDC workflows. Alarm and notification messages are sent by email or PagerDuty protocol. One notification protocol type is used in an SDDC for all notification messages.
Note  
  
You must enable monitoring and notifications when you are first creating your cluster, or enable notifications in an existing cluster, to use this feature. For more information, see[Adding a Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/cluster-add.htm)and[Editing a Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/cluster-edit.htm). VMware Bare Metal Instance Alarms

You can enable alarms that monitor your ESXi bare metal host instances. Alarms are triggered when the number of health issues for a bare metal instance are not zero. Any non-zero value indicates a health defect.

When you enable alarms for an SDDC, all bare metal ESXi host instances in the SDDC are monitored. A separate alarm with a unique name is created for each instance. You can also choose the severity for the alarm, the interval at which the metric is emitted, and the delay time that the condition must be maintained before the alarm triggers. VMware Events

Services emit events for resources or data. For example, VMware Solution emits events for SDDCs ESXi hosts. Services emit different types of events for resources, which are distinguished as event types . SDDCs and ESXi hosts have event types of create and delete, for example. Event types are the changes that produce events by a given resource.

For general Events service information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm). SDDC-Related Events

Service Resource Event
VMware Solution VMware HCX licenses Upgrade HCX Begin
VMware Solution VMware HCX licenses Upgrade HCX End
VMware Solution VMware HCX licenses Downgrade HCX Begin
VMware Solution VMware HCX licenses Downgrade HCX End
VMware Solution VMware HCX licenses Cancel Downgrade HCX Begin
VMware Solution VMware HCX licenses Cancel Downgrade HCX End
VMware Solution VMware HCX licenses Refresh HCX Licenses Status Begin
VMware Solution VMware HCX licenses Refresh HCX Licenses Status End
VMware Solution SDDCs Create SDDC Begin
VMware Solution SDDCs Create SDDC End
VMware Solution SDDCs Delete SDDC Begin
VMware Solution SDDCs Delete SDDC End
VMware Solution SDDCs Update SDDC
VMware Solution ESXi Host Create ESXi Host Begin
VMware Solution ESXi Host Create ESXi Host End
VMware Solution ESXi Host Delete ESXi Host Begin
VMware Solution ESXi Host Delete ESXi Host End
VMware Solution ESXi Host Update ESXi Host
Compute Instance Action Begin
Compute Instance Action End
Compute Instance Change Compartment Begin
Compute Instance Change Compartment End
Compute Instance Terminate Begin
Compute Instance Terminate End
Networking Subnet Delete
Networking Subnet Update
Networking VCN Delete
Networking VCN Update
Networking VLAN Update
Networking VLAN Delete

See[Creating a VMware Solution SDDC](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/ocvssettingupsddc.htm)for instructions about enabling notifications when you use the Create workflow.

## Using the Console

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- Edit the cluster you want as described in[Editing an SDDC Cluster](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/cluster-edit.htm).
The Edit cluster panel opens.
- (Optional) In the Notifications section, enable notifications and provide information about alarms and notifications.
- (Optional) Enable instance alarms and provide information about the alarm:

- Alarm name prefix: Each bare metal ESXi host has a separate alarm created for it. Enter a prefix that will appear at the beginning of the alarm names for this SDDC.
- Alarm severity: Choose a severity for the alarm. You can choose Info, Warning, Error, or Critical. All non-zero health issues for a bare metal instance will trigger an alarm with the selected severity.
- Interval: The interval at which the metric is emitted. Default: 1 minute.
- Trigger delay: The number of minutes that the condition must be maintained before the alarm is in firing state. Default: 1 minute.
- Select an existing notification topic, or create a new one. To create a new topic, choose Create new and enter the following information:

- Topic name: Enter a friendly name for the notification topic.
- Subscription protocol: Choose the protocol that you want to use to receive your notifications. Default is email.
- Email address: Choose the email address or address list you want to send the notification to.
- Notification compartment: Choose a compartment for the notification.
- Choose events that you want to receive notifications for. By default, all available notifications are selected.

- To deselect a notification event, select the X on the notification.
- To reselect a notification event, select on the selection field and select the notification from the list.
-
