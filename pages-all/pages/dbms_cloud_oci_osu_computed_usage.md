# OSub Usage Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html#dcoc-content-body)

## OSub Usage Functions

Package: DBMS_CLOUD_OCI_OSU_COMPUTED_USAGE

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

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPUTED_USAGE_AGGREGATEDS Function

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

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

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

(optional) The maximum number of items to return in a paginated \"List\" call. Example: `500`

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`).

Allowed values are: 'timeCreated', 'timeOfArrival', 'timeMeteredOn'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`x_one_origin_region`

(optional) The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://csaap-e.oracle.com.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OSub Usage Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html#ADSDK-GUID-847660CE-DF6E-4366-AE45-97FBEB042998)
- [GET_COMPUTED_USAGE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html#ADSDK-GUID-54127D4E-2C2D-4C20-95E5-BCBD6AB01519)
- [LIST_COMPUTED_USAGE_AGGREGATEDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html#ADSDK-GUID-098ED9B0-BB0A-4352-9A90-79BE6E37BD0D)
- [LIST_COMPUTED_USAGES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_osu_computed_usage.html#ADSDK-GUID-06324872-9611-420E-9233-08BFE7B56D93)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
