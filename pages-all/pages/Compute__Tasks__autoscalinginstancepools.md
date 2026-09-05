# Autoscaling
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm
- Fetched: 2026-09-05 01:50 CDT

# Autoscaling

Autoscaling lets you automatically adjust the number or the lifecycle state of compute instances in an instance pool. This helps you provide consistent performance for your end users during periods of high demand, and helps you reduce your costs during periods of low demand.

You can apply the following types of autoscaling to an instance pool:
- [Metric-based autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#metric-based-autoscaling): An autoscaling action is triggered when a performance metric meets or exceeds a threshold.
- [Schedule-based autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#schedule-based-autoscaling): Autoscaling events take place at the specific times that you schedule.

Autoscaling is supported for virtual machine (VM) and bare metal instance pools that use standard, dense I/O, and GPU[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm).

You can perform the following tasks with Autoscaling.
- [Listing Autoscaling Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-listing-configurations_tabs.htm)
- [Creating a Metric-based Autoscaling Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-metric-based_tabs.htm)
- [Creating Schedule-based Autoscaling Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-create-schedule-based_tabs.htm)
- [Editing a Metric-based Autoscaling Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-metric-based_tabs.htm)
- [Editing a Schedule-based Autoscaling Configuration and Viewing Pool Size Forecast](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-schedule-based_tabs.htm)
- [Enabling and Disabling Autoscaling Configurations and Policies](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-enable-disable-cfg-policy_tabs.htm)
- [Deleting Autoscaling Configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-delete-configuration_tabs.htm)
- [Tracking Autoscaling Events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools-topic-tracking-autoscaling-with-events.htm)

## How Autoscaling Works: the Basics

You use autoscaling configurations to automatically manage the size and lifecycle state of your instance pools. When autoscaling automatically provisions instances in an instance pool, the pool scales out . When autoscaling removes instances from the pool, the pool scales in . You can also use autoscaling to stop and start instances in an instance pool based on a schedule.

When an instance pool scales in, instances are terminated (deleted). Instances are terminated in this order: the number of instances is balanced across[availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm), and then balanced across[fault domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). Finally, within a fault domain, the oldest instance is terminated first.

An autoscaling configuration includes one or more autoscaling policies. These policies define the criteria that trigger autoscaling actions and the actions to take. Each autoscaling configuration can either have one metric-based autoscaling policy, or multiple schedule-based autoscaling policies. You can add a maximum of 50 schedule-based autoscaling policies to an autoscaling configuration.

Each instance pool can have only one autoscaling configuration.

## Metric-Based Autoscaling

In metric-based autoscaling, you choose a performance metric to monitor, and set thresholds that the performance metric must reach to trigger an autoscaling event. When system usage meets a threshold, autoscaling dynamically resizes the instance pool in near-real time. As load increases, the pool scales out. As load decreases, the pool scales in.
Tip  
  
Avoid changing the value assigned to the initial number of instances after the pool has scaled. Lowering this value after the number of instances in the pool size has increased will cause instances in the pool to terminate. If you need to change this value, the new value should equal or exceed the number of instances currently in the pool.

Metric-based autoscaling relies on[performance metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computemetrics.htm)that are collected by the[Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm), such as CPU utilization. These performance metrics are aggregated into one-minute time periods and then averaged across all instances in the instance pool. When three consecutive values (that is, the average metrics for three consecutive minutes) meet the threshold, an autoscaling event is triggered.

A cooldown period between metric-based autoscaling events lets the system stabilize at the updated level. The cooldown period starts when the instance pool reaches the Running state. Autoscaling continues to evaluate performance metrics during the cooldown period. When the cooldown period ends, autoscaling adjusts the instance pool's size again if needed.

## Schedule-Based Autoscaling

You can use schedule-based autoscaling to scale the pool size based on demand or to stop and start instances on a schedule.

Schedule-based autoscaling is ideal for instance pools where demand behaves predictably based on a schedule, such a month, date, or time of day. Schedules can be recurring or one-time. For example:
- An instance pool has heavy use during business hours. The pool has lighter use on evenings and weekends. You can schedule the pool to scale out on weekday mornings, and to scale in on weekday evenings.
- An instance pool has high demand on New Years Eve. You can schedule the pool to scale out every year on December 30, and to scale in on January 2.
- You're releasing a new application that runs in the instance pool, and expect that many people will start using the application after the public announcement. In advance, you can schedule the instances in the pool to start on the day of release.

A schedule-based autoscaling configuration can have multiple autoscaling policies, each with a different schedule and target pool size or lifecycle action. To configure scale-in and scale-out events, you must create at least two separate policies. One policy defines the target pool size and schedule for scaling in, and the other policy defines the target pool size and schedule for scaling out. Likewise, if you want to schedule stop and start events, you must create at least two separate policies. One policy defines the lifecycle action and schedule for stopping the instances, and the other policy defines the lifecycle action and schedule for starting the instances.

After a schedule-based autoscaling policy is run, the instance pool stays at the target pool size or lifecycle state until something else changes the pool size or lifecycle state, such as a different autoscaling policy. However, if you manually change the pool size or lifecycle state, schedule-based autoscaling does not readjust the pool size or lifecycle state until the next scheduled autoscaling policy is run.

When you use schedule-based autoscaling to stop or reboot instances, the information on the instances is preserved. When the instances are started after a shutdown, they are returned to the state they were in before the shutdown occurred.

You define autoscaling schedules using cron expressions. Autoscaling uses the[Quartz cron implementation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html). You can use an online cron expression generator to verify your cron expressions; one example is[FREEFORMATTER](https://www.freeformatter.com/cron-expression-generator-quartz.html).

Provide all times in UTC.
Note  
  
Schedule-based autoscaling configurations include an attribute for cooldown period, which you see in the Console and when using the API, SDKs, and CLI. However, the cooldown period does not impact schedule-based autoscaling configurations.

### Multiple Schedule Management

If multiple schedule-based autoscaling policies exist, the schedules might conflict. If a conflict occurs, Oracle chooses one lifecycle state policy and one autoscaling policy to run. The lifecycle state policy runs first.

For the lifecycle state policy, the policy with the highest priority action is chosen. The actions are prioritized as follows, listed from highest to lowest priority:
- Force reboot
- Reboot
- Start
- Force stop
- Stop

For the autoscaling policy, the policy with the highest instance count is chosen.

To see how the autoscaling schedule is expected to affect the pool size in the future,[view the pool size forecast](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscaling-edit-schedule-based_tabs.htm).

### About Cron Expressions

A[cron expression](https://en.wikipedia.org/wiki/Cron)is a string composed of six or seven fields that represent the different parts of a schedule, such as hours or days of the week. Cron expressions use this format:

`<second> <minute> <hour> <day of month> <month> <day of week> <year>`

[Cron Expressions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#)

The following table lists the values and special characters that are allowed for each field.

Field Allowed Values Allowed Special Characters
Second

0

Note: When using the API, CLI, or SDKs for autoscaling, you must specify 0 as the value for seconds, even though other values will create a valid cron expression. You don't need to provide any value for seconds when using the Console. None
Minute 0-59 * - , /
Hour 0-23 * - , /
Day of the month 1-31 * - , ? / L W
Month 1-12 or JAN-DEC * - , /
Day of the week 1-7 or SUN-SAT * - , ? / L #
Year 1970-2099 * - , /

The special characters are described in the following table.

Special Character Description Example
* Indicates all values for a field. * in the month field means every month.
- Indicates a range of values. 8-17 in the hour field means hours 8 through 17, or 8 a.m. through 5 p.m.
, Indicates multiple values. 3,5 in the day-of-the-week field means Tuesday and Thursday.
?

Indicates no specific values.

When you want to specify a day of the month, use ? in the day-of-the-week field.

When you want to specify a day of the week, use ? in the day-of-the-month field. 0 0 10 ? * MON * means 10 a.m. on every Monday.
/ Use n / m to indicate increments. The value before the slash is the start time, and the number after the slash is the value to increment by. 0/20 in the minute field means the minutes 0, 20, and 40.
L

Last day of the week or last day of the month.

Use x L in the day-of-the-week field to indicate the last x day of the month.

Use L- n in the day-of-the-month field to indicate an offset of n days from the last day of the month.

Do not L use with multiple values or a range of values.

L in the day-of-the-month field means January 31, February 28 in non-leap years, and so on.

6L in the day-of-the-week field means the last Friday of the month.

L-5 means 5 days before the last day of the month.
W

The weekday (Monday - Friday) that is nearest to the given day.

The value does not cross months.

You can combine the L and W characters (LW) in the day-of-month field to indicate last weekday of the month.

Do not use W with multiple values or a range of values. 10W means the nearest weekday to the 10th of the month. If the 10th is a Saturday, it means Friday the 9th. If the 10th is a Sunday, it means Monday the 11th. If the 10th is a Wednesday, it means Wednesday the 10th.
# Use x # n to indicate the n th x day of the month. 5#2 means the second Thursday of the month.

### Example Cron Expressions

Use these example cron expressions as a starting point to create your own autoscaling schedules. Combine each cron expression with a target pool size to create an autoscaling policy. Then, include one or more autoscaling policies in an autoscaling configuration.

[Cron Examples](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#)

Goal: A one-time schedule with only one scaling event. At 11:00 p.m. on December 31, 2020, scale an instance pool to 100 instances. You'll need one autoscaling policy.
- 

Policy 1:
- Target pool size: 100 instances
- Execution time: 11:00 p.m. on the 31st day of December, in 2020
- Cron expression: 0 0 23 31 12 ? 2020

Goal: A one-time schedule with a scale-out event and a scale-in event. At 10:00 a.m. on March 1, 2021, scale out to 75 instances. At 4 p.m. on March 7, 2021, scale in to 30 instances. You'll need two autoscaling policies.
- 

Policy 1 - scale out:
- Target pool size: 75 instances
- Execution time: 10:00 a.m. on the 1st day of March, in 2021
- Cron expression: 0 0 10 1 3 ? 2021
- 

Policy 2 - scale in:
- Target pool size: 30 instances
- Execution time: 4:00 p.m. on the 7th day of March, in 2021
- Cron expression: 0 0 16 7 3 ? 2021

Goal: A recurring daily schedule. On weekday mornings at 8:30 a.m., scale out to 10 instances. On weekday evenings at 6 p.m., scale in to two instances. You'll need two autoscaling policies.
- 

Policy 1 - morning scale out:
- Target pool size: 10 instances
- Execution time: 8:30 a.m. on every Monday through Friday, in every month, in every year
- Cron expression: 0 30 8 ? * MON-FRI *
- 

Policy 2 - evening scale in:
- Target pool size: 2 instances
- Execution time: 6:00 p.m. on every Monday through Friday, in every month, in every year
- Cron expression: 0 0 18 ? * MON-FRI *

Goal: A recurring weekly schedule. On Tuesdays and Thursdays, scale the pool to 30 instances. On all other days of the week, scale the pool to 20 instances. You'll need two autoscaling policies.
- 

Policy 1 - Tuesday and Thursday:
- Target pool size: 30 instances
- Execution time: 1 a.m. on every Tuesday and Thursday, in every month, in every year
- Cron expression: 0 0 1 ? * TUE,THU *
- 

Policy 2 - all other days:
- Target pool size: 20 instances
- Execution time: 1 a.m. on Sunday through Monday, Wednesday, and Friday though Saturday, in every month, in every year
- Cron expression: 0 0 1 ? * SUN-MON,WED,FRI-SAT *

Goal: A recurring monthly schedule. On all days of the month, set the pool size to 20 instances. On the 15th day of the month, scale out to 40 instances. You'll need two autoscaling policies.
- 

Policy 1 - daily pool size:
- Target pool size: 20 instances
- Execution time: Midnight on every day, in every month, in every year
- Cron expression: 0 0 0 * * ? *
- 

Policy 2 - scale out:
- Target pool size: 40 instances
- Execution time: 12:05 a.m. on the 15th day of the month, in every month, in every year
- Cron expression: 0 5 0 15 * ? *

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: For a typical policy that gives access to autoscaling configurations, see[Let users manage Compute autoscaling configurations](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#autoscaling).

## Tagging Resources

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

## Requirements for Autoscaling

- You have an[instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm). Optionally, you can attach a load balancer or network load balancer to the instance pool.
- For metric-based autoscaling,[monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)on the instances in the instance pool, and the[Monitoring service is receiving metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#FindOutIfEnabled)that are emitted by the instance. When you initially create an instance pool using instances that support monitoring,[monitoring is enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm)by default, regardless of the settings in the pool's instance configuration.
- You have sufficient[service limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)
