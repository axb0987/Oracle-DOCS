# Details for Integration 3
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_integrationgen3.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Integration 3

Logging details for Integration 3 logs.

## Resources
- Integration Instance

## Log Categories

API value (ID): Console (Display Name) Description
all Activity Stream Includes logging activity and activity tracing (if tracing is enabled).

## Availability

Integration 3 logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#top).

## Contents of an Integration Log

An Integration 3 log record contains the following fields:

Field Description Example
specversion Oracle Cloud Infrastructure Logging schema version. 1.0
type Category of the log. Possible values:
- Activity Stream com.oraclecloud.integration.integrationinstance.activitystream
source OCID of the integration instance. ocid1.integrationinstance.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
id Unique ID for this log entry. 38c5cc58-f9f6-11eb-bee4-0200170046fa
time Log creation time. 2021-07-10T16:15:59.469Z
oracle.loggroupid OCID of the log group. ocid1.loggroup.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
oracle.logid OCID of the service log object. ocid1.log.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
oracle.tenantid OCID of the tenancy. ocid1.tenancy.oc1.. &lt;unique_ID&gt;
oracle.compartmentid OCID of the compartment that the log group belongs to. ocid1.compartment.oc1.. &lt;unique_ID&gt;
oracle.ingestedtime The time the log was ingested by Oracle Cloud Infrastructure Logging. 2021-07-10T16:16:01.527Z
data.actionName Name of the logging activity action. log2
data.actionType The type of action, which is always LOG. LOG
data.instanceId ID for one integration/flow execution instance. 65202025
data.integrationFlowIdentifier Integration/Flow name with version. INTEGRATION!01.00.0000
data.message Service log message, which is always a logging activity message. Length of parameter is 4
data.executedTime Time at which the logging activity message was created. 2022-05-13T04:38:37.198Z
data.userId User who executed the integration/flow. &lt;user id&gt;

## Sample Integration Log
```

```
