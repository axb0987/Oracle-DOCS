# Cloud Guard Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#dcoc-content-body)

## Cloud Guard Functions

Package: DBMS_CLOUD_OCI_CG_CLOUD_GUARD

### ADD_COMPARTMENT Function

Add an existing compartment to a security zone. If you previously removed a subcompartment from a security zone, you can add it back to the same security zone. The security zone ensures that resources in the subcompartment comply with the security zone's policies.

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`add_compartment_details`

(required) The compartment to add to the security zone.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CANCEL_WORK_REQUEST Function

Cancels the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DATA_SOURCE_COMPARTMENT Function

Moves the DataSource from current compartment to another.

Syntax
```

```

Parameters

Parameter Description

`data_source_id`

(required) DataSource OCID

`change_data_source_compartment_details`

(required) The compartment id of the DataSource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DETECTOR_RECIPE_COMPARTMENT Function

Moves the DetectorRecipe from current compartment to another.

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`change_detector_recipe_compartment_details`

(required) The target compartment id.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_MANAGED_LIST_COMPARTMENT Function

Moves the ManagedList from current compartment to another.

Syntax
```

```

Parameters

Parameter Description

`managed_list_id`

(required) The cloudguard list OCID to be passed in the request.

`change_managed_list_compartment_details`

(required) The compartment id of the ManagedList

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_RESPONDER_RECIPE_COMPARTMENT Function

Moves the ResponderRecipe from current compartment to another.

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`change_responder_recipe_compartment_details`

(required) The target compartment id.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_RECIPE_COMPARTMENT Function

Moves a security zone recipe to a different compartment. When provided, `If-Match` is checked against `ETag` values of the resource.

Syntax
```

```

Parameters

Parameter Description

`security_recipe_id`

(required) The unique identifier of the security zone recipe (`SecurityRecipe`)

`change_security_recipe_compartment_details`

(required) The compartment to which you want to move the recipe.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_SECURITY_ZONE_COMPARTMENT Function

Moves a security zone to a different compartment. When provided, `If-Match` is checked against `ETag` values of the resource.

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`change_security_zone_compartment_details`

(required) The compartment to which you want to move the security zone.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_MASK_RULE Function

Creates a new Data Mask Rule Definition

Syntax
```

```

Parameters

Parameter Description

`create_data_mask_rule_details`

(required) Definition for the new Data Mask Rule.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DATA_SOURCE Function

Creates a DataSource

Syntax
```

```

Parameters

Parameter Description

`create_data_source_details`

(required) Details for the new DataSource.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DETECTOR_RECIPE Function

Creates a DetectorRecipe

Syntax
```

```

Parameters

Parameter Description

`create_detector_recipe_details`

(required) Details for the new DetectorRecipe.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DETECTOR_RECIPE_DETECTOR_RULE Function

Create the DetectorRule

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`create_detector_recipe_detector_rule_details`

(required) The details with which detector rule has to be created.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MANAGED_LIST Function

Creates a new ManagedList.

Syntax
```

```

Parameters

Parameter Description

`create_managed_list_details`

(required) Details for the new ManagedList.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_RESPONDER_RECIPE Function

Create a ResponderRecipe.

Syntax
```

```

Parameters

Parameter Description

`create_responder_recipe_details`

(required) Details for ResponderRecipe.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SECURITY_RECIPE Function

Creates a security zone recipe. A security zone recipe is a collection of security zone policies.

Syntax
```

```

Parameters

Parameter Description

`create_security_recipe_details`

(required) Details for the new `SecurityRecipe`.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SECURITY_ZONE Function

Creates a security zone for a compartment. A security zone enforces all security zone policies in a given security zone recipe. Any actions that violate a policy are denied. By default, any subcompartments are also in the same security zone.

Syntax
```

```

Parameters

Parameter Description

`create_security_zone_details`

(required) Details for the new `SecurityZone`.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TARGET Function

Creates a new Target

Syntax
```

```

Parameters

Parameter Description

`create_target_details`

(required) Details for the new Target.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TARGET_DETECTOR_RECIPE Function

Attach a DetectorRecipe with the Target

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`attach_target_detector_recipe_details`

(required) Details for associating DetectorRecipe to Target

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TARGET_RESPONDER_RECIPE Function

Attach a ResponderRecipe with the Target

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`attach_target_responder_recipe_details`

(required) Details for associating ResponderRecipe to Target

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_MASK_RULE Function

Deletes a DataMaskRule identified by dataMaskRuleId

Syntax
```

```

Parameters

Parameter Description

`data_mask_rule_id`

(required) OCID of dataMaskRule

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DATA_SOURCE Function

Deletes a DataSource identified by dataSourceId

Syntax
```

```

Parameters

Parameter Description

`data_source_id`

(required) DataSource OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DETECTOR_RECIPE Function

Deletes a DetectorRecipe identified by detectorRecipeId

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DETECTOR_RECIPE_DETECTOR_RULE Function

Deletes DetectorRecipeDetectorRule

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`detector_rule_id`

(required) The key of Detector Rule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DETECTOR_RECIPE_DETECTOR_RULE_DATA_SOURCE Function

Delete the DetectorRecipeDetectorRuleDataSource resource by identifier

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`detector_rule_id`

(required) The key of Detector Rule.

`data_source_id`

(required) DataSource OCID

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MANAGED_LIST Function

Deletes a managed list identified by managedListId

Syntax
```

```

Parameters

Parameter Description

`managed_list_id`

(required) The cloudguard list OCID to be passed in the request.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_RESPONDER_RECIPE Function

Delete the ResponderRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SECURITY_RECIPE Function

Deletes a security zone recipe. The recipe can't be associated with an existing security zone.

Syntax
```

```

Parameters

Parameter Description

`security_recipe_id`

(required) The unique identifier of the security zone recipe (`SecurityRecipe`)

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SECURITY_ZONE Function

Deletes an existing security zone with a given identifier.

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TARGET Function

Deletes a Target identified by targetId

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TARGET_DETECTOR_RECIPE Function

Delete the TargetDetectorRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TARGET_RESPONDER_RECIPE Function

Delete the TargetResponderRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### EXECUTE_RESPONDER_EXECUTION Function

Executes the responder execution. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`responder_execution_id`

(required) The identifier of the responder execution.

`compartment_id`

(required) The ID of the compartment in which to list resources.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`execute_responder_execution_details`

(optional) Details for Responder Configuration

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONDITION_METADATA_TYPE Function

Returns ConditionType with its details.

Syntax
```

```

Parameters

Parameter Description

`condition_metadata_type_id`

(required) The type of the condition meta data.

Allowed values are: 'ActivityCondition', 'SecurityCondition', 'CloudGuardCondition', 'ThreatCondition'

`opc_request_id`

(optional) The client request ID for tracing.

`service_type`

(optional) ServiceType filter for the condition meta data.

`resource_type`

(optional) Resource filter for the condition meta data.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIGURATION Function

GET Cloud Guard Configuration Details for a Tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_MASK_RULE Function

Returns a DataMaskRule identified by DataMaskRuleId

Syntax
```

```

Parameters

Parameter Description

`data_mask_rule_id`

(required) OCID of dataMaskRule

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DATA_SOURCE Function

Returns a DataSource identified by dataSourceId

Syntax
```

```

Parameters

Parameter Description

`data_source_id`

(required) DataSource OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DETECTOR Function

Returns a Detector identified by detectorId.

Syntax
```

```

Parameters

Parameter Description

`detector_id`

(required) The Name of Detector.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DETECTOR_RECIPE Function

Returns a DetectorRecipe identified by detectorRecipeId

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DETECTOR_RECIPE_DETECTOR_RULE Function

Get DetectorRule by identifier

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`detector_rule_id`

(required) The key of Detector Rule.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DETECTOR_RULE Function

Returns a Detector Rule identified by detectorRuleId

Syntax
```

```

Parameters

Parameter Description

`detector_id`

(required) The Name of Detector.

`detector_rule_id`

(required) The key of Detector Rule.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_LIST Function

Returns a managed list identified by managedListId

Syntax
```

```

Parameters

Parameter Description

`managed_list_id`

(required) The cloudguard list OCID to be passed in the request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROBLEM Function

Returns a Problems response

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESOURCE_PROFILE Function

Returns resource profile details

Syntax
```

```

Parameters

Parameter Description

`resource_profile_id`

(required) OCID of the resource profile.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESPONDER_EXECUTION Function

Returns a Responder Execution identified by responderExecutionId

Syntax
```

```

Parameters

Parameter Description

`responder_execution_id`

(required) The identifier of the responder execution.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESPONDER_RECIPE Function

Get a ResponderRecipe by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESPONDER_RECIPE_RESPONDER_RULE Function

Get ResponderRule by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`responder_rule_id`

(required) The id of ResponderRule

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RESPONDER_RULE Function

Get a ResponderRule by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_rule_id`

(required) The id of ResponderRule

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_POLICY Function

Gets a security zone policy using its identifier. When a policy is enabled in a security zone, then any action in the zone that attempts to violate that policy is denied.

Syntax
```

```

Parameters

Parameter Description

`security_policy_id`

(required) The unique identifier of the security zone policy (`SecurityPolicy`)

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_RECIPE Function

Gets a security zone recipe by identifier. A security zone recipe is a collection of security zone policies.

Syntax
```

```

Parameters

Parameter Description

`security_recipe_id`

(required) The unique identifier of the security zone recipe (`SecurityRecipe`)

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECURITY_ZONE Function

Gets a security zone by its identifier. A security zone is associated with a security zone recipe and enforces all security zone policies in the recipe. Any actions in the zone's compartments that violate a policy are denied.

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SIGHTING Function

Returns Sighting details

Syntax
```

```

Parameters

Parameter Description

`sighting_id`

(required) OCID of the sighting.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET Function

Returns a Target identified by targetId

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_DETECTOR_RECIPE Function

Get a TargetDetectorRecipe by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_DETECTOR_RECIPE_DETECTOR_RULE Function

Get DetectorRule by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`detector_rule_id`

(required) The id of DetectorRule

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_RESPONDER_RECIPE Function

Get a TargetResponderRecipe by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TARGET_RESPONDER_RECIPE_RESPONDER_RULE Function

Get ResponderRule by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`responder_rule_id`

(required) The id of ResponderRule

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets details of the work request with the given ID.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CONDITION_METADATA_TYPES Function

Returns a list of condition types.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_MASK_RULES Function

Returns a list of all Data Mask Rules in the root 'compartmentId' passed.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`data_mask_rule_status`

(optional) The status of the dataMaskRule.

Allowed values are: 'ENABLED', 'DISABLED'

`target_id`

(optional) OCID of target

`iam_group_id`

(optional) OCID of iamGroup

`target_type`

(optional) Type of target

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_SOURCE_EVENTS Function

Returns a list of events from CloudGuard DataSource

Syntax
```

```

Parameters

Parameter Description

`data_source_id`

(required) DataSource OCID

`l_region`

(optional) A filter to return only resource their region matches the given region.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DATA_SOURCES Function

Returns a list of all Data Sources in a compartment The ListDataSources operation returns only the data Sources in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListdataSources on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`data_source_feed_provider`

(optional) A filter to return only resources their feedProvider matches the given DataSourceFeedProvider.

Allowed values are: 'LOGGINGQUERY'

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`logging_query_type`

(optional) A filter to return only resources their query type matches the given LoggingQueryType.

Allowed values are: 'INSIGHT'

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DETECTOR_RECIPE_DETECTOR_RULES Function

Returns a list of DetectorRule associated with DetectorRecipe.

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DETECTOR_RECIPES Function

Returns a list of all Detector Recipes in a compartment The ListDetectorRecipes operation returns only the detector recipes in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListDetectorRecipes on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`resource_metadata_only`

(optional) Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard are returned.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DETECTOR_RULES Function

Returns a list of detector rules for the detectorId passed.

Syntax
```

```

Parameters

Parameter Description

`detector_id`

(required) The Name of Detector.

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DETECTORS Function

Returns detector catalog - list of detectors supported by Cloud Guard

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPACTED_RESOURCES Function

Returns a list of Impacted Resources for a CloudGuard Problem

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_LIST_TYPES Function

Returns all ManagedList types supported by Cloud Guard

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MANAGED_LISTS Function

Returns a list of ListManagedLists. The ListManagedLists operation returns only the managed lists in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return ManagedLists in only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListManagedLists on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`resource_metadata_only`

(optional) Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard are returned.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`list_type`

(optional) The type of the ManagedList.

Allowed values are: 'CIDR_BLOCK', 'USERS', 'GROUPS', 'IPV4ADDRESS', 'IPV6ADDRESS', 'RESOURCE_OCID', 'REGION', 'COUNTRY', 'STATE', 'CITY', 'TAGS', 'GENERIC'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_POLICIES Function

Returns the list of global policy statements needed by Cloud Guard when enabling

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

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

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROBLEM_ENDPOINTS Function

Returns a list of endpoints associated with a cloud guard problem

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROBLEM_ENTITIES Function

Returns a list of entities for a CloudGuard Problem

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROBLEM_HISTORIES Function

Returns a list of Actions done on CloudGuard Problem

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`problem_id`

(required) OCId of the problem.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROBLEMS Function

Returns a list of all Problems identified by the Cloud Guard The ListProblems operation returns only the problems in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListProblems on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_last_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_last_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`time_first_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_first_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`lifecycle_detail`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED', 'DELETED'

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'ACTIVE', 'INACTIVE'

`l_region`

(optional) OCI Monitoring region.

`risk_level`

(optional) Risk level of the Problem.

`resource_type`

(optional) Resource Type associated with the resource.

`city`

(optional) City of the problem.

`state`

(optional) State of the problem.

`country`

(optional) Country of the problem.

`label`

(optional) Label associated with the Problem.

`detector_rule_id_list`

(optional) Comma seperated list of detector rule ids to be passed in to match against Problems.

`detector_type`

(optional) The field to list the Problems by Detector Type. Valid values are IAAS_ACTIVITY_DETECTOR and IAAS_CONFIGURATION_DETECTOR

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`target_id`

(optional) The ID of the target in which to list resources.

`problem_category`

(optional) Setting this to `SECURITY_ZONE` returns only security-zone related violations.

Allowed values are: 'SECURITY_ZONE'

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`resource_id`

(optional) The ID of the resource associated with the problem.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for riskLevel, timeLastDetected and resourceName is descending. Default order for riskLevel and resourceName is ascending. If no value is specified timeLastDetected is default.

Allowed values are: 'riskLevel', 'timeLastDetected', 'resourceName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECOMMENDATIONS Function

Returns a list of all Recommendations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for riskLevel and timeCreated is descending. If no value is specified riskLevel is default.

Allowed values are: 'riskLevel', 'timeCreated'

`target_id`

(optional) The ID of the target in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_detail`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'OPEN', 'RESOLVED', 'DISMISSED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_PROFILE_ENDPOINTS Function

Returns a list of endpoints for Cloud Guard resource profile

Syntax
```

```

Parameters

Parameter Description

`resource_profile_id`

(required) OCID of the resource profile.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_PROFILE_IMPACTED_RESOURCES Function

Returns a list of impacted resources for Cloud Guard resource profile

Syntax
```

```

Parameters

Parameter Description

`resource_profile_id`

(required) OCID of the resource profile.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_PROFILES Function

Returns a list of all resource profiles identified by the Cloud Guard The ListResourceProfiles operation returns only resource profiles that match the passed filters. The ListResourceProfiles operation returns only the resource profiles in `compartmentId` passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListResourceProfiles on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_last_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_last_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`time_first_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_first_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`resource_types`

(optional) A filter to return only resources that match the list of resource types given

`risk_score_greater_than_or_equal_to`

(optional) risk score filter

`risk_score_less_than_or_equal_to`

(optional) risk score filter

`techniques`

(optional) A filter to return only resources that match the list of techniques given

`tactics`

(optional) A filter to return only resources that match the list of tactics given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort resource profiles. Only one sort order may be provided. Default order for timeLastDetected is descending. If no value is specified timeLastDetected is default.

Allowed values are: 'riskScore', 'riskScoreGrowth', 'timeFirstDetected', 'timeLastDetected', 'sightingsCount', 'displayName', 'type'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESOURCE_TYPES Function

Returns a list of resource types.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`detector_id`

(optional) Detector type

Allowed values are: 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR'

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESPONDER_ACTIVITIES Function

Returns a list of Responder activities done on CloudGuard Problem

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for responderRuleName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'responderRuleName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESPONDER_EXECUTIONS Function

Returns a list of Responder Executions. A Responder Execution is an entity that tracks the collective execution of multiple Responder Rule Executions for a given Problem.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`responder_rule_ids`

(optional) Responder Rule Ids filter for the Responder Executions.

`time_created_greater_than_or_equal_to`

(optional) Creation Start time for filtering

`time_created_less_than_or_equal_to`

(optional) Creation End time for filtering

`time_completed_greater_than_or_equal_to`

(optional) Completion End Time

`time_completed_less_than_or_equal_to`

(optional) Completion Start Time

`target_id`

(optional) The ID of the target in which to list resources.

`resource_type`

(optional) Resource Type associated with the resource.

`responder_type`

(optional) The field to list the Responder Executions by Responder Type. Valid values are REMEDIATION and NOTIFICATION

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`responder_execution_status`

(optional) The status of the responder execution in which to list responders.

Allowed values are: 'STARTED', 'AWAITING_CONFIRMATION', 'AWAITING_INPUT', 'SUCCEEDED', 'FAILED', 'SKIPPED', 'ALL'

`responder_execution_mode`

(optional) The mode of the responder execution in which to list responders.

Allowed values are: 'MANUAL', 'AUTOMATED', 'ALL'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for responderRuleName and resourceName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'responderRuleName', 'resourceName', 'timeCompleted'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESPONDER_RECIPE_RESPONDER_RULES Function

Returns a list of ResponderRule associated with ResponderRecipe.

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESPONDER_RECIPES Function

Returns a list of all ResponderRecipes in a compartment The ListResponderRecipe operation returns only the targets in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListResponderRecipe on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`resource_metadata_only`

(optional) Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard are returned.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RESPONDER_RULES Function

Returns a list of ResponderRule.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_POLICIES Function

Returns a list of security zone policies. Specify any compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The unique identifier of the security zone policy (`SecurityPolicy`)

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_RECIPES Function

Gets a list of all security zone recipes in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The unique identifier of the security zone recipe (`SecurityRecipe`)

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECURITY_ZONES Function

Gets a list of all security zones in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) The unique identifier of the security zone (`SecurityZone`)

`security_recipe_id`

(optional) The unique identifier of the security zone recipe (`SecurityRecipe`)

`is_required_security_zones_in_subtree`

(optional) security zones in the subtree

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SIGHTING_ENDPOINTS Function

Returns Sighting endpoints details

Syntax
```

```

Parameters

Parameter Description

`sighting_id`

(required) OCID of the sighting.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SIGHTING_IMPACTED_RESOURCES Function

Return a list of Impacted Resources for a CloudGuard Sighting

Syntax
```

```

Parameters

Parameter Description

`sighting_id`

(required) OCID of the sighting.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SIGHTINGS Function

Returns a list of all Sightings identified by the Cloud Guard The ListSightings operation returns only sightings that match the passed filters. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListSightings on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`problem_id`

(optional) OCID of the problem.

`resource_profile_id`

(optional) OCID of the resource profile.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated'

`time_last_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_last_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TACTICS Function

Returns a list of tactics associated with detector rules.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_DETECTOR_RECIPE_DETECTOR_RULES Function

Returns a list of DetectorRule associated with DetectorRecipe within a Target.

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_DETECTOR_RECIPES Function

Returns a list of all detector recipes associated with the target identified by targetId

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_RESPONDER_RECIPE_RESPONDER_RULES Function

Returns a list of ResponderRule associated with ResponderRecipe within a Target.

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName', 'riskLevel'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGET_RESPONDER_RECIPES Function

Returns a list of all responder recipes associated with the target identified by targetId

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TARGETS Function

Returns a list of all Targets in a compartment The ListTargets operation returns only the targets in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform ListTargets on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`is_non_security_zone_targets_only_query`

(optional) Default is false. When set to true, only the targets that would be deleted as part of security zone creation will be returned.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TECHNIQUES Function

Returns a list of techniques associated with detector rules.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`tactics`

(optional) A filter to return only resources that match the list of tactics given.

`lifecycle_state`

(optional) The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.

Allowed values are: 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_ERRORS Function

Return a (paginated) list of errors for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUEST_LOGS Function

Return a (paginated) list of logs for a given work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The ID of the asynchronous request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.

Allowed values are: 'timeCreated'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`status`

(optional) A filter to return only resources their lifecycleState matches the given OperationStatus.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'WAITING', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resource_id`

(optional) The ID of the resource affected by the work request.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

Allowed values are: 'timeAccepted'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_COMPARTMENT Function

Removes an existing compartment from a security zone. When you remove a subcompartment from a security zone, it no longer enforces security zone policies on the resources in the subcompartment. You can't remove the primary compartment that was used to create the security zone.

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`remove_compartment_details`

(required) The compartment to remove from the security zone.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_RISK_SCORES Function

Examines the number of problems related to the resource and the relative severity of those problems.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SECURITY_SCORE_SUMMARIZED_TREND Function

Measures the number of resources examined across all regions and compares it with the number of problems detected, for a given time period.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_score_computed_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.

`time_score_computed_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to today's current time.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SECURITY_SCORES Function

Measures the number of resources examined across all regions and compares it with the number of problems detected.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_ACTIVITY_PROBLEMS Function

Returns the summary of Activity type problems identified by cloud guard, for a given set of dimensions. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. The compartmentId to be passed with `accessLevel` and `compartmentIdInSubtree` params has to be the root compartment id (tenant-id) only.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`include_unknown_locations`

(optional) Default is false. When set to true, the summary of activity problems that has unknown values for city, state or country will be included.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_PROBLEMS Function

Returns the number of problems identified by cloud guard, for a given set of dimensions. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`list_dimensions`

(required) The possible attributes based on which the problems can be distinguished.

Allowed values are: 'RESOURCE_TYPE', 'REGION', 'COMPARTMENT_ID', 'RISK_LEVEL'

`compartment_id`

(required) The ID of the compartment in which to list resources.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_RESPONDER_EXECUTIONS Function

Returns the number of Responder Executions, for a given set of dimensions. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`responder_executions_dimensions`

(required) The possible attributes based on which the responder executions can be distinguished

Allowed values are: 'RESPONDER_RULE_TYPE', 'RESPONDER_EXECUTION_STATUS'

`compartment_id`

(required) The ID of the compartment in which to list resources.

`responder_type_filter`

(optional) The possible filters for Responder Type Dimension to distinguish Responder Executions. If no values are passed, the metric for responder executions of all reponder types are returned

Allowed values are: 'REMEDIATION', 'NOTIFICATION'

`responder_execution_status_filter`

(optional) The possible filters for Responder Type Dimension to distinguish Responder Executions. If no values are passed, the metric for responder executions of all status are returned

Allowed values are: 'STARTED', 'AWAITING_CONFIRMATION', 'SUCCEEDED', 'FAILED', 'SKIPPED'

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_RISK_SCORES Function

DEPRECATED

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_SECURITY_SCORES Function

DEPRECATED

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_TOP_TREND_RESOURCE_PROFILE_RISK_SCORES Function

Summarizes the resource profile risk score top trends for the given time range based on the search filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_score_computed_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.

`time_score_computed_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to today's current time.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`sort_by`

(optional) The field to sort trendlines for resource profiles. Only one sort order may be provided. If no value is specified riskScore is default.

Allowed values are: 'riskScore', 'riskScoreGrowth', 'timeFirstDetected', 'timeLastDetected'

`l_count`

(optional) Number of resource profile risk score trend-lines to be displayed. Default value is 10.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_TREND_PROBLEMS Function

Returns the number of problems identified by cloud guard, for a given time period. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_first_detected_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to current time - 30 days.

`time_first_detected_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to current time.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_TREND_RESOURCE_RISK_SCORES Function

Summarizes the resource risk score trend for the given time range based on the search filters.

Syntax
```

```

Parameters

Parameter Description

`request_summarized_trend_resource_risk_scores_details`

(required) The filter to fetch risk score trend.

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_score_computed_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.

`time_score_computed_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to today's current time.

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_TREND_RESPONDER_EXECUTIONS Function

Returns the number of remediations performed by Responders, for a given time period. The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`. The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_completed_greater_than_or_equal_to`

(optional) Completion End Time

`time_completed_less_than_or_equal_to`

(optional) Completion Start Time

`compartment_id_in_subtree`

(optional) Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`access_level`

(optional) Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.

Allowed values are: 'RESTRICTED', 'ACCESSIBLE'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REQUEST_SUMMARIZED_TREND_SECURITY_SCORES Function

DEPRECATED

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`time_score_computed_greater_than_or_equal_to`

(optional) Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.

`time_score_computed_less_than_or_equal_to`

(optional) End time for a filter. If end time is not specified, end time will be set to today's current time.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SKIP_BULK_RESPONDER_EXECUTION Function

Skips the execution for a bulk of responder executions The operation is atomic in nature

Syntax
```

```

Parameters

Parameter Description

`skip_bulk_responder_execution_details`

(required) A list of responder execution ids to skip the execution

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SKIP_RESPONDER_EXECUTION Function

Skips the execution of the responder execution. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`responder_execution_id`

(required) The identifier of the responder execution.

`compartment_id`

(required) The ID of the compartment in which to list resources.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### TRIGGER_RESPONDER Function

push the problem to responder

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`trigger_responder_details`

(required) The responder may update the problem.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_BULK_PROBLEM_STATUS Function

Updates the statuses in bulk for a list of problems The operation is atomic in nature

Syntax
```

```

Parameters

Parameter Description

`update_bulk_problem_status_details`

(required) A list of problem ids to be passed in to update the Problem status

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIGURATION Function

Enable/Disable Cloud Guard. The reporting region cannot be updated once created.

Syntax
```

```

Parameters

Parameter Description

`update_configuration_details`

(required) Update Configuration Details of Cloud Guard for a Tenancy.

`compartment_id`

(required) The ID of the compartment in which to list resources.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_MASK_RULE Function

Updates a DataMaskRule identified by dataMaskRuleId

Syntax
```

```

Parameters

Parameter Description

`data_mask_rule_id`

(required) OCID of dataMaskRule

`update_data_mask_rule_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DATA_SOURCE Function

Updates a data source identified by dataSourceId

Syntax
```

```

Parameters

Parameter Description

`data_source_id`

(required) DataSource OCID

`update_data_source_details`

(required) Details for the DataSource to be updated

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DETECTOR_RECIPE Function

Updates a detector recipe identified by detectorRecipeId

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`update_detector_recipe_details`

(required) Details for the DetectorRecipe to be updated

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DETECTOR_RECIPE_DETECTOR_RULE Function

Update the DetectorRule by identifier

Syntax
```

```

Parameters

Parameter Description

`detector_recipe_id`

(required) DetectorRecipe OCID

`detector_rule_id`

(required) The key of Detector Rule.

`update_detector_recipe_detector_rule_details`

(required) The details to be updated for DetectorRule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_MANAGED_LIST Function

Updates a managed list identified by managedListId

Syntax
```

```

Parameters

Parameter Description

`managed_list_id`

(required) The cloudguard list OCID to be passed in the request.

`update_managed_list_details`

(required) Details for the ManagedList to be updated

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROBLEM_STATUS Function

updates the problem details

Syntax
```

```

Parameters

Parameter Description

`problem_id`

(required) OCId of the problem.

`update_problem_status_details`

(required) The additional details for the problem.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RESPONDER_RECIPE Function

Update the ResponderRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`update_responder_recipe_details`

(required) The details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RESPONDER_RECIPE_RESPONDER_RULE Function

Update the ResponderRule by identifier

Syntax
```

```

Parameters

Parameter Description

`responder_recipe_id`

(required) OCID of ResponderRecipe

`responder_rule_id`

(required) The id of ResponderRule

`update_responder_recipe_responder_rule_details`

(required) The details to be updated for ResponderRule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_RECIPE Function

Updates a security zone recipe. A security zone recipe is a collection of security zone policies.

Syntax
```

```

Parameters

Parameter Description

`security_recipe_id`

(required) The unique identifier of the security zone recipe (`SecurityRecipe`)

`update_security_recipe_details`

(required) The information to be updated in the security zone recipe.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SECURITY_ZONE Function

Updates the security zone identified by its id

Syntax
```

```

Parameters

Parameter Description

`security_zone_id`

(required) The unique identifier of the security zone (`SecurityZone`)

`update_security_zone_details`

(required) The security zone information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET Function

Updates a Target identified by targetId

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`update_target_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_DETECTOR_RECIPE Function

Update the TargetDetectorRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`update_target_detector_recipe_details`

(required) The details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_DETECTOR_RECIPE_DETECTOR_RULE Function

Update the DetectorRule by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_detector_recipe_id`

(required) OCID of TargetDetectorRecipe

`detector_rule_id`

(required) The id of DetectorRule

`update_target_detector_recipe_detector_rule_details`

(required) The details to be updated for DetectorRule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_RESPONDER_RECIPE Function

Update the TargetResponderRecipe resource by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`update_target_responder_recipe_details`

(required) The details to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TARGET_RESPONDER_RECIPE_RESPONDER_RULE Function

Update the ResponderRule by identifier

Syntax
```

```

Parameters

Parameter Description

`target_id`

(required) OCID of target

`target_responder_recipe_id`

(required) OCID of TargetResponderRecipe

`responder_rule_id`

(required) The id of ResponderRule

`update_target_responder_recipe_responder_rule_details`

(required) The details to be updated for ResponderRule.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://cloudguard-cp-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Cloud Guard Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-86CD817F-8318-43BF-9080-CA91531B6F04)
- [ADD_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-85059CDE-AD83-4483-B852-5E970B6FB0A9)
- [CANCEL_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E4B74036-7D7C-4EE5-A53B-D894AA84EF9D)
- [CHANGE_DATA_SOURCE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-DB6E712E-08C4-4F21-9D06-1D4ADF07FF4E)
- [CHANGE_DETECTOR_RECIPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-02F75E6C-FE59-4278-8133-45FE8989B24B)
- [CHANGE_MANAGED_LIST_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-8757EC72-606F-48BB-8671-6F942266D2E1)
- [CHANGE_RESPONDER_RECIPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2DBA8654-C44A-4813-B39D-CD54B5FE1755)
- [CHANGE_SECURITY_RECIPE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-93BC9190-6880-4A05-B189-E082569FFA17)
- [CHANGE_SECURITY_ZONE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-1B4D0CF9-C7B3-42A3-BC62-4CFCA09A4A24)
- [CREATE_DATA_MASK_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-EDDAC051-33C6-44A9-832D-747903D168D3)
- [CREATE_DATA_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-74E48332-424B-4AD3-A447-173F16F1129C)
- [CREATE_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-5B73E21F-FDFD-4EFF-950D-B9319881AA88)
- [CREATE_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-CCC26B3E-5226-458E-AA82-6879CB9C44C6)
- [CREATE_MANAGED_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FAA0B3E4-94DA-4A32-9A28-F420ACB92D63)
- [CREATE_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FEEA6281-75FA-4588-805A-1F8BDA69A94C)
- [CREATE_SECURITY_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-0C7A8F2C-CB83-439B-BA1D-12C7623D1ECC)
- [CREATE_SECURITY_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E79CBF6B-5B90-41F4-805D-B4690A38A636)
- [CREATE_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-05473AD8-0B60-4CD3-8FA3-A34DEB54B00B)
- [CREATE_TARGET_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FCE95BE5-7DFB-409A-820F-6E3376C8B52C)
- [CREATE_TARGET_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-D187720E-5478-4E1F-8CC9-9E730AEBF591)
- [DELETE_DATA_MASK_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-3F3F5D97-1F51-4B77-B1BF-C4CFBE4F0851)
- [DELETE_DATA_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-F1CF4A01-862A-408C-B4AF-6C23460D3A4F)
- [DELETE_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-55C7EF56-1C67-4444-84C8-CA06A5FCAD8F)
- [DELETE_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-743973F3-B02D-4698-8CFC-003CC608C703)
- [DELETE_DETECTOR_RECIPE_DETECTOR_RULE_DATA_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-F2EB47B4-2EA5-400F-A92F-8366AF858B61)
- [DELETE_MANAGED_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-958ECD9A-88CC-4347-83F0-726F84A02582)
- [DELETE_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-165CE9FF-6CA3-42EA-8CC9-D9364C88A492)
- [DELETE_SECURITY_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B93A87C4-28AC-4F35-9023-B0E156D9B9FF)
- [DELETE_SECURITY_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-C8714646-23EC-471F-80E5-B2AEB73049E2)
- [DELETE_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-EA13A8CB-043A-496E-95F4-BDA2CBBDBCF4)
- [DELETE_TARGET_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B9F1FBA1-4304-4AA0-8D9A-F25C02ABE7C7)
- [DELETE_TARGET_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2278F420-6368-4D2E-B673-3839EE5B6595)
- [EXECUTE_RESPONDER_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-0E5A0162-E14C-4B70-8C11-E7DF347905BE)
- [GET_CONDITION_METADATA_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-71821320-12DF-4B05-8F8C-72D1A0DA8B77)
- [GET_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-3C592B92-6216-41FB-98F8-BAD310E8D2CE)
- [GET_DATA_MASK_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-199C2699-0F6D-4557-8C16-CA6F77F2AB42)
- [GET_DATA_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-85DA8F9F-7DA8-46AC-884D-CC686AAD0C32)
- [GET_DETECTOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-D9CF008C-76C7-480C-932B-F27BD4D6E765)
- [GET_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-239B1FE9-8187-498D-9223-6785EE09447B)
- [GET_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-6941D3B1-F9CC-4844-8911-02340B6CC114)
- [GET_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2C5E5EF0-F3B3-4A02-8807-6DB8C8C9E839)
- [GET_MANAGED_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-97BC20B5-E76D-4D5D-AD99-ED35CA6FC933)
- [GET_PROBLEM Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FAA7EDE9-E5BE-4B08-AA65-6A5984C23F77)
- [GET_RESOURCE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-4F3F77B4-CF88-458F-BE59-54E89D5C8515)
- [GET_RESPONDER_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B54FD408-AFE0-40F9-B2EB-8C4DB7193932)
- [GET_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-67FEB976-E86B-4379-8B09-AA7188204186)
- [GET_RESPONDER_RECIPE_RESPONDER_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-83F9BD1F-5581-4B58-B004-47A3D3E81008)
- [GET_RESPONDER_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-7BD7B476-DF37-4372-B80B-FB4249FFCEB5)
- [GET_SECURITY_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-013A9C90-2FFF-433A-8BFD-F6AC179B37F0)
- [GET_SECURITY_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-723FFE79-7679-4483-8F74-431FFCDBE1C5)
- [GET_SECURITY_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-1578F37D-21E2-4F5D-AC2D-CF0D82486FB6)
- [GET_SIGHTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-CCB11BC7-26E1-4800-8143-E55CED1B6CFA)
- [GET_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-6221447C-FBD0-4683-A84F-2CFF86912C2B)
- [GET_TARGET_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-922AE5FA-11CB-4C14-8940-76A49EA23B39)
- [GET_TARGET_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-6B3F7BEF-6DA4-4DB5-B99A-0BF8BC3D7F1B)
- [GET_TARGET_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E80480ED-2C51-437A-B356-DA603DD6618E)
- [GET_TARGET_RESPONDER_RECIPE_RESPONDER_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-3D5094D8-35A9-4285-93A7-4C6F1E0C9494)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-D4BB7E34-F1EB-4BF9-B081-11EEEC396606)
- [LIST_CONDITION_METADATA_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-C7795936-A7AC-429F-B638-1C79502E270B)
- [LIST_DATA_MASK_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2358BC7E-19AF-4A27-AABD-E477CE73AA44)
- [LIST_DATA_SOURCE_EVENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-EB727961-C774-4C81-B318-13C651532FB7)
- [LIST_DATA_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-07DC63D5-56AC-4D0F-913E-024A17E8789B)
- [LIST_DETECTOR_RECIPE_DETECTOR_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-3B21A25F-CDDF-4309-9A7B-ED17E77AF3DA)
- [LIST_DETECTOR_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-A6F0A972-3800-4F47-9F7A-D01BD86F370F)
- [LIST_DETECTOR_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-121E9664-8C42-4022-AE2B-F18385CA89DC)
- [LIST_DETECTORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-F805BC87-81D5-41B0-9C29-F9487105E42F)
- [LIST_IMPACTED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2F17679E-6BEF-4098-9DBF-6D38EEF14107)
- [LIST_MANAGED_LIST_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-CCFA3B40-48FB-40BE-82C0-DACDDA181DBA)
- [LIST_MANAGED_LISTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2CF7AA9D-C7C2-4DB1-9B21-CD0E4A1AEE96)
- [LIST_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-C656C729-51D9-4F36-ACFC-79A7FBAFC77C)
- [LIST_PROBLEM_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-BA201C5E-D076-43F7-A400-956E401C09AF)
- [LIST_PROBLEM_ENTITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-6827D9A5-E26A-49DD-BB15-823716DD5E1C)
- [LIST_PROBLEM_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-A18F4A77-6DCF-4A05-915B-D55B5B0C5B03)
- [LIST_PROBLEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-EDF274AF-A05D-4D30-BB4F-65B55394A205)
- [LIST_RECOMMENDATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-199CB74F-BB88-4223-A9A8-C12A1C67467A)
- [LIST_RESOURCE_PROFILE_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-D5317E7A-CB51-462C-BA63-5C856DF29D59)
- [LIST_RESOURCE_PROFILE_IMPACTED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-69E778D5-4F06-4ACF-8280-E83B3798820E)
- [LIST_RESOURCE_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-5B825725-46AD-4980-AD03-E4CFFBD8DE05)
- [LIST_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-CD59FE43-3369-4EAC-9A10-2D8197A45295)
- [LIST_RESPONDER_ACTIVITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FDAA4308-1F0D-4D15-9129-9DE661190016)
- [LIST_RESPONDER_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-BE6A93DF-7387-4D04-9AAB-1FEE25BDE04D)
- [LIST_RESPONDER_RECIPE_RESPONDER_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-FCE8DDCD-7EC6-49C6-AF79-C2F882B6A9C4)
- [LIST_RESPONDER_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E52F65C6-F5FD-48FC-B175-72A42CE44FFB)
- [LIST_RESPONDER_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-02B08766-48E3-4B49-81D3-C4604250791B)
- [LIST_SECURITY_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-94F38C68-FDE6-4FBB-A8D8-8A072734E44D)
- [LIST_SECURITY_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-8F95F7FD-E98F-44F5-BFC4-8015162CED10)
- [LIST_SECURITY_ZONES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-AA139BF6-154A-4A65-81F1-CE8C5C3FF72C)
- [LIST_SIGHTING_ENDPOINTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-77E01FEE-E326-4439-BDD0-C3A4EF1D2DE7)
- [LIST_SIGHTING_IMPACTED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-469A0BD8-17B1-43BB-9319-35B7EB65F225)
- [LIST_SIGHTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-857F7736-6825-4067-AA0C-A2BEC83C0230)
- [LIST_TACTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-DF8EEC98-D91B-4A19-8333-D15070111B1C)
- [LIST_TARGET_DETECTOR_RECIPE_DETECTOR_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-8FAD7AA5-8FDF-423E-8C05-EC75B5C61CCB)
- [LIST_TARGET_DETECTOR_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-23AC0F10-1FAC-4608-A12B-6A93D3BEB290)
- [LIST_TARGET_RESPONDER_RECIPE_RESPONDER_RULES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-79EF183D-AC81-4DE0-8074-2B9A6351B5D4)
- [LIST_TARGET_RESPONDER_RECIPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-58C1672B-87F4-40CE-9FCF-C6D504310011)
- [LIST_TARGETS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-357A2E7B-2AFD-47B9-B9A3-9445EF52FC68)
- [LIST_TECHNIQUES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-88AD4720-386A-4E97-891B-7884E061C3CB)
- [LIST_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-C61DE807-0D94-4EE8-B61C-8FAA0B7EA80D)
- [LIST_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-AAD88E6A-E5D7-4C65-8793-08FE1C90D504)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-4D091D5E-317E-44CE-99C6-272EBB2CEF02)
- [REMOVE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-82F6B872-D39C-41AF-9FC5-DC03D7359583)
- [REQUEST_RISK_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-56157575-1372-4245-B0B0-B11742C84448)
- [REQUEST_SECURITY_SCORE_SUMMARIZED_TREND Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E0D18650-94DA-4F17-8EFF-C92E40BDEECF)
- [REQUEST_SECURITY_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-F9F1A46A-E9AF-4D86-8C9A-8C1EAE81EB2B)
- [REQUEST_SUMMARIZED_ACTIVITY_PROBLEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B5D964AB-8473-4FFA-B391-C0B961A21A71)
- [REQUEST_SUMMARIZED_PROBLEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B797D304-9154-43A8-87BC-774DFAA3F70F)
- [REQUEST_SUMMARIZED_RESPONDER_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-DDBADB36-FE37-4CB5-8646-A2FE54DDC1E9)
- [REQUEST_SUMMARIZED_RISK_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-785E4ABD-42B9-4D3D-9012-AC44BAF07AEF)
- [REQUEST_SUMMARIZED_SECURITY_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E41D0ED9-FE98-4688-B408-8FE531C7645E)
- [REQUEST_SUMMARIZED_TOP_TREND_RESOURCE_PROFILE_RISK_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-BD026404-01AA-45E7-A315-EBD67C65F7B0)
- [REQUEST_SUMMARIZED_TREND_PROBLEMS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-7EBE8CCB-C270-4814-8C92-69B70A3BA20A)
- [REQUEST_SUMMARIZED_TREND_RESOURCE_RISK_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-71424E2C-15EE-4A66-BAF4-A2C171FCD0F7)
- [REQUEST_SUMMARIZED_TREND_RESPONDER_EXECUTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-D58B6F4B-D415-4865-855A-2C3F2329DF60)
- [REQUEST_SUMMARIZED_TREND_SECURITY_SCORES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-498DCB05-0196-47CE-9526-A525CF1C598C)
- [SKIP_BULK_RESPONDER_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B4187A9C-4ED5-4F62-BAA6-A64E0B0CE159)
- [SKIP_RESPONDER_EXECUTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-05D2B4D9-3F58-4BC7-99A6-D38CD5117410)
- [TRIGGER_RESPONDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-C036066B-11FD-4B0B-919C-BAEAAF5E62B8)
- [UPDATE_BULK_PROBLEM_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-8A969779-C6B2-43A5-89B3-DC0B3F6C5A2F)
- [UPDATE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-488804D2-0AEC-420C-9B97-CEAF7C0E59FB)
- [UPDATE_DATA_MASK_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-7A31AACC-E1AF-43E5-9740-D1C48FC6103A)
- [UPDATE_DATA_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-39E9D51D-C5D8-44BA-9F2A-C778A0678EFF)
- [UPDATE_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-2596ED87-4EE4-4236-9E67-808B168EAA09)
- [UPDATE_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-B4412FAA-7670-40D2-AC8F-BEF289A3A17C)
- [UPDATE_MANAGED_LIST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-370F4417-6A56-40A3-BCB8-7D8B312EE914)
- [UPDATE_PROBLEM_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-BC2751E8-B4E9-4FBD-BF70-035FA239B6F8)
- [UPDATE_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-EA32A52B-D8E3-4D92-8B1D-90A77847633B)
- [UPDATE_RESPONDER_RECIPE_RESPONDER_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-A306B55B-49DD-463F-95A2-E8B791661474)
- [UPDATE_SECURITY_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-31BCFCAC-B64F-43FC-BD4B-9CB0A9F73EB5)
- [UPDATE_SECURITY_ZONE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-6469AEA4-48A1-4EEC-8D63-0586D4FF9ABC)
- [UPDATE_TARGET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-935D5640-7C46-419B-ABE4-A495568B9604)
- [UPDATE_TARGET_DETECTOR_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-F8EF410A-09C9-466F-AF73-81CECCFF11B7)
- [UPDATE_TARGET_DETECTOR_RECIPE_DETECTOR_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-9175F6B9-BCC9-42E2-BD7C-E903DABE2289)
- [UPDATE_TARGET_RESPONDER_RECIPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-E2E2E2E0-0D82-4B40-8EDB-A40EC9F4E3DD)
- [UPDATE_TARGET_RESPONDER_RECIPE_RESPONDER_RULE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cg_cloud_guard.html#ADSDK-GUID-9CFCF16B-D057-49EB-BA3C-4255A26583F3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
