# Logging Ingestion Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#dcoc-content-body)

## Logging Ingestion Common Types

### DBMS_CLOUD_OCI_LOGGING_INGESTION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_INGESTION_ERROR_T Type

An error has occurred.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_T Type

Contains the log content with the associated timestamp and ID. Each entry should be less than 1 MB size.

Syntax
```

```

Fields

Field Description

`data`

(required) The log entry content.

`id`

(required) UUID uniquely representing this logEntry. This is not an OCID related to any oracle resource.

`time`

(optional) Optional. The timestamp associated with the log entry. An RFC3339-formatted date-time string with milliseconds precision. If unspecified, defaults to PutLogsDetails.defaultlogentrytime.

### DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_logging_ingestion_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_BATCH_T Type

A single batch of Log Entries.

Syntax
```

```

Fields

Field Description

`entries`

(required) List of data entries.

`source`

(required) Source of the logs that generated the message. This could be the instance name, hostname, or the source used to read the event. For example, \"ServerA\".

`l_type`

(required) This field signifies the type of logs being ingested. For example: ServerA.requestLogs.

`subject`

(optional) This optional field is useful for specifying the specific sub-resource or input file used to read the event. For example: \"/var/log/application.log\".

`defaultlogentrytime`

(required) The timestamp for all log entries in this batch. This can be considered as the default timestamp for each entry, unless it is overwritten by the entry time. An RFC3339-formatted date-time string with milliseconds precision.

### DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_BATCH_TBL Type

Nested table type of dbms_cloud_oci_logging_ingestion_log_entry_batch_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LOGGING_INGESTION_PUT_LOGS_DETAILS_T Type

The request body for the PutLogs request.

Syntax
```

```

Fields

Field Description

`specversion`

(required) Required for identifying the version of the data format being used. Permitted values include: \"1.0\"

`log_entry_batches`

(required) List of log-batches. Each batch has a single source, type and subject.

- [Logging Ingestion Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-1B995921-FA24-4FED-BE82-F74EA9880774)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-01D26B57-F2D4-4EAA-A08B-4CE41D7697F7)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-4B065784-6560-4E9E-B7CD-1860CA41A8F1)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-EE0491F1-B331-49E6-B88A-DBD6DFE67079)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-70DA1340-6E9C-4D96-BC4F-20C032DE04FD)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_BATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-03C1CFB9-9463-4A4E-AE85-8581919A21E6)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_LOG_ENTRY_BATCH_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-5126E7CD-0694-447D-8120-E59E8B82659F)
- [DBMS_CLOUD_OCI_LOGGING_INGESTION_PUT_LOGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/logging_ingestion_t.html#ADSDK-GUID-D1BBEF84-275B-4043-ACD4-7A9BCC2AC2BD)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
