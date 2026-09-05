# Details for Integration Generation 2
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_integration.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Integration Generation 2

Logging details for Integration logs.

## Resources
- Integration Instance

## Log Categories

API value (ID): Console (Display Name) Description
all Activity Stream Includes logging activity and activity tracing (if tracing enabled).

## Availability

Integration logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Contents of a Integration Log

An Integration log record contains the following fields:

Field Description Example
specversion Oracle Cloud Infrastructure Logging schema version. 1.0
type Category of the log. Possible values:
- Activity Stream com.oraclecloud.integration.integrationinstance.activitystream
source Integration instance display name. DemoPublicLog
id Unique ID for this log entry. 38c5cc58-f9f6-11eb-bee4-0200170046fa
time Log creation time. 2021-07-10T16:15:59.469Z
oracle.loggroupid OCID of the log group. ocid1.loggroup.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
oracle.logid OCID of the service log object. ocid1.log.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
oracle.tenantid OCID of the tenancy. ocid1.tenancy.oc1.. &lt;unique_ID&gt;
oracle.compartmentid OCID of the compartment that the log group belongs to. ocid1.compartment.oc1.. &lt;unique_ID&gt;
oracle.ingestedtime The time the log was ingested by Oracle Cloud Infrastructure Logging. 2021-07-10T16:16:01.527Z
data.actionName actionName is optional. Available for actionType, other than invoke/trigger actionType. log2
data.actionType The type of action, such as Map, Invoke, and so on. Logger
data.operationName operationName is optional. Available only for invoke/trigger actionType. execute
data.endpointName endpointName is optional. Available only for invoke/trigger actionType. outbound
data.executionTimeInMillis Time taken in milliseconds to complete the activity. Optional field. 18
data.instanceId ID for one integration/flow execution instance. 65202025
data.integrationFlowIdentifier Integration/Flow name with version. DEMOREST!01.00.0000
data.message Service log message. This can be a logging activity message, trace message (if tracing enabled), or payload (if tracing with payload enabled). Length of parameter is 4
data.userId User who executed the integration/flow. &lt;user id&gt;

## Sample Integration Log
```

```
