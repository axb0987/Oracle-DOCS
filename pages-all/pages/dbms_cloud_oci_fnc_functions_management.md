# Functions Management Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html
- Fetched: 2026-09-05 19:07 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#dcoc-content-body)

## Functions Management Functions

Package: DBMS_CLOUD_OCI_FNC_FUNCTIONS_MANAGEMENT

### CHANGE_APPLICATION_COMPARTMENT Function

Moves an application into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources Between Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

Syntax
```

```

Parameters

Parameter Description

`application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this application.

`change_application_compartment_details`

(required) Properties to change the compartment of an application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_APPLICATION Function

Creates a new application.

Syntax
```

```

Parameters

Parameter Description

`create_application_details`

(required) Specification of the application to create

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_FUNCTION Function

Creates a new function.

Syntax
```

```

Parameters

Parameter Description

`create_function_details`

(required) Specification of the function to create

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_APPLICATION Function

Deletes an application.

Syntax
```

```

Parameters

Parameter Description

`application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this application.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_FUNCTION Function

Deletes a function.

Syntax
```

```

Parameters

Parameter Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this function.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_APPLICATION Function

Retrieves an application.

Syntax
```

```

Parameters

Parameter Description

`application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this application.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_FUNCTION Function

Retrieves a function.

Syntax
```

```

Parameters

Parameter Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this function.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PBF_LISTING Function

Fetches a Pre-built Function(PBF) Listing. Returns a PbfListing response model.

Syntax
```

```

Parameters

Parameter Description

`pbf_listing_id`

(required) unique PbfListing identifier

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PBF_LISTING_VERSION Function

Gets a PbfListingVersion by identifier for a PbfListing.

Syntax
```

```

Parameters

Parameter Description

`pbf_listing_version_id`

(required) unique PbfListingVersion identifier

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_APPLICATIONS Function

Lists applications for a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to which this resource belongs.

`limit`

(optional) The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10

`page`

(optional) The pagination token for a list query returned by a previous operation

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`lifecycle_state`

(optional) A filter to return only applications that match the lifecycle state in this parameter. Example: `Creating`

`display_name`

(optional) A filter to return only applications with display names that match the display name string. Matching is exact.

`id`

(optional) A filter to return only applications with the specified OCID.

`sort_order`

(optional) Specifies sort order. * **ASC:** Ascending sort order. * **DESC:** Descending sort order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `displayName` * **timeCreated:** Sorts by timeCreated. * **displayName:** Sorts by displayName. * **id:** Sorts by id.

Allowed values are: 'timeCreated', 'id', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FUNCTIONS Function

Lists functions for an application.

Syntax
```

```

Parameters

Parameter Description

`application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application to which this function belongs.

`limit`

(optional) The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10

`page`

(optional) The pagination token for a list query returned by a previous operation

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`lifecycle_state`

(optional) A filter to return only functions that match the lifecycle state in this parameter. Example: `Creating`

`display_name`

(optional) A filter to return only functions with display names that match the display name string. Matching is exact.

`id`

(optional) A filter to return only functions with the specified OCID.

`sort_order`

(optional) Specifies sort order. * **ASC:** Ascending sort order. * **DESC:** Descending sort order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `displayName` * **timeCreated:** Sorts by timeCreated. * **displayName:** Sorts by displayName. * **id:** Sorts by id.

Allowed values are: 'timeCreated', 'id', 'displayName'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PBF_LISTING_VERSIONS Function

Fetches a wrapped list of all Pre-built Function(PBF) Listing versions. Returns a PbfListingVersionCollection containing an array of PbfListingVersionSummary response models. Note that the PbfListingIdentifier must be provided as a query parameter, otherwise an exception shall be thrown.

Syntax
```

```

Parameters

Parameter Description

`pbf_listing_id`

(required) unique PbfListing identifier

`pbf_listing_version_id`

(optional) unique PbfListingVersion identifier

`name`

(optional) Matches a PbfListingVersion based on a provided semantic version name for a PbfListingVersion. Each PbfListingVersion name is unique with respect to its associated PbfListing.

`is_current_version`

(optional) Matches the current version (the most recently added version with an Active lifecycleState) associated with a PbfListing.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`limit`

(optional) The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10

`page`

(optional) The pagination token for a list query returned by a previous operation

`sort_order`

(optional) Specifies sort order. * **ASC:** Ascending sort order. * **DESC:** Descending sort order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PBF_LISTINGS Function

Fetches a wrapped list of all Pre-built Function(PBF) Listings. Returns a PbfListingCollection containing an array of PbfListingSummary response models.

Syntax
```

```

Parameters

Parameter Description

`pbf_listing_id`

(optional) unique PbfListing identifier

`name`

(optional) A filter to return only resources that match the entire PBF name given.

`name_contains`

(optional) A filter to return only resources that contain the supplied filter text in the PBF name given.

`name_starts_with`

(optional) A filter to return only resources that start with the supplied filter text in the PBF name given.

`trigger`

(optional) A filter to return only resources that match the service trigger sources of a PBF.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

`limit`

(optional) The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10

`page`

(optional) The pagination token for a list query returned by a previous operation

`sort_order`

(optional) Specifies sort order. * **ASC:** Ascending sort order. * **DESC:** Descending sort order.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending.

Allowed values are: 'timeCreated', 'name'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TRIGGERS Function

Returns a list of Triggers.

Syntax
```

```

Parameters

Parameter Description

`name`

(optional) A filter to return only resources that match the service trigger source of a PBF.

`limit`

(optional) The maximum number of items to return. 1 is the minimum, 50 is the maximum. Default: 10

`page`

(optional) The pagination token for a list query returned by a previous operation

`sort_order`

(optional) Specifies sort order. * **ASC:** Ascending sort order. * **DESC:** Descending sort order.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_APPLICATION Function

Modifies an application

Syntax
```

```

Parameters

Parameter Description

`application_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this application.

`update_application_details`

(required) The new application spec to apply

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_FUNCTION Function

Modifies a function

Syntax
```

```

Parameters

Parameter Description

`function_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of this function.

`update_function_details`

(required) The new function spec to apply

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://functions.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Functions Management Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-D7182F6F-018F-4237-AB56-0B6ACD12D616)
- [CHANGE_APPLICATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-78AFC15F-035D-498A-9C0C-9F90A7441883)
- [CREATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-59B6D2C1-4641-4311-AD45-459A58916105)
- [CREATE_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-DD14C610-3748-4822-A4BC-62A1454C5C5F)
- [DELETE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-86FFD746-E79D-4CE0-A505-B46C71989AD4)
- [DELETE_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-A2E1957E-052B-48EC-906B-05D3FDC190D6)
- [GET_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-53125874-D7A9-4E26-AFD2-2B3F1B773724)
- [GET_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-D4A1A7C1-A872-4184-B2A1-FD6ACBE5EA83)
- [GET_PBF_LISTING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-75472D8C-38C3-4148-ACFE-3D2E0E03346E)
- [GET_PBF_LISTING_VERSION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-F850AF8C-31D9-4ACC-BD42-1386D49D334E)
- [LIST_APPLICATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-70ADF4E3-FD3D-4554-A6B2-C8A557B0705C)
- [LIST_FUNCTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-025B6E34-231E-4DA7-ACBC-84A74BCADD64)
- [LIST_PBF_LISTING_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-40724B63-E7EC-4877-BA4B-CE01D8462B32)
- [LIST_PBF_LISTINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-EE28D4D6-A0F8-483D-BCC0-41E7A23000CA)
- [LIST_TRIGGERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-F47521BB-496C-4F0E-B121-45FBABB324A2)
- [UPDATE_APPLICATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-1A196131-E9AA-485B-B946-749BE17D18FD)
- [UPDATE_FUNCTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_fnc_functions_management.html#ADSDK-GUID-6BF66F66-C6FE-447D-BCB5-76FE5E617640)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
