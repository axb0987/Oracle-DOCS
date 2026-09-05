# Securing Connector Hub
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/sch_security.htm
- Fetched: 2026-09-05 03:05 CDT

# Securing Connector Hub

This topic provides security information and recommendations for the Oracle Cloud Infrastructure Connector Hub service.

## Security Responsibilities

To use Connector Hub securely, learn about your security and compliance responsibilities.

In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. Security in the cloud is a shared responsibility between you and Oracle.

Oracle is responsible for the following security requirements:
- Physical Security: Oracle is responsible for protecting the global infrastructure that runs all services offered in Oracle Cloud Infrastructure. This infrastructure consists of the hardware, software, networking, and facilities that run Oracle Cloud Infrastructure services.

Your security responsibilities are described on this page, which include the following areas:
- Access Control: Limit privileges as much as possible. Users should be given only the access necessary to perform their work.

## Initial Security Tasks

Use this checklist to identify the tasks you perform to secure Connector Hub in a new Oracle Cloud Infrastructure tenancy.

Task More Information
Use IAM policies to grant access to users and resources[IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/sch_security.htm#iam-policies)

## Routine Security Tasks

After getting started with Connector Hub, use this checklist to identify security tasks that we recommend you perform regularly.

Connector Hub does not have any security tasks that you need to perform regularly.

## IAM Policies

Use policies to limit access to Connector Hub.

A policy specifies who can access Oracle Cloud Infrastructure resources and how. For more information, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).

Assign a group the least privileges that are required to perform their responsibilities. Each policy has a verb that describes what actions the group is allowed to do. From the least amount of access to the most, the available verbs are:`inspect`,`read`,`use`, and`manage`.

### User Access Policies

To work with connectors, a user must be in a group, and a policy must grant that group the appropriate authorization within the compartment or tenancy.

Create, update, and delete connectors (no queues or streams)

Let the specified group create, update, and delete connectors in the specified compartment.
```

```

Update connectors only (no queues or streams)

Let the specified group update connectors only in the specified compartment. The group can't create or delete connectors.
```

```

Create, update, and delete connectors with queues

Let the specified group read queues in the specified compartment and create and update connectors that use a[Queue source](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-queue-source.htm)or a[Queue target](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#supported-targets). Also let the group delete connectors in the specified compartment.
```

```

Create, update, and delete connectors with streams

Let the specified group read streams and stream pools in the specified compartment and create and update connectors that use a[Streaming source](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector-streaming-source.htm)or a[Streaming target](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#supported-targets). Also let the group delete connectors in the specified compartment.
```

```

For more information about Connector Hub policies, see[Details for Connector Hub](https://docs.oracle.com/iaas/Content/Identity/Reference/serviceconnectorhubpolicyreference.htm).

### Service Access Policies

Note  
  
Ensure that any policy you create complies with your company guidelines.

To move data, your connector must have authorization to access the specified resources in the source , task , and target services. Some resources are accessible without policies. Default policies providing the required authorization are offered when you use the Console to define a connector. These policies are limited to the context of the connector. You can either accept the[default policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti)or ensure that you have the proper authorizations in[custom policies for user and service access](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#auth-custom).

For example, the following default policy is offered when you create or edit a connector that[moves data from Logging to Monitoring](https://docs.oracle.com/iaas/Content/connector-hub/alarmlogs.htm).
```

```

For more information, including default policies, see[Access to Source, Task, and Target Services](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti__target-access).

### Cross-Tenancy Connector Access

Use cross-tenancy connector access to share connectors with another organization that has its own tenancy. For example, share connectors with another business unit in your company, a customer of your company, or a company that provides services to your company.
Note  
  
To create a connector that accesses resources in other tenancies, you must use the OCI SDK, CLI, or API. (The[policy builder](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-Using_the_Policy_Builder.htm)in the Console doesn't provide information from other tenancies, or suggest Endorse, Admit, or Define statements.) For CLI and API instructions, see[Creating a Connector](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector.htm).

To access and share resources, the administrators of both tenancies need to create special policy statements that explicitly state the resources that can be accessed and shared. These special statements use the words Define , Endorse , and Admit . For more information about these statements, see[Cross-Tenancy Access Policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/iam-cross-domain.htm).

#### Source Tenancy Policy Statements

Use a policy statement in the source tenancy to:

- Admit a connector from a destination tenancy to access resources in your (source) tenancy
- Endorse a connector to access resources in the destination tenancy
- Endorse a group to access resources in the destination tenancy
Note  
  
The following example policy statements are formatted for readability. Before using copies of these statements, remove new lines, tabs, and spaces. Admit any connector from the destination tenancy to access a specific kind of resource in your (source) tenancy
```

```
For examples, see[Examples](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/sch_security.htm#connector-cross-tenancy-examples). To find the permissions required for a specific type of resource accessed by a connector, see[Default Policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti__default-policies). Endorse a group in your (source) tenancy to do anything with any connector in any tenancy

```

```
Endorse a group in your (source) tenancy to do anything with any connector in the destination tenancy only To write a policy that reduces the scope of tenancy access, the source administrator must reference the destination tenancy OCID provided by the destination administrator.

```

```

#### Destination Tenancy Policy Statements

Use a policy statement in the destination tenancy to:

- Endorse a connector to access resources in the source tenancy
- Admit a connector from the source tenancy to access resources in your (destination) tenancy
- Admit a group or dynamic group from the source tenancy to access resources in your (destination) tenancy
Note  
  
The following example policy statements are formatted for readability. Before using copies of these statements, remove new lines, tabs, and spaces. Endorse any connector in your (destination) tenancy to access a specific kind of resource in the source tenancy
```

```
For examples, see[Examples](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/sch_security.htm#connector-cross-tenancy-examples). To find the permissions required for a specific type of resource accessed by a connector, see[Default Policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti__default-policies). Admit a group from the source tenancy to do anything with any connector in your (destination) tenancy

```

```
Admit a group from the source tenancy to read connectors in the`SharedConnectors`compartment only (in your destination tenancy)

```

```
Admit a dynamic group from the source tenancy to read connectors in the`SharedConnectors`compartment only (in your destination tenancy)

```

```
To find the permissions required for a specific type of resource accessed by a dynamic group, see[Custom Policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#auth-custom).

#### Examples

Note  
  

- Write cross-tenancy policies before[creating the connector](https://docs.oracle.com/iaas/Content/connector-hub/create-service-connector.htm). You must use the OCI SDK, CLI, or API to create a cross-tenancy connector.
- The following example policy statements are formatted for readability. Before using copies of these statements, remove new lines, tabs, and spaces.
- To endorse or admit a connector for access to a source, target, or task resource that isn't covered in these examples, use the resource permissions in the[default policies](https://docs.oracle.com/iaas/Content/connector-hub/overview.htm#Authenti__default-policies).

##### Stream Source in Another Tenancy

Write policies for a connector to move data from a stream in a different tenancy to a bucket in the connector's tenancy.  
  

Callout Description
1 Stream used as connector source
2 Connector that moves data from the stream to the bucket
3 Bucket used as connector target

Following are the policies for moving this data from the stream in Tenancy A to the bucket in Tenancy B, using the connector in Tenancy B. Tenancy A Admit any connector in the specified compartment of Tenancy B to access any stream in the specified compartment of this tenancy.
```

```
Tenancy B Endorse any connector in this tenancy to access any stream in Tenancy A.
```

```
Allow any connector in the specified compartment of this tenancy to move data to the bucket (same tenancy).
```

```

##### Log Source in Another Tenancy

Write policies for a connector to move data from a log in a different tenancy to a log group in the connector's tenancy.  
  

Callout Description
1 Log used as connector source
2 Connector that moves data from the log to the log group
3 Log group used as connector target Tenancy A Admit any connector in the specified compartment of Tenancy B to access any log in the specified compartment of this tenancy.
```

```
Tenancy B Endorse any connector in this tenancy to access any log in Tenancy A.
```

```
Allow any connector in the specified compartment of this tenancy to move data to the log group (same tenancy).
```

```

##### Function Target in Another Tenancy

Write policies for a connector to move data from a log in the connector's tenancy to a function in a different tenancy.  
  

Callout Description
1 Log used as connector source
2 Connector that moves data from the log to the function
3 Function used as connector target Tenancy A Endorse any connector in the specified compartment of this tenancy to access any function in the specified compartment of Tenancy B.
```

```
Allow any connector in the specified compartment of this tenancy to access any log (same tenancy).
```

```
Tenancy B Admit any connector in Tenancy A to access any function in this tenancy.
```

```

##### Source Metric and Target Bucket in Other Tenancies

Write policies for a connector to move data from a metric in a different tenancy (A) to a function in a different tenancy (C).  
  

Callout Description
1 Metric used as connector source
2 Connector that moves data from the metric to the bucket
3 Bucket used as connector target Tenancy A Admit any connector in the specified compartment of Tenancy B to access any metric in the specified compartment of this tenancy.
```

```
Tenancy B Endorse any connector in this tenancy to access any metric in Tenancy A.
```

```
Endorse any connector in this tenancy to access any bucket in Tenancy C.
```

```
Tenancy C Admit any connector in the specified compartment of Tenancy B to move data to any bucket in the specified compartment of this tenancy.
```

```
