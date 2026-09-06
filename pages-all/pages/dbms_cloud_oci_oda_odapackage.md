# ODA ODA Package Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#dcoc-content-body)

## ODA ODA Package Functions

Package: DBMS_CLOUD_OCI_ODA_ODAPACKAGE

### CREATE_IMPORTED_PACKAGE Function

Starts an asynchronous job to import a package into a Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`create_imported_package_details`

(required) Parameter values required to import the package.

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IMPORTED_PACKAGE Function

Starts an asynchronous job to delete a package from a Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`package_id`

(required) Unique Digital Assistant package identifier.

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IMPORTED_PACKAGE Function

Returns a list of summaries for imported packages in the instance.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`package_id`

(required) Unique Digital Assistant package identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_PACKAGE Function

Returns details about a package, and how to import it.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`package_id`

(required) Unique Digital Assistant package identifier.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IMPORTED_PACKAGES Function

Returns a list of summaries for imported packages in the instance.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`name`

(optional) List only the information for the package with this name. Package names are unique to a publisher and may not change. Example: `My Package`

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_PACKAGES Function

Returns a page of summaries for packages that are available for import. The optional odaInstanceId query parameter can be used to filter packages that are available for import by a specific instance. If odaInstanceId query parameter is not provided, the returned list will include packages available within the region indicated by the request URL. The optional resourceType query param may be specified to filter packages that contain the indicated resource type. If no resourceType query param is given, packages containing all resource types will be returned. The optional name query parameter can be used to limit the list to packages whose name matches the given name. The optional displayName query parameter can be used to limit the list to packages whose displayName matches the given name. The optional isLatestVersionOnly query parameter can be used to limit the returned list to include only the latest version of any given package. If not specified, all versions of any otherwise matching package will be returned. If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter.

Syntax
```

```

Parameters

Parameter Description

`oda_instance_id`

(optional) List only the information for this Digital Assistant instance.

`resource_type`

(optional) Resource type identifier. Used to limit query results to the items which are applicable to the given type.

`compartment_id`

(optional) List the packages that belong to this compartment.

`name`

(optional) List only the information for the package with this name. Package names are unique to a publisher and may not change. Example: `My Package`

`display_name`

(optional) List only the information for the Digital Assistant instance with this user-friendly name. These names don't have to be unique and may change. Example: `My new resource`

`is_latest_version_only`

(optional) Should we return only the latest version of a package (instead of all versions)?

`limit`

(optional) The maximum number of items to return per page.

`page`

(optional) The page at which to start retrieving results. You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter. Example: `MToxMA==`

`sort_order`

(optional) Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) Sort on this field. You can specify one sort order only. The default sort field is `TIMECREATED`. The default sort order for `TIMECREATED` is descending, and the default sort order for `DISPLAYNAME` is ascending.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IMPORTED_PACKAGE Function

Starts an asynchronous job to update a package within a Digital Assistant instance. To monitor the status of the job, take the `opc-work-request-id` response header value and use it to call `GET /workRequests/{workRequestId}`.

Syntax
```

```

Parameters

Parameter Description

`update_imported_package_details`

(required) Parameter values required to import the package, with updated values.

`oda_instance_id`

(required) Unique Digital Assistant instance identifier.

`package_id`

(required) Unique Digital Assistant package identifier.

`is_replace_skills`

(optional) Should old skills be replaced by new skills if packageId differs from already imported package?

`opc_retry_token`

(optional) A token that uniquely identifies a request so that you can retry the request if there's a timeout or server error without the risk of executing that same action again. Retry tokens expire after 24 hours, but they can become invalid before then if there are conflicting operations. For example, if an instance was deleted and purged from the system, then the service might reject a retry of the original creation request.

`if_match`

(optional) For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.

`opc_request_id`

(optional) The client request ID for tracing. This value is included in the opc-request-id response header.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://digitalassistant-api.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [ODA ODA Package Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-DCEAB911-CCB8-4C9F-AB35-2DEA11600245)
- [CREATE_IMPORTED_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-3FBBD5C2-DADE-427C-94FB-982C1EB09F37)
- [DELETE_IMPORTED_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-818B61E3-2220-468E-AEAD-D2A7A8EA9D9B)
- [GET_IMPORTED_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-56B98300-FED9-426E-B330-470B974E9107)
- [GET_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-59D1BD90-CC99-4FCB-A4D1-B65CDCE98579)
- [LIST_IMPORTED_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-605042CD-4F99-46A9-BFE8-DEA925CEE6B8)
- [LIST_PACKAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-4B66259F-3091-4A97-BEBF-E556B01C7047)
- [UPDATE_IMPORTED_PACKAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oda_odapackage.html#ADSDK-GUID-2EBB45AA-9874-4276-A3B6-8895CF5BF039)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
