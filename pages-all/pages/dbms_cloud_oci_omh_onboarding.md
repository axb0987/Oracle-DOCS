# OS Management Hub Onboarding Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#dcoc-content-body)

## OS Management Hub Onboarding Functions

Package: DBMS_CLOUD_OCI_OMH_ONBOARDING

### CREATE_PROFILE Function

Creates a registration profile. A profile is a supplementary file for the OS Management Hub agentry that dictates the content for a managed instance at registration time.

Syntax
```

```

Parameters

Parameter Description

`create_profile_details`

(required) Details for the new registration profile.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PROFILE Function

Deletes a specified registration profile.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The OCID of the registration profile.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PROFILE Function

Gets information about the specified registration profile.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The OCID of the registration profile.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PROFILES Function

Lists registration profiles that match the specified compartment or profile OCID. Filter the list against a variety of criteria including but not limited to its name, status, vendor name, and architecture type.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) The OCID of the compartment that contains the resources to list.

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`profile_type`

(optional) A filter to return registration profiles that match the given profileType.

Allowed values are: 'SOFTWARESOURCE', 'GROUP', 'LIFECYCLE', 'STATION'

`profile_id`

(optional) The OCID of the registration profile.

`os_family`

(optional) A filter to return only profiles that match the given osFamily.

Allowed values are: 'ORACLE_LINUX_9', 'ORACLE_LINUX_8', 'ORACLE_LINUX_7'

`arch_type`

(optional) A filter to return only profiles that match the given archType.

Allowed values are: 'X86_64', 'AARCH64', 'I686', 'NOARCH', 'SRC'

`vendor_name`

(optional) A filter to return only profiles that match the given vendorName.

Allowed values are: 'ORACLE'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`lifecycle_state`

(optional) A filter to return only registration profile whose lifecycleState matches the given lifecycleState.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PROFILE Function

Updates the specified profile's name, description, and tags.

Syntax
```

```

Parameters

Parameter Description

`profile_id`

(required) The OCID of the registration profile.

`update_profile_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Hub Onboarding Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-BB5FBA21-3473-4E81-86D4-E79B6D609089)
- [CREATE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-58BAEB7E-41A6-4E8C-9C35-D7A065479818)
- [DELETE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-2157B000-2779-4C2A-90B7-F6F3CAE0862A)
- [GET_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-77C80B47-8BFB-4132-930D-D8FB926A606F)
- [LIST_PROFILES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-B8AC3AAD-AC1F-481C-95D9-F69E0B9ECA24)
- [UPDATE_PROFILE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_onboarding.html#ADSDK-GUID-28ED77CE-8622-46F0-88E0-82C4CAC699E5)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
