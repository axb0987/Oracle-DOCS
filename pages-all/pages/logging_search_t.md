# Logging Search Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#dcoc-content-body)

## Logging Search Common Types

### DBMS_CLOUD_OCI_LOGGING_SEARCH_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_SEARCH_ERROR_T Type

Error response object.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOGGING_SEARCH_FIELD_INFO_T Type

Contains field schema information.

Syntax
```

```

Fields

Field Description

`field_name`

(required) Field name

`field_type`

(required) Field type - * `STRING`: A sequence of characters. * `NUMBER`: Numeric type which can be an integer or floating point. * `BOOLEAN`: Either true or false. * `ARRAY`: An ordered collection of values.

Allowed values are: 'STRING', 'NUMBER', 'BOOLEAN', 'ARRAY'

### DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_LOGS_DETAILS_T Type

Search request object.

Syntax
```

```

Fields

Field Description

`time_start`

(required) Start filter log's date and time, in the format defined by RFC3339.

`time_end`

(required) End filter log's date and time, in the format defined by RFC3339.

`search_query`

(required) Query corresponding to the search operation. This query is parsed and validated before execution and should follow the specification. For more information on the query language specification, see[Logging Query Language Specification](https://docs.oracle.com/iaas/Content/Logging/Reference/query_language_specification.htm).

`is_return_field_info`

(optional) Whether to return field schema information for the log stream specified in searchQuery.

### DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_T Type

A log search result entry.

Syntax
```

```

Fields

Field Description

`data`

(required) JSON blob containing the search entry with the projected fields.

### DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_SUMMARY_T Type

Summary of results.

Syntax
```

```

Fields

Field Description

`result_count`

(optional) Total number of search results.

`field_count`

(optional) Total number of field schema information.

### DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_TBL Type

Nested table type of dbms_cloud_oci_logging_search_search_result_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_SEARCH_FIELD_INFO_TBL Type

Nested table type of dbms_cloud_oci_logging_search_field_info_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESPONSE_T Type

Search response object.

Syntax
```

```

Fields

Field Description

`results`

(optional) List of search results

`fields`

(optional) List of log field schema information.

`summary`

(required)

- [Logging Search Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-F39E52B5-7DDE-46D4-ACCC-65C4B0AC15D8)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-27C45076-6E41-42F6-ABCE-2C6587E4F623)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-CCA9B6D8-6FC6-4515-B86E-169FEA234D78)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_FIELD_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-7E564435-87AD-4D8F-90FB-ACAB91ECFE64)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_LOGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-186C61D2-4D0A-4F1B-A751-2A975095FEC4)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-112BFAF1-14D0-4BA5-8C9F-A399664111B4)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-A4F75B91-BD7F-41E2-B9A8-C7FECC4D225E)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESULT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-0DE1D68D-5AC3-48FC-A932-A2EA7AD8A8F3)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_FIELD_INFO_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-6DD27109-2552-4FBB-8188-ECCBDACC58DB)
- [DBMS_CLOUD_OCI_LOGGING_SEARCH_SEARCH_RESPONSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_search_t.html#ADSDK-GUID-7CFC5DCD-623A-4F34-ACA4-2F0A1A47F249)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
