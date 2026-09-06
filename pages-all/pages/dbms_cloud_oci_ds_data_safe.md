# Data Safe Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#dcoc-content-body)

## Data Safe Functions

Package: DBMS_CLOUD_OCI_DS_DATA_SAFE

### ACTIVATE_TARGET_DATABASE Function

Reactivates a previously deactivated Data Safe target database.

Syntax
```

```

Parameters

Parameter Description

`activate_target_database_details`

(required) The details used to reactivate a target database in Data Safe.

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_MASKING_COLUMNS_FROM_SDM Function

Adds columns to the specified masking policy from the associated sensitive data model. It automatically pulls all the sensitive columns and their relationships from the sensitive data model and uses this information to create columns in the masking policy. It also assigns default masking formats to these columns based on the associated sensitive types.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ALERTS_UPDATE Function

Updates alerts in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`alerts_update_details`

(required) The details to update the alerts in the specified compartment.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### APPLY_DISCOVERY_JOB_RESULTS Function

Applies the results of a discovery job to the specified sensitive data model. Note that the plannedAction attribute of discovery results is used for processing them. You should first use PatchDiscoveryJobResults to set the plannedAction attribute of the discovery results you want to process. ApplyDiscoveryJobResults automatically reads the plannedAction attribute and updates the sensitive data model to reflect the actions you planned.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`apply_discovery_job_results_details`

(required) Details to apply the discovery results to a sensitive data model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### APPLY_SDM_MASKING_POLICY_DIFFERENCE Function

Applies the difference of a SDM Masking policy difference resource to the specified masking policy. Note that the plannedAction attribute of difference columns is used for processing. You should first use PatchSdmMaskingPolicyDifferenceColumns to set the plannedAction attribute of the difference columns you want to process. ApplySdmMaskingPolicyDifference automatically reads the plannedAction attribute and updates the masking policy to reflect the actions you planned. If the sdmMaskingPolicydifferenceId is not passed, the latest sdmMaskingPolicydifference is used. Note that if the masking policy associated with the SdmMaskingPolicyDifference used for this operation is not associated with the original SDM anymore, this operation won't be allowed.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`apply_sdm_masking_policy_difference_details`

(required) Details to apply the SDM Masking policy difference columns to a masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CALCULATE_AUDIT_VOLUME_AVAILABLE Function

Calculates the volume of audit events available on the target database to be collected. Measurable up to the defined retention period of the audit target resource.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`calculate_audit_volume_available_details`

(required) Details for the calculation of audit volume available on target database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CALCULATE_AUDIT_VOLUME_COLLECTED Function

Calculates the volume of audit events collected by data safe.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`calculate_audit_volume_collected_details`

(required) Details for the calculation of audit volume collected by data safe.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancel the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ALERT_COMPARTMENT Function

Moves the specified alert into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`alert_id`

(required) The OCID of alert.

`change_alert_compartment_details`

(required) The details used to change the compartment of an alert.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUDIT_ARCHIVE_RETRIEVAL_COMPARTMENT Function

Moves the archive retreival to the specified compartment. When provided, if-Match is checked against ETag value of the resource.

Syntax
```

```

Parameters

Parameter Description

`audit_archive_retrieval_id`

(required) OCID of the archive retrieval.

`change_audit_archive_retrieval_compartment_details`

(required) The details used to change the compartment of a archive retrieval.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUDIT_POLICY_COMPARTMENT Function

Moves the specified audit policy and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`audit_policy_id`

(required) Unique audit policy identifier.

`change_audit_policy_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_AUDIT_PROFILE_COMPARTMENT Function

Moves the specified audit profile and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`change_audit_profile_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATA_SAFE_PRIVATE_ENDPOINT_COMPARTMENT Function

Moves the Data Safe private endpoint and its dependent resources to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`data_safe_private_endpoint_id`

(required) The OCID of the private endpoint.

`change_data_safe_private_endpoint_compartment_details`

(required) The details used to change the compartment of a Data Safe private endpoint.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATABASE_SECURITY_CONFIG_COMPARTMENT Function

Moves the specified database security configuration and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`database_security_config_id`

(required) The OCID of the database security configuration resource.

`change_database_security_config_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DISCOVERY_JOB_COMPARTMENT Function

Moves the specified discovery job and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`change_discovery_job_compartment_details`

(required) The details used to change the compartment of a resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_LIBRARY_MASKING_FORMAT_COMPARTMENT Function

Moves the specified library masking format into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`library_masking_format_id`

(required) The OCID of the library masking format.

`change_library_masking_format_compartment_details`

(required) Details to change the compartment of a library masking format.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MASKING_POLICY_COMPARTMENT Function

Moves the specified masking policy and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`change_masking_policy_compartment_details`

(required) Details to change the compartment of a masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_ON_PREM_CONNECTOR_COMPARTMENT Function

Moves the specified on-premises connector into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`change_on_prem_connector_compartment_details`

(required) The details used to change the compartment of an on-premises connector.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REPORT_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`report_id`

(required) Unique report identifier

`change_report_compartment_details`

(required) Details for the different Report.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_REPORT_DEFINITION_COMPARTMENT Function

Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`change_report_definition_compartment_details`

(required) Details for the different ReportDefinition.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_RETENTION Function

Change the online and offline months .

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`change_retention_details`

(required) Details for the audit retention months to be modified.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SDM_MASKING_POLICY_DIFFERENCE_COMPARTMENT Function

Moves the specified SDM masking policy difference into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`change_sdm_masking_policy_difference_compartment_details`

(required) The details used to change the compartment of a resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_ASSESSMENT_COMPARTMENT Function

Moves the specified saved security assessment or future scheduled assessments into a different compartment. To start, call first the operation ListSecurityAssessments with filters \"type = save_schedule\". This returns the scheduleAssessmentId. Then, call this changeCompartment with the scheduleAssessmentId. The existing saved security assessments created due to the schedule are not moved. However, all new saves will be associated with the new compartment.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`change_security_assessment_compartment_details`

(required) The details used to change the compartment of a security assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_POLICY_COMPARTMENT Function

Moves the specified security policy and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`security_policy_id`

(required) The OCID of the security policy resource.

`change_security_policy_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_POLICY_DEPLOYMENT_COMPARTMENT Function

Moves the specified security policy deployment and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`security_policy_deployment_id`

(required) The OCID of the security policy deployment resource.

`change_security_policy_deployment_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SENSITIVE_DATA_MODEL_COMPARTMENT Function

Moves the specified sensitive data model and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`change_sensitive_data_model_compartment_details`

(required) Details to change the compartment of a sensitive data model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SENSITIVE_TYPE_COMPARTMENT Function

Moves the specified sensitive type into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`sensitive_type_id`

(required) The OCID of the sensitive type.

`change_sensitive_type_compartment_details`

(required) Details to change the compartment of a sensitive type.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SQL_COLLECTION_COMPARTMENT Function

Moves the specified SQL collection and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`change_sql_collection_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SQL_FIREWALL_POLICY_COMPARTMENT Function

Moves the specified SQL Firewall policy and its dependent resources into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`sql_firewall_policy_id`

(required) The OCID of the SQL Firewall policy resource.

`change_sql_firewall_policy_compartment_details`

(required) Details for the compartment move.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TARGET_ALERT_POLICY_ASSOCIATION_COMPARTMENT Function

Moves the specified target-alert policy Association into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`target_alert_policy_association_id`

(required) The OCID of the target-alert policy association.

`change_target_alert_policy_association_compartment_details`

(required) The details used to change the compartment of a target-alert policy association.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TARGET_DATABASE_COMPARTMENT Function

Moves the Data Safe target database to the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`change_target_database_compartment_details`

(required) Details of the move compartment request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_USER_ASSESSMENT_COMPARTMENT Function

Moves the specified saved user assessment or future scheduled assessments into a different compartment. To start storing scheduled user assessments on a different compartment, first call the operation ListUserAssessments with the filters \"type = save_schedule\". That call returns the scheduleAssessmentId. Then call ChangeUserAssessmentCompartment with the scheduleAssessmentId. The existing saved user assessments created per the schedule are not be moved. However, all new saves will be associated with the new compartment.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`change_user_assessment_compartment_details`

(required) The details used to change the compartment of a user assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COMPARE_SECURITY_ASSESSMENT Function

Compares two security assessments. For this comparison, a security assessment can be a saved assessment, a latest assessment, or a baseline assessment. For example, you can compare saved assessment or a latest assessment against a baseline.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`compare_security_assessment_details`

(required) Details of the security assessment comparison.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### COMPARE_USER_ASSESSMENT Function

Compares two user assessments. For this comparison, a user assessment can be a saved, a latest assessment, or a baseline. As an example, it can be used to compare a user assessment saved or a latest assessment with a baseline.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`compare_user_assessment_details`

(required) Details of the user assessment comparison.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUDIT_ARCHIVE_RETRIEVAL Function

Creates a work request to retrieve archived audit data. This asynchronous process will usually take over an hour to complete. Save the id from the response of this operation. Call GetAuditArchiveRetrieval operation after an hour, passing the id to know the status of this operation.

Syntax
```

```

Parameters

Parameter Description

`create_audit_archive_retrieval_details`

(required) Details for creating retrieving archived audit data.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_SAFE_PRIVATE_ENDPOINT Function

Creates a new Data Safe private endpoint.

Syntax
```

```

Parameters

Parameter Description

`create_data_safe_private_endpoint_details`

(required) Details to create a new private endpoint.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DISCOVERY_JOB Function

Performs incremental data discovery for the specified sensitive data model. It uses the target database associated with the sensitive data model. After performing data discovery, you can use ListDiscoveryJobResults to view the discovery results, PatchDiscoveryJobResults to specify the action you want perform on these results, and then ApplyDiscoveryJobResults to process the results and apply them to the sensitive data model.

Syntax
```

```

Parameters

Parameter Description

`create_discovery_job_details`

(required) The details used to run an incremental data discovery job

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LIBRARY_MASKING_FORMAT Function

Creates a new library masking format. A masking format can have one or more format entries. The combined output of all the format entries is used for masking. It provides the flexibility to define a masking format that can generate different parts of a data value separately and then combine them to get the final data value for masking. Note that you cannot define masking condition in a library masking format.

Syntax
```

```

Parameters

Parameter Description

`create_library_masking_format_details`

(required) Details to create a new library masking format.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MASKING_COLUMN Function

Creates a new masking column in the specified masking policy. Use this operation to add parent columns only. It automatically adds the child columns from the associated sensitive data model or target database. If you provide the sensitiveTypeId attribute but not the maskingFormats attribute, it automatically assigns the default masking format associated with the specified sensitive type. Alternatively, if you provide the maskingFormats attribute, the specified masking formats are assigned to the column. Using the maskingFormats attribute, you can assign one or more masking formats to a column. You need to specify a condition as part of each masking format. It enables you to do &lt;a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/conditional-masking.html\"&gt;conditional masking&lt;/a&gt; so that you can mask the column data values differently using different masking conditions. A masking format can have one or more format entries. The combined output of all the format entries is used for masking. It provides the flexibility to define a masking format that can generate different parts of a data value separately and then combine them to get the final data value for masking. You can use the maskingColumnGroup attribute to group the columns that you would like to mask together. It enables you to do &lt;a href=\"https://docs.oracle.com/en/cloud/paas/data-safe/udscs/group-masking1.html#GUID-755056B9-9540-48C0-9491-262A44A85037\"&gt;group or compound masking&lt;/a&gt; that ensures that the masked data across the columns in a group continue to retain the same logical relationship.

Syntax
```

```

Parameters

Parameter Description

`create_masking_column_details`

(required) Details to create a new masking column.

`masking_policy_id`

(required) The OCID of the masking policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MASKING_POLICY Function

Creates a new masking policy and associates it with a sensitive data model or a target database. To use a sensitive data model as the source of masking columns, set the columnSource attribute to SENSITIVE_DATA_MODEL and provide the sensitiveDataModelId attribute. After creating a masking policy, you can use the AddMaskingColumnsFromSdm operation to automatically add all the columns from the associated sensitive data model. In this case, the target database associated with the sensitive data model is used for column and masking format validations. You can also create a masking policy without using a sensitive data model. In this case, you need to associate your masking policy with a target database by setting the columnSource attribute to TARGET and providing the targetId attribute. The specified target database is used for column and masking format validations. After creating a masking policy, you can use the CreateMaskingColumn or PatchMaskingColumns operation to manually add columns to the policy. You need to add the parent columns only, and it automatically adds the child columns (in referential relationship with the parent columns) from the associated sensitive data model or target database.

Syntax
```

```

Parameters

Parameter Description

`create_masking_policy_details`

(required) Details to create a new masking policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ON_PREM_CONNECTOR Function

Creates a new on-premises connector.

Syntax
```

```

Parameters

Parameter Description

`create_on_prem_connector_details`

(required) The details used to create a new on-premises connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REPORT_DEFINITION Function

Creates a new report definition with parameters specified in the body. The report definition is stored in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`create_report_definition_details`

(required) Details for the new report definition.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SDM_MASKING_POLICY_DIFFERENCE Function

Creates SDM masking policy difference for the specified masking policy. It finds the difference between masking columns of the masking policy and sensitive columns of the SDM. After performing this operation, you can use ListDifferenceColumns to view the difference columns, PatchSdmMaskingPolicyDifferenceColumns to specify the action you want perform on these columns, and then ApplySdmMaskingPolicyDifference to process the difference columns and apply them to the masking policy.

Syntax
```

```

Parameters

Parameter Description

`create_sdm_masking_policy_difference_details`

(required) The details used to create a SDM masking policy difference resource

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SECURITY_ASSESSMENT Function

Creates a new saved security assessment for one or multiple targets in a compartment. When this operation is performed, it will save the latest assessments in the specified compartment. If a schedule is passed, it will persist the latest assessments, at the defined date and time, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

Syntax
```

```

Parameters

Parameter Description

`create_security_assessment_details`

(required) The details used to create a new saved security assessment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SENSITIVE_COLUMN Function

Creates a new sensitive column in the specified sensitive data model.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`create_sensitive_column_details`

(required) Details to create a new sensitive column.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SENSITIVE_DATA_MODEL Function

Creates a new sensitive data model. If schemas and sensitive types are provided, it automatically runs data discovery and adds the discovered columns to the sensitive data model. Otherwise, it creates an empty sensitive data model that can be updated later.

Syntax
```

```

Parameters

Parameter Description

`create_sensitive_data_model_details`

(required) Details to create a new sensitive data model.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SENSITIVE_TYPE Function

Creates a new sensitive type, which can be a basic sensitive type with regular expressions or a sensitive category. While sensitive types are used for data discovery, sensitive categories are used for logically grouping the related or similar sensitive types.

Syntax
```

```

Parameters

Parameter Description

`create_sensitive_type_details`

(required) Details to create a new sensitive type.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SQL_COLLECTION Function

Creates a new SQL collection resource.

Syntax
```

```

Parameters

Parameter Description

`create_sql_collection_details`

(required) Details of the SQL collection.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TARGET_ALERT_POLICY_ASSOCIATION Function

Creates a new target-alert policy association to track a alert policy applied on target.

Syntax
```

```

Parameters

Parameter Description

`create_target_alert_policy_association_details`

(required) The details used to create a new target-alert policy association.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TARGET_DATABASE Function

Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console.

Syntax
```

```

Parameters

Parameter Description

`create_target_database_details`

(required) Details of the target database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_USER_ASSESSMENT Function

Creates a new saved user assessment for one or multiple targets in a compartment. It saves the latest assessments in the specified compartment. If a scheduled is passed in, this operation persists the latest assessments that exist at the defined date and time, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

Syntax
```

```

Parameters

Parameter Description

`create_user_assessment_details`

(required) The details used to create a new saved user assessment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_TARGET_DATABASE Function

Deactivates a target database in Data Safe.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUDIT_ARCHIVE_RETRIEVAL Function

To unload retrieved archive data, call the operation ListAuditArchiveRetrieval first. This will return the auditArchiveRetrievalId. Then call this operation with auditArchiveRetrievalId.

Syntax
```

```

Parameters

Parameter Description

`audit_archive_retrieval_id`

(required) OCID of the archive retrieval.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUDIT_TRAIL Function

Deletes the specified audit trail.

Syntax
```

```

Parameters

Parameter Description

`audit_trail_id`

(required) The OCID of the audit trail.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_SAFE_PRIVATE_ENDPOINT Function

Deletes the specified Data Safe private endpoint.

Syntax
```

```

Parameters

Parameter Description

`data_safe_private_endpoint_id`

(required) The OCID of the private endpoint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DISCOVERY_JOB Function

Deletes the specified discovery job.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DISCOVERY_JOB_RESULT Function

Deletes the specified discovery result.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`result_key`

(required) The unique key that identifies the discovery result.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LIBRARY_MASKING_FORMAT Function

Deletes the specified library masking format.

Syntax
```

```

Parameters

Parameter Description

`library_masking_format_id`

(required) The OCID of the library masking format.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MASKING_COLUMN Function

Deletes the specified masking column.

Syntax
```

```

Parameters

Parameter Description

`masking_column_key`

(required) The unique key that identifies the masking column. It's numeric and unique within a masking policy.

`masking_policy_id`

(required) The OCID of the masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MASKING_POLICY Function

Deletes the specified masking policy.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ON_PREM_CONNECTOR Function

Deletes the specified on-premises connector.

Syntax
```

```

Parameters

Parameter Description

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_REPORT_DEFINITION Function

Deletes the specified report definition. Only the user created report definition can be deleted. The seeded report definitions cannot be deleted.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SDM_MASKING_POLICY_DIFFERENCE Function

Deletes the specified SDM Masking policy difference.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SECURITY_ASSESSMENT Function

Deletes the specified saved security assessment or schedule. To delete a security assessment schedule, first call the operation ListSecurityAssessments with filters \"type = save_schedule\". That operation returns the scheduleAssessmentId. Then, call DeleteSecurityAssessment with the scheduleAssessmentId. If the assessment being deleted is the baseline for that compartment, then it will impact all baselines in the compartment.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SENSITIVE_COLUMN Function

Deletes the specified sensitive column.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`sensitive_column_key`

(required) The unique key that identifies the sensitive column. It's numeric and unique within a sensitive data model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SENSITIVE_DATA_MODEL Function

Deletes the specified sensitive data model.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SENSITIVE_TYPE Function

Deletes the specified sensitive type.

Syntax
```

```

Parameters

Parameter Description

`sensitive_type_id`

(required) The OCID of the sensitive type.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SQL_COLLECTION Function

Deletes the specified SQL collection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SQL_FIREWALL_POLICY Function

Deletes the SQL Firewall policy resource.

Syntax
```

```

Parameters

Parameter Description

`sql_firewall_policy_id`

(required) The OCID of the SQL Firewall policy resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TARGET_ALERT_POLICY_ASSOCIATION Function

Deletes the specified target-alert policy Association.

Syntax
```

```

Parameters

Parameter Description

`target_alert_policy_association_id`

(required) The OCID of the target-alert policy association.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TARGET_DATABASE Function

Deregisters the specified database from Data Safe and removes the target database from the Data Safe Console.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_USER_ASSESSMENT Function

Deletes the specified saved user assessment or schedule. To delete a user assessment schedule, first call the operation ListUserAssessments with filters \"type = save_schedule\". That call returns the scheduleAssessmentId. Then call DeleteUserAssessment with the scheduleAssessmentId. If the assessment being deleted is the baseline for that compartment, then it will impact all baselines in the compartment.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DISCOVER_AUDIT_TRAILS Function

Updates the list of audit trails created under audit profile.The operation can be used to create new audit trails for target database when they become available for audit collection because of change of database version or change of database unified mode or change of data base edition or being deleted previously etc.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_DISCOVERY_REPORT Function

Downloads an already-generated discovery report. Note that the GenerateDiscoveryReportForDownload operation is a prerequisite for the DownloadDiscoveryReport operation. Use GenerateDiscoveryReportForDownload to generate a discovery report file and then use DownloadDiscoveryReport to download the generated file. By default, it downloads report for all the columns in a sensitive data model. Use the discoveryJobId attribute to download report for a specific discovery job.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`download_discovery_report_details`

(required) Details to download a discovery report.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_MASKING_LOG Function

Downloads the masking log generated by the last masking operation on a target database using the specified masking policy.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`download_masking_log_details`

(required) Details to download masking log.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_MASKING_POLICY Function

Downloads an already-generated file corresponding to the specified masking policy. Note that the GenerateMaskingPolicyForDownload operation is a prerequisite for the DownloadMaskingPolicy operation. Use GenerateMaskingPolicyForDownload to generate a masking policy file and then use DownloadMaskingPolicy to download the generated file.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`download_masking_policy_details`

(required) Details to download a masking policy file.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_MASKING_REPORT Function

Downloads an already-generated masking report. Note that the GenerateMaskingReportForDownload operation is a prerequisite for the DownloadMaskingReport operation. Use GenerateMaskingReportForDownload to generate a masking report file and then use DownloadMaskingReport to download the generated file.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`download_masking_report_details`

(required) Details to download a masking report.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_PRIVILEGE_SCRIPT Function

Downloads the privilege script to grant/revoke required roles from the Data Safe account on the target database.

Syntax
```

```

Parameters

Parameter Description

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_SECURITY_ASSESSMENT_REPORT Function

Downloads the report of the specified security assessment. To download the security assessment report, it needs to be generated first. Please use GenerateSecurityAssessmentReport to generate a downloadable report in the preferred format (PDF, XLS).

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`download_security_assessment_report_details`

(required) Details of the report.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_SENSITIVE_DATA_MODEL Function

Downloads an already-generated file corresponding to the specified sensitive data model. Note that the GenerateSensitiveDataModelForDownload operation is a prerequisite for the DownloadSensitiveDataModel operation. Use GenerateSensitiveDataModelForDownload to generate a data model file and then use DownloadSensitiveDataModel to download the generated file.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`download_sensitive_data_model_details`

(required) Details to download a sensitive data model file.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DOWNLOAD_USER_ASSESSMENT_REPORT Function

Downloads the report of the specified user assessment. To download the user assessment report, it needs to be generated first. Please use GenerateUserAssessmentReport to generate a downloadable report in the preferred format (PDF, XLS).

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`download_user_assessment_report_details`

(required) Details of the report.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_DATA_SAFE_CONFIGURATION Function

Enables Data Safe in the tenancy and region.

Syntax
```

```

Parameters

Parameter Description

`enable_data_safe_configuration_details`

(required) The details used to enable Data Safe.

`compartment_id`

(optional) A filter to return only resources that match the specified compartment OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_DISCOVERY_REPORT_FOR_DOWNLOAD Function

Generates a downloadable discovery report. It's a prerequisite for the DownloadDiscoveryReport operation. Use this endpoint to generate a discovery report file and then use DownloadDiscoveryReport to download the generated file. By default, it generates report for all the columns in a sensitive data model. Use the discoveryJobId attribute to generate report for a specific discovery job.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`generate_discovery_report_for_download_details`

(required) Details to generate a downloadable discovery report.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_MASKING_POLICY_FOR_DOWNLOAD Function

Generates a downloadable file corresponding to the specified masking policy. It's a prerequisite for the DownloadMaskingPolicy operation. Use this endpoint to generate a masking policy file and then use DownloadMaskingPolicy to download the generated file. Note that file generation and download are serial operations. The download operation can't be invoked while the generate operation is in progress.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`generate_masking_policy_for_download_details`

(required) Details to generate a masking policy file.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_MASKING_REPORT_FOR_DOWNLOAD Function

Generates a downloadable masking report. It's a prerequisite for the DownloadMaskingReport operation. Use this endpoint to generate a masking report file and then use DownloadMaskingReport to download the generated file.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`generate_masking_report_for_download_details`

(required) Details to generate a downloadable masking report.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_ON_PREM_CONNECTOR_CONFIGURATION Function

Creates and downloads the configuration of the specified on-premises connector.

Syntax
```

```

Parameters

Parameter Description

`generate_on_prem_connector_configuration_details`

(required) The details used to create and download on-premises connector's configuration.

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_REPORT Function

Generates a .xls or .pdf report based on parameters and report definition.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`generate_report_details`

(required) Details for report generation. It contains details such as PDF/XLS and filter parameters like audit event time limits, number of rows and target databases etc

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(dateGenerated ge '2021-12-18T01-00-26') and (ilmTarget eq 'dscs-target')

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_SECURITY_ASSESSMENT_REPORT Function

Generates the report of the specified security assessment. You can get the report in PDF or XLS format. After generating the report, use DownloadSecurityAssessmentReport to download it in the preferred format.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`generate_security_assessment_report_details`

(required) Details of the report.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD Function

Generates a downloadable file corresponding to the specified sensitive data model. It's a prerequisite for the DownloadSensitiveDataModel operation. Use this endpoint to generate a data model file and then use DownloadSensitiveDataModel to download the generated file. Note that file generation and download are serial operations. The download operation can't be invoked while the generate operation is in progress.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`generate_sensitive_data_model_for_download_details`

(required) Details to generate a sensitive data model file.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_SQL_FIREWALL_POLICY Function

Generates or appends to the SQL Firewall policy using the specified SQL collection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_USER_ASSESSMENT_REPORT Function

Generates the report of the specified user assessment. The report is available in PDF or XLS format. After generating the report, use DownloadUserAssessmentReport to download it in the preferred format.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`generate_user_assessment_report_details`

(required) Details of the report.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALERT Function

Gets the details of the specified alerts.

Syntax
```

```

Parameters

Parameter Description

`alert_id`

(required) The OCID of alert.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ALERT_POLICY Function

Gets the details of alert policy by its ID.

Syntax
```

```

Parameters

Parameter Description

`alert_policy_id`

(required) The OCID of the alert policy.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUDIT_ARCHIVE_RETRIEVAL Function

Gets the details of the specified archive retreival.

Syntax
```

```

Parameters

Parameter Description

`audit_archive_retrieval_id`

(required) OCID of the archive retrieval.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUDIT_POLICY Function

Gets a audit policy by identifier.

Syntax
```

```

Parameters

Parameter Description

`audit_policy_id`

(required) Unique audit policy identifier.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUDIT_PROFILE Function

Gets the details of audit profile resource and associated audit trails of the audit profile.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUDIT_TRAIL Function

Gets the details of audit trail.

Syntax
```

```

Parameters

Parameter Description

`audit_trail_id`

(required) The OCID of the audit trail.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPATIBLE_FORMATS_FOR_DATA_TYPES Function

Gets a list of basic masking formats compatible with the supported data types. The data types are grouped into the following categories - Character - Includes CHAR, NCHAR, VARCHAR2, and NVARCHAR2 Numeric - Includes NUMBER, FLOAT, RAW, BINARY_FLOAT, and BINARY_DOUBLE Date - Includes DATE and TIMESTAMP LOB - Includes BLOB, CLOB, and NCLOB All - Includes all the supported data types

Syntax
```

```

Parameters

Parameter Description

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPATIBLE_FORMATS_FOR_SENSITIVE_TYPES Function

Gets a list of library masking formats compatible with the existing sensitive types. For each sensitive type, it returns the assigned default masking format as well as the other library masking formats that have the sensitiveTypeIds attribute containing the OCID of the sensitive type.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_SAFE_CONFIGURATION Function

Gets the details of the Data Safe configuration.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) A filter to return only resources that match the specified compartment OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_SAFE_PRIVATE_ENDPOINT Function

Gets the details of the specified Data Safe private endpoint.

Syntax
```

```

Parameters

Parameter Description

`data_safe_private_endpoint_id`

(required) The OCID of the private endpoint.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATABASE_SECURITY_CONFIG Function

Gets a database security configuration by identifier.

Syntax
```

```

Parameters

Parameter Description

`database_security_config_id`

(required) The OCID of the database security configuration resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DIFFERENCE_COLUMN Function

Gets the details of the specified SDM Masking policy difference column.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`difference_column_key`

(required) The unique key that identifies the difference column.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DISCOVERY_JOB Function

Gets the details of the specified discovery job.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DISCOVERY_JOB_RESULT Function

Gets the details of the specified discovery result.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`result_key`

(required) The unique key that identifies the discovery result.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LIBRARY_MASKING_FORMAT Function

Gets the details of the specified library masking format.

Syntax
```

```

Parameters

Parameter Description

`library_masking_format_id`

(required) The OCID of the library masking format.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MASKING_COLUMN Function

Gets the details of the specified masking column.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`masking_column_key`

(required) The unique key that identifies the masking column. It's numeric and unique within a masking policy.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MASKING_POLICY Function

Gets the details of the specified masking policy.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MASKING_REPORT Function

Gets the details of the specified masking report.

Syntax
```

```

Parameters

Parameter Description

`masking_report_id`

(required) The OCID of the masking report.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ON_PREM_CONNECTOR Function

Gets the details of the specified on-premises connector.

Syntax
```

```

Parameters

Parameter Description

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROFILE Function

Lists the details of given profile available on the target. The GetProfile operation returns only the profiles in the specified 'userAssessmentId'. This does not include any subcompartments of the current compartment.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`profile_name`

(required) Profile name to get detailed information .

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPORT Function

Gets a report by identifier

Syntax
```

```

Parameters

Parameter Description

`report_id`

(required) Unique report identifier

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPORT_CONTENT Function

Downloads the specified report in the form of .xls or .pdf.

Syntax
```

```

Parameters

Parameter Description

`report_id`

(required) Unique report identifier

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_REPORT_DEFINITION Function

Gets the details of report definition specified by the identifier

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SDM_MASKING_POLICY_DIFFERENCE Function

Gets the details of the specified SDM Masking policy difference.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_ASSESSMENT Function

Gets the details of the specified security assessment.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_ASSESSMENT_COMPARISON Function

Gets the details of the comparison report for the security assessments submitted for comparison.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`comparison_security_assessment_id`

(required) The OCID of the security assessment baseline.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_POLICY Function

Gets a security policy by the specified OCID of the security policy resource.

Syntax
```

```

Parameters

Parameter Description

`security_policy_id`

(required) The OCID of the security policy resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_POLICY_DEPLOYMENT Function

Gets a security policy deployment by identifier.

Syntax
```

```

Parameters

Parameter Description

`security_policy_deployment_id`

(required) The OCID of the security policy deployment resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_POLICY_ENTRY_STATE Function

Gets a security policy entity states by identifier.

Syntax
```

```

Parameters

Parameter Description

`security_policy_deployment_id`

(required) The OCID of the security policy deployment resource.

`security_policy_entry_state_id`

(required) Unique security policy entry state identifier. The unique id for a given security policy entry state can be obtained from the list api by passing the OCID of the corresponding security policy deployment resource as the query parameter.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SENSITIVE_COLUMN Function

Gets the details of the specified sensitive column.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`sensitive_column_key`

(required) The unique key that identifies the sensitive column. It's numeric and unique within a sensitive data model.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SENSITIVE_DATA_MODEL Function

Gets the details of the specified sensitive data model.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SENSITIVE_TYPE Function

Gets the details of the specified sensitive type.

Syntax
```

```

Parameters

Parameter Description

`sensitive_type_id`

(required) The OCID of the sensitive type.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_COLLECTION Function

Gets a SQL collection by identifier.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SQL_FIREWALL_POLICY Function

Gets a SQL Firewall policy by identifier.

Syntax
```

```

Parameters

Parameter Description

`sql_firewall_policy_id`

(required) The OCID of the SQL Firewall policy resource.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_ALERT_POLICY_ASSOCIATION Function

Gets the details of target-alert policy association by its ID.

Syntax
```

```

Parameters

Parameter Description

`target_alert_policy_association_id`

(required) The OCID of the target-alert policy association.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_DATABASE Function

Returns the details of the specified Data Safe target database.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_ASSESSMENT Function

Gets a user assessment by identifier.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_ASSESSMENT_COMPARISON Function

Gets the details of the comparison report for the user assessments submitted for comparison.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`comparison_user_assessment_id`

(required) The OCID of the baseline user assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets the details of the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALERT_ANALYTICS Function

Returns the aggregation details of the alerts.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`time_started`

(optional) An optional filter to return audit events whose creation time in the database is greater than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(optional) An optional filter to return audit events whose creation time in the database is less than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`query_time_zone`

(optional) Default time zone is UTC if no time zone provided. The date-time considerations of the resource will be in accordance with the specified time zone.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'displayName', 'timeCreated'

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** | query=(timeCreated ge '2021-06-04T01-00-26') and (targetNames eq 'target_1') query=(featureDetails.userName eq \"user\") and (targetNames eq \"target_1\") Supported fields: severity status alertType targetIds targetNames operationTime lifecycleState displayName timeCreated timeUpdated featureDetails.* (* can be any field in nestedStrMap in Feature Attributes in Alert Summary. For example - userName,object,clientHostname,osUserName,clientIPs,clientId,commandText,commandParam,clientProgram,objectType,targetOwner)

`summary_field`

(optional) Specifies a subset of summarized fields to be returned in the response.

Allowed values are: 'alertType', 'targetIds', 'targetNames', 'alertSeverity', 'alertStatus', 'timeCreated', 'policyId', 'open', 'closed', 'critical', 'high', 'medium', 'low', 'alertcount'

`group_by`

(optional) A groupBy can only be used in combination with summaryField parameter. A groupBy value has to be a subset of the values mentioned in summaryField parameter.

Allowed values are: 'alertType', 'targetIds', 'targetNames', 'alertSeverity', 'alertStatus', 'timeCreated', 'policyId'

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALERT_POLICIES Function

Gets a list of all alert policies.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`alert_policy_id`

(optional) A filter to return policy by it's OCID.

`l_type`

(optional) An optional filter to return only alert policies of a certain type.

Allowed values are: 'AUDITING', 'SECURITY_ASSESSMENT', 'USER_ASSESSMENT'

`is_user_defined`

(optional) An optional filter to return only alert policies that are user-defined or not.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`lifecycle_state`

(optional) An optional filter to return only alert policies that have the given life-cycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort parameter may be provided.

Allowed values are: 'displayName', 'timeCreated'

`opc_request_id`

(optional) Unique identifier for the request.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALERT_POLICY_RULES Function

Lists the rules of the specified alert policy. The alert policy is said to be satisfied when all rules in the policy evaulate to true. If there are three rules: rule1,rule2 and rule3, the policy is satisfied if rule1 AND rule2 AND rule3 is True.

Syntax
```

```

Parameters

Parameter Description

`alert_policy_id`

(required) The OCID of the alert policy.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALERTS Function

Gets a list of all alerts.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`id`

(optional) A filter to return alert by it's OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'displayName', 'timeCreated'

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** | query=(timeCreated ge '2021-06-04T01-00-26') and (targetNames eq 'target_1') query=(featureDetails.userName eq \"user\") and (targetNames eq \"target_1\") Supported fields: severity status alertType targetIds targetNames operationTime lifecycleState displayName timeCreated timeUpdated featureDetails.* (* can be any field in nestedStrMap in Feature Attributes in Alert Summary. For example - userName,object,clientHostname,osUserName,clientIPs,clientId,commandText,commandParam,clientProgram,objectType,targetOwner)

`field`

(optional) Specifies a subset of fields to be returned in the response.

Allowed values are: 'id', 'displayName', 'alertType', 'targetIds', 'targetNames', 'severity', 'status', 'operationTime', 'operation', 'operationStatus', 'timeCreated', 'timeUpdated', 'policyId', 'lifecycleState'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_ARCHIVE_RETRIEVALS Function

Returns the list of audit archive retrieval.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`audit_archive_retrieval_id`

(optional) OCID of the archive retrieval.

`target_id`

(optional) The OCID of the target associated with the archive retrieval.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only resources that matches the specified lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'NEEDS_ATTENTION', 'FAILED', 'DELETING', 'DELETED', 'UPDATING'

`time_of_expiry`

(optional) The date time when retrieved archive data will be deleted from Data Safe and unloaded back into archival.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_EVENT_ANALYTICS Function

By default the ListAuditEventAnalytics operation will return all of the summary columns. To filter for a specific summary column, specify it in the `summaryField` query parameter. **Example:** /ListAuditEventAnalytics?summaryField=targetName&amp;summaryField=userName&amp;summaryField=clientHostname &amp;summaryField=dmls&amp;summaryField=privilegeChanges&amp;summaryField=ddls&amp;summaryField=loginFailure&amp;summaryField=loginSuccess &amp;summaryField=allRecord&amp;q=(auditEventTime ge \"2021-06-13T23:49:14\") /ListAuditEventAnalytics?timeStarted=2022-08-18T11:02:26.000Z&amp;timeEnded=2022-08-24T11:02:26.000Z This will give number of events grouped by periods. Period can be 1 day, 1 week, etc. /ListAuditEventAnalytics?summaryField=targetName&amp;groupBy=targetName This will give the number of events group by targetName. Only targetName summary column would be returned.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`limit`

(optional) For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(operationTime ge '2021-06-04T01-00-26') and (eventName eq 'LOGON')

`summary_field`

(optional) Specifies a subset of summarized fields to be returned in the response.

Allowed values are: 'auditEventTime', 'dbUserName', 'targetId', 'targetName', 'targetClass', 'objectType', 'clientHostname', 'clientProgram', 'clientId', 'auditType', 'eventName', 'allRecord', 'auditSettingsChange', 'dbSchemaChange', 'entitlementChange', 'loginFailure', 'loginSuccess', 'allViolations', 'realmViolations', 'ruleViolations', 'dvconfigActivities', 'ddls', 'dmls', 'privilegeChanges', 'auditSettingsEnables', 'auditSettingsDisables', 'selects', 'creates', 'alters', 'drops', 'grants', 'revokes'

`time_started`

(optional) An optional filter to return audit events whose creation time in the database is greater than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(optional) An optional filter to return audit events whose creation time in the database is less than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`query_time_zone`

(optional) Default time zone is UTC if no time zone provided. The date-time considerations of the resource will be in accordance with the specified time zone.

`group_by`

(optional) A groupBy can only be used in combination with summaryField parameter. A groupBy value has to be a subset of the values mentioned in summaryField parameter.

Allowed values are: 'auditEventTime', 'dbUserName', 'targetId', 'targetName', 'targetClass', 'objectType', 'clientHostname', 'clientProgram', 'clientId', 'auditType', 'eventName'

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If this query parameter is specified, the result is ordered based on this query parameter value.

Allowed values are: 'targetId', 'targetClass', 'targetName', 'objectType', 'dbUserName', 'eventName', 'auditEventTime', 'clientHostname', 'clientProgram', 'clientId', 'auditType'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_EVENTS Function

The ListAuditEvents operation returns specified `compartmentId` audit Events only. The list does not include any audit Events associated with the `subcompartments` of the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListAuditEvents on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(operationTime ge '2021-06-04T01-00-26') and (eventName eq 'LOGON')

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If this query parameter is specified, the result is sorted by this query parameter value.

Allowed values are: 'dbUserName', 'targetName', 'databaseType', 'targetClass', 'auditEventTime', 'timeCollected', 'osUserName', 'operation', 'operationStatus', 'eventName', 'errorCode', 'errorMessage', 'objectType', 'objectName', 'objectOwner', 'clientHostname', 'clientIp', 'isAlerted', 'actionTaken', 'clientProgram', 'commandText', 'commandParam', 'extendedEventAttributes', 'auditLocation', 'osTerminal', 'clientId', 'auditPolicies', 'auditType'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_POLICIES Function

Retrieves a list of all audited targets with their corresponding provisioned audit policies, and their provisioning conditions. The ListAuditPolicies operation returns only the audit policies in the specified `compartmentId`. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListAuditPolicies on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`lifecycle_state`

(optional) The current state of the audit policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'FAILED', 'NEEDS_ATTENTION', 'DELETING', 'DELETED'

`audit_policy_id`

(optional) An optional filter to return only resources that match the specified id.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_POLICY_ANALYTICS Function

Gets a list of aggregated audit policy details on the target databases. A audit policy aggregation helps understand the overall state of policies provisioned on targets. It is especially useful to create dashboards or to support analytics. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform SummarizedAuditPolicyInfo on the specified `compartmentId` and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. **Example:** ListAuditPolicyAnalytics?groupBy=auditPolicyCategory

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`group_by`

(optional) The group by parameter to summarize audit policy aggregation.

Allowed values are: 'auditPolicyCategory', 'auditPolicyName', 'targetId'

`audit_policy_category`

(optional) The category to which the audit policy belongs to.

Allowed values are: 'BASIC_ACTIVITY', 'ADMIN_USER_ACTIVITY', 'USER_ACTIVITY', 'ORACLE_PREDEFINED', 'COMPLIANCE_STANDARD', 'CUSTOM', 'SQL_FIREWALL_AUDITING'

`audit_policy_name`

(optional) In case of seeded policies, it is the policy name defined by Data Safe. In case of custom Policies, it is the policy name that is used to create the policies on the target database. In case of Oracle Pre-seeded policies, it is the default policy name of the same.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`lifecycle_state`

(optional) The current state of the audit policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'FAILED', 'NEEDS_ATTENTION', 'DELETING', 'DELETED'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_PROFILE_ANALYTICS Function

Gets a list of audit profile aggregated details . A audit profile aggregation helps understand the overall state of audit profile profiles. As an example, it helps understand how many audit profiles have paid usage. It is especially useful to create dashboards or to support analytics. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform AuditProfileAnalytics on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`group_by`

(optional) The group by parameter for summarize operation on audit.

Allowed values are: 'isPaidUsageEnabled'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_PROFILES Function

Gets a list of all audit profiles. The ListAuditProfiles operation returns only the audit profiles in the specified `compartmentId`. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListAuditProfiles on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`audit_profile_id`

(optional) A optional filter to return only resources that match the specified id.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A optional filter to return only resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'FAILED', 'NEEDS_ATTENTION', 'DELETED'

`is_override_global_retention_setting`

(optional) A optional filter to return only resources that match the specified retention configured value.

`is_paid_usage_enabled`

(optional) Indicates if you want to continue audit record collection beyond the free limit of one million audit records per month per target database, incurring additional charges. The default value is inherited from the global settings. You can change at the global level or at the target level.

`audit_collected_volume_greater_than_or_equal_to`

(optional) A filter to return only items that have count of audit records collected greater than or equal to the specified value.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_TRAIL_ANALYTICS Function

Gets a list of audit trail aggregated details . A audit trail aggregation helps understand the overall state of trails. As an example, it helps understand how many trails are running or stopped. It is especially useful to create dashboards or to support analytics. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform AuditTrailAnalytics on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`group_by`

(optional) The group by parameter for summarize operation on audit trail.

Allowed values are: 'location', 'lifecycleState', 'status', 'targetId'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUDIT_TRAILS Function

Gets a list of all audit trails. The ListAuditTrails operation returns only the audit trails in the specified `compartmentId`. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListAuditTrails on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`audit_trail_id`

(optional) A optional filter to return only resources that match the specified id.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A optional filter to return only resources that match the specified lifecycle state.

Allowed values are: 'INACTIVE', 'UPDATING', 'ACTIVE', 'DELETING', 'FAILED', 'NEEDS_ATTENTION'

`status`

(optional) A optional filter to return only resources that match the specified sub-state of audit trail.

Allowed values are: 'STARTING', 'COLLECTING', 'RECOVERING', 'IDLE', 'STOPPING', 'STOPPED', 'RESUMING', 'RETRYING', 'NOT_STARTED', 'STOPPED_NEEDS_ATTN', 'STOPPED_FAILED'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABLE_AUDIT_VOLUMES Function

Retrieves a list of audit trails, and associated audit event volume for each trail up to defined start date.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`work_request_id`

(required) The OCID of the work request.

`trail_location`

(optional) The audit trail location.

`month_in_consideration_greater_than`

(optional) Specifying `monthInConsiderationGreaterThan` parameter will retrieve all items for which the event month is greater than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T00:00:00.000Z

`month_in_consideration_less_than`

(optional) Specifying `monthInConsiderationLessThan` parameter will retrieve all items for which the event month is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T00:00:00.000Z

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order(sortOrder). The default order for all fields is ascending.

Allowed values are: 'monthInConsideration', 'volume', 'trailLocation'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COLLECTED_AUDIT_VOLUMES Function

Gets a list of all collected audit volume data points.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`work_request_id`

(required) The OCID of the work request.

`month_in_consideration_greater_than`

(optional) Specifying `monthInConsiderationGreaterThan` parameter will retrieve all items for which the event month is greater than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T00:00:00.000Z

`month_in_consideration_less_than`

(optional) Specifying `monthInConsiderationLessThan` parameter will retrieve all items for which the event month is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T00:00:00.000Z

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order(sortOrder). The default order for all fields is ascending.

Allowed values are: 'monthInConsideration', 'onlineVolume', 'archivedVolume'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COLUMNS Function

Returns a list of column metadata objects.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`schema_name`

(optional) A filter to return only items related to specific schema name.

`table_name`

(optional) A filter to return only items related to specific table name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`datatype`

(optional) A filter to return only items related to specific datatype.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified.

Allowed values are: 'SCHEMANAME', 'TABLENAME', 'COLUMNNAME', 'DATATYPE'

`schema_name_contains`

(optional) A filter to return only items if schema name contains a specific string.

`table_name_contains`

(optional) A filter to return only items if table name contains a specific string.

`column_name_contains`

(optional) A filter to return only items if column name contains a specific string.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_SAFE_PRIVATE_ENDPOINTS Function

Gets a list of Data Safe private endpoints.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`vcn_id`

(optional) A filter to return only resources that match the specified VCN OCID.

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NA'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATABASE_SECURITY_CONFIGS Function

Retrieves a list of all database security configurations in Data Safe. The ListDatabaseSecurityConfigs operation returns only the database security configurations in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListDatabaseSecurityConfigs on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the database security configuration.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'FAILED', 'NEEDS_ATTENTION', 'DELETING', 'DELETED'

`database_security_config_id`

(optional) An optional filter to return only resources that match the specified OCID of the database security configuration resource.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DIFFERENCE_COLUMNS Function

Gets a list of columns of a SDM masking policy difference resource based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`difference_type`

(optional) A filter to return only the SDM masking policy difference columns that match the specified difference type

`planned_action`

(optional) A filter to return only the SDM masking policy difference columns that match the specified planned action.

`sync_status`

(optional) A filter to return the SDM masking policy difference columns based on the value of their syncStatus attribute.

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for schemaName is descending. The default order for differenceType, schemaName, objectName, columnName and plannedAction is ascending.

Allowed values are: 'differenceType', 'schemaName', 'objectName', 'columnName', 'plannedAction'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_ANALYTICS Function

Gets consolidated discovery analytics data based on the specified query parameters. If CompartmentIdInSubtreeQueryParam is specified as true, the behaviour is equivalent to accessLevel \"ACCESSIBLE\" by default.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`group_by`

(optional) Attribute by which the discovery analytics data should be grouped.

Allowed values are: 'targetId', 'sensitiveDataModelId', 'sensitiveTypeId', 'targetIdAndSensitiveDataModelId', 'sensitiveTypeIdAndTargetId', 'sensitiveTypeIdAndSensitiveDataModelId'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`sensitive_data_model_id`

(optional) A filter to return only the resources that match the specified sensitive data model OCID.

`sensitive_type_id`

(optional) A filter to return only items related to a specific sensitive type OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`is_common`

(optional) A filter to return only the common sensitive type resources. Common sensitive types belong to library sensitive types which are frequently used to perform sensitive data discovery.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_JOB_RESULTS Function

Gets a list of discovery results based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`discovery_type`

(optional) A filter to return only the resources that match the specified discovery type.

`planned_action`

(optional) A filter to return only the resources that match the specified planned action.

`is_result_applied`

(optional) A filter to return the discovery result resources based on the value of their isResultApplied attribute.

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeFinished is descending. The default order for discoveryType, schemaName, objectName, columnName and plannedAction is ascending.

Allowed values are: 'discoveryType', 'timeFinished', 'schemaName', 'objectName', 'columnName', 'plannedAction'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DISCOVERY_JOBS Function

Gets a list of incremental discovery jobs based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`discovery_job_id`

(optional) A filter to return only the resources that match the specified discovery job OCID.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`sensitive_data_model_id`

(optional) A filter to return only the resources that match the specified sensitive data model OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeFinished is descending. The default order for displayName is ascending.

Allowed values are: 'timeStarted', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FINDINGS Function

List all the findings from all the targets in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`opc_request_id`

(optional) Unique identifier for the request.

`severity`

(optional) A filter to return only findings of a particular risk level.

Allowed values are: 'HIGH', 'MEDIUM', 'LOW', 'EVALUATE', 'ADVISORY', 'PASS'

`references`

(optional) An optional filter to return only findings that match the specified reference.

Allowed values are: 'STIG', 'CIS', 'GDPR'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`finding_key`

(optional) Each finding in security assessment has an associated key (think of key as a finding's name). For a given finding, the key will be the same across targets. The user can use these keys to filter the findings.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GRANTS Function

Gets a list of grants for a particular user in the specified user assessment. A user grant contains details such as the privilege name, type, category, and depth level. The depth level indicates how deep in the hierarchy of roles granted to roles a privilege grant is. The userKey in this operation is a system-generated identifier. Perform the operation ListUsers to get the userKey for a particular user.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`user_key`

(required) The unique user key. This is a system-generated identifier. ListUsers gets the user key for a user.

`grant_key`

(optional) A filter to return only items that match the specified user grant key.

`grant_name`

(optional) A filter to return only items that match the specified user grant name.

`privilege_type`

(optional) A filter to return only items that match the specified privilege grant type.

`privilege_category`

(optional) A filter to return only items that match the specified user privilege category.

`depth_level`

(optional) A filter to return only items that match the specified user grant depth level.

`depth_level_greater_than_or_equal_to`

(optional) A filter to return only items that are at a level greater than or equal to the specified user grant depth level.

`depth_level_less_than`

(optional) A filter to return only items that are at a level less than the specified user grant depth level.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order (sortOrder). The default order for grantName is ascending.

Allowed values are: 'grantName', 'grantType', 'privilegeCategory', 'depthLevel', 'key'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIBRARY_MASKING_FORMATS Function

Gets a list of library masking formats based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`library_masking_format_id`

(optional) A filter to return only the resources that match the specified library masking format OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'NEEDS_ATTENTION', 'FAILED'

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`library_masking_format_source`

(optional) A filter to return the library masking format resources based on the value of their source attribute.

Allowed values are: 'ORACLE', 'USER'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for displayName is ascending. The displayName sort order is case sensitive.

Allowed values are: 'displayName', 'timeCreated'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKED_COLUMNS Function

Gets a list of masked columns present in the specified masking report and based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`masking_report_id`

(required) The OCID of the masking report.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for all the fields is ascending.

Allowed values are: 'schemaName', 'objectName'

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`object_type`

(optional) A filter to return only items related to a specific object type.

Allowed values are: 'ALL', 'TABLE', 'EDITIONING_VIEW'

`masking_column_group`

(optional) A filter to return only the resources that match the specified masking column group.

`sensitive_type_id`

(optional) A filter to return only items related to a specific sensitive type OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_ANALYTICS Function

Gets consolidated masking analytics data based on the specified query parameters. If CompartmentIdInSubtreeQueryParam is specified as true, the behaviour is equivalent to accessLevel \"ACCESSIBLE\" by default.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`group_by`

(optional) Attribute by which the masking analytics data should be grouped.

Allowed values are: 'targetId', 'policyId'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`masking_policy_id`

(optional) A filter to return only the resources that match the specified masking policy OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_COLUMNS Function

Gets a list of masking columns present in the specified masking policy and based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for other fields is ascending.

Allowed values are: 'timeCreated', 'schemaName', 'objectName', 'dataType'

`masking_column_lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'NEEDS_ATTENTION', 'FAILED'

`data_type`

(optional) A filter to return only resources that match the specified data types.

Allowed values are: 'CHARACTER', 'DATE', 'LOB', 'NUMERIC'

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`object_type`

(optional) A filter to return only items related to a specific object type.

Allowed values are: 'ALL', 'TABLE', 'EDITIONING_VIEW'

`masking_column_group`

(optional) A filter to return only the resources that match the specified masking column group.

`sensitive_type_id`

(optional) A filter to return only items related to a specific sensitive type OCID.

`is_masking_enabled`

(optional) A filter to return the masking column resources based on the value of their isMaskingEnabled attribute. A value of true returns only those columns for which masking is enabled. A value of false returns only those columns for which masking is disabled. Omitting this parameter returns all the masking columns in a masking policy.

`is_seed_required`

(optional) A filter to return masking columns based on whether the assigned masking formats need a seed value for masking. A value of true returns those masking columns that are using Deterministic Encryption or Deterministic Substitution masking format.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`time_updated_greater_than_or_equal_to`

(optional) Search for resources that were updated after a specific date. Specifying this parameter corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated after the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`time_updated_less_than`

(optional) Search for resources that were updated before a specific date. Specifying this parameter corresponding `timeUpdatedLessThan` parameter will retrieve all resources updated before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_OBJECTS Function

Gets a list of masking objects present in the specified masking policy and based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order is ascending.

Allowed values are: 'schemaName', 'objectName', 'objectType'

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`object_type`

(optional) A filter to return only items related to a specific object type.

Allowed values are: 'ALL', 'TABLE', 'EDITIONING_VIEW'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_POLICIES Function

Gets a list of masking policies based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`masking_policy_id`

(optional) A filter to return only the resources that match the specified masking policy OCID.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'NEEDS_ATTENTION', 'FAILED'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for displayName is ascending. The displayName sort order is case sensitive.

Allowed values are: 'displayName', 'timeCreated'

`sensitive_data_model_id`

(optional) A filter to return only the resources that match the specified sensitive data model OCID.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_REPORTS Function

Gets a list of masking reports based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`masking_policy_id`

(optional) A filter to return only the resources that match the specified masking policy OCID.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeMaskingFinished is descending.

Allowed values are: 'timeMaskingFinished'

`opc_request_id`

(optional) Unique identifier for the request.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MASKING_SCHEMAS Function

Gets a list of masking schemas present in the specified masking policy and based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order is ascending.

Allowed values are: 'schemaName'

`schema_name`

(optional) A filter to return only items related to specific schema name.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ON_PREM_CONNECTORS Function

Gets a list of on-premises connectors.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`on_prem_connector_id`

(optional) A filter to return only the on-premises connector that matches the specified id.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`on_prem_connector_lifecycle_state`

(optional) A filter to return only on-premises connector resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROFILE_ANALYTICS Function

Gets a list of aggregated user profile details in the specified compartment. This provides information about the overall profiles available. For example, the user profile details include how many users have the profile assigned and do how many use password verification function. This data is especially useful content for dashboards or to support analytics. When you perform the ListProfileAnalytics operation, if the parameter compartmentIdInSubtree is set to \"true,\" and if the parameter accessLevel is set to ACCESSIBLE, then the operation returns compartments in which the requestor has INSPECT permissions on at least one resource, directly or indirectly (in subcompartments). If the operation is performed at the root compartment and the requestor does not have access to at least one subcompartment of the compartment specified by compartmentId, then \"Not Authorized\" is returned. The parameter compartmentIdInSubtree applies when you perform ListProfileAnalytics on the compartmentId passed and when it is set to true, the entire hierarchy of compartments can be returned. To use ListProfileAnalytics to get a full list of all compartments and subcompartments in the tenancy from the root compartment, set the parameter compartmentIdInSubtree to true and accessLevel to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`profile_name`

(optional) A filter to return only items that match the specified profile name.

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROFILE_SUMMARIES Function

Gets a list of user profiles containing the profile details along with the target id and user counts. The ListProfiles operation returns only the profiles belonging to a certain target. If compartment type user assessment id is provided, then profile information for all the targets belonging to the pertaining compartment is returned. The list does not include any subcompartments of the compartment under consideration. The parameter 'accessLevel' specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when 'compartmentIdInSubtree' is set to 'true'. The parameter 'compartmentIdInSubtree' applies when you perform ListUserProfiles on the 'compartmentId' belonging to the assessmentId passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter 'compartmentIdInSubtree' to true and 'accessLevel' to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`profile_name`

(optional) A filter to return only items that match the specified profile name.

`is_user_created`

(optional) An optional filter to return the user created profiles.

`password_verification_function`

(optional) An optional filter to filter the profiles based on password verification function.

`user_count_greater_than_or_equal`

(optional) An optional filter to return the profiles having user count greater than or equal to the provided value.

`user_count_less_than`

(optional) An optional filter to return the profiles having user count less than the provided value.

`failed_login_attempts_greater_than_or_equal`

(optional) An optional filter to return the profiles having allow failed login attempts number greater than or equal to the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`failed_login_attempts_less_than`

(optional) An optional filter to return the profiles having failed login attempts number less than the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`sessions_per_user_greater_than_or_equal`

(optional) An optional filter to return the profiles permitting the user to spawn multiple sessions having count. greater than or equal to the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`sessions_per_user_less_than`

(optional) An optional filter to return the profiles permitting the user to spawn multiple sessions having count less than the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`inactive_account_time_greater_than_or_equal`

(optional) An optional filter to return the profiles allowing inactive account time in days greater than or equal to the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`inactive_account_time_less_than`

(optional) An optional filter to return the profiles allowing inactive account time in days less than the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`password_lock_time_greater_than_or_equal`

(optional) An optional filter to return the profiles having password lock number greater than or equal to the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`password_lock_time_less_than`

(optional) An optional filter to return the profiles having password lock number less than the provided value. String value is used for accommodating the \"UNLIMITED\" and \"DEFAULT\" values.

`sort_by`

(optional) The field to sort by. You can specify only one sort order (sortOrder). The default order is targetId ASC.

Allowed values are: 'profileName', 'targetId', 'isUserCreated', 'passwordVerificationFunction', 'userCount', 'sessionsPerUser', 'inactiveAccountTime', 'passwordLockTime', 'failedLoginAttempts'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPORT_DEFINITIONS Function

Gets a list of report definitions. The ListReportDefinitions operation returns only the report definitions in the specified `compartmentId`. It also returns the seeded report definitions which are available to all the compartments.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) The name of the report definition to query.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting parameter order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'DISPLAYORDER'

`opc_request_id`

(optional) Unique identifier for the request.

`is_seeded`

(optional) A boolean flag indicating to list seeded report definitions. Set this parameter to get list of seeded report definitions.

`data_source`

(optional) Specifies the name of a resource that provides data for the report. For example alerts, events.

Allowed values are: 'EVENTS', 'ALERTS', 'VIOLATIONS', 'ALLOWED_SQL'

`lifecycle_state`

(optional) An optional filter to return only resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED'

`category`

(optional) An optional filter to return only resources that match the specified category.

Allowed values are: 'CUSTOM_REPORTS', 'SUMMARY', 'ACTIVITY_AUDITING'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REPORTS Function

Gets a list of all the reports in the compartment. It contains information such as report generation time.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) The name of the report definition to query.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeGenerated is descending. Default order for displayName is ascending. If no value is specified timeGenerated is default.

Allowed values are: 'timeGenerated', 'displayName'

`report_definition_id`

(optional) The ID of the report definition to filter the list of reports

`opc_request_id`

(optional) Unique identifier for the request.

`lifecycle_state`

(optional) An optional filter to return only resources that match the specified lifecycle state.

Allowed values are: 'UPDATING', 'ACTIVE'

`l_type`

(optional) An optional filter to return only resources that match the specified type.

Allowed values are: 'GENERATED', 'SCHEDULED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROLES Function

Returns a list of role metadata objects.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`role_name`

(optional) A filter to return only a specific role based on role name.

`is_oracle_maintained`

(optional) A filter to return roles based on whether they are maintained by oracle or not.

`authentication_type`

(optional) A filter to return roles based on authentication type.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified.

Allowed values are: 'ROLENAME'

`role_name_contains`

(optional) A filter to return only items if role name contains a specific string.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SCHEMAS Function

Returns list of schema.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`schema_name`

(optional) A filter to return only items related to specific schema name.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified.

Allowed values are: 'SCHEMANAME'

`is_oracle_maintained`

(optional) A filter to return only items related to specific type of schema.

`schema_name_contains`

(optional) A filter to return only items if schema name contains a specific string.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SDM_MASKING_POLICY_DIFFERENCES Function

Gets a list of SDM and masking policy difference resources based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`difference_access_level`

(optional) Valid value is ACCESSIBLE. Default is ACCESSIBLE. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment).

Allowed values are: 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`sensitive_data_model_id`

(optional) A filter to return only the resources that match the specified sensitive data model OCID.

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle states.

`masking_policy_id`

(optional) A filter to return only the resources that match the specified masking policy OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreationStarted is descending. The default order for displayName is ascending.

Allowed values are: 'timeCreationStarted', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_ASSESSMENTS Function

Gets a list of security assessments. The ListSecurityAssessments operation returns only the assessments in the specified `compartmentId`. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSecurityAssessments on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`l_type`

(optional) A filter to return only items that match the specified security assessment type.

Allowed values are: 'LATEST', 'SAVED', 'SAVE_SCHEDULE', 'COMPARTMENT'

`schedule_assessment_id`

(optional) The OCID of the security assessment of type SAVE_SCHEDULE.

`is_schedule_assessment`

(optional) A filter to return only security assessments of type save schedule.

`triggered_by`

(optional) A filter to return only security asessments that were created by either user or system.

Allowed values are: 'USER', 'SYSTEM'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`is_baseline`

(optional) A filter to return only the security assessments that are set as a baseline.

`sort_by`

(optional) The field to sort by. You can specify only one sort order(sortOrder). The default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName'

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'SUCCEEDED', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_POLICIES Function

Retrieves a list of all security policies in Data Safe. The ListSecurityPolicies operation returns only the security policies in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSecurityPolicies on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the security policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'FAILED', 'DELETING', 'DELETED'

`security_policy_id`

(optional) An optional filter to return only resources that match the specified OCID of the security policy resource.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_POLICY_DEPLOYMENTS Function

Retrieves a list of all security policy deployments in Data Safe. The ListSecurityPolicyDeployments operation returns only the security policy deployments in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSecurityPolicyDeployments on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the security policy deployment.

Allowed values are: 'CREATING', 'UPDATING', 'DEPLOYED', 'NEEDS_ATTENTION', 'FAILED', 'DELETING', 'DELETED'

`security_policy_deployment_id`

(optional) An optional filter to return only resources that match the specified OCID of the security policy deployment resource.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`security_policy_id`

(optional) An optional filter to return only resources that match the specified OCID of the security policy resource.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_POLICY_ENTRY_STATES Function

Retrieves a list of all security policy entry states in Data Safe. The ListSecurityPolicyEntryStates operation returns only the security policy entry states for the specified security policy entry.

Syntax
```

```

Parameters

Parameter Description

`security_policy_deployment_id`

(required) The OCID of the security policy deployment resource.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`deployment_status`

(optional) The current state of the security policy deployment.

Allowed values are: 'CREATED', 'MODIFIED', 'CONFLICT', 'UNAUTHORIZED', 'DELETED'

`security_policy_entry_id`

(optional) An optional filter to return only resources that match the specified security policy entry OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENSITIVE_COLUMNS Function

Gets a list of sensitive columns present in the specified sensitive data model based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`time_updated_greater_than_or_equal_to`

(optional) Search for resources that were updated after a specific date. Specifying this parameter corresponding `timeUpdatedGreaterThanOrEqualTo` parameter will retrieve all resources updated after the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`time_updated_less_than`

(optional) Search for resources that were updated before a specific date. Specifying this parameter corresponding `timeUpdatedLessThan` parameter will retrieve all resources updated before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339.

`sensitive_column_lifecycle_state`

(optional) Filters the sensitive column resources with the given lifecycle state values.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED'

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`column_name`

(optional) A filter to return only a specific column based on column name.

`object_type`

(optional) A filter to return only items related to a specific object type.

Allowed values are: 'ALL', 'TABLE', 'EDITIONING_VIEW'

`data_type`

(optional) A filter to return only the resources that match the specified data types.

`status`

(optional) A filter to return only the sensitive columns that match the specified status.

Allowed values are: 'VALID', 'INVALID'

`sensitive_type_id`

(optional) A filter to return only the sensitive columns that are associated with one of the sensitive types identified by the specified OCIDs.

`parent_column_key`

(optional) A filter to return only the sensitive columns that are children of one of the columns identified by the specified keys.

`relation_type`

(optional) A filter to return sensitive columns based on their relationship with their parent columns. If set to NONE, it returns the sensitive columns that do not have any parent. The response includes the parent columns as well as the independent columns that are not in any relationship. If set to APP_DEFINED, it returns all the child columns that have application-level (non-dictionary) relationship with their parents. If set to DB_DEFINED, it returns all the child columns that have database-level (dictionary-defined) relationship with their parents.

Allowed values are: 'NONE', 'APP_DEFINED', 'DB_DEFINED'

`column_group`

(optional) A filter to return only the sensitive columns that belong to the specified column group.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for schemaName, objectName, and columnName is ascending.

Allowed values are: 'timeCreated', 'schemaName', 'objectName', 'columnName', 'dataType'

`opc_request_id`

(optional) Unique identifier for the request.

`is_case_in_sensitive`

(optional) A boolean flag indicating whether the search should be case-insensitive. The search is case-sensitive by default. Set this parameter to true to do case-insensitive search.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENSITIVE_DATA_MODELS Function

Gets a list of sensitive data models based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`sensitive_data_model_id`

(optional) A filter to return only the resources that match the specified sensitive data model OCID.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENSITIVE_OBJECTS Function

Gets a list of sensitive objects present in the specified sensitive data model based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`schema_name`

(optional) A filter to return only items related to specific schema name.

`object_name`

(optional) A filter to return only items related to a specific object name.

`object_type`

(optional) A filter to return only items related to a specific object type.

Allowed values are: 'ALL', 'TABLE', 'EDITIONING_VIEW'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order is ascending.

Allowed values are: 'schemaName', 'objectName', 'objectType'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENSITIVE_SCHEMAS Function

Gets a list of sensitive schemas present in the specified sensitive data model based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`schema_name`

(optional) A filter to return only items related to specific schema name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order is ascending.

Allowed values are: 'schemaName'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENSITIVE_TYPES Function

Gets a list of sensitive types based on the specified query parameters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`sensitive_type_id`

(optional) A filter to return only items related to a specific sensitive type OCID.

`sensitive_type_source`

(optional) A filter to return the sensitive type resources based on the value of their source attribute.

Allowed values are: 'ORACLE', 'USER'

`entity_type`

(optional) A filter to return the sensitive type resources based on the value of their entityType attribute.

Allowed values are: 'SENSITIVE_TYPE', 'SENSITIVE_CATEGORY'

`parent_category_id`

(optional) A filter to return only the sensitive types that are children of the sensitive category identified by the specified OCID.

`default_masking_format_id`

(optional) A filter to return only the sensitive types that have the default masking format identified by the specified OCID.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sorting parameter (sortOrder). The default order for timeCreated is descending. The default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) A filter to return only the resources that match the specified lifecycle state.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`is_common`

(optional) A filter to return only the common sensitive type resources. Common sensitive types belong to library sensitive types which are frequently used to perform sensitive data discovery.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_COLLECTION_ANALYTICS Function

Retrieves a list of all SQL collection analytics in Data Safe. The ListSqlCollectionAnalytics operation returns only the analytics for the SQL collections in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSqlCollections on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the SQL collection.

Allowed values are: 'CREATING', 'UPDATING', 'COLLECTING', 'COMPLETED', 'INACTIVE', 'FAILED', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`group_by`

(optional) The group by parameter to summarize SQL collection aggregation.

Allowed values are: 'targetId', 'lifecycleState'

`time_started`

(optional) An optional filter to return the stats of the SQL collection logs collected after the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(optional) An optional filter to return the stats of the SQL collection logs collected before the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_COLLECTION_LOG_INSIGHTS Function

Retrieves a list of the SQL collection log analytics.

Syntax
```

```

Parameters

Parameter Description

`time_started`

(required) An optional filter to return the stats of the SQL collection logs collected after the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(required) An optional filter to return the stats of the SQL collection logs collected before the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`group_by`

(optional) The group by parameter to summarize SQL collection log insights aggregation.

Allowed values are: 'clientIp', 'clientProgram', 'clientOsUserName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_COLLECTIONS Function

Retrieves a list of all SQL collections in Data Safe. The ListSqlCollections operation returns only the SQL collections in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSqlCollections on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the SQL collection.

Allowed values are: 'CREATING', 'UPDATING', 'COLLECTING', 'COMPLETED', 'INACTIVE', 'FAILED', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`sql_collection_id`

(optional) An optional filter to return only resources that match the specified OCID of the SQL collection resource.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`db_user_name`

(optional) A filter to return only items that match the specified user name.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting parameter order (sortOrder) can be specified. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME', 'TIMELASTSTARTED'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_ALLOWED_SQL_ANALYTICS Function

Returns the aggregation details of all SQL Firewall allowed SQL statements. The ListSqlFirewallAllowedSqlAnalytics operation returns the aggregates of the SQL Firewall allowed SQL statements in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSqlFirewallAllowedSqlAnalytics on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(currentUser eq 'SCOTT') and (topLevel eq 'YES')

`group_by`

(optional) The group by parameter to summarize the allowed SQL aggregation.

Allowed values are: 'dbUserName', 'sqlLevel', 'sqlFirewallPolicyId', 'lifecycleState'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_ALLOWED_SQLS Function

Retrieves a list of all SQL Firewall allowed SQL statements. The ListSqlFirewallAllowedSqls operation returns only the SQL Firewall allowed SQL statements in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSqlFirewallPolicies on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(currentUser eq 'SCOTT') and (topLevel eq 'YES')

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort parameter should be provided.

Allowed values are: 'displayName', 'timeCollected'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_POLICIES Function

Retrieves a list of all SQL Firewall policies. The ListSqlFirewallPolicies operation returns only the SQL Firewall policies in the specified `compartmentId`. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSqlFirewallPolicies on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`security_policy_id`

(optional) An optional filter to return only resources that match the specified OCID of the security policy resource.

`lifecycle_state`

(optional) The current state of the SQL Firewall policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'FAILED', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`sql_firewall_policy_id`

(optional) An optional filter to return only resources that match the specified OCID of the SQL Firewall policy resource.

`db_user_name`

(optional) A filter to return only items that match the specified user name.

`violation_action`

(optional) An optional filter to return only resources that match the specified violation action.

Allowed values are: 'block', 'observe'

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_POLICY_ANALYTICS Function

Gets a list of aggregated SQL Firewall policy details. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform SummarizedSqlFirewallPolicyInfo on the specified `compartmentId` and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`group_by`

(optional) The group by parameter to summarize SQL Firewall policy aggregation.

Allowed values are: 'violationAction', 'enforcementScope', 'securityPolicyId', 'lifecycleState'

`lifecycle_state`

(optional) The current state of the SQL Firewall policy.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'FAILED', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`security_policy_id`

(optional) An optional filter to return only resources that match the specified OCID of the security policy resource.

`time_started`

(optional) An optional filter to return the summary of the SQL Firewall policies created after the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(optional) An optional filter to return the summary of the SQL Firewall policies created before the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_VIOLATION_ANALYTICS Function

Returns the aggregation details of the SQL Firewall violations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`time_started`

(optional) An optional filter to return audit events whose creation time in the database is greater than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_ended`

(optional) An optional filter to return audit events whose creation time in the database is less than and equal to the date-time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`query_time_zone`

(optional) Default time zone is UTC if no time zone provided. The date-time considerations of the resource will be in accordance with the specified time zone.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If this query parameter is specified, the result is sorted by this query parameter value.

Allowed values are: 'dbUserName', 'targetId', 'targetName', 'operationTime', 'timeCollected', 'clientOsUserName', 'operation', 'currentDbUserName', 'sqlLevel', 'clientIp', 'clientProgram', 'violationCause', 'violationAction', 'violationCount'

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(operationTime ge '2021-06-04T01-00-26') and (violationAction eq 'BLOCKED')

`summary_field`

(optional) Specifies a subset of summarized fields to be returned in the response.

Allowed values are: 'dbUserName', 'targetName', 'clientOsUserName', 'operation', 'sqlText', 'currentDbUserName', 'sqlLevel', 'clientIp', 'clientProgram', 'violationCause', 'violationAction', 'selects', 'creates', 'alters', 'drops', 'grants', 'revokes'

`group_by`

(optional) A groupBy can only be used in combination with summaryField parameter. A groupBy value has to be a subset of the values mentioned in summaryField parameter.

Allowed values are: 'dbUserName', 'targetName', 'operationTime', 'timeCollected', 'clientOsUserName', 'operation', 'sqlText', 'currentDbUserName', 'sqlLevel', 'clientIp', 'clientProgram', 'violationCause', 'violationAction'

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SQL_FIREWALL_VIOLATIONS Function

Gets a list of all the SQL Firewall violations captured by the firewall.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique identifier for the request.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) If this query parameter is specified, the result is sorted by this query parameter value.

Allowed values are: 'dbUserName', 'targetId', 'targetName', 'operationTime', 'timeCollected', 'clientOsUserName', 'operation', 'currentDbUserName', 'sqlLevel', 'clientIp', 'clientProgram', 'violationCause', 'violationAction'

`scim_query`

(optional) The scimQuery query parameter accepts filter expressions that use the syntax described in Section 3.2.2.2 of the System for Cross-Domain Identity Management (SCIM) specification, which is available at[RFC3339](https://tools.ietf.org/html/draft-ietf-scim-api-12). In SCIM filtering expressions, text, date, and time values must be enclosed in quotation marks, with date and time values using ISO-8601 format. (Numeric and boolean values should not be quoted.) **Example:** query=(operationTime ge '2021-06-04T01-00-26') and (violationAction eq 'BLOCKED')

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TABLES Function

Returns a list of table metadata objects.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`schema_name`

(optional) A filter to return only items related to specific schema name.

`table_name`

(optional) A filter to return only items related to specific table name.

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified.

Allowed values are: 'SCHEMANAME', 'TABLENAME'

`table_name_contains`

(optional) A filter to return only items if table name contains a specific string.

`schema_name_contains`

(optional) A filter to return only items if schema name contains a specific string.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_ALERT_POLICY_ASSOCIATIONS Function

Gets a list of all target-alert policy associations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`target_alert_policy_association_id`

(optional) A filter to return only items related to a specific target-alert policy association ID.

`alert_policy_id`

(optional) A filter to return policy by it's OCID.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`lifecycle_state`

(optional) An optional filter to return only alert policies that have the given life-cycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort parameter may be provided.

Allowed values are: 'DISPLAYNAME', 'TIMECREATED', 'TIMEUPDATED'

`opc_request_id`

(optional) Unique identifier for the request.

`time_created_greater_than_or_equal_to`

(optional) A filter to return only the resources that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_DATABASES Function

Returns the list of registered target databases in Data Safe.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`associated_resource_id`

(optional) A filter to return the target databases that are associated to the resource id passed in as a parameter value.

`target_database_id`

(optional) A filter to return the target database that matches the specified OCID.

`display_name`

(optional) A filter to return only resources that match the specified display name.

`lifecycle_state`

(optional) A filter to return only target databases that match the specified lifecycle state.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'NEEDS_ATTENTION', 'FAILED'

`database_type`

(optional) A filter to return only target databases that match the specified database type.

Allowed values are: 'DATABASE_CLOUD_SERVICE', 'AUTONOMOUS_DATABASE', 'INSTALLED_DATABASE'

`infrastructure_type`

(optional) A filter to return only target databases that match the specified infrastructure type.

Allowed values are: 'ORACLE_CLOUD', 'CLOUD_AT_CUSTOMER', 'ON_PREMISES', 'NON_ORACLE_CLOUD'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USER_ANALYTICS Function

Gets a list of aggregated user details from the specified user assessment. This provides information about the overall state. of database user security. For example, the user details include how many users have the DBA role and how many users are in the critical category. This data is especially useful content for dashboards or to support analytics. When you perform the ListUserAnalytics operation, if the parameter compartmentIdInSubtree is set to \"true,\" and if the parameter accessLevel is set to ACCESSIBLE, then the operation returns compartments in which the requestor has INSPECT permissions on at least one resource, directly or indirectly (in subcompartments). If the operation is performed at the root compartment and the requestor does not have access to at least one subcompartment of the compartment specified by compartmentId, then \"Not Authorized\" is returned. The parameter compartmentIdInSubtree applies when you perform ListUserAnalytics on the compartmentId passed and when it is set to true, the entire hierarchy of compartments can be returned. To use ListUserAnalytics to get a full list of all compartments and subcompartments in the tenancy from the root compartment, set the parameter compartmentIdInSubtree to true and accessLevel to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`user_category`

(optional) A filter to return only items that match the specified user category.

`user_key`

(optional) A filter to return only items that match the specified user key.

`account_status`

(optional) A filter to return only items that match the specified account status.

`authentication_type`

(optional) A filter to return only items that match the specified authentication type.

`user_name`

(optional) A filter to return only items that match the specified user name.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`time_last_login_greater_than_or_equal_to`

(optional) A filter to return users whose last login time in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_last_login_less_than`

(optional) A filter to return users whose last login time in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_user_created_greater_than_or_equal_to`

(optional) A filter to return users whose creation time in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_user_created_less_than`

(optional) A filter to return users whose creation time in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_password_last_changed_greater_than_or_equal_to`

(optional) A filter to return users whose last password change in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_password_last_changed_less_than`

(optional) A filter to return users whose last password change in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order (sortOrder). The default order for userName is ascending.

Allowed values are: 'userName', 'userCategory', 'accountStatus', 'timeLastLogin', 'targetId', 'timeUserCreated', 'authenticationType', 'timePasswordChanged'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USER_ASSESSMENTS Function

Gets a list of user assessments. The ListUserAssessments operation returns only the assessments in the specified `compartmentId`. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListUserAssessments on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`display_name`

(optional) A filter to return only resources that match the specified display name.

`schedule_user_assessment_id`

(optional) The OCID of the user assessment of type SAVE_SCHEDULE.

`is_schedule_assessment`

(optional) A filter to return only user assessments of type SAVE_SCHEDULE.

`is_baseline`

(optional) A filter to return only user assessments that are set as baseline.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`l_type`

(optional) A filter to return only items that match the specified assessment type.

Allowed values are: 'LATEST', 'SAVED', 'COMPARTMENT', 'SAVE_SCHEDULE'

`triggered_by`

(optional) A filter to return user assessments that were created by either the system or by a user only.

Allowed values are: 'USER', 'SYSTEM'

`time_created_greater_than_or_equal_to`

(optional) A filter to return only user assessments that were created after the specified date and time, as defined by[RFC3339](https://tools.ietf.org/html/rfc3339). Using timeCreatedGreaterThanOrEqualTo parameter retrieves all assessments created after that date. **Example:** 2016-12-19T16:39:57.600Z

`time_created_less_than`

(optional) Search for resources that were created before a specific date. Specifying this parameter corresponding `timeCreatedLessThan` parameter will retrieve all resources created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by RFC 3339. **Example:** 2016-12-19T16:39:57.600Z

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`lifecycle_state`

(optional) The current state of the user assessment.

Allowed values are: 'CREATING', 'SUCCEEDED', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order (sortOrder). The default order for timeCreated is descending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USERS Function

Gets a list of users of the specified user assessment. The result contains the database user details for each user, such as user type, account status, last login time, user creation time, authentication type, user profile, and the date and time of the latest password change. It also contains the user category derived from these user details as well as privileges granted to each user.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`user_category`

(optional) A filter to return only items that match the specified user category.

`user_role`

(optional) A filter to return only items that match the specified user role.

`user_profile`

(optional) A filter to return only items that match the specified user profile.

`user_type`

(optional) A filter to return only items that match the specified user type. The possible values can be - ADMIN_PRIVILEGED - APPLICATION - PRIVILEGED - SCHEMA - NON_PRIVILEGED as specified by '#/definitions/userTypes'.

`user_key`

(optional) A filter to return only items that match the specified user key.

`account_status`

(optional) A filter to return only items that match the specified account status.

`authentication_type`

(optional) A filter to return only items that match the specified authentication type.

`user_name`

(optional) A filter to return only items that match the specified user name.

`target_id`

(optional) A filter to return only items related to a specific target OCID.

`time_last_login_greater_than_or_equal_to`

(optional) A filter to return users whose last login time in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_last_login_less_than`

(optional) A filter to return users whose last login time in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_user_created_greater_than_or_equal_to`

(optional) A filter to return users whose creation time in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_user_created_less_than`

(optional) A filter to return users whose creation time in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_password_last_changed_greater_than_or_equal_to`

(optional) A filter to return users whose last password change in the database is greater than or equal to the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`time_password_last_changed_less_than`

(optional) A filter to return users whose last password change in the database is less than the date and time specified, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339). **Example:** 2016-12-19T16:39:57.600Z

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_order`

(optional) The sort order to use, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can specify only one sort order (sortOrder). The default order for userName is ascending.

Allowed values are: 'userName', 'userCategory', 'accountStatus', 'timeLastLogin', 'targetId', 'timeUserCreated', 'authenticationType', 'timePasswordChanged'

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Gets a list of errors for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Gets a list of log entries for the specified work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Gets a list of work requests.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) A filter to return only resources that match the specified compartment OCID.

`operation_type`

(optional) A filter to return only work requests that match the specific operation type.

`sort_by`

(optional) The field used for sorting. Only one sorting parameter can be specified. The default order is descending.

Allowed values are: 'STARTTIME', 'FINISHTIME', 'ACCEPTEDTIME'

`sort_order`

(optional) The sorting order for the work requests, either ascending (ASC) or descending (DESC).

Allowed values are: 'ASC', 'DESC'

`resource_id`

(optional) A filter to return only work requests that match the specified resource OCID.

`target_database_id`

(optional) A filter to return only work requests that are associated to the specified target database OCID.

`opc_request_id`

(optional) Unique identifier for the request.

`page`

(optional) For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MASK_DATA Function

Masks data using the specified masking policy.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`mask_data_details`

(required) Details to mask data.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MODIFY_GLOBAL_SETTINGS Function

Modifies Global Settings in Data Safe in the tenancy and region.

Syntax
```

```

Parameters

Parameter Description

`modify_global_settings_details`

(required) The details used to update global settings in Data Safe.

`compartment_id`

(required) The OCID of the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_ALERTS Function

Updates the status of one or more alert specified by the alert IDs.

Syntax
```

```

Parameters

Parameter Description

`patch_alerts_details`

(required) The alert details to update the status of one or more alert specified by the alert IDs.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.

`access_level`

(optional) Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_DISCOVERY_JOB_RESULTS Function

Patches one or more discovery results. You can use this operation to set the plannedAction attribute before using ApplyDiscoveryJobResults to process the results based on this attribute.

Syntax
```

```

Parameters

Parameter Description

`discovery_job_id`

(required) The OCID of the discovery job.

`patch_discovery_job_result_details`

(required) Details to patch discovery results.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_MASKING_COLUMNS Function

Patches one or more columns in the specified masking policy. Use it to create, or update masking columns. To create masking columns, use CreateMaskingColumnDetails as the patch value. And to update masking columns, use UpdateMaskingColumnDetails as the patch value.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`patch_masking_columns_details`

(required) Details to patch masking columns.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_SDM_MASKING_POLICY_DIFFERENCE_COLUMNS Function

Patches one or more SDM masking policy difference columns. You can use this operation to set the plannedAction attribute before using ApplySdmMaskingPolicyDifference to process the difference based on this attribute.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`patch_sdm_masking_policy_difference_columns_details`

(required) Details to patch difference columns.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_SENSITIVE_COLUMNS Function

Patches one or more columns in the specified sensitive data model. Use it to create, update, or delete sensitive columns. To create sensitive columns, use CreateSensitiveColumnDetails as the patch value. And to update sensitive columns, use UpdateSensitiveColumnDetails as the patch value.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`patch_sensitive_column_details`

(required) Details to patch sensitive columns.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PATCH_TARGET_ALERT_POLICY_ASSOCIATION Function

Creates new target-alert policy associations that will be applied on the target database.

Syntax
```

```

Parameters

Parameter Description

`patch_target_alert_policy_association_details`

(required) The details used to patch the target-alert policy associations.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PROVISION_AUDIT_POLICY Function

Provision audit policy.

Syntax
```

```

Parameters

Parameter Description

`provision_audit_policy_details`

(required) Details for provisioning the given policies on the source target database.

`audit_policy_id`

(required) Unique audit policy identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PURGE_SQL_COLLECTION_LOGS Function

Purge the SQL collection logs for the specified SqlCollection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_DATABASE_SECURITY_CONFIGURATION Function

Refreshes the specified database security configuration.

Syntax
```

```

Parameters

Parameter Description

`database_security_config_id`

(required) The OCID of the database security configuration resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_SECURITY_ASSESSMENT Function

Runs a security assessment, refreshes the latest assessment, and saves it for future reference. The assessment runs with a securityAssessmentId of type LATEST. Before you start, first call the ListSecurityAssessments operation with filter \"type = latest\" to get the security assessment id for the target's latest assessment.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`run_security_assessment_details`

(required) Details to create an on-demand saved security assessment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_SQL_COLLECTION_LOG_INSIGHTS Function

Refresh the specified SQL collection Log Insights.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REFRESH_USER_ASSESSMENT Function

Refreshes the latest assessment and saves it for future reference. This operation runs with a userAssessmentId of type LATEST. Before you start, first call the ListUserAssessments operation with filter \"type = latest\" to get the user assessment ID for the target's latest assessment.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`run_user_assessment_details`

(required) The details required to create an on-demand saved user assessment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_SCHEDULE_REPORT Function

Deletes the schedule of a .xls or .pdf report.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESUME_AUDIT_TRAIL Function

Resumes the specified audit trail once it got stopped.

Syntax
```

```

Parameters

Parameter Description

`audit_trail_id`

(required) The OCID of the audit trail.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESUME_WORK_REQUEST Function

Resume the given work request. Issuing a resume does not guarantee of immediate resume of the work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RETRIEVE_AUDIT_POLICIES Function

Retrieves the audit policy details from the source target database.

Syntax
```

```

Parameters

Parameter Description

`audit_policy_id`

(required) Unique audit policy identifier.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SCHEDULE_REPORT Function

Schedules a .xls or .pdf report based on parameters and report definition.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`schedule_report_details`

(required) The details for the audit report schedule. It contains details such as schedule, MIME type .xls/.pdf and number of rows.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SET_SECURITY_ASSESSMENT_BASELINE Function

Sets the saved security assessment as the baseline in the compartment where the the specified assessment resides. The security assessment needs to be of type 'SAVED'.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`base_line_details`

(optional) Details of security assessment that need to be updated while setting the baseline.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SET_USER_ASSESSMENT_BASELINE Function

Sets the saved user assessment as the baseline in the compartment where the specified assessment resides. The user assessment needs to be of type 'SAVED'.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`base_line_details`

(optional) Details of user assessment that need to be updated while setting the baseline.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_AUDIT_TRAIL Function

Starts collection of audit records on the specified audit trail.

Syntax
```

```

Parameters

Parameter Description

`start_audit_trail_details`

(required) Details for the starting audit.

`audit_trail_id`

(required) The OCID of the audit trail.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### START_SQL_COLLECTION Function

Start the specified SQL collection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_AUDIT_TRAIL Function

Stops the specified audit trail.

Syntax
```

```

Parameters

Parameter Description

`audit_trail_id`

(required) The OCID of the audit trail.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### STOP_SQL_COLLECTION Function

Stops the specified SQL collection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUSPEND_WORK_REQUEST Function

Suspend the given work request. Issuing a suspend does not guarantee of a immediate suspend of the work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UNSET_SECURITY_ASSESSMENT_BASELINE Function

Removes the baseline setting for the saved security assessment. The saved security assessment is no longer considered a baseline. Sets the if-match parameter to the value of the etag from a previous GET or POST response for that resource.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UNSET_USER_ASSESSMENT_BASELINE Function

Removes the baseline setting for the saved user assessment. The saved user assessment is no longer considered a baseline. Sets the if-match parameter to the value of the etag from a previous GET or POST response for that resource.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ALERT Function

Updates the status of the specified alert.

Syntax
```

```

Parameters

Parameter Description

`alert_id`

(required) The OCID of alert.

`update_alert_details`

(required) The details used to update alert status.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUDIT_ARCHIVE_RETRIEVAL Function

Updates the audit archive retrieval.

Syntax
```

```

Parameters

Parameter Description

`audit_archive_retrieval_id`

(required) OCID of the archive retrieval.

`update_audit_archive_retrieval_details`

(required) Details to update the audit archive retrieval.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUDIT_POLICY Function

Updates the audit policy.

Syntax
```

```

Parameters

Parameter Description

`audit_policy_id`

(required) Unique audit policy identifier.

`update_audit_policy_details`

(required) Details to update the audit policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUDIT_PROFILE Function

Updates one or more attributes of the specified audit profile.

Syntax
```

```

Parameters

Parameter Description

`audit_profile_id`

(required) The OCID of the audit.

`update_audit_profile_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUDIT_TRAIL Function

Updates one or more attributes of the specified audit trail.

Syntax
```

```

Parameters

Parameter Description

`audit_trail_id`

(required) The OCID of the audit trail.

`update_audit_trail_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_SAFE_PRIVATE_ENDPOINT Function

Updates one or more attributes of the specified Data Safe private endpoint.

Syntax
```

```

Parameters

Parameter Description

`data_safe_private_endpoint_id`

(required) The OCID of the private endpoint.

`update_data_safe_private_endpoint_details`

(required) The details used to update a Data Safe private endpoint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATABASE_SECURITY_CONFIG Function

Updates the database security configuration.

Syntax
```

```

Parameters

Parameter Description

`database_security_config_id`

(required) The OCID of the database security configuration resource.

`update_database_security_config_details`

(required) Details to update the database security configuration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LIBRARY_MASKING_FORMAT Function

Updates one or more attributes of the specified library masking format. Note that updating the formatEntries attribute replaces all the existing masking format entries with the specified format entries.

Syntax
```

```

Parameters

Parameter Description

`library_masking_format_id`

(required) The OCID of the library masking format.

`update_library_masking_format_details`

(required) Details to update a library masking format.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MASKING_COLUMN Function

Updates one or more attributes of the specified masking column. Note that updating the maskingFormats attribute replaces the currently assigned masking formats with the specified masking formats.

Syntax
```

```

Parameters

Parameter Description

`masking_column_key`

(required) The unique key that identifies the masking column. It's numeric and unique within a masking policy.

`masking_policy_id`

(required) The OCID of the masking policy.

`update_masking_column_details`

(required) Details to update a masking column.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MASKING_POLICY Function

Updates one or more attributes of the specified masking policy.

Syntax
```

```

Parameters

Parameter Description

`masking_policy_id`

(required) The OCID of the masking policy.

`update_masking_policy_details`

(required) Details to update a masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ON_PREM_CONNECTOR Function

Updates one or more attributes of the specified on-premises connector.

Syntax
```

```

Parameters

Parameter Description

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`update_on_prem_connector_details`

(required) The details used to update a on-premises connector.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ON_PREM_CONNECTOR_WALLET Function

Updates the wallet for the specified on-premises connector to a new version.

Syntax
```

```

Parameters

Parameter Description

`update_on_prem_connector_wallet_details`

(required) The details used to update an on-premises connector's wallet.

`on_prem_connector_id`

(required) The OCID of the on-premises connector.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_REPORT_DEFINITION Function

Updates the specified report definition. Only user created report definition can be updated. Seeded report definitions need to be saved as new report definition first.

Syntax
```

```

Parameters

Parameter Description

`report_definition_id`

(required) Unique report definition identifier

`update_report_definition_details`

(required) Details for the modified report definition.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SDM_MASKING_POLICY_DIFFERENCE Function

Updates one or more attributes of the specified sdm masking policy difference.

Syntax
```

```

Parameters

Parameter Description

`sdm_masking_policy_difference_id`

(required) The OCID of the SDM masking policy difference.

`update_sdm_masking_policy_difference_details`

(required) Details to update a sdm masking policy difference.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_ASSESSMENT Function

Updates one or more attributes of the specified security assessment. This operation allows to update the security assessment displayName, description, or schedule.

Syntax
```

```

Parameters

Parameter Description

`security_assessment_id`

(required) The OCID of the security assessment.

`update_security_assessment_details`

(required) The information to be updated.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_POLICY Function

Updates the security policy.

Syntax
```

```

Parameters

Parameter Description

`security_policy_id`

(required) The OCID of the security policy resource.

`update_security_policy_details`

(required) Details to update the security policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_POLICY_DEPLOYMENT Function

Updates the security policy deployment.

Syntax
```

```

Parameters

Parameter Description

`security_policy_deployment_id`

(required) The OCID of the security policy deployment resource.

`update_security_policy_deployment_details`

(required) Details to update the security policy deployment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SENSITIVE_COLUMN Function

Updates one or more attributes of the specified sensitive column.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`sensitive_column_key`

(required) The unique key that identifies the sensitive column. It's numeric and unique within a sensitive data model.

`update_sensitive_column_details`

(required) Details to update a sensitive column.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SENSITIVE_DATA_MODEL Function

Updates one or more attributes of the specified sensitive data model. Note that updating any attribute of a sensitive data model does not perform data discovery.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`update_sensitive_data_model_details`

(required) Details to update a sensitive data model.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SENSITIVE_TYPE Function

Updates one or more attributes of the specified sensitive type.

Syntax
```

```

Parameters

Parameter Description

`sensitive_type_id`

(required) The OCID of the sensitive type.

`update_sensitive_type_details`

(required) Details to update a sensitive type.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SQL_COLLECTION Function

Updates the SQL collection.

Syntax
```

```

Parameters

Parameter Description

`sql_collection_id`

(required) The OCID of the SQL collection resource.

`update_sql_collection_details`

(required) Details to update the SQL collection.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SQL_FIREWALL_POLICY Function

Updates the SQL Firewall policy.

Syntax
```

```

Parameters

Parameter Description

`sql_firewall_policy_id`

(required) The OCID of the SQL Firewall policy resource.

`update_sql_firewall_policy_details`

(required) Details to update the SQL Firewall policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_ALERT_POLICY_ASSOCIATION Function

Updates the specified target-alert policy association.

Syntax
```

```

Parameters

Parameter Description

`target_alert_policy_association_id`

(required) The OCID of the target-alert policy association.

`update_target_alert_policy_association_details`

(required) The details used to update the target-alert policy association.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_DATABASE Function

Updates one or more attributes of the specified Data Safe target database.

Syntax
```

```

Parameters

Parameter Description

`target_database_id`

(required) The OCID of the Data Safe target database.

`update_target_database_details`

(required) Details used to update the target database in Data Safe.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USER_ASSESSMENT Function

Updates one or more attributes of the specified user assessment. This operation allows to update the user assessment displayName, description, or schedule.

Syntax
```

```

Parameters

Parameter Description

`user_assessment_id`

(required) The OCID of the user assessment.

`update_user_assessment_details`

(required) The information to be updated.

`opc_request_id`

(optional) Unique identifier for the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_MASKING_POLICY Function

Uploads a masking policy file (also called template) to update the specified masking policy. To create a new masking policy using a file, first use the CreateMaskingPolicy operation to create an empty masking policy and then use this endpoint to upload the masking policy file. Note that the upload operation replaces the content of the specified masking policy, including all the existing columns and masking formats, with the content of the file.

Syntax
```

```

Parameters

Parameter Description

`upload_masking_policy_details`

(required) Details to upload a masking policy file.

`masking_policy_id`

(required) The OCID of the masking policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_SENSITIVE_DATA_MODEL Function

Uploads a sensitive data model file (also called template) to update the specified sensitive data model. To create a new sensitive data model using a file, first use the CreateSensitiveDataModel operation to create an empty data model and then use this endpoint to upload the data model file. Note that the upload operation replaces the content of the specified sensitive data model, including all the existing columns and their relationships, with the content of the file.

Syntax
```

```

Parameters

Parameter Description

`sensitive_data_model_id`

(required) The OCID of the sensitive data model.

`upload_sensitive_data_model_details`

(required) Details to upload a sensitive data model file.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique identifier for the request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://datasafe.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Data Safe Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-35B38D67-EC16-4B03-9F2D-5D1A70CDF753)
- [ACTIVATE_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1944F120-EBAB-4CC2-AFB6-09EF9C729834)
- [ADD_MASKING_COLUMNS_FROM_SDM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-89318F5D-F90B-41BA-9F4A-E3BB96850C0C)
- [ALERTS_UPDATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E841C026-00C9-4606-AB27-1A75A9E7D42B)
- [APPLY_DISCOVERY_JOB_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-710ACE38-638A-4CED-8705-12923836A9E0)
- [APPLY_SDM_MASKING_POLICY_DIFFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5DCF8829-818F-451B-9528-03A7163F113C)
- [CALCULATE_AUDIT_VOLUME_AVAILABLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-DF4CFC96-132D-45A9-842F-59F2194EDF54)
- [CALCULATE_AUDIT_VOLUME_COLLECTED Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0AB5E3CD-8C43-427C-8CE6-ABC1A8DB7483)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-41BFED10-E17C-4341-9734-37A38DA05D32)
- [CHANGE_ALERT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C577B8D2-944A-4477-895D-7109F2B6977F)
- [CHANGE_AUDIT_ARCHIVE_RETRIEVAL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-66B8E7E7-AFD2-408F-8B5D-433ED14A1CEA)
- [CHANGE_AUDIT_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E89CCAD6-154F-4745-A074-96BAAA835B59)
- [CHANGE_AUDIT_PROFILE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2851D9CE-283F-48E5-9579-7A44DF736ECD)
- [CHANGE_DATA_SAFE_PRIVATE_ENDPOINT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E7B6326C-C639-477B-A1B0-968F4E05D14E)
- [CHANGE_DATABASE_SECURITY_CONFIG_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B746A3DF-C35E-46F0-8EDD-A2B4119198EC)
- [CHANGE_DISCOVERY_JOB_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-58C07354-657B-4ED4-9F6B-8791E67D8D87)
- [CHANGE_LIBRARY_MASKING_FORMAT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7E02E6A2-8014-4DC2-9D35-796B7276C325)
- [CHANGE_MASKING_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C8C687FB-E663-4703-B17E-B78D1447B0C7)
- [CHANGE_ON_PREM_CONNECTOR_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5A102D19-CEFE-46A8-923B-31CC94287F42)
- [CHANGE_REPORT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FEA706BA-9C9E-4008-B9E7-29318A57A587)
- [CHANGE_REPORT_DEFINITION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C230B229-3C15-4AC2-84F8-3D4AD8BB170C)
- [CHANGE_RETENTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FD93B965-F571-499A-9DB9-8B9BC15F74D6)
- [CHANGE_SDM_MASKING_POLICY_DIFFERENCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-15343CBC-B146-457B-8ED0-65A26A35EB68)
- [CHANGE_SECURITY_ASSESSMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8C6BE05B-D4C5-4A6D-8316-B0C927DBCC03)
- [CHANGE_SECURITY_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-EE44962D-1501-42CE-B83E-F80884609142)
- [CHANGE_SECURITY_POLICY_DEPLOYMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8A7777C5-587A-4024-9C4F-90BE38C402EC)
- [CHANGE_SENSITIVE_DATA_MODEL_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A69922DD-CD7E-41FA-AE98-8BF93279153D)
- [CHANGE_SENSITIVE_TYPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5995497E-3D77-431D-8549-63A7A3CF9DA9)
- [CHANGE_SQL_COLLECTION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C639DC28-8F68-4F7F-9AF2-811048E0A258)
- [CHANGE_SQL_FIREWALL_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9659BB9A-0007-4F72-AB1A-815CA0FB0C76)
- [CHANGE_TARGET_ALERT_POLICY_ASSOCIATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CCDC70D9-EFBA-4C10-A37C-DFAB21E20C1C)
- [CHANGE_TARGET_DATABASE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FEA6F2A1-F9ED-438A-9FFB-21986E07A02F)
- [CHANGE_USER_ASSESSMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A96CA7D7-FC3E-4A3E-91FC-06C05D38262A)
- [COMPARE_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C776D414-F08C-42FE-AEB7-FD79B91BC8FE)
- [COMPARE_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-15A324AA-3016-453A-9D7A-B7C8B7418EA0)
- [CREATE_AUDIT_ARCHIVE_RETRIEVAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-24CCD71C-093F-443E-8EC7-285A2ADB1BAA)
- [CREATE_DATA_SAFE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-150AE595-FCED-4E51-8BB8-3EB21E058E12)
- [CREATE_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-AB7EA03A-A1FE-43C3-9FF7-4B8DD61DA79B)
- [CREATE_LIBRARY_MASKING_FORMAT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9B15BF31-BEDE-4C1A-ACA5-95B3C0B726BF)
- [CREATE_MASKING_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4F5EDAA9-8EC3-49ED-8FB6-58267E3D119E)
- [CREATE_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9BB44174-14D2-46EF-BBDB-96087BC31A4B)
- [CREATE_ON_PREM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9AAD060C-8FB1-4E1D-9D3C-B4ABCC5C3BF3)
- [CREATE_REPORT_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B9423AC6-833D-425E-98C3-9724EE272A0F)
- [CREATE_SDM_MASKING_POLICY_DIFFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7A92F055-D4B6-4449-80E1-8AAF57012597)
- [CREATE_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-20DBC366-9251-42A9-B21F-814A91D18D66)
- [CREATE_SENSITIVE_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-195D39DC-CB9E-4B9C-9E3B-CA69BC7569DA)
- [CREATE_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-98BD71BC-FB2F-400C-8D74-6DCAAF01F678)
- [CREATE_SENSITIVE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FA9E51F4-6736-4DA2-979F-40D06ADFC0B6)
- [CREATE_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-29536C9C-4565-4A4B-A769-EA7D59C6C4FC)
- [CREATE_TARGET_ALERT_POLICY_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7CEEE650-9C49-4DEE-995A-3C549CA52125)
- [CREATE_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6C3300C6-5FDF-45D5-A4A2-82AED2A17C5B)
- [CREATE_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6F7A0D5B-2580-4AF7-85F0-21A9EC057393)
- [DEACTIVATE_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BDF0EC6B-94B2-4B20-B904-39B6F782445A)
- [DELETE_AUDIT_ARCHIVE_RETRIEVAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D4B57B3E-7DE8-4669-BAFC-70180C798573)
- [DELETE_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B6022DA8-AE35-4F5A-A4DB-190DACF22620)
- [DELETE_DATA_SAFE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-57598EB3-1A4B-46D2-975F-FB9AB1093C1A)
- [DELETE_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-24EE7F3B-3318-40E7-B4CF-C49CBCD560D3)
- [DELETE_DISCOVERY_JOB_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D8B021B7-FAD6-4BDD-9379-1EA1BB3C2413)
- [DELETE_LIBRARY_MASKING_FORMAT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-83F91092-25D6-42AD-9322-73433907E7DB)
- [DELETE_MASKING_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-87CFD1F3-763D-4958-AD3D-92D72F1B4BAD)
- [DELETE_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2DF98F25-69E0-46ED-B21A-D95093984FEC)
- [DELETE_ON_PREM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0E8E5D21-4546-4CB6-A9C6-269CA2EA330A)
- [DELETE_REPORT_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-569AC061-40E4-4795-A40A-EF338D7323ED)
- [DELETE_SDM_MASKING_POLICY_DIFFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A05570CA-2B72-405B-8422-6C813D11B695)
- [DELETE_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F346E1E9-E3C7-4716-B0BC-619839185D89)
- [DELETE_SENSITIVE_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9B74C2F7-45DF-41CD-8673-EDD6A11116EB)
- [DELETE_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-DD478FA2-F92C-4AB6-8782-FE6985346923)
- [DELETE_SENSITIVE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1572061B-46D2-4606-9670-809AE58F3CEC)
- [DELETE_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C951D84F-BBF3-4B6F-A148-E0D5CAC00484)
- [DELETE_SQL_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3AB70BF3-8355-469C-9CCE-0B46CE0C4819)
- [DELETE_TARGET_ALERT_POLICY_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B7540DD8-59EF-4F70-A69B-A1C36E087EED)
- [DELETE_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-47842009-A1CC-427A-95CA-DAEC7F6088E9)
- [DELETE_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2ABD775C-4741-4FCA-8C18-148BCDA2F413)
- [DISCOVER_AUDIT_TRAILS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0BD6A83C-9E0E-4E0F-8FF3-D8A7637ECDAC)
- [DOWNLOAD_DISCOVERY_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-866D4634-B702-4CAD-9B47-2304459F822F)
- [DOWNLOAD_MASKING_LOG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-73559E6D-ADC6-4CC3-A4F9-0A061EB97BA2)
- [DOWNLOAD_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-27AA6ED7-F8F7-4907-930A-156166E311A5)
- [DOWNLOAD_MASKING_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FB97FA5E-D149-4AB0-8B25-CF2B7E9F1574)
- [DOWNLOAD_PRIVILEGE_SCRIPT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8181992D-830C-4EF8-A35B-43F4278AD3E3)
- [DOWNLOAD_SECURITY_ASSESSMENT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E0336AA7-E782-484D-A217-BA95F5D56E4A)
- [DOWNLOAD_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2BEC27C9-5CA8-46EF-8F06-403F876F25D0)
- [DOWNLOAD_USER_ASSESSMENT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1343555D-6BDD-4A6D-A008-D4F1CE00F1E8)
- [ENABLE_DATA_SAFE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E5D8E100-4928-494D-9692-EB22FE4B79EB)
- [GENERATE_DISCOVERY_REPORT_FOR_DOWNLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B364C9E1-A32B-4380-8CA7-9FB2CAB20D02)
- [GENERATE_MASKING_POLICY_FOR_DOWNLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1D89FF39-B9ED-4B73-A3FD-8DD028B1A95C)
- [GENERATE_MASKING_REPORT_FOR_DOWNLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CACF4C19-9FAD-46E9-B316-13EE416A8019)
- [GENERATE_ON_PREM_CONNECTOR_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A9C3BECB-71CE-44B6-A8E0-7AEE8BAF2BE8)
- [GENERATE_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-925CBB76-3DC4-47A4-BDEF-E7CF1A0856CE)
- [GENERATE_SECURITY_ASSESSMENT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3479ACA7-E3E6-4065-8912-6AD2E03269F0)
- [GENERATE_SENSITIVE_DATA_MODEL_FOR_DOWNLOAD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-56B9E592-48E1-4796-96F5-86445D5EB412)
- [GENERATE_SQL_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-930F0F21-C964-4772-A53D-C72EF4CD320D)
- [GENERATE_USER_ASSESSMENT_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-296C59B8-5F18-46E6-83B2-2461CA4CF73F)
- [GET_ALERT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-119C2236-63A7-4AC0-BED6-A6728D320936)
- [GET_ALERT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BEA03138-D6B0-41AD-8351-1F1A28D58152)
- [GET_AUDIT_ARCHIVE_RETRIEVAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9E7AD345-F3ED-4BD7-8688-8D52A5ACB265)
- [GET_AUDIT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-350BF042-5E3C-40E6-8C66-3B299500627D)
- [GET_AUDIT_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3E62AD20-067F-4D41-A9F1-53A59FDB7193)
- [GET_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-857B7602-C8BB-475D-A325-6FF0AC7A10D1)
- [GET_COMPATIBLE_FORMATS_FOR_DATA_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8D124466-47DC-4F95-910D-FC67CA32768B)
- [GET_COMPATIBLE_FORMATS_FOR_SENSITIVE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9CA69586-1AFB-42BD-A823-C8952CF9245B)
- [GET_DATA_SAFE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-AC0C7A77-0406-49FF-B0DA-9C09BE7197CE)
- [GET_DATA_SAFE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9B7BA65E-E8AF-46EE-99F7-1DA8F8E8643F)
- [GET_DATABASE_SECURITY_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6F75742C-9740-46C5-86ED-7C04F92C8836)
- [GET_DIFFERENCE_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-02455757-A220-4DD8-9610-D30056B17148)
- [GET_DISCOVERY_JOB Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6A970F84-4E28-4B15-BA30-13F8A70E3929)
- [GET_DISCOVERY_JOB_RESULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E7E14A82-B6F8-4196-B3D5-9046FC1FF2D3)
- [GET_LIBRARY_MASKING_FORMAT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2DAD7B2D-B34E-479F-A02B-16B895FDB673)
- [GET_MASKING_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C93BFFCA-5EE4-471E-9529-7762E9DD8A91)
- [GET_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E97A19B2-8A6C-41D1-B0C5-D6A11B325444)
- [GET_MASKING_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-122BEBE9-C18F-49C2-AA13-709AEFA5B326)
- [GET_ON_PREM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D3213DB2-F3C3-4E7D-A952-099CAC56D614)
- [GET_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BBAF256F-9A88-4EFD-B951-A1BDB2DD3950)
- [GET_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E38D9EEC-AEE3-437A-814B-216AEB4260E1)
- [GET_REPORT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CE7FBC6C-8175-445F-B3F2-5E8F40ACA88E)
- [GET_REPORT_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F92D6ADA-BE68-4101-8964-AE329728A158)
- [GET_SDM_MASKING_POLICY_DIFFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C4BCE902-D7B2-4336-9E12-3008AC1D9B5E)
- [GET_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6F99DDB2-BCB0-4BD2-97A8-49BCF49D65A3)
- [GET_SECURITY_ASSESSMENT_COMPARISON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A80535F0-1427-493C-B6A1-1BE10AF1CA7C)
- [GET_SECURITY_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A50F7C45-8425-400D-8BB8-CE53A7274C6C)
- [GET_SECURITY_POLICY_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2906B133-879D-4AC1-B826-226DE8FFFBAB)
- [GET_SECURITY_POLICY_ENTRY_STATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-52E4C2E6-5C2D-457E-B1C3-C62EA2597734)
- [GET_SENSITIVE_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F099FB33-006D-4CE3-9063-423118E2A9BF)
- [GET_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2790C38B-4933-4200-B86A-C584FEF18AED)
- [GET_SENSITIVE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BCCEC95D-AFBA-4BFC-A718-0D6D9FF10563)
- [GET_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1C8606D6-674C-43B5-B855-5FF01E177937)
- [GET_SQL_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-710ACB25-C25B-4E9A-86EC-D9FCAD63E90B)
- [GET_TARGET_ALERT_POLICY_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-18BB6C30-5AAA-4A9B-B97D-035BD89AFD72)
- [GET_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8B01DA70-DF0F-4867-9D02-58A1004BB345)
- [GET_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D2455B6B-E489-416E-8EB1-032586B67EA4)
- [GET_USER_ASSESSMENT_COMPARISON Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-92818022-F491-413A-81E0-D6259EED2A23)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-127DBE60-97DA-4E01-BA18-D45C9F874913)
- [LIST_ALERT_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C7679D05-48BC-4F63-BC63-1853B8B07BF9)
- [LIST_ALERT_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B4AF0B69-D1E7-40AA-B615-43933E6E765A)
- [LIST_ALERT_POLICY_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A3B9907E-555C-412B-8D75-BB9AFF29F85E)
- [LIST_ALERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2A4A6B29-35FE-4832-8864-05F73314A524)
- [LIST_AUDIT_ARCHIVE_RETRIEVALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3E1902B5-6651-489A-A80F-4AA0C54D8512)
- [LIST_AUDIT_EVENT_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-262E0A67-F276-4580-9FE1-E20FB965BDE6)
- [LIST_AUDIT_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4CEACA14-4312-4D6A-9C43-E72FD812A224)
- [LIST_AUDIT_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-313B2E4B-2FE0-4F03-8066-9932C5EA7757)
- [LIST_AUDIT_POLICY_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-EF10EBC1-0CAD-4EFE-8C74-6838625F901A)
- [LIST_AUDIT_PROFILE_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0C0543F7-C27F-4791-B135-714A32C4664E)
- [LIST_AUDIT_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0CE58BFA-A66C-4156-AFB2-DBDF21EF6B33)
- [LIST_AUDIT_TRAIL_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-DB16F32B-F910-4DA8-8B64-61A754E05C1F)
- [LIST_AUDIT_TRAILS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-62601873-AA9F-4740-A53F-49F27A4D23C1)
- [LIST_AVAILABLE_AUDIT_VOLUMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-27B15038-9216-49BF-9695-839B73887D99)
- [LIST_COLLECTED_AUDIT_VOLUMES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6DC2D8B5-77FD-4B3D-947B-F803CFE3DC40)
- [LIST_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-ECD1A317-8580-4B9E-A162-40102AC867CF)
- [LIST_DATA_SAFE_PRIVATE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D9418139-D857-4E5A-9BD2-BCC2606FDF30)
- [LIST_DATABASE_SECURITY_CONFIGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9D71F622-C7EA-4E17-B831-3080A7BEBDE3)
- [LIST_DIFFERENCE_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8E8B5644-6B54-4FD9-AC64-6EFA80FEE27E)
- [LIST_DISCOVERY_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9B403A24-EDBE-46D1-A6EA-7A8701D1DF71)
- [LIST_DISCOVERY_JOB_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D9695F8D-D16A-459E-BF71-3DE907E377CB)
- [LIST_DISCOVERY_JOBS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D36F973D-F70D-4E6D-87C3-E0D52A33CA40)
- [LIST_FINDINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B411D436-1E24-46A4-A3E6-5E702AF62CE1)
- [LIST_GRANTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3520B111-0D9C-41D7-86AC-A71D2867B773)
- [LIST_LIBRARY_MASKING_FORMATS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-EFBB9641-6E97-4082-BC19-8C4E79BC44C9)
- [LIST_MASKED_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1DFE09A2-DBB3-4E6D-AFE8-29EC80419A9B)
- [LIST_MASKING_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4B0E315C-6112-4B93-B96A-F51F639FE252)
- [LIST_MASKING_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2C42137C-4FEB-46D5-8B9F-1DCA09247E78)
- [LIST_MASKING_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-71F04819-F4B3-46ED-B790-A24A0A8D9D66)
- [LIST_MASKING_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F0B184AF-03D8-45C8-909E-C1B229B2EF6C)
- [LIST_MASKING_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-8148335D-5560-4611-8EA8-CCCA267FEFB7)
- [LIST_MASKING_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FEB6C064-18DC-49D3-8A05-BA7783ADD45D)
- [LIST_ON_PREM_CONNECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-75917B7A-E375-4E62-97AA-C2C421B18AA4)
- [LIST_PROFILE_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4A5DD8C0-AA0D-4273-80CF-BFD1C0E54EF2)
- [LIST_PROFILE_SUMMARIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D76FDA2C-8C3C-49D0-9D25-13EC63B6F9EB)
- [LIST_REPORT_DEFINITIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C168C82D-07FC-409F-9D40-116CA3D8D9CF)
- [LIST_REPORTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-710A4C4F-7149-4119-8DEF-09E4A41D3A9E)
- [LIST_ROLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C224918E-0B9C-4AF2-85CC-116FF9200C5B)
- [LIST_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-233B0EDD-22B0-495B-B8B2-11E0298F259B)
- [LIST_SDM_MASKING_POLICY_DIFFERENCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5B4C365C-2E10-49D2-8A5A-6A1FA263AFD8)
- [LIST_SECURITY_ASSESSMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A853045F-31D5-4B0D-8089-88923B98036C)
- [LIST_SECURITY_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B367C7EA-F55F-4274-A18C-C7C3BD2416B5)
- [LIST_SECURITY_POLICY_DEPLOYMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-DE18E170-B680-41ED-AF6C-218F786365B4)
- [LIST_SECURITY_POLICY_ENTRY_STATES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E1E8EF89-8D59-4138-B527-858C70EBD865)
- [LIST_SENSITIVE_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-EADE042E-C137-44FC-977A-E9AE70698144)
- [LIST_SENSITIVE_DATA_MODELS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-83B91ABF-A660-4220-A7B3-E93AA86864A1)
- [LIST_SENSITIVE_OBJECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-659ACE39-0301-407F-8089-C6868530CF4A)
- [LIST_SENSITIVE_SCHEMAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4B5CA008-5910-417F-AB13-AD29B94A5F34)
- [LIST_SENSITIVE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-79FE42AB-8296-47D2-B654-5D7883B31399)
- [LIST_SQL_COLLECTION_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-060EEAB5-3722-4DFE-B057-385C5FC776D4)
- [LIST_SQL_COLLECTION_LOG_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E75BD75A-D60E-430B-8F8E-3848B7326CC9)
- [LIST_SQL_COLLECTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BBD99031-5858-4311-AF1C-66CD52CAE20D)
- [LIST_SQL_FIREWALL_ALLOWED_SQL_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-97F7CB38-C338-4FB4-BAE7-9B21B4998C1E)
- [LIST_SQL_FIREWALL_ALLOWED_SQLS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1614FB92-EE8A-47DD-8834-44DAD0D7C87F)
- [LIST_SQL_FIREWALL_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-02D44265-CC1F-44DB-BCB6-4EAC2238987B)
- [LIST_SQL_FIREWALL_POLICY_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7A4D455A-DAE7-43B3-AFBB-EF4312F307F9)
- [LIST_SQL_FIREWALL_VIOLATION_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CA90F6E5-3DAD-4EB9-9EAE-69CAFE3A0E89)
- [LIST_SQL_FIREWALL_VIOLATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7B847665-871F-485C-A601-3EA43CE531C3)
- [LIST_TABLES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-2D8DB18B-E2EC-40C0-B697-E2D90E5DCD04)
- [LIST_TARGET_ALERT_POLICY_ASSOCIATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BA901D65-FA53-4EDA-9130-D9A637C6DEDA)
- [LIST_TARGET_DATABASES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1661F497-FA48-48EC-B13F-AB42AD5FED0F)
- [LIST_USER_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E0FD26BB-7EC6-4D6C-816D-74D09748862C)
- [LIST_USER_ASSESSMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6CED79E8-1F85-4074-95CE-FEA5E23D7F1C)
- [LIST_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CBE9D536-242F-445D-82D4-D51044E1C2E1)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0CEAD2F2-AAA4-4AF9-BB77-E3360B2AF806)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-84047833-0BA1-48A7-A138-598022D3CABF)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-62CD6B96-1275-42A0-8804-B6A77AC89813)
- [MASK_DATA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4E1D1573-DEB7-459C-BB5F-B5293E6867CC)
- [MODIFY_GLOBAL_SETTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-10D9D0B3-FCE1-42A0-8B6F-071C80E614E4)
- [PATCH_ALERTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5334ED0C-B640-4682-9C2B-A9DCBE3A03AA)
- [PATCH_DISCOVERY_JOB_RESULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-638F3EC2-305F-4703-9348-832EA48641EF)
- [PATCH_MASKING_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1D7DB8EA-88F6-4181-9588-BF5E3D46BD2A)
- [PATCH_SDM_MASKING_POLICY_DIFFERENCE_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-C0978D1C-2F58-4FEE-A02F-26D3F226A19D)
- [PATCH_SENSITIVE_COLUMNS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-799108CE-8A18-4883-AADA-75F41E75E665)
- [PATCH_TARGET_ALERT_POLICY_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4F3B6A14-1512-472D-8C49-F074F86AAAC6)
- [PROVISION_AUDIT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D7E51DCD-2342-4543-BA86-47A51870D5FF)
- [PURGE_SQL_COLLECTION_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E9F9433A-D8D9-4E96-8EEB-56EED856B0DF)
- [REFRESH_DATABASE_SECURITY_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-23746A73-EC83-49C8-A162-DB04E74DBF8B)
- [REFRESH_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-4F1F7A8F-22BA-4660-AB84-818D39FA24D5)
- [REFRESH_SQL_COLLECTION_LOG_INSIGHTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-41823D65-767A-4BD2-9ABF-2ADB6B55C54A)
- [REFRESH_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A6C60C77-C6CC-4453-B650-F8CD7A9726EB)
- [REMOVE_SCHEDULE_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E4E3EC5E-4901-40C4-9D28-46FE9BB0CA00)
- [RESUME_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-9E6A96DC-A617-43E0-B84A-1CF6500438D5)
- [RESUME_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-3DD3A585-27E6-4DB1-BB52-7E63A5857395)
- [RETRIEVE_AUDIT_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6F47B935-BD96-4EE7-B4AD-67A2E9B90B9E)
- [SCHEDULE_REPORT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-BCEB61F9-1F4F-404E-ADCE-29A82C857A3A)
- [SET_SECURITY_ASSESSMENT_BASELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-EE3CB6A7-39E2-43D4-91B9-0166D5E9F4DD)
- [SET_USER_ASSESSMENT_BASELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-CA5F0F83-137F-40C6-9DBC-8C1D44EA2161)
- [START_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-486B415D-FEC1-4426-BBD4-3AB795AC2E1F)
- [START_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D84EA1F9-2795-4500-B234-189B5255456A)
- [STOP_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-5A3265B6-FB85-452D-A771-B3F5948C94B2)
- [STOP_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-10A97796-D10E-4299-BD16-ADE87DB073A5)
- [SUSPEND_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0935BF85-1D49-4D88-A5CE-05B96AACF35D)
- [UNSET_SECURITY_ASSESSMENT_BASELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-AF946BF3-8D3F-4EB2-A2B8-2E3A9F0DE612)
- [UNSET_USER_ASSESSMENT_BASELINE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-AF79B0F2-B0AC-4E61-A340-207062817415)
- [UPDATE_ALERT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-E474DEF1-ADBB-46FC-8610-FEAC45F71B51)
- [UPDATE_AUDIT_ARCHIVE_RETRIEVAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B2EB0511-32D4-46EF-A06E-34BA151EDE8F)
- [UPDATE_AUDIT_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1FAF3E81-3CA6-4D2E-ABB5-5DDA8D49EF5C)
- [UPDATE_AUDIT_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-A21BE671-33A2-4ED1-A746-BE6E0283979D)
- [UPDATE_AUDIT_TRAIL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-20D01D59-C550-40E5-99FF-86240AE4D6B5)
- [UPDATE_DATA_SAFE_PRIVATE_ENDPOINT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B311160D-FB3B-4F44-AA75-7D3C89C054E8)
- [UPDATE_DATABASE_SECURITY_CONFIG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-6EF80FDC-6998-47D8-85AC-CA29AAE3BEDA)
- [UPDATE_LIBRARY_MASKING_FORMAT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-493442E2-E1CB-49C7-9B02-D155A97A0101)
- [UPDATE_MASKING_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-0A0F96BD-9B4A-4DC3-9A62-FA270AB0A31A)
- [UPDATE_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D1A3A7DD-8298-408C-BCC3-874C80FD6BCE)
- [UPDATE_ON_PREM_CONNECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D45A2A46-31BE-47FB-87CD-A590AAA47E67)
- [UPDATE_ON_PREM_CONNECTOR_WALLET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-57BF52A5-7946-4D5B-8D74-891EE547B5A2)
- [UPDATE_REPORT_DEFINITION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7E124E77-F551-4C31-B639-FA990E531EF6)
- [UPDATE_SDM_MASKING_POLICY_DIFFERENCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-22EDB164-C804-42EE-8FAD-C09B3627CCB5)
- [UPDATE_SECURITY_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-DEF3B6F6-A65D-4C7D-A175-BF01F16D5B56)
- [UPDATE_SECURITY_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-1823114B-0BA8-40DB-811E-9B4E69CD9BF2)
- [UPDATE_SECURITY_POLICY_DEPLOYMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F1B8A9C3-0D8A-441C-B52A-0F1417303B4C)
- [UPDATE_SENSITIVE_COLUMN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-412D119F-76E5-48E0-B658-7BD842539D4B)
- [UPDATE_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FE1D09F9-F0BC-44D6-8F50-5D4300AD3282)
- [UPDATE_SENSITIVE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-FF4B90C1-30A1-4EA7-8F98-FB245A3E65D1)
- [UPDATE_SQL_COLLECTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-D50B3D34-0FA2-4E6C-98CF-411DA063A896)
- [UPDATE_SQL_FIREWALL_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-7F9C15F2-94B6-42CF-B42C-FF6F045C6BEC)
- [UPDATE_TARGET_ALERT_POLICY_ASSOCIATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-F78788B0-74E8-4C24-9810-A19DAA3CAA3A)
- [UPDATE_TARGET_DATABASE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-19E240EA-84A2-451E-922F-A8EF8229B510)
- [UPDATE_USER_ASSESSMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-B86EE266-1C83-4955-B7AE-EA9E6BD60AF3)
- [UPLOAD_MASKING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-371867BB-0F53-4840-88BC-2F3B4E1C0A9E)
- [UPLOAD_SENSITIVE_DATA_MODEL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ds_data_safe.html#ADSDK-GUID-01C115C5-7788-4C5E-96D2-DA332CBFFD3C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
