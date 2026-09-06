# Limits Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#dcoc-content-body)

## Limits Functions

Package: DBMS_CLOUD_OCI_LM_LIMITS

### GET_RESOURCE_AVAILABILITY Function

For a given compartmentId, resource limit name, and scope, returns the following: * The number of available resources associated with the given limit. * The usage in the selected compartment for the given limit. Note that not all resource limits support this API. If the value is not available, the API returns a 404 response.

Syntax
```

```

Parameters

Parameter Description

`service_name`

(required) The service name of the target quota.

`limit_name`

(required) The limit name for which to fetch the data.

`compartment_id`

(required) The OCID of the compartment for which data is being fetched.

`availability_domain`

(optional) This field is mandatory if the scopeType of the target resource limit is AD. Otherwise, this field should be omitted. If the above requirements are not met, the API returns a 400 - InvalidParameter response.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIMIT_DEFINITIONS Function

Includes a list of resource limits that are currently supported. If the 'areQuotasSupported' property is true, you can create quota policies on top of this limit at the compartment level.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

`service_name`

(optional) The target service name.

`name`

(optional) Optional field, filter for a specific resource limit.

`sort_by`

(optional) The field to sort by.

Allowed values are: 'name', 'description'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. By default, it is ascending.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LIMIT_VALUES Function

Includes a full list of resource limits belonging to a given service.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

`service_name`

(required) The target service name.

`scope_type`

(optional) Filter entries by scope type.

Allowed values are: 'GLOBAL', 'REGION', 'AD'

`availability_domain`

(optional) Filter entries by availability domain. This implies that only AD-specific values are returned.

`name`

(optional) Optional field, can be used to see a specific resource limit value.

`sort_by`

(optional) The field to sort by. The sorting is by availabilityDomain, as a second level field, if available.

Allowed values are: 'name'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. By default, it is ascending.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICES Function

Returns the list of supported services. This includes the programmatic service name, along with the friendly service name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

`sort_by`

(optional) The field to sort by.

Allowed values are: 'name', 'description'

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'. By default, it is ascending.

Allowed values are: 'ASC', 'DESC'

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://limits.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Limits Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#ADSDK-GUID-AC5E5F67-FE49-4271-8B23-15A422D7BCE0)
- [GET_RESOURCE_AVAILABILITY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#ADSDK-GUID-C80D1B59-09E5-4575-A8DF-C8D330995C03)
- [LIST_LIMIT_DEFINITIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#ADSDK-GUID-997A7FC0-FDE0-4DC9-B8B8-37CD13BFC200)
- [LIST_LIMIT_VALUES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#ADSDK-GUID-191CEE42-B19F-42E2-84FB-0BCB03C46355)
- [LIST_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lm_limits.html#ADSDK-GUID-3D491E96-3432-4C65-A9E4-031AFBB19DF2)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
