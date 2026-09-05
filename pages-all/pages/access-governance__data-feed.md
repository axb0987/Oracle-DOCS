# Data Feed in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/data-feed.htm
- Fetched: 2026-09-05 03:13 CDT

# Data Feed in Oracle Access Governance

Event Data Publishing is a process to export one-time and sequentially and continually publish ongoing data events to external systems, such as an Oracle Cloud Infrastructure (OCI) cloud account. With Oracle Access Governance, you have the flexibility to export one-off and continually publish data events, such as identity, identity collections, policy, resource, access to resources, and so on, to your cloud tenancy. You may use this data for deriving insights, storing data for compliance, or for analyzing access management and governance data.

An event refers to any change in data state that occurs when there's creation, modification, or deletion of Oracle Access Governance components, such as identity, policies, resources, and so on.

Using Event Data Publisher, administrators get the complete control over access and identity data and may use it to automate event logging, streamline compliance reporting. For example, you may enable Data Feed to view insights on access violations in real-time.

## Understanding Data Event Publishing Flow

Let's understand the Data Event Publishing flow in Oracle Access Governance:

Data Event Publishing flow uses OCI Buckets for one-off export, and publish subsequent updates either to OCI Streams or OCI Buckets depending on the file size.  

  

- Perform preliminary steps within your OCI cloud account to receive the data. For details, see[Set Up OCI Tenancy for Data Publisher and Streaming](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- Use the Data Feed service of Oracle Access Governance to publish the data to your cloud system.
- Establish a connection with Oracle Access Governance by entering the configuration details. For details, see[Configure Event Data Publisher in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm).
- The Data Feed event publisher service extracts the data components available in Oracle Access Governance. On Day 0, the initial event exports a complete snapshot of data components to OCI Object Storage Bucket as JSONL files. Day 0 events will be published to OCI Object Storage Bucket.
- The Data Event Handler maintains the publishing status and returns a success or failure notification.
- For Day N , whenever there's a change in the state of data components, related to creation, modification, or deletion of components, the Data Feed event publisher detects the change in real-time, and publishes the sequential messages to the OCI Streams. The maximum size of a message can be 1 MB.
- For Day N , if the message size is greater than 1 MB, the Data Feed event publisher publishes the updates to OCI Buckets as a new version appending or replacing entries in the versioned JSONL file.
- For Audit Events, all the operational activities happening within Oracle Access Governance are published to OCI Streams. Customers can then consume this data to generate insightful reports, track changes over time, and enhance their security and compliance monitoring.

## Initial Data Event and Incremental Data Events : Day 0 and Day N Events

You can export and publish Oracle Access Governance data to either to OCI Streams or OCI Buckets.

Day 0 Event Publishing with Buckets

On Day 0, which is the initial data export Oracle Access Governance is exported to the OCI Bucket as JSONL files (`.jsonl`). These files can handle multiple JSON objects in a single payload efficiently. You'll receive multiple files per data component.

On Day 0, the Data Feed event publisher sends the start message to OCI Bucket with messageType as`Day0`, operation`CREATE`and status`START`. Until all the data objects are exported, each of the Day 0 output object file contains the status`In_PROGRESS`. Once completed, the Data Feed event publisher sends the end message for Day 0. with the status either`SUCCESS`or`FAILED`. The success or failure status is displayed on the Oracle Access Governance Console, including the name of the administrator who performed the publishing operation.

Day N Event Publishing with OCI Streams or OCI Buckets

After Day 0, subsequent updates are published in real-time either to OCI Streams or to OCI Buckets. Each message published onto the streams has an`eventTime`attribute to help the consumer service manage the ordering of events.
Depending on the file size, the publishing destination is determined.
- If the file size is less than one megabyte (`< 1 MB`), then updates are published to OCI Streams in the JSON format. The data in streams is base64 encoded, ensuring fast transmission. To consume the message, you need to decode the data, and then leverage it for further use.
- If the file size is greater than one megabyte (`> 1 MB`), then updates are published to OCI Buckets as versions to Day 0 output files, in the JSONL format.

## Available Data Components for Publishing

You can export and publish the following data components:

### Audit Events

Scope : All operations within Oracle Access Governance

messageType :`AUDIT_EVENTS`

Audit Events record operational activities in Oracle Access Governance. Audit Events focus on security and compliance, and essentially track user actions, containing details of who did what, when and where in the system.

All the CRUD operations happening within Oracle Access Governance are recorded and published as Audit Events in near real-time to OCI Streams. Once recorded, these cannot be changed. Example : Access Bundle creation audit events record details like Who created the bundle? What permissions are included?, Who can request access? and Approval workflow status? . For schema reference and attribute details, see[Audit Events Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#audithistory-reference-schema-and-sample).

### Access Bundle

Scope : Oracle Access Governance Roles

messageType :`ACCESS_BUNDLE`

All access bundles created manually or automatically using the recommendation system in Oracle Access Governance will be published as`ACCESS_BUNDLE`events. The output file contains access bundles containing specific permissions and owner details. For schema reference and attribute details, see[Access Bundle Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#access-bundle-reference-schema-and-sample).

### Access Guardrails

Scope : Access Guardrails created in Oracle Access Governance

messageType :`ACCESS_GUARDRAIL`

Access Guardrails created and managed within Oracle Access Governance will be published as`ACCESS_GUARDRAIL`events. The output file contains predefined conditions and evaluation criteria that must be met by identities before gaining access to a resource. For schema reference and attribute details, see[Access Guardrail Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#access-guardrail-reference-schema-and-sample).

### Identity

Scope : All Active Identities (Workforce or Consumers)

messageType :`IDENTITY`

All the active identities, workforce or consumers, are published as`IDENTITY`events to OCI Buckets and OCI streams. The output file contains the composite identity profile details, tagged as the`globalIdentity`attribute. It contains access profile details, including core and custom attributes. A composite identity profile in Oracle Access Governance is built up using attributes from one or more orchestrated systems. For example,`jobCode`of an identity may be ingested from and identity profile details, such as firstName, lastName from Oracle Fusion Cloud Applications. Oracle Access Governance uses attributes listed in`globalIdentity`as a source of truth to perform various governance and provisioning operations.

Additionally, it contains an array of identity attributes incoming from other integrated orchestrated systems, tagged as`targetIdentities`matched with this composite identity profile . For example, a composite identity profile in Oracle Access Governance uses identity details from Oracle Fusion Cloud Applications, but if the same identity is available in Microsoft Entra ID and matched with the composite identity, then the identity attributes available in Microsoft Entra ID will be published as part of`targetIdentities`. For schema reference and attribute details, see[Identity Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#identity-reference-schema-and-sample).

### Group

Scope : OCI IAM Groups

messageType :`OCI_GROUP`

All the available OCI IAM group ingested into Oracle Access Governance will be published as`OCI_GROUP`events.

The output file contains OCI identifiers, such as domain id, compartment id, identity collection name, description, identity collections with an array of identities included in an identity collection. Update and Create operations share the same schema. However, when a new identity collection is created, you'll not receive any identities in remove attribute. For schema reference and attribute details, see[Group Reference Schema and Samples](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#group-reference-schema-and-samples).

### Global Identity collection

Scope : OCI IAM Groups

messageType :`GLOBAL_IDENTITY_COLLECTION`

All the Identity collections ingested within Oracle Access Governance will be published as`GLOBAL_IDENTITY_COLLECTION`events. The Identity Collections may or may not be managed by Oracle Access Governance.

If the identity collection is`agManaged true`, then the output file contains membership rules, conditions, members count, and ownership details. If the identity collection is`agManaged false`, then it contains details of OCI Groups or Active Directory Groups, not created or managed within Oracle Access Governance. You can view custom metadata attributes for that group and membership count information. For schema reference and attribute details, see[Identity Collection Reference Schema and Samples](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#group-reference-schema-and-samples).

### Cloud Policy

Scope : OCI Policies

messageType :`CLOUD_POLICY`

All the available OCI policies ingested into Oracle Access Governance will be published as`CLOUD_POLICY`events. For an OCI policy, the output file contains OCI identifiers, such as domain id, compartment id, policy name, description. It contains policy details, including the subject to whom the access is granted, access type and scope of access granted. For schema reference and attribute details, see[Cloud Policies Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#cloud-policies-reference-schema-and-sample).

### Resource

Scope : All resources

messageType :`RESOURCE`

All available resources across all orchestrated systems ingested into Oracle Access Governance will be published as`RESOURCE`events. The output file contains resource identifiers within Oracle Access Governance and in OCI, resource name, description, and resource type. For schema reference and attribute details, see[Resource Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#resource-reference-schema-and-sample).

### Role

Scope : Oracle Access Governance Roles

messageType :`ROLE`

All roles created and managed within Oracle Access Governance will be published as`ROLE`events. The output file contains mandatory identifiers along with within Oracle Access Governance and in OCI, resource name, description, and resource type. For schema reference and attribute details, see[Resource Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#resource-reference-schema-and-sample).

### Policy

Scope : Policies ingested into Oracle Access Governance

messageType :`POLICY`

All policies ingested into Oracle Access Governance will be published as`POLICY`events. The output file contains policy rules and policy statements indicating what access bundle or role should be associated to what identity collection. For schema reference and attribute details, see[Policies Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#policies-reference-schema-and-sample).

### Cloud Policy to Resource Mapping

Scope : OCI policies and OCI resources

messageType : For policy to resource mapping, it is`POLICY_STATEMENT_RESOURCE_MAPPING`. For resource to policy mapping, it is`RESOURCE_POLICY_STATEMENT_MAPPING`.
Access component contains two methods to see the same data:
- Policy Granting Access to Resources : List of resources governed by a specific policy. Each JSON object contains a policy statement detailing a set of resources attached to it. In this data, the focus is on a specific policy governing a set of resources.
- Resources Access using Policy Statements : List of policies associated with a resource. Each JSON object contains a resource detailing set of policies applied to it. It is the reverse process and focus is on a specific resource.

For schema reference and attribute details, see[Access Policy to Resource Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#access-policy-to-resource-schema-sample)and[Access Resource to Policy Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#access-resource-to-policy-schema-sample).

### Permissions

Scope : Permissions ingested into Oracle Access Governance

messageType :`PERMISSION`

All permissions ingested within Oracle Access Governance will be published as`PERMISSION`events. The output file contains permission attributes, including ID, external ID to track the source of the permission, resource details and custom attributes for the permission. For schema reference and attribute details, see[Permission Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#permission-reference-schema-and-sample).

### Permission Assignment

Scope : Permissions managed by Oracle Access Governance

messageType :`PERMISSION_ASSIGNMENT`

All permissions provisioned to an identity and managed within Oracle Access Governance will be published as`PERMISSION_ASSIGNMENT`events. The output file contains permission and resource details assigned to the identity, including the identity ID, orchestrated system to which the permissions apply, permission and resource identifiers, account and provisioning status. For schema reference and attribute details, see[Permission Assignment Reference Schema and Sample](https://docs.oracle.com/en-us/iaas/Content/access-governance/event-data-publishing-reference-schema-and-samples.htm#permission-assignment-reference-schema-and-sample)
