# License Manager Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html
- Fetched: 2026-09-05 19:09 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#dcoc-content-body)

## License Manager Functions

Package: DBMS_CLOUD_OCI_LIM_LICENSE_MANAGER

### BULK_UPLOAD_LICENSE_RECORDS Function

Bulk upload the product licenses and license records for a given compartment.

Syntax
```

```

Parameters

Parameter Description

`bulk_upload_license_records_details`

(required) Details required for the bulk upload of product licenses and license records.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_LICENSE_RECORD Function

Creates a new license record for the given product license ID.

Syntax
```

```

Parameters

Parameter Description

`create_license_record_details`

(required) Details needed to create a new license record.

`product_license_id`

(required) Unique product license identifier.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_PRODUCT_LICENSE Function

Creates a new product license.

Syntax
```

```

Parameters

Parameter Description

`create_product_license_details`

(required) Details for creating a new product license.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_LICENSE_RECORD Function

Removes a license record.

Syntax
```

```

Parameters

Parameter Description

`license_record_id`

(required) Unique license record identifier.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_PRODUCT_LICENSE Function

Removes a product license.

Syntax
```

```

Parameters

Parameter Description

`product_license_id`

(required) Unique product license identifier.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_BULK_UPLOAD_TEMPLATE Function

Provides the bulk upload file template.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CONFIGURATION Function

Retrieves configuration for a compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LICENSE_METRIC Function

Retrieves the license metrics for a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_compartment_id_in_subtree`

(optional) Indicates if the given compartment is the root compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_LICENSE_RECORD Function

Retrieves license record details by the license record ID in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`license_record_id`

(required) Unique license record identifier.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PRODUCT_LICENSE Function

Retrieves product license details by product license ID in a given compartment.

Syntax
```

```

Parameters

Parameter Description

`product_license_id`

(required) Unique product license identifier.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_LICENSE_RECORDS Function

Retrieves all license records for a given product license ID.

Syntax
```

```

Parameters

Parameter Description

`product_license_id`

(required) Unique product license identifier.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_order`

(optional) The sort order to use, whether `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `expirationDate` * **expirationDate:** Sorts by expiration date of the license record.

Allowed values are: 'expirationDate'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRODUCT_LICENSE_CONSUMERS Function

Retrieves the product license consumers for a particular product license ID.

Syntax
```

```

Parameters

Parameter Description

`product_license_id`

(required) Unique product license identifier.

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_compartment_id_in_subtree`

(optional) Indicates if the given compartment is the root compartment.

`sort_order`

(optional) The sort order to use, whether `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `licenseUnitsRequired` * **licenseUnitsRequired:** Sorts by licenseUnitsRequired of the Resource.

Allowed values are: 'licenseUnitsRequired'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PRODUCT_LICENSES Function

Retrieves all the product licenses from a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_compartment_id_in_subtree`

(optional) Indicates if the given compartment is the root compartment.

`sort_order`

(optional) The sort order to use, whether `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `totalLicenseUnitsConsumed` * **totalLicenseUnitsConsumed:** Sorts by totalLicenseUnitsConsumed of ProductLicense.

Allowed values are: 'totalLicenseUnitsConsumed'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TOP_UTILIZED_PRODUCT_LICENSES Function

Retrieves the top utilized product licenses for a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_compartment_id_in_subtree`

(optional) Indicates if the given compartment is the root compartment.

`sort_order`

(optional) The sort order to use, whether `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `totalLicenseUnitsConsumed` * **totalLicenseUnitsConsumed:** Sorts by totalLicenseUnitsConsumed of ProductLicense.

Allowed values are: 'totalLicenseUnitsConsumed'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TOP_UTILIZED_RESOURCES Function

Retrieves the top utilized resources for a given compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_compartment_id_in_subtree`

(optional) Indicates if the given compartment is the root compartment.

`resource_unit_type`

(optional) A filter to return only resources whose unit matches the given resource unit.

Allowed values are: 'OCPU', 'ECPU'

`sort_order`

(optional) The sort order to use, whether `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Specifies the attribute with which to sort the rules. Default: `totalUnits` * **totalUnits:** Sorts by totalUnits consumed by resource.

Allowed values are: 'totalUnits'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CONFIGURATION Function

Updates the configuration for the compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The compartment[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)used for the license record, product license, and configuration.

`update_configuration_details`

(required) Configuration details that need to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_LICENSE_RECORD Function

Updates license record entity details.

Syntax
```

```

Parameters

Parameter Description

`license_record_id`

(required) Unique license record identifier.

`update_license_record_details`

(required) Details to update a license record entity.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_PRODUCT_LICENSE Function

Updates the list of images for a product license.

Syntax
```

```

Parameters

Parameter Description

`product_license_id`

(required) Unique product license identifier.

`update_product_license_details`

(required) The list of images that needs to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://licensemanager.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [License Manager Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-EED5E97A-C11E-48D2-83CD-569FD816FA43)
- [BULK_UPLOAD_LICENSE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-D80C5EFD-00EA-4BF1-A5AB-EB009DA08A60)
- [CREATE_LICENSE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-0821138D-EB82-4E8A-AB55-D76B46BCCDFF)
- [CREATE_PRODUCT_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-2FC5B073-440D-4BC0-A223-EFDA2E4BDE4B)
- [DELETE_LICENSE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-C5D94F15-21C0-451E-B5FD-1E69DF32E7E3)
- [DELETE_PRODUCT_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-6F74A000-CC2D-40E5-B8CF-2509CE170285)
- [GET_BULK_UPLOAD_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-5B09E0DB-5699-4436-92D3-32842C8A4DDE)
- [GET_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-EACE2867-4A32-4C02-BBD1-D2C961EF27D9)
- [GET_LICENSE_METRIC Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-2A517DB3-6E30-4B2B-A473-5040CB4C6D13)
- [GET_LICENSE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-E7070795-AE49-47C9-8276-45F4E58BDACD)
- [GET_PRODUCT_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-5AAA0DA1-B543-448E-9612-FB5816A2C2ED)
- [LIST_LICENSE_RECORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-F4DC95FE-908A-4C4D-92C5-36BE9EA9740E)
- [LIST_PRODUCT_LICENSE_CONSUMERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-FE846602-D5C7-47FC-B964-8387EB3209A3)
- [LIST_PRODUCT_LICENSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-DC53CF5D-A888-4294-BEE7-2EC75990B849)
- [LIST_TOP_UTILIZED_PRODUCT_LICENSES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-74B0B037-6D07-45C6-96E3-C8BDBFEB2BBB)
- [LIST_TOP_UTILIZED_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-A84FD353-4A91-4316-BDC7-171403139113)
- [UPDATE_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-BB43CC8C-701A-4767-8132-6CEF774FBF38)
- [UPDATE_LICENSE_RECORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-6DCD77BC-8919-43A5-BC68-2B0889DDB7D5)
- [UPDATE_PRODUCT_LICENSE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_lim_license_manager.html#ADSDK-GUID-7C06F808-5EBC-4FD3-98B8-64509456C5A8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
