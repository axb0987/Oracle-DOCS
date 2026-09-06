# Limits Quotas Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#dcoc-content-body)

## Limits Quotas Functions

Package: DBMS_CLOUD_OCI_LM_QUOTAS

### ADD_QUOTA_LOCK Function

Adds a lock to a resource.

Syntax
```

```

Parameters

Parameter Description

`quota_id`

(required) The OCID of the quota.

`add_lock_details`

(required)

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_QUOTA Function

Creates a new quota with the details supplied.

Syntax
```

```

Parameters

Parameter Description

`create_quota_details`

(required) Request object for creating a new quota.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request can be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_QUOTA Function

Deletes the quota corresponding to the given OCID.

Syntax
```

```

Parameters

Parameter Description

`quota_id`

(required) The OCID of the quota.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_QUOTA Function

Gets the quota for the OCID specified.

Syntax
```

```

Parameters

Parameter Description

`quota_id`

(required) The OCID of the quota.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_QUOTAS Function

Lists all quotas on resources from the given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) name

`lifecycle_state`

(optional) Filters returned quotas based on the given state.

Allowed values are: 'ACTIVE'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. By default, it is ascending.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. Time created is default ordered as descending. Display name is default ordered as ascending.

Allowed values are: 'NAME', 'TIMECREATED'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_QUOTA_LOCK Function

Remove a lock from a resource.

Syntax
```

```

Parameters

Parameter Description

`quota_id`

(required) The OCID of the quota.

`remove_lock_details`

(required)

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_QUOTA Function

Updates the quota corresponding to given OCID with the details supplied.

Syntax
```

```

Parameters

Parameter Description

`quota_id`

(required) The OCID of the quota.

`update_quota_details`

(required) Request object for updating a quota.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Limits Quotas Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-EDB891A3-059D-4077-9A21-DC410D3B44D1)
- [ADD_QUOTA_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-C4A66C68-E6B0-4C01-ABDC-5DD80446E41E)
- [CREATE_QUOTA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-23836E32-05CF-48EF-8547-DE92B3B6FE61)
- [DELETE_QUOTA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-CF8D0819-350E-423C-B87C-8F7A7E6C9B1F)
- [GET_QUOTA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-2EDFC98E-ACE2-456C-8AC8-21E821B17F17)
- [LIST_QUOTAS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-A52C6EF7-926D-42D4-A152-6572C870294F)
- [REMOVE_QUOTA_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-F18E1972-E5EA-405D-8FB6-AC13581D6C68)
- [UPDATE_QUOTA Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_quotas.html#ADSDK-GUID-04F7D1B7-0773-4618-8069-DF41BA87BF8B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
