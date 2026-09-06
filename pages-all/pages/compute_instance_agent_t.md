# Compute Instance Agent Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#dcoc-content-body)

## Compute Instance Agent Common Types

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_AVAILABLE_PLUGIN_SUMMARY_T Type

Describes where the plugin is supported

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name

`summary`

(optional) A brief description of the plugin functionality

`is_supported`

(required) Is the plugin supported or not

`is_enabled_by_default`

(required) Is the plugin enabled or disabled by default

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_TARGET_T Type

The target instance that the command runs on.

Syntax
```

```

Fields

Field Description

`instance_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target instance.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_DETAILS_T Type

The source of the command.

Syntax
```

```

Fields

Field Description

`source_type`

(required) The source type for the command. The following values are supported: - `TEXT` - uses a plain text command that is specified inline with the request. - `OBJECT_STORAGE_URI` - imports a command from an Object Storage URL. - `OBJECT_STORAGE_TUPLE` - imports a command from an Object Storage bucket. For background information about Object Storage buckets and URLs, see[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm).

Allowed values are: 'TEXT', 'OBJECT_STORAGE_URI', 'OBJECT_STORAGE_TUPLE'

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_DETAILS_T Type

The output destination for the command.

Syntax
```

```

Fields

Field Description

`output_type`

(required) The output type for the command. The following values are supported: - `TEXT` - the command output is returned as plain text. - `OBJECT_STORAGE_URI` - the command output is saved to an Object Storage URL. - `OBJECT_STORAGE_TUPLE` - the command output is saved to an Object Storage bucket. For background information about Object Storage buckets and URLs, see[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm).

Allowed values are: 'TEXT', 'OBJECT_STORAGE_URI', 'OBJECT_STORAGE_TUPLE'

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_CONTENT_T Type

The contents of the command.

Syntax
```

```

Fields

Field Description

`source`

(required) The source of the command.

`output`

(optional) The output destination for the command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_CREATE_INSTANCE_AGENT_COMMAND_DETAILS_T Type

Creation details for an Oracle Cloud Agent command.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to create the command in.

`execution_time_out_in_seconds`

(required) The amount of time that Oracle Cloud Agent is given to run the command on the instance before timing out. The timer starts when Oracle Cloud Agent starts the command. Zero means no timeout.

`display_name`

(optional) A user-friendly name for the command. It does not have to be unique. Avoid entering confidential information. Example: `Database Backup Script`

`target`

(required) The target instance to run the command on.

`content`

(required) The contents of the command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_ERROR_T Type

Error response

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_T Type

The command payload.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the command.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the command.

`display_name`

(optional) A user-friendly name. Does not have to be unique. Avoid entering confidential information.

`time_created`

(optional) The date and time the command was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(optional) The date and time the command was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`is_canceled`

(optional) Whether a request was made to cancel the command. Canceling a command is a best-effort attempt.

`execution_time_out_in_seconds`

(optional) The amount of time that Oracle Cloud Agent is given to run the command on the instance before timing out. The timer starts when Oracle Cloud Agent starts the command. Zero means no timeout.

`target`

(required) The target instance that the command runs on.

`content`

(required) The contents of the command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_CONTENT_T Type

The execution output from a command.

Syntax
```

```

Fields

Field Description

`output_type`

(required) The output destination type for the command. The following values are supported: - TEXT - the command output is returned as plain text. - OBJECT_STORAGE_URI - the command output is saved to an Object Storage URL. - OBJECT_STORAGE_TUPLE - the command output is saved to an Object Storage bucket. For background information about Object Storage buckets and URLs, see[Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm).

Allowed values are: 'TEXT', 'OBJECT_STORAGE_URI', 'OBJECT_STORAGE_TUPLE'

`exit_code`

(required) The exit code for the command. Exit code `0` indicates success.

`message`

(optional) An optional status message that Oracle Cloud Agent can populate for additional troubleshooting.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_T Type

A command's execution summary.

Syntax
```

```

Fields

Field Description

`instance_agent_command_id`

(required) The OCID of the command

`instance_id`

(required) The OCID of the instance

`delivery_state`

(required) Specifies the command delivery state. * `VISIBLE` - The command is visible to instance. * `PENDING` - The command is pending ack from the instance. * `ACKED` - The command has been received and acked by the instance. * `ACKED_CANCELED` - The canceled command has been received and acked by the instance. * `EXPIRED` - The instance has not requested for commands and its delivery has expired.

Allowed values are: 'VISIBLE', 'PENDING', 'ACKED', 'ACKED_CANCELED', 'EXPIRED'

`lifecycle_state`

(required) command execution life cycle state. * `ACCEPTED` - The command execution has been accepted to run. * `IN_PROGRESS` - The command execution is in progress. * `SUCCEEDED` - The command execution is successful. * `FAILED` - The command execution has failed. * `TIMED_OUT` - The command execution has timedout. * `CANCELED` - The command execution has canceled.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'CANCELED'

`time_created`

(required) The command creation date

`time_updated`

(required) The command last updated at date.

`sequence_number`

(required) The large non-consecutive number that Run Command Service assigns to each created command.

`display_name`

(optional) The user friendly display name of the command.

`content`

(required)

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type

The execution output from a command when saved to an Object Storage bucket.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_via_object_storage_tuple_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_content_t`type.

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket for the command output.

`namespace_name`

(required) The Object Storage namespace for the command output.

`object_name`

(required) The Object Storage object name for the command output.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_OBJECT_STORAGE_URI_DETAILS_T Type

The execution output from a command when saved to an Object Storage URL.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_via_object_storage_uri_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_content_t`type.

Fields

Field Description

`output_uri`

(required) The Object Storage URL or pre-authenticated request (PAR) for the command output.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_TEXT_DETAILS_T Type

The execution output from a command when returned in plain text.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_via_text_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_execution_output_content_t`type.

Fields

Field Description

`text`

(optional) The command output.

`text_sha256`

(optional) SHA-256 checksum value of the text content.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_SUMMARY_T Type

Execution details for a command.

Syntax
```

```

Fields

Field Description

`instance_agent_command_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the command.

`instance_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the instance.

`delivery_state`

(required) The command delivery state. * `VISIBLE` - The command is visible to the instance. * `PENDING` - The command is pending acknowledgment from the instance. * `ACKED` - The command has been received and acknowledged by the instance. * `ACKED_CANCELED` - The canceled command has been received and acknowledged by the instance. * `EXPIRED` - The instance has not requested for commands and the command's delivery has expired.

Allowed values are: 'VISIBLE', 'PENDING', 'ACKED', 'ACKED_CANCELED', 'EXPIRED'

`lifecycle_state`

(required) The command execution lifecycle state. * `ACCEPTED` - The command has been accepted to run. * `IN_PROGRESS` - The command is in progress. * `SUCCEEDED` - The command was successfully executed. * `FAILED` - The command failed to execute. * `TIMED_OUT` - The command execution timed out. * `CANCELED` - The command execution was canceled.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'CANCELED'

`time_created`

(required) The date and time the command was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(required) The date and time the command was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`sequence_number`

(required) A large, non-consecutive number that Oracle Cloud Agent assigns to each created command.

`display_name`

(optional) A user-friendly name. Does not have to be unique.

`content`

(required) The execution output from a command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type

The command output destination when saved to an Object Storage bucket.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_via_object_storage_tuple_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_details_t`type.

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket for the command output.

`namespace_name`

(required) The Object Storage namespace for the command output.

`object_name`

(required) The Object Storage object name for the command output.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_OBJECT_STORAGE_URI_DETAILS_T Type

The command output destination when saved to an Object Storage URL.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_via_object_storage_uri_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_details_t`type.

Fields

Field Description

`output_uri`

(required) The Object Storage URL or pre-authenticated request (PAR) for the command output.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_TEXT_DETAILS_T Type

The command output destination when returned in plain text.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_via_text_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_output_details_t`type.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type

The source of the command when imported from an Object Storage bucket.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_via_object_storage_tuple_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_details_t`type.

Fields

Field Description

`bucket_name`

(required) The Object Storage bucket for the command.

`namespace_name`

(required) The Object Storage namespace for the command.

`object_name`

(required) The Object Storage object name for the command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type

The source of the command when imported from an Object Storage URL.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_via_object_storage_uri_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_details_t`type.

Fields

Field Description

`source_uri`

(required) The Object Storage URL or pre-authenticated request (PAR) for the command.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_TEXT_DETAILS_T Type

The source of the command when provided using plain text.

Syntax
```

```

`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_via_text_details_t`is a subtype of the`dbms_cloud_oci_compute_instance_agent_instance_agent_command_source_details_t`type.

Fields

Field Description

`text`

(required) The plain text command.

`text_sha256`

(optional) SHA-256 checksum value of the text content.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SUMMARY_T Type

Summary information for a command.

Syntax
```

```

Fields

Field Description

`instance_agent_command_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the command.

`display_name`

(optional) A user-friendly name. Does not have to be unique.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the command.

`time_created`

(required) The date and time the command was created, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`time_updated`

(required) The date and time the command was last updated, in the format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`is_canceled`

(optional) Whether a request was made to cancel the command. Canceling a command is a best-effort attempt.

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_PLUGIN_T Type

The agent plugin

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name

`status`

(required) The plugin status Specified the plugin state on the instance * `RUNNING` - The plugin is in running state * `STOPPED` - The plugin is in stopped state * `NOT_SUPPORTED` - The plugin is not supported on this platform * `INVALID` - The plugin state is not recognizable by the service

Allowed values are: 'RUNNING', 'STOPPED', 'NOT_SUPPORTED', 'INVALID'

`time_last_updated_utc`

(required) The last update time of the plugin in UTC

`message`

(optional) The optional message from the agent plugin

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_PLUGIN_SUMMARY_T Type

The agent plugin information

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name

`status`

(required) The plugin status Specified the plugin state on the instance * `RUNNING` - The plugin is in running state * `STOPPED` - The plugin is in stopped state * `NOT_SUPPORTED` - The plugin is not supported on this platform * `INVALID` - The plugin state is not recognizable by the service

Allowed values are: 'RUNNING', 'STOPPED', 'NOT_SUPPORTED', 'INVALID'

`time_last_updated_utc`

(required) The last update time of the plugin in UTC

### DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_PLUGIN_T Type

The agent plugin

Syntax
```

```

Fields

Field Description

`name`

(required) The plugin name

`version`

(required) The plugin version

`status`

(required) The plugin status

`last_update_time`

(optional) The last update time of the plugin

`message`

(optional) The optional message from the agent plugin

- [Compute Instance Agent Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-D7606384-8BE1-4E78-B188-FD4F22D5830B)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-D568AB89-06B1-47C0-B857-95B0B32F7185)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_AVAILABLE_PLUGIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-4766CC32-5269-47F3-8550-863A848735A7)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-91A56123-46D4-48F8-BF11-B9D87CBA1A61)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-F8BCD875-F532-49B6-911A-DD72FC142FBB)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-2179D4EC-2F14-49EB-881C-96F0C90F5D2B)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_CONTENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-AE91810F-235F-42F6-80AC-AF1732D08F07)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_CREATE_INSTANCE_AGENT_COMMAND_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-B8F73EE3-47D3-4D7B-9B98-452E882BB20E)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-6FC7594E-8E2C-4EA6-83AE-CA88E09CA5DE)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-1282F532-F855-4264-BB61-AE656A9C4A61)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_CONTENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-1260AA9E-3624-423A-B7BA-D45CF58F9CA9)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-5FD781AB-41D1-4BD2-B2FC-8EC4ADE345FC)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-EEBD03CA-CE7F-41B2-AB18-B4F515815316)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_OBJECT_STORAGE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-6E891745-E078-4FBC-B173-91C8DE57A38E)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_OUTPUT_VIA_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-16F089E1-694B-4BBC-9B40-2E479E63DE63)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_EXECUTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-E2856D92-93DB-45BE-AE05-52D61EA1BA60)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-99A4260F-2AA6-4DED-BCED-5EA4F60906CB)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_OBJECT_STORAGE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-9B1E5D97-A51C-4FCA-B1F1-7BB04F945938)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_OUTPUT_VIA_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-CF6B0E8A-E9C2-4010-890C-16530FCE1E4B)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_OBJECT_STORAGE_TUPLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-6D7179D1-AB86-448B-870F-DBB3A490F229)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_OBJECT_STORAGE_URI_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-C7BA8FEA-34A3-413B-B0C5-3A7C7CEAE093)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SOURCE_VIA_TEXT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-D7A359DD-3372-465C-8588-003663E85CF6)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_COMMAND_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-E020F754-40B2-4A85-8283-BC464D559DA4)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_PLUGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-FDEF4F66-D516-4FD4-B5FA-B3A11020DE4C)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_INSTANCE_AGENT_PLUGIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-70605560-0FD2-4F7D-B19D-37B022E9D271)
- [DBMS_CLOUD_OCI_COMPUTE_INSTANCE_AGENT_PLUGIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/compute_instance_agent_t.html#ADSDK-GUID-E351A5B8-9223-45B5-852A-845BE4381BE8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
