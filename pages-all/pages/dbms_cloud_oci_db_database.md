# Database Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html
- Fetched: 2026-09-05 19:06 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#dcoc-content-body)

## Database Functions

Package: DBMS_CLOUD_OCI_DB_DATABASE

### ACTIVATE_EXADATA_INFRASTRUCTURE Function

Activates the specified Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`activate_exadata_infrastructure_details`

(required) The activation details for the Exadata infrastructure and the additional storage servers requested.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_STORAGE_CAPACITY_CLOUD_EXADATA_INFRASTRUCTURE Function

Makes the storage capacity from additional storage servers available for Cloud VM Cluster consumption. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_STORAGE_CAPACITY_EXADATA_INFRASTRUCTURE Function

Makes the storage capacity from additional storage servers available for VM Cluster consumption. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_VIRTUAL_MACHINE_TO_CLOUD_VM_CLUSTER Function

Add Virtual Machines to the Cloud VM cluster. Applies to Exadata Cloud instances only.

Syntax
```

```

Parameters

Parameter Description

`add_virtual_machine_to_cloud_vm_cluster_details`

(required) Request to add Virtual Machines to the Cloud VM cluster.

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_VIRTUAL_MACHINE_TO_VM_CLUSTER Function

Add Virtual Machines to the VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`add_virtual_machine_to_vm_cluster_details`

(required) Request to add Virtual Machines to the VM cluster.

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### AUTONOMOUS_DATABASE_MANUAL_REFRESH Function

Initiates a data refresh for an Autonomous Database refreshable clone. Data is refreshed from the source database to the point of a specified timestamp.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_database_manual_refresh_details`

(required) Request details for manually refreshing an Autonomous Database refreshable clone.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_BACKUP Function

Cancel automatic/standalone full/incremental create backup workrequests specified by the backup Id.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUTONOMOUS_CONTAINER_DATABASE_COMPARTMENT Function

Move the Autonomous Container Database and its dependent resources to the specified compartment. For more information about moving Autonomous Container Databases, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move Autonomous Container Database to a different compartment

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUTONOMOUS_DATABASE_COMPARTMENT Function

Move the Autonomous Database and its dependent resources to the specified compartment. For more information about moving Autonomous Databases, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move Autonomous Database to a different compartment

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_COMPARTMENT Function

**Deprecated.** Use the`CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT`Function operation to move an Exadata infrastructure resource to a different compartment and`CHANGE_CLOUD_AUTONOMOUS_VM_CLUSTER_COMPARTMENT`Function operation to move an Autonomous Exadata VM cluster to a different compartment. For more information, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move an Autonomous Exadata Infrastructure resource to a different compartment.

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT Function

Moves an Autonomous VM cluster and its dependent resources to another compartment. Applies to Exadata Cloud@Customer only. For systems in the Oracle cloud, see`CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT`Function.

Syntax
```

```

Parameters

Parameter Description

`change_autonomous_vm_cluster_compartment_details`

(required) Request to move Autonomous VM cluster to a different compartment

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_BACKUP_DESTINATION_COMPARTMENT Function

Move the backup destination and its dependent resources to the specified compartment. For more information, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move backup destination to a different compartment.

`backup_destination_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CLOUD_AUTONOMOUS_VM_CLUSTER_COMPARTMENT Function

Moves an Autonomous Exadata VM cluster in the Oracle cloud and its dependent resources to another compartment. For Exadata Cloud@Customer systems, see`CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT`Function.

Syntax
```

```

Parameters

Parameter Description

`change_cloud_autonomous_vm_cluster_compartment_details`

(required) Request to move cloud Autonomous VM cluster to a different compartment

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT Function

Moves a cloud Exadata infrastructure resource and its dependent resources to another compartment. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.For more information about moving resources to a different compartment, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_cloud_exadata_infrastructure_compartment_details`

(required) Request to move cloud Exadata infrastructure resource to a different compartment.

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CLOUD_VM_CLUSTER_COMPARTMENT Function

Moves a cloud VM cluster and its dependent resources to another compartment. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`change_cloud_vm_cluster_compartment_details`

(required) Request to move cloud VM cluster to a different compartment

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_SOFTWARE_IMAGE_COMPARTMENT Function

Move the Database Software Image and its dependent resources to the specified compartment. For more information about moving Databse Software Images, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move Database Software Image to a different compartment

`database_software_image_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATAGUARD_ROLE Function

Switch the Autonomous Container Database role between Standby and Snapshot Standby. For more information about changing Autonomous Container Databases Dataguard Role, see[Convert Physical Standby to Snapshot Standby](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#ADBCL-GUID-D3B503F1-0032-4B0D-9F00-ACAE8151AB80)and[Convert Snapshot Standby to Physical Standby](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbcl/index.html#ADBCL-GUID-E8D7E0EE-8244-467D-B33A-1BC6F969A0A4).

Syntax
```

```

Parameters

Parameter Description

`change_dataguard_role_details`

(required) Request to Change the Autonomous Container Database Dataguard role.

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DB_SYSTEM_COMPARTMENT Function

Moves the DB system and its dependent resources to the specified compartment. For more information about moving DB systems, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move the DB system to a different compartment. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DISASTER_RECOVERY_CONFIGURATION Function

This operation updates the cross-region disaster recovery (DR) details of the standby Autonomous Database Serverless database, and must be run on the standby side.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_disaster_recovery_configuration_details`

(required) Request to update the cross-region disaster recovery (DR) details of the standby Autonomous Database Serverless database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXADATA_INFRASTRUCTURE_COMPARTMENT Function

Moves an Exadata infrastructure resource and its dependent resources to another compartment. Applies to Exadata Cloud@Customer instances only. To move an Exadata Cloud Service infrastructure resource to another compartment, use the`CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT`Function operation.

Syntax
```

```

Parameters

Parameter Description

`change_exadata_infrastructure_compartment_details`

(required) Request to move Exadata infrastructure to a different compartment

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXTERNAL_CONTAINER_DATABASE_COMPARTMENT Function

Move the`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function and its dependent resources to the specified compartment. For more information about moving external container databases, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move the external container database to a different compartment.

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXTERNAL_NON_CONTAINER_DATABASE_COMPARTMENT Function

Move the external non-container database and its dependent resources to the specified compartment. For more information about moving external non-container databases, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move the external non-container database to a different compartment.

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_EXTERNAL_PLUGGABLE_DATABASE_COMPARTMENT Function

Move the`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function and its dependent resources to the specified compartment. For more information about moving external pluggable databases, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move the`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource to a different compartment.

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_KEY_STORE_COMPARTMENT Function

Move the key store resource to the specified compartment. For more information about moving key stores, see[Moving Database Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Database/Concepts/databaseoverview.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`change_key_store_compartment_details`

(required) Request to move key store to a different compartment

`key_store_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_KEY_STORE_TYPE Function

Changes encryption key management type

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`change_key_store_type_details`

(required) Request to change the source of the encryption key for the database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ONEOFF_PATCH_COMPARTMENT Function

Move the one-off patch to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`change_compartment_details`

(required) Request to move one-off patch to a different compartment

`oneoff_patch_id`

(required) The one-off patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_VM_CLUSTER_COMPARTMENT Function

Moves a VM cluster and its dependent resources to another compartment. Applies to Exadata Cloud@Customer instances only. To move a cloud VM cluster in an Exadata Cloud Service instance to another compartment, use the`CHANGE_CLOUD_VM_CLUSTER_COMPARTMENT`Function operation.

Syntax
```

```

Parameters

Parameter Description

`change_vm_cluster_compartment_details`

(required) Request to move the Exadata Cloud@Customer VM cluster to a different compartment.

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHECK_EXTERNAL_DATABASE_CONNECTOR_CONNECTION_STATUS Function

Check the status of the external database connection specified in this connector. This operation will refresh the connectionStatus and timeConnectionStatusLastUpdated fields.

Syntax
```

```

Parameters

Parameter Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector resource (`ExternalDatabaseConnectorId`).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COMPLETE_EXTERNAL_BACKUP_JOB Function

Changes the status of the standalone backup resource to `ACTIVE` after the backup is created from the on-premises database and placed in Oracle Cloud Infrastructure Object Storage. **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See[Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud](https://docs.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm)for more information.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`complete_external_backup_job_details`

(required) Updates the status of the backup resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY Function

Configures the Autonomous Database Vault service[key](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`configure_autonomous_database_vault_key_details`

(required) Configuration details for the Autonomous Database Vault service[key](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONFIGURE_SAAS_ADMIN_USER Function

This operation updates SaaS administrative user configuration of the Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`configure_saas_admin_user_details`

(required) Request to update SaaS administrative user configuration of the Autonomous Database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONVERT_TO_PDB Function

Converts a non-container database to a pluggable database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`convert_to_pdb_details`

(required) Request to convert a non-container database to a pluggable database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CONVERT_TO_REGULAR_PLUGGABLE_DATABASE Function

Converts a Refreshable clone to Regular pluggable database (PDB). Pluggable Database will be in `READ_WRITE` openmode after conversion.

Syntax
```

```

Parameters

Parameter Description

`convert_to_regular_pluggable_database_details`

(required) Request to convert a Refreshable clone pluggable database (PDB) to a Regular pluggable database.

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION_VIP Function

Creates a new application virtual IP (VIP) address in the specified cloud VM cluster based on the request parameters you provide.

Syntax
```

```

Parameters

Parameter Description

`create_application_vip_details`

(required) Request to create a new application virtual IP (VIP) address.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTONOMOUS_CONTAINER_DATABASE Function

Creates an Autonomous Container Database in the specified Autonomous Exadata Infrastructure.

Syntax
```

```

Parameters

Parameter Description

`create_autonomous_container_database_details`

(required) Request to create an Autonomous Container Database in a specified Autonomous Exadata Infrastructure or in Autonomous VM Cluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Create a new Autonomous Data Guard association. An Autonomous Data Guard association represents the replication relationship between the specified Autonomous Container database and a peer Autonomous Container database. For more information, see[Using Oracle Data Guard](https://docs.oracle.com/iaas/Content/Database/Tasks/usingdataguard.htm). All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`create_autonomous_container_database_dataguard_association_details`

(required) A request to create an Autonomous Data Guard association.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTONOMOUS_DATABASE Function

Creates a new Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`create_autonomous_database_details`

(required) Request to create a new Autonomous Database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTONOMOUS_DATABASE_BACKUP Function

Creates a new Autonomous Database backup for the specified database based on the provided request parameters.

Syntax
```

```

Parameters

Parameter Description

`create_autonomous_database_backup_details`

(required) Request to create a new Autonomous Database backup.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTONOMOUS_VM_CLUSTER Function

Creates an Autonomous VM cluster for Exadata Cloud@Customer. To create an Autonomous VM Cluster in the Oracle cloud, see`CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`create_autonomous_vm_cluster_details`

(required) Request to create an Autonomous VM cluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKUP Function

Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

Syntax
```

```

Parameters

Parameter Description

`create_backup_details`

(required) Request to create a new database backup.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_BACKUP_DESTINATION Function

Creates a backup destination in an Exadata Cloud@Customer system.

Syntax
```

```

Parameters

Parameter Description

`create_backup_destination_details`

(required) Request to create a new backup destination.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER Function

Creates an Autonomous Exadata VM cluster in the Oracle cloud. For Exadata Cloud@Customer systems, see`CREATE_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`create_cloud_autonomous_vm_cluster_details`

(required) Request to create a cloud Autonomous VM cluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CLOUD_EXADATA_INFRASTRUCTURE Function

Creates a cloud Exadata infrastructure resource. This resource is used to create either an[Exadata Cloud Service](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm)instance or an Autonomous Database on dedicated Exadata infrastructure.

Syntax
```

```

Parameters

Parameter Description

`create_cloud_exadata_infrastructure_details`

(required) Request to create a cloud Exadata infrastructure resource in an[Exadata Cloud Service](https://docs.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm)instance.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CLOUD_VM_CLUSTER Function

Creates a cloud VM cluster.

Syntax
```

```

Parameters

Parameter Description

`create_cloud_vm_cluster_details`

(required) Request to create a cloud VM cluster. Applies to Exadata Cloud Service instances only. See[The New Exadata Cloud Service Resource Model](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)for information on this resource type.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONSOLE_CONNECTION Function

Creates a new console connection to the specified database node. After the console connection has been created and is available, you connect to the console using SSH.

Syntax
```

```

Parameters

Parameter Description

`create_console_connection_details`

(required) Request object for creating an CreateConsoleConnection

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONSOLE_HISTORY Function

Captures the most recent serial console data (up to a megabyte) for the specified database node.

Syntax
```

```

Parameters

Parameter Description

`create_console_history_details`

(required) Request object for creating a console history.

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_GUARD_ASSOCIATION Function

Creates a new Data Guard association. A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see[Using Oracle Data Guard](https://docs.oracle.com/iaas/Content/Database/Tasks/usingdataguard.htm). All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`create_data_guard_association_details`

(required) A request to create a Data Guard association.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE Function

Creates a new database in the specified Database Home. If the database version is provided, it must match the version of the Database Home. Applies to Exadata and Exadata Cloud@Customer systems.

Syntax
```

```

Parameters

Parameter Description

`create_new_database_details`

(required) Request to create a new database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE_SOFTWARE_IMAGE Function

create database software image in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_database_software_image_details`

(required) Request to create database software image.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DB_HOME Function

Creates a new Database Home in the specified database system based on the request parameters you provide. Applies to bare metal DB systems, Exadata systems, and Exadata Cloud@Customer systems.

Syntax
```

```

Parameters

Parameter Description

`create_db_home_with_db_system_id_details`

(required) Request to create a new Database Home.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXADATA_INFRASTRUCTURE Function

Creates an Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only. To create an Exadata Cloud Service infrastructure resource, use the`CREATE_CLOUD_EXADATA_INFRASTRUCTURE`Function operation.

Syntax
```

```

Parameters

Parameter Description

`create_exadata_infrastructure_details`

(required) Request to create Exadata Cloud@Customer infrastructure.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_BACKUP_JOB Function

Creates a new backup resource and returns the information the caller needs to back up an on-premises Oracle Database to Oracle Cloud Infrastructure. **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See[Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud](https://docs.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm)for more information.

Syntax
```

```

Parameters

Parameter Description

`create_external_backup_job_details`

(required) Request to create a cloud backup resource for a database running outside the cloud.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_CONTAINER_DATABASE Function

Creates a new external container database resource.

Syntax
```

```

Parameters

Parameter Description

`create_external_container_database_details`

(required) Request to create a new external container database resource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_DATABASE_CONNECTOR Function

Creates a new external database connector.

Syntax
```

```

Parameters

Parameter Description

`create_external_database_connector_details`

(required) Request to create a connector to an external database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_NON_CONTAINER_DATABASE Function

Creates a new ExternalNonContainerDatabase resource

Syntax
```

```

Parameters

Parameter Description

`create_external_non_container_database_details`

(required) Request to create a new external non-container database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_EXTERNAL_PLUGGABLE_DATABASE Function

Registers a new`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource.

Syntax
```

```

Parameters

Parameter Description

`create_external_pluggable_database_details`

(required) Request to create a new external pluggable database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_KEY_STORE Function

Creates a Key Store.

Syntax
```

```

Parameters

Parameter Description

`create_key_store_details`

(required) Request to create a new key store.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MAINTENANCE_RUN Function

Creates a maintenance run with one of the following: The latest available release update patch (RUP) for the Autonomous Container Database. The latest available RUP and DST time zone (TZ) file updates for the Autonomous Container Database. Creates a maintenance run to update the DST TZ file for the Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`create_maintenance_run_details`

(required) Request to create a Maintenance Run for the resource.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ONEOFF_PATCH Function

Creates one-off patch for specified database version to download.

Syntax
```

```

Parameters

Parameter Description

`create_oneoff_patch_details`

(required) Request to create a one-off patch to download.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PLUGGABLE_DATABASE Function

Creates and starts a pluggable database in the specified container database. Pluggable Database can be created using different operations (e.g. LocalClone, RemoteClone, Relocate ) with this API. Use the`START_PLUGGABLE_DATABASE`Function and`STOP_PLUGGABLE_DATABASE`Function APIs to start and stop the pluggable database.

Syntax
```

```

Parameters

Parameter Description

`create_pluggable_database_details`

(required) Request to create pluggable database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VM_CLUSTER Function

Creates an Exadata Cloud@Customer VM cluster.

Syntax
```

```

Parameters

Parameter Description

`create_vm_cluster_details`

(required) Request to create a VM cluster. Applies to Exadata Cloud@Customer instances only. See`CREATE_CLOUD_VM_CLUSTER_DETAILS`Function for details on creating a cloud VM cluster in an Exadata Cloud Service instance.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_VM_CLUSTER_NETWORK Function

Creates the VM cluster network. Applies to Exadata Cloud@Customer instances only. To create a cloud VM cluster in an Exadata Cloud Service instance, use the`CREATE_CLOUD_VM_CLUSTER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_details`

(required) Request to create the Cloud@Customer VM cluster network.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DB_NODE_ACTION Function

Performs one of the following power actions on the specified DB node: - start - power on - stop - power off - softreset - ACPI shutdown and power on - reset - power off and power on **Note:** Stopping a node affects billing differently, depending on the type of DB system: *Bare metal and Exadata systems* - The _stop_ state has no effect on the resources you consume. Billing continues for DB nodes that you stop, and related resources continue to apply against any relevant quotas. You must terminate the DB system (`TERMINATE_DB_SYSTEM`Function) to remove its resources from billing and quotas. *Virtual machine DB systems* - Stopping a node stops billing for all OCPUs associated with that node, and billing resumes when you restart the node.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`action`

(required) The action to perform on the DB Node.

Allowed values are: 'STOP', 'START', 'SOFTRESET', 'RESET'

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION_VIP Function

Deletes and deregisters the specified application virtual IP (VIP) address.

Syntax
```

```

Parameters

Parameter Description

`application_vip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application virtual IP (VIP) address.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTONOMOUS_DATABASE Function

Deletes the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTONOMOUS_DATABASE_BACKUP Function

Deletes a long-term backup. You cannot delete other backups using this API.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTONOMOUS_VM_CLUSTER Function

Deletes the specified Autonomous VM cluster in an Exadata Cloud@Customer system. To delete an Autonomous VM Cluster in the Oracle cloud, see`DELETE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKUP Function

Deletes a full backup. You cannot delete automatic backups using this API.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_BACKUP_DESTINATION Function

Deletes a backup destination in an Exadata Cloud@Customer system.

Syntax
```

```

Parameters

Parameter Description

`backup_destination_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CLOUD_AUTONOMOUS_VM_CLUSTER Function

Deletes the specified Autonomous Exadata VM cluster in the Oracle cloud. For Exadata Cloud@Customer systems, see`DELETE_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CLOUD_EXADATA_INFRASTRUCTURE Function

Deletes the cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`is_delete_vm_clusters`

(optional) If `true`, forces the deletion the specified cloud Exadata infrastructure resource as well as all associated VM clusters. If `false`, the cloud Exadata infrastructure resource can be deleted only if it has no associated VM clusters. Default value is `false`.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CLOUD_VM_CLUSTER Function

Deletes the specified cloud VM cluster. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONSOLE_CONNECTION Function

Deletes the specified database node console connection.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_connection_id`

(required) The OCID of the console connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONSOLE_HISTORY Function

Deletes the specified database node console history.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_history_id`

(required) The OCID of the console history.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE Function

Deletes the specified database. Applies only to Exadata systems. The data in this database is local to the Exadata system and will be lost when the database is deleted. Oracle recommends that you back up any data in the Exadata system prior to deleting it. You can use the `performFinalBackup` parameter to have the Exadata system database backed up before it is deleted.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`perform_final_backup`

(optional) Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work. This parameter is used in multiple APIs. Refer to the API description for details on how the operation uses it.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE_SOFTWARE_IMAGE Function

Delete a database software image

Syntax
```

```

Parameters

Parameter Description

`database_software_image_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DB_HOME Function

Deletes a Database Home. Applies to bare metal DB systems, Exadata Cloud Service, and Exadata Cloud@Customer systems. Oracle recommends that you use the `performFinalBackup` parameter to back up any data on a bare metal DB system before you delete a Database Home. On an Exadata Cloud@Customer system or an Exadata Cloud Service system, you can delete a Database Home only when there are no databases in it and therefore you cannot use the `performFinalBackup` parameter to back up data.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`perform_final_backup`

(optional) Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work. This parameter is used in multiple APIs. Refer to the API description for details on how the operation uses it.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXADATA_INFRASTRUCTURE Function

Deletes the Exadata Cloud@Customer infrastructure.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_CONTAINER_DATABASE Function

Deletes the`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function resource. Any external pluggable databases registered under this container database must be deleted in your Oracle Cloud Infrastructure tenancy prior to this operation.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_DATABASE_CONNECTOR Function

Deletes an external database connector. Any services enabled using the external database connector must be deleted prior to this operation.

Syntax
```

```

Parameters

Parameter Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector resource (`ExternalDatabaseConnectorId`).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_NON_CONTAINER_DATABASE Function

Deletes the Oracle Cloud Infrastructure resource representing an external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_EXTERNAL_PLUGGABLE_DATABASE Function

Deletes the`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function. resource.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_KEY_STORE Function

Deletes a key store.

Syntax
```

```

Parameters

Parameter Description

`key_store_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ONEOFF_PATCH Function

Deletes a one-off patch.

Syntax
```

```

Parameters

Parameter Description

`oneoff_patch_id`

(required) The one-off patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PLUGGABLE_DATABASE Function

Deletes the specified pluggable database.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VM_CLUSTER Function

Deletes the specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_VM_CLUSTER_NETWORK Function

Deletes the specified VM cluster network. Applies to Exadata Cloud@Customer instances only. To delete a cloud VM cluster in an Exadata Cloud Service instance, use the`DELETE_CLOUD_VM_CLUSTER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE Function

Asynchronously deregisters this Autonomous Database with Data Safe.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`deregister_autonomous_database_data_safe_details`

(optional) Details for deregistering an Autonomous Database with Data Safe.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AUTONOMOUS_DATABASE_MANAGEMENT Function

Disables Database Management for the Autonomous Database resource.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS Function

Disables Operations Insights for the Autonomous Database resource.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_DATABASE_MANAGEMENT Function

Disables the Database Management service for the database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function

Disable Database Management service for the external container database.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING Function

Disable Stack Monitoring for the external container database.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function

Disable Database Management Service for the external non-container database. For more information about the Database Management Service, see[Database Management Service](https://docs.oracle.com/iaas/database-management/index.html).

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS Function

Disable Operations Insights for the external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING Function

Disable Stack Monitoring for the external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT Function

Disable Database Management Service for the external pluggable database. For more information about the Database Management Service, see[Database Management Service](https://docs.oracle.com/iaas/database-management/index.html).

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS Function

Disable Operations Insights for the external pluggable database.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING Function

Disable Stack Monitoring for the external pluggable database.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISABLE_PLUGGABLE_DATABASE_MANAGEMENT Function

Disables the Database Management service for the pluggable database.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_EXADATA_INFRASTRUCTURE_CONFIG_FILE Function

Downloads the configuration file for the specified Exadata Cloud@Customer infrastructure.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_ONEOFF_PATCH Function

Download one-off patch.

Syntax
```

```

Parameters

Parameter Description

`oneoff_patch_id`

(required) The one-off patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_VALIDATION_REPORT Function

Downloads the network validation report file for the specified VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_VM_CLUSTER_NETWORK_CONFIG_FILE Function

Downloads the configuration file for the specified VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_AUTONOMOUS_DATABASE_MANAGEMENT Function

Enables Database Management for Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS Function

Enables the specified Autonomous Database with Operations Insights.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_DATABASE_MANAGEMENT Function

Enables the Database Management service for an Oracle Database located in Oracle Cloud Infrastructure. This service allows the database to access tools including Metrics and Performance hub. Database Management is enabled at the container database (CDB) level.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_database_management_details`

(required) Request to enable the Database Management service for an Oracle Database located in Oracle Cloud Infrastructure.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function

Enables Database Management Service for the external container database. For more information about the Database Management Service, see[Database Management Service](https://docs.oracle.com/iaas/database-management/index.html).

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_container_database_database_management_details`

(required) Request to enable the Database Management Service for an external container database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING Function

Enable Stack Monitoring for the external container database.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_container_database_stack_monitoring_details`

(required) Details to enable Stack Monitoring on the external container database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function

Enable Database Management Service for the external non-container database. For more information about the Database Management Service, see[Database Management Service](https://docs.oracle.com/iaas/database-management/index.html).

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_non_container_database_database_management_details`

(required) Request to enable the Database Management Service for an external non-container database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS Function

Enable Operations Insights for the external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_non_container_database_operations_insights_details`

(required) Details to enable Operations Insights on the external non-container database

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING Function

Enable Stack Monitoring for the external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_non_container_database_stack_monitoring_details`

(required) Details to enable Stack Monitoring on the external non-container database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT Function

Enable Database Management Service for the external pluggable database. For more information about the Database Management Service, see[Database Management Service](https://docs.oracle.com/iaas/database-management/index.html).

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_pluggable_database_database_management_details`

(required) Request to enable the Database Management Service for an external database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS Function

Enable Operations Insights for the external pluggable database.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_pluggable_database_operations_insights_details`

(required) Details to enable Operations Insights on the external pluggable database

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING Function

Enable Stack Monitoring for the external pluggable database.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_external_pluggable_database_stack_monitoring_details`

(required) Details to enable Stack Monitoring on the external pluggable database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_PLUGGABLE_DATABASE_MANAGEMENT Function

Enables the Database Management service for an Oracle Pluggable Database located in Oracle Cloud Infrastructure. This service allows the pluggable database to access tools including Metrics and Performance hub. Database Management is enabled at the pluggable database (PDB) level.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`enable_pluggable_database_management_details`

(required) Request to enable the Database Management service for an Oracle Pluggable Database located in Oracle Cloud Infrastructure.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FAIL_OVER_AUTONOMOUS_DATABASE Function

Initiates a failover the specified Autonomous Database to a standby. To perform a failover to a standby located in a remote region, specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote standby using the `peerDbId` parameter.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`peer_db_id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Data Guard standby database located in a different (remote) region from the source primary Autonomous Database.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FAILOVER_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Fails over the standby Autonomous Container Database identified by the autonomousContainerDatabaseId parameter to the primary Autonomous Container Database after the existing primary Autonomous Container Database fails or becomes unreachable. A failover can result in data loss, depending on the protection mode in effect at the time the primary Autonomous Container Database fails.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### FAILOVER_DATA_GUARD_ASSOCIATION Function

Performs a failover to transition the standby database identified by the `databaseId` parameter into the specified Data Guard association's primary role after the existing primary database fails or becomes unreachable. A failover might result in data loss depending on the protection mode in effect at the time of the primary database failure.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`data_guard_association_id`

(required) The Data Guard association's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`failover_data_guard_association_details`

(required) A request to perform a failover, transitioning a standby database into a primary database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_AUTONOMOUS_DATABASE_WALLET Function

Creates and downloads a wallet for the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`generate_autonomous_database_wallet_details`

(required) Request to create a new Autonomous Database wallet.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_RECOMMENDED_VM_CLUSTER_NETWORK Function

Generates a recommended Cloud@Customer VM cluster network configuration.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`generate_recommended_network_details`

(required) Request to generate a recommended Cloud@Customer VM cluster network configuration.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION_VIP Function

Gets information about a specified application virtual IP (VIP) address.

Syntax
```

```

Parameters

Parameter Description

`application_vip_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application virtual IP (VIP) address.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_CONTAINER_DATABASE Function

Gets information about the specified Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Gets an Autonomous Container Database enabled with Autonomous Data Guard associated with the specified Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_CONTAINER_DATABASE_RESOURCE_USAGE Function

Get resource usage details for the specified Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_DATABASE Function

Gets the details of the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_DATABASE_BACKUP Function

Gets information about the specified Autonomous Database backup.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATION Function

Gets an Autonomous Data Guard-enabled database associated with the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_DATABASE_REGIONAL_WALLET Function

Gets the Autonomous Database regional wallet details.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_DATABASE_WALLET Function

Gets the wallet details for the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function

**Deprecated.** Use the`GET_CLOUD_EXADATA_INFRASTRUCTURE`Function operation to get details of an Exadata Infrastructure resource and the`GET_CLOUD_AUTONOMOUS_VM_CLUSTER`Function operation to get details of an Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_PATCH Function

Gets information about a specific autonomous patch.

Syntax
```

```

Parameters

Parameter Description

`autonomous_patch_id`

(required) The autonomous patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_VIRTUAL_MACHINE Function

Gets the details of specific Autonomous Virtual Machine.

Syntax
```

```

Parameters

Parameter Description

`autonomous_virtual_machine_id`

(required) The Autonomous Virtual machine[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_VM_CLUSTER Function

Gets information about the specified Autonomous VM cluster for an Exadata Cloud@Customer system. To get information about an Autonomous VM Cluster in the Oracle cloud, see`GET_CLOUD_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE Function

Get the resource usage details for the specified Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKUP Function

Gets information about the specified backup.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BACKUP_DESTINATION Function

Gets information about the specified backup destination in an Exadata Cloud@Customer system.

Syntax
```

```

Parameters

Parameter Description

`backup_destination_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_AUTONOMOUS_VM_CLUSTER Function

Gets information about the specified Autonomous Exadata VM cluster in the Oracle cloud. For Exadata Cloud@Custustomer systems, see`GET_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE Function

Get the resource usage details for the specified Cloud Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_EXADATA_INFRASTRUCTURE Function

Gets information about the specified cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_EXADATA_INFRASTRUCTURE_UNALLOCATED_RESOURCES Function

Gets unallocated resources information for the specified Cloud Exadata infrastructure.

Syntax
```

```

Parameters

Parameter Description

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_VM_CLUSTER Function

Gets information about the specified cloud VM cluster. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_VM_CLUSTER_IORM_CONFIG Function

Gets the IORM configuration for the specified cloud VM cluster in an Exadata Cloud Service instance. If you have not specified an IORM configuration, the default configuration is returned.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_VM_CLUSTER_UPDATE Function

Gets information about a specified maintenance update package for a cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CLOUD_VM_CLUSTER_UPDATE_HISTORY_ENTRY Function

Gets the maintenance update history details for the specified update history entry. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_history_entry_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONSOLE_CONNECTION Function

Gets the specified database node console connection's information.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_connection_id`

(required) The OCID of the console connection.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONSOLE_HISTORY Function

Gets information about the specified database node console history.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_history_id`

(required) The OCID of the console history.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONSOLE_HISTORY_CONTENT Function

Retrieves the specified database node console history contents upto a megabyte.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_history_id`

(required) The OCID of the console history.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_GUARD_ASSOCIATION Function

Gets the specified Data Guard association's configuration information.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`data_guard_association_id`

(required) The Data Guard association's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE Function

Gets information about the specified database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_SOFTWARE_IMAGE Function

Gets information about the specified database software image.

Syntax
```

```

Parameters

Parameter Description

`database_software_image_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_UPGRADE_HISTORY_ENTRY Function

gets the upgrade history for a specified database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`upgrade_history_entry_id`

(required) The database/db system upgrade History[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_HOME Function

Gets information about the specified Database Home.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_HOME_PATCH Function

Gets information about a specified patch package.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_HOME_PATCH_HISTORY_ENTRY Function

Gets the patch history details for the specified patchHistoryEntryId

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_history_entry_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch history entry.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_NODE Function

Gets information about the specified database node.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SERVER Function

Gets information about the Exadata Db server.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ExadataInfrastructure.

`db_server_id`

(required) The DB server[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SYSTEM Function

Gets information about the specified DB system. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SYSTEM_PATCH Function

Gets information the specified patch.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SYSTEM_PATCH_HISTORY_ENTRY Function

Gets the details of the specified patch operation on the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_history_entry_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch history entry.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DB_SYSTEM_UPGRADE_HISTORY_ENTRY Function

Gets the details of the specified operating system upgrade operation for the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`upgrade_history_entry_id`

(required) The database/db system upgrade History[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXADATA_INFRASTRUCTURE Function

Gets information about the specified Exadata infrastructure. Applies to Exadata Cloud@Customer instances only. To get information on an Exadata Cloud Service infrastructure resource, use the`GET_CLOUD_EXADATA_INFRASTRUCTURE`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`excluded_fields`

(optional) If provided, the specified fields will be excluded in the response.

Allowed values are: 'multiRackConfigurationFile'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXADATA_INFRASTRUCTURE_OCPUS Function

Gets details of the available and consumed OCPUs for the specified Autonomous Exadata Infrastructure resource.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXADATA_INFRASTRUCTURE_UN_ALLOCATED_RESOURCES Function

Gets un allocated resources information for the specified Exadata infrastructure. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`db_servers`

(optional) The list of[OCIDs](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Db servers.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXADATA_IORM_CONFIG Function

Gets the IORM configuration settings for the specified cloud Exadata DB system. All Exadata service instances have default IORM settings. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model. The`GET_CLOUD_VM_CLUSTER_IORM_CONFIG`Function API is used for this operation with Exadata systems using the new resource model.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_BACKUP_JOB Function

Gets information about the specified external backup job. **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See[Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud](https://docs.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm)for more information.

Syntax
```

```

Parameters

Parameter Description

`backup_id`

(required) The backup[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_CONTAINER_DATABASE Function

Gets information about the specified external container database.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_DATABASE_CONNECTOR Function

Gets information about the specified external database connector.

Syntax
```

```

Parameters

Parameter Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector resource (`ExternalDatabaseConnectorId`).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_NON_CONTAINER_DATABASE Function

Gets information about a specific external non-container database.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_EXTERNAL_PLUGGABLE_DATABASE Function

Gets information about a specific`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INFRASTRUCTURE_TARGET_VERSIONS Function

Gets details of the Exadata Infrastructure target system software versions that can be applied to the specified infrastructure resource for maintenance updates. Applies to Exadata Cloud@Customer and Exadata Cloud instances only.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`target_resource_id`

(optional) The target resource ID.

`target_resource_type`

(optional) The type of the target resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_KEY_STORE Function

Gets information about the specified key store.

Syntax
```

```

Parameters

Parameter Description

`key_store_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MAINTENANCE_RUN Function

Gets information about the specified maintenance run.

Syntax
```

```

Parameters

Parameter Description

`maintenance_run_id`

(required) The maintenance run OCID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MAINTENANCE_RUN_HISTORY Function

Gets information about the specified maintenance run history.

Syntax
```

```

Parameters

Parameter Description

`maintenance_run_history_id`

(required) The maintenance run history OCID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ONEOFF_PATCH Function

Gets information about the specified one-off patch.

Syntax
```

```

Parameters

Parameter Description

`oneoff_patch_id`

(required) The one-off patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PDB_CONVERSION_HISTORY_ENTRY Function

Gets the details of operations performed to convert the specified database from non-container (non-CDB) to pluggable (PDB).

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`pdb_conversion_history_entry_id`

(required) The database conversion history[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PLUGGABLE_DATABASE Function

Gets information about the specified pluggable database.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER Function

Gets information about the VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER_NETWORK Function

Gets information about the specified VM cluster network. Applies to Exadata Cloud@Customer instances only. To get information about a cloud VM cluster in an Exadata Cloud Service instance, use the`GET_CLOUD_VM_CLUSTER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER_PATCH Function

Gets information about a specified patch package.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER_PATCH_HISTORY_ENTRY Function

Gets the patch history details for the specified patch history entry.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`patch_history_entry_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the patch history entry.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER_UPDATE Function

Gets information about a specified maintenance update package for a VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_VM_CLUSTER_UPDATE_HISTORY_ENTRY Function

Gets the maintenance update history details for the specified update history entry. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_history_entry_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the maintenance update history entry.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LAUNCH_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function

**Deprecated** To create a new Autonomous Database system on dedicated Exadata Infrastructure, use the`CREATE_CLOUD_EXADATA_INFRASTRUCTURE`Function and`CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function operations instead. Note that to create an Autonomous VM cluster, you must have an existing Exadata Infrastructure resource to contain the VM cluster.

Syntax
```

```

Parameters

Parameter Description

`launch_autonomous_exadata_infrastructure_details`

(required) **Deprecated.** Use the`CREATE_CLOUD_EXADATA_INFRASTRUCTURE`Function or`CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function operations instead.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LAUNCH_DB_SYSTEM Function

Creates a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed. An initial database is created on the DB system based on the request parameters you provide and some default options. For detailed information about default options, see[Bare metal and virtual machine DB system default options.](https://docs.oracle.com/iaas/Content/Database/Tasks/creatingDBsystem.htm#Default)**Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model. Use the`CREATE_CLOUD_EXADATA_INFRASTRUCTURE`Function and`CREATE_CLOUD_VM_CLUSTER`Function APIs to provision a new Exadata Cloud Service instance.

Syntax
```

```

Parameters

Parameter Description

`launch_db_system_details`

(required) Request to launch a DB system. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATION_VIPS Function

Gets a list of application virtual IP (VIP) addresses on a cloud VM cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cloud_vm_cluster_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the cloud VM cluster associated with the application virtual IP (VIP) address.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATIONS Function

Gets a list of the Autonomous Container Databases with Autonomous Data Guard-enabled associated with the specified Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_CONTAINER_DATABASE_VERSIONS Function

Gets a list of supported Autonomous Container Database versions.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`service_component`

(required) The service component to use, either ADBD or EXACC.

Allowed values are: 'ADBD', 'EXACC'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_CONTAINER_DATABASES Function

Gets a list of the Autonomous Container Databases in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_exadata_infrastructure_id`

(optional) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_vm_cluster_id`

(optional) The Autonomous VM Cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`infrastructure_type`

(optional) A filter to return only resources that match the given Infrastructure Type.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`service_level_agreement_type`

(optional) A filter to return only resources that match the given service-level agreement type exactly.

`cloud_autonomous_vm_cluster_id`

(optional) The cloud Autonomous VM Cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASE_BACKUPS Function

Gets a list of Autonomous Database backups based on either the `autonomousDatabaseId` or `compartmentId` specified as a query parameter.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`l_type`

(optional) A filter to return only backups that matches with the given type of Backup.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASE_CHARACTER_SETS Function

Gets a list of supported character sets.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique identifier for the request.

`is_shared`

(optional) Specifies whether this request is for an Autonomous Database Serverless instance. By default, this request will be for Autonomous Database on Dedicated Exadata Infrastructure.

`is_dedicated`

(optional) Specifies if the request is for an Autonomous Database Dedicated instance. The default request is for an Autonomous Database Dedicated instance.

`character_set_type`

(optional) Specifies whether this request pertains to database character sets or national character sets.

Allowed values are: 'DATABASE', 'NATIONAL'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASE_CLONES Function

Lists the Autonomous Database clones for the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'NONE', 'TIMECREATED', 'DISPLAYNAME'

`clone_type`

(optional) A filter to return only resources that match the given clone type exactly.

Allowed values are: 'REFRESHABLE_CLONE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATIONS Function

Gets a list of the Autonomous Data Guard-enabled databases associated with the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASE_REFRESHABLE_CLONES Function

Lists the OCIDs of the Autonomous Database local and connected remote refreshable clones with the region where they exist for the specified source database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DATABASES Function

Gets a list of Autonomous Databases based on the query parameters specified.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_id`

(optional) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`infrastructure_type`

(optional) A filter to return only resources that match the given Infrastructure Type.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`db_workload`

(optional) A filter to return only autonomous database resources that match the specified workload type.

`db_version`

(optional) A filter to return only autonomous database resources that match the specified dbVersion.

`is_free_tier`

(optional) Filter on the value of the resource's 'isFreeTier' property. A value of `true` returns only Always Free resources. A value of `false` excludes Always Free resources from the returned results. Omitting this parameter returns both Always Free and paid resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`is_refreshable_clone`

(optional) Filter on the value of the resource's 'isRefreshableClone' property. A value of `true` returns only refreshable clones. A value of `false` excludes refreshable clones from the returned results. Omitting this parameter returns both refreshable clones and databases that are not refreshable clones.

`is_data_guard_enabled`

(optional) A filter to return only resources that have Data Guard enabled.

`is_resource_pool_leader`

(optional) Filter if the resource is the resource pool leader. A value of `true` returns only resource pool leader.

`resource_pool_leader_id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resourcepool Leader Autonomous Database.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DB_PREVIEW_VERSIONS Function

Gets a list of supported Autonomous Database versions. Note that preview version software is only available for Autonomous Database Serverless (https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) databases.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for DBWORKLOAD is ascending. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'DBWORKLOAD'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_DB_VERSIONS Function

Gets a list of supported Autonomous Database versions.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`db_workload`

(optional) A filter to return only autonomous database resources that match the specified workload type.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SHAPES Function

**Deprecated.**

Syntax
```

```

Parameters

Parameter Description

`availability_domain`

(required) The name of the Availability Domain.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_EXADATA_INFRASTRUCTURES Function

**Deprecated.** Use the`LIST_CLOUD_EXADATA_INFRASTRUCTURES`Function operation to list Exadata Infrastructures in the Oracle cloud and the`LIST_CLOUD_AUTONOMOUS_VM_CLUSTERS`Function operation to list Autonomous Exadata VM clusters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_VIRTUAL_MACHINES Function

Lists the Autonomous Virtual Machines in the specified Autonomous VM Cluster and Compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_vm_cluster_id`

(required) The Autonomous Virtual machine[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_VM_CLUSTER_ACD_RESOURCE_USAGE Function

Gets the list of resource usage details for all the Autonomous Container Database in the specified Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTONOMOUS_VM_CLUSTERS Function

Gets a list of Exadata Cloud@Customer Autonomous VM clusters in the specified compartment. To list Autonomous VM Clusters in the Oracle Cloud, see`LIST_CLOUD_AUTONOMOUS_VM_CLUSTERS`Function.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_infrastructure_id`

(optional) If provided, filters the results for the given Exadata Infrastructure.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKUP_DESTINATION Function

Gets a list of backup destinations in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`l_type`

(optional) A filter to return only resources that match the given type of the Backup Destination.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BACKUPS Function

Gets a list of backups based on the `databaseId` or `compartmentId` specified. Either one of these query parameters must be provided.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_AUTONOMOUS_VM_CLUSTER_ACD_RESOURCE_USAGE Function

Gets the list of resource usage details for all the Cloud Autonomous Container Database in the specified Cloud Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_AUTONOMOUS_VM_CLUSTERS Function

Lists Autonomous Exadata VM clusters in the Oracle cloud. For Exadata Cloud@Customer systems, see`LIST_AUTONOMOUS_VM_CLUSTERS`Function.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cloud_exadata_infrastructure_id`

(optional) If provided, filters the results for the specified cloud Exadata infrastructure.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_EXADATA_INFRASTRUCTURES Function

Gets a list of the cloud Exadata infrastructure resources in the specified compartment. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_VM_CLUSTER_UPDATE_HISTORY_ENTRIES Function

Gets the history of the maintenance update actions performed on the specified cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_type`

(optional) A filter to return only resources that match the given update type exactly.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_VM_CLUSTER_UPDATES Function

Lists the maintenance updates that can be applied to the specified cloud VM cluster. Applies to Exadata Cloud Service instances only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_type`

(optional) A filter to return only resources that match the given update type exactly.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CLOUD_VM_CLUSTERS Function

Gets a list of the cloud VM clusters in the specified compartment. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cloud_exadata_infrastructure_id`

(optional) If provided, filters the results for the specified cloud Exadata infrastructure.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only cloud VM clusters that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONSOLE_CONNECTIONS Function

Lists the console connections for the specified database node.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONSOLE_HISTORIES Function

Lists the console histories for the specified database node.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONTAINER_DATABASE_PATCHES Function

Lists the patches applicable to the requested container database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`autonomous_patch_type`

(optional) Autonomous patch type, either \"QUARTERLY\" or \"TIMEZONE\".

Allowed values are: 'QUARTERLY', 'TIMEZONE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_GUARD_ASSOCIATIONS Function

Lists all Data Guard associations for the specified database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_SOFTWARE_IMAGES Function

Gets a list of the database software images in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`image_type`

(optional) A filter to return only resources that match the given image type exactly.

`image_shape_family`

(optional) A filter to return only resources that match the given image shape family exactly.

`is_upgrade_supported`

(optional) If provided, filters the results to the set of database versions which are supported for Upgrade.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_UPGRADE_HISTORY_ENTRIES Function

Gets the upgrade history for a specified database in a bare metal or virtual machine DB system.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`upgrade_action`

(optional) A filter to return only upgradeHistoryEntries that match the specified Upgrade Action.

`lifecycle_state`

(optional) A filter to return only upgradeHistoryEntries that match the given lifecycle state exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is ascending.

Allowed values are: 'TIMESTARTED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASES Function

Gets a list of the databases in the specified Database Home.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`db_home_id`

(optional) A Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exadata DB system that you want to filter the database results by. Applies only to Exadata DB systems.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DBNAME is ascending. The DBNAME sort order is case sensitive.

Allowed values are: 'DBNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`db_name`

(optional) A filter to return only resources that match the entire database name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_HOME_PATCH_HISTORY_ENTRIES Function

Lists the history of patch operations on the specified Database Home.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_HOME_PATCHES Function

Lists patches applicable to the requested Database Home.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_HOMES Function

Lists the Database Homes in the specified DB system and compartment. A Database Home is a directory where Oracle Database software is installed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`db_system_id`

(optional) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of database versions which are supported for the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`backup_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup. Specify a backupId to list only the DB systems or DB homes that support creating a database using this backup in this compartment.

`db_version`

(optional) A filter to return only DB Homes that match the specified dbVersion.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_NODES Function

Lists the database nodes in the specified DB system and compartment. A database node is a server running database software.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`db_system_id`

(optional) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of database versions which are supported for the DB system.

`vm_cluster_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VM cluster.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) Sort by TIMECREATED. Default order for TIMECREATED is descending.

Allowed values are: 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`db_server_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Exacc Db server.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SERVERS Function

Lists the Exadata DB servers in the ExadataInfrastructureId and specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_infrastructure_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the ExadataInfrastructure.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`sort_by`

(optional) Sort by TIMECREATED. Default order for TIMECREATED is descending.

Allowed values are: 'TIMECREATED'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_COMPUTE_PERFORMANCES Function

Gets a list of expected compute performance parameters for a virtual machine DB system based on system configuration.

Syntax
```

```

Parameters

Parameter Description

`db_system_shape`

(optional) If provided, filters the results to the set of database versions which are supported for the given shape.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_PATCH_HISTORY_ENTRIES Function

Gets the history of the patch actions performed on the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_PATCHES Function

Lists the patches applicable to the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_SHAPES Function

Gets a list of the shapes that can be used to launch a new DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`availability_domain`

(optional) The name of the Availability Domain.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_STORAGE_PERFORMANCES Function

Gets a list of possible expected storage performance parameters of a VMDB System based on Configuration.

Syntax
```

```

Parameters

Parameter Description

`storage_management`

(required) The DB system storage management option. Used to list database versions available for that storage manager. Valid values are `ASM` and `LVM`. * ASM specifies Oracle Automatic Storage Management * LVM specifies logical volume manager, sometimes called logical disk manager.

`shape_type`

(optional) Optional. Filters the performance results by shape type.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEM_UPGRADE_HISTORY_ENTRIES Function

Gets the history of the upgrade actions performed on the specified DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is ascending.

Allowed values are: 'TIMESTARTED'

`upgrade_action`

(optional) A filter to return only upgradeHistoryEntries that match the specified Upgrade Action.

`lifecycle_state`

(optional) A filter to return only upgrade history entries that match the given lifecycle state exactly.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_SYSTEMS Function

Lists the DB systems in the specified compartment. You can specify a `backupId` to list only the DB systems that support creating a database using this backup in this compartment. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`backup_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup. Specify a backupId to list only the DB systems or DB homes that support creating a database using this backup in this compartment.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_VERSIONS Function

Gets a list of supported Oracle Database versions.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`db_system_shape`

(optional) If provided, filters the results to the set of database versions which are supported for the given shape.

`db_system_id`

(optional) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of database versions which are supported for the DB system.

`storage_management`

(optional) The DB system storage management option. Used to list database versions available for that storage manager. Valid values are `ASM` and `LVM`. * ASM specifies Oracle Automatic Storage Management * LVM specifies logical volume manager, sometimes called logical disk manager.

`is_upgrade_supported`

(optional) If provided, filters the results to the set of database versions which are supported for Upgrade.

`is_database_software_image_supported`

(optional) If true, filters the results to the set of Oracle Database versions that are supported for OCI database software images.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXADATA_INFRASTRUCTURES Function

Lists the Exadata infrastructure resources in the specified compartment. Applies to Exadata Cloud@Customer instances only. To list the Exadata Cloud Service infrastructure resources in a compartment, use the`LIST_CLOUD_EXADATA_INFRASTRUCTURES`Function operation.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`excluded_fields`

(optional) If provided, the specified fields will be excluded in the response.

Allowed values are: 'multiRackConfigurationFile'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_CONTAINER_DATABASES Function

Gets a list of the external container databases in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_DATABASE_CONNECTORS Function

Gets a list of the external database connectors in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`external_database_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database whose connectors will be listed.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_NON_CONTAINER_DATABASES Function

Gets a list of the ExternalNonContainerDatabases in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_EXTERNAL_PLUGGABLE_DATABASES Function

Gets a list of the`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resources in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`external_container_database_id`

(optional) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FLEX_COMPONENTS Function

Gets a list of the flex components that can be used to launch a new DB system. The flex component determines resources to allocate to the DB system - Database Servers and Storage Servers.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`name`

(optional) A filter to return only resources that match the entire name given. The match is not case sensitive.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for NAME is ascending. The NAME sort order is case sensitive.

Allowed values are: 'NAME'

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GI_VERSIONS Function

Gets a list of supported GI versions for the Exadata Cloud@Customer VM cluster.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`shape`

(optional) If provided, filters the results for the given shape.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_KEY_STORES Function

Gets a list of key stores in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MAINTENANCE_RUN_HISTORY Function

Gets a list of the maintenance run histories in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`target_resource_id`

(optional) The target resource ID.

`target_resource_type`

(optional) The type of the target resource.

`maintenance_type`

(optional) The maintenance type.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIME_SCHEDULED and TIME_ENDED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIME_SCHEDULED', 'TIME_ENDED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) The state of the maintenance run history.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`maintenance_subtype`

(optional) The sub-type of the maintenance run.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MAINTENANCE_RUNS Function

Gets a list of the maintenance runs in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`target_resource_id`

(optional) The target resource ID.

`target_resource_type`

(optional) The type of the target resource.

`maintenance_type`

(optional) The maintenance type.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIME_SCHEDULED and TIME_ENDED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive. **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIME_SCHEDULED', 'TIME_ENDED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`availability_domain`

(optional) A filter to return only resources that match the given availability domain exactly.

`maintenance_subtype`

(optional) The sub-type of the maintenance run.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ONEOFF_PATCHES Function

Lists one-off patches in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PDB_CONVERSION_HISTORY_ENTRIES Function

Gets the pluggable database conversion history for a specified database in a bare metal or virtual machine DB system.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`pdb_conversion_action`

(optional) A filter to return only the pluggable database conversion history entries that match the specified conversion action. For example, you can use this filter to return only entries for the precheck operation.

`lifecycle_state`

(optional) A filter to return only the pluggable database conversion history entries that match the specified lifecycle state. For example, you can use this filter to return only entries in the \"failed\" lifecycle state.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). The default order for `TIMECREATED` is ascending.

Allowed values are: 'TIMESTARTED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PLUGGABLE_DATABASES Function

Gets a list of the pluggable databases in a database or compartment. You must provide either a `databaseId` or `compartmentId` value.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for PDBNAME is ascending. The PDBNAME sort order is case sensitive.

Allowed values are: 'PDBNAME', 'TIMECREATED'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`pdb_name`

(optional) A filter to return only pluggable databases that match the entire name given. The match is not case sensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SYSTEM_VERSIONS Function

Gets a list of supported Exadata system versions for a given shape and GI version.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`shape`

(required) Specifies shape query parameter.

`gi_version`

(required) Specifies gi version query parameter.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTER_NETWORKS Function

Gets a list of the VM cluster networks in the specified compartment. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTER_PATCH_HISTORY_ENTRIES Function

Gets the history of the patch actions performed on the specified VM cluster in an Exadata Cloud@Customer system.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTER_PATCHES Function

Lists the patches applicable to the specified VM cluster in an Exadata Cloud@Customer system.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTER_UPDATE_HISTORY_ENTRIES Function

Gets the history of the maintenance update actions performed on the specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_type`

(optional) A filter to return only resources that match the given update type exactly.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTER_UPDATES Function

Lists the maintenance updates that can be applied to the specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_type`

(optional) A filter to return only resources that match the given update type exactly.

Allowed values are: 'GI_UPGRADE', 'GI_PATCH', 'OS_UPDATE'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_VM_CLUSTERS Function

Lists the VM clusters in the specified compartment. Applies to Exadata Cloud@Customer instances only. To list the cloud VM clusters in an Exadata Cloud Service instance, use the`LIST_CLOUD_VM_CLUSTERS`Function operation.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_infrastructure_id`

(optional) If provided, filters the results for the given Exadata Infrastructure.

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycle state exactly.

`display_name`

(optional) A filter to return only resources that match the entire display name given. The match is not case sensitive.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LOCAL_CLONE_PLUGGABLE_DATABASE Function

**Deprecated.** Use`CREATE_PLUGGABLE_DATABASE`Function for Pluggable Database LocalClone Operation. Clones and starts a pluggable database (PDB) in the same database (CDB) as the source PDB. The source PDB must be in the `READ_WRITE` openMode to perform the clone operation.

Syntax
```

```

Parameters

Parameter Description

`local_clone_pluggable_database_details`

(required) Request to clone a pluggable database locally.

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MIGRATE_EXADATA_DB_SYSTEM_RESOURCE_MODEL Function

Migrates the Exadata DB system to the new[Exadata resource model](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model). All related resources will be migrated.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MIGRATE_VAULT_KEY Function

Changes encryption key management from customer-managed, using the[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm), to Oracle-managed.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`migrate_vault_key_details`

(required) Request to change the source of the encryption key for the database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MODIFY_DATABASE_MANAGEMENT Function

Updates one or more attributes of the Database Management service for the database.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`modify_database_management_details`

(required) The data to update one or more attributes of the Database Management Service for the database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MODIFY_PLUGGABLE_DATABASE_MANAGEMENT Function

Updates one or more attributes of the Database Management service for the pluggable database.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`modify_pluggable_database_management_details`

(required) The data to update one or more attributes of the Database Management Service for the pluggable database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_PLUGGABLE_DATABASE Function

Refreshes a pluggable database (PDB) Refreshable clone.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE Function

Asynchronously registers this Autonomous Database with Data Safe.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`register_autonomous_database_data_safe_details`

(optional) Request to register an Autonomous Database with Data Safe.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REINSTATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Reinstates a disabled standby Autonomous Container Database, identified by the autonomousContainerDatabaseId parameter, to an active standby Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REINSTATE_DATA_GUARD_ASSOCIATION Function

Reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`data_guard_association_id`

(required) The Data Guard association's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`reinstate_data_guard_association_details`

(required) A request to reinstate a database in a standby role.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOTE_CLONE_PLUGGABLE_DATABASE Function

**Deprecated.** Use`CREATE_PLUGGABLE_DATABASE`Function for Pluggable Database RemoteClone Operation. Clones a pluggable database (PDB) to a different database from the source PDB. The cloned PDB will be started upon completion of the clone operation. The source PDB must be in the `READ_WRITE` openMode when performing the clone. For Exadata Cloud@Customer instances, the source pluggable database (PDB) must be on the same Exadata Infrastructure as the target container database (CDB) to create a remote clone.

Syntax
```

```

Parameters

Parameter Description

`remote_clone_pluggable_database_details`

(required) Request to clone a pluggable database (PDB) to a different database (CDB) from the source PDB.

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_VIRTUAL_MACHINE_FROM_CLOUD_VM_CLUSTER Function

Remove Virtual Machines from the Cloud VM cluster. Applies to Exadata Cloud instances only.

Syntax
```

```

Parameters

Parameter Description

`remove_virtual_machine_from_cloud_vm_cluster_details`

(required) Request to remove Virtual Machines from the Cloud VM cluster.

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_VIRTUAL_MACHINE_FROM_VM_CLUSTER Function

Remove Virtual Machines from the VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`remove_virtual_machine_from_vm_cluster_details`

(required) Request to remove Virtual Machines from the VM cluster.

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESIZE_VM_CLUSTER_NETWORK Function

Adds or removes Db server network nodes to extend or shrink the existing VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`resize_vm_cluster_network_details`

(required) Request to add or remove Db server network nodes in the VM cluster network.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESOURCE_POOL_SHAPES Function

Lists available resource pools shapes.

Syntax
```

```

Parameters

Parameter Description

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The pagination token to continue listing from.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTART_AUTONOMOUS_CONTAINER_DATABASE Function

Rolling restarts the specified Autonomous Container Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTART_AUTONOMOUS_DATABASE Function

Restarts the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTORE_AUTONOMOUS_DATABASE Function

Restores an Autonomous Database based on the provided request parameters.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`restore_autonomous_database_details`

(required) Request to perform an Autonomous Database restore.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTORE_DATABASE Function

Restore a Database based on the request parameters you provide.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`restore_database_details`

(required) Request to perform database restore.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_AUTONOMOUS_CONTAINER_DATABASE_ENCRYPTION_KEY Function

Creates a new version of an existing[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)key.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_AUTONOMOUS_DATABASE_ENCRYPTION_KEY Function

Rotate existing AutonomousDatabase[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)key.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS Function

Rotates the Oracle REST Data Services (ORDS) certificates for Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`rotate_autonomous_vm_cluster_ords_certs_details`

(required) Request to rotate the Oracle REST Data Services (ORDS) certificates on Autonomous Exadata VM cluster.

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_AUTONOMOUS_VM_CLUSTER_SSL_CERTS Function

Rotates the SSL certificates for Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`rotate_autonomous_vm_cluster_ssl_certs_details`

(required) Request to rotate the SSL certificates on Autonomous Exadata VM cluster.

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS Function

Rotates the Oracle REST Data Services (ORDS) certificates for a cloud Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`rotate_cloud_autonomous_vm_cluster_ords_certs_details`

(optional) Request to rotate the Oracle REST Data Services (ORDS) certificates on Cloud Autonomous Exadata VM cluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_SSL_CERTS Function

Rotates the SSL certficates for a cloud Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`rotate_cloud_autonomous_vm_cluster_ssl_certs_details`

(optional) Request to rotate the SSL certificates on Cloud Autonomous Exadata VM cluster.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_ORDS_CERTS Function

**Deprecated.** Use the`ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS`Function to rotate Oracle REST Data Services (ORDS) certs for an Autonomous Exadata VM cluster instead.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_PLUGGABLE_DATABASE_ENCRYPTION_KEY Function

Create a new version of the existing encryption key.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_SSL_CERTS Function

**Deprecated.** Use the`ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_SSL_CERTS`Function to rotate SSL certs for an Autonomous Exadata VM cluster instead.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROTATE_VAULT_KEY Function

Creates a new version of an existing[Vault service](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)key.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SAAS_ADMIN_USER_STATUS Function

This operation gets SaaS administrative user status of the Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SCAN_EXTERNAL_CONTAINER_DATABASE_PLUGGABLE_DATABASES Function

Scans for pluggable databases in the specified external container database. This operation will return un-registered pluggable databases in the`GET_WORK_REQUEST`Function operation.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector resource (`ExternalDatabaseConnectorId`).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SHRINK_AUTONOMOUS_DATABASE Function

This operation shrinks the current allocated storage down to the current actual used data storage (actualUsedDataStorageSizeInTBs). The if the base storage value for the database (dataStorageSizeInTBs) is larger than the actualUsedDataStorageSizeInTBs value, you are billed for the base storage value.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_AUTONOMOUS_DATABASE Function

Starts the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_PLUGGABLE_DATABASE Function

Starts a stopped pluggable database. The `openMode` value of the pluggable database will be `READ_WRITE` upon completion.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_AUTONOMOUS_DATABASE Function

Stops the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_PLUGGABLE_DATABASE Function

Stops a pluggable database. The `openMode` value of the pluggable database will be `MOUNTED` upon completion.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SWITCHOVER_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Switches over the primary Autonomous Container Database of an Autonomous Data Guard peer association to standby role. The standby Autonomous Container Database associated with autonomousContainerDatabaseDataguardAssociationId assumes the primary Autonomous Container Database role. A switchover incurs no data loss.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SWITCHOVER_AUTONOMOUS_DATABASE Function

Initiates a switchover of the specified Autonomous Database to the associated standby database. Applicable only to databases with Autonomous Data Guard enabled. To perform a switchover to a standby located in a remote region, specify the[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the remote standby using the `peerDbId` parameter.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique identifier for the request.

`peer_db_id`

(optional) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Data Guard standby database located in a different (remote) region from the source primary Autonomous Database.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SWITCHOVER_DATA_GUARD_ASSOCIATION Function

Performs a switchover to transition the primary database of a Data Guard association into a standby role. The standby database associated with the `dataGuardAssociationId` assumes the primary database role. A switchover guarantees no data loss.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`data_guard_association_id`

(required) The Data Guard association's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`switchover_data_guard_association_details`

(required) Request to swtichover a primary to a standby.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TERMINATE_AUTONOMOUS_CONTAINER_DATABASE Function

Terminates an Autonomous Container Database, which permanently deletes the container database and any databases within the container database. The database data is local to the Autonomous Exadata Infrastructure and will be lost when the container database is terminated. Oracle recommends that you back up any data in the Autonomous Container Database prior to terminating it.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TERMINATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function

**Deprecated.** To terminate an Exadata Infrastructure resource in the Oracle cloud, use the`DELETE_CLOUD_EXADATA_INFRASTRUCTURE`Function operation. To delete an Autonomous Exadata VM cluster in the Oracle cloud, use the`DELETE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TERMINATE_DB_SYSTEM Function

Terminates a DB system and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB system and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB system prior to terminating it. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_CONTAINER_DATABASE Function

Updates the properties of an Autonomous Container Database, such as display name, maintenance preference, backup retention, and tags.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_container_database_details`

(required) Request to update the properties of an Autonomous Container Database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function

Update Autonomous Data Guard association.

Syntax
```

```

Parameters

Parameter Description

`autonomous_container_database_id`

(required) The Autonomous Container Database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`autonomous_container_database_dataguard_association_id`

(required) The Autonomous Container Database-Autonomous Data Guard association[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_container_database_data_guard_association_details`

(required) A request to update Data Guard association of a database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_DATABASE Function

Updates one or more attributes of the specified Autonomous Database. See the UpdateAutonomousDatabaseDetails resource for a full list of attributes that can be updated.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_database_details`

(required) Request to update the properties of an Autonomous Database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_DATABASE_BACKUP Function

Updates the Autonomous Database backup of the specified database based on the request parameters.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_backup_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Autonomous Database backup.

`update_autonomous_database_backup_details`

(required) Request to update an existing Autonomous Database backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_DATABASE_REGIONAL_WALLET Function

Updates the Autonomous Database regional wallet.

Syntax
```

```

Parameters

Parameter Description

`update_autonomous_database_wallet_details`

(required) Request to update the properties of Autonomous Database regional wallet.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_DATABASE_WALLET Function

Updates the wallet for the specified Autonomous Database.

Syntax
```

```

Parameters

Parameter Description

`autonomous_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_database_wallet_details`

(required) Request to update the properties of an Autonomous Database wallet.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function

**Deprecated.** Use the`UPDATE_CLOUD_EXADATA_INFRASTRUCTURE`Function operation to update an Exadata Infrastructure resource and`UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function operation to update an Autonomous Exadata VM cluster.

Syntax
```

```

Parameters

Parameter Description

`autonomous_exadata_infrastructure_id`

(required) The Autonomous Exadata Infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_exadata_infrastructures_details`

(required) Request to update the properties of a Autonomous Exadata Infrastructure.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTONOMOUS_VM_CLUSTER Function

Updates the specified Autonomous VM cluster for the Exadata Cloud@Customer system.To update an Autonomous VM Cluster in the Oracle cloud, see`UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`autonomous_vm_cluster_id`

(required) The autonomous VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_autonomous_vm_cluster_details`

(required) Request to update the attributes of an Autonomous VM cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BACKUP_DESTINATION Function

If no database is associated with the backup destination: - For a RECOVERY_APPLIANCE backup destination, updates the connection string and/or the list of VPC users. - For an NFS backup destination, updates the NFS location.

Syntax
```

```

Parameters

Parameter Description

`backup_destination_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup destination.

`update_backup_destination_details`

(required) For a RECOVERY_APPLIANCE backup destination, request to update the connection string and/or the list of VPC users. For an NFS backup destination, request to update the NFS location.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER Function

Updates the specified Autonomous Exadata VM cluster in the Oracle cloud. For Exadata Cloud@Customer systems, see`UPDATE_AUTONOMOUS_VM_CLUSTER`Function.

Syntax
```

```

Parameters

Parameter Description

`cloud_autonomous_vm_cluster_id`

(required) The Cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_cloud_autonomous_vm_cluster_details`

(required) Request to update the attributes of a cloud VM cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLOUD_EXADATA_INFRASTRUCTURE Function

Updates the Cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_exadata_infrastructure_id`

(required) The cloud Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_cloud_exadata_infrastructure_details`

(required) Request to update the properties of an cloud Exadata infrastructure resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLOUD_VM_CLUSTER Function

Updates the specified cloud VM cluster. Applies to Exadata Cloud Service instances and Autonomous Database on dedicated Exadata infrastructure only.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_cloud_vm_cluster_details`

(required) Request to update the attributes of a cloud VM cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CLOUD_VM_CLUSTER_IORM_CONFIG Function

Updates the IORM settings for the specified cloud VM cluster in an Exadata Cloud Service instance.

Syntax
```

```

Parameters

Parameter Description

`cloud_vm_cluster_id`

(required) The cloud VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`cloud_vm_cluster_iorm_config_update_details`

(required) Request to perform database update.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONSOLE_CONNECTION Function

Updates the specified database node console connection.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_connection_id`

(required) The OCID of the console connection.

`update_console_connection_details`

(required) Request to update the specified database node console connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONSOLE_HISTORY Function

Updates the specified database node console history.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`console_history_id`

(required) The OCID of the console history.

`update_console_history_details`

(required) Request to update the specified database node console history.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_GUARD_ASSOCIATION Function

Updates the Data Guard association the specified database. This API can be used to change the `protectionMode` and `transportType` of the Data Guard association.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`data_guard_association_id`

(required) The Data Guard association's[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_data_guard_association_details`

(required) A request to update Data Guard association of a database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE Function

Update the specified database based on the request parameters provided.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_database_details`

(required) Request to perform database update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_SOFTWARE_IMAGE Function

Updates the properties of a Database Software Image, like Display Nmae

Syntax
```

```

Parameters

Parameter Description

`database_software_image_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_database_software_image_details`

(required) Request to update the properties of a DB system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DB_HOME Function

Patches the specified Database Home.

Syntax
```

```

Parameters

Parameter Description

`db_home_id`

(required) The Database Home[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_db_home_details`

(required) Request to update the properties of a Database Home.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DB_NODE Function

Updates the specified database node.

Syntax
```

```

Parameters

Parameter Description

`db_node_id`

(required) The database node[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_db_node_details`

(required) Request to update the specified database node.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DB_SYSTEM Function

Updates the properties of the specified DB system. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_db_system_details`

(required) Request to update the properties of a DB system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXADATA_INFRASTRUCTURE Function

Updates the Exadata infrastructure resource. Applies to Exadata Cloud@Customer instances only. To update an Exadata Cloud Service infrastructure resource, use the`UPDATE_CLOUD_EXADATA_INFRASTRUCTURE`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_exadata_infrastructure_details`

(required) Request to update the properties of an Exadata Cloud@Customer infrastructure.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXADATA_IORM_CONFIG Function

Updates IORM settings for the specified Exadata DB system. **Note:** Deprecated for Exadata Cloud Service systems. Use the[new resource model APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model)instead. For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See[Switching an Exadata DB System to the New Resource Model and APIs](https://docs.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm)for details on converting existing Exadata DB systems to the new resource model. The`UPDATE_CLOUD_VM_CLUSTER_IORM_CONFIG`Function API is used for Exadata systems using the new resource model.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`exadata_iorm_config_update_details`

(required) Request to perform database update.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_CONTAINER_DATABASE Function

Updates the properties of an`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function resource, such as the display name.

Syntax
```

```

Parameters

Parameter Description

`external_container_database_id`

(required) The ExternalContainerDatabase[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_external_container_database_details`

(required) Request to update the properties of an`CREATE_EXTERNAL_CONTAINER_DATABASE_DETAILS`Function resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_DATABASE_CONNECTOR Function

Updates the properties of an external database connector, such as the display name.

Syntax
```

```

Parameters

Parameter Description

`external_database_connector_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the external database connector resource (`ExternalDatabaseConnectorId`).

`update_external_database_connector_details`

(required) Request to update the properties of an external database connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_NON_CONTAINER_DATABASE Function

Updates the properties of an external non-container database, such as the display name.

Syntax
```

```

Parameters

Parameter Description

`external_non_container_database_id`

(required) The external non-container database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_external_non_container_database_details`

(required) Request to update the properties of an external non-container database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_EXTERNAL_PLUGGABLE_DATABASE Function

Updates the properties of an`CREATE_EXTERNAL_PLUGGABLE_DATABASE_DETAILS`Function resource, such as the display name.

Syntax
```

```

Parameters

Parameter Description

`external_pluggable_database_id`

(required) The ExternalPluggableDatabaseId[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_external_pluggable_database_details`

(required) Request to update the properties of an external pluggable database resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_KEY_STORE Function

If no database is associated with the key store, edit the key store.

Syntax
```

```

Parameters

Parameter Description

`key_store_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the key store.

`update_key_store_details`

(required) Request to update the attributes of a key store.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MAINTENANCE_RUN Function

Updates the properties of a maintenance run, such as the state of a maintenance run.

Syntax
```

```

Parameters

Parameter Description

`maintenance_run_id`

(required) The maintenance run OCID.

`update_maintenance_run_details`

(required) Request to update the properties of a maintenance run.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ONEOFF_PATCH Function

Updates the properties of the specified one-off patch.

Syntax
```

```

Parameters

Parameter Description

`oneoff_patch_id`

(required) The one-off patch[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_oneoff_patch_details`

(required) Request to update the properties of a one-off patch.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PLUGGABLE_DATABASE Function

Updates the specified pluggable database.

Syntax
```

```

Parameters

Parameter Description

`pluggable_database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_pluggable_database_details`

(required) Request to perform pluggable database update.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VM_CLUSTER Function

Updates the specified VM cluster. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`vm_cluster_id`

(required) The VM cluster[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_vm_cluster_details`

(required) Request to update the attributes of a VM cluster.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_VM_CLUSTER_NETWORK Function

Updates the specified VM cluster network. Applies to Exadata Cloud@Customer instances only. To update a cloud VM cluster in an Exadata Cloud Service instance, use the`UPDATE_CLOUD_VM_CLUSTER`Function operation.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`update_vm_cluster_network_details`

(required) Request to update the properties of a VM cluster network.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPGRADE_DATABASE Function

Upgrades the specified Oracle Database instance.

Syntax
```

```

Parameters

Parameter Description

`database_id`

(required) The database[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`upgrade_database_details`

(required) Request to perform a database upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPGRADE_DB_SYSTEM Function

Upgrades the operating system and grid infrastructure of the DB system.

Syntax
```

```

Parameters

Parameter Description

`db_system_id`

(required) The DB system[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`upgrade_db_system_details`

(required) Request to perform an upgrade of the operating system and the Oracle Grid Infrastructure (GI) of the DB system.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_VM_CLUSTER_NETWORK Function

Validates the specified VM cluster network. Applies to Exadata Cloud@Customer instances only.

Syntax
```

```

Parameters

Parameter Description

`exadata_infrastructure_id`

(required) The Exadata infrastructure[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`vm_cluster_network_id`

(required) The VM cluster network[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://database.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Database Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-826727FE-DB27-416C-B7AA-97FCE7ADDECF)
- [ACTIVATE_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D4703D47-2EB0-4EB1-8308-F5EB55AE40AE)
- [ADD_STORAGE_CAPACITY_CLOUD_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9021B1C2-6247-4985-8374-5BDAB0E88FF5)
- [ADD_STORAGE_CAPACITY_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DECD772D-FEBA-4FDD-AAAA-2D9B58F0F1B4)
- [ADD_VIRTUAL_MACHINE_TO_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-49AAE9DC-E674-4C99-81E4-43F11ED8B433)
- [ADD_VIRTUAL_MACHINE_TO_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7CCC14D3-1721-47EB-A0C5-378E19A7EEA7)
- [AUTONOMOUS_DATABASE_MANUAL_REFRESH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9DA5EAC2-114F-4161-81C3-B0BBB8968C70)
- [CANCEL_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B90DCE32-08E9-49A4-8F31-84CCF5331686)
- [CHANGE_AUTONOMOUS_CONTAINER_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-CB1186EC-C963-4F14-A10A-B93EC62D326D)
- [CHANGE_AUTONOMOUS_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DEEB67B7-F786-4B86-8620-10D902DA2A0D)
- [CHANGE_AUTONOMOUS_EXADATA_INFRASTRUCTURE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C37F323B-DA1C-48F1-98DF-43E18F8D64C1)
- [CHANGE_AUTONOMOUS_VM_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-773F2DAE-E49B-4C1D-9972-9C8607D6EDAA)
- [CHANGE_BACKUP_DESTINATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D44AED44-C101-4145-96A4-C6379B0D84A6)
- [CHANGE_CLOUD_AUTONOMOUS_VM_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-612059A9-D0F0-4602-B959-A29F98E0B4E9)
- [CHANGE_CLOUD_EXADATA_INFRASTRUCTURE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-259D2913-726B-439D-B7E7-6CD91E1C2C5F)
- [CHANGE_CLOUD_VM_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A99329EE-9DF9-4DF7-95D7-A0BEE9398768)
- [CHANGE_DATABASE_SOFTWARE_IMAGE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-972F8665-E591-44DA-B402-DC169E365FAB)
- [CHANGE_DATAGUARD_ROLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2F54989B-AACD-4FE6-9E4C-617813F35440)
- [CHANGE_DB_SYSTEM_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C0960342-3845-4DCB-AE6A-5E4E971C456B)
- [CHANGE_DISASTER_RECOVERY_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-93781C62-D616-4A79-AAD3-17D47C941FC6)
- [CHANGE_EXADATA_INFRASTRUCTURE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-80377B13-F33B-4835-A0C4-AD6D2F08A3A0)
- [CHANGE_EXTERNAL_CONTAINER_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-487E5674-F750-4DD3-939E-780D5569F8E1)
- [CHANGE_EXTERNAL_NON_CONTAINER_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8A9A3B2A-B39B-4062-8DA5-664FDD8438D4)
- [CHANGE_EXTERNAL_PLUGGABLE_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0C2D8C67-BA1E-45F1-810C-D86BFE7AE1BC)
- [CHANGE_KEY_STORE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-91F5832F-2432-44D3-8DC7-AED1E6C8B14E)
- [CHANGE_KEY_STORE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2F136BB3-C965-4754-A400-A39B33B9DA72)
- [CHANGE_ONEOFF_PATCH_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-67950836-659B-4964-9C40-8515A3375199)
- [CHANGE_VM_CLUSTER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8F272B17-9538-4E3C-A740-2D36C7F89925)
- [CHECK_EXTERNAL_DATABASE_CONNECTOR_CONNECTION_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AC1BBA16-ABA9-454F-B095-F4E20B5D2A54)
- [COMPLETE_EXTERNAL_BACKUP_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-462F4C00-2385-4D95-B2C8-78122AEFD4F0)
- [CONFIGURE_AUTONOMOUS_DATABASE_VAULT_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A176311A-8E05-4674-83B8-DF7A392387DD)
- [CONFIGURE_SAAS_ADMIN_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-957834FC-6160-49EE-8C3F-58659280DD88)
- [CONVERT_TO_PDB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-22340B34-C5B2-447B-B4C5-957C60907B9F)
- [CONVERT_TO_REGULAR_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A13ADF48-7174-4B0C-8642-FC7C88D3803F)
- [CREATE_APPLICATION_VIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F2EE1D89-AD57-4DAD-93A4-A15975C0E3C7)
- [CREATE_AUTONOMOUS_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-99908260-AE31-4613-8091-F465F2E7BC3F)
- [CREATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3050A121-4357-4787-84C2-70014DD4D021)
- [CREATE_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-963053EE-578F-4A12-9031-EE235843207B)
- [CREATE_AUTONOMOUS_DATABASE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2F2D97EC-B436-4890-8222-9522AC7BB608)
- [CREATE_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D9EE8986-3719-4213-9E8A-F49F3121E570)
- [CREATE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2EF15884-799B-4E5B-880F-92DCD7437BB5)
- [CREATE_BACKUP_DESTINATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-44142859-3546-4587-BDFE-E48ED5F07612)
- [CREATE_CLOUD_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A2BE3BB3-18B3-4133-B015-450D4F8D4A76)
- [CREATE_CLOUD_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-160CE3E9-7D2B-4590-BA2D-06E1C286B471)
- [CREATE_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DD11DC4A-763F-4835-950B-47D3DE1071E9)
- [CREATE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-FB1890DB-8B18-443D-B214-C765C6C57702)
- [CREATE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B4B6312D-3344-4977-A2BD-F5C9BF6848A3)
- [CREATE_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-12663092-D41D-4A55-9388-57A37FA9B8DB)
- [CREATE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E1204BAD-527D-4417-8E76-F494FD6F78C5)
- [CREATE_DATABASE_SOFTWARE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F4F3737C-8A18-4DDD-97FC-C1A8450A024E)
- [CREATE_DB_HOME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0F83A165-6579-42E5-90F3-CC08AB1FEC46)
- [CREATE_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6A47DF4E-F92F-472E-9F1F-30B0B7E440C4)
- [CREATE_EXTERNAL_BACKUP_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5FA67524-B44D-41F9-817F-ED2223C526F2)
- [CREATE_EXTERNAL_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D779146D-A39E-4DF4-889F-F09ABBB33E90)
- [CREATE_EXTERNAL_DATABASE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2B8090DC-35AC-4AD1-B239-ACBC444BE9C2)
- [CREATE_EXTERNAL_NON_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6C918111-183B-47C1-8BA3-1BC33C812CD4)
- [CREATE_EXTERNAL_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-001F1914-A7E8-4275-B249-7D681E3D8D7F)
- [CREATE_KEY_STORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2F8468AC-0C88-44F3-93EB-4C964FF694EB)
- [CREATE_MAINTENANCE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3ADD1E3E-EC2B-46DA-A8B9-626BA0D62CD2)
- [CREATE_ONEOFF_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9B07F94C-93A3-4E13-930A-CF0C39497793)
- [CREATE_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3D451232-A996-4EE2-9C0C-8E7369C80364)
- [CREATE_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BEE66A11-D0A3-4129-BFE8-9E837EDE0EC6)
- [CREATE_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-855FDC72-E8FF-448D-8409-9D01ABFEA0F3)
- [DB_NODE_ACTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-40817AD7-44B6-46AA-BBF0-368EC8055C38)
- [DELETE_APPLICATION_VIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A63433FE-EE69-4943-A1B1-665621C11A44)
- [DELETE_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5C2F1317-4841-4C2C-9DC0-B18B222F58DD)
- [DELETE_AUTONOMOUS_DATABASE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4FEFCA8A-FCCB-444E-A17F-C52B4C7D7B0E)
- [DELETE_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-24113405-20CD-4878-9853-18BDF536F389)
- [DELETE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C730FD4D-8D48-40B0-A345-5B84F3C438D9)
- [DELETE_BACKUP_DESTINATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9B3FF680-8413-4CFE-BDA9-2BDBB045F6B1)
- [DELETE_CLOUD_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3BA25AC0-C51F-402C-A76D-782C4C218D22)
- [DELETE_CLOUD_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5F7CF2DE-9401-4752-8D34-31A6DB1AEEB2)
- [DELETE_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-37298271-76C6-4D8B-A5C3-F12FDC8869D0)
- [DELETE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D5256EB3-A18B-4945-8918-813634DA2248)
- [DELETE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3F26C072-77C6-4154-97F0-97542BBA54DA)
- [DELETE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4C02F14D-B57B-42BE-8E31-F3116B79BDC4)
- [DELETE_DATABASE_SOFTWARE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F0D409A9-765B-4C2B-BBA2-FD1C1746445C)
- [DELETE_DB_HOME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9E873FB1-79E7-416E-9BFD-2AE6D98448DA)
- [DELETE_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-748831DF-EA1B-4823-B05C-AA8A020F2741)
- [DELETE_EXTERNAL_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8CB8C904-81EC-45F3-9BDA-A90EC1728B42)
- [DELETE_EXTERNAL_DATABASE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C6E46A31-29CA-451D-B001-D0282D7798FE)
- [DELETE_EXTERNAL_NON_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-079C73D3-17E6-40E1-BA57-CD3B45DEB32D)
- [DELETE_EXTERNAL_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8C86FBE5-DEC6-4554-87F5-4C4172870334)
- [DELETE_KEY_STORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6249C412-F1D7-4FE5-8E9D-44CCDC5A9D6D)
- [DELETE_ONEOFF_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7F5B116A-2369-4CF8-A344-A2D0FB81262C)
- [DELETE_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-82259AE5-5A5B-4478-BAD1-FAFA87F31700)
- [DELETE_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-171B31B2-936A-41E1-9ADE-B537CE1BD62F)
- [DELETE_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D9499241-A615-4B3A-88E8-5C2E08610D63)
- [DEREGISTER_AUTONOMOUS_DATABASE_DATA_SAFE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E966316B-CFC2-4D40-83FD-7A0B3FCA7F27)
- [DISABLE_AUTONOMOUS_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F904C276-A388-41BE-B28C-3E8B5BA060C3)
- [DISABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-62891F69-C784-49CD-9768-2F20105B2DBB)
- [DISABLE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1F75189C-7C6D-4938-A2FF-33295E4A24A0)
- [DISABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C51C99B1-2025-45B1-8E7B-A365322FBE4A)
- [DISABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-629EE5ED-AF7C-4551-96DF-6122AC34F3D0)
- [DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A55ED779-BFF0-401A-B7B2-E0BEFC5A089C)
- [DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B5D1606C-F87F-4CF8-9C66-911B2F02AD68)
- [DISABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E8D757C1-F9C2-4533-9284-61DC501E316B)
- [DISABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BE96B969-3228-4090-9E65-2DFD6C9A3DC9)
- [DISABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E4537D0B-F07F-4F45-9C6D-7AFFCA7553E8)
- [DISABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-92B72EE4-676A-4D97-8494-6243BA012EFB)
- [DISABLE_PLUGGABLE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3EFFC138-6AB9-4CD7-AF9B-89C8C14FE74B)
- [DOWNLOAD_EXADATA_INFRASTRUCTURE_CONFIG_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0EAE1299-386C-4081-AEE4-02FAB1C6A4B8)
- [DOWNLOAD_ONEOFF_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-CC413E0A-4DCD-4E80-A334-D07FDDCAF7D1)
- [DOWNLOAD_VALIDATION_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4FB3DEF2-A08D-4C34-80FA-E3F6F18B085D)
- [DOWNLOAD_VM_CLUSTER_NETWORK_CONFIG_FILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-97C79370-E80C-413C-A57C-49B28F5CD907)
- [ENABLE_AUTONOMOUS_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1334AECC-AF43-4E3C-9D19-627B7B779175)
- [ENABLE_AUTONOMOUS_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DFF3902E-C867-431C-B8DC-C2552B54B098)
- [ENABLE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9190B289-5878-451F-B1C2-69DEAEC5D38C)
- [ENABLE_EXTERNAL_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-58FDDF05-6CBF-481B-9CAF-F868FC461942)
- [ENABLE_EXTERNAL_CONTAINER_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1969062B-DB1A-42E7-8D69-5FA87B9B6D0B)
- [ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3424DAA5-9F40-4C01-8769-DFAB21F12311)
- [ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-88A9523B-C65E-46E4-920C-E1E82320D5D4)
- [ENABLE_EXTERNAL_NON_CONTAINER_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-214FD15E-87C1-4AB9-80FE-3206CE46D457)
- [ENABLE_EXTERNAL_PLUGGABLE_DATABASE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7D40AE5A-BA2E-42A3-8C6C-9429577870C8)
- [ENABLE_EXTERNAL_PLUGGABLE_DATABASE_OPERATIONS_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DCD4ED74-07AD-4244-B5E3-B9EA6EFE3A9F)
- [ENABLE_EXTERNAL_PLUGGABLE_DATABASE_STACK_MONITORING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4CD1A995-09FC-487E-8FCD-1F4A8ED116D9)
- [ENABLE_PLUGGABLE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6F15EB0B-9A58-44A8-BCD5-F821E5F44536)
- [FAIL_OVER_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-57E5F661-8991-4F23-BC65-0FF3319BA4AC)
- [FAILOVER_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D16076DD-58D1-4E08-9B7B-5420BF540C8C)
- [FAILOVER_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7C373DA7-2A95-4372-8341-C78625C50DDB)
- [GENERATE_AUTONOMOUS_DATABASE_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-78931020-927F-4FDD-B16F-6DB5E0BF660F)
- [GENERATE_RECOMMENDED_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8CB2D16F-073F-4814-A977-85AF796B1A9E)
- [GET_APPLICATION_VIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A288108B-D40B-4B81-AAE2-21595DC54038)
- [GET_AUTONOMOUS_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9C537E5F-08A0-40F4-B370-FC4304348409)
- [GET_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E690349C-CBC4-4321-A99F-1AC09D2DF517)
- [GET_AUTONOMOUS_CONTAINER_DATABASE_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9315B77C-E982-4AB5-9DB0-EFD759702F19)
- [GET_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-647475AE-54A8-4C3E-94D5-D490FF4EBD80)
- [GET_AUTONOMOUS_DATABASE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4C33F677-45F1-4AE2-9291-B325B75B5939)
- [GET_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E5159F80-F74B-40BE-BF59-5636970376B5)
- [GET_AUTONOMOUS_DATABASE_REGIONAL_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DC7F6A60-DCBA-4802-B4A0-15035241C5D0)
- [GET_AUTONOMOUS_DATABASE_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BDDCEBB9-CC83-446B-8C0D-F254B8CD729F)
- [GET_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-81729D50-201A-4894-A5DF-88F4EEC0BEF0)
- [GET_AUTONOMOUS_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E69D7B19-A4B1-4B96-A1F0-39BADB354CD9)
- [GET_AUTONOMOUS_VIRTUAL_MACHINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B1C99F57-097E-4ED8-BA5C-5728B139FE6C)
- [GET_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F7831740-EA64-4C35-A454-9D5FEDAFB205)
- [GET_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-56B63831-033E-458E-9DC8-1382DD26BC93)
- [GET_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-37756ACA-0B70-457C-B9F0-685A6E4F3C85)
- [GET_BACKUP_DESTINATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-861F68B1-8BAF-49D1-8F27-ABF8BB9C3162)
- [GET_CLOUD_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BB18EF35-C26B-4B51-8C11-354003036404)
- [GET_CLOUD_AUTONOMOUS_VM_CLUSTER_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BBE4CD86-072D-49C7-A1C1-3BBA64736F3D)
- [GET_CLOUD_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DB3CC9FD-C7E4-47C1-839C-456C70748E82)
- [GET_CLOUD_EXADATA_INFRASTRUCTURE_UNALLOCATED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-19330169-1BE8-4468-A0C8-D78D3734B08E)
- [GET_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F114DF5B-12FC-4D31-B340-B55C7852073D)
- [GET_CLOUD_VM_CLUSTER_IORM_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-10427C17-0262-4001-8501-3B128708EE53)
- [GET_CLOUD_VM_CLUSTER_UPDATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-007D9925-BC24-416F-B3FE-EC6C5A42D902)
- [GET_CLOUD_VM_CLUSTER_UPDATE_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2761FF9C-020F-4596-9F0B-F1086A6FD756)
- [GET_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F2207827-900B-408D-85CC-E4157BED7195)
- [GET_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-13099410-C199-4175-AE26-36FFAFA87ECD)
- [GET_CONSOLE_HISTORY_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4C478B03-D696-4994-9DC9-2BE23D63B551)
- [GET_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8B785A47-1102-4B08-80E8-9652956B7010)
- [GET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F15CBA6D-D978-4968-A53A-F27EE2B24B05)
- [GET_DATABASE_SOFTWARE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B5D64688-0CA2-4026-8D61-1B4D62750B90)
- [GET_DATABASE_UPGRADE_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-07799120-BD54-49C0-BC39-D942E25C8845)
- [GET_DB_HOME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E3C98101-82B7-41AD-AC79-031CD350F4AE)
- [GET_DB_HOME_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8BC49873-146B-4184-A17D-7E3B18EB4456)
- [GET_DB_HOME_PATCH_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AC0F942A-EFB5-4343-819F-3BAF1A9E2616)
- [GET_DB_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A474F519-8553-41F7-A2B3-6A848688600D)
- [GET_DB_SERVER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E11F1205-E6ED-49BD-9F5C-2D01A4F567A5)
- [GET_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4FF7BDDD-EF0B-4335-813E-890A231AEB05)
- [GET_DB_SYSTEM_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7E739BC4-77D1-417D-98DD-834526CA6429)
- [GET_DB_SYSTEM_PATCH_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F5F4713D-27FA-4813-877C-6C4D59C7D877)
- [GET_DB_SYSTEM_UPGRADE_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B868467D-ECC8-43A8-A074-9382AE9C7DAF)
- [GET_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-195BC7A7-4079-4508-A14C-EDCC1EBB19BE)
- [GET_EXADATA_INFRASTRUCTURE_OCPUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E21B4E54-586C-490C-9387-CCFD14457388)
- [GET_EXADATA_INFRASTRUCTURE_UN_ALLOCATED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A6D3204A-138D-42A8-A94F-C249616C25EB)
- [GET_EXADATA_IORM_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BDC0BA5D-80F5-4276-8E8C-419898255503)
- [GET_EXTERNAL_BACKUP_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-49CFFEB2-BB2A-4E33-8598-382D6E82A23C)
- [GET_EXTERNAL_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-CED958D7-5052-4084-BA7E-B367F8313C61)
- [GET_EXTERNAL_DATABASE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-520046A7-408C-4CF3-BC8B-440D4DB8FCD7)
- [GET_EXTERNAL_NON_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-142B71BE-E3A0-4E04-912E-0DFF7D711072)
- [GET_EXTERNAL_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-989C3BDE-D5FE-43A4-9CF7-30D77B3A4A91)
- [GET_INFRASTRUCTURE_TARGET_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A68A6E6A-4B4A-4C7A-BDAC-3EE7466AC08F)
- [GET_KEY_STORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0B6564CA-C885-4ADA-886C-262D0E3D61F7)
- [GET_MAINTENANCE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-922A21C7-5DDE-4625-804C-5CCB7DA78CE8)
- [GET_MAINTENANCE_RUN_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3259C1F3-6DFF-47F8-8AFB-03B4D13DCE57)
- [GET_ONEOFF_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7103FC87-42AC-4262-AF75-6352E6035381)
- [GET_PDB_CONVERSION_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A3E18784-0D17-4E8C-8013-8F20B2556939)
- [GET_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-ECB94276-A2B4-45F8-92E9-1EEE8D35555D)
- [GET_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C695CB9C-0BCE-48C0-8B2D-E1E15DD6212A)
- [GET_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5DEEC226-E398-4722-9F44-21AF75C02556)
- [GET_VM_CLUSTER_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3102F22F-EB17-4107-992F-3968CE443B3D)
- [GET_VM_CLUSTER_PATCH_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-475DB9E7-18F6-4E7B-A919-378FC4E1D9E3)
- [GET_VM_CLUSTER_UPDATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2FCDD1E8-95EB-463E-8B46-B688DAA5B86A)
- [GET_VM_CLUSTER_UPDATE_HISTORY_ENTRY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A2F773B4-F252-4F7A-8DFF-1A2660EDAFB1)
- [LAUNCH_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-84DB5193-6216-49BD-9D4F-67469932010D)
- [LAUNCH_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7CC402E6-8190-4EE6-9174-BC9EA40CFFF3)
- [LIST_APPLICATION_VIPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-EE84D566-06A9-4AAB-9232-C0AE0889D5FC)
- [LIST_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-829B0110-1682-4F5B-961B-712F0E824049)
- [LIST_AUTONOMOUS_CONTAINER_DATABASE_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F9421B9B-F97B-4BA9-B461-73CF21A6B566)
- [LIST_AUTONOMOUS_CONTAINER_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6588C3BB-D00C-42EC-A8A4-DB8C831F4AAF)
- [LIST_AUTONOMOUS_DATABASE_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0F1025D1-3107-4A85-81A8-71A402427297)
- [LIST_AUTONOMOUS_DATABASE_CHARACTER_SETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1790F9B1-89EA-45F7-A89B-30296E56E3DC)
- [LIST_AUTONOMOUS_DATABASE_CLONES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A1D9BCA8-0F42-48AA-8E09-102D8AA4A39B)
- [LIST_AUTONOMOUS_DATABASE_DATAGUARD_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E89847F2-778A-4E85-9B85-7C1076091244)
- [LIST_AUTONOMOUS_DATABASE_REFRESHABLE_CLONES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-924DE13C-952B-4E05-A94F-1311DD4B0F9F)
- [LIST_AUTONOMOUS_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3377FF8C-3291-4409-A989-595D3CF39AED)
- [LIST_AUTONOMOUS_DB_PREVIEW_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7049EEBA-8EDC-4C32-A0FD-09FB277E4CDE)
- [LIST_AUTONOMOUS_DB_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F6C01DC6-2849-47BE-A0BA-778743E75982)
- [LIST_AUTONOMOUS_EXADATA_INFRASTRUCTURE_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7ED14049-19C5-4D8B-A370-AD873E14BA8B)
- [LIST_AUTONOMOUS_EXADATA_INFRASTRUCTURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AB7CCB8E-6CE5-4D14-A934-A3DFA66F7C3D)
- [LIST_AUTONOMOUS_VIRTUAL_MACHINES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-CA3CC16F-135B-49AE-A565-6BFC1BAFFCCD)
- [LIST_AUTONOMOUS_VM_CLUSTER_ACD_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D865837B-C85F-4151-825D-83E923040407)
- [LIST_AUTONOMOUS_VM_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4FCB47F9-C6E8-4BBD-B537-EF848D254930)
- [LIST_BACKUP_DESTINATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-956B2F89-7843-4513-BBD7-2F9E8163DA16)
- [LIST_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4D1A5598-35A7-4EDE-BCBF-ABEC95D13DD9)
- [LIST_CLOUD_AUTONOMOUS_VM_CLUSTER_ACD_RESOURCE_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BA28A8E2-6A8D-4750-82F8-A12A24F7CD0E)
- [LIST_CLOUD_AUTONOMOUS_VM_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8BC886C9-9146-4D29-9556-FB14861195B4)
- [LIST_CLOUD_EXADATA_INFRASTRUCTURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D459AD7D-F453-41DD-8AD4-A51A41DBD351)
- [LIST_CLOUD_VM_CLUSTER_UPDATE_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E782ED94-833C-4D14-B280-4A4592CA63E8)
- [LIST_CLOUD_VM_CLUSTER_UPDATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-15610E4F-A7A2-4169-B775-B534DE9F318A)
- [LIST_CLOUD_VM_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9FD4CE8F-EC34-4077-91EC-113E7C2D5E44)
- [LIST_CONSOLE_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F5FEEED5-4F90-4A92-9A11-AF8901E22785)
- [LIST_CONSOLE_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-FB06104F-76E7-4123-879D-2169C9DD9F65)
- [LIST_CONTAINER_DATABASE_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7CE61571-9E01-41E0-984F-9C6B59041D54)
- [LIST_DATA_GUARD_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E71BDC2B-F596-4AAE-A9FA-3D43658DF650)
- [LIST_DATABASE_SOFTWARE_IMAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D7A81A8F-1E05-4632-80C8-EA5994A38266)
- [LIST_DATABASE_UPGRADE_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DC27E53A-EAB8-43B0-92F1-AEF2AF0F2BBF)
- [LIST_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-464457AC-C25B-46DD-BD11-89FBF580261D)
- [LIST_DB_HOME_PATCH_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-52383396-96EE-4146-988D-CE29DE566DC1)
- [LIST_DB_HOME_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-81BBCADF-A002-4343-AC9B-C37EC809E295)
- [LIST_DB_HOMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-352CD4EB-0BFA-41BA-A447-EB022E9FE485)
- [LIST_DB_NODES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AAB7BD2C-B7FC-421E-95DF-3E425AF2B1C9)
- [LIST_DB_SERVERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0AB57408-7ECC-4620-9CBD-A156D6AD6B47)
- [LIST_DB_SYSTEM_COMPUTE_PERFORMANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F06777F7-BD24-4A2C-9BDC-A0C69AD9EF6A)
- [LIST_DB_SYSTEM_PATCH_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-293BFE8A-14CF-4DC7-A17C-82F8582DB524)
- [LIST_DB_SYSTEM_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-328C6E87-8BAE-4D3F-A6E5-58176F30D1C1)
- [LIST_DB_SYSTEM_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-090C1342-7B8C-4947-8B98-B0E3BF7C8273)
- [LIST_DB_SYSTEM_STORAGE_PERFORMANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-71347B9B-E578-4B1B-96C7-5EC192A8C4FC)
- [LIST_DB_SYSTEM_UPGRADE_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-176C0175-DF4B-4C61-B2CB-256E2A320571)
- [LIST_DB_SYSTEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-45130998-4CA1-4640-A027-DB3BE2BEE9D2)
- [LIST_DB_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2B5737A9-A68B-4204-876A-57345082D5DB)
- [LIST_EXADATA_INFRASTRUCTURES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-EDB77458-A722-4683-8280-E25A894B7268)
- [LIST_EXTERNAL_CONTAINER_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BE04AF7C-A5DC-4A6B-8F75-BF7D8CDEF039)
- [LIST_EXTERNAL_DATABASE_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7FC97449-66B4-4A14-A869-CBA860610BCD)
- [LIST_EXTERNAL_NON_CONTAINER_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5DD218A3-BB46-414B-8E3A-4D91E83770DA)
- [LIST_EXTERNAL_PLUGGABLE_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-4E552233-9ABA-46E9-AB2C-744D8AC0D4AB)
- [LIST_FLEX_COMPONENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1606ED8D-C225-4C23-935F-8FAFB62491B9)
- [LIST_GI_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D306472C-FAF9-401B-BCBF-E86B0E7758FA)
- [LIST_KEY_STORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C7308805-491B-4109-9402-5AEA730E0895)
- [LIST_MAINTENANCE_RUN_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AABDE61A-B5FB-4E77-9D9D-0A64C15945CB)
- [LIST_MAINTENANCE_RUNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D8D2795F-8F29-413C-A5C7-0DE20E062663)
- [LIST_ONEOFF_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D1122E31-B0C3-4981-8260-A45954E13AD7)
- [LIST_PDB_CONVERSION_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B2F69235-73EC-4E05-A37A-CB1F295FECF3)
- [LIST_PLUGGABLE_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-23204D0E-4133-419F-B587-3BA07EB713E8)
- [LIST_SYSTEM_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F15BD32F-C635-4081-A0C1-FFF9B901C58B)
- [LIST_VM_CLUSTER_NETWORKS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5D02C147-F9DE-4905-8E2D-B9955FE48ED8)
- [LIST_VM_CLUSTER_PATCH_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-39397BEF-CB12-45DF-8A9F-1B3FBB38208F)
- [LIST_VM_CLUSTER_PATCHES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-055C0ED0-EAD0-49C1-BA7A-4782DA47DE04)
- [LIST_VM_CLUSTER_UPDATE_HISTORY_ENTRIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A5C8B2AE-EAC0-4510-8CEF-B150721C5F41)
- [LIST_VM_CLUSTER_UPDATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-935C5BF9-324D-4290-90D4-0E596BA7B634)
- [LIST_VM_CLUSTERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A74C84FB-B567-41BD-9457-2B79416419EF)
- [LOCAL_CLONE_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-43418EF5-23BC-40CB-9828-5A80FC4C9FE4)
- [MIGRATE_EXADATA_DB_SYSTEM_RESOURCE_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D8356EDE-490F-42F5-A8A8-2E24F5D47D4A)
- [MIGRATE_VAULT_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-077FA799-B521-4B1C-9CEB-C9E00EDB97D9)
- [MODIFY_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9C0A67EB-8A08-4197-888D-27776D92498F)
- [MODIFY_PLUGGABLE_DATABASE_MANAGEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A412BC71-FD68-4FD8-B259-E66A9E70CDE2)
- [REFRESH_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-38F1C1DE-86C4-41A1-8A4F-B5389F037F68)
- [REGISTER_AUTONOMOUS_DATABASE_DATA_SAFE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-BAC681D3-CF94-42CF-B7DC-4818C9F55F11)
- [REINSTATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7E21EC43-F68A-477D-82B2-703959F58118)
- [REINSTATE_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B001FC10-263C-4B1D-A531-D97A1E934DD4)
- [REMOTE_CLONE_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6E12ABEA-C20F-4A61-AE4F-A7076D3373A4)
- [REMOVE_VIRTUAL_MACHINE_FROM_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D5BF049C-0B52-4A37-9C9F-B95389C6DE5F)
- [REMOVE_VIRTUAL_MACHINE_FROM_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-71CF15B8-F72E-44C5-A9BC-A69D4DA2F42F)
- [RESIZE_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D6F532D9-B4A2-45CC-8AA7-F1E5281B2CBD)
- [RESOURCE_POOL_SHAPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E7E4367D-8FFA-45F1-B2DE-D482111A402B)
- [RESTART_AUTONOMOUS_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-732AA2E8-40FA-4CE1-8D36-A769C9082EBC)
- [RESTART_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-1C55CC90-3D44-4929-92EE-7935B9CF9942)
- [RESTORE_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-56D9ED90-59F0-4093-86F4-68FDC3DDBBA6)
- [RESTORE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-934B20A5-C363-42D4-8BE7-BE29AC178F00)
- [ROTATE_AUTONOMOUS_CONTAINER_DATABASE_ENCRYPTION_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-ADD4605F-CD87-444C-BDC8-33A167C868E3)
- [ROTATE_AUTONOMOUS_DATABASE_ENCRYPTION_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-9C735E0E-1BF1-48D1-B367-C124C8B74016)
- [ROTATE_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-EBED616E-2988-4759-878A-755C981F9F45)
- [ROTATE_AUTONOMOUS_VM_CLUSTER_SSL_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3472D45C-D268-46E4-8744-AED632FB65F0)
- [ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_ORDS_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-0A3EC212-BC2E-48C3-B896-541458283B14)
- [ROTATE_CLOUD_AUTONOMOUS_VM_CLUSTER_SSL_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-380A207A-351C-4FEE-A3DA-58939A029A2E)
- [ROTATE_ORDS_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-119048A6-5745-4DAB-9421-4CEEA1E3D1A1)
- [ROTATE_PLUGGABLE_DATABASE_ENCRYPTION_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-642C3A5E-71C8-4267-9DBB-6284D0958B69)
- [ROTATE_SSL_CERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DD1FCF60-BA0F-44F0-AB38-B0410B906A2A)
- [ROTATE_VAULT_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-50626DE3-BC89-4644-915C-B0256F558A04)
- [SAAS_ADMIN_USER_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3A55CF5A-9DE2-46C8-B5B5-20A6DD45729A)
- [SCAN_EXTERNAL_CONTAINER_DATABASE_PLUGGABLE_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A154A89D-ADA1-4D0E-8D23-8C7784834E5A)
- [SHRINK_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7E921CB7-4140-4BBD-937A-1A8B9C187479)
- [START_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B21BCBDB-E33D-48F6-805A-ECFD8FF75107)
- [START_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-81771EC2-CF57-432F-A7A7-E280FBCF0264)
- [STOP_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D157156C-75E4-4654-8610-965A4A20ED42)
- [STOP_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-05F8DAEB-3B1E-40A6-BD3E-10EE73DC9D54)
- [SWITCHOVER_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-2D191335-B631-48CC-91A1-E7D4E70E0B7E)
- [SWITCHOVER_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-CA39DE74-BB09-4B6D-95FB-CB04356A8E06)
- [SWITCHOVER_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-733DBA67-081A-41B1-BE0F-99F4A480B134)
- [TERMINATE_AUTONOMOUS_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F51CFA64-ABFE-4E33-A06D-D0AF94232C80)
- [TERMINATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-8CCB7714-0C43-468E-A902-6B9B58E1F1C3)
- [TERMINATE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6AFD8A96-4FA0-4CC4-865C-07A3E776D0AC)
- [UPDATE_AUTONOMOUS_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7DF669D1-A883-46F1-90B8-DB850A2390F6)
- [UPDATE_AUTONOMOUS_CONTAINER_DATABASE_DATAGUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-44F0171E-2A02-4DD9-B48C-DC03A6A40496)
- [UPDATE_AUTONOMOUS_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-E63BC9B6-72BE-4821-968B-EE64BE0FB271)
- [UPDATE_AUTONOMOUS_DATABASE_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B5DDBBCE-ABCF-4462-A0F9-2A852DBF6E19)
- [UPDATE_AUTONOMOUS_DATABASE_REGIONAL_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-08840DCD-4F01-4F08-9849-1D7A22DFF38B)
- [UPDATE_AUTONOMOUS_DATABASE_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-30ABADAA-2B74-48F4-861C-EE9595FEE8FF)
- [UPDATE_AUTONOMOUS_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-C3423BDB-2F33-48F7-941A-9765914EBA6A)
- [UPDATE_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-5C69A0D6-B029-4E2E-837B-8A6E6A20C5B6)
- [UPDATE_BACKUP_DESTINATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-51FB4228-C92C-4406-84D3-F15255719885)
- [UPDATE_CLOUD_AUTONOMOUS_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-532CEE2A-04DA-4B30-BCF7-C4B6320F142E)
- [UPDATE_CLOUD_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-599BBBCC-ECA4-458F-A548-1BE445939B55)
- [UPDATE_CLOUD_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-04EB4D9B-C257-4097-9ECF-E02577331DBE)
- [UPDATE_CLOUD_VM_CLUSTER_IORM_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-F3687221-7BC6-4C99-9916-E5FF312DD964)
- [UPDATE_CONSOLE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DF62E8D1-A781-457C-8D55-ADD68858797F)
- [UPDATE_CONSOLE_HISTORY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-FD432C13-DBF3-45DA-8340-13375984FBBC)
- [UPDATE_DATA_GUARD_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A7C5689C-C288-44F2-BDC5-748FB3C7603C)
- [UPDATE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-AD65AA9F-E50A-4AD0-914D-955EBB8B8C11)
- [UPDATE_DATABASE_SOFTWARE_IMAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-DC86695A-DC63-4DB8-B608-8A287C3406A4)
- [UPDATE_DB_HOME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A7C5F248-4180-49D4-8CE8-7699E41973AD)
- [UPDATE_DB_NODE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-20C52152-C001-45BB-BA0C-EEDF4A9280EE)
- [UPDATE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-40DFCF1A-CB21-465A-90C2-90EBF810DD21)
- [UPDATE_EXADATA_INFRASTRUCTURE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-720E5F0F-1852-424A-849E-242F629A3C95)
- [UPDATE_EXADATA_IORM_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-59B63281-B3A1-4BFD-99CF-04B991712697)
- [UPDATE_EXTERNAL_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-44D698E3-1D01-4E3A-B63D-4CA7ADD38656)
- [UPDATE_EXTERNAL_DATABASE_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-95E149A2-EAB4-4535-AB6A-FD5E79BEAAD7)
- [UPDATE_EXTERNAL_NON_CONTAINER_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-B7CCC7B0-9E27-4961-8E69-6A513A031915)
- [UPDATE_EXTERNAL_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-7AD4A271-A69B-4D72-95CF-50DC46B41BE7)
- [UPDATE_KEY_STORE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-D22F092A-B287-48DF-A3C2-D278FEA489D3)
- [UPDATE_MAINTENANCE_RUN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-45FA7139-89D6-4ACF-BA82-A6BE9679CCEA)
- [UPDATE_ONEOFF_PATCH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-695AE4BA-8995-4DBD-BB86-7442C65476FC)
- [UPDATE_PLUGGABLE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-FEB1FFF9-035A-4B90-95F3-71475959B642)
- [UPDATE_VM_CLUSTER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-FC2F8D11-A221-4F64-9876-ED5A1F3BCE0F)
- [UPDATE_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-053D1AFF-2881-4425-8743-609DCB5450DE)
- [UPGRADE_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-3E9E693A-9CD3-4405-98AC-A0DD5479CC1A)
- [UPGRADE_DB_SYSTEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-6081B826-6429-4830-B6F6-118AFCF9C897)
- [VALIDATE_VM_CLUSTER_NETWORK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_db_database.html#ADSDK-GUID-A4677910-DE41-4DBB-A2B7-B85E12D5E4F3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
