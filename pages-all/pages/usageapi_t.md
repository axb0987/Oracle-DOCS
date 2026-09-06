# Usage API Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#dcoc-content-body)

## Usage API Common Types

### DBMS_CLOUD_OCI_USAGEAPI_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_AVERAGE_CARBON_EMISSION_T Type

Average carbon emission.

Syntax
```

```

Fields

Field Description

`sku_part_number`

(required) The sku part number.

`average_carbon_emission`

(required) The average carbon emissions by SKU.

### DBMS_CLOUD_OCI_USAGEAPI_CLEAN_ENERGY_USAGE_T Type

Clean energy usage.

Syntax
```

```

Fields

Field Description

`l_region`

(required) The region.

`ad`

(optional) The availability domain.

`usage`

(required) The percentage of clean enery used.

### DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_T Type

A configuration.

Syntax
```

```

Fields

Field Description

`key`

(required) The configuration key.

`l_values`

(optional) The configuration value.

### DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_TBL Type

Nested table type of dbms_cloud_oci_usageapi_configuration_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_AGGREGATION_T Type

The available configurations.

Syntax
```

```

Fields

Field Description

`items`

(required) The list of available configurations.

### DBMS_CLOUD_OCI_USAGEAPI_COST_ANALYSIS_UI_T Type

The common fields for Cost Analysis UI rendering.

Syntax
```

```

Fields

Field Description

`graph`

(optional) The graph type.

Allowed values are: 'BARS', 'LINES', 'STACKED_LINES'

`is_cumulative_graph`

(optional) A cumulative graph.

### DBMS_CLOUD_OCI_USAGEAPI_TAG_T Type

The tag used for filtering.

Syntax
```

```

Fields

Field Description

`namespace`

(optional) The tag namespace.

`key`

(optional) The tag key.

`value`

(optional) The tag value.

### DBMS_CLOUD_OCI_USAGEAPI_TAG_TBL Type

Nested table type of dbms_cloud_oci_usageapi_tag_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_SAVED_CUSTOM_TABLE_T Type

The custom table for Cost Analysis UI rendering.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name of the custom table.

`row_group_by`

(optional) The row groupBy key list. example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\"]`

`column_group_by`

(optional) The column groupBy key list. example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\"]`

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only one tag in the list is supported. For example: `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

`compartment_depth`

(optional) The compartment depth level.

`version`

(optional) The version of the custom table.

### DBMS_CLOUD_OCI_USAGEAPI_CREATE_CUSTOM_TABLE_DETAILS_T Type

New custom table detail.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID.

`saved_report_id`

(required) The associated saved report OCID.

`saved_custom_table`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_FORECAST_T Type

Forecast configuration of usage/cost.

Syntax
```

```

Fields

Field Description

`forecast_type`

(optional) BASIC uses the exponential smoothing (ETS) model to project future usage/costs based on history data. The basis for projections is a periodic set of equivalent historical days for which the projection is being made.

Allowed values are: 'BASIC'

`time_forecast_started`

(optional) The forecast start time. Defaults to UTC-1 if not specified.

`time_forecast_ended`

(required) The forecast end time.

### DBMS_CLOUD_OCI_USAGEAPI_DIMENSION_T Type

The dimension used for filtering. Availabe dimensions are: \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", and \"tenantName\". For example: `[{value: \"COMPUTE\", key: \"service\"}]`

Syntax
```

```

Fields

Field Description

`key`

(required) The dimension key.

`value`

(required) The dimension value.

### DBMS_CLOUD_OCI_USAGEAPI_DIMENSION_TBL Type

Nested table type of dbms_cloud_oci_usageapi_dimension_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_FILTER_ABS_T

The filter object for query usage.

Syntax
```

```

Fields

Field Description

`operator`

(optional) The filter operator. Example: 'AND', 'OR', 'NOT'.

Allowed values are: 'AND', 'NOT', 'OR'

`dimensions`

(optional) The dimensions to filter on.

`tags`

(optional) The tags to filter on.

### DBMS_CLOUD_OCI_USAGEAPI_FILTER_ABS_TBL Type

Nested table type of dbms_cloud_oci_usageapi_filter_abs_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_FILTER_T Type

The filter object for query usage.

Syntax
```

```

Fields

Field Description

`filters`

(optional) The nested filter object.

### DBMS_CLOUD_OCI_USAGEAPI_FILTER_TBL Type

Nested table type of dbms_cloud_oci_usageapi_filter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_REPORT_QUERY_T Type

The request of the generated Cost Analysis report.

Syntax
```

```

Fields

Field Description

`tenant_id`

(required) Tenant ID.

`time_usage_started`

(optional) The usage start time.

`time_usage_ended`

(optional) The usage end time.

`granularity`

(required) The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.

Allowed values are: 'HOURLY', 'DAILY', 'MONTHLY', 'TOTAL'

`is_aggregate_by_time`

(optional) Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.

`forecast`

(optional)

`query_type`

(optional) The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data AllCredit - Query the credit adjustments and expired credit

Allowed values are: 'USAGE', 'COST', 'CREDIT', 'EXPIREDCREDIT', 'ALLCREDIT'

`group_by`

(optional) Aggregate the result by. example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\"]`

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

`compartment_depth`

(optional) The compartment depth level.

`filter`

(optional)

`date_range_name`

(optional) The UI date range, for example, LAST_THREE_MONTHS. Conflicts with timeUsageStarted and timeUsageEnded.

Allowed values are: 'LAST_SEVEN_DAYS', 'LAST_TEN_DAYS', 'MTD', 'LAST_TWO_MONTHS', 'LAST_THREE_MONTHS', 'ALL', 'LAST_SIX_MONTHS', 'LAST_ONE_YEAR', 'YTD', 'CUSTOM'

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_DEFINITION_T Type

The common fields for queries.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The query display name. Avoid entering confidential information.

`report_query`

(required)

`cost_analysis_ui`

(required)

`version`

(required) The saved query version.

### DBMS_CLOUD_OCI_USAGEAPI_CREATE_QUERY_DETAILS_T Type

New query detail with savedRequestSummarizedUsagesDetails, savedCostAnalysisUI, and displayName.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_RESULT_LOCATION_T Type

The location where usage or cost CSVs will be uploaded defined by `locationType`, which corresponds with type-specific characteristics.

Syntax
```

```

Fields

Field Description

`location_type`

(required) Defines the type of location where the usage or cost CSVs will be stored.

Allowed values are: 'OBJECT_STORAGE'

### DBMS_CLOUD_OCI_USAGEAPI_DATE_RANGE_T Type

Static or dynamic date range `dateRangeType`, which corresponds with type-specific characteristics.

Syntax
```

```

Fields

Field Description

`date_range_type`

(required) Defines whether the schedule date range is STATIC or DYNAMIC.

Allowed values are: 'STATIC', 'DYNAMIC'

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_PROPERTIES_T Type

The query properties.

Syntax
```

```

Fields

Field Description

`group_by`

(optional) Aggregate the result by. For example: [ \"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\" ]

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: [ { \"namespace\": \"oracle\", \"key\": \"createdBy\" ]

`filter`

(optional)

`compartment_depth`

(optional) The depth level of the compartment.

`granularity`

(required) The usage granularity. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. Allowed values are: DAILY MONTHLY

Allowed values are: 'DAILY', 'MONTHLY'

`query_type`

(optional) The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Allowed values are: USAGE COST USAGE_AND_COST

Allowed values are: 'USAGE', 'COST', 'USAGE_AND_COST'

`is_aggregate_by_time`

(optional) Specifies whether aggregated by time. If isAggregateByTime is true, all usage or cost over the query time period will be added up.

`date_range`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_CREATE_SCHEDULE_DETAILS_T Type

The saved schedule.

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name of the user-created schedule.

`compartment_id`

(required) The customer tenancy.

`description`

(optional) The description of the schedule.

`output_file_format`

(optional) Specifies the supported output file format.

Allowed values are: 'CSV', 'PDF'

`saved_report_id`

(optional) The saved report ID which can also be used to generate a query.

`result_location`

(required)

`schedule_recurrences`

(required) Specifies the frequency according to when the schedule will be run, in the x-obmcs-recurring-time format described in[RFC 5545 section 3.3.10](https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10). Supported values are : ONE_TIME, DAILY, WEEKLY and MONTHLY.

`time_scheduled`

(required) The date and time of the first time job execution.

`query_properties`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_REPORT_QUERY_T Type

The request of the generated usage carbon emissions report.

Syntax
```

```

Fields

Field Description

`tenant_id`

(required) Tenant ID.

`time_usage_started`

(optional) The usage start time.

`time_usage_ended`

(optional) The usage end time.

`is_aggregate_by_time`

(optional) Specifies whether aggregated by time. If isAggregateByTime is true, all usage or cost over the query time period will be added up.

`group_by`

(optional) Specifies what to aggregate the result by. For example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\"]`

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

`compartment_depth`

(optional) The compartment depth level.

`filter`

(optional)

`date_range_name`

(optional) The UI date range, for example, LAST_THREE_MONTHS. It will override timeUsageStarted and timeUsageEnded properties.

Allowed values are: 'LAST_TWO_MONTHS', 'LAST_THREE_MONTHS', 'LAST_SIX_MONTHS', 'LAST_ONE_YEAR', 'CUSTOM'

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_DEFINITION_T Type

The common fields for queries.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The query display name. Avoid entering confidential information.

`report_query`

(required)

`cost_analysis_ui`

(required)

`version`

(required) The saved query version.

### DBMS_CLOUD_OCI_USAGEAPI_CREATE_USAGE_CARBON_EMISSIONS_QUERY_DETAILS_T Type

New query detail with savedRequestUsageCarbonEmissionsDetails, savedCostAnalysisUI, and displayName.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The compartment OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_T Type

The saved custom table.

Syntax
```

```

Fields

Field Description

`id`

(required) The custom table OCID.

`saved_report_id`

(optional) The custom table associated saved report OCID.

`compartment_id`

(optional) The custom table compartment OCID.

`saved_custom_table`

(optional)

### DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_SUMMARY_T Type

Custom table in the list request.

Syntax
```

```

Fields

Field Description

`id`

(required) The custom table OCID.

`saved_custom_table`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_custom_table_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_COLLECTION_T Type

A custom table list.

Syntax
```

```

Fields

Field Description

`items`

(required) Custom tables list.

### DBMS_CLOUD_OCI_USAGEAPI_DYNAMIC_DATE_RANGE_T Type

The saved dynamic date range (required when the static date range is missing).

Syntax
```

```

`dbms_cloud_oci_usageapi_dynamic_date_range_t`is a subtype of the`dbms_cloud_oci_usageapi_date_range_t`type.

Fields

Field Description

`dynamic_date_range_type`

(required)

Allowed values are: 'LAST_7_DAYS', 'LAST_10_DAYS', 'LAST_CALENDAR_WEEK', 'LAST_CALENDAR_MONTH', 'LAST_2_CALENDAR_MONTHS', 'LAST_3_CALENDAR_MONTHS', 'LAST_6_CALENDAR_MONTHS', 'LAST_30_DAYS', 'MONTH_TO_DATE', 'LAST_YEAR', 'YEAR_TODATE', 'ALL'

### DBMS_CLOUD_OCI_USAGEAPI_ERROR_T Type

Erorr details.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_USAGEAPI_OBJECT_STORAGE_LOCATION_T Type

The object storage location where usage or cost CSVs will be uploaded.

Syntax
```

```

`dbms_cloud_oci_usageapi_object_storage_location_t`is a subtype of the`dbms_cloud_oci_usageapi_result_location_t`type.

Fields

Field Description

`l_region`

(required) The destination Object Store Region specified by the customer.

`namespace`

(required) The namespace needed to determine the object storage bucket.

`bucket_name`

(required) The bucket name where usage or cost CSVs will be uploaded.

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_T Type

The query to filter and aggregate.

Syntax
```

```

Fields

Field Description

`id`

(required) The query OCID.

`compartment_id`

(required) The compartment OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_SUMMARY_T Type

Query summery in the list request.

Syntax
```

```

Fields

Field Description

`id`

(required) The query OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_query_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_QUERY_COLLECTION_T Type

A query list.

Syntax
```

```

Fields

Field Description

`items`

(required) Query list.

### DBMS_CLOUD_OCI_USAGEAPI_REQUEST_SUMMARIZED_USAGES_DETAILS_T Type

Details for the '/usage' query.

Syntax
```

```

Fields

Field Description

`tenant_id`

(required) Tenant ID.

`time_usage_started`

(required) The usage start time.

`time_usage_ended`

(required) The usage end time.

`granularity`

(required) The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.

Allowed values are: 'HOURLY', 'DAILY', 'MONTHLY', 'TOTAL'

`is_aggregate_by_time`

(optional) Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.

`forecast`

(optional)

`query_type`

(optional) The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.

Allowed values are: 'USAGE', 'COST', 'CREDIT', 'EXPIREDCREDIT', 'ALLCREDIT'

`group_by`

(optional) Aggregate the result by. example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"tenantId\", \"tenantName\"]`

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

`compartment_depth`

(optional) The compartment depth level.

`filter`

(optional)

### DBMS_CLOUD_OCI_USAGEAPI_REQUEST_USAGE_CARBON_EMISSIONS_DETAILS_T Type

Details for the '/usageCarbonEmissions' query.

Syntax
```

```

Fields

Field Description

`tenant_id`

(required) Tenant ID.

`time_usage_started`

(required) The usage start time.

`time_usage_ended`

(required) The usage end time.

`is_aggregate_by_time`

(optional) Specifies whether aggregated by time. If isAggregateByTime is true, all usage carbon emissions over the query time period will be added up.

`group_by`

(optional) Aggregate the result by. For example: `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\", \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\", \"resourceId\", \"resourceName\", \"tenantId\", \"tenantName\", \"subscriptionId\"]`

`group_by_tag`

(optional) GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

`compartment_depth`

(optional) The compartment depth level.

`filter`

(optional)

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_T Type

The schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID representing a unique shedule.

`name`

(required) The unique name of the schedule created by the user.

`compartment_id`

(required) The customer tenancy.

`result_location`

(required)

`description`

(optional) The description of the schedule.

`time_next_run`

(optional) The date and time of the next job execution.

`output_file_format`

(optional) Specifies the supported output file format.

Allowed values are: 'CSV', 'PDF'

`saved_report_id`

(optional) The saved report ID which can also be used to generate a query.

`schedule_recurrences`

(required) Specifies the frequency according to when the schedule will be run, in the x-obmcs-recurring-time format described in[RFC 5545 section 3.3.10](https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10). Supported values are : ONE_TIME, DAILY, WEEKLY and MONTHLY.

`time_scheduled`

(required) The date and time of the first time job execution.

`query_properties`

(optional)

`time_created`

(required) The date and time the schedule was created.

`lifecycle_state`

(required) The schedule lifecycle state.

Allowed values are: 'ACTIVE', 'INACTIVE'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_SUMMARY_T Type

Schedule summary for the list schedule.

Syntax
```

```

Fields

Field Description

`id`

(required) The schedule OCID.

`name`

(required) The unique name of the user-created schedule.

`description`

(optional) The description of the schedule.

`time_next_run`

(optional) The date and time of the next job execution.

`schedule_recurrences`

(required) Specifies the frequency according to when the schedule will be run, in the x-obmcs-recurring-time format described in[RFC 5545 section 3.3.10](https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10). Supported values are : ONE_TIME, DAILY, WEEKLY and MONTHLY.

`time_scheduled`

(required) The date and time of the first time job execution.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`lifecycle_state`

(required) The schedule summary lifecycle state.

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_COLLECTION_T Type

A schedule collection.

Syntax
```

```

Fields

Field Description

`items`

(required) Schedule summary list.

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_T Type

The saved schedule run.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid representing unique shedule run

`schedule_id`

(required) The ocid representing unique shedule

`time_created`

(required) The time when schedule started executing

`time_finished`

(required) The time when schedule finished executing

`lifecycle_state`

(required) Specifies if the schedule job was run successfully or not.

Allowed values are: 'FAILED', 'SUCCEEDED'

`lifecycle_details`

(required) Additional details about scheduled run failure

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_SUMMARY_T Type

The saved history past run.

Syntax
```

```

Fields

Field Description

`id`

(required) The ocid representing unique shedule run

`schedule_id`

(required) The ocid representing unique shedule

`time_created`

(required) The time when schedule started executing

`time_finished`

(required) The time when schedule finished executing

`lifecycle_state`

(required) Specifies if the schedule job was run successfully or not.

`lifecycle_details`

(required) Additional details about scheduled run failure

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_scheduled_run_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_COLLECTION_T Type

The schedule past run list.

Syntax
```

```

Fields

Field Description

`items`

(required) The schedule past run list.

### DBMS_CLOUD_OCI_USAGEAPI_STATIC_DATE_RANGE_T Type

The saved static date range (required when the dynamic date range is missing).

Syntax
```

```

`dbms_cloud_oci_usageapi_static_date_range_t`is a subtype of the`dbms_cloud_oci_usageapi_date_range_t`type.

Fields

Field Description

`time_usage_started`

(required) The usage start time.

`time_usage_ended`

(required) The usage end time.

### DBMS_CLOUD_OCI_USAGEAPI_UPDATE_CUSTOM_TABLE_DETAILS_T Type

Details for updating the custom table.

Syntax
```

```

Fields

Field Description

`saved_custom_table`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_UPDATE_QUERY_DETAILS_T Type

Details for the query to update reportQuery, costAnalysisUI, and displayName.

Syntax
```

```

Fields

Field Description

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_UPDATE_SCHEDULE_DETAILS_T Type

Details for updating the custom table.

Syntax
```

```

Fields

Field Description

`description`

(optional) The description of the schedule.

`output_file_format`

(optional) Specifies the supported output file format.

Allowed values are: 'CSV', 'PDF'

`result_location`

(optional)

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_USAGEAPI_UPDATE_USAGE_CARBON_EMISSIONS_QUERY_DETAILS_T Type

Details for the query to update usageCarbonEmissionsQuery, costAnalysisUI, and displayName.

Syntax
```

```

Fields

Field Description

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_SUMMARY_T Type

The usage store result.

Syntax
```

```

Fields

Field Description

`tenant_id`

(optional) The tenancy OCID.

`tenant_name`

(optional) The tenancy name.

`compartment_id`

(optional) The compartment OCID.

`compartment_path`

(optional) The compartment path, starting from root.

`compartment_name`

(optional) The compartment name.

`service`

(optional) The service name that is incurring the cost.

`resource_name`

(optional) The resource name that is incurring the cost.

`resource_id`

(optional) The resource OCID that is incurring the cost.

`l_region`

(optional) The region of the usage.

`ad`

(optional) The availability domain of the usage.

`weight`

(optional) The resource size being metered.

`shape`

(optional) The resource shape.

`sku_part_number`

(optional) The SKU part number.

`sku_name`

(optional) The SKU friendly name.

`unit`

(optional) The usage unit.

`discount`

(optional) The discretionary discount applied to the SKU.

`list_rate`

(optional) The SKU list rate (not discount).

`platform`

(optional) Platform for the cost.

`time_usage_started`

(required) The usage start time.

`time_usage_ended`

(required) The usage end time.

`computed_amount`

(optional) The computed cost.

`computed_quantity`

(optional) The usage number.

`overages_flag`

(optional) The SPM OverageFlag.

`unit_price`

(optional) The price per unit.

`currency`

(optional) The price currency.

`subscription_id`

(optional) The subscription ID.

`overage`

(optional) The overage usage.

`is_forecast`

(optional) The forecasted data.

`tags`

(optional) For grouping, a tag definition. For filtering, a definition and key.

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_usage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_AGGREGATION_T Type

The account (tenant) usage.

Syntax
```

```

Fields

Field Description

`group_by`

(optional) Aggregate the result by.

`items`

(required) A list of usage items.

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_SUMMARY_T Type

The usage carbon emission store result.

Syntax
```

```

Fields

Field Description

`tenant_id`

(optional) The tenancy OCID.

`tenant_name`

(optional) The tenancy name.

`compartment_id`

(optional) The compartment OCID.

`compartment_path`

(optional) The compartment path, starting from root.

`compartment_name`

(optional) The compartment name.

`service`

(optional) The service name that is incurring the cost.

`resource_name`

(optional) The resource name that is incurring the cost.

`resource_id`

(optional) The resource OCID that is incurring the cost.

`l_region`

(optional) The region of the usage.

`ad`

(optional) The availability domain of the usage.

`sku_part_number`

(optional) The SKU part number.

`sku_name`

(optional) The SKU friendly name.

`platform`

(optional) Platform for the cost.

`time_usage_started`

(required) The usage start time.

`time_usage_ended`

(required) The usage end time.

`computed_carbon_emission`

(required) The carbon emission in MTCO2 unit.

`emission_calculation_method`

(required) The method used to calculate carbon emission.

`subscription_id`

(optional) The subscription ID.

`tags`

(optional) For grouping, a tag definition. For filtering, a definition and key.

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_usage_carbon_emission_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_AGGREGATION_T Type

The account (tenant) usage carbon emissions.

Syntax
```

```

Fields

Field Description

`group_by`

(optional) Aggregate the result by.

`items`

(required) A list of usage carbon emission items.

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_T Type

The usage carbon emissions saved query to filter and aggregate.

Syntax
```

```

Fields

Field Description

`id`

(required) The query OCID.

`compartment_id`

(required) The compartment OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_SUMMARY_T Type

Usage carbon emissions query summary in the list request.

Syntax
```

```

Fields

Field Description

`id`

(required) The query OCID.

`query_definition`

(required)

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_usageapi_usage_carbon_emissions_query_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_COLLECTION_T Type

A usage carbon emissions query list.

Syntax
```

```

Fields

Field Description

`items`

(required) Usage carbon emissions query list.

- [Usage API Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C82DBE4C-2819-47A0-B4BC-7DD46D53CC3C)
- [DBMS_CLOUD_OCI_USAGEAPI_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-72923BA2-7F1B-43D3-BEEC-31FAA9CA23B1)
- [DBMS_CLOUD_OCI_USAGEAPI_AVERAGE_CARBON_EMISSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-3CDDEAB9-A77A-49A6-804F-8AF0D47CA73E)
- [DBMS_CLOUD_OCI_USAGEAPI_CLEAN_ENERGY_USAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C1FD4B59-5EB4-4963-9069-71C18668047A)
- [DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-A7C74172-FED2-419C-B9EF-9FA8773BEAE1)
- [DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-84DEBAD3-E917-4D9A-B279-F237A9232F14)
- [DBMS_CLOUD_OCI_USAGEAPI_CONFIGURATION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-76567A6D-794C-4771-93B6-1C5F2142E85F)
- [DBMS_CLOUD_OCI_USAGEAPI_COST_ANALYSIS_UI_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-12FEFB35-2C86-4709-AB47-EAF5205FCBD8)
- [DBMS_CLOUD_OCI_USAGEAPI_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-70831CFA-3238-456C-B30B-032D9497655F)
- [DBMS_CLOUD_OCI_USAGEAPI_TAG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-38BB7CB8-92AC-4BCA-8C38-38A26498D463)
- [DBMS_CLOUD_OCI_USAGEAPI_SAVED_CUSTOM_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-31C00E20-4FBF-4EBD-963D-C7566A2B73C1)
- [DBMS_CLOUD_OCI_USAGEAPI_CREATE_CUSTOM_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-A6DCDC7A-2E16-4D9E-A459-3A9232FDD019)
- [DBMS_CLOUD_OCI_USAGEAPI_FORECAST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-DC12F147-0428-4F9C-AF0C-E74E0DD48D9E)
- [DBMS_CLOUD_OCI_USAGEAPI_DIMENSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-E22C4523-8025-4A48-9E3C-3CA0C843691C)
- [DBMS_CLOUD_OCI_USAGEAPI_DIMENSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-239668F6-979C-4E0F-B7DD-E00C549C1791)
- [DBMS_CLOUD_OCI_USAGEAPI_FILTER_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-4AC1E87C-4A0D-49E5-B817-93021A244477)
- [DBMS_CLOUD_OCI_USAGEAPI_FILTER_ABS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-768C2A0A-87DE-4DAD-B435-415641F6AC9A)
- [DBMS_CLOUD_OCI_USAGEAPI_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-3A4193E5-7186-4F14-B5B4-7FCA4A44158B)
- [DBMS_CLOUD_OCI_USAGEAPI_FILTER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-0D4D627F-1A87-4181-B187-3040BA70A887)
- [DBMS_CLOUD_OCI_USAGEAPI_REPORT_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-EDBB05B8-9F3E-403F-81CD-BED9A64FBE03)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-3A57873C-9BEF-4C30-A065-B1A90F8B2FA5)
- [DBMS_CLOUD_OCI_USAGEAPI_CREATE_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-B5F126EF-DBD8-4615-8846-17C32A146491)
- [DBMS_CLOUD_OCI_USAGEAPI_RESULT_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-68BE9802-4339-4921-B72E-54F924B56B11)
- [DBMS_CLOUD_OCI_USAGEAPI_DATE_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C3CC6D7B-C0BB-4404-BA30-8F76A6B3E049)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-0BBD931E-2CE6-4EE2-8985-A96481D6EC35)
- [DBMS_CLOUD_OCI_USAGEAPI_CREATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C0F1027B-EE74-4612-B487-3A60D388B7A5)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_REPORT_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-E61FC324-7374-4E3F-BAAA-E05B335E03AD)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-CAAB04D7-E1F1-4C87-AD84-9292DA7989A5)
- [DBMS_CLOUD_OCI_USAGEAPI_CREATE_USAGE_CARBON_EMISSIONS_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-1EF557AA-96AB-41A8-BE64-C14B6A9B5795)
- [DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-0AB8F2BA-6DDA-471A-AD1A-A5A7147C56AA)
- [DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-468F5765-F0EC-4F84-8A76-680A0B1F4F1D)
- [DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-CD19C157-796A-42D0-88D2-734B5D5D4B08)
- [DBMS_CLOUD_OCI_USAGEAPI_CUSTOM_TABLE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-FDC33CFE-D66F-43B4-86DD-A38E5C38DD8D)
- [DBMS_CLOUD_OCI_USAGEAPI_DYNAMIC_DATE_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-BC3713DC-E297-4C70-A5C4-B8F1FE400FEF)
- [DBMS_CLOUD_OCI_USAGEAPI_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-8C5D6EA0-80F8-40D4-9C58-6D2BA1972A4E)
- [DBMS_CLOUD_OCI_USAGEAPI_OBJECT_STORAGE_LOCATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-8D89FCA6-0353-42CB-9FC6-2FDB30538CB8)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-DDFB3BF1-E79B-4088-80D9-B141807D4EA6)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-A3B3534C-1264-456C-8063-B8C531272410)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-6F3FC25D-9350-493F-9E57-54C45CA39846)
- [DBMS_CLOUD_OCI_USAGEAPI_QUERY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-11B8DA21-5840-49B0-964C-8E395648C25C)
- [DBMS_CLOUD_OCI_USAGEAPI_REQUEST_SUMMARIZED_USAGES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C72E422C-93E6-45FD-A951-93F4141F621E)
- [DBMS_CLOUD_OCI_USAGEAPI_REQUEST_USAGE_CARBON_EMISSIONS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-DD4D76A6-0C7D-469B-8B7C-D9F3CBE7826E)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-AC4DE495-4FF6-4802-8062-887CBD0C4BC8)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-71555B9B-FC28-4D85-B3B9-6C2BDB4F60D8)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-0EE43713-B74F-457E-BA42-BC2715F93D90)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-1958E4BD-0B4F-4A65-AFE7-B7802FF7D7E4)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-9BC2F4C9-001F-47DA-8705-40556F30AF14)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C54B8F03-A05B-401D-853E-4F4D41E009C0)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-B22D317D-CB42-42CE-BF57-C64C63A33329)
- [DBMS_CLOUD_OCI_USAGEAPI_SCHEDULED_RUN_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-D90BBCEE-E936-472B-8FED-EAB0B73C1F7F)
- [DBMS_CLOUD_OCI_USAGEAPI_STATIC_DATE_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C19A8259-843C-41DB-A780-AFF3BCF400FD)
- [DBMS_CLOUD_OCI_USAGEAPI_UPDATE_CUSTOM_TABLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-0BA0CCC3-AAB4-4590-84FC-86EFBD8A2E98)
- [DBMS_CLOUD_OCI_USAGEAPI_UPDATE_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-7E3EF803-5C83-4B8B-9903-D00F7A271976)
- [DBMS_CLOUD_OCI_USAGEAPI_UPDATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-8044D754-0C06-49ED-B412-3620578E129A)
- [DBMS_CLOUD_OCI_USAGEAPI_UPDATE_USAGE_CARBON_EMISSIONS_QUERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-D792E295-459B-43E2-80DF-6E8B7930D8F4)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-39C166D8-D5CA-437A-A2CE-0A346A7DFB11)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-28656F78-5D54-4829-A570-2D5E3C04EBD7)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-06DF8C1B-2748-4CDA-9F59-01106812EBA1)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-447F9BC2-C8BB-494E-81EB-F2F5589FC962)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-C9FBA089-1177-4AE3-A372-5DA086CA6FFE)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSION_AGGREGATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-18D56356-3E73-4FAC-969E-83917C91F1C3)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-BCAFFC43-476F-4077-B5D6-5128AA60E047)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-9763E65D-E3DA-4062-BC85-69DEA6C636BB)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-CDD220DC-4E81-47C6-85FE-01A78FB82A48)
- [DBMS_CLOUD_OCI_USAGEAPI_USAGE_CARBON_EMISSIONS_QUERY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/usageapi_t.html#ADSDK-GUID-E93B5D28-54C4-4BE1-9739-27FD9294284D)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
