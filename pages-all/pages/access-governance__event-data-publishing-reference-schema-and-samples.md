# Event Data Publishing Reference Schema and Sample Files
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm
- Fetched: 2026-09-05 03:14 CDT

# Event Data Publishing Reference Schema and Sample Files

Defines schema and sample output code snippet of Oracle Access Governance components published to Oracle Cloud Infrastructure (OCI) Buckets and OCI Streams.

## Header Schema and Sample Output Reference

There are headers related to event types, covering Day 0 and Day N export, and another event types, covering for publishing of data objects, which includes policies, identities, resources, and so on for create, update, and delete operations.

### Day 0 Message Header Schema
```

```

### Day 0 Sample Header
```

```

### Day 0 Object Export Header Schema
```

```

### Sample Output: Day 0 Object Export Header
```

```

### Day N Object Export Header Schema
```

```

### Sample Output: Day 0 Object Export Header
```

```

### Header Schema Attribute Definition

Here's the schema for Day 0 and Day N headers available in the output file.

Header Schema Attribute Definition for Day 0
Attributes Description
correlationId Unique identifier to correlate two or more events. For example, if a new resource is created and a new policy grants access to the resource, two events will be published and be identified with this identifier.
eventId Unique identifier for each event published either to OCI Bucket or OCI Streams. It ensures that each event can be processed and traced distinctly.
eventTime Timestamp when the event occurred with nanosecond precision. This is required to consume data sequentially and accurately.

Format :`YYYY-MM-DDTHH:MM:SS.sssssssssZ`
eventTypeversion Schema version used for sending response for each event. If there are significant changes to schema, then version is updated. For more details, refer[Semantic Versioning Guidelines](https://semver.org/).
messageType Type of data component being published. For example, a few possible values:
```

```

operation Basic operations associated with the data publishing event. It can be CREATE, UPDATE, DELETE. For some operations, such as policies, if you have to update a policy, events are published with a combination of Create and Delete operations than the update operation.
status Event Publishing status. Possible values: START, IN PROGRESS, SUCCESS, FAILED. These are sent in the output files. However, on the Oracle Access Governance Console, you can see Success or Failure status.
eventType Event value used by the service to track the event operation. For example, if we add a new policy statement in a policy, the value is`com.oracle.idm.agcs.data.enablement.policyStatement.created`
opcRequestId Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.
tenancyId Tenancy Oracle Cloud Identifier (OCID) where data is published by .Oracle Access Governance.
serviceInstanceId Service Instance OCID of your Oracle Access Governance application.

## Audit History Schema and Sample Output File

Here's Audit History schema.

### Audit Events Schema
```

```

### Sample Output Code Snippet

The data section of the JSONL contains details about an audit event related to creating an access bundle in Oracle Access Governance. The event type is`com.example.idm.agcs.audit.permission-manager.createAccessBundle`. In this example, the bundle named de-test was created with Active status , requiring no approval , and is managed by Ama Maclead .
```

```

### Audit History Schema Attribute Definition

Here's the attribute definition for an Audit History output file, containing creation of access bundle event.

Audit History Data Schema Attribute Definition
Attributes Description
data Contains detailed request, response, identity, and event-related details.
source Name of the Oracle Access Governance service that generated the event. For example, access bundle originate from source`permission-manager`.
request Details of the API request, if the event was triggered by an API request.
response Details of the API response to the request if the event was triggered by an API request.
identity The client identifiers and Oracle Access Governance global identity associated with the API request that triggered the event.
eventType A unique identifier for the type of event that was generated.
eventTypeVersion REST API version of the service that generated the event .
contentType

The format of the data sent in the event
availabilityDomain The OCI availability domain from which the event was generated.
stateChange Details of changes in state of Oracle Access Governance resource.
To view a list of supported audit event types, see[Audit Event Services and Operations](https://docs.oracle.com/en-us/iaas/Content/access-governance/audit-event-types.htm#audit-event-types).

## Access Bundle Schema and Sample Output File

Here's Access Bundle schema for creation, modification, and deletion.

### Access Bundle Create/Update Schema
```

```

### Access Bundle Delete Schema
```

```

### Sample Output Code Snippet
```

```

### Access Bundle Schema Attribute Definition

Here's the attribute definition for an Access Bundle output file.

Access Bundle Schema Attribute Definition
Attributes Description
id Unique identifier for each access bundle.
externalId External system identifier for the system.
name Name of the Access Bundle.
description Description of Access Bundle.
displayName Display name of the access bundle.
requestableBy The identity type that may request the Access Bundle. For example,`ANY`or`NONE`.
status

Status of the Access Bundle. For example,`ACTIVE`,`DRAFT`, and so on.
approvalWorkflow The id of the approval workflow that is applicable to the Access Bundle.
targetId Orchestrated system identifier.
accessBundleType`ACCESS_BUNDLE`
permissions Lists the specific permissions associated with this Access Bundle.

## Access Guardrails Reference Schema and Sample Output File

Here's Access Guardrails schema for creation, modification, and deletion.

### Access Guardrails Create/Update Schema
```

```

### Access Guardrails Delete Schema
```

```

### Sample Output Code Snippet
```

```

```

```

### Access Guardrails Schema Attribute Definition

Here's the attribute definition for an Access Guardrails output file.

Access Guardrails Attribute Definition
Attributes Description
id Unique identifier for access guardrails.
externalId External system identifier for tracking. This is same as id for access guardrails,as it is created within Oracle Access Governance.
name Name of access guardrails.
description Identifier for the type of permission granted.
isDetectiveViolationCheckEnabled Boolean flag indicating if violation detection is enabled.
lifecycleState

The current state of the access guardrails. For example,`ACTIVE`,`INACTIVE`,`DELETED`.
rules List of conditions for the access guardrails.
conditions Specific constraints what you want to enforce.
actionOnFailure Specifies the action or operation that Oracle Access Governance must perform when an access guardrails violation is triggered. The failure action is governed by actionType (e.g.,`REVOKE_LATER`or`REVOKE_IMMEDIATELY`)
createdByRef Reference to the who created the Access Guardrails.

## Approval Workflows Reference Schema and Sample Output File

Here's Oracle Access Governance approval workflows schema for creation, modification, and deletion.

### Approval Workflow Created/Updated Schema
```

```

### Approval Workflow Sub Schema
```

```

### Sample Output Code Snippet for Approval Workflow
```

```

### Approval Workflow Schema Attribute Definition

Here's the attribute definition for an approval workflow output file.

Attributes Description
id Unique identifier for the approval workflow object.
name Name of the approval workflow.
description Description of the workflow's purpose.
status Status of the workflow. For example,`ACTIVE`,`DISABLED`,`DELETED`.
createdBy Name of the user that created the object.
CreatedOn Timestamp (epoch milliseconds) when the object was created.
version Version of this object, incremented with each update.
etagVersion Timestamp (epoch milliseconds) representing the version.

## Identity Reference Schema and Sample Output File

Here's Identity schema for creation, modification, and deletion.

### Identity Creation Schema
```

```

### Identity Modification Schema
```

```

### Identity Deletion Schema
```

```

### Sample Output Code Snippet
```

```

### Identity Schema Attribute Definition

Here's the attribute definition for an identity export file.

Identity Schema Attribute Definition for Day 0
Attributes Description
globalIdentity Composite identity profile object used by Oracle Access Governance as a source of truth to perform various governance and provisioning operations. It contains access profile details, including core and custom attributes. For more information, refer to[Identities Access Details Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/enterprise-wide-access-profile-reference.htm#identities-access-details-reference),
globalIdentity → id Unique identifier for the resource within Oracle Access Governance. This also includes the orchestrated system information from where the resource value is ingested.
targetIdentities Orchestrated identity object integrated with Oracle Access Governance and matched with the composite identity profile.
targetIdentities → id Unique identifier for the resource within Oracle Access Governance. In this case, it depicts orchestrated system integrated with Oracle Access Governance. This includes the orchestrated system name identifier.
targetId Unique identifier for the orchestrated system integrated with Oracle Access Governance.

## Group Reference Schema and Sample Output File

Here's group schema for creation, modification, and deletion.

### Group Created/Updated Schema
```

```

### Group Identities Modification Sub-Schema

Whenever identities in the group changes.
```

```

### Group Deleted Schema
```

```

### Sample Output Code Snippet
```

```

### Group Schema Attribute Definition

Here's the attribute definition for a group export file. You'll only be able to publish OCI group details.

Group Schema Attribute Definition
Attributes Description
id Unique identifier for the resource within Oracle Access Governance. This also includes the orchestrated system information from where the resource value is ingested.
domainId Unique domain identifier (OCID) associated with the identity collection (IAM group) ingested into Oracle Access Governance. This is applicable only for OCI orchestrated system and contains OCI IAM groups.
externalId Refers to OCID of the object on the OCI console. For an OCI group, the external id may look like`ocid1.group.oc1.ab1234a`
compartmentId Unique compartment identifier (OCID) associated with the identity collection. This is applicable only for OCI orchestrated system and contains OCI IAM groups.
name Identity collection name.
description Identity collection description.
add Array of identities included in the identity collection.
remove Array of identities excluded from this identity collection. Update and Create operations share the same schema. However, when a new identity collection is created, you'll not receive any identities in this attribute.

## Global Identity Collection Reference Schema and Sample Output File

Here's Global identity collection schema for creation, modification, and deletion.

### Global Identity Collection Created/Updated Schema
```

```

### Global Identity Collection Deleted Schema
```

```

### Sample Output Code Snippet
```

```

### Global Identity Collection Schema Attribute Definition

Here's the attribute definition for the global identity collection managed by or ingested into Oracle Access Governance.

Global Identity Collection Schema Attribute Definition
Attributes Description
agManaged Indicated if the identity collection is managed by Oracle Access Governance.
displayName Identity collection display name.
identityGroupType Specifies the type of identity group (`HUMAN`or`OCI_GROUP`).
membershipRule Defines rules for membership criteria based on certain conditional statements.
managedByIds List of IDs managing this identity group.
tags Any associated tags for categorization
name Identity Collection name.
status Current status of the identity collection. (For example,`ACTIVE`,`DRAFT`, and so on).
createdBy Identity that created the group. For OCI Identity Collections, it is`AG System`.
currentMembers Number of active members in the group.
expectedMembers Expected number of members based on rules.

## Ownership Collection Reference Schema and Sample Output File

Here's Oracle Access Governance ownership collection schema for creation, modification, and sample output.

### Ownership collection Created/Updated Schema
```

```

### Sample Output Code Snippet
```

```

### Ownership collection Schema Attribute Definition

Here's the attribute definition for an ownership collection output file.

Ownership collection Schema Attribute Definition
Attributes Description
ownershipCollectionId Unique identifier for the ownership collection.
entityId Identifier for the associated entity.
isPrimary Indicates if the entity is the primary owner ("true" or "false")
entityName Display name for the entity.
externalId External system identifier for this entity.
usageName Purpose or type of the ownership collection.
timeCreated Creation timestamp (epoch milliseconds).
lastModified Last modification timestamp (epoch milliseconds).

## Cloud Policies Reference Schema and Sample Output File

Here's cloud policy schema for creation and deletion.

### Policies Creation Schema
```

```

### Policies Modification Schema

Policy Modifications are handled using a combination of create and delete operations. To update a policy, existing policy is first deleted before replacing it with a policy with new parameters.

### Policies Deletion Schema
```

```

### Sample Output Code Snippet
```

```

### Cloud Policies Schema Attribute Definition

Here's the attribute definition for cloud policy that grants access to resources.

Cloud Policy Schema Attribute Definition
Attributes Description
id Unique identifier for the policy assigned within Oracle Access Governance.
cloudType Indicates that policy applies to OCI.
compartmentId Unique compartment identifier (OCID) associated with the policy. This is applicable only for OCI policies.
externalId Unique policy identifier in OCI, called OCID. For policy, the external id may look like`ocid1.policy.oc1.aa1234`
policyStatementId Unique identifier for each policy statement associated with the policy.
name Cloud policy name.
description Cloud policy description
statement Policy rules governing control of resources. Each policy consists of one or more policy statements
subjects Array of principals to which the access is granted by this policy, for example, IAM group-name.
verb Access grant type assigned to a resource by using verbs in the policy. Possible verbs may be`inspect`,`read`,`use`,`inspect`.`manage`.
resourceType Array of resource types associated with a policy. It can be family resource-type or individual resource-type. For example,`instance`,`volumes`,`volume-family`, and so on. For more information, see[Resource Types in OCI](https://docs.oracle.com/iaas/Content/Identity/policiesgs/policies_topic-ResourceTypes.htm).
location Scope of access granted through this policy, such as specific compartment or entire tenancy.

## Policy Schema and Sample Output File

Here's policy schema for creation, modification, and deletion. It contains policy rules and statements that govern access to resources.

### Policy Created/Updated Schema
```

```

### Policy Rule sub-schema

Whenever policy rules change for a policy, it uses the following schema.
```

```

### Policy Deleted Schema
```

```

### Sample Output Code Snippet
```

```

### Policy Schema Attribute Definition

Here's the attribute definition for an policy output file.

Policy Schema Attribute Definition
Attributes Description
id Unique identifier for each policy.
name Name of the policy.
displayName Display name of the policy.
requestableBy The identity type that may request the Access Bundle. For example,`ANY`or`NONE`.
status

Status of the policy. For example,`ACTIVE`,`INACTIVE`.
policyVersion Version of the policy indicating updates.
policyRules List of rules associated with the policy
ruleAction Defines the action taken, such as`Assign`or`Allow`.
ruleStatement Specifies what the rule does in a statement form.

  
`Assign role [AG_System_Sharedgroups.ICF.VisionDirectory.f9b72xxxx834] to identity-group [DevOps_Team]`  

ruleStatus Current status of the rule (e.g.,`ACTIVE`).
ruleType Rule type. For example,`RBAC_RULE`,`ABAC_RULE`.

## Permission Reference Schema and Sample Output File

Here's Permission schema for creation, modification, and deletion.

### Permission Create/Update Schema
```

```

### Permission Delete Schema
```

```

### Sample Output Code Snippet

You'll receive JSONL format. The`headers`section contains metadata such as event type, timestamps, correlation IDs, tenancy details, and request identifiers. Each line represents`permission`entries, each defining permission details, group IDs, external identifiers, associated resource IDs, target IDs, and operation types.
```

```

### Permission Schema Attribute Definition

Here's the attribute definition for an permission output file.

Permission Schema Attribute Definition
Attributes Description
id Unique identifier for each permission, such as groups or privileges .
externalId External system identifier for the permission, such as distinguished name identifier
name Name of the permission. For example, Active Directory Group`IT_Admins`
permissionTypeId Identifier for the type of permission granted.
resourceId Unique identifier for the resource associated with the permission.
targetId Identifier of the target system where permissions apply.
customAttributes Additional attributes related to the permission.
operationType Specifies the operation performed while provisioning. For example`CREATE`or`UPDATE`.

## Permission Assignment Reference Schema and Sample Output File

Here's permission assignment schema for creation, modification, and deletion, including the sub-schema.

### Permission Assignment Create/Update Schema
```

```

### Permission Assignment Sub-Schema
```

```

### Permission Assignment Delete Schema
```

```

### Sample Output Code Snippet

This JSON data represents global identities and their associated access permissions , detailing which identity accounts have been granted access. It includes permission assignments linked to a specific resource and tracks the provisioning status of each account.
```

```

### Permission Assignment Schema Attribute Definition

Here's the attribute definition for an permission assignment output file.

Identity Schema Attribute Definition for Day 0
Attributes Description
globalIdentity Composite identity profile object used by Oracle Access Governance as a source of truth to perform various governance and provisioning operations. It contains access profile details, including core and custom attributes. For more information, refer to[Identities Access Details Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/enterprise-wide-access-profile-reference.htm#identities-access-details-reference),
targetIdentities Unique identifier of the orchestrated identity object integrated with Oracle Access Governance and matched with the composite identity profile.
add List of permissions granted to the global identity.
id Unique identifier for each permission assignment.
externalId External system identifier for the permission entry.
status Provisioning status of the permission (for example,`PROVISIONED`).
accountStatus Indicates whether the account is active (`true`or`false`).
targetId Identifier of the target system where permissions apply.
targetType Type of the target system (for example,`ICF`).
granttype Specifies how permission is granted (For example,`DIRECT`).
permissionId Unique identifier for the assigned permission.
permissionName Name of the permission granted.
resourceId Identifier of the resource associated with the permission.
resourceDisplayName User-friendly name of the resource (For example,`AD2`).

## Roles Reference Schema and Sample Output File

Here's Oracle Access Governance roles schema for creation, modification, and deletion.

### Roles Created/Updated Schema
```

```

### Roles Deleted Schema
```

```

### Sample Output Code Snippet
```

```

### Roles Schema Attribute Definition

Here's the attribute definition for an Roles output file.

Roles Schema Attribute Definition
Attributes Description
id Unique identifier for each access bundle.
externalId External system identifier for the system.
name Name of the role.
description Description of role.
displayName Display name of the role.
requestableBy The identity type that may request the role. For example,`ANY`or`NONE`.
status

Status of the role. For example,`ACTIVE`,`DRAFT`, and so on.
approvalWorkflow The id of the approval workflow that is applicable to the role.
accessBundles List of associated access bundles.
createdOn Timestamp indicating when the role was created.
createdBy User who created the role.
updatedBy User who last modified the role.
updatedOn Timestamp indicating when the role was last updated.
agManaged Boolean flag indicating if the entity is managed automatically

## Resource Reference Schema and Sample

Here's resource schema for creation, modification, and deletion.

### Resource Creation Schema
```

```

### Resource Modification Schema
```

```

### Resource Deletion Schema
```

```

### Sample Output Code Snippet
```

```

### Resources Schema Attribute Definition

Here's the attribute definition for an resource export file.

Resource Schema Attribute Definition
Attributes Description
id Unique identifier assigned within Oracle Access Governance for resource tracing. It also contains orchestrated system identifier from which the resource is ingested into Oracle Access Governance.
externalId Unique resource identifier in OCI.
targetId Unique identifier for the orchestrated system integrated with Oracle Access Governance.
tenancyId Unique tenancy identifier (OCID) in which the resource is located. This is applicable only for OCI orchestrated system and contains OCI resources.
resourceName Resource name.
resourceType Resource Type
description Resource description

## Resource to Policy Statement

Here's a schema for list of policies associated with a resource.

### Policy Statement to Resource Creation Schema
```

```

### Sample Output Code Snippet
```

```

### Resources to Policy Schema Attribute Definition

Here's the attribute definition for an identity export file.

Resource to Policy Schema Attribute Definition
Attributes Description
compartmentId Unique compartment identifier (OCID) associated with the resource. This is applicable only for OCI resources.
id Unique identifier for the resource assigned within Oracle Access Governance.
externalId Unique resource identifier in OCI, called resource OCID.
targetId Unique identifier to identify orchestrated system associated with the resource.
policies Array of policies attached to a resource. Each policy contains details like policy id, policy statement id, and external id to identify policies

## Policy Statement to Resource

Here's a schema for a policy statement associated with a list of resources.

### Policy Statement to Resource Creation Schema
```

```

### Sample Output Code Snippet
```

```

### Policy to Resources Schema Attribute Definition

Here are the definitions of the attribute included in the policy access to resource export file.

Attributes Description
compartmentId Unique compartment identifier (OCID) associated with a policy. This is applicable only for OCI policies.
id Unique identifier for the policy assigned within Oracle Access Governance.
externalId Unique policy identifier in OCI, called OCID.
targetId Unique identifier to identify orchestrated system associated with the policy.
