# Managing Exadata Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm
- Fetched: 2026-09-05 02:11 CDT

# Managing Exadata Instances

Important  
  
The My Services dashboard and APIs are deprecated.

The following procedures walk you through creating, modifying, and deleting Exadata instances used with the[Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/).
Important  
  
These procedures are for use with Oracle Database Exadata Database Service on Cloud@Customer ONLY . For more information, see[Administering Oracle Database Exadata Cloud at Customer](https://docs.oracle.com/en/cloud/cloud-at-customer/exadata-cloud-at-customer/exacc/get-started-this-service.html). These procedures DO NOT apply to the Exadata Cloud Service available in Oracle Cloud Infrastructure.

## Prerequisites

Before you can manage Exadata instances, you need to:
- Subscribe to an Oracle Cloud service
- Obtain account credentials with required roles assigned
- Determine your API endpoint

[To subscribe to an Oracle Cloud service](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

To access[Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/), you must request a trial or paid subscription to an Oracle Cloud service.

[To obtain account credentials and role assignments](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Ask your account administrator for the following items to access[Oracle Cloud My Services API](https://docs.oracle.com/iaas/api/#/en/itas/latest/):
- 

Account credentials:
- 

User name and password
- 

Identity domain ID

An identity domain ID can be either the IDCS GUID that identifies the identity domain for the users within Identity Cloud Service (IDCS) or the Identity Domain name for a traditional Cloud Account.
- 

Required roles assigned to above user name

[To determine your API endpoint](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Insert the identity domain ID provided by the account administrator ( &lt;domain&gt; ) between`/itas/`and`/myservices/`.

Example:

```

```

## Creating Exadata Instances

This section covers how to create a basic Exadata instance, an instance with custom IP network configuration, and an instance with multi-VM support.

[To create a basic Exadata instance](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the required payload to create a new instance for a given service entitlement (Exadata in our case).

In the following example, &lt;domain&gt; is the identity domain ID.

```

```

#### Attributes

Name Description
requestPayload.name

Required: Yes

Type: String

Name of the Exadata instance. This name:
- Must not exceed 25 characters.
- Must start with a letter.
- Must contain only lower case letters and numbers.
- Must not contain spaces or any other special characters.
- Must be unique within the identity domain.

requestPayload.

serviceEntitlementId

Required: Yes

Type: String

Service Entitlement for the Exadata instance. See "Exadata Service Entitlement discovery." Note that any "cesi-" or "sub-" prefix should not be included.

requestPayload.

customAttributes.

ExaUnitName

Required: Yes

Type: String

A name for your Exadata Database Machine environment. This name is also used as the cluster name for the Oracle Grid Infrastructure installation.

requestPayload.

customAttributes.

CreateSparse

Required: Yes

Type: String

"Y" to create a disk group that is based on sparse grid disks, else "N".

You must select this option to enable Exadata Cloud Service snapshots. Exadata snapshots enable space-efficient clones of Oracle databases that can be created and destroyed very quickly and easily.

requestPayload.

customAttributes.

BackupToDisk

Required: Yes

Type: String

"Y" to use "Database backups on Exadata Storage", else "N".

This option configures the Exadata storage to enable local database backups on Exadata storage.

requestPayload.

customAttributes.

isBYOL

Required: Yes

Type: String

"Y" to indicate that the Exadata Cloud Service instance uses Oracle Database licenses that are provided by you rather than licenses that are provided are part of the service subscription, else "N".

This option only affects the billing that is associated with the service instance. It has no effect on the technical configuration of the Exadata Cloud Service instance.

requestPayload.

customAttributes.

PickRackSize

Required: Yes

Type: String

Specify the rack configuration for your service instance. Exact allowed values depend on your purchase. Typical values are like "Full Rack", "Half Rack", "Quarter Rack" or "Eighth Rack".

requestPayload.

customAttributes.

SELECTED_DC_ID

Required: Yes

Type: String

Data center that will host your Exadata Cloud Service instance. See "Exadata Service Entitlement discovery" to obtain the Eligible Data Center IDs.

[To create an Exadata instance with custom IP network configuration](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the attributes ClientNetwork and BackupNetwork as part of the payload. The following example includes these optional attributes as well as required attributes.

In the following example, &lt;domain&gt; is the identity domain ID.

```

```

#### Attributes

Name Description

requestPayload.

customAttributes.

ClientNetwork

Required: Yes

Type: Url

IP network definitions for the network that is primarily used for client access to the database servers. Applications typically access databases on Exadata Cloud Service through this network using Oracle Net Services in conjunction with Single Client Access Name (SCAN) and Oracle RAC Virtual IP (VIP) interfaces.

requestPayload.

customAttributes.

BackupNetwork

Required: Yes

Type: Url

IP network definitions for the network that is typically used to access the database servers for various purposes, including backups and bulk data transfers.

[To create an Exadata instance with multi-VM support](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

If your Exadata system environment is enabled to support multiple virtual machine (VM) clusters, then you can define up to eight clusters and specify how the overall Exadata system resources are allocated to them.

In a configuration with multiple VM clusters, each VM cluster is allocated a dedicated portion of the overall Exadata system resources, with no over-provisioning or resource sharing. On the compute nodes, a separate VM is defined for each VM cluster, and each VM is allocated a dedicated portion of the available compute node CPU, memory, and local disk resources. Each VM cluster is also allocated a dedicated portion of the overall Exadata storage.

Post a request with the attributes EXAUNIT_ALLOCATIONS and MULTIVM_ENABLED as part of the payload. The following example includes these optional attributes as well as required attributes.

In the following example, &lt;domain&gt; is the identity domain ID and &lt;base64_encoded_string&gt; is a base64 encoding of the payload following the example.

Example payload for request:

```

```

Payload for &lt;base64_encoded_string&gt; :

```

```

#### Attributes

Name Description

requestId

Required: Optional

Type: String

Unique UUID

TotalNumOfCores

ForCluster

Required: Yes

Type: String

The number of CPU cores that are allocated to the VM cluster. This is the total number of CPU cores that are allocated evenly across all of the compute nodes in the VM cluster. Must be a multiple of numComputes as returned by a call to ecra/endpoint/clustershapes.

TotalMemoryInGb

Required: Yes

Type: String

The amount of memory (in GB) that is allocated to the VM cluster. This is the total amount of memory that is allocated evenly across all of the compute nodes in the VM cluster. Must be a multiple of numComputes as returned by a call to ecra/endpoint/clustershapes.

StorageInTb

Required: Yes

Type: String

The total amount of Exadata storage (in TB) that is allocated to the VM cluster. This storage is allocated evenly from all of the Exadata Storage Servers.

OracleHomeDiskSize

InGb

Required: Yes

Type: String

The amount of local disk storage (in GB) that is allocated to each database server in the first VM cluster.

## Modifying Exadata Instances

This section covers how to add a cluster to an existing instance, reshape a cluster, and delete a cluster.

[To add a cluster to an existing instance](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of AddCluster.

In the following example, &lt;domain&gt; is the identity domain ID, &lt;instanceId&gt; and &lt;serviceEntitlementId&gt; are returned from iTAS serviceInstances, and &lt;base64_encoded_string&gt; is a base64 encoding of the payload following the example.

Example payload for request:

```

```

Payload for &lt;base64_encoded_string&gt; :

```

```

[To reshape a cluster](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of ReshapeCluster.

In the following example, &lt;domain&gt; is the identity domain ID and &lt;base64_encoded_string&gt; is a base64 encoding of the payload following the example.

Example payload for request:

```

```

Payload for &lt;base64_encoded_string&gt; :

```

```

Important  
  

- 

Only one attribute can be modified per Reshape request. The payload should contain only the modified attribute. Example:
```

```

- When doing a Reshape with the`OracleHomeDiskSizeInGb`attribute, use the name`OhomePartitionInGB`.
- The value for`TotalNumOfCoresForCluster`must be a multiple of`numComputes`as returned by a call to`ecra/endpoint/clustershapes`.
- The value for`TotalMemoryInGb`must be a multiple of`numComputes`as returned by a call to`ecra/endpoint/clustershapes`.

[To delete a cluster](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-UPDATE and a base64 encoding of a payload that includes the Operation value of DeleteCluster.

In the following example, &lt;domain&gt; is the identity domain ID and &lt;base64_encoded_string&gt; is a base64 encoding of the payload following the example.

Example payload for request:

```

```

Payload for &lt;base64_encoded_string&gt; :

```

```

## Deleting Exadata Instances

This section covers how to delete Exadata instances.
Important  
  
Delete all existing multi-VM clusters before deleting the Exadata instance. Following this guidance prevents the instance ending up in an invalid state.

[To delete an instance](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Post a request with the operationItemDefinition of CIM-Exadata-CUSTOM-PRODUCTION-DELETE.

In the following example, &lt;domain&gt; is the identity domain ID.

Example payload for request:

```

```

## Discovering Entitlements and Instances

This section describes how to discover service entitlements and service instances.

[To discover service entitlements](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Send the following request:

```

```

Example payload returned for this request:

```

```

Eligible Data Centers:

Use:
```

```

where`{ServiceEntitlementId}`is a service entitlement ID such as`cesi-500074601`. This will provide additional information such as:

```

```

[To discover service instances](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/managingexadatainstances.htm#)

Send the following request:

```

```

Example payload returned for this request:

```

```
