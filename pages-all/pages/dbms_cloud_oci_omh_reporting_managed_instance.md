# OS Management Hub Reporting Managed Instance Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html
- Fetched: 2026-09-05 19:11 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html#dcoc-content-body)

## OS Management Hub Reporting Managed Instance Functions

Package: DBMS_CLOUD_OCI_OMH_REPORTING_MANAGED_INSTANCE

### GET_MANAGED_INSTANCE_ANALYTIC_CONTENT Function

Returns a CSV format report of managed instances matching the given filters.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(optional) This compartmentId is used to list managed instances within a compartment. Or serve as an additional filter to restrict only managed instances with in certain compartment if other filter presents.

`managed_instance_group_id`

(optional) The OCID of the managed instance group for which to list resources.

`lifecycle_environment_id`

(optional) The OCID of the lifecycle environment.

`lifecycle_stage_id`

(optional) The OCID of the lifecycle stage for which to list resources.

`status`

(optional) A filter to return only instances whose managed instance status matches the given status.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING', 'REGISTRATION_ERROR'

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`instance_location`

(optional) Filter instances by Location. Used when report target type is compartment or group.

Allowed values are: 'ON_PREMISE', 'OCI_COMPUTE', 'AZURE', 'EC2'

`security_updates_available_equals_to`

(optional) A filter to return instances with number of available security updates equals to the number specified.

`bug_updates_available_equals_to`

(optional) A filter to return instances with number of available bug updates equals to the number specified.

`security_updates_available_greater_than`

(optional) A filter to return instances with number of available security updates greater than the number specified.

`bug_updates_available_greater_than`

(optional) A filter to return instances with number of available bug updates greater than the number specified.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MANAGED_INSTANCE_CONTENT Function

Returns a CSV format report of a single managed instance whose associated Erratas match the given filters.

Syntax
```

```

Parameters

Parameter Description

`managed_instance_id`

(required) The OCID of the managed instance.

`advisory_name`

(optional) The assigned erratum name. It's unique and not changeable. Example: `ELSA-2020-5804`

`advisory_name_contains`

(optional) A filter to return resources that may partially match the erratum advisory name given.

`advisory_type`

(optional) A filter to return only errata that match the given advisory types.

Allowed values are: 'SECURITY', 'BUGFIX', 'ENHANCEMENT'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### SUMMARIZE_MANAGED_INSTANCE_ANALYTICS Function

Returns a list of user specified metrics for a collection of managed instances.

Syntax
```

```

Parameters

Parameter Description

`metric_names`

(required) A filter to return only metrics whose name matches the given metric names.

Allowed values are: 'TOTAL_INSTANCE_COUNT', 'INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT', 'INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT', 'NORMAL_INSTANCE_COUNT', 'ERROR_INSTANCE_COUNT', 'WARNING_INSTANCE_COUNT', 'UNREACHABLE_INSTANCE_COUNT', 'REGISTRATION_FAILED_INSTANCE_COUNT', 'INSTANCE_SECURITY_UPDATES_COUNT', 'INSTANCE_BUGFIX_UPDATES_COUNT'

`compartment_id`

(optional) This compartmentId is used to list managed instances within a compartment. Or serve as an additional filter to restrict only managed instances with in certain compartment if other filter presents.

`managed_instance_group_id`

(optional) The OCID of the managed instance group for which to list resources.

`lifecycle_environment_id`

(optional) The OCID of the lifecycle environment.

`lifecycle_stage_id`

(optional) The OCID of the lifecycle stage for which to list resources.

`status`

(optional) A filter to return only instances whose managed instance status matches the given status.

Allowed values are: 'NORMAL', 'UNREACHABLE', 'ERROR', 'WARNING', 'REGISTRATION_ERROR'

`display_name`

(optional) A filter to return resources that match the given display names.

`display_name_contains`

(optional) A filter to return resources that may partially match the given display name.

`instance_location`

(optional) Filter instances by Location. Used when report target type is compartment or group.

Allowed values are: 'ON_PREMISE', 'OCI_COMPUTE', 'AZURE', 'EC2'

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `50`

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine). Example: `3`

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for name is ascending.

Allowed values are: 'name'

`sort_order`

(optional) The sort order to use, either 'ASC' or 'DESC'.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://osmh.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [OS Management Hub Reporting Managed Instance Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html#ADSDK-GUID-F3D20AB9-6D96-476A-9C40-7B6E6DF7EFB6)
- [GET_MANAGED_INSTANCE_ANALYTIC_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html#ADSDK-GUID-18987EF9-9476-496A-8234-99B56EA20775)
- [GET_MANAGED_INSTANCE_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html#ADSDK-GUID-B258FF15-99C2-45FE-9B06-41EF18BF1495)
- [SUMMARIZE_MANAGED_INSTANCE_ANALYTICS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_omh_reporting_managed_instance.html#ADSDK-GUID-9A306B02-F98B-44B5-8741-AF3CC1F47992)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
