# Securing Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/monitoring_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Monitoring

This topic provides security information and recommendations for the Oracle Cloud Infrastructure Monitoring service.

## Security Responsibilities

To use Monitoring securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Monitoring in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies)

## Routine Security Tasks

After getting started with Monitoring, use this checklist to identify security tasks that we recommend you perform regularly.

Monitoring does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Monitoring.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

For more information about Monitoring policies, see[Details for Health Checks](https://docs.oracle.com/iaas/Content/Identity/Reference/healthcheckpolicyreference.htm).

### Alarm Access for Groups

#### List Alarms and Alarm Status

Create this policy to allow a group to[list alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm.htm)and[list alarm statuses](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-alarm-status.htm).
```

```

#### Get Alarm Details and History

Create this policy to allow a group to[get alarm details](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm.htm)and[get alarm history](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/get-alarm-history.htm). The`read metrics`line is required for getting alarm history.
```

```

#### Manage Alarms

Create this policy to allow a group to[manage alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm), using streams and existing topics for notifications. This policy doesn't allow creation of new topics.
Note  
  
To limit the group to the permissions required for selecting streams, replace`use streams`with`{STREAM_READ, STREAM_PRODUCE}`.
```

```

#### Manage Alarms and Create Topics

Create this policy to allow a group to[manage alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm), including[creating topics (and subscriptions) for notifications](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-topic.htm)(and[using streams for notifications](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-edit-alarm-notification-stream.htm)).
Note  
  
To limit the group to the permissions required for selecting streams, replace`use streams`with`{STREAM_READ, STREAM_PRODUCE}`.
```

```

### Metric Access for Groups

#### List Metric Definitions

Create this policy to allow a group to[list metric definitions](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/list-metric.htm)in a compartment.
```

```

#### Query Metrics

Create this policy to allow a group to[query metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm)in a compartment.
```

```

#### Query Metrics for a Metric Namespace

Create this policy to allow a group to[query metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm)in a compartment, restricted to a metric namespace.
```

```

#### Publish Custom Metrics

Create this policy to allow a group to[publish custom metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)to a metric namespace, as well as view metric data, create alarms and topics, and use streams with alarms.
Note  
  
To limit the group to the permissions required for selecting streams, replace`use streams`with`{STREAM_READ, STREAM_PRODUCE}`.
```

```

### Metric Access for Resources

If you want compute instances or other resources to monitor metrics through API calls, then do the following.

For more information about compute instances calling APIs, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).
- 

Add the resources to a[dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)using its matching rules.
- 

Create a policy that allows that dynamic group to access metrics.
```

```

### Cross-Tenancy Metric Access

Use cross-tenancy metric access to share metrics with another organization that has its own tenancy. For example, share metrics with another business unit in your company, a customer of your company, or a company that provides services to your company.

To access and share resources, the administrators of both tenancies need to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words Define , Endorse , and Admit . For more information about these statements, see[Cross-Tenancy Access Policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/iam-cross-domain.htm).

#### Source Tenancy Policy Statements

The source and target tenancy administrators create policy statements that endorse a source IAM group allowed to manage resources in the destination tenancy.

Example: Endorse`MetricsAdminsUserGroup`to do anything with any metric resource in any tenancy:

```

```

To write a policy that reduces the scope of tenancy access, the source administrator must reference the destination tenancy OCID provided by the destination administrator.

Example: Endorse`MetricsAdminsUserGroup`to read metric resources in the destination tenancy (`DestinationTenancy`) only:

```

```

To allow a group to[publish metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm)to the destination tenancy, use the`manage`verb:

Example: Endorse`MetricsAdminsUserGroup`to manage metric resources in the destination tenancy (`DestinationTenancy`) only:

```

```

Example: Endorse a dynamic group (`MetricsAdminsDynamicGroup`) to read metric resources in the destination tenancy:

```

```

#### Destination Tenancy Policy Statements

Example: Endorse`MetricsAdminsUserGroup`in the source tenancy (`MetricsAdminsUserGroupInSource`) to do anything with any metric resource in your tenancy:

```

```

Example: Endorse`MetricsAdminsUserGroup`in the source tenancy (`MetricsAdminsUserGroupInSource`) to read metrics resources in the`SharedMetrics`compartment only:

```

```

Example: Endorse a dynamic group (`MetricsAdminsDynamicGroup`) in the source tenancy (`MetricsAdminsDynamicGroupInSource`) to read metric resources in the`SharedMetrics`compartment only:

```

```
