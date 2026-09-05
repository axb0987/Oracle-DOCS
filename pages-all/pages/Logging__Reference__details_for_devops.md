# Details for DevOps Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Reference/details_for_devops.htm
- Fetched: 2026-09-05 02:37 CDT

# Details for DevOps Logging

Logging details for DevOps logs.

## Resources
- devopsproject

## Log Categories

API value (ID): Console (Display Name) Description
all DevOps Logs Includes all DevOps service-related logs.

## Availability

DevOps logging is available in all the regions of the[commercial realms](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Comments

You can enable DevOps logs for a given project, which means deployments are logged for all the pipelines inside that project. For more information, see[DevOps Logs](https://docs.oracle.com/iaas/Content/devops/using/devops_logs.htm).

## Contents of a DevOps Log

A DevOps log record contains the following fields:

Field Description Example
specversion Oracle Cloud Infrastructure Logging schema version. 1.0
type Category of the log. Possible values:
- build
- deployment com.oraclecloud.devops.build, com.oraclecloud.devops.deployment
source Name of the Project the log is associated with or OCID of the build pipeline to which the log belongs to. myDemoProject, ocid1.devopsbuildpipeline.oc1.`<region_ID>`.`<unique_ID>`
subject OCID of the target resource where the deployment is getting executed or OCID of the build run for the build pipeline to which the logs belong to.
Possible values for target resource:
- instance
- fnfunc
- cluster ocid1.devopsbuildrun.oc1.`<region_ID>`.`<unique_ID>`, ocid1.instance.oc1.`<region_ID>`.`<unique_ID>`
id Random UUID, unique to each log entry. e3002eaa-d717-472e-8474-d024943a0f27
time Time the log was generated in the DevOps Service. 2021-02-18T18:21:52.024Z
oracle.loggroupid OCID of the log group. ocid1. &lt;loggroup&gt; .oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
oracle.logid OCID of the service log object. ocid1.log.oc1. &lt;region_id&gt; . &lt;unique_ID&gt;
oracle.tenantid OCID of the tenancy. ocid1. &lt;tenancy&gt; .oc1.. &lt;unique_ID&gt;
oracle.compartmentid OCID of the compartment that the log group belongs to. ocid1. &lt;compartment&gt; .oc1.. &lt;unique_ID&gt;
oracle.ingestedtime The time the log was ingested by OCILogging. 2021-02-18T18:22:01.453Z
data.buildRunId OCID of the build run with which log message is associated. ocid1.devopsbuildrun.oc1.`<region_ID>`.`<unique_ID>`
data.buildPipelineId OCID of the build pipeline with which the log message is associated. ocid1.devopsbuildpipeline.oc1.`<region_ID>`.`<unique_ID>`
data.buildStageId OCID of the build pipeline stage with which the log message is associated. ocid1.devopsbuildpipelinestage.oc1.`<region_ID>`.`<unique_ID>`
data.deploymentId OCID of the deployment with which log message is associated. ocid1.devopsdeployment.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
data.deployPipelineId OCID of the deployment pipeline ID with which the log message is associated. ocid1.devopsdeploypipeline.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
data.deployStageId OCID of the deploy stage ID with which the log message is associated. ocid1.devopsdeploystage.oc1. &lt;region_ID&gt; . &lt;unique_ID&gt;
data.message DevOps service log message. Manual Approval stage: Waiting for required approvals.
data.producer Producer of the log message. Some of the logs are produced by the DevOps service code, while other logs are produced by scripts from the customer. For example, the deployment service can run scripts provided by the customer during the deployment to instance groups. Such customer-provided scripts could produce STDOUT and STDERROR messages, which are also included in the log. The producer field can distinguish them accordingly.
Possible Values:
- DEVOPS_SERVICE
- USER_SCRIPT
- USER_COMMAND DEVOPS_SERVICE

## Sample DevOps Logs

Sample build log :
```

```

Sample deployment log :
```

```

## Using CLI to View Deployment Logs
Run the following CLI command providing the given details. The compartment, log group, and the log associated with the[DevOps project](https://docs.oracle.com/iaas/Content/devops/using/devops_projects.htm). Time range, which is related to the time of deployment. You can filter the result by`deploymentId`:
- REGION, for example,`us-ashburn-1`
- START_YYYY_MM_DD, for example,`2023-01-09`
- END_YYYY_MM_DD, for example,`2023-01-10`
- COMPARTMENT_ID, for example,`ocid1.compartment.oc1..<unique_ID>`
- LOG_GROUP, for example,`ocid1.loggroup.oc1.<region_ID>.<unique_ID>`
- LOG, for example,`ocid1.log.oc1.<region_ID>.<unique_ID>`
- DEPLOYMENT_ID, for example,`ocid1.devopsdeployment.oc1.<region_ID>.<unique_ID>`

```

```

Sample log output :
```

```
