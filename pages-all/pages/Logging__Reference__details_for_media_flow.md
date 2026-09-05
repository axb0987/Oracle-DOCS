# Details for Media Flow
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_media_flow.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for Media Flow

Logging details for Media Flow logs.

## Resources
- Media Workflow

## Log Categories

API value (ID): Console (Display Name) Description
execution Execution Events Includes the Media Flow execution logs.

## Availability

Media Flow logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

You can enable Media Flow logs for the Media Workflow resources, which means that the executions are logged for all the jobs included in a media workflow. See[Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm#enabling_logging)and[Media Flow Logs](https://docs.oracle.com/iaas/Content/media-services/mediaflow/media-flow-logging.htm)for details.

## Contents of a Media Flow Log

Property Description Example
mediaWorkflowId OCID of the Media Workflow resource. ocid1.mediaworkflow.oc1.`<region_ID>`.`<unique_ID>`
mediaWorkflowJobId OCID of the Media Workflow Job resource. ocid1.mediaworkflowjob.oc1.`<region_ID>`.`<unique_ID>`
message Log messages exposed to user Publicly available log messages.
- Job added to queue
- Task thumbnail started
- Job status updated to SUCCEEDED
taskKey The key of the task step.
- move
- transcribe
- thumbnail
taskType The type of the task step.
- thumbnail
- getFiles
- transcribe
compartment id OCID of the compartment. ocid1.compartment.oc1.`<region_ID>`.`<unique_ID>`
ingestedtime The time when the log is ingested. 2022-09-13T16:29:51.044Z
loggroupid OCID of the log group. ocid1.loggroup.oc1.`<region_ID>`.`<unique_ID>`
logid OCID of the log. ocid1.log.oc1.`<region_ID>`.`<unique_ID>`
tenantid OCID of the tenant. ocid1.tenancy.oc1..`<region_ID>`.`<unique_ID>`
source OCID of the Media Workflow. ocid1.mediaworkflow.oc1.`<region_ID>`.`<unique_ID>`
specversion The spec version, which is 1.0 for all the logs. 1.0
time Time of ingestion. 2022-09-13T16:29:17.304Z
type Category of the log. EXECUTION

## Example Media Flow Logs
```

```

```

```
