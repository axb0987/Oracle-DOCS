# Tenant Manager Control Plane Domain Governance Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#dcoc-content-body)

## Tenant Manager Control Plane Domain Governance Functions

Package: DBMS_CLOUD_OCI_TMCP_DOMAIN_GOVERNANCE

### CREATE_DOMAIN_GOVERNANCE Function

Adds domain governance to a claimed domain.

Syntax
```

```

Parameters

Parameter Description

`create_domain_governance_details`

(required) Parameters for adding domain governance to a claimed domain.

`opc_retry_token`

(optional) A token that uniquely identifies a request, so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request will be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DOMAIN_GOVERNANCE Function

Removes domain governance from a claimed domain.

Syntax
```

```

Parameters

Parameter Description

`domain_governance_id`

(required) The domain governance OCID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DOMAIN_GOVERNANCE Function

Gets information about the domain governance entity.

Syntax
```

```

Parameters

Parameter Description

`domain_governance_id`

(required) The domain governance OCID.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DOMAIN_GOVERNANCES Function

Return a (paginated) list of domain governance entities.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`domain_id`

(optional) The domain OCID.

`domain_governance_id`

(optional) The domain governance OCID.

`lifecycle_state`

(optional) The lifecycle state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`name`

(optional) A filter to return only resources that exactly match the name given.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DOMAIN_GOVERNANCE Function

Updates the domain governance entity.

Syntax
```

```

Parameters

Parameter Description

`domain_governance_id`

(required) The domain governance OCID.

`update_domain_governance_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Tenant Manager Control Plane Domain Governance Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-ED51600B-114A-4A81-9699-2B0A6A35FBEF)
- [CREATE_DOMAIN_GOVERNANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-CA235FEE-89C8-42C8-891B-AEBA40C18AAA)
- [DELETE_DOMAIN_GOVERNANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-FB45DD9A-DEF6-4C30-BE8F-6AFD46F113D6)
- [GET_DOMAIN_GOVERNANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-D3577E1A-4327-4B4D-8395-BD3E9484AF7B)
- [LIST_DOMAIN_GOVERNANCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-2EF540EA-7BAA-46FF-9953-D39BF5C7F979)
- [UPDATE_DOMAIN_GOVERNANCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_domain_governance.html#ADSDK-GUID-A5B0E590-C255-433D-8C93-1CF7FC406502)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
