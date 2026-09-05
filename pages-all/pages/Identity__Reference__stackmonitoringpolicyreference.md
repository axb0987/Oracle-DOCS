# Details for Stack Monitoring
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for Stack Monitoring

This topic covers details for writing policies to control access to the Stack Monitoring service.

## Individual Resource-Types

`appmgmt-monitored-instance`

`appmgmt-work-request`

`stack-monitoring-resource`

`stack-monitoring-resource-type`

`stack-monitoring-task`

`stack-monitoring-discovery-job`

`stack-monitoring-work-request`

`stack-monitoring-metric-extension`

`stack-monitoring-config`

`stack-monitoring-baselineable-metric`

`stack-monitoring-process-set`

`stack-monitoring-monitoring-template`

`stack-monitoring-defined-monitoring-template`

## Aggregate Resource-Types

`appmgmt-family`

`stack-monitoring-family`

### Comments

See the table in[Permissions Required for each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#stackmonitoringpolicyreference_topic-Permissions_Required_for_Each_API_Operation)for details of the API operations covered by each verb, for each individual resource-type.

## Supported Variables

Only the general variables are supported (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).

## Details for Verb + Resource-Type Combinations

The following tables shows the[permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[appmgmt-monitored-instance](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect APPMGMT_MONITORED_INSTANCE_INSPECT`ListMonitoredInstances`none
read INSPECT +

APPMGMT_MONITORED_INSTANCE_READ`GetMonitoredInstance`none
use READ +

APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH`PublishTopProcessesMetrics`none
manage USE +

APPMGMT_MONITORED_INSTANCE_ACTIVATE`ActivateMonitoringPlugin`none

[appmgmt-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect APPMGMT_WORK_REQUEST_INSPECT`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`none
read INSPECT+

APPMGMT_WORK_REQUEST_READ`GetWorkRequest`none

[appmgmt-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

APPMGMT_MONITORED_INSTANCE_INSPECT

APPMGMT_WORK_REQUEST_INSPECT`ListMonitoredInstances`

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`none
read INSPECT +

APPMGMT_MONITORED_INSTANCE_READ

APPMGMT_WORK_REQUEST_READ`GetMonitoredInstance`

`GetWorkRequest`none
use READ +

APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH`PublishTopProcessesMetrics`none
manage USE +

APPMGMT_MONITORED_INSTANCE_ACTIVATE`ActivateMonitoringPlugin`none

[stack-monitoring-resource](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

STACK_MONITORING_RESOURCE_INSPECT

STACK_MONITORING_RESOURCE_ASSOC_INSPECT`SearchMonitoredResources`

`SearchMonitoredResourceMembers`

`SearchMonitoredResourceAssociations`none
read INSPECT +

STACK_MONITORING_RESOURCE_READ`GetMonitoredResource`none
use READ + none none
manage USE +

STACK_MONITORING_RESOURCE_CREATE

STACK_MONITORING_RESOURCE_UPDATE

STACK_MONITORING_RESOURCE_DELETE

STACK_MONITORING_RESOURCE_MOVE

STACK_MONITORING_RESOURCE_ASSOC_CREATE

STACK_MONITORING_RESOURCE_ASSOC_DELETE`CreateMonitoredResource`

`UpdateMonitoredResource`

`DeleteMonitoredResource`

`ChangeMonitoredResourceCompartment`

`DisableExternalDatabase`

`AssociateMonitoredResources`

`DisassociateMonitoredResources`none

[stack-monitoring-resource-type](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_RESOURCE_TYPE_INSPECT`ListMonitoredResourceTypes`none
read INSPECT +

STACK_MONITORING_RESOURCE_TYPE_READ`GetMonitoredResourceType`none
use READ + none none
manage USE +

STACK_MONITORING_RESOURCE_TYPE_CREATE

STACK_MONITORING_RESOURCE_TYPE_UPDATE

STACK_MONITORING_RESOURCE_TYPE_DELETE`CreateMonitoredResourceType`

`UpdateMonitoredResourceType`

`DeleteMonitoredResourceType`none

[stack-monitoring-task](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_TASK_INSPECT`ListTasks`none
read INSPECT +

STACK_MONITORING_TASK_READ`GetTask`none
use READ + none none
manage USE +

STACK_MONITORING_TASK_CREATE

STACK_MONITORING_TASK_UPDATE

STACK_MONITORING_TASK_DELETE

STACK_MONITORING_TASK_MOVE`CreateTask`

`UpdateTask`

`DeleteTask`

`MoveTask`none

[stack-monitoring-discovery-job](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verb Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_DISCOVERY_JOB_INSPECT`ListDiscoveryJobs`none
read INSPECT +

STACK_MONITORING_DISCOVERY_JOB_READ`GetDiscoveryJob`none
use READ + none none
manage USE +

STACK_MONITORING_DISCOVERY_JOB_CREATE

STACK_MONITORING_DISCOVERY_JOB_DELETE

STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMI T`CreateDiscoveryJob`

`DeleteDiscoveryJob`

`SubmitDiscoveryJobResult`

`SubmitDiscoveryJobFailure`none

[stack-monitoring-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_WORK_REQUEST_INSPECT`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`none
read INSPECT +

STACK_MONITORING_WORK_REQUEST_READ`GetWorkRequest`none

[stack-monitoring-metric-extension](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_METRIC_EXTENSION_INSPECT`ListMetricExtensions`none
read INSPECT +

STACK_MONITORING_METRIC_EXTENSION_READ`GetMetricExtension`none
use READ +

STACK_MONITORING_METRIC_EXTENSION_ENABLE

STACK_MONITORING_METRIC_EXTENSION_DISABLE`EnableMetricExtension`

`DisableMetricExtension`none
manage USE +

STACK_MONITORING_METRIC_EXTENSION_CREATE

STACK_MONITORING_METRIC_EXTENSION_UPDATE

STACK_MONITORING_METRIC_EXTENSION_DELETE

STACK_MONITORING_METRIC_EXTENSION_TEST

STACK_MONITORING_METRIC_EXTENSION_PUBLISH

STACK_MONITORING_METRIC_EXTENSION_MOVE`CreateMetricExtension`

`UpdateMetricExtension`

`DeleteMetricExtension`

`TestMetricExtension`

`PublishMetricExtension`

`ChangeMetricExtensionCompartment`none

[stack-monitoring-config](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_CONFIG_INSPECT`ListConfigs`none
read INSPECT +

STACK_MONITORING_CONFIG_READ`GetConfig`none
use READ + none none
manage USE +

STACK_MONITORING_CONFIG_CREATE

STACK_MONITORING_CONFIG_UPDATE

STACK_MONITORING_CONFIG_DELETE

STACK_MONITORING_CONFIG_MOVE`CreateConfig`

`UpdateConfig`

`DeleteConfig`

`ChangeConfigCompartment`none

[stack-monitoring-baselineable-metric](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_BASELINEABLE_METRIC_INSPECT`ListBaselineableMetrics`none
read INSPECT +

STACK_MONITORING_BASELINEABLE_METRIC_READ`GetBaselineableMetric`none
use READ +

STACK_MONITORING_BASELINEABLE_METRIC_EVALUAT E`EvaluateBaselineableMetric`none
manage USE +

STACK_MONITORING_BASELINEABLE_METRIC_CREATE

STACK_MONITORING_BASELINEABLE_METRIC_UPDATE

STACK_MONITORING_BASELINEABLE_METRIC_DELETE

`CreateBaselineableMetric`

`UpdateBaselineableMetric`

`DeleteBaselineableMetric`none

[stack-monitoring-process-set](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_PROCESS_SET_INSPECT`ListProcessSets`none
read INSPECT +

STACK_MONITORING_PROCESS_SET_READ`GetProcessSet`none
use READ + none none
USE +

STACK_MONITORING_PROCESS_SET_CREATE  

STACK_MONITORING_PROCESS_SET_UPDATE

STACK_MONITORING_PROCESS_SET_DELETE

STACK_MONITORING_PROCESS_SET_MOVE`CreateProcessSet`

`UpdateProcessSet`

`DeleteProcessSet`

`ChangeProcessSetCompartment`none

[stack-monitoring-monitoring-template](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

STACK_MONITORING_MONITORING_TEMPLATE_INSPECT

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECT

`ListMonitoringTemplates`

`ListAlarmConditions`none
read INSPECT +

STACK_MONITORING_MONITORING_TEMPLATE_READ

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ

`GetMonitoringTemplate`

`GetAlarmCondition`none
use READ +

STACK_MONITORING_MONITORING_TEMPLATE_APPLY

STACK_MONITORING_MONITORING_TEMPLATE_UNAPPLY

`ApplyMonitoringTemplate`

`UnapplyMonitoringTemplate`none
manage USE +

STACK_MONITORING_MONITORING_TEMPLATE_CREATE

STACK_MONITORING_MONITORING_TEMPLATE_UPDATE

STACK_MONITORING_MONITORING_TEMPLATE_DELETE

STACK_MONITORING_MONITORING_TEMPLATE_EXPORT

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATE

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATE

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE

`CreateMonitoringTemplate`

`UpdateMonitoringTemplate`

`DeleteMonitoringTemplate`

`ExportMonitoringTemplate`

`CreateAlarmCondition`

`UpdateAlarmCondition`

`DeleteAlarmCondition`none

[stack-monitoring-defined-monitoring-template](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

STACK_MONITORING_DEFINED_MONITORING_TEMPLATE_INSPECT`ListDefinedMonitoringTemplates`none

[stack-monitoring-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect STACK_MONITORING_RESOURCE_INSPECT

STACK_MONITORING_RESOURCE_ASSOC_INSPECT

STACK_MONITORING_RESOURCE_TYPE_INSPECT

STACK_MONITORING_PROCESS_SET_INSPECT

STACK_MONITORING_BASELINEABLE_METRIC_INSPECT

STACK_MONITORING_CONFIG_INSPECT

STACK_MONITORING_METRIC_EXTENSION_INSPECT

STACK_MONITORING_WORK_REQUEST_INSPECT

STACK_MONITORING_DISCOVERY_JOB_INSPECT

STACK_MONITORING_TASK_INSPECT

STACK_MONITORING_MONITORING_TEMPLATE_INSPECT

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECT

STACK_MONITORING_DEFINED_MONITORING_TEMPLATE_INSPECT`SearchMonitoredResources`

`SearchMonitoredResourceMembers`

`SearchMonitoredResourceAssociations`

`ListMonitoredResourceTypes`

`ListTasks`

`ListDiscoveryJobs`

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`

`ListMetricExtensionsListConfigs`

`ListBaselineableMetrics`

`ListProcessSets`

`ListMonitoringTemplates`

`ListAlarmConditions`

`ListDefinedMonitoringTemplates`none
read INSPECT +

STACK_MONITORING_RESOURCE_READ

STACK_MONITORING_RESOURCE_TYPE_READ

STACK_MONITORING_TASK_READ

STACK_MONITORING_DISCOVERY_JOB_READ

STACK_MONITORING_WORK_REQUEST_READ

STACK_MONITORING_METRIC_EXTENSION_READ

STACK_MONITORING_CONFIG_READ

STACK_MONITORING_BASELINEABLE_METRIC_READ

STACK_MONITORING_PROCESS_SET_READ

STACK_MONITORING_MONITORING_TEMPLATE_READ

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ`GetMonitoredResource`

`GetMonitoredResourceType`

`GetTask`

`GetDiscoveryJob`

`GetWorkRequest`

`GetMetricExtension`

`GetConfig`

`GetBaselineableMetric`

`GetProcessSet`

`GetMonitoringTemplate`

`GetAlarmCondition`none
use READ +

STACK_MONITORING_METRIC_EXTENSION_ENABLE

STACK_MONITORING_METRIC_EXTENSION_DISABLE

STACK_MONITORING_BASELINEABLE_METRIC_EVALUATE

STACK_MONITORING_MONITORING_TEMPLATE_APPLY

STACK_MONITORING_MONITORING_TEMPLATE_UNAPPLY`EnableMetricExtension`

`DisableMetricExtension`

`EvaluateBaselineableMetric`

`ApplyMonitoringTemplate`

`UnapplyMonitoringTemplate`none
manage USE +

STACK_MONITORING_RESOURCE_CREATE

STACK_MONITORING_RESOURCE_UPDATE

STACK_MONITORING_RESOURCE_DELETE

STACK_MONITORING_RESOURCE_MOVE

STACK_MONITORING_RESOURCE_ASSOC_CREATE

STACK_MONITORING_RESOURCE_ASSOC_DELETE

STACK_MONITORING_RESOURCE_TYPE_CREATE

STACK_MONITORING_RESOURCE_TYPE_UPDATE

STACK_MONITORING_RESOURCE_TYPE_DELETE

STACK_MONITORING_TASK_CREATE

STACK_MONITORING_TASK_UPDATE

STACK_MONITORING_TASK_DELETE

STACK_MONITORING_TASK_MOVE

STACK_MONITORING_DISCOVERY_JOB_CREATE

STACK_MONITORING_DISCOVERY_JOB_DELETE

STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMIT

STACK_MONITORING_METRIC_EXTENSION_CREATE

STACK_MONITORING_METRIC_EXTENSION_UPDATE

STACK_MONITORING_METRIC_EXTENSION_DELETE

STACK_MONITORING_METRIC_EXTENSION_TEST

STACK_MONITORING_METRIC_EXTENSION_PUBLISH

STACK_MONITORING_METRIC_EXTENSION_MOVE

STACK_MONITORING_CONFIG_CREATE

STACK_MONITORING_CONFIG_UPDATE

STACK_MONITORING_CONFIG_DELETE

STACK_MONITORING_CONFIG_MOVE

STACK_MONITORING_BASELINEABLE_METRIC_CREATE

STACK_MONITORING_BASELINEABLE_METRIC_UPDATE

STACK_MONITORING_BASELINEABLE_METRIC_DELETE

STACK_MONITORING_PROCESS_SET_CREATE

STACK_MONITORING_PROCESS_SET_UPDATE

STACK_MONITORING_PROCESS_SET_DELETE

STACK_MONITORING_PROCESS_SET_MOVE

STACK_MONITORING_MONITORING_TEMPLATE_CREATE

STACK_MONITORING_MONITORING_TEMPLATE_UPDATE

STACK_MONITORING_MONITORING_TEMPLATE_DELETE

STACK_MONITORING_MONITORING_TEMPLATE_EXPORT

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATE

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATE

STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE`CreateMonitoredResource`

`UpdateMonitoredResource`

`DeleteMonitoredResource`

`ChangeMonitoredResourceCompartment`

`DisableExternalDatabase`

`AssociateMonitoredResources`

`DisassociateMonitoredResources`

`CreateMonitoredResourceType`

`UpdateMonitoredResourceType`

`DeleteMonitoredResourceType`

`CreateTask`

`UpdateTask`

`DeleteTask`

`MoveTask`

`CreateDiscoveryJob`

`DeleteDiscoveryJob`

`SubmitDiscoveryJobResult`

`SubmitDiscoveryJobFailure`

`CreateMetricExtension`

`UpdateMetricExtension`

`DeleteMetricExtension`

`TestMetricExtension`

`PublishMetricExtension`

`ChangeMetricExtensionCompartment`

`CreateConfig`

`UpdateConfig`

`DeleteConfig`

`ChangeConfigCompartment`

`CreateBaselineableMetric`

`UpdateBaselineableMetric`

`DeleteBaselineableMetric`

`CreateProcessSet`

`UpdateProcessSet`

`DeleteProcessSet`

`ChangeProcessSetCompartment`

`CreateMonitoringTemplate`

`UpdateMonitoringTemplate`

`DeleteMonitoringTemplate`

`ExportMonitoringTemplate`

`CreateAlarmCondition`

`UpdateAlarmCondition`

`DeleteAlarmCondition`none

## Permissions Required for each API Operation

The following tables list the API operations in alphabetical order. For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

### Appmgmt (Control Plane)

API Operation Permissions Required to Use the Operation
`ListMonitoredInstances`APPMGMT_MONITORED_INSTANCE_INSPECT
`GetMonitoredInstance`APPMGMT_MONITORED_INSTANCE_READ
`ActivateMonitoringPlugin`APPMGMT_MONITORED_INSTANCE_ACTIVATE
`PublishTopProcessesMetrics`APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH
`ListWorkRequests`APPMGMT_WORK_REQUEST_INSPECT
`GetWorkRequest`APPMGMT_WORK_REQUEST_READ
`ListWorkRequestErrors`APPMGMT_WORK_REQUEST_READ
`ListWorkRequestLogs`APPMGMT_WORK_REQUEST_READ

### Stack Monitoring (Data Plane)

API Operation PermissionsRequired to Use the Operation
`CreateMonitoredResourceType`STACK_MONITORING_RESOURCE_TYPE_CREATE
`GetMonitoredResourceType`STACK_MONITORING_RESOURCE_TYPE_READ
`UpdateMonitoredResourceType`STACK_MONITORING_RESOURCE_TYPE_UPDATE
`DeleteMonitoredResourceType`STACK_MONITORING_RESOURCE_TYPE_DELETE
`ListMonitoredResourceTypes`STACK_MONITORING_RESOURCE_TYPE_INSPECT
`CreateTask`STACK_MONITORING_TASK_CREATE
`GetTask`STACK_MONITORING_TASK_READ
`UpdateTask`STACK_MONITORING_TASK_UPDATE
`DeleteTask`STACK_MONITORING_TASK_DELETE
`ListTasks`STACK_MONITORING_TASK_INSPECT
`MoveTask`STACK_MONITORING_TASK_MOVE
`CreateMonitoredResource`STACK_MONITORING_RESOURCE_CREATE
`GetMonitoredResource`STACK_MONITORING_RESOURCE_READ
`UpdateMonitoredResource`STACK_MONITORING_RESOURCE_UPDATE
`DeleteMonitoredResource`STACK_MONITORING_RESOURCE_DELETE
`SearchMonitoredResources`STACK_MONITORING_RESOURCE_INSPECT
`SearchMonitoredResourceMembers`STACK_MONITORING_RESOURCE_INSPECT
`ChangeMonitoredResourceCompartment`STACK_MONITORING_RESOURCE_MOVE
`AssociateMonitoredResources`STACK_MONITORING_RESOURCE_ASSOC_CREATE
`DisassociateMonitoredResources`STACK_MONITORING_RESOURCE_ASSOC_DELETE
`SearchMonitoredResourceAssociations`STACK_MONITORING_RESOURCE_ASSOC_INSPECT
`DisableExternalDatabase`STACK_MONITORING_RESOURCE_UPDATE
`ListDiscoveryResourceTypes`STACK_MONITORING_DISCOVERY_RESOURCE_TYPE_INSPECT
`ListWorkRequests`STACK_MONITORING_WORK_REQUEST_INSPECT
`GetWorkRequest`STACK_MONITORING_WORK_REQUEST_READ
`ListWorkRequestErrors`STACK_MONITORING_WORK_REQUEST_READ
`ListWorkRequestLogs`STACK_MONITORING_WORK_REQUEST_READ
`CreateDiscoveryJob`STACK_MONITORING_DISCOVERY_JOB_CREATE
`ListDiscoveryJobs`STACK_MONITORING_DISCOVERY_JOB_INSPECT
`GetDiscoveryJob`STACK_MONITORING_DISCOVERY_JOB_READ
`DeleteDiscoveryJob`STACK_MONITORING_DISCOVERY_JOB_DELETE
`SubmitDiscoveryJobResult`STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMIT
`SubmitDiscoveryJobFailure`STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMIT
`ListMetricExtensions`STACK_MONITORING_METRIC_EXTENSION_INSPECT
`CreateMetricExtension`STACK_MONITORING_METRIC_EXTENSION_CREATE
`GetMetricExtension`STACK_MONITORING_METRIC_EXTENSION_READ
`UpdateMetricExtension`STACK_MONITORING_METRIC_EXTENSION_UPDATE
`DeleteMetricExtension`STACK_MONITORING_METRIC_EXTENSION_DELETE
`TestMetricExtension`STACK_MONITORING_METRIC_EXTENSION_TEST
`PublishMetricExtension`STACK_MONITORING_METRIC_EXTENSION_PUBLISH
`EnableMetricExtension`STACK_MONITORING_METRIC_EXTENSION_ENABLE
`DisableMetricExtension`STACK_MONITORING_METRIC_EXTENSION_DISABLE
`ChangeMetricExtensionCompartment`STACK_MONITORING_METRIC_EXTENSION_MOVE
`ListConfigs`STACK_MONITORING_CONFIG_INSPECT
`CreateConfig`STACK_MONITORING_CONFIG_CREATE
`GetConfig`STACK_MONITORING_CONFIG_READ
`UpdateConfig`STACK_MONITORING_CONFIG_UPDATE
`DeleteConfig`STACK_MONITORING_CONFIG_DELETE
`ChangeConfigCompartment`STACK_MONITORING_CONFIG_MOVE
`ListBaselineableMetrics`STACK_MONITORING_BASELINEABLE_METRIC_INSPECT
`CreateBaselineableMetric`STACK_MONITORING_BASELINEABLE_METRIC_CREATE
`GetBaselineableMetric`STACK_MONITORING_BASELINEABLE_METRIC_READ
`UpdateBaselineableMetric`STACK_MONITORING_BASELINEABLE_METRIC_UPDATE
`DeleteBaselineableMetric`STACK_MONITORING_BASELINEABLE_METRIC_DELETE
`EvaluateBaselineableMetric`STACK_MONITORING_BASELINEABLE_METRIC_EVALUATE
`CreateProcessSet`STACK_MONITORING_PROCESS_SET_CREATE
`ListProcessSets`STACK_MONITORING_PROCESS_SET_INSPECT
`GetProcessSet`STACK_MONITORING_PROCESS_SET_READ
`DeleteProcessSet`STACK_MONITORING_PROCESS_SET_DELETE
`UpdateProcessSet`STACK_MONITORING_PROCESS_SET_UPDATE
`ChangeProcessSetCompartment`STACK_MONITORING_PROCESS_SET_MOVE
`GetMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_READ
`CreateMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_CREATE
`UpdateMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_UPDATE
`DeleteMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_DELETE
`ExportMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_EXPORT
`ListMonitoringTemplates`STACK_MONITORING_MONITORING_TEMPLATE_INSPECT
`GetAlarmCondition`STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ
`CreateAlarmCondition`STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATE
`UpdateAlarmCondition`STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATE
`DeleteAlarmCondition`STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE
`ListAlarmConditions`STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECT
`ApplyMonitoringTemplate`STACK_MONITORING_MONITORING_TEMPLATE_APPLY
`UnapplyMonitoringTemplate`
