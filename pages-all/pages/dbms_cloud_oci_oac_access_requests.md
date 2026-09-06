# Operator Access Control Access Requests Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html
- Fetched: 2026-09-05 19:10 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#dcoc-content-body)

## Operator Access Control Access Requests Functions

Package: DBMS_CLOUD_OCI_OAC_ACCESS_REQUESTS

### APPROVE_ACCESS_REQUEST Function

Approves an access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`approve_access_request_details`

(required) Details regarding the approval of an access request created by the operator.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ACCESS_REQUEST Function

Gets details of an access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### INTERACTION_REQUEST Function

Posts query for additional information for the given access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`interaction_request_details`

(required) Details containing Query for additional information provided by Customer.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ACCESS_REQUEST_HISTORIES Function

Returns a history of all status associated with the accessRequestId.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ACCESS_REQUESTS Function

Lists all access requests in the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`resource_name`

(optional) A filter to return only resources that match the given ResourceName.

`resource_type`

(optional) A filter to return only lists of resources that match the entire given service type.

`lifecycle_state`

(optional) A filter to return only resources whose lifecycleState matches the given AccessRequest lifecycleState.

Allowed values are: 'CREATED', 'APPROVALWAITING', 'PREAPPROVED', 'APPROVED', 'MOREINFO', 'REJECTED', 'DEPLOYED', 'DEPLOYFAILED', 'UNDEPLOYED', 'UNDEPLOYFAILED', 'CLOSEFAILED', 'REVOKEFAILED', 'EXPIRYFAILED', 'REVOKING', 'REVOKED', 'EXTENDING', 'EXTENDED', 'EXTENSIONREJECTED', 'COMPLETING', 'COMPLETED', 'EXPIRED', 'APPROVEDFORFUTURE', 'INREVIEW'

`time_start`

(optional) Query start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd parameters are used together.

`time_end`

(optional) Query start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd parameters are used together.

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

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INTERACTIONS Function

Lists the MoreInformation interaction between customer and operators.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REJECT_ACCESS_REQUEST Function

Rejects an access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`reject_access_request_details`

(required) Details regarding the rejection of an access request created by the operator.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REVIEW_ACCESS_REQUEST Function

Reviews the access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`review_access_request_details`

(required) Details regarding the approval of an access request created by the operator.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REVOKE_ACCESS_REQUEST Function

Revokes an already approved access request.

Syntax
```

```

Parameters

Parameter Description

`access_request_id`

(required) unique AccessRequest identifier

`revoke_access_request_details`

(required) Details regarding the revocation of an access request created by the operator.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://operator-access-control.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Operator Access Control Access Requests Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-E31D0E96-66E0-45D9-8422-0B22933F626F)
- [APPROVE_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-6CFE7179-7EC9-4B39-B077-3652514E24BC)
- [GET_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-93B94A37-5749-4B96-8370-F1359DA267EA)
- [INTERACTION_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-298777A9-ACF4-4B78-8119-BEEE30F6D772)
- [LIST_ACCESS_REQUEST_HISTORIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-C60ED568-8B80-4CBE-974E-5A8D783A1897)
- [LIST_ACCESS_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-E4F96D6A-8E3B-418B-9392-80CF35C5FFD8)
- [LIST_INTERACTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-58129D24-75EE-471E-94FB-5FCD6688FA2A)
- [REJECT_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-6D5E6184-AB52-4D61-9981-D7E22D4A0F85)
- [REVIEW_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-D67B3CF9-22D6-4CB8-970A-2A2C0B6A5582)
- [REVOKE_ACCESS_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oac_access_requests.html#ADSDK-GUID-21C8D38E-2C79-4C0E-AB27-AE9A505312D3)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
