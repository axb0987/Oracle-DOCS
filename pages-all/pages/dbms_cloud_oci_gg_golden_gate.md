# Golden Gate Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#dcoc-content-body)

## Golden Gate Functions

Package: DBMS_CLOUD_OCI_GG_GOLDEN_GATE

### CANCEL_DEPLOYMENT_BACKUP Function

Cancels a Deployment Backup creation process.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`cancel_deployment_backup_details`

(required) A placeholder for any additional metadata to describe the deployment backup cancel.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_DEPLOYMENT_UPGRADE Function

Cancels a DeploymentUpgrade, applicable only for DeploymentUpgrade in Waiting state. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`cancel_deployment_upgrade_details`

(required) A placeholder for any additional metadata to describe the cancel snooze of deployment upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_SNOOZE_DEPLOYMENT_UPGRADE Function

Cancel snooze of a DeploymentUpgrade. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`cancel_snooze_deployment_upgrade_details`

(required) A placeholder for any additional metadata to describe the cancel snooze of deployment upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_CONNECTION_COMPARTMENT Function

Moves the Connection into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Connection.

`change_connection_compartment_details`

(required) Properties to change the compartment of a Connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_REGISTRATION_COMPARTMENT Function

Note: Deprecated. Use the /connections API instead. Moves the DatabaseRegistration into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`database_registration_id`

(required) A unique DatabaseRegistration identifier.

`change_database_registration_compartment_details`

(required) Properties to change the compartment of a DatabaseRegistration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DEPLOYMENT_BACKUP_COMPARTMENT Function

Moves a DeploymentBackup into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`change_deployment_backup_compartment_details`

(required) Properties to change the compartment of a DeploymentBackup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DEPLOYMENT_COMPARTMENT Function

Moves the Deployment into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the resource. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`change_deployment_compartment_details`

(required) Properties to change the compartment of a Deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COLLECT_DEPLOYMENT_DIAGNOSTIC Function

Collects the diagnostic of a Deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`collect_deployment_diagnostic_details`

(required) Metadata about the deployment diagnostic. This also includes the Object storage information where the diagnostic will be uploaded

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COPY_DEPLOYMENT_BACKUP Function

Creates a copy of a Deployment Backup.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`copy_deployment_backup_details`

(required) A placeholder for any additional metadata to describe the copy of a Deployment Backup.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CERTIFICATE Function

Creates a new certificate to truststore.

Syntax
```

```

Parameters

Parameter Description

`create_certificate_details`

(required) Specifications to create the certificate to truststore.

`deployment_id`

(required) A unique Deployment identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION Function

Creates a new Connection.

Syntax
```

```

Parameters

Parameter Description

`create_connection_details`

(required) Specification of the Connection to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CONNECTION_ASSIGNMENT Function

Creates a new Connection Assignment.

Syntax
```

```

Parameters

Parameter Description

`create_connection_assignment_details`

(required) Specification of the connection assignment to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATABASE_REGISTRATION Function

Note: Deprecated. Use the /connections API instead. Creates a new DatabaseRegistration.

Syntax
```

```

Parameters

Parameter Description

`create_database_registration_details`

(required) Specification of the DatabaseRegistration to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOYMENT Function

Creates a new Deployment.

Syntax
```

```

Parameters

Parameter Description

`create_deployment_details`

(required) Specifications to create the Deployment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DEPLOYMENT_BACKUP Function

Creates a new DeploymentBackup.

Syntax
```

```

Parameters

Parameter Description

`create_deployment_backup_details`

(required) Specification of the DeploymentBackup to create.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CERTIFICATE Function

Deletes the certificate from truststore.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`certificate_key`

(required) A unique certificate identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION Function

Deletes a Connection.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CONNECTION_ASSIGNMENT Function

Deletes a Connection Assignment.

Syntax
```

```

Parameters

Parameter Description

`connection_assignment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Connection Assignment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATABASE_REGISTRATION Function

Note: Deprecated. Use the /connections API instead. Deletes a DatabaseRegistration.

Syntax
```

```

Parameters

Parameter Description

`database_registration_id`

(required) A unique DatabaseRegistration identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOYMENT Function

Deletes the Deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DEPLOYMENT_BACKUP Function

Deletes a DeploymentBackup.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEPLOYMENT_WALLET_EXISTS Function

Checks if a wallet is already present in the deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`deployment_wallet_exists_details`

(required) A placeholder for any additional metadata to describe the deployment start.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXPORT_DEPLOYMENT_WALLET Function

Export the OGG wallet from the deployment to OCI vault. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`export_deployment_wallet_details`

(required) Metadata to export the OGG wallet from deployment. This also includes the OCI vault information where the wallet will be exported to

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CERTIFICATE Function

Retrieves a Certificate.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`certificate_key`

(required) A unique certificate identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION Function

Retrieves a Connection.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Connection.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONNECTION_ASSIGNMENT Function

Retrieves a Connection Assignment.

Syntax
```

```

Parameters

Parameter Description

`connection_assignment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Connection Assignment.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_REGISTRATION Function

Note: Deprecated. Use the /connections API instead. Retrieves a DatabaseRegistration.

Syntax
```

```

Parameters

Parameter Description

`database_registration_id`

(required) A unique DatabaseRegistration identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOYMENT Function

Retrieves a deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOYMENT_BACKUP Function

Retrieves a DeploymentBackup.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DEPLOYMENT_UPGRADE Function

Retrieves a deployment upgrade.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Retrieve the WorkRequest identified by the given OCID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_DEPLOYMENT_WALLET Function

Imports an OGG wallet from the OCI Vault to the Deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`import_deployment_wallet_details`

(required) Metadata to import wallet to deployment. This also includes the OCI Vault information where the wallet will be imported from

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CERTIFICATES Function

Returns a list of certificates from truststore.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`lifecycle_state`

(optional) A filter to return only connections having the 'lifecycleState' given.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTION_ASSIGNMENTS Function

Lists the Connection Assignments in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment in which to list resources.

`connection_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection.

`name`

(optional) The name of the connection in the assignment (aliasName).

`lifecycle_state`

(optional) A filter to return only connection assignments having the 'lifecycleState' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONNECTIONS Function

Lists the Connections in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`technology_type`

(optional) The array of technology types.

Allowed values are: 'GOLDENGATE', 'GENERIC', 'OCI_AUTONOMOUS_DATABASE', 'OCI_AUTONOMOUS_JSON_DATABASE', 'OCI_MYSQL', 'OCI_OBJECT_STORAGE', 'OCI_STREAMING', 'ORACLE_DATABASE', 'ORACLE_EXADATA', 'ORACLE_NOSQL', 'ORACLE_WEBLOGIC_JMS', 'AMAZON_RDS_ORACLE', 'AMAZON_RDS_SQLSERVER', 'AMAZON_S3', 'AMAZON_AURORA_MYSQL', 'AMAZON_AURORA_POSTGRESQL', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'AMAZON_RDS_MARIADB', 'AMAZON_RDS_MYSQL', 'AMAZON_RDS_POSTGRESQL', 'APACHE_KAFKA', 'AZURE_COSMOS_DB_FOR_MONGODB', 'AZURE_DATA_LAKE_STORAGE', 'AZURE_EVENT_HUBS', 'AZURE_MYSQL', 'AZURE_POSTGRESQL', 'AZURE_SQLSERVER_MANAGED_INSTANCE', 'AZURE_SQLSERVER_NON_MANAGED_INSTANCE', 'AZURE_SYNAPSE_ANALYTICS', 'CONFLUENT_KAFKA', 'CONFLUENT_SCHEMA_REGISTRY', 'ELASTICSEARCH', 'GOOGLE_BIGQUERY', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_CLOUD_SQL_MYSQL', 'GOOGLE_CLOUD_SQL_POSTGRESQL', 'GOOGLE_CLOUD_SQL_SQLSERVER', 'HDFS', 'MARIADB', 'MICROSOFT_SQLSERVER', 'MONGODB', 'MYSQL_SERVER', 'POSTGRESQL_SERVER', 'REDIS', 'SINGLESTOREDB', 'SINGLESTOREDB_CLOUD', 'SNOWFLAKE'

`connection_type`

(optional) The array of connection types.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`assigned_deployment_id`

(optional) The OCID of the deployment which for the connection must be assigned.

`assignable_deployment_id`

(optional) Filters for compatible connections which can be, but currently not assigned to the deployment specified by its id.

`assignable_deployment_type`

(optional) Filters for connections which can be assigned to the latest version of the specified deployment type.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`lifecycle_state`

(optional) A filter to return only connections having the 'lifecycleState' given.

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_REGISTRATIONS Function

Note: Deprecated. Use the /connections API instead. Lists the DatabaseRegistrations in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`lifecycle_state`

(optional) A filter to return only the resources that match the 'lifecycleState' given.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENT_BACKUPS Function

Lists the Backups in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment in which to list resources.

`lifecycle_state`

(optional) A filter to return only the resources that match the 'lifecycleState' given.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENT_TYPES Function

Returns an array of DeploymentTypeDescriptor

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`deployment_type`

(optional) The type of deployment, the value determines the exact 'type' of the service executed in the deployment. Default value is DATABASE_ORACLE.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`ogg_version`

(optional) Allows to query by a specific GoldenGate version.

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENT_UPGRADES Function

Lists the Deployment Upgrades in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment in which to list resources.

`lifecycle_state`

(optional) A filter to return only the resources that match the 'lifecycleState' given.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENT_VERSIONS Function

Returns the list of available deployment versions.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment in which to list resources.

`deployment_type`

(optional) The type of deployment, the value determines the exact 'type' of the service executed in the deployment. Default value is DATABASE_ORACLE.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENT_WALLETS_OPERATIONS Function

Lists the wallets export/import operations to/from a deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeStarted' is descending.

Allowed values are: 'timeStarted'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DEPLOYMENTS Function

Lists the Deployments in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`supported_connection_type`

(optional) The connection type which the deployment must support.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`assigned_connection_id`

(optional) The OCID of the connection which for the deployment must be assigned.

`assignable_connection_id`

(optional) Return the deployments to which the specified connectionId may be assigned.

`lifecycle_state`

(optional) A filter to return only the resources that match the 'lifecycleState' given.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_sub_state`

(optional) A filter to return only the resources that match the 'lifecycleSubState' given.

Allowed values are: 'RECOVERING', 'STARTING', 'STOPPING', 'MOVING', 'UPGRADING', 'RESTORING', 'BACKUP_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS'

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`fqdn`

(optional) A filter to return only the resources that match the 'fqdn' given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeCreated' is descending. Default order for 'displayName' is ascending. If no value is specified timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MESSAGES Function

Lists the DeploymentMessages for a deployment. The sorting order is not important. By default first will be Upgrade message, next Exception message and then Storage Utilization message.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRAIL_FILES Function

Lists the TrailFiles for a deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`trail_file_id`

(optional) A Trail File identifier

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeLastUpdated' is descending. Default order for 'displayName' is ascending. If no value is specified displayName is the default.

Allowed values are: 'timeLastUpdated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRAIL_SEQUENCES Function

Lists the Trail Sequences for a TrailFile in a given deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`trail_file_id`

(required) A Trail File identifier

`trail_sequence_id`

(optional) A Trail Sequence identifier

`display_name`

(optional) A filter to return only the resources that match the entire 'displayName' given.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Default order for 'timeLastUpdated' is descending. Default order for 'displayName' is ascending. If no value is specified displayName is the default.

Allowed values are: 'timeLastUpdated', 'displayName'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Lists work request errors.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Lists work request logs.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request concerns multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resource_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the resource in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESCHEDULE_DEPLOYMENT_UPGRADE Function

Reschedules a DeploymentUpgrade, applicable only for DeploymentUpgrade in Waiting state. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`reschedule_deployment_upgrade_details`

(required) Properties to reschedule DeploymentUpgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESTORE_DEPLOYMENT Function

Restores a Deployment from a Deployment Backup created from the same Deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`restore_deployment_details`

(required) A placeholder for any additional metadata to describe the deployment restore.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ROLLBACK_DEPLOYMENT_UPGRADE Function

Rollback a deployment to it's previous version. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`rollback_deployment_upgrade_details`

(required) A placeholder for any additional metadata to describe the deployment rollback.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SNOOZE_DEPLOYMENT_UPGRADE Function

Snooze a DeploymentUpgrade. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`snooze_deployment_upgrade_details`

(required) A placeholder for any additional metadata to describe the snooze of deployment upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_DEPLOYMENT Function

Starts a Deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`start_deployment_details`

(required) A placeholder for any additional metadata to describe the deployment start.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_DEPLOYMENT Function

Stops a Deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`stop_deployment_details`

(required) A placeholder for any additional metadata to describe the deployment stop.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TEST_CONNECTION_ASSIGNMENT Function

Tests the connectivity between given GoldenGate deployment and one of the associated database / service. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`connection_assignment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Connection Assignment.

`test_connection_assignment_details`

(required) A placeholder for any additional metadata to describe the requested tests of the assigned connection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONNECTION Function

Updates the Connection.

Syntax
```

```

Parameters

Parameter Description

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a Connection.

`update_connection_details`

(required) The new Connection specifications to apply.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_REGISTRATION Function

Note: Deprecated. Use the /connections API instead. Updates the DatabaseRegistration.

Syntax
```

```

Parameters

Parameter Description

`database_registration_id`

(required) A unique DatabaseRegistration identifier.

`update_database_registration_details`

(required) The new DatabaseRegistration specifications to apply.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOYMENT Function

Modifies a Deployment.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`update_deployment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DEPLOYMENT_BACKUP Function

Modifies a Deployment Backup.

Syntax
```

```

Parameters

Parameter Description

`deployment_backup_id`

(required) A unique DeploymentBackup identifier.

`update_deployment_backup_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPGRADE_DEPLOYMENT Function

Upgrade a Deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_id`

(required) A unique Deployment identifier.

`upgrade_deployment_details`

(required) A placeholder for any additional metadata to describe the deployment upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPGRADE_DEPLOYMENT_UPGRADE Function

Upgrade a deployment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`deployment_upgrade_id`

(required) A unique Deployment Upgrade identifier.

`upgrade_deployment_upgrade_details`

(required) A placeholder for any additional metadata to describe the deployment upgrade.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried, in case of a timeout or server error, without the risk of executing that same action again. Retry tokens expire after 24 hours but can be invalidated before then due to conflicting operations. For example, if a resource was deleted and purged from the system, then a retry of the original creation request is rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://goldengate.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Golden Gate Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-5DC627CE-0932-4DD5-8EF4-BF5F41D5206E)
- [CANCEL_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-5E213847-6BDB-4610-99EB-C8C0E3300578)
- [CANCEL_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-0457C7DB-2DCF-442B-9FFE-2972550A94B3)
- [CANCEL_SNOOZE_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-06F7A50A-9B44-4CF1-A616-1A3608755A49)
- [CHANGE_CONNECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-4CCE85BC-7872-414A-AF0C-C70DE1BEC3EF)
- [CHANGE_DATABASE_REGISTRATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-7E057D2B-279F-41D9-8E85-2C8B8640F079)
- [CHANGE_DEPLOYMENT_BACKUP_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-48D9DA9E-F3FE-4B48-AE77-930BFB00DC4A)
- [CHANGE_DEPLOYMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-669FAA16-FA45-4790-8FD2-BF541378EBA1)
- [COLLECT_DEPLOYMENT_DIAGNOSTIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-F18EE2A2-6C49-4CB3-B5FA-8C5246F3D7E1)
- [COPY_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-DE75A08F-C769-484D-AF6D-2119740DC6F5)
- [CREATE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-961C7C1D-0499-420B-82E9-5EF0052C9003)
- [CREATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-5A35B124-E1EB-4661-8BE6-AA184ACC2A4B)
- [CREATE_CONNECTION_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-D2B43025-C5EA-4F9F-946B-5C83734D7C7C)
- [CREATE_DATABASE_REGISTRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-CA728201-D017-4929-A0BF-7F20C7B29B1E)
- [CREATE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-3000BF24-C2C5-4711-986C-C94A248A536E)
- [CREATE_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-34A7DE13-14F7-499D-8BC0-AE8A4E6F8EDB)
- [DELETE_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-136F0A84-6BA0-4A59-90D2-D20A61559874)
- [DELETE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-B94D92B6-66E1-4950-84CA-B8578BE1E012)
- [DELETE_CONNECTION_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-B8DB99E0-B52C-4555-8F1E-1E0BC1727B4A)
- [DELETE_DATABASE_REGISTRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-595C03D4-5F3B-4620-80F1-E8168A4E800F)
- [DELETE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-1F4E0FAA-0BD7-4B87-BB3D-5AC7E45CFA10)
- [DELETE_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-75B810DB-849B-42C1-B1B7-B117174C6B98)
- [DEPLOYMENT_WALLET_EXISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-823FB726-72E8-4ACB-9244-3C68045DC287)
- [EXPORT_DEPLOYMENT_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-A90D457C-4572-4FC9-8852-A8B840016E72)
- [GET_CERTIFICATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-BF811AAA-4CF2-4C61-A0B9-2B20F6645DF8)
- [GET_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-26BD1B08-F713-4F5E-94E9-20206BCBFF6F)
- [GET_CONNECTION_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-B921E48F-D7E1-4417-881D-A1F7CE174EB5)
- [GET_DATABASE_REGISTRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-51EC221E-EE77-4F07-BB67-A848A109BD9B)
- [GET_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-A24F0569-093E-43C7-8BB7-4B648505CC2C)
- [GET_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-63D9E478-EEAB-4449-90CE-2ADF4CF2AC1B)
- [GET_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-C6C8B4EF-8584-4B12-8472-1BF5143C6040)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-00F88CBD-4CF5-46CF-9B75-4103B1E412A2)
- [IMPORT_DEPLOYMENT_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-D1BF07C6-0312-4C8B-854C-95AF8C8C4AB2)
- [LIST_CERTIFICATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-7AA75FD8-1717-4014-9761-B31EECADC955)
- [LIST_CONNECTION_ASSIGNMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-6DD639F4-9E9A-49C8-A921-A57F29CA47A8)
- [LIST_CONNECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-764B3E79-47C8-4E33-A98A-8E85B016C708)
- [LIST_DATABASE_REGISTRATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-860D8C96-12EF-43A0-8943-23E0D1C40380)
- [LIST_DEPLOYMENT_BACKUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-354E42C7-9CCD-4C20-83D7-6A1561CF3473)
- [LIST_DEPLOYMENT_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-DA66BD6A-6686-4E41-8545-B9FDFE84AB9C)
- [LIST_DEPLOYMENT_UPGRADES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-41D92FA3-DCD2-432B-B1A9-D263808EA119)
- [LIST_DEPLOYMENT_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-06DD3D64-9C51-44A1-ABBB-88BEDEEA583F)
- [LIST_DEPLOYMENT_WALLETS_OPERATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-AF875028-2BD9-46B8-A788-334A08197F14)
- [LIST_DEPLOYMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-8D11BEA5-5947-4CE4-98CC-0841221C4164)
- [LIST_MESSAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-64C16456-02E2-4C6B-B21D-5A0444EA0E04)
- [LIST_TRAIL_FILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-7EEBD683-CE96-4F82-8322-0E03221CEB56)
- [LIST_TRAIL_SEQUENCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-EE5111B0-D7A2-436D-BDA0-F2AF131A1596)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-D219D2CA-F36C-4582-B49C-8E65346B8641)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-F10C800C-B98C-43FD-BDD3-B09A72E140C5)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-33AC5C22-BFF8-433E-AAE0-4C084CBA349D)
- [RESCHEDULE_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-204E5FBA-5AA6-4281-8AFA-CD07833974E3)
- [RESTORE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-9FFD5F8D-17B8-4F56-88A0-047939DAD506)
- [ROLLBACK_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-263AB106-770C-4C56-9400-A06599A28BA1)
- [SNOOZE_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-BDDF1CD6-7F20-4CA8-B56F-4E9D57A175C7)
- [START_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-29F81780-B1A4-49C0-91A5-7250467485D2)
- [STOP_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-85426CE4-84A0-4979-965C-6DEA7836B1B6)
- [TEST_CONNECTION_ASSIGNMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-785A8BAB-A9D6-43F1-B758-D6C7CB26E346)
- [UPDATE_CONNECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-B1597BBB-6D18-4173-A623-57BFB919D882)
- [UPDATE_DATABASE_REGISTRATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-DC84FBE5-45AE-45CC-84BD-34BFC3180095)
- [UPDATE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-C5D68B85-15D0-4289-B446-11FB5B0CA62E)
- [UPDATE_DEPLOYMENT_BACKUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-C4AED8E5-507C-413E-8B62-54393E6B942C)
- [UPGRADE_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-78CC0A94-BA60-4A1C-9649-7FD21F037CE3)
- [UPGRADE_DEPLOYMENT_UPGRADE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gg_golden_gate.html#ADSDK-GUID-A645D646-C357-408A-991A-6BB76AB76E6C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
