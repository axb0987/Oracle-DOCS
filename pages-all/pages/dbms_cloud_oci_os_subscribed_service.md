# One Subscription Subscribed Service Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscribed_service.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscribed_service.html#dcoc-content-body)

## One Subscription Subscribed Service Functions

Package: DBMS_CLOUD_OCI_OS_SUBSCRIBED_SERVICE

### GET_SUBSCRIBED_SERVICE Function

This API returns the subscribed service details corresponding to the id provided

Syntax
```

```

Parameters

Parameter Description

`subscribed_service_id`

(required) The Subscribed Service Id

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. In this mechanism, the client sends the required field names as the query parameters for an API to the server, and the server trims down the default response content by removing the fields that are not required by the client. The parameter used to control what fields to return should be a query string parameter called \"fields\" of type array, and usecollectionFormat

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SUBSCRIBED_SERVICES Function

This list API returns all subscribed services for given Subscription ID

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`subscription_id`

(required) Line level Subscription Id

`order_line_id`

(optional) Order Line identifier at subscribed service level . This identifier is originated in Order Management module. Default is null.

`status`

(optional) This param is used to filter subscribed services based on its status

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: '500'

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order ('sortOrder').

Allowed values are: 'ORDERNUMBER', 'TIMEINVOICING'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [One Subscription Subscribed Service Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscribed_service.html#ADSDK-GUID-053E10CD-854D-4DC1-9A09-8D68D94E9AD9)
- [GET_SUBSCRIBED_SERVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscribed_service.html#ADSDK-GUID-91B041BF-9454-4BA0-AA57-C6C03BE92FEC)
- [LIST_SUBSCRIBED_SERVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_subscribed_service.html#ADSDK-GUID-FC9BC8BF-A2B7-4FCB-AB6F-C0AB51E99C78)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
