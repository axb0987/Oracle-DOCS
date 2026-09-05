# Custom Metrics Walkthrough
- Source: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/custom-metrics-walkthrough.htm
- Fetched: 2026-09-05 02:39 CDT

# Custom Metrics Walkthrough

Walk through common use cases with custom metrics: publishing, querying, creating an alarm, and triggering the alarm to observe its`Firing`status.

## Task 1: Publish Custom Metrics

See[Publishing Custom Metrics Using the API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).

## Task 2: Query the Published Custom Metrics

See[Creating a Query for a Custom Metric](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/query-metric-custom.htm).

## Task 3: Create an Alarm

Create an alarm to get an email when the number of product orders (`productOrder`) in a 5-minute time period is higher than 100.

The following instructions show how to use Basic mode in the Console. For basic alarm instructions, see[Editing the MQL Expression When Creating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm-mql.htm)(for Advanced mode, including MQL) and[Creating an Alarm](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/create-alarm.htm)(for CLI and API).
- Open the Create alarm page:
- Open the navigation menu and select Observability &amp; Management . Under Monitoring , select Alarm Definitions .
- Select Create alarm .
- Provide values for the following fields:
- Alarm name (under Define alarm ): Too Many Product Orders
- Alarm severity : Info
- Alarm body : High number of product orders received (over 100 in a five-minute period).
- Compartment (under Metric description ): The compartment containing the resources that you want to monitor. By default, the first accessible compartment is selected.
- Metric namespace : mymetricsnamespace
- Resource group : divisionX
- Metric name : productOrder
- Interval : 5m
- Statistic : Sum
- Trigger rule :
- Operator : greater than
- Value : 100
- Trigger delay minutes : 1
- Destination (under Define alarm notifications ): Select Notifications .
- 

Create a topic : Provide values for the following fields:
- Topic name : extreme-product-order-volume
- Topic description : Channel to notify of high number of product orders received (over 100 in a five-minute period).
- Subscription protocol : Email
- Subscription email : (enter your email address)

The metric chart under the Define alarm section dynamically displays the last six hours of emitted metrics for`productOrder`under the resource group`DivisionX`.
- Select Save alarm .

Notifications sends a confirmation request to the email address configured in the new subscription.
- Confirm the new email subscription. See[Confirming a Subscription](https://docs.oracle.com/iaas/Content/Notification/Tasks/confirm-subscription.htm).

## Trigger the Alarm

Trigger the alarm to observe its`Firing`status.
- Publish a set of data points to trigger the alarm. Send a request that shows over 100 orders within 5 minutes.

For instructions, see[Publishing Custom Metrics Using the API](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
- Get the alarm's details.

For instructions, see[Getting an Alarm's Details](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/get-alarm.htm).

The alarm is in`Firing`state.
- Check your email.

For reference, see[Email (Formatted)](https://docs.oracle.com/en-us/iaas/Content/Monitoring/Tasks/../alarm-message-examples.htm#email-formatted)on the overview page.

The email indicates that the alarm is in`Firing`
