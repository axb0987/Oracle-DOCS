# Threat Intelligence Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#dcoc-content-body)

## Threat Intelligence Functions

Package: DBMS_CLOUD_OCI_TI_THREATINTEL

### GET_INDICATOR Function

Get detailed information about a threat indicator with a given identifier.

Syntax
```

```

Parameters

Parameter Description

`indicator_id`

(required) The unique identifier (OCID) of the threat indicator.

`compartment_id`

(required) The OCID of the tenancy (root compartment) that is used to filter results.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://api-threatintel.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INDICATOR_COUNTS Function

Get the current count of each threat indicator type. Indicator counts can be sorted in ascending or descending order.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the tenancy (root compartment) that is used to filter results.

`opc_request_id`

(optional) The client request ID for tracing.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://api-threatintel.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INDICATORS Function

Get a list of threat indicator summaries based on the search criteria.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the tenancy (root compartment) that is used to filter results.

`threat_type_name`

(optional) The threat type of entites to be returned. To filter for multiple threat types, repeat this parameter.

`l_type`

(optional) The indicator type of entities to be returned.

Allowed values are: 'DOMAIN_NAME', 'FILE_NAME', 'MD5_HASH', 'SHA1_HASH', 'SHA256_HASH', 'IP_ADDRESS', 'URL'

`value`

(optional) The indicator value of entities to be returned.

`confidence_greater_than_or_equal_to`

(optional) The minimum confidence score of entities to be returned.

`time_updated_greater_than_or_equal_to`

(optional) The oldest update time of entities to be returned.

`time_updated_less_than`

(optional) Return indicators updated before the provided time.

`time_last_seen_greater_than_or_equal_to`

(optional) The oldest last seen time of entities to be returned.

`time_last_seen_less_than`

(optional) Return indicators last seen before the provided time.

`time_created_greater_than_or_equal_to`

(optional) The oldest created/first seen time of entities to be returned.

`time_created_less_than`

(optional) Return indicators created/first seen before the provided time.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one field to sort by may be provided.

Allowed values are: 'confidence', 'timeCreated', 'timeUpdated', 'timeLastSeen'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://api-threatintel.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_THREAT_TYPES Function

Gets a list of threat types that are available to use as parameters when querying indicators. The list is sorted by threat type name according to the sort order query param.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the tenancy (root compartment) that is used to filter results.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://api-threatintel.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_INDICATORS Function

Get indicator summaries based on advanced search criteria.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the tenancy (root compartment) that is used to filter results.

`summarize_indicators_details`

(required) Query Parameters to search for indicators.

`opc_request_id`

(optional) The client request ID for tracing.

`limit`

(optional) The maximum number of items to return.

`page`

(optional) A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://api-threatintel.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Threat Intelligence Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-082D9E8B-9F51-427A-8BB0-36570433BC89)
- [GET_INDICATOR Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-2E10990E-7CCF-4EB9-8578-B21771DCA15C)
- [LIST_INDICATOR_COUNTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-B3554C07-77D1-4D1A-8E3C-B86F3BDFEB07)
- [LIST_INDICATORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-AEED81CD-141A-412E-9454-DE2D557DB4D6)
- [LIST_THREAT_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-EBD22BA5-7858-4855-96A1-4DBFF23F051D)
- [SUMMARIZE_INDICATORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ti_threatintel.html#ADSDK-GUID-A7435E02-F53C-4039-8573-DAF73AC81526)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
