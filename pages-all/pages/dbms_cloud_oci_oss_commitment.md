# OSub Subscription Commitment Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_commitment.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_commitment.html#dcoc-content-body)

## OSub Subscription Commitment Functions

Package: DBMS_CLOUD_OCI_OSS_COMMITMENT

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

`x_one_gateway_subscription_id`

(optional) This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

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

(required) The OCID of the compartment.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: `500`

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`).

Allowed values are: 'TIMECREATED', 'TIMESTART'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`x_one_gateway_subscription_id`

(optional) This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSub Subscription Commitment Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_commitment.html#ADSDK-GUID-823D5C2C-33F7-4476-A8B7-4B086745711E)
- [GET_COMMITMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_commitment.html#ADSDK-GUID-BBCE499C-6AFC-4DF9-B48D-0D777A7F4E21)
- [LIST_COMMITMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_oss_commitment.html#ADSDK-GUID-36C58432-2859-4842-90EC-5BB682B47E6B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
