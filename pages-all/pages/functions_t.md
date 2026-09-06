# Functions Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#dcoc-content-body)

## Functions Common Types

### DBMS_CLOUD_OCI_FUNCTIONS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_TRACE_CONFIG_T Type

Define the tracing configuration for an application.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Define if tracing is enabled for the resource.

`domain_id`

(optional) The OCID of the collector (e.g. an APM Domain) trace events will be sent to.

### DBMS_CLOUD_OCI_FUNCTIONS_KEY_DETAILS_T Type

The properties that define the kms keys used by Functions for Image Signature verification.

Syntax
```

```

Fields

Field Description

`kms_key_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the KMS key that will be used to verify the image signature.

### DBMS_CLOUD_OCI_FUNCTIONS_KEY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_functions_key_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_IMAGE_POLICY_CONFIG_T Type

Define the image signature verification policy for an application.

Syntax
```

```

Fields

Field Description

`is_policy_enabled`

(required) Define if image signature verification policy is enabled for the application.

`key_details`

(optional) A list of KMS key details.

### DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_T Type

An application contains functions and defined attributes shared between those functions, such as network configuration and configuration. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application.

`compartment_id`

(optional) The OCID of the compartment that contains the application.

`display_name`

(optional) The display name of the application. The display name is unique within the compartment containing the application.

`lifecycle_state`

(optional) The current state of the application.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`config`

(optional) Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`subnet_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the application.

`shape`

(optional) Valid values are `GENERIC_X86`, `GENERIC_ARM` and `GENERIC_X86_ARM`. Default is `GENERIC_X86`. Setting this to `GENERIC_X86`, will run the functions in the application on X86 processor architecture. Setting this to `GENERIC_ARM`, will run the functions in the application on ARM processor architecture. When set to `GENERIC_X86_ARM`, functions in the application are run on either X86 or ARM processor architecture. Accepted values are: `GENERIC_X86`, `GENERIC_ARM`, `GENERIC_X86_ARM`

Allowed values are: 'GENERIC_X86', 'GENERIC_ARM', 'GENERIC_X86_ARM'

`network_security_group_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.

`syslog_url`

(optional) A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls. The syslog URL must be reachable from all of the subnets configured for the application. Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL. Example: `tcp://logserver.myserver:1234`

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(optional) The time the application was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`time_updated`

(optional) The time the application was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`image_policy_config`

(optional)

### DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_SUMMARY_T Type

Summary of an application.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the application.

`compartment_id`

(optional) The OCID of the compartment that contains the application.

`display_name`

(optional) The display name of the application. The display name is unique within the compartment containing the application.

`lifecycle_state`

(optional) The current state of the application.

`subnet_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the application.

`shape`

(optional) Valid values are `GENERIC_X86`, `GENERIC_ARM` and `GENERIC_X86_ARM`. Default is `GENERIC_X86`. Setting this to `GENERIC_X86`, will run the functions in the application on X86 processor architecture. Setting this to `GENERIC_ARM`, will run the functions in the application on ARM processor architecture. When set to `GENERIC_X86_ARM`, functions in the application are run on either X86 or ARM processor architecture. Accepted values are: `GENERIC_X86`, `GENERIC_ARM`, `GENERIC_X86_ARM`

Allowed values are: 'GENERIC_X86', 'GENERIC_ARM', 'GENERIC_X86_ARM'

`network_security_group_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(optional) The time the application was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`time_updated`

(optional) The time the application was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`image_policy_config`

(optional)

### DBMS_CLOUD_OCI_FUNCTIONS_CHANGE_APPLICATION_COMPARTMENT_DETAILS_T Type

Properties to change the compartment of an application.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_FUNCTIONS_CONFIG_DETAILS_T Type

Details about the required and optional Function configurations needed for proper performance of the PBF.

Syntax
```

```

Fields

Field Description

`key`

(required) The key name of the config param.

`description`

(required) Details about why this config is required and what it will be used for.

`is_optional`

(optional) Is this a required config or an optional one. Requests with required config params missing will be rejected.

### DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_PROVISIONED_CONCURRENCY_CONFIG_T Type

Define the strategy for provisioned concurrency for the function.

Syntax
```

```

Fields

Field Description

`strategy`

(required) The strategy for provisioned concurrency to be used.

Allowed values are: 'CONSTANT', 'NONE'

### DBMS_CLOUD_OCI_FUNCTIONS_CONSTANT_PROVISIONED_CONCURRENCY_CONFIG_T Type

Configuration specifying a constant amount of provisioned concurrency.

Syntax
```

```

`dbms_cloud_oci_functions_constant_provisioned_concurrency_config_t`is a subtype of the`dbms_cloud_oci_functions_function_provisioned_concurrency_config_t`type.

Fields

Field Description

`l_count`

(required) Configuration specifying a constant amount of provisioned concurrency.

### DBMS_CLOUD_OCI_FUNCTIONS_CREATE_APPLICATION_DETAILS_T Type

Properties for a new application.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to create the application within.

`display_name`

(required) The display name of the application. The display name must be unique within the compartment containing the application. Avoid entering confidential information.

`config`

(optional) Application configuration. These values are passed on to the function as environment variables, functions may override application configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`subnet_ids`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the subnets in which to run functions in the application.

`shape`

(optional) Valid values are `GENERIC_X86`, `GENERIC_ARM` and `GENERIC_X86_ARM`. Default is `GENERIC_X86`. Setting this to `GENERIC_X86`, will run the functions in the application on X86 processor architecture. Setting this to `GENERIC_ARM`, will run the functions in the application on ARM processor architecture. When set to `GENERIC_X86_ARM`, functions in the application are run on either X86 or ARM processor architecture. Accepted values are: `GENERIC_X86`, `GENERIC_ARM`, `GENERIC_X86_ARM`

Allowed values are: 'GENERIC_X86', 'GENERIC_ARM', 'GENERIC_X86_ARM'

`network_security_group_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.

`syslog_url`

(optional) A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls. The syslog URL must be reachable from all of the subnets configured for the application. Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL. Example: `tcp://logserver.myserver:1234`

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`image_policy_config`

(optional)

### DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_SOURCE_DETAILS_T Type

The source details for the Function. The function can be created from various sources.

Syntax
```

```

Fields

Field Description

`source_type`

(required) Type of the Function Source. Possible values: PBF.

Allowed values are: 'PRE_BUILT_FUNCTIONS'

### DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_TRACE_CONFIG_T Type

Define the tracing configuration for a function.

Syntax
```

```

Fields

Field Description

`is_enabled`

(optional) Define if tracing is enabled for the resource.

### DBMS_CLOUD_OCI_FUNCTIONS_CREATE_FUNCTION_DETAILS_T Type

Properties to create a new function.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The display name of the function. The display name must be unique within the application containing the function. Avoid entering confidential information.

`application_id`

(required) The OCID of the application this function belongs to.

`image`

(optional) The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. Example: `phx.ocir.io/ten/functions/function:0.0.1`

`image_digest`

(optional) The image digest for the version of the image that will be pulled when invoking this function. If no value is specified, the digest currently associated with the image in the OCI Registry will be used. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`

`source_details`

(optional)

`memory_in_m_bs`

(required) Maximum usable memory for the function (MiB).

`config`

(optional) Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`timeout_in_seconds`

(optional) Timeout for executions of the function. Value in seconds.

`provisioned_concurrency_config`

(optional)

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_FUNCTIONS_ERROR_T Type

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

### DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_T Type

A function resource defines the code (Docker image) and configuration for a specific function. Functions are defined in applications. Avoid entering confidential information.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the function.

`display_name`

(optional) The display name of the function. The display name is unique within the application containing the function.

`lifecycle_state`

(optional) The current state of the function.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`application_id`

(optional) The OCID of the application the function belongs to.

`compartment_id`

(optional) The OCID of the compartment that contains the function.

`image`

(optional) The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. Example: `phx.ocir.io/ten/functions/function:0.0.1`

`image_digest`

(optional) The image digest for the version of the image that will be pulled when invoking this function. If no value is specified, the digest currently associated with the image in the OCI Registry will be used. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`

`source_details`

(optional)

`shape`

(optional) The processor shape (`GENERIC_X86`/`GENERIC_ARM`) on which to run functions in the application, extracted from the image manifest.

Allowed values are: 'GENERIC_X86', 'GENERIC_ARM', 'GENERIC_X86_ARM'

`memory_in_m_bs`

(optional) Maximum usable memory for the function (MiB).

`config`

(optional) Function configuration. Overrides application configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`timeout_in_seconds`

(optional) Timeout for executions of the function. Value in seconds.

`provisioned_concurrency_config`

(optional)

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`invoke_endpoint`

(optional) The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and can be cached.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(optional) The time the function was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`time_updated`

(optional) The time the function was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

### DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_SUMMARY_T Type

Summary of a function.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the function.

`display_name`

(optional) The display name of the function. The display name is unique within the application containing the function.

`application_id`

(optional) The OCID of the application the function belongs to.

`compartment_id`

(optional) The OCID of the compartment that contains the function.

`lifecycle_state`

(optional) The current state of the function.

`image`

(optional) The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. Example: `phx.ocir.io/ten/functions/function:0.0.1`

`image_digest`

(optional) The image digest for the version of the image that will be pulled when invoking this function. If no value is specified, the digest currently associated with the image in the OCI Registry will be used. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`

`source_details`

(optional)

`shape`

(optional) The processor shape (`GENERIC_X86`/`GENERIC_ARM`) on which to run functions in the application, extracted from the image manifest.

Allowed values are: 'GENERIC_X86', 'GENERIC_ARM', 'GENERIC_X86_ARM'

`memory_in_m_bs`

(optional) Maximum usable memory for the function (MiB).

`timeout_in_seconds`

(optional) Timeout for executions of the function. Value in seconds.

`provisioned_concurrency_config`

(optional)

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`invoke_endpoint`

(optional) The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and can be cached.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(optional) The time the function was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

`time_updated`

(optional) The time the function was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-09-12T22:47:12.613Z`

### DBMS_CLOUD_OCI_FUNCTIONS_NONE_PROVISIONED_CONCURRENCY_CONFIG_T Type

Configuration specifying no provisioned concurrency

Syntax
```

```

`dbms_cloud_oci_functions_none_provisioned_concurrency_config_t`is a subtype of the`dbms_cloud_oci_functions_function_provisioned_concurrency_config_t`type.

### DBMS_CLOUD_OCI_FUNCTIONS_PUBLISHER_DETAILS_T Type

Contains details about the publisher of this PBF Listing.

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the Publisher

### DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_T Type

PBF specific triggers for activating a PBF.

Syntax
```

```

Fields

Field Description

`name`

(required) A brief descriptive name for the PBF trigger.

### DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_TBL Type

Nested table type of dbms_cloud_oci_functions_trigger_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_T Type

PbfListing resources provide details about the available PBFs for consumption by the user. This resource contains details about PBF's functionality, policies required, configuration parameters expected etc.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A brief descriptive name for the PBF listing. The PBF listing name must be unique, and not match and existing PBF.

`description`

(required) A short overview of the PBF Listing: the purpose of the PBF and and associated information.

`publisher_details`

(required)

`triggers`

(optional) An array of Trigger. A list of triggers that may activate the PBF.

`time_created`

(required) The time the PbfListing was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The last time the PbfListing was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the PBF resource.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_SUMMARY_T Type

Summary of the PbfListing.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation.

`name`

(required) A brief descriptive name for the PBF listing. The PBF listing name must be unique, and not match and existing PBF.

`description`

(required) A short overview of the PBF Listing: the purpose of the PBF and and associated information.

`publisher_details`

(required)

`triggers`

(optional) An array of Trigger. A list of triggers that may activate the PBF.

`time_created`

(required) The time the PbfListing was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The last time the PbfListing was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the PBF resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FUNCTIONS_POLICY_DETAILS_T Type

A policy required for this PBF execution.

Syntax
```

```

Fields

Field Description

`policy`

(required) Policy required for PBF execution

`description`

(required) Details about why this policy is required and what it will be used for.

### DBMS_CLOUD_OCI_FUNCTIONS_POLICY_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_functions_policy_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_REQUIREMENT_DETAILS_T Type

Minimum memory required by this PBF. The user should use memory greater than or equal to this value while configuring the Function.

Syntax
```

```

Fields

Field Description

`min_memory_required_in_m_bs`

(required) Minimum memory required by this PBF. The user should use memory greater than or equal to this value while configuring the Function.

`policies`

(optional) List of policies required for this PBF execution.

### DBMS_CLOUD_OCI_FUNCTIONS_CONFIG_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_functions_config_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_T Type

This represents a version of a PbfListing. Each new update from the publisher or the change in the image will result in the creation of new PbfListingVersion resource creation. This is a sub-resource of a PbfListing.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`pbf_listing_id`

(required) The OCID of the PbfListing this resource version belongs to.

`name`

(required) Semantic version

`config`

(optional) Details about the required and optional Function configurations needed for proper performance of the PBF.

`requirements`

(required)

`change_summary`

(required) Details changes are included in this version.

`triggers`

(required) An array of Trigger. A list of triggers that may activate the PBF.

`time_created`

(required) The time the PbfListingVersion was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The last time the PbfListingVersion was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the PBF resource.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETED'

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_SUMMARY_T Type

Summary of the PbfListingVersion.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`pbf_listing_id`

(required) The OCID of the PbfListing this resource version belongs to.

`name`

(required) Semantic version

`config`

(optional) Details about the required and optional Function configurations needed for proper performance of the PBF.

`requirements`

(required)

`change_summary`

(required) Details changes are included in this version.

`triggers`

(required) An array of Trigger. A list of triggers that may activate the PBF.

`time_created`

(required) The time the PbfListingVersion was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The last time the PbfListingVersion was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the PBF resource.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_functions_pbf_listing_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSIONS_COLLECTION_T Type

Results of a PbfListingVersion search. Contains both PbfListingVersionSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of PbfListingVersion.

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_functions_pbf_listing_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTINGS_COLLECTION_T Type

Results of a PbfListing search. Contains boh PbfListingSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of PbfListingSummary.

### DBMS_CLOUD_OCI_FUNCTIONS_PRE_BUILT_FUNCTION_SOURCE_DETAILS_T Type

The source of the Function which is based on a Pre-Built Function Listing (PbfListing).

Syntax
```

```

`dbms_cloud_oci_functions_pre_built_function_source_details_t`is a subtype of the`dbms_cloud_oci_functions_function_source_details_t`type.

Fields

Field Description

`pbf_listing_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the PbfListing this function is sourced from.

### DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_SUMMARY_T Type

Summary of the Trigger.

Syntax
```

```

Fields

Field Description

`name`

(required) A brief descriptive name for the PBF trigger.

### DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_functions_trigger_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_FUNCTIONS_TRIGGERS_COLLECTION_T Type

Results of a Trigger search. Contains boh TriggerSummary items and other information, such as metadata.

Syntax
```

```

Fields

Field Description

`items`

(required) List of TriggerSummary.

### DBMS_CLOUD_OCI_FUNCTIONS_UPDATE_APPLICATION_DETAILS_T Type

Properties to update an application.

Syntax
```

```

Fields

Field Description

`config`

(optional) Application configuration. These values are passed on to the function as environment variables, functions may override application configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`network_security_group_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)s of the Network Security Groups to add the application to.

`syslog_url`

(optional) A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls. The syslog URL must be reachable from all of the subnets configured for the application. Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL. Example: `tcp://logserver.myserver:1234`

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`image_policy_config`

(optional)

### DBMS_CLOUD_OCI_FUNCTIONS_UPDATE_FUNCTION_DETAILS_T Type

Updates attributes of a function.

Syntax
```

```

Fields

Field Description

`image`

(optional) The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. If an image is specified but no value for imageDigest is provided, the digest currently associated with the image tag in the OCI Registry will be used. Example: `phx.ocir.io/ten/functions/function:0.0.1`

`image_digest`

(optional) The image digest for the version of the image that will be pulled when invoking this function. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`

`memory_in_m_bs`

(optional) Maximum usable memory for the function (MiB).

`config`

(optional) Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters. Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}` The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.

`timeout_in_seconds`

(optional) Timeout for executions of the function. Value in seconds.

`provisioned_concurrency_config`

(optional)

`trace_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Functions Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-A03CBB84-66F2-4E37-A660-5F85B7B002BF)
- [DBMS_CLOUD_OCI_FUNCTIONS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-8E359115-1F0C-4223-880D-AE98D117F534)
- [DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_TRACE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-3CD82717-BCAC-4B1B-90CF-F2E8A8302908)
- [DBMS_CLOUD_OCI_FUNCTIONS_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-6CD82B2B-7829-4E54-A338-191FCD1DFB6E)
- [DBMS_CLOUD_OCI_FUNCTIONS_KEY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-A39BD8F2-4C51-4380-8582-89BD2B98D230)
- [DBMS_CLOUD_OCI_FUNCTIONS_IMAGE_POLICY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-C04A08AE-DF21-49B4-88C7-3C1A6312CAA1)
- [DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-F6A3C409-59F3-46FC-AA26-CED17C296F2B)
- [DBMS_CLOUD_OCI_FUNCTIONS_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-8465EB32-C830-445A-A846-B5F762C1F898)
- [DBMS_CLOUD_OCI_FUNCTIONS_CHANGE_APPLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-13C2007F-2117-4A79-B64A-5EEC5A930DDB)
- [DBMS_CLOUD_OCI_FUNCTIONS_CONFIG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-D678192D-015C-46A4-B697-856804BBF531)
- [DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_PROVISIONED_CONCURRENCY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-6757E7F5-CF94-4082-9344-9B00C7B75266)
- [DBMS_CLOUD_OCI_FUNCTIONS_CONSTANT_PROVISIONED_CONCURRENCY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-321D6EC5-1D96-42CE-B13F-8EDF2D124247)
- [DBMS_CLOUD_OCI_FUNCTIONS_CREATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-7413F61F-88F3-48B8-8EA4-0E152E7EC56F)
- [DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-AF5C6B7D-774C-4092-A99D-926E00C3AAA7)
- [DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_TRACE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-F2A85A15-563D-45EE-8CAE-2DC24F14FDC7)
- [DBMS_CLOUD_OCI_FUNCTIONS_CREATE_FUNCTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-17200910-B1ED-460E-A694-1068BEB3D102)
- [DBMS_CLOUD_OCI_FUNCTIONS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-17D67979-5076-4080-B444-E782E8B22C40)
- [DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-EA7681D4-D77B-470A-87DA-CABE73AF0FC5)
- [DBMS_CLOUD_OCI_FUNCTIONS_FUNCTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-0ECF63AA-3A1F-433A-9C23-CA0B718AB85B)
- [DBMS_CLOUD_OCI_FUNCTIONS_NONE_PROVISIONED_CONCURRENCY_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-C201C6D5-7F9C-41DB-8C09-B64B033FE06F)
- [DBMS_CLOUD_OCI_FUNCTIONS_PUBLISHER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-7F2AD623-0DB9-4777-A9BD-0C517BFC1DB6)
- [DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-49113275-3C0A-4DC7-A1BC-7E811B06835A)
- [DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-D8DA9888-68B2-4A2D-91F3-3515733549EF)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-85C03FA6-BECF-4AD9-8657-7578E3924261)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-C4C62D92-4671-48DF-9EE9-F6195810E525)
- [DBMS_CLOUD_OCI_FUNCTIONS_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-CC4BA8BF-B1E1-431C-A40F-5ECC1CC365D3)
- [DBMS_CLOUD_OCI_FUNCTIONS_POLICY_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-5D637BDB-3F57-4E23-8FAE-E90512D90C52)
- [DBMS_CLOUD_OCI_FUNCTIONS_REQUIREMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-CE389932-C3B2-48A0-B351-8DAB11FE8B2B)
- [DBMS_CLOUD_OCI_FUNCTIONS_CONFIG_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-55B1334F-1072-41D7-B3FD-21DA5ABDF9D7)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-5C5AD987-6073-400F-B497-2D27695ADFF0)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-339BBED3-A8B0-4B03-8DC2-C91A4F9F4025)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-1D6D1188-A977-4A0D-A224-969C68A4CEB0)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_VERSIONS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-19B55D64-3B21-42FA-9562-3BEE9133A5F0)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTING_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-606435A9-9D62-4FCF-9D3E-17C96BDE1D7C)
- [DBMS_CLOUD_OCI_FUNCTIONS_PBF_LISTINGS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-B1ABDB59-70C5-472A-B684-214E667F30EB)
- [DBMS_CLOUD_OCI_FUNCTIONS_PRE_BUILT_FUNCTION_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-6DC550F7-7D92-4B3F-8CAB-5181CB297C7A)
- [DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-471A828F-DDA6-4830-BF16-8ADBB008B5EB)
- [DBMS_CLOUD_OCI_FUNCTIONS_TRIGGER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-85FF4F6F-01BE-45D0-B0AE-159F17332259)
- [DBMS_CLOUD_OCI_FUNCTIONS_TRIGGERS_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-88D28A53-EE4B-4B95-8E39-58133FF1325C)
- [DBMS_CLOUD_OCI_FUNCTIONS_UPDATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-7CB9D79D-59E9-4C48-B269-5A154D8BEF17)
- [DBMS_CLOUD_OCI_FUNCTIONS_UPDATE_FUNCTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/functions_t.html#ADSDK-GUID-1FE52033-E2FA-4530-BDED-6FA4C37C375E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
