# WAA Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#dcoc-content-body)

## WAA Functions

Package: DBMS_CLOUD_OCI_WAA_WAA

### CHANGE_WEB_APP_ACCELERATION_COMPARTMENT Function

Moves a Web App Acceleration resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`change_web_app_acceleration_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_WEB_APP_ACCELERATION_POLICY_COMPARTMENT Function

Moves a WebAppAccelerationfPolicy resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`change_web_app_acceleration_policy_compartment_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_WEB_APP_ACCELERATION Function

Creates a new WebAppAcceleration.

Syntax
```

```

Parameters

Parameter Description

`create_web_app_acceleration_details`

(required) Details for the new WebAppAcceleration.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_WEB_APP_ACCELERATION_POLICY Function

Creates a new WebAppAccelerationPolicy.

Syntax
```

```

Parameters

Parameter Description

`create_web_app_acceleration_policy_details`

(required) Details for the new WebAppAccelerationPolicy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WEB_APP_ACCELERATION Function

Deletes a WebAppAcceleration resource identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_WEB_APP_ACCELERATION_POLICY Function

Deletes a WebAppAccelerationPolicy resource identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WEB_APP_ACCELERATION Function

Gets a WebAppAcceleration by OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WEB_APP_ACCELERATION_POLICY Function

Gets a WebAppAccelerationPolicy with the given OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WEB_APP_ACCELERATION_POLICIES Function

Gets a list of all WebAppAccelerationPolicies in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`id`

(optional) A filter to return only the WebAppAccelerationPolicy with the given[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WEB_APP_ACCELERATIONS Function

Gets a list of all WebAppAccelerations in a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment in which to list resources.

`id`

(optional) A filter to return only the WebAppAcceleration with the given[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`web_app_acceleration_policy_id`

(optional) A filter to return only the WebAppAcceleration with the given[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of related WebAppAccelerationPolicy.

`lifecycle_state`

(optional) A filter to return only resources that match the given lifecycleState.

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PURGE_WEB_APP_ACCELERATION_CACHE Function

Clears resources from the cache of the WebAppAcceleration. Each new request for a purged resource will be forwarded to the origin server to fetch a new version of the resource.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`purge_web_app_acceleration_cache_details`

(required) Options for the cache purge.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_WEB_APP_ACCELERATION Function

Updates the WebAppAcceleration identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAcceleration.

`update_web_app_acceleration_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_WEB_APP_ACCELERATION_POLICY Function

Update the WebAppAccelerationPolicy identified by the OCID.

Syntax
```

```

Parameters

Parameter Description

`web_app_acceleration_policy_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the WebAppAccelerationPolicy.

`update_web_app_acceleration_policy_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waa.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [WAA Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-C5C7376C-3D8F-47F1-A6A0-80B2BAF8C827)
- [CHANGE_WEB_APP_ACCELERATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-5DFF17EC-4F65-446F-8374-774A2919D862)
- [CHANGE_WEB_APP_ACCELERATION_POLICY_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-E4B90058-949F-4B26-9ABC-B3567C6C7792)
- [CREATE_WEB_APP_ACCELERATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-9D798F69-2528-460F-8D67-A243589FDF09)
- [CREATE_WEB_APP_ACCELERATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-2D654ECC-1F63-4FA5-A728-6F77656356BA)
- [DELETE_WEB_APP_ACCELERATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-D79DED42-7744-47DA-864D-086B2BD22F33)
- [DELETE_WEB_APP_ACCELERATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-46678B02-9D99-42E0-B64A-68AB24DF9097)
- [GET_WEB_APP_ACCELERATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-509FFA61-5541-4F12-AA95-2CDAC9B9DBA6)
- [GET_WEB_APP_ACCELERATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-A2535BD7-15FC-4F9C-9FBF-D95D584529EE)
- [LIST_WEB_APP_ACCELERATION_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-7BA8AB3D-B504-4A53-AB77-953B59DDD4E5)
- [LIST_WEB_APP_ACCELERATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-42D8125C-1CF9-451F-9006-6329914525F7)
- [PURGE_WEB_APP_ACCELERATION_CACHE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-EB2C04F3-33D6-41EB-BF23-23E208EB1CD2)
- [UPDATE_WEB_APP_ACCELERATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-6BA0CFCF-1916-43B8-8E41-0E5F8A6E9493)
- [UPDATE_WEB_APP_ACCELERATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_waa_waa.html#ADSDK-GUID-2CC69DA6-9085-4660-AC0C-A7263D8F5141)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
