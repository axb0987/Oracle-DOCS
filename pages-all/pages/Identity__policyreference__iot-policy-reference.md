# Details for the Internet of Things Platform
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm
- Fetched: 2026-09-05 02:26 CDT

# Details for the Internet of Things Platform

Review details for writing policies to control access to your Oracle Cloud Infrastructure Internet of Things (IoT).

Permissions are managed through OCI policies. For administrators, if you're new to policies, see[How IAM Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)and[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm).

## User Policies

These policies define which users can access IoT resources and what actions they can perform. You must have the appropriate permissions in a policy to create, update, or manage IoT resources. This applies whether you use the Console, REST API, SDK, CLI, or any other interface. The policy must explicitly grant access to the IoT service and the resources you intend to work with. If you encounter an “unauthorized” or “permission denied” message, contact your administrator to verify your permissions and the compartments available to you. By default, only members of the`Administrators`group have full access to IoT resources. Other users need custom policies granting the necessary rights for their roles.

To work with IoT resources a user must be in a group and a policy must grant that group the appropriate authorization within the compartment or tenancy.

For instructions on how to create and manage policies using the Console or API, see[Overview of Working with Policies](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies.htm#overview_policies).

Example user policy syntax using resource types:

Let the specified group manage all IoT resources in the specified compartment.
```

```

Let the specified group read IoT domain groups in a specific compartment.

```

```

## Additional Required Policies

Some IoT configurations use resources from other OCI services. In addition to the policies for IoT resource types, configure the applicable policies for digital twin authentication, VCN access, metrics, and Events.

### Digital Twin Authentication Policies

A digital twin instance that ingests device data must include an authentication ID that references either a Vault secret OCID or a Certificates service certificate OCID. To configure the authentication resource and authentication ID,[create a secret for a digital twin instance](https://docs.oracle.com/iaas/Content/internet-of-things/create-secret-digital-twin.htm)or[create a certificate for a digital twin instance](https://docs.oracle.com/iaas/Content/internet-of-things/digital-twin-instance-certificate.htm).

If the digital twin instance uses a Vault secret, add this policy in the compartment that contains the secret. Replace &lt;vault-OCID&gt; with the OCID of the vault that contains the secret:
```

```

If the digital twin instance uses a certificate, add these policies in the compartment that contains the certificate:
```

```

### VCN Access Policy

After you[create an IoT domain group](https://docs.oracle.com/iaas/Content/internet-of-things/create-domain-group.htm), you can[configure data access for the IoT domain group](https://docs.oracle.com/iaas/Content/internet-of-things/configure-domain-group-access.htm)by associating one or more VCNs. To let the IoT Platform read VCNs in a specific compartment, add this policy:
```

```

### Metrics Policies

To let a group query[IoT metrics](https://docs.oracle.com/iaas/Content/internet-of-things/metrics.htm)in the compartment that contains an IoT domain, add this policy:
```

```

To let a group query metrics across the tenancy, add this policy instead:
```

```

### Events Policies

To monitor or route IoT lifecycle events, grant users permission to view the IoT resources and to create or manage Events rules in the target compartment. See the[Events prerequisites](https://docs.oracle.com/iaas/Content/internet-of-things/events.htm#prerequisites)and[Events](https://docs.oracle.com/iaas/Content/internet-of-things/events.htm)for the supported IoT event types and instructions for configuring rules and actions.

## Resource-Types

The IoT Platform provides aggregate and individual resource types for writing policies. Grant policies by individual or aggregate resource-type.

## Aggregate Resource-Types

Using aggregate resource types lets you create fewer, broader policies. For example, instead of writing separate policies to allow a group to manage[IoT domains](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-domain),[IoT domain groups](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-domain-group),[IoT Flow Runtimes](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-flow-runtime),[digital twin models](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-digital-twin-model),[digital twin instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-digital-twin-instance),[digital twin adapters](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-digital-twin-adapter), and[digital twin relationships](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-digital-twin-relationship), you can write a single policy that grants access to the aggregate resource types.

To create an IoT domain the user must have a policy for read access to the associated IoT domain group.

For example, you can assign a family to an administrator and assign users individual resource types based on a specific role. For more information, see[Manage Access and Assign Roles.](https://docs.oracle.com/iaas/process-automation/oci-process-automation/manage-access-and-assign-roles.html)
- `iot-family`: This includes every permission in the following individual resource-types:
- `iot-domain-family`
- `iot-digital-twin-family`
- `iot-domain-family`: This includes every permission in the following individual resource-types:
- `iot-domain-group`
- `iot-domain`
- `iot-flow-runtime`
- `iot-work-request`
- `iot-digital-twin-family`: This includes every permission in the following individual resource-types:
- `iot-digital-twin-model`
- `iot-digital-twin-adapter`
- `iot-digital-twin-instance`
- `iot-digital-twin-relationship`

## Individual Resource-Types

Use the individual resource-type policies to allow users to work with specific IoT resources.
- `iot-domain-group`
- `iot-domain`
- `iot-flow-runtime`
- `iot-work-request`
- `iot-digital-twin-model`
- `iot-digital-twin-instance`
- `iot-digital-twin-adapter`
- `iot-digital-twin-relationship`

## Supported Variables

To add conditions to your policies, you can either use OCI general variables or service-specific variables.

IoT platform supports the[General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)for use with resources.

No service-specific variables.

## Details for Verbs + Resource Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`, to`read`,`use`, and then`manage`. For example, a group that can use a resource can also inspect and read that resource.

There are various OCI verbs and resource types you can use to create a policy.

Examples defining policies using specific permissions:

```

```

```

```

## iot-family

The following sections describe the permissions and API operations covered by each verb for IoT service. The level of access is cumulative as you go from`inspect`to`read`, to`use`, to`manage`.

Let the specified group manage all IoT resources in the specified compartment.
```

```

The`iot-family`contains all of the following permissions.

Verbs Permissions APIs Fully Covered
inspect

IOT_DOMAIN_GROUP_INSPECT

IOT_DOMAIN_INSPECT

IOT_FLOW_RUNTIME_INSPECT

IOT_WORK_REQUEST_INSPECT

IOT_DIGITAL_TWIN_MODEL_INSPECT

IOT_DIGITAL_TWIN_ADAPTER_INSPECT

IOT_DIGITAL_TWIN_INSTANCE_INSPECT

IOT_DIGITAL_TWIN_RELATIONSHIP_INSPECT

`ListIotDomainGroups`

`ListIotDomains`

`ListIotFlowRuntimes`

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`

`ListDigitalTwinModels`

`ListDigitalTwinAdapters`

`ListDigitalTwinInstances`

`ListDigitalTwinRelationships`
read INSPECT +

IOT_DOMAIN_GROUP_READ

IOT_DOMAIN_READ

IOT_FLOW_RUNTIME_READ

IOT_FLOW_RUNTIME_FLOWS_READ

IOT_WORK_REQUEST_READ

IOT_DIGITAL_TWIN_MODEL_READ

IOT_DIGITAL_TWIN_ADAPTER_READ

IOT_DIGITAL_TWIN_INSTANCE_READ

IOT_DIGITAL_TWIN_RELATIONSHIP_READ

`GetIotDomainGroup`

`GetIotDomain`

`GetIotFlowRuntime`

`GetIotFlowRuntimeFlows`

`GetWorkRequest`

`GetDigitalTwinModel`

`GetDigitalTwinModelSpec`

`GetDigitalTwinAdapter`

`GetDigitalTwinInstance`

`GetDigitalTwinInstanceContent`

`GetDigitalTwinRelationship`
use READ +

IOT_DOMAIN_GROUP_UPDATE

IOT_DOMAIN_UPDATE

IOT_FLOW_RUNTIME_UPDATE

IOT_FLOW_RUNTIME_FLOWS_UPDATE

IOT_DIGITAL_TWIN_MODEL_UPDATE

IOT_DIGITAL_TWIN_ADAPTER_UPDATE

IOT_DIGITAL_TWIN_INSTANCE_UPDATE

IOT_DIGITAL_TWIN_INSTANCE_COMMAND_INVOKE

IOT_DIGITAL_TWIN_RELATIONSHIP_UPDATE

`UpdateIotDomainGroup`

`ConfigureIotDomainGroupDataAccess`

`UpdateIotDomain`

`ConfigureIotDomainDataAccess`

`ChangeIotDomainDataRetentionPeriod`

`UpdateIotFlowRuntime`

`UpdateIotFlowRuntimeFlows`

`UpdateDigitalTwinModel`

`UpdateDigitalTwinAdapter`

`UpdateDigitalTwinInstance`

`InvokeRawCommand`

`UpdateDigitalTwinRelationship`
manage USE +

IOT_DOMAIN_GROUP_CREATE

IOT_DOMAIN_GROUP_DELETE

IOT_DOMAIN_GROUP_MOVE

IOT_DOMAIN_CREATE

IOT_DOMAIN_DELETE

IOT_DOMAIN_MOVE

IOT_FLOW_RUNTIME_CREATE

IOT_FLOW_RUNTIME_DELETE

IOT_FLOW_RUNTIME_MOVE

IOT_DIGITAL_TWIN_MODEL_CREATE

IOT_DIGITAL_TWIN_MODEL_DELETE

IOT_DIGITAL_TWIN_ADAPTER_CREATE

IOT_DIGITAL_TWIN_ADAPTER_DELETE

IOT_DIGITAL_TWIN_INSTANCE_CREATE

IOT_DIGITAL_TWIN_INSTANCE_DELETE

IOT_DIGITAL_TWIN_RELATIONSHIP_CREATE

IOT_DIGITAL_TWIN_RELATIONSHIP_DELETE

`CreateIotDomainGroup`

`DeleteIotDomainGroup`

`ChangeIotDomainGroupCompartment`

`CreateIotDomain`

`DeleteIotDomain`

`ChangeIotDomainCompartment`

`CreateIotFlowRuntime`

`DeleteIotFlowRuntime`

`ChangeIotFlowRuntimeCompartment`

`CreateDigitalTwinModel`

`DeleteDigitalTwinModel`

`CreateDigitalTwinAdapter`

`DeleteDigitalTwinAdapter`

`CreateDigitalTwinInstance`

`DeleteDigitalTwinInstance`

`CreateDigitalTwinRelationship`

`DeleteDigitalTwinRelationship`

## iot-domain-family

Let the specified group manage all IoT domain resources in the specified compartment.
```

```

Note  
  
To create an IoT domain the user must have a policy for at least read access to the associated IoT domain group.

Verbs Permissions APIs Fully Covered
inspect

IOT_DOMAIN_GROUP_INSPECT

IOT_DOMAIN_INSPECT

IOT_FLOW_RUNTIME_INSPECT

IOT_WORK_REQUEST_INSPECT

`ListIotDomainGroups`

`ListIotDomains`

`ListIotFlowRuntimes`

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`
read INSPECT +

IOT_DOMAIN_GROUP_READ

IOT_DOMAIN_READ

IOT_FLOW_RUNTIME_READ

IOT_FLOW_RUNTIME_FLOWS_READ

IOT_WORK_REQUEST_READ

`GetIotDomainGroup`

`GetIotDomain`

`GetIotFlowRuntime`

`GetIotFlowRuntimeFlows`

`GetWorkRequest`
use READ +

IOT_DOMAIN_GROUP_UPDATE

IOT_DOMAIN_UPDATE

IOT_FLOW_RUNTIME_UPDATE

IOT_FLOW_RUNTIME_FLOWS_UPDATE

`UpdateIotDomainGroup`

`ConfigureIotDomainGroupDataAccess`

`UpdateIotDomain`

`ConfigureIotDomainDataAccess`

`ChangeIotDomainDataRetentionPeriod`

`UpdateIotFlowRuntime`

`UpdateIotFlowRuntimeFlows`
manage USE +

IOT_DOMAIN_GROUP_CREATE

IOT_DOMAIN_GROUP_DELETE

IOT_DOMAIN_GROUP_MOVE

IOT_DOMAIN_CREATE

IOT_DOMAIN_DELETE

IOT_DOMAIN_MOVE

IOT_FLOW_RUNTIME_CREATE

IOT_FLOW_RUNTIME_DELETE

IOT_FLOW_RUNTIME_MOVE

`CreateIotDomainGroup`

`DeleteIotDomainGroup`

`ChangeIotDomainGroupCompartment`

`CreateIotDomain`

`DeleteIotDomain`

`ChangeIotDomainCompartment`

`CreateIotFlowRuntime`

`DeleteIotFlowRuntime`

`ChangeIotFlowRuntimeCompartment`

## iot-digital-twin-family

Let the specified group manage all IoT digital twin resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_DIGITAL_TWIN_MODEL_INSPECT

IOT_DIGITAL_TWIN_ADAPTER_INSPECT

IOT_DIGITAL_TWIN_INSTANCE_INSPECT

IOT_DIGITAL_TWIN_RELATIONSHIP_INSPECT

`ListDigitalTwinModels`

`ListDigitalTwinAdapters`

`ListDigitalTwinInstances`

`ListDigitalTwinRelationships`
read INSPECT +

IOT_DIGITAL_TWIN_MODEL_READ

IOT_DIGITAL_TWIN_ADAPTER_READ

IOT_DIGITAL_TWIN_INSTANCE_READ

IOT_DIGITAL_TWIN_RELATIONSHIP_READ

`GetDigitalTwinModel`

`GetDigitalTwinModelSpec`

`GetDigitalTwinAdapter`

`GetDigitalTwinInstance`

`GetDigitalTwinInstanceContent`

`GetDigitalTwinRelationship`
use READ +

IOT_DIGITAL_TWIN_MODEL_UPDATE

IOT_DIGITAL_TWIN_ADAPTER_UPDATE

IOT_DIGITAL_TWIN_INSTANCE_UPDATE

IOT_DIGITAL_TWIN_INSTANCE_COMMAND_INVOKE

IOT_DIGITAL_TWIN_RELATIONSHIP_UPDATE

`UpdateDigitalTwinModel`

`UpdateDigitalTwinAdapter`

`UpdateDigitalTwinInstance`

`InvokeRawCommand`

`UpdateDigitalTwinRelationship`
manage USE +

IOT_DIGITAL_TWIN_MODEL_CREATE

IOT_DIGITAL_TWIN_MODEL_DELETE

IOT_DIGITAL_TWIN_ADAPTER_CREATE

IOT_DIGITAL_TWIN_ADAPTER_DELETE

IOT_DIGITAL_TWIN_INSTANCE_CREATE

IOT_DIGITAL_TWIN_INSTANCE_DELETE

IOT_DIGITAL_TWIN_RELATIONSHIP_CREATE

IOT_DIGITAL_TWIN_RELATIONSHIP_DELETE

`CreateDigitalTwinModel`

`DeleteDigitalTwinModel`

`CreateDigitalTwinAdapter`

`DeleteDigitalTwinAdapter`

`CreateDigitalTwinInstance`

`DeleteDigitalTwinInstance`

`CreateDigitalTwinRelationship`

`DeleteDigitalTwinRelationship`

## iot-domain-group

Let the specified group manage all IoT domain group resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect IOT_DOMAIN_GROUP_INSPECT

`ListIotDomainGroups`
read INSPECT +

IOT_DOMAIN_GROUP_READ

`GetIotDomainGroup`
use READ +

IOT_DOMAIN_GROUP_UPDATE

`UpdateIotDomainGroup`

`ConfigureIotDomainGroupDataAccessDetails`
manage USE +

IOT_DOMAIN_GROUP_CREATE

IOT_DOMAIN_GROUP_DELETE

IOT_DOMAIN_GROUP_MOVE

`CreateIotDomainGroup`

`DeleteIotDomainGroup`

`ChangeIotDomainGroupCompartment`

## iot-domain

Let the specified group manage all IoT domain resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect IOT_DOMAIN_INSPECT

`ListIotDomains`
read INSPECT +

IOT_DOMAIN_READ

`GetIotDomain`
use READ +

IOT_DOMAIN_UPDATE

`UpdateIotDomain`

`ConfigureIotDomainDataAccess`

`ChangeIotDomainDataRetentionPeriod`
manage USE +

IOT_DOMAIN_CREATE

IOT_DOMAIN_DELETE

IOT_DOMAIN_MOVE

`CreateIotDomain`

`DeleteIotDomain`

`ChangeIotDomainCompartment`

## iot-flow-runtime

Let the specified group manage all IoT Flow Runtime resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_FLOW_RUNTIME_INSPECT

`ListIotFlowRuntimes`
read INSPECT +

IOT_FLOW_RUNTIME_READ

IOT_FLOW_RUNTIME_FLOWS_READ

`GetIotFlowRuntime`

`GetIotFlowRuntimeFlows`
use READ +

IOT_FLOW_RUNTIME_UPDATE

IOT_FLOW_RUNTIME_FLOWS_UPDATE

`UpdateIotFlowRuntime`

`UpdateIotFlowRuntimeFlows`
manage USE +

IOT_FLOW_RUNTIME_CREATE

IOT_FLOW_RUNTIME_DELETE

IOT_FLOW_RUNTIME_MOVE

`CreateIotFlowRuntime`

`DeleteIotFlowRuntime`

`ChangeIotFlowRuntimeCompartment`

## Policies: Creating a Flow Runtime With a Log

Before you[create a Flow Runtime](https://docs.oracle.com/iaas/Content/internet-of-things/create-iot-flow-runtime.htm)with a service log, create one of the following policy sets. The required permissions depend on whether you specify an existing log or only a log group.

Existing log: If you specify both a log group and an existing log, grant the IoT domain permission to read log groups and grant the Flow Runtime permission to use log content:
```

```

Automatic log creation: If you specify only a log group, OCI IoT creates the log automatically. Grant the IoT domain permission to manage log groups and grant the Flow Runtime permission to use log content:
```

```

Create the applicable policy set in the compartment that contains the log group or in an appropriate parent compartment. Replace &lt;customer-log-compartment&gt; with the name of the compartment that contains the log group, &lt;domain-compartment-ocid&gt; with the OCID of the compartment that contains the IoT domain, and &lt;flow-runtime-compartment-ocid&gt; with the OCID of the compartment that contains the Flow Runtime.

## Policies for Flow Runtime Resource Principals

The policies in the[iot-flow-runtime](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#iot-flow-runtime)section control who can create and manage Flow Runtime resources.

The policies in this section let a Flow Runtime resource principal access other OCI resources. Configure a supported OCI node to use Resource Principal authentication when you want the Flow Runtime to access a target OCI resource without storing a user's API-signing key in the flow.

A dynamic group and an IAM policy work together:
- Dynamic group: A dynamic group identifies which Flow Runtime resource principals are members. A Flow Runtime that matches the dynamic group rule automatically becomes a member. See[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).
- IAM policy: An IAM policy grants the dynamic group permission to perform specified operations on target OCI resources.

This approach centralizes access management in IAM and supports least privilege. Limit the dynamic group to the intended Flow Runtimes, and grant only the permissions required for the target service, compartment, and resource.
Note  
  
When you create a Flow runtime with a log, use[Logging policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iot-policy-reference.htm#flow-runtime-logging-policy)do not use this dynamic group. They authorize the IoT domain and Flow Runtime by using`any-user`with`request.principal.*`conditions.

Required when What the policy does Where to create the policy Related scenario
Connecting to a customer Autonomous AI Database Lets the Flow Runtime resource principal connect to the approved database. The compartment containing the database or an appropriate parent compartment.[Monitor Normalized IoT Data, Send Commands, and Email Alerts](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm)
Using an Object Storage node Lets the resource principal download objects or, when explicitly granted, create and overwrite objects. The compartment containing the bucket.[Ingesting Batch Data from Object Storage](https://docs.oracle.com/iaas/Content/internet-of-things/ingest-batch-data-flow-runtime.htm)
Using an OCI Notifications node Lets the resource principal publish messages to an approved topic. The compartment containing the topic.[Monitor Normalized IoT Data, Send Commands, and Email Alerts](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm)
Using IoT command Lets the resource principal invoke commands. The compartment containing the IoT resources.[Monitor Normalized IoT Data, Send Commands, and Email Alerts](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm)

Create a dynamic group with a matching rule for the[Flow Runtimes](https://docs.oracle.com/iaas/Content/internet-of-things/flow-runtimes.htm)that need access. The following rule includes every Flow Runtime in one compartment:
```

```

Replace &lt;flow-runtime-dynamic-group&gt; in the following examples with the name of this dynamic group.

## Autonomous AI Database Policy

If the Flow Runtime needs database access, use this policy to let the Flow Runtime resource principal connect to a customer Autonomous AI Database in a specific compartment. For an example, see[Monitor Normalized IoT Data, Send Commands, and Email Alerts](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm).
```

```

Note  
  
The database must also be configured for IAM authentication and must map the resource principal to an authorized database user.

## Object Storage Policies

If the Flow Runtime needs to use Object Storage, as in[Ingesting Batch Data from Object Storage](https://docs.oracle.com/iaas/Content/internet-of-things/ingest-batch-data-flow-runtime.htm), apply the following policies.

Let the Flow Runtime resource principal download objects from a specific bucket.
```

```

When the flow must upload new objects or overwrite existing objects, add this policy:
```

```

## Notifications Policy

If you complete the[monitoring and action scenario](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm), choose one of the following policy examples to let the Flow Runtime resource principal publish messages to the scenario's Notifications topic.

Granular permission (least privilege):
```

```

Verb with individual resource type (broader access): The`use`verb includes publishing and the other permissions that it covers for`ons-topics`.
```

```

## IoT Node Policies

If you complete the[monitoring and action scenario](https://docs.oracle.com/iaas/Content/internet-of-things/egress-iot-flow-runtime.htm), choose one of the following policy examples to let the Flow Runtime resource principal invoke a command on a digital twin instance.

Granular permission (least privilege):
```

```

Verb with individual resource type (broader access): The`use`verb includes command invocation and the other permissions that it covers for`iot-digital-twin-instance`.
```

```

## iot-work-request

Let the specified group manage all IoT work request resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_WORK_REQUEST_INSPECT

`ListWorkRequests`

`ListWorkRequestErrors`

`ListWorkRequestLogs`
read INSPECT+

IOT_WORK_REQUEST_READ

`GetWorkRequest`

## iot-digital-twin-model

Let the specified group manage all IoT digital twin model resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_DIGITAL_TWIN_MODEL_INSPECT`ListDigitalTwinModels`
read INSPECT+

IOT_DIGITAL_TWIN_MODEL_READ

`GetDigitalTwinModel`

`GetDigitalTwinModelSpec`
use READ +

IOT_DIGITAL_TWIN_MODEL_UPDATE`UpdateDigitalTwinModel`
manage USE +

IOT_DIGITAL_TWIN_MODEL_CREATE

IOT_DIGITAL_TWIN_MODEL_DELETE

`CreateDigitalTwinModel`

`DeleteDigitalTwinModel`

## iot-digital-twin-adapter

Let the specified group manage all IoT digital twin adapter resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_DIGITAL_TWIN_ADAPTER_INSPECT`ListDigitalTwinAdapters`
read INSPECT+

IOT_DIGITAL_TWIN_ADAPTER_READ`GetDigitalTwinAdapter`
use READ +

IOT_DIGITAL_TWIN_ADAPTER_UPDATE`UpdateDigitalTwinAdapter`
manage USE +

IOT_DIGITAL_TWIN_ADAPTER_CREATE

IOT_DIGITAL_TWIN_ADAPTER_DELETE

`CreateDigitalTwinAdapter`

`DeleteDigitalTwinAdapter`

## iot-digital-twin-instance

Let the specified group manage all IoT digital twin instance resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect

IOT_DIGITAL_TWIN_INSTANCE_INSPECT`ListDigitalTwinInstances`
read INSPECT+

IOT_DIGITAL_TWIN_INSTANCE_READ

`GetDigitalTwinInstance`

`GetDigitalTwinInstanceContent`
use READ +

IOT_DIGITAL_TWIN_INSTANCE_UPDATE`UpdateDigitalTwinInstance`
use READ +

IOT_DIGITAL_TWIN_INSTANCE_COMMAND_INVOKE

`InvokeRawCommand`
manage USE +

IOT_DIGITAL_TWIN_INSTANCE_CREATE

IOT_DIGITAL_TWIN_INSTANCE_DELETE

`CreateDigitalTwinInstance`

`DeleteDigitalTwinInstance`

## iot-digital-twin-relationship

Let the specified group manage all IoT digital twin relationship resources in the specified compartment.
```

```

Verbs Permissions APIs Fully Covered
inspect IOT_DIGITAL_TWIN_RELATIONSHIP_INSPECT

`ListDigitalTwinRelationships`
read INSPECT +

IOT_DIGITAL_TWIN_RELATIONSHIP_READ`GetDigitalTwinRelationship`
use READ +

IOT_DIGITAL_TWIN_RELATIONSHIP_UPDATE

`UpdateDigitalTwinRelationship`
manage USE +

IOT_DIGITAL_TWIN_RELATIONSHIP_CREATE

IOT_DIGITAL_TWIN_RELATIONSHIP_DELETE

`CreateDigitalTwinRelationship`

`DeleteDigitalTwinRelationship`
