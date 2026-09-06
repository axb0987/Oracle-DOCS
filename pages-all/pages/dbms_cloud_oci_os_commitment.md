# One Subscription Commitment Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_commitment.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_commitment.html#dcoc-content-body)

## One Subscription Commitment Functions

Package: DBMS_CLOUD_OCI_OS_COMMITMENT

### GET_COMMITMENT Function

This API returns the commitment details corresponding to the id provided

Syntax
```

```

Parameters

Parameter Description

`commitment_id`

(required) The Commitment Id

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMMITMENTS Function

This list API returns all commitments for a particular Subscribed Service

Syntax
```

```

Parameters

Parameter Description

`subscribed_service_id`

(required) This param is used to get the commitments for a particular subscribed service

`compartment_id`

(required) The OCID of the root compartment.

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

- [One Subscription Commitment Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_commitment.html#ADSDK-GUID-1428D6FC-83C7-46F8-879D-154AB6B20410)
- [GET_COMMITMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_commitment.html#ADSDK-GUID-098EC370-F0B5-44DA-9DE9-1BC571D2FD2F)
- [LIST_COMMITMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_commitment.html#ADSDK-GUID-E2188D48-D747-4F96-A0CE-2FFBB8739654)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
