# Work Requests Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html
- Fetched: 2026-09-05 19:22 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#dcoc-content-body)

## Work Requests Common Types

### DBMS_CLOUD_OCI_WORK_REQUESTS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_WORK_REQUESTS_ERROR_T Type

An error code and message from an API request failure.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_RESOURCE_T Type

A resource that is created or operated on by an asynchronous operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource was affected by the operation that spawned the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS'

`entity_type`

(required) The resource type the work request affects.

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_work_requests_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources that are affected by this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable log message.

`l_timestamp`

(required) The date and time the log message was written.

### DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this work request.

`percent_complete`

(required) The percentage complete of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

- [Work Requests Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-FBD53961-B340-4F0F-B9BB-13810A25CE1F)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-8B5BFA10-14EF-4F51-A5C0-81603633BB4B)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-92CB66A6-D277-4B4D-84AA-FCD59D3F436E)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-FCE171E5-8CE6-475D-82A5-B2E0200F3E0A)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-F6D2F532-B3B4-41CB-BA21-CE4A6ECA7F2B)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-AF778AB4-5CE4-4A94-A8AD-5FEEF90BA2A5)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-A20C557C-9FB2-44E8-B636-D94D14FEDF52)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-04D8E6D0-F33F-44F0-8D3F-00D9D429BE8A)
- [DBMS_CLOUD_OCI_WORK_REQUESTS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/work_requests_t.html#ADSDK-GUID-120A7FA0-F37D-4F90-81D8-58366F5CDE76)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
