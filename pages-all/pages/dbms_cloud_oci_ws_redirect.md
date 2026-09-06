# WAAS Redirect Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html
- Fetched: 2026-09-05 19:15 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#dcoc-content-body)

## WAAS Redirect Functions

Package: DBMS_CLOUD_OCI_WS_REDIRECT

### CHANGE_HTTP_REDIRECT_COMPARTMENT Function

Moves HTTP Redirect into a different compartment. When provided, If-Match is checked against ETag values of the WAAS policy.

Syntax
```

```

Parameters

Parameter Description

`http_redirect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`change_http_redirect_compartment_details`

(required)

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_HTTP_REDIRECT Function

Creates a new HTTP Redirect on the WAF edge.

Syntax
```

```

Parameters

Parameter Description

`create_http_redirect_details`

(required) The details of the HTTP Redirect.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_HTTP_REDIRECT Function

Deletes a redirect.

Syntax
```

```

Parameters

Parameter Description

`http_redirect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_HTTP_REDIRECT Function

Gets the details of a HTTP Redirect.

Syntax
```

```

Parameters

Parameter Description

`http_redirect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_HTTP_REDIRECTS Function

Gets a list of HTTP Redirects.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment. This number is generated when the compartment is created.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

`page`

(optional) The value of the `opc-next-page` response header from the previous paginated call.

`sort_order`

(optional) The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort the results of the List query.

Allowed values are: 'id', 'domain', 'target', 'displayName'

`id`

(optional) Filter redirects using a list of redirect OCIDs.

`display_name`

(optional) Filter redirects using a display name.

`lifecycle_state`

(optional) Filter redirects using a list of lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING', 'DELETED'

`time_created_greater_than_or_equal_to`

(optional) A filter that matches redirects created on or after the specified date and time.

`time_created_less_than`

(optional) A filter that matches redirects created before the specified date-time. Default to 1 day before now.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_HTTP_REDIRECT Function

Updates the details of a HTTP Redirect, including target and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged.

Syntax
```

```

Parameters

Parameter Description

`http_redirect_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the HTTP Redirect.

`update_http_redirect_details`

(required) The details of the HTTP Redirect to update.

`opc_request_id`

(optional) The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

`if_match`

(optional) For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://waas.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [WAAS Redirect Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-0E78B039-FE02-47D1-B685-79727650AE21)
- [CHANGE_HTTP_REDIRECT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-B5834C33-2EE5-45CE-B1DF-4BE08273615D)
- [CREATE_HTTP_REDIRECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-AB10D25E-CF92-4736-9B71-DA2306D31A44)
- [DELETE_HTTP_REDIRECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-CF667AE3-9FA8-48D0-9AC2-56A3C80CE09B)
- [GET_HTTP_REDIRECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-D4E2CB76-E1A6-40F4-893F-B6246AB32E03)
- [LIST_HTTP_REDIRECTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-9A6337B1-7DA2-49F0-A65E-2C37AFCD183C)
- [UPDATE_HTTP_REDIRECT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ws_redirect.html#ADSDK-GUID-545A97D2-6BD0-49B9-9871-21D0CF378883)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
