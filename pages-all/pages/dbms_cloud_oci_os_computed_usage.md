# One Subscription Computed Usage Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html
- Fetched: 2026-09-05 19:12 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html#dcoc-content-body)

## One Subscription Computed Usage Functions

Package: DBMS_CLOUD_OCI_OS_COMPUTED_USAGE

### GET_COMPUTED_USAGE Function

This is an API which returns Computed Usage corresponding to the id passed

Syntax
```

```

Parameters

Parameter Description

`computed_usage_id`

(required) The Computed Usage Id

`compartment_id`

(required) The OCID of the root compartment.

`fields`

(optional) Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AGGREGATED_COMPUTED_USAGES Function

This is a collection API which returns a list of aggregated computed usage details (there can be multiple Parent Products under a given SubID each of which is represented under Subscription Service Line # in SPM).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`subscription_id`

(required) Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.

`time_from`

(required) Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.

`time_to`

(required) Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.

`parent_product`

(optional) Product part number for subscribed service line, called parent product.

`grouping`

(optional) Grouping criteria to use for aggregate the computed Usage, either hourly (`HOURLY`), daily (`DAILY`), monthly(`MONTHLY`) or none (`NONE`) to not follow a grouping criteria by date.

Allowed values are: 'HOURLY', 'DAILY', 'MONTHLY', 'NONE'

`limit`

(optional) The maximum number aggregatedComputedUsages of items to return within the Subscription \"List\" call, this counts the overall count across all items Example: `500`

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTED_USAGES Function

This is a collection API which returns a list of Computed Usages for given filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the root compartment.

`subscription_id`

(required) Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.

`time_from`

(required) Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.

`time_to`

(required) Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.

`parent_product`

(optional) Product part number for subscribed service line, called parent product.

`computed_product`

(optional) Product part number for Computed Usage .

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. Default: (`50`) Example: '500'

`page`

(optional) The value of the 'opc-next-page' response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending ('ASC') or descending ('DESC').

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`).

Allowed values are: 'timeCreated', 'timeOfArrival', 'timeMeteredOn'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [One Subscription Computed Usage Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html#ADSDK-GUID-48ED15A5-1F2A-430A-B52A-4800E6C70B8E)
- [GET_COMPUTED_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html#ADSDK-GUID-B0A410FD-CDFD-4086-AA15-7BFBEBFCB3E4)
- [LIST_AGGREGATED_COMPUTED_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html#ADSDK-GUID-4085C428-984A-4658-BC9B-7B456FC24836)
- [LIST_COMPUTED_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_os_computed_usage.html#ADSDK-GUID-674E7489-7257-42BE-BE20-96CA506EDB73)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
