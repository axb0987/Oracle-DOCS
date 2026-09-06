# Data Integration Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html
- Fetched: 2026-09-05 19:03 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#dcoc-content-body)

## Data Integration Common Types

### DBMS_CLOUD_OCI_DATAINTEGRATION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_CALL_ATTRIBUTE_T Type

The abstract write attribute.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the abstract call attribute.

Allowed values are: 'BIP_CALL_ATTRIBUTE', 'GENERIC_REST_CALL_ATTRIBUTE'

`fetch_size`

(optional) The fetch size for reading.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARENT_REFERENCE_T Type

A reference to the object's parent.

Syntax
```

```

Fields

Field Description

`parent`

(optional) Key of the parent object.

`root_doc_id`

(optional) Key of the root document object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_BASE_TYPE_T Type

Base type for the type system.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The property which disciminates the subtypes.

Allowed values are: 'DYNAMIC_TYPE', 'STRUCTURED_TYPE', 'DATA_TYPE', 'JAVA_TYPE', 'CONFIGURED_TYPE', 'COMPOSITE_TYPE', 'DERIVED_TYPE', 'ARRAY_TYPE', 'MAP_TYPE', 'MATERIALIZED_COMPOSITE_TYPE'

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`description`

(optional) A user defined description for the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PARAMETER_DEFINITION_T Type

The configurable properties of an object type.

Syntax
```

```

Fields

Field Description

`parameter_type`

(optional)

`parameter_name`

(optional) This object represents the configurable properties for an object type.

`description`

(optional) A user defined description for the object.

`default_value`

(optional) The default value for the parameter.

`class_field_name`

(optional) The parameter class field name.

`is_static`

(optional) Specifies whether the parameter is static or not.

`is_class_field_value`

(optional) Specifies whether the parameter is a class field or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_DEFINITION_T Type

The configuration details of a configurable object. This contains one or more config param definitions.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`is_contained`

(optional) Specifies whether the configuration is contained or not.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`config_parameter_definitions`

(optional) The parameter configuration details.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_TYPE_T Type

A `DataType` object is a simple primitive type that describes the type of a single atomic unit of data. For example, `INT`, `VARCHAR`, `NUMBER`, and so on.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`dt_type`

(optional) The data type.

Allowed values are: 'PRIMITIVE', 'STRUCTURED'

`type_system_name`

(optional) The data type system name.

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_TYPE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_data_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_SYSTEM_T Type

The type system maps from and to a type.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`type_mapping_to`

(optional) The type system to map to.

`type_mapping_from`

(optional) The type system to map from.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`types`

(optional) An array of types.

### DBMS_CLOUD_OCI_DATAINTEGRATION_AGGREGATOR_SUMMARY_T Type

A summary type containing information about the object's aggregator including its type, key, name and description.

Syntax
```

```

Fields

Field Description

`l_type`

(optional) The type of the aggregator.

`key`

(optional) The key of the aggregator object.

`name`

(optional) The name of the aggregator.

`identifier`

(optional) The identifier of the aggregator.

`description`

(optional) The description of the aggregator.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_SUMMARY_T Type

Details of the count statistic summary object.

Syntax
```

```

Fields

Field Description

`object_type`

(optional) The type of object for the count statistic object.

Allowed values are: 'PROJECT', 'FOLDER', 'DATA_FLOW', 'DATA_ASSET', 'CONNECTION', 'TASK', 'APPLICATION', 'FUNCTION_LIBRARY', 'USER_DEFINED_FUNCTION'

`object_count`

(optional) The value for the count statistic object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_count_statistic_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_T Type

A count statistics.

Syntax
```

```

Fields

Field Description

`object_type_count_list`

(required) The array of statistics.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_METADATA_T Type

A summary type containing information about the object including its key, name and when/who created/updated it.

Syntax
```

```

Fields

Field Description

`created_by`

(optional) The user that created the object.

`created_by_name`

(optional) The user that created the object.

`updated_by`

(optional) The user that updated the object.

`updated_by_name`

(optional) The user that updated the object.

`time_created`

(optional) The date and time that the object was created.

`time_updated`

(optional) The date and time that the object was updated.

`aggregator_key`

(optional) The owning object key for this object.

`aggregator`

(optional)

`identifier_path`

(optional) The full path to identify this object.

`info_fields`

(optional) Information property fields.

`registry_version`

(optional) The registry version of the object.

`labels`

(optional) Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

`is_favorite`

(optional) Specifies whether this object is a favorite or not.

`count_statistics`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_T Type

The schema object.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object's type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`resource_name`

(optional) A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.

`description`

(optional) User-defined description for the schema.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`is_has_containers`

(optional) Specifies whether the schema has containers.

`default_connection`

(optional) The default connection key.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_PROPERTY_T Type

The connection name/value pair.

Syntax
```

```

Fields

Field Description

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`value`

(optional) The value for the connection name property.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_PROPERTY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_connection_property_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_T Type

The connection summary object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the connection.

Allowed values are: 'ORACLE_ADWC_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLEDB_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION', 'BIP_CONNECTION', 'LAKE_CONNECTION', 'ORACLE_PEOPLESOFT_CONNECTION', 'ORACLE_EBS_CONNECTION', 'ORACLE_SIEBEL_CONNECTION', 'HDFS_CONNECTION', 'MYSQL_HEATWAVE_CONNECTION', 'REST_NO_AUTH_CONNECTION', 'REST_BASIC_AUTH_CONNECTION'

`key`

(optional) Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description for the connection.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`primary_schema`

(optional)

`connection_properties`

(optional) The properties for the connection.

`is_default`

(optional) The default property for the connection.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_OBJECT_STORAGE_T Type

The connection details for an Oracle Object Storage data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`credential_file_content`

(optional) The credential file content from an Oracle Object Storage wallet.

`user_id`

(optional) The OCI user OCID for the user to connect to.

`finger_print`

(optional) The fingerprint for the user.

`pass_phrase`

(optional) The passphrase for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_T Type

The summary object for data asset.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the data asset.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'LAKE_DATA_ASSET', 'ORACLE_PEOPLESOFT_DATA_ASSET', 'ORACLE_SIEBEL_DATA_ASSET', 'ORACLE_EBS_DATA_ASSET', 'HDFS_DATA_ASSET', 'MYSQL_HEATWAVE_DATA_ASSET', 'REST_DATA_ASSET'

`key`

(optional) Generated key that can be used in API calls to identify data asset.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) The user-defined description of the data asset.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`external_key`

(optional) The external key for the object.

`asset_properties`

(optional) Additional properties for the data asset.

`native_type_system`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_OBJECT_STORAGE_T Type

Summary details for the Oracle Object storage data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`oci_region`

(optional) The Oracle Object storage Region ie. us-ashburn-1

`url`

(optional) The Oracle Object storage URL.

`tenancy_id`

(optional) The OCI tenancy OCID.

`namespace`

(optional) The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_CALL_ATTRIBUTE_T Type

Properties to configure reading from a FUSION_APP BIP data asset / connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_bip_call_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_call_attribute_t`type.

Fields

Field Description

`offset_parameter`

(optional) Name of BIP report parameter to control the offset of the chunk.

`fetch_next_rows_parameter`

(optional) Name of BIP report parameter to control the fetch next rows of the chunk.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_DATA_OPERATION_CONFIG_T Type

The information about the data operation.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of data operation.

Allowed values are: 'READ_OPERATION_CONFIG', 'WRITE_OPERATION_CONFIG'

`metadata_config_properties`

(optional) This map is used for passing extra metatdata configuration that is required by read / write operation.

`derived_attributes`

(optional) this map is used for passing BIP report parameter values.

`call_attribute`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PARAMETER_VALUE_T Type

Contains the parameter configuration values.

Syntax
```

```

Fields

Field Description

`string_value`

(optional) A string value of the parameter.

`int_value`

(optional) An integer value of the parameter.

`object_value`

(optional) An object value of the parameter.

`ref_value`

(optional) The root object reference value.

`parameter_value`

(optional) Reference to the parameter by its key.

`root_object_value`

(optional) The root object value, used in custom parameters.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_VALUES_T Type

Configuration values can be string, objects, or parameters.

Syntax
```

```

Fields

Field Description

`config_param_values`

(optional) The configuration parameter values.

`parent_ref`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_T Type

The `TypedObject` class is a base class for any model object that has a type.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the types object.

Allowed values are: 'SHAPE', 'INPUT_PORT', 'SHAPE_FIELD', 'INPUT_FIELD', 'DERIVED_FIELD', 'MACRO_FIELD', 'OUTPUT_FIELD', 'DYNAMIC_PROXY_FIELD', 'OUTPUT_PORT', 'DYNAMIC_INPUT_FIELD', 'PROXY_FIELD', 'PARAMETER', 'PIVOT_FIELD', 'MACRO_PIVOT_FIELD', 'CONDITIONAL_OUTPUT_PORT', 'INPUT_PROXY_FIELD', 'MATERIALIZED_DYNAMIC_FIELD', 'DECISION_OUTPUT_PORT'

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FIELD_T Type

The type representing the abstract field concept.

Syntax
```

```

`dbms_cloud_oci_dataintegration_abstract_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FORMAT_ATTRIBUTE_T Type

The abstract format attribute.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the format attribute.

Allowed values are: 'JSON_FORMAT', 'CSV_FORMAT', 'AVRO_FORMAT'

`is_file_pattern`

(optional) Defines whether a file pattern is supported.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FORMATTED_TEXT_T Type

The type of the formatted text.

Syntax
```

```

Fields

Field Description

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FREQUENCY_DETAILS_T Type

The model that holds the frequency details.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the model

Allowed values are: 'HOURLY', 'DAILY', 'MONTHLY', 'WEEKLY', 'MONTHLY_RULE', 'CUSTOM'

`frequency`

(optional) the frequency of the schedule.

Allowed values are: 'HOURLY', 'DAILY', 'MONTHLY', 'WEEKLY', 'CUSTOM'

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_READ_ATTRIBUTE_T Type

The abstract read attribute.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the abstract read attribute.

Allowed values are: 'ORACLEREADATTRIBUTE', 'ORACLE_READ_ATTRIBUTE', 'BICC_READ_ATTRIBUTE', 'BIP_READ_ATTRIBUTE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_WRITE_ATTRIBUTE_T Type

The abstract write attribute.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the abstract write attribute.

Allowed values are: 'ORACLEWRITEATTRIBUTE', 'ORACLEATPWRITEATTRIBUTE', 'ORACLEADWCWRITEATTRIBUTE', 'OBJECTSTORAGEWRITEATTRIBUTE', 'ORACLE_WRITE_ATTRIBUTE', 'ORACLE_ATP_WRITE_ATTRIBUTE', 'ORACLE_ADWC_WRITE_ATTRIBUTE', 'OBJECT_STORAGE_WRITE_ATTRIBUTE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_typed_object_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PORT_T Type

The input port details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_input_port_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`port_type`

(optional) The port details for the data asset.Type.

Allowed values are: 'DATA', 'CONTROL', 'MODEL'

`fields`

(optional) An array of fields.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_T Type

Parameters are created and assigned values that can be configured for each integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_parameter_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional) This can either be a string value referencing the type or a BaseType object.

`default_value`

(optional) The default value of the parameter.

`root_object_default_value`

(optional) The default value of the parameter which can be an object in DIS, such as a data entity.

`is_input`

(optional) Specifies whether the parameter is input value.

`is_output`

(optional) Specifies whether the parameter is output value.

`output_aggregation_type`

(optional) The output aggregation type.

Allowed values are: 'MIN', 'MAX', 'COUNT', 'SUM'

`type_name`

(optional) The type of value the parameter was created for.

`used_for`

(optional) The param name for which parameter is created for for eg. driver Shape, Operation etc.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_PROXY_FIELD_T Type

The type representing the dynamic proxy field concept. Dynamic proxy fields have a reference to another field.

Syntax
```

```

`dbms_cloud_oci_dataintegration_dynamic_proxy_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MATERIALIZED_COMPOSITE_TYPE_T Type

A `MaterializedCompositeType` represents a type that is composed of a list of sub-types, for example an `Address` type. The sub-types can be simple `DataType` or other `CompositeType` objects. Typically, a `CompositeType` may represent an arbitrarily deep hierarchy of types.

Syntax
```

```

`dbms_cloud_oci_dataintegration_materialized_composite_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`elements`

(optional) An array of elements.

`path_names`

(optional) An array of path names corresponding to the elements. The path names are used when referring to the field in an expression.

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_MATERIALIZED_DYNAMIC_FIELD_T Type

A materialized dynamic field, rules have been applied and all fields are concrete.

Syntax
```

```

`dbms_cloud_oci_dataintegration_materialized_dynamic_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`scope`

(optional) Reference key value to an object within the document.

`l_type`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PORT_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_input_port_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATOR_T Type

An operator defines some data integration semantics in a data flow. It may be reading/writing data or transforming the data.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The model type of the operator.

Allowed values are: 'SOURCE_OPERATOR', 'FILTER_OPERATOR', 'JOINER_OPERATOR', 'AGGREGATOR_OPERATOR', 'PROJECTION_OPERATOR', 'TARGET_OPERATOR', 'FLATTEN_OPERATOR', 'DISTINCT_OPERATOR', 'SORT_OPERATOR', 'UNION_OPERATOR', 'INTERSECT_OPERATOR', 'MINUS_OPERATOR', 'MERGE_OPERATOR', 'FUNCTION_OPERATOR', 'SPLIT_OPERATOR', 'START_OPERATOR', 'END_OPERATOR', 'PIPELINE_OPERATOR', 'DECISION_OPERATOR', 'TASK_OPERATOR', 'EXPRESSION_OPERATOR', 'LOOKUP_OPERATOR', 'PIVOT_OPERATOR'

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Details about the operator.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parameters`

(optional) An array of parameters used in the data flow.

`op_config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_AGGREGATOR_T Type

The information about the aggregator operator. The aggregate operator performs calculations, like sum or count, on all rows or a group of rows to create new, derivative attributes.

Syntax
```

```

`dbms_cloud_oci_dataintegration_aggregator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`group_by_columns`

(optional)

`materialized_group_by_columns`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_OBJECT_METADATA_T Type

A summary type containing information about the object including its key, name and when/who created/updated it.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`name_path`

(optional) The fully qualified path of the published object, which would include its project and folder.

`l_type`

(optional) The type of the object in patch.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`object_version`

(optional) The object version.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`action`

(optional) The patch action indicating if object was created, updated, or deleted.

Allowed values are: 'CREATED', 'DELETED', 'UPDATED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_SOURCE_APPLICATION_INFO_T Type

The information about the application.

Syntax
```

```

Fields

Field Description

`workspace_id`

(optional) The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.

`application_key`

(optional) The source application key to use when creating the application.

`application_version`

(optional) The source application version of the application.

`last_patch_key`

(optional) The last patch key for the application.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_OBJECT_METADATA_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_patch_object_metadata_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_T Type

The application type contains the audit summary information and the definition of the application.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_DETAILS_T Type

The information about the application.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify application.

`model_type`

(required) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) version

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_T Type

The application summary type contains the audit summary information and the definition of the application.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_COLLECTION_T Type

This is the collection of application summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of application summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ARRAY_TYPE_T Type

Array type object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_array_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`element_type`

(optional) Seeded type

### DBMS_CLOUD_OCI_DATAINTEGRATION_AUTH_CONFIG_T Type

Authentication configuration for Generic REST invocation.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify this object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`model_type`

(optional) The specific authentication configuration to be used for Generic REST invocation.

Allowed values are: 'OCI_RESOURCE_AUTH_CONFIG'

### DBMS_CLOUD_OCI_DATAINTEGRATION_AUTH_DETAILS_T Type

Authentication type to be used for Generic REST invocation. This is deprecated.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`model_type`

(optional) The authentication mode to be used for Generic REST invocation.

Allowed values are: 'NO_AUTH_DETAILS', 'RESOURCE_PRINCIPAL_AUTH_DETAILS'

### DBMS_CLOUD_OCI_DATAINTEGRATION_AVRO_FORMAT_ATTRIBUTE_T Type

The AVRO format attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_avro_format_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_format_attribute_t`type.

Fields

Field Description

`compression`

(optional) The compression for the file.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTOR_ATTRIBUTE_T Type

Marker class for connector attributes.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the abstract read attribute.

Allowed values are: 'EXTERNAL_STORAGE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_STORAGE_T Type

BICC Connector Attribute.Object Storage as External storage where the BICC extracted files are written

Syntax
```

```

`dbms_cloud_oci_dataintegration_external_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_connector_attribute_t`type.

Fields

Field Description

`storage_id`

(optional) Id of the external stoarge configured in BICC console. Usually its numeric.

`storage_name`

(optional) Name of the external storage configured in BICC console

`host`

(optional) Object Storage host Url. DO not give http/https.

`tenancy_id`

(optional) Tenancy OCID for the OOS bucket

`namespace`

(optional) Namespace for the OOS bucket

`bucket`

(optional) Bucket Name where BICC extracts stores the files

### DBMS_CLOUD_OCI_DATAINTEGRATION_BICC_READ_ATTRIBUTES_T Type

Properties to configure reading from BICC.

Syntax
```

```

`dbms_cloud_oci_dataintegration_bicc_read_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_read_attribute_t`type.

Fields

Field Description

`fetch_size`

(optional) The fetch size for reading.

`extract_strategy`

(optional) Extraction Strategy - FULL|INCREMENTAL

Allowed values are: 'FULL', 'INCREMENTAL'

`external_storage`

(optional)

`initial_extract_date`

(optional) Date from where extract should start

`last_extract_date`

(optional) Date last extracted

### DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_REPORT_PARAMETER_VALUE_T Type

Report parameter name and value to be passed for BIP Report extraction.

Syntax
```

```

Fields

Field Description

`name`

(required) BIP Report parameter name.

`value`

(required) BIP Report parameter value.

### DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_REPORT_PARAMETER_VALUE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_bip_report_parameter_value_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_READ_ATTRIBUTES_T Type

Properties to configure reading from a FUSION_APP BIP data asset / connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_bip_read_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_read_attribute_t`type.

Fields

Field Description

`fetch_size`

(optional) The fetch size for reading.

`row_limit`

(optional) The maximum number of rows to read.

`offset_parameter`

(optional) Name of BIP report parameter to control the start of the chunk

`fetch_next_rows_parameter`

(optional) Name of BIP report parameter to control the start of the chunk

`custom_parameters`

(optional) An array of custom BIP report parameters and their values.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CANCEL_REST_CALL_CONFIG_T Type

The REST API configuration for cancelling the task.

Syntax
```

```

Fields

Field Description

`method_type`

(optional) The REST method to use.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`request_headers`

(optional) The headers for the REST call.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHANGE_COMPARTMENT_DETAILS_T Type

The information needed to change the workspace compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the the workspace to.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHANGE_DIS_APPLICATION_COMPARTMENT_DETAILS_T Type

The information needed to change the DIS Application compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment to move the the DIS Application to.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_USED_BY_T Type

Referenced object information.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the published object.

`name`

(optional) The name of an published object.

`name_path`

(optional) The name path of the published object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_USED_BY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_reference_used_by_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_T Type

Child reference contains application configuration information.

Syntax
```

```

Fields

Field Description

`key`

(optional) The reference's key, key of the object that is being used by a published object or its dependents.

`name`

(optional) The name of reference object.

`identifier`

(optional) The identifier of reference object.

`identifier_path`

(optional) The identifier path of reference object.

`description`

(optional) The description of reference object.

`l_type`

(optional) The type of the reference object.

Allowed values are: 'ORACLEDB_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_ADWC_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BIP_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION'

`target_object`

(optional) The new reference object to use instead of the original reference. For example, this can be a data asset reference.

`aggregator_key`

(optional) The aggregator key of the child reference object. For example, this can be a data asset key.

`used_by`

(optional) List of published objects where this is used.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_DETAIL_T Type

References used in an application.

Syntax
```

```

Fields

Field Description

`key`

(optional) The child reference key.

`target_object`

(optional) The new reference object to use instead of the original reference. For example, this can be a connection reference.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_T Type

A field map is a way to map a source row shape to a target row shape that may be different.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The model type for the field map.

Allowed values are: 'DIRECT_NAMED_FIELD_MAP', 'COMPOSITE_FIELD_MAP', 'DIRECT_FIELD_MAP', 'RULE_BASED_FIELD_MAP', 'CONDITIONAL_COMPOSITE_FIELD_MAP', 'NAMED_ENTITY_MAP', 'RULE_BASED_ENTITY_MAP'

`description`

(optional) Detailed description for the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_field_map_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_FIELD_MAP_T Type

A composite field map.

Syntax
```

```

`dbms_cloud_oci_dataintegration_composite_field_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`field_maps`

(optional) An array of field maps.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_VALUE_T Type

User defined value for a parameter.

Syntax
```

```

Fields

Field Description

`simple_value`

(optional) A simple value for the parameter.

`root_object_value`

(optional) This can be any object such as a file entity, a schema, or a table.

### DBMS_CLOUD_OCI_DATAINTEGRATION_STATE_T Type

State stored in All States Map of Composite State

Syntax
```

```

Fields

Field Description

`name`

(optional) A simple name for the State.

`parameter_value`

(optional)

`time_value`

(optional) To store a date value for the State we use dateValue attribute.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REGISTRY_METADATA_T Type

Information about the object and its parent.

Syntax
```

```

Fields

Field Description

`aggregator_key`

(optional) The owning object's key for this object.

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.

`registry_version`

(optional) The registry version.

`key`

(optional) The identifying key for the object.

`is_favorite`

(optional) Specifies whether this object is a favorite or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_STATE_T Type

The composite state object provides information on the state of a task or schedule.

Syntax
```

```

Fields

Field Description

`composite_state_aggregator`

(optional) The type of the Composite State Aggregator.

Allowed values are: 'TASK_SCHEDULE', 'TASK', 'TASK_OPERATOR'

`key`

(optional) Generated key that can be used in API calls to identify Composite State.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`all_states_map`

(optional) Map that stores all the States for a given Task or Schedule

`registry_metadata`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_TYPE_ABS_T

A `CompositeType` represents a type that is composed of a list of sub-types, for example an `Address` type. The sub-types can be simple `DataType` or other `CompositeType` objects. Typically, a `CompositeType` may represent an arbitrarily deep hierarchy of types.

Syntax
```

```

`dbms_cloud_oci_dataintegration_composite_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`elements`

(optional) An array of elements.

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_TYPE_T Type

A `CompositeType` represents a type that is composed of a list of sub-types, for example an `Address` type. The sub-types can be simple `DataType` or other `CompositeType` objects. Typically, a `CompositeType` may represent an arbitrarily deep hierarchy of types.

Syntax
```

```

`dbms_cloud_oci_dataintegration_composite_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_composite_type_abs_t`type.

Fields

Field Description

`parent_type`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_COMPRESSION_T Type

The optional compression configuration.

Syntax
```

```

Fields

Field Description

`codec`

(optional) Compression algorithm

Allowed values are: 'NONE', 'AUTO', 'GZIP', 'BZIP2', 'DEFLATE', 'LZ4', 'SNAPPY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_RULE_T Type

Base type for how fields are projected. There are many different mechanisms for doing this such as by a name pattern, datatype and so on. See the `modelType` property for the types.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the project rule.

Allowed values are: 'NAME_PATTERN_RULE', 'TYPE_LIST_RULE', 'NAME_LIST_RULE', 'TYPED_NAME_PATTERN_RULE', 'RENAME_RULE', 'GROUPED_NAME_PATTERN_RULE'

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`is_java_regex_syntax`

(optional) Specifies whether the rule uses a java regex syntax.

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`description`

(optional) A user defined description for the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_RULE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_projection_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_COMPOSITE_FIELD_MAP_T Type

A conditional composite field map.

Syntax
```

```

`dbms_cloud_oci_dataintegration_conditional_composite_field_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`field_map_scope`

(optional) An array of projection rules.

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`field_maps`

(optional) An array of field maps.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_PORT_LINK_T Type

Details about the link between two data flow operators.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The model type of the object.

Allowed values are: 'CONDITIONAL_INPUT_LINK', 'OUTPUT_LINK', 'INPUT_LINK'

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`description`

(optional) Detailed description for the object.

`port`

(optional) Key of FlowPort reference

### DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_LINK_T Type

Details about the outgoing data of an operator in a data flow design.

Syntax
```

```

`dbms_cloud_oci_dataintegration_output_link_t`is a subtype of the`dbms_cloud_oci_dataintegration_flow_port_link_t`type.

Fields

Field Description

`to_links`

(optional) The links from this output link to connect to other links in flow.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPRESSION_T Type

An expression node.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`expr_string`

(optional) The expression string for the object.

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_INPUT_LINK_T Type

The information about the conditional input link.

Syntax
```

```

`dbms_cloud_oci_dataintegration_conditional_input_link_t`is a subtype of the`dbms_cloud_oci_dataintegration_flow_port_link_t`type.

Fields

Field Description

`from_link`

(optional)

`field_map`

(optional)

`condition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_OUTPUT_PORT_T Type

The conditional output port details, used in operators such as split.

Syntax
```

```

`dbms_cloud_oci_dataintegration_conditional_output_port_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`port_type`

(optional) The port details for the data asset.Type.

Allowed values are: 'DATA', 'CONTROL', 'MODEL'

`fields`

(optional) An array of fields.

`split_condition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PROVIDER_ABS_T

The information about the configuration provider.

Syntax
```

```

Fields

Field Description

`bindings`

(optional) The configuration provider bindings.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PROVIDER_T Type

The information about the configuration provider.

Syntax
```

```

Fields

Field Description

`child_providers`

(optional) The child providers.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_T Type

Represents a data source in the Data Integration service.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the data asset.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'LAKE_DATA_ASSET', 'ORACLE_PEOPLESOFT_DATA_ASSET', 'ORACLE_SIEBEL_DATA_ASSET', 'ORACLE_EBS_DATA_ASSET', 'HDFS_DATA_ASSET', 'MYSQL_HEATWAVE_DATA_ASSET', 'REST_DATA_ASSET'

`key`

(optional) Generated key that can be used in API calls to identify data asset.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description of the data asset.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`external_key`

(optional) The external key for the object.

`asset_properties`

(optional) Additional properties for the data asset.

`native_type_system`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_T Type

The connection for a data asset.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the connection.

Allowed values are: 'ORACLE_ADWC_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLEDB_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION', 'BIP_CONNECTION', 'LAKE_CONNECTION', 'ORACLE_PEOPLESOFT_CONNECTION', 'ORACLE_EBS_CONNECTION', 'ORACLE_SIEBEL_CONNECTION', 'HDFS_CONNECTION', 'MYSQL_HEATWAVE_CONNECTION', 'REST_NO_AUTH_CONNECTION', 'REST_BASIC_AUTH_CONNECTION'

`key`

(optional) Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description for the connection.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`primary_schema`

(optional)

`connection_properties`

(optional) The properties for the connection.

`is_default`

(optional) The default property for the connection.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIGURATION_DETAILS_T Type

A key map. If provided, key is replaced with generated key.

Syntax
```

```

Fields

Field Description

`data_asset`

(optional)

`connection`

(optional)

`compartment_id`

(optional) The compartment ID of the object store.

`schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIGURED_TYPE_T Type

A `ConfiguredType` represents a type that has built-in configuration to the type itself. An example is a `SSN` type whose basic type is `VARCHAR`, but the type itself also has a built-in configuration like length=10.

Syntax
```

```

`dbms_cloud_oci_dataintegration_configured_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`wrapped_type`

(optional) A wrapped type, may be a string or a BaseType.

`config_values`

(optional)

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_DETAILS_T Type

The connection details for a data asset.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the connection.

Allowed values are: 'ORACLE_ADWC_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLEDB_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION', 'BIP_CONNECTION', 'LAKE_CONNECTION', 'ORACLE_PEOPLESOFT_CONNECTION', 'ORACLE_EBS_CONNECTION', 'ORACLE_SIEBEL_CONNECTION', 'HDFS_CONNECTION', 'MYSQL_HEATWAVE_CONNECTION', 'REST_NO_AUTH_CONNECTION', 'REST_BASIC_AUTH_CONNECTION'

`key`

(optional) Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description for the connection.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`primary_schema`

(optional)

`connection_properties`

(optional) The properties for the connection.

`is_default`

(optional) The default property for the connection.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SECRET_CONFIG_T Type

Secret configuration if used for storing sensitive info

Syntax
```

```

Fields

Field Description

`model_type`

(required) If OCI vault is used for storing sensitive info

Allowed values are: 'OCI_VAULT_SECRET_CONFIG'

### DBMS_CLOUD_OCI_DATAINTEGRATION_SENSITIVE_ATTRIBUTE_T Type

The sensitive attribute to be used for sensitive content (for password/wallet).

Syntax
```

```

Fields

Field Description

`secret_config`

(optional)

`value`

(optional) Attribute to provide sensitive content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ADWC_T Type

The connection details for an Autonomous Data Warehouse data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Data Warehouse instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ADWC_DETAILS_T Type

The connection details for an Autonomous Data Warehouse data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_adwc_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Data Warehouse instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_AMAZON_S3_T Type

The connection details for Amazon s3 data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`access_key`

(optional)

`secret_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_AMAZON_S3_DETAILS_T Type

The connection details for an Oracle Database data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_amazon_s3_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`access_key`

(optional)

`secret_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ATP_T Type

The connection details for an Autonomous Transaction Processing data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Transaction Processing instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ATP_DETAILS_T Type

The connection details for an Autonomous Transaction Processing data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_atp_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Transaction Processing instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BICC_T Type

The connection details for a FUSION_APP BICC Connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_bicc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

`default_external_storage`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BICC_DETAILS_T Type

The connection details for a FUSION_APP BICC connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_bicc_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

`default_external_storage`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BIP_T Type

The connection details for a Fusion applications BIP connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_bip_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BIP_DETAILS_T Type

The connection details for a Fusion applications BIP connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_bip_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_HDFS_T Type

The connection details for the HDFS data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`hdfs_principal`

(required) The HDFS principal.

`data_node_principal`

(required) The HDFS Data Node principal.

`name_node_principal`

(required) The HDFS Name Node principal.

`realm`

(optional) HDFS Realm name.

`key_distribution_center`

(optional) The HDFS Key Distribution Center.

`key_tab_content`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_HDFS_DETAILS_T Type

The connection details for the HDFS data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_hdfs_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`hdfs_principal`

(required) The HDFS principal.

`data_node_principal`

(required) The HDFS Data Node principal.

`name_node_principal`

(required) The HDFS Name Node principal.

`realm`

(optional) HDFS Realm name.

`key_distribution_center`

(optional) The HDFS Key Distribution Center.

`key_tab_content`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_JDBC_T Type

The connection details for a generic JDBC data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_JDBC_DETAILS_T Type

The connection details for a generic JDBC data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_jdbc_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_LAKE_T Type

The connection details for a Lake connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_LAKE_DETAILS_T Type

The connection details for a Lake connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_lake_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_T Type

The connection details for a MYSQL data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_DETAILS_T Type

The connection details for a MYSQL data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_my_sql_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type

The connection details for a MYSQL HeatWave data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_HEAT_WAVE_DETAILS_T Type

The connection details for a MYSQL HeatWave data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_my_sql_heat_wave_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_OBJECT_STORAGE_T Type

The connection details for an Oracle Object Storage data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`credential_file_content`

(optional) The credential file content from an Oracle Object Storage wallet.

`user_id`

(optional) The OCI user OCID for the user to connect to.

`finger_print`

(optional) The fingerprint for the user.

`pass_phrase`

(optional) The passphrase for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_OBJECT_STORAGE_DETAILS_T Type

The connection summary details for an Oracle Object Storage data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_object_storage_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`credential_file_content`

(optional) The credential file content from an Oracle Object Storage wallet.

`user_id`

(optional) The OCI user OCID for the user to connect to.

`finger_print`

(optional) The fingerprint for the user.

`pass_phrase`

(optional) The passphrase for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_T Type

The connection details for an Oracle Database data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_DETAILS_T Type

The connection details for an Oracle Database data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_EBS_T Type

The connection details for E-Business Suite data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_EBS_DETAILS_T Type

The connection details for an E-Business Suite data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_ebs_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type

The connection details for an Oracle PeopleSoft data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_DETAILS_T Type

The connection details for an Oracle PeopleSoft data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_people_soft_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_SIEBEL_T Type

The connection details for an Oracle Siebel data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_SIEBEL_DETAILS_T Type

The connection details for an Oracle Siebel data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_oracle_siebel_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_BASIC_AUTH_T Type

The connection details for a basic auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_rest_basic_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

Fields

Field Description

`username`

(optional) Username for the connection.

`password_secret`

(optional)

`auth_header`

(optional) Optional header name if used other than default header(Authorization).

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_BASIC_AUTH_DETAILS_T Type

The connection details for a basic auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_rest_basic_auth_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

Fields

Field Description

`username`

(optional) Username for the connection.

`password_secret`

(optional)

`auth_header`

(optional) Optional header name if used other than default header(Authorization).

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_NO_AUTH_T Type

The connection details for a no auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_rest_no_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_NO_AUTH_DETAILS_T Type

The connection details for a no auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_from_rest_no_auth_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_COLLECTION_T Type

This is the collection of connection summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of connection summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ADWC_T Type

The connection summary details for an Autonomous Data Warehouse data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Data Warehouse instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_AMAZON_S3_T Type

The connection summary details for Amazons3 data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`access_key`

(optional)

`secret_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ATP_T Type

The connection details for an Autonomous Transaction Processing data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Transaction Processing instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_BICC_T Type

The connection summary details for a FUSION_APP BICC connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_bicc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_BIP_T Type

The connection summary details for a Fusion applications BIP connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_bip_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_HDFS_T Type

The connection summary details for the HDFS data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`hdfs_principal`

(required) The HDFS principal.

`data_node_principal`

(required) The HDFS Data Node principal.

`name_node_principal`

(required) The HDFS Name Node principal.

`realm`

(optional) HDFS Realm name.

`key_distribution_center`

(optional) The HDFS Key Distribution Center.

`key_tab_content`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_JDBC_T Type

The connection details for a generic JDBC data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_LAKE_T Type

The connection summary details for a Lake connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_MY_SQL_T Type

The connection details for a MYSQL data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_MY_SQL_HEAT_WAVE_T Type

The connection details for a MYSQL HeatWave data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_T Type

The connection summary details for an Oracle Database data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_EBS_T Type

The connection summary details for E-Business Suite data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_PEOPLE_SOFT_T Type

The connection summary details for an Oracle PeopleSoft data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_SIEBEL_T Type

The connection summary details for an Oracle Siebel data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_REST_BASIC_AUTH_T Type

The connection summary for a basic auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_rest_basic_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

Fields

Field Description

`username`

(optional) Username for the connection.

`password_secret`

(optional)

`auth_header`

(optional) Optional header name if used other than default header(Authorization).

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_REST_NO_AUTH_T Type

The connection summary for a no auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_connection_summary_from_rest_no_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_connection_summary_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MESSAGE_T Type

The details of a message.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of message (error, warning, or info).

Allowed values are: 'ERROR', 'WARNING', 'INFO'

`code`

(required) The message code.

`message`

(required) The message text.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_T Type

The information about connection validation.

Syntax
```

```

Fields

Field Description

`validation_message`

(optional)

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_T Type

The information about connection validation.

Syntax
```

```

Fields

Field Description

`validation_message`

(optional)

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_connection_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_COLLECTION_T Type

A list of connection validation summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of connection validation summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_CONFLICT_RESOLUTION_T Type

Copy Object Conflict resolution.

Syntax
```

```

Fields

Field Description

`duplicate_prefix`

(optional) In case of DUPLICATE mode, this prefix will be used to disambiguate the object.

`duplicate_suffix`

(optional) In case of DUPLICATE mode, this suffix will be used to disambiguate the object.

`request_type`

(required) Copy Object Conflict Resolution Type (RETAIN/DUPLICATE/REPLACE).

Allowed values are: 'RETAIN', 'DUPLICATE', 'REPLACE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_METADATA_SUMMARY_T Type

Details of copied objects.

Syntax
```

```

Fields

Field Description

`old_key`

(optional) Old key of the object from where the object was copied. For example a dataflow key within the project being copied.

`new_key`

(optional) New key of the object to identify the copied object. For example the new dataflow key.

`name`

(optional) Name of the object.

`identifier`

(optional) Object identifier.

`object_type`

(optional) Object type.

`object_version`

(optional) Object version.

`aggregator_key`

(optional) Aggregator key

`name_path`

(optional) Object name path.

`time_updated_in_millis`

(optional) time at which this object was last updated.

`resolution_action`

(optional) Object resolution action.

Allowed values are: 'CREATED', 'RETAINED', 'DUPLICATED', 'REPLACED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_METADATA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_copy_object_metadata_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_T Type

Copy metadata object request.

Syntax
```

```

Fields

Field Description

`key`

(optional) Copy object request key.

`source_workspace_id`

(optional) The workspace id of the source from where we need to copy object.

`object_keys`

(optional) The list of the objects to be copied.

`copy_conflict_resolution`

(optional)

`copy_metadata_object_request_status`

(optional) Copy Object request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'TERMINATING', 'TERMINATED'

`created_by`

(optional) OCID of the user who initiated copy request.

`created_by_name`

(optional) Name of the user who created the copy object request.

`total_source_object_count`

(optional) Number of source objects to be copied.

`total_objects_copied_into_target`

(optional) Number of objects copied into the target.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`copied_items`

(optional) The array of copy object details.

`referenced_items`

(optional) The array of copied referenced objects.

`name`

(optional) Name of the copy object request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_T Type

Copy metadata object response summary.

Syntax
```

```

Fields

Field Description

`key`

(optional) Copy object request key.

`source_workspace_id`

(optional) The workspace id of the source from where we need to copy object.

`object_keys`

(optional) The list of the objects to be copied.

`copy_conflict_resolution`

(optional)

`copy_metadata_object_request_status`

(optional) Copy Object request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'TERMINATING', 'TERMINATED'

`created_by`

(optional) OCID of the user who initiated copy request.

`created_by_name`

(optional) Name of the user who created the copy object request.

`total_source_object_count`

(optional) Number of source objects to be copied.

`total_objects_copied_into_target`

(optional) Number of objects copied into the target.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`copied_items`

(optional) The array of copy object details.

`referenced_items`

(optional) The array of copied referenced objects.

`name`

(optional) Name of the copy object request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_copy_object_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_COLLECTION_T Type

This is the collection of copy object requests.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of copy object requests status summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_SOURCE_APPLICATION_INFO_T Type

The information about the application.

Syntax
```

```

Fields

Field Description

`workspace_id`

(optional) The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.

`application_key`

(optional) The source application key to use when creating the application.

`copy_type`

(optional) Parameter to specify the link between SOURCE and TARGET application after copying. CONNECTED - Indicate that TARGET application is conneced to SOURCE and can be synced after copy. DISCONNECTED - Indicate that TARGET application is not conneced to SOURCE and can evolve independently.

Allowed values are: 'CONNECTED', 'DISCONNECTED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_APPLICATION_DETAILS_T Type

Properties used in application create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Currently not used on application creation. Reserved for future.

`model_version`

(optional) The object's model version.

`model_type`

(optional) The type of the application.

Allowed values are: 'INTEGRATION_APPLICATION'

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`source_application_info`

(optional)

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONFIG_PROVIDER_T Type

The type to create a config provider.

Syntax
```

```

Fields

Field Description

`bindings`

(optional) bindings

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_DETAILS_T Type

Properties used in connection create operations.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the connection.

Allowed values are: 'ORACLE_ADWC_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLEDB_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION', 'BIP_CONNECTION', 'LAKE_CONNECTION', 'ORACLE_PEOPLESOFT_CONNECTION', 'ORACLE_EBS_CONNECTION', 'ORACLE_SIEBEL_CONNECTION', 'HDFS_CONNECTION', 'MYSQL_HEATWAVE_CONNECTION', 'REST_NO_AUTH_CONNECTION', 'REST_BASIC_AUTH_CONNECTION'

`key`

(optional) Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description for the connection.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`connection_properties`

(optional) The properties for the connection.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ADWC_T Type

The details to create an Autonomous Data Warehouse data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Data Warehouse instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_AMAZON_S3_T Type

The details to create a Amazon S3 connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`access_key`

(optional)

`secret_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ATP_T Type

The details to create an Autonomous Transaction Processing data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Transaction Processing instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_BICC_T Type

The connection summary details for a FUSION_APP BICC connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_bicc_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

`default_external_storage`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_BIP_T Type

The details to create a Fusion applications BIP connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_bip_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_HDFS_T Type

The details to create the HDFS data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`hdfs_principal`

(required) The HDFS principal.

`data_node_principal`

(required) The HDFS Data Node principal.

`name_node_principal`

(required) The HDFS Name Node principal.

`realm`

(optional) HDFS Realm name.

`key_distribution_center`

(optional) The HDFS Key Distribution Center.

`key_tab_content`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_JDBC_T Type

The details to create a generic JDBC data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_LAKE_T Type

The details to create a Lake connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_MY_SQL_T Type

The details to create a MYSQL data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type

The details to create a MYSQL HeatWave data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_OBJECT_STORAGE_T Type

The details to create an Oracle Object Storage data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`credential_file_content`

(optional) The credential file content from an Oracle Object Storage wallet.

`user_id`

(optional) The OCI user OCID for the user to connect to.

`finger_print`

(optional) The fingerprint for the user.

`pass_phrase`

(optional) The passphrase for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_T Type

The details to create an Oracle Database data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_EBS_T Type

The details to create E-Business Suite data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type

The details to create an Oracle PeopleSoft data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_SIEBEL_T Type

The details to create an Oracle Siebel data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_REST_BASIC_AUTH_T Type

The details to create a basic auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_rest_basic_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

Fields

Field Description

`username`

(required) Username for the connection.

`password_secret`

(required)

`auth_header`

(optional) Optional header name if used other than default header(Authorization).

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_REST_NO_AUTH_T Type

The details to create a no auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_connection_from_rest_no_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_DETAILS_T Type

Properties used in data asset update operations.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the data asset.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'LAKE_DATA_ASSET', 'ORACLE_PEOPLESOFT_DATA_ASSET', 'ORACLE_SIEBEL_DATA_ASSET', 'ORACLE_EBS_DATA_ASSET', 'HDFS_DATA_ASSET', 'MYSQL_HEATWAVE_DATA_ASSET', 'REST_DATA_ASSET'

`key`

(optional) Currently not used on data asset creation. Reserved for future.

`model_version`

(optional) The model version of an object.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description of the data asset.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`external_key`

(optional) The external key for the object.

`asset_properties`

(optional) Additional properties for the data asset.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_VALIDATION_DETAILS_T Type

The properties used in create connection validation operations.

Syntax
```

```

Fields

Field Description

`data_asset`

(optional)

`connection`

(optional)

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_COPY_OBJECT_REQUEST_DETAILS_T Type

Details of copy object.

Syntax
```

```

Fields

Field Description

`source_workspace_id`

(required) The workspace id of the source from where we need to copy object.

`object_keys`

(required) The list of the objects to be copied.

`copy_conflict_resolution`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ADWC_T Type

Details for the Autonomous Data Warehouse data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Data Warehouse instance service name.

`driver_class`

(optional) The Autonomous Data Warehouse driver class.

`credential_file_content`

(optional) The credential file content from a Autonomous Data Warehouse wallet.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`region_id`

(optional) The Autonomous Data Warehouse instance region Id.

`tenancy_id`

(optional) The Autonomous Data Warehouse instance tenancy Id.

`compartment_id`

(optional) The Autonomous Data Warehouse instance compartment Id.

`autonomous_db_id`

(optional) Tha Autonomous Database Id

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_AMAZON_S3_T Type

Details for the Amazons3 data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`l_region`

(optional) The region for Amazon s3

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ATP_T Type

Details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Transaction Processing instance service name.

`driver_class`

(optional) The Autonomous Transaction Processing driver class.

`credential_file_content`

(optional) The credential file content from an Autonomous Transaction Processing wallet.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`region_id`

(optional) The Autonomous Data Warehouse instance region Id.

`tenancy_id`

(optional) The Autonomous Data Warehouse instance tenancy Id.

`compartment_id`

(optional) The Autonomous Data Warehouse instance compartment Id.

`autonomous_db_id`

(optional) Tha Autonomous Database Id

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_FUSION_APP_T Type

Details for the FUSION_APP data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_fusion_app_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`service_url`

(optional) The generic JDBC host name.

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_HDFS_T Type

Details for the HDFS data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The HDFS hostname.

`port`

(required) The HDFS port.

`protocol`

(required) The HDFS Protocol name.

`validate_certificate`

(optional) Specifies whether certificate validation is needed

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_JDBC_T Type

Details for the generic JDBC data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`data_asset_type`

(optional) The data asset type for the generic JDBC data asset.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_LAKE_T Type

Details for the Lake data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`lake_id`

(required) The Lake Ocid.

`metastore_id`

(optional) The metastoreId for the specified Lake Resource.

`lake_proxy_endpoint`

(optional) The lakeProxyEndpoint for the specified Lake Resource.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_MY_SQL_T Type

Details for the MYSQL data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`service_name`

(optional) The generic JDBC service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type

Details for the MYSQL HeatWave data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The MySql HeatWave host name.

`port`

(required) The MySql HeatWave port number.

`service_name`

(optional) The MySql HeatWave service name for the database.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_OBJECT_STORAGE_T Type

Details for the Oracle Object storage data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`oci_region`

(optional) The Oracle Object storage Region ie. us-ashburn-1

`url`

(optional) The Oracle Object storage URL.

`tenancy_id`

(optional) The OCI tenancy OCID.

`namespace`

(optional) The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_T Type

Details for the Oracle Database data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The Oracle Database hostname.

`port`

(optional) The Oracle Database port.

`service_name`

(optional) The service name for the data asset.

`driver_class`

(optional) The Oracle Database driver class.

`sid`

(optional) The Oracle Database SID.

`credential_file_content`

(optional) The credential file content from a wallet for the data asset.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_EBS_T Type

Details for the E-Business Suite data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle EBS hostname.

`port`

(required) The Oracle EBS port.

`service_name`

(optional) The service name for the data asset.

`driver_class`

(optional) The Oracle EBS driver class.

`sid`

(optional) The Oracle EBS SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_T Type

Details for the Oracle PeopleSoft data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle PeopleSoft hostname.

`port`

(required) The Oracle PeopleSoft port.

`service_name`

(optional) The service name for the data asset.

`driver_class`

(optional) The Oracle PeopleSoft driver class.

`sid`

(optional) The Oracle PeopleSoft SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_SIEBEL_T Type

Details for the Oracle Siebel data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle Siebel hostname.

`port`

(required) The Oracle Siebel port.

`service_name`

(optional) The service name for the data asset.

`driver_class`

(optional) The Oracle Siebel driver class.

`sid`

(optional) The Oracle Siebel SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_REST_T Type

Details to create Rest data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_data_asset_from_rest_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_data_asset_details_t`type.

Fields

Field Description

`base_url`

(required) The base url of the rest server.

`manifest_file_content`

(required) The manifest file content of the rest APIs.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_LINK_T Type

Details about the incoming data to an operator in a data flow design.

Syntax
```

```

`dbms_cloud_oci_dataintegration_input_link_t`is a subtype of the`dbms_cloud_oci_dataintegration_flow_port_link_t`type.

Fields

Field Description

`from_link`

(optional) The from link reference.

`field_map`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UI_PROPERTIES_T Type

The UI properties of the object.

Syntax
```

```

Fields

Field Description

`coordinate_x`

(optional) The X coordinate of the object.

`coordinate_y`

(optional) The Y coordinate of the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_LINK_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_input_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_LINK_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_output_link_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_NODE_T Type

The flow node can be connected to other nodes in a data flow with input and output links and is bound to an opertor which defines the semantics of the node.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`input_links`

(optional) An array of input links.

`output_links`

(optional) An array of output links.

`operator`

(optional)

`ui_properties`

(optional)

`config_provider_delegate`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_NODE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_flow_node_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_FLOW_DETAILS_T Type

Properties used in data flow create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_WRAPPER_T Type

A wrapper for a typed object.

Syntax
```

```

Fields

Field Description

`typed_object`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_WRAPPER_T Type

A wrapper for a field map.

Syntax
```

```

Fields

Field Description

`field_map`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_FLOW_VALIDATION_DETAILS_T Type

The properties used in create dataflow validation operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

`typed_object_map`

(optional) A hash map that maps TypedObject keys to the object itself, for java sdk.

`target_field_map_summary`

(optional) A hash map that maps TypedObject keys to a field map that maps to the typed object as a target, for java sdk.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DETAILED_DESCRIPTION_DETAILS_T Type

Properties used in detailed description create operations.

Syntax
```

```

Fields

Field Description

`logo`

(optional) Base64 encoded image to represent logo of the object.

`detailed_description`

(optional) Base64 encoded rich text description of the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DIS_APPLICATION_DETAILS_T Type

Properties used in application create operations.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`key`

(optional) Currently not used on application creation. Reserved for future.

`model_version`

(optional) The object's model version.

`model_type`

(optional) The type of the application.

Allowed values are: 'INTEGRATION_APPLICATION'

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`source_application_info`

(optional)

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_DETAILS_T Type

The data entity shape object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The data entity type.

Allowed values are: 'FILE_ENTITY', 'SQL_ENTITY', 'OBJECT_ENTITY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_T Type

The shape object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_shape_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_TYPE_T Type

A `DerivedType` object represents a more complex type that is derived from a set of simple types, for example an `Address` or `SSN` data type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_derived_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_LIBRARY_T Type

The Data Integration type library container type.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`types`

(optional) types

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_NATIVE_SHAPE_FIELD_T Type

The native shape field object.

Syntax
```

```

Fields

Field Description

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`model_type`

(optional) The model type reference.

`l_type`

(optional) The type reference.

`config_values`

(optional)

`position`

(optional) The position of the attribute.

`default_value_string`

(optional) The default value.

`is_mandatory`

(optional) Specifies whether the field is mandatory.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_FIELD_T Type

The shape field object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_shape_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional) The reference to the type.

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to categorize content.

`native_shape_field`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_ATTRIBUTE_T Type

An attribute within a key, the attribute property is being deprecated.

Syntax
```

```

Fields

Field Description

`position`

(optional) The position of the attribute.

`shape_field`

(optional)

`attribute`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_ATTRIBUTE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_key_attribute_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_KEY_T Type

The unqique key object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The key type.

Allowed values are: 'PRIMARY_KEY', 'UNIQUE_KEY'

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`attribute_refs`

(optional) An array of attribute references.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_T Type

The key object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The key type.

Allowed values are: 'FOREIGN_KEY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOREIGN_KEY_T Type

The foreign key object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_foreign_key_t`is a subtype of the`dbms_cloud_oci_dataintegration_key_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`attribute_refs`

(optional) An array of attribute references.

`update_rule`

(optional) The update rule.

`delete_rule`

(optional) The delete rule.

`reference_unique_key`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FORMAT_T Type

The data format object.

Syntax
```

```

Fields

Field Description

`format_attribute`

(optional)

`l_type`

(optional) type

Allowed values are: 'XML', 'JSON', 'CSV', 'ORC', 'PARQUET', 'AVRO'

`compression_config`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_KEY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_unique_key_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOREIGN_KEY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_foreign_key_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_FILE_T Type

The file data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_entity_shape_from_file_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_entity_shape_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_OBJECT_T Type

The application object entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_entity_shape_from_object_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_entity_shape_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL', 'OBJECT'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_SQL_T Type

The SQL entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_entity_shape_from_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_entity_shape_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`sql_query`

(optional) sqlQuery

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXPORT_REQUEST_DETAILS_T Type

Details of export request. Export is supported using three ways. First, when objectKeys are provided, export of those objects take place. Second, when filter are provided, all the objects based on the filter provided are exported. Third, when neither objectKeys nor filters are provided, we export all the design objects for the workspace.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) Name of the Object Storage bucket where the object will be exported.

`file_name`

(optional) Name of the exported zip file.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`is_object_overwrite_enabled`

(optional) Flag to control whether to overwrite the object if it is already present at the provided object storage location.

`object_keys`

(optional) Field is used to specify which object keys to export

`are_references_included`

(optional) This field controls if the references will be exported along with the objects

`filters`

(optional) Filters for exported objects

### DBMS_CLOUD_OCI_DATAINTEGRATION_RESOURCE_CONFIGURATION_T Type

Properties related to a resource.

Syntax
```

```

Fields

Field Description

`spark_version`

(required) The version of the spark used while creating an Oracle Cloud Infrastructure Data Flow application.

`driver_shape`

(required) The VM shape of the driver used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the driver cores and memory.

`executor_shape`

(required) The shape of the executor used while creating an Oracle Cloud Infrastructure Data Flow application. It sets the executor cores and memory.

`total_executors`

(required) Number of executor VMs requested while creating an Oracle Cloud Infrastructure Data Flow application.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXTERNAL_PUBLICATION_DETAILS_T Type

Properties used to publish an Oracle Cloud Infrastructure Data Flow object.

Syntax
```

```

Fields

Field Description

`application_id`

(optional) The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.

`application_compartment_id`

(required) The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.

`display_name`

(required) The name of the application.

`description`

(optional) The details of the data flow or the application.

`resource_configuration`

(optional)

`configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXTERNAL_PUBLICATION_VALIDATION_DETAILS_T Type

The task type contains the audit summary information and the definition of the task that is published externally.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify the task. On scenarios where reference to the task is needed, a value can be passed in the create operation.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_FOLDER_DETAILS_T Type

The properties used in folder create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Currently not used on folder creation. Reserved for future.

`model_version`

(optional) The model version of an object.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the folder.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_FUNCTION_LIBRARY_DETAILS_T Type

The properties used in FunctionLibrary create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Currently not used on FunctionLibrary creation. Reserved for future.

`model_version`

(optional) The model version of an object.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the FunctionLibrary.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_CONFLICT_RESOLUTION_T Type

Import Objects Conflict resolution.

Syntax
```

```

Fields

Field Description

`duplicate_prefix`

(optional) In case of DUPLICATE mode, prefix will be used to disambiguate the object.

`duplicate_suffix`

(optional) In case of DUPLICATE mode, suffix will be used to disambiguate the object.

`import_conflict_resolution_type`

(required) Import Objects Conflict resolution Type (RETAIN/DUPLICATE/REPLACE).

Allowed values are: 'DUPLICATE', 'REPLACE', 'RETAIN'

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_IMPORT_REQUEST_DETAILS_T Type

Details of import object.

Syntax
```

```

Fields

Field Description

`bucket_name`

(required) Name of the Object Storage bucket where the object will be imported from.

`file_name`

(required) Name of the zip file to be imported.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`object_key_for_import`

(optional) Key of the object inside which all the objects will be imported

`import_conflict_resolution`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PATCH_DETAILS_T Type

Properties used in patch create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object's key.

`model_version`

(optional) The object's model version.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`patch_type`

(required) The type of the patch applied or being applied on the application.

Allowed values are: 'PUBLISH', 'REFRESH', 'UNPUBLISH'

`object_keys`

(required) The array of object keys to publish into application.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ROOT_OBJECT_T Type

A base class for all model types, including First Class and its contained objects.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_VARIABLE_T Type

Variable definitions in the pipeline.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify variable. On scenarios where reference to the variable is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`l_type`

(optional)

`config_values`

(optional)

`default_value`

(optional) A default value for the vairable.

`root_object_default_value`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_VARIABLE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_variable_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PIPELINE_DETAILS_T Type

Properties used in pipeline create operations

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`model_type`

(optional) The type of the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) A list of nodes attached to the pipeline

`parameters`

(optional) A list of additional parameters required in pipeline.

`flow_config_values`

(optional)

`variables`

(optional) The list of variables required in pipeline.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PIPELINE_VALIDATION_DETAILS_T Type

The properties used in create pipeline validation operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`model_type`

(optional) The type of the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) A list of nodes attached to the pipeline.

`parameters`

(optional) A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.

`flow_config_values`

(optional)

`variables`

(optional) The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PROJECT_DETAILS_T Type

The properties used in project create operations.

Syntax
```

```

Fields

Field Description

`model_version`

(optional) The model version of an object.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the project.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`key`

(optional) Generated key that can be used in API calls to identify project.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_SCHEDULE_DETAILS_T Type

The details for creating a schedule.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`frequency_details`

(optional)

`timezone`

(optional) The timezone for the schedule.

`is_daylight_adjustment_enabled`

(optional) A flag to indicate whether daylight adjustment should be considered or not.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_PORT_T Type

The output port details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_output_port_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`port_type`

(optional) The port details for the data asset.Type.

Allowed values are: 'DATA', 'CONTROL', 'MODEL'

`fields`

(optional) An array of fields.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_PORT_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_output_port_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_DETAILS_T Type

Properties used in task create operations.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the task.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_T Type

The data flow type contains the audit summary information and the definition of the data flow.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

`typed_object_map`

(optional) A hash map that maps TypedObject keys to the object itself, for java sdk.

`target_field_map_summary`

(optional) A hash map that maps TypedObject keys to a field map that maps to the typed object as a target, for java sdk.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_DATA_LOADER_TASK_T Type

The information about a data flow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`data_flow`

(optional)

`conditional_composite_field_map`

(optional)

`is_single_load`

(optional) Defines whether Data Loader task is used for single load or multiple

`parallel_load_limit`

(optional) Defines the number of entities being loaded in parallel at a time for a Data Loader task

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_INTEGRATION_TASK_T Type

The information about the integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATAFLOW_APPLICATION_T Type

Minimum information required to recognize a Dataflow Application object.

Syntax
```

```

Fields

Field Description

`application_id`

(optional) The application id for which Oracle Cloud Infrastructure data flow task is to be created.

`compartment_id`

(optional) The compartmentId id under which Oracle Cloud Infrastructure dataflow application lies.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_DETAILS_T Type

OCI DataFlow Shape configuration. Use shapeOcpuParam and shapeMemoryParam config params for configuring number of OCPUs and memory in GBs respectively.

Syntax
```

```

Fields

Field Description

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_OCI_DATAFLOW_TASK_T Type

The information about the OCI Dataflow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_oci_dataflow_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`dataflow_application`

(optional)

`driver_shape_details`

(optional)

`executor_shape_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_T Type

A pipeline is a logical grouping of tasks that together perform a higher level operation. For example, a pipeline could contain a set of tasks that load and clean data, then execute a dataflow to analyze the data. The pipeline allows you to manage the activities as a unit instead of individually. Users can also schedule the pipeline instead of the tasks independently.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`model_type`

(optional) The type of the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) A list of nodes attached to the pipeline.

`parameters`

(optional) A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.

`flow_config_values`

(optional)

`variables`

(optional) The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_PIPELINE_TASK_T Type

The information about the pipeline task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_pipeline_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXECUTE_REST_CALL_CONFIG_T Type

The REST API configuration for execution.

Syntax
```

```

Fields

Field Description

`method_type`

(optional) The REST method to use.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`request_headers`

(optional) The headers for the REST call.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_POLL_REST_CALL_CONFIG_T Type

The REST API configuration for polling.

Syntax
```

```

Fields

Field Description

`method_type`

(optional) The REST method to use.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`request_headers`

(optional) The headers for the REST call.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_EXPRESSION_T Type

The expression that can be created, using the execute stage output in REST Task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_typed_expression_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`expression`

(optional) The expression string for the object.

`l_type`

(optional) The object type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_EXPRESSION_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_typed_expression_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_REST_TASK_T Type

The information about the Generic REST task. The endpoint and cancelEndpoint properties are deprecated, use the properties executeRestCallConfig, cancelRestCallConfig and pollRestCallConfig for execute, cancel and polling of the calls.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_rest_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`auth_details`

(optional)

`auth_config`

(optional)

`endpoint`

(optional)

`method_type`

(optional) The REST method to use. This property is deprecated, use ExecuteRestCallConfig's methodType property instead.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`headers`

(optional) Headers data for the request.

`json_data`

(optional) JSON data for payload body. This property is deprecated, use ExecuteRestCallConfig's payload config param instead.

`api_call_mode`

(optional) The REST invocation pattern to use. ASYNC_OCI_WORKREQUEST is being deprecated as well as cancelEndpoint/MethodType.

Allowed values are: 'SYNCHRONOUS', 'ASYNC_OCI_WORKREQUEST', 'ASYNC_GENERIC'

`cancel_endpoint`

(optional)

`cancel_method_type`

(optional) The REST method to use for canceling the original request.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`execute_rest_call_config`

(optional)

`cancel_rest_call_config`

(optional)

`poll_rest_call_config`

(optional)

`typed_expressions`

(optional) List of typed expressions.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCRIPT_T Type

The script object.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_SQL_TASK_T Type

The information about the SQL task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_from_sql_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_details_t`type.

Fields

Field Description

`script`

(optional)

`sql_script_type`

(optional) Indicates whether the task is invoking a custom SQL script or stored procedure.

Allowed values are: 'STORED_PROCEDURE', 'SQL_CODE'

`operation`

(optional) Describes the shape of the execution result

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_RUN_DETAILS_T Type

The properties used in task run create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`config_provider`

(optional)

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`task_schedule_key`

(optional) Optional task schedule key reference.

`ref_task_run_id`

(optional) Reference Task Run Id to be used for re-run

`re_run_type`

(optional) Supported re-run types

Allowed values are: 'BEGINNING', 'FAILED', 'STEP'

`step_id`

(optional) Step Id for running from a certain step.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_T Type

The schedule object

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`frequency_details`

(optional)

`timezone`

(optional) The timezone for the schedule.

`is_daylight_adjustment_enabled`

(optional) A flag to indicate daylight saving.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_SCHEDULE_DETAILS_T Type

The create task details.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`schedule_ref`

(optional)

`config_provider_delegate`

(optional)

`is_enabled`

(optional) Whether the task schedule is enabled.

`number_of_retries`

(optional) The number of retries.

`retry_delay`

(optional) The retry delay, the unit for measurement is in the property retry delay unit.

`retry_delay_unit`

(optional) The unit for the retry delay.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`start_time_millis`

(optional) The start time in milliseconds.

`end_time_millis`

(optional) The end time in milliseconds.

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`is_backfill_enabled`

(optional) Whether the backfill is enabled.

`auth_mode`

(optional) The authorization mode for the task.

Allowed values are: 'OBO', 'RESOURCE_PRINCIPAL', 'USER_CERTIFICATE'

`expected_duration`

(optional) The expected duration of the task execution.

`expected_duration_unit`

(optional) The expected duration unit of the task execution.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_DETAILS_T Type

The task type contains the audit summary information and the definition of the task.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the task.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in the create operation.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_DATA_LOADER_TASK_T Type

The information about a data flow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_validation_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_validation_details_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_INTEGRATION_TASK_T Type

The information about the integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_validation_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_validation_details_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_PIPELINE_TASK_T Type

The information about a pipeline task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_create_task_validation_from_pipeline_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_create_task_validation_details_t`type.

Fields

Field Description

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_SIGNATURE_T Type

The function signature can specify function paramaters and/or function return type.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

Allowed values are: 'DIS_FUNCTION_SIGNATURE'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`ret_type`

(optional)

`arguments`

(optional) An array of function arguments.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_SIGNATURE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_function_signature_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_USER_DEFINED_FUNCTION_DETAILS_T Type

Properties used in user defined function create operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(required) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(required) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_USER_DEFINED_FUNCTION_VALIDATION_DETAILS_T Type

The properties used in create UserDefinedFunction validation operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

Allowed values are: 'DIS_USER_DEFINED_FUNCTION'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_WORKSPACE_DETAILS_T Type

The information needed to create a new workspace.

Syntax
```

```

Fields

Field Description

`vcn_id`

(optional) The OCID of the VCN the subnet is in.

`subnet_id`

(optional) The OCID of the subnet for customer connected databases.

`dns_server_ip`

(optional) The IP of the custom DNS.

`dns_server_zone`

(optional) The DNS zone of the custom DNS to use to resolve names.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user defined description for the workspace.

`display_name`

(required) A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.

`compartment_id`

(required) The OCID of the compartment containing the workspace.

`is_private_network_enabled`

(optional) Specifies whether the private network connection is enabled or disabled.

`registry_id`

(optional) DCMS Data Asset Registry ID to which the workspace is associated

`endpoint_id`

(optional) DCMS Private Endpoint ID associated with workspace if the pvt networking is enabled

`registry_name`

(optional) DCMS Data Asset Registry display name

`registry_compartment_id`

(optional) DCMS Data Asset Registry Compartment Identifier

`endpoint_name`

(optional) DCMS Private Endpoint Name

`endpoint_compartment_id`

(optional) DCMS PRivate Endpoint Compartment Identifier

### DBMS_CLOUD_OCI_DATAINTEGRATION_CSV_FORMAT_ATTRIBUTE_T Type

The CSV format attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_csv_format_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_format_attribute_t`type.

Fields

Field Description

`encoding`

(optional) The encoding for the file.

`escape_character`

(optional) The escape character for the CSV format.

`delimiter`

(optional) The delimiter for the CSV format.

`quote_character`

(optional) The quote character for the CSV format.

`has_header`

(optional) Defines whether the file has a header row.

`timestamp_format`

(optional) Format for timestamp information.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CUSTOM_FREQUENCY_DETAILS_T Type

Frequency details model to set cron-based frequency

Syntax
```

```

`dbms_cloud_oci_dataintegration_custom_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`custom_expression`

(optional) This holds the complete cron expression for this schedule, for example, 10 0/5 * * * ? that fires every 5 minutes, at 10 seconds after the minute (i.e. 10:00:10 am, 10:05:10 am, etc.)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TIME_T Type

A model to hold time in hour:minute:second format.

Syntax
```

```

Fields

Field Description

`hour`

(optional) The hour value.

`minute`

(optional) The minute value.

`second`

(optional) The second value.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DAILY_FREQUENCY_DETAILS_T Type

Frequency details model to set daily frequency

Syntax
```

```

`dbms_cloud_oci_dataintegration_daily_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`interval`

(optional) This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.

`time`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ADWC_DETAILS_T Type

Details for the Autonomous Data Warehouse data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_adwc_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Data Warehouse instance service name.

`service_names`

(optional) Array of service names that are available for selection in the serviceName property.

`driver_class`

(optional) The Autonomous Data Warehouse driver class.

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_AMAZON_S3_T Type

Details for the MYSQL data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`l_region`

(optional) The region for Amazon s3

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ATP_DETAILS_T Type

Details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_atp_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Transaction Processing instance service name.

`service_names`

(optional) Array of service names that are available for selection in the serviceName property.

`driver_class`

(optional) The Autonomous Transaction Processing driver class.

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_FUSION_APP_T Type

Details for the FUSION_APP data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_fusion_app_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`service_url`

(optional) The service url of the BI Server.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_HDFS_DETAILS_T Type

Details for the HDFS data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_hdfs_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(required) The HDFS hostname.

`port`

(required) The HDFS port.

`protocol`

(required) The HDFS Protocol name.

`validate_certificate`

(optional) Specifies whether certificate validation is needed

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_JDBC_T Type

Details for the generic JDBC data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`data_asset_type`

(optional) The data asset type for the generic JDBC data asset.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_LAKE_DETAILS_T Type

Details for the Lake data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_lake_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`lake_id`

(required) The Lake Ocid.

`metastore_id`

(optional) The metastoreId for the specified Lake Resource.

`lake_proxy_endpoint`

(optional) The lakeProxyEndpoint for the specified Lake Resource.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_MY_SQL_T Type

Details for the MYSQL data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`service_name`

(optional) The generic JDBC service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type

Details for the MYSQL HeatWave data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(optional) The MySql HeatWave host name.

`port`

(optional) The MySql HeatWave port number.

`service_name`

(optional) The MySql HeatWave service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_OBJECT_STORAGE_DETAILS_T Type

Details for the Oracle Object storage data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_object_storage_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`oci_region`

(optional) The Oracle Object storage Region ie. us-ashburn-1

`url`

(optional) The Oracle Object storage URL.

`tenancy_id`

(optional) The OCI tenancy OCID.

`namespace`

(optional) The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_DETAILS_T Type

Details for the Oracle Database data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_oracle_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(optional) The Oracle Database hostname.

`port`

(optional) The Oracle Database port.

`service_name`

(optional) The Oracle Database service name.

`driver_class`

(optional) The Oracle Database driver class.

`sid`

(optional) The Oracle Database SID.

`credential_file_content`

(optional) The credential file content from a wallet for the data asset.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_EBS_DETAILS_T Type

Details for the E-Business Suite data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_oracle_ebs_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(required) The Oracle EBS hostname.

`port`

(required) The Oracle EBS port.

`service_name`

(optional) The Oracle EBS service name.

`driver_class`

(optional) The Oracle EBS driver class.

`sid`

(optional) The Oracle EBS SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_DETAILS_T Type

Details for the Oracle PeopleSoft data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_oracle_people_soft_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(required) The Oracle PeopleSoft hostname.

`port`

(required) The Oracle PeopleSoft port.

`service_name`

(optional) The Oracle PeopleSoft service name.

`driver_class`

(optional) The Oracle PeopleSoft driver class.

`sid`

(optional) The Oracle PeopleSoft SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_SIEBEL_DETAILS_T Type

Details for the Oracle Siebel data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_oracle_siebel_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`host`

(required) The Oracle Siebel hostname.

`port`

(required) The Oracle Siebel port.

`service_name`

(optional) The Oracle Siebel service name.

`driver_class`

(optional) The Oracle Siebel driver class.

`sid`

(optional) The Oracle Siebel SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_REST_DETAILS_T Type

Details for the Rest data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_from_rest_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_t`type.

Fields

Field Description

`base_url`

(optional) The base url of the rest server.

`manifest_file_content`

(optional) The manifest file content of the rest APIs.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_data_asset_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_COLLECTION_T Type

This is the collection of data asset summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of data asset summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ADWC_T Type

Summary details for the Autonomous Data Warehouse data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Data Warehouse instance service name.

`service_names`

(optional) Array of service names that are available for selection in the serviceName property.

`driver_class`

(optional) The Autonomous Data Warehouse driver class.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_AMAZON_S3_T Type

Summary details for the Amazon s3 data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`l_region`

(optional) The region for Amazon s3

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ATP_T Type

Summary details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Transaction Processing instance service name.

`service_names`

(optional) Array of service names that are available for selection in the serviceName property.

`driver_class`

(optional) The Autonomous Transaction Processing driver class.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_FUSION_APP_T Type

Summary details for the FUSION_APP data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_fusion_app_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`service_url`

(optional) The generic JDBC host name.

`default_connection`

(optional)

`staging_data_asset`

(optional)

`staging_connection`

(optional)

`bucket_schema`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_HDFS_T Type

Summary details for the HDFS data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(required) The HDFS hostname.

`port`

(required) The HDFS port.

`protocol`

(required) The HDFS Protocol name.

`validate_certificate`

(optional) Specifies whether certificate validation is needed

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_JDBC_T Type

Summary details for the generic JDBC data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`data_asset_type`

(optional) The data asset type for the generic JDBC data asset.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_LAKE_T Type

Summary details for the Lake data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`lake_id`

(required) The Lake Ocid.

`metastore_id`

(optional) The metastoreId for the specified Lake Resource.

`lake_proxy_endpoint`

(optional) The lakeProxyEndpoint for the specified Lake Resource.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_MY_SQL_T Type

Summary details for the MYSQL data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`service_name`

(optional) The generic JDBC service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_MY_SQL_HEAT_WAVE_T Type

Summary details for the MYSQL HeatWave data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(optional) The MySql HeatWave host name.

`port`

(optional) The MySql HeatWave port number.

`service_name`

(optional) The MySql HeatWave service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_T Type

Summary details for the Oracle Database data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(optional) The Oracle Database hostname.

`port`

(optional) The Oracle Database port.

`service_name`

(optional) The Oracle Database service name.

`driver_class`

(optional) The Oracle Database driver class.

`sid`

(optional) The Oracle Database SID.

`credential_file_content`

(optional) The credential file content from a wallet for the data asset.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_EBS_T Type

Summary details for E-Business Suite data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(required) The Oracle EBS hostname.

`port`

(required) The Oracle EBS port.

`service_name`

(optional) The Oracle EBS service name.

`driver_class`

(optional) The Oracle EBS driver class.

`sid`

(optional) The Oracle EBS SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_PEOPLE_SOFT_T Type

Summary details for the Oracle PeopleSoft data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(required) The Oracle PeopleSoft hostname.

`port`

(required) The Oracle PeopleSoft port.

`service_name`

(optional) The Oracle PeopleSoft service name.

`driver_class`

(optional) The Oracle PeopleSoft driver class.

`sid`

(optional) The Oracle PeopleSoft SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_SIEBEL_T Type

Summary details for the Oracle Siebel data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`host`

(required) The Oracle Siebel hostname.

`port`

(required) The Oracle Siebel port.

`service_name`

(optional) The Oracle Siebel service name.

`driver_class`

(optional) The Oracle Siebel driver class.

`sid`

(optional) The Oracle Siebel SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_REST_T Type

Rest data asset summary.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_asset_summary_from_rest_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_asset_summary_t`type.

Fields

Field Description

`base_url`

(optional) The base url of the rest server.

`manifest_file_content`

(optional) The manifest file content of the rest APIs.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_T Type

The data entity object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The data entity type.

Allowed values are: 'VIEW_ENTITY', 'TABLE_ENTITY', 'FILE_ENTITY', 'SQL_ENTITY', 'OBJECT_ENTITY', 'DATA_STORE_ENTITY', 'DERIVED_ENTITY'

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_DETAILS_T Type

The data entity details object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The data entity type.

Allowed values are: 'VIEW_ENTITY', 'TABLE_ENTITY', 'FILE_ENTITY', 'SQL_ENTITY', 'OBJECT_ENTITY', 'DATA_STORE_ENTITY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_DATA_STORE_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_data_store_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER', 'DATA_STORE'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`filters`

(optional) Filters present in the Datastore. It can be Null.

`is_effective_date_disabled`

(optional) It shows whether or not effective date is disabled

`is_flex_data_store`

(optional) It shows whether the datastore is of flex type

`is_silent_error`

(optional) It shows whether the extraction of this datastore will stop on error

`supports_incremental`

(optional) It shows whether the datastore supports Incremental Extract or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_DATA_STORE_ENTITY_DETAILS_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_data_store_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER', 'DATA_STORE'

`other_type_label`

(optional) Specifies other type labels.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`filters`

(optional) Filters present in the Datastore. It can be Null.

`is_effective_date_disabled`

(optional) It shows whether or not effective date is disabled

`is_flex_data_store`

(optional) It shows whether the datastore is of flex type

`is_silent_error`

(optional) It shows whether the extraction of this datastore will stop on error

`supports_incremental`

(optional) It shows whether the datastore supports Incremental Extract or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_FILE_T Type

The file data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_file_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_FILE_ENTITY_DETAILS_T Type

The file data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_file_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_OBJECT_T Type

The Application Object entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_object_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL', 'OBJECT'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_OBJECT_ENTITY_DETAILS_T Type

The application object entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_object_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL', 'OBJECT'

`other_type_label`

(optional) Specifies other type labels.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_SQL_T Type

The sql entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`sql_query`

(optional) sqlQuery

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_SQL_ENTITY_DETAILS_T Type

The sql entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_sql_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL'

`other_type_label`

(optional) Specifies other type labels.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`sql_query`

(optional) sqlQuery

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_TABLE_T Type

The table entity data entity.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_table_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_TABLE_ENTITY_DETAILS_T Type

The table entity data entity.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_table_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_VIEW_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_view_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_VIEW_ENTITY_DETAILS_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_from_view_entity_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_details_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type labels.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_T Type

The data entity summary object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The data entity type.

Allowed values are: 'VIEW_ENTITY', 'TABLE_ENTITY', 'FILE_ENTITY', 'SQL_ENTITY', 'OBJECT_ENTITY', 'DATA_STORE_ENTITY'

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_data_entity_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_COLLECTION_T Type

This is the collection of data entity summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of data entity summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_DATA_STORE_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_data_store_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER', 'DATA_STORE'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`filters`

(optional) Query filter for the extract. It can be Null.

`is_effective_date_disabled`

(optional) It shows whether or not effective date is disabled

`is_flex_data_store`

(optional) Is Flex data store. Metadata csv will be generated for flex data store

`is_silent_error`

(optional) Should the VO failure fail the whole batch?

`supports_incremental`

(optional) It shows whether the datastore supports Incremental Extract or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_FILE_T Type

The file data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_file_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_OBJECT_T Type

The application object entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_object_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL', 'OBJECT'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_SQL_T Type

The sql entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`sql_query`

(optional) sqlQuery

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_TABLE_T Type

The table entity data entity.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_table_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_VIEW_T Type

The view entity data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_data_entity_summary_from_view_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_summary_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_DETAILS_T Type

The information about a data flow.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_T Type

The data flow summary type contains the audit summary information and the definition of the data flow.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

`typed_object_map`

(optional) A hash map that maps TypedObject keys to the object itself, for java sdk.

`target_field_map_summary`

(optional) A hash map that maps TypedObject keys to a field map that maps to the typed object as a target, for java sdk.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_data_flow_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_COLLECTION_T Type

This is the collection of data flow summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of data flow summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_T Type

The information about a data flow validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the data flow object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_T Type

The information about a data flow validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the data flow object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_data_flow_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_COLLECTION_T Type

A list of data flow validation summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of validation summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DECISION_OPERATOR_T Type

An operator for chosing pipeline path using a condition

Syntax
```

```

`dbms_cloud_oci_dataintegration_decision_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`trigger_rule`

(optional) The merge condition. The conditions are ALL_SUCCESS - All the preceeding operators need to be successful. ALL_FAILED - All the preceeding operators should have failed. ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

Allowed values are: 'ALL_SUCCESS', 'ALL_FAILED', 'ALL_COMPLETE'

`config_provider_delegate`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DECISION_OUTPUT_PORT_T Type

The conditional output port details, used in operators such as decision operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_decision_output_port_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`port_type`

(required) The port details for the data asset.Type.

Allowed values are: 'DATA', 'CONTROL', 'MODEL'

`fields`

(optional) An array of fields.

`decision_output_port_type`

(required) The port based on what decision expression evaluates to.

Allowed values are: 'EVAL_ERROR', 'EVAL_TRUE', 'EVAL_FALSE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_T Type

The information about a dependent object.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_T Type

Details of the dependent object.

Syntax
```

```

Fields

Field Description

`created_by`

(optional) The user that created the object.

`created_by_name`

(optional) The user that created the object.

`updated_by`

(optional) The user that updated the object.

`updated_by_name`

(optional) The user that updated the object.

`time_created`

(optional) The date and time that the object was created.

`time_updated`

(optional) The date and time that the object was updated.

`aggregator_key`

(optional) The owning object key for this object.

`aggregator`

(optional)

`identifier_path`

(optional) The full path to identify this object.

`info_fields`

(optional) Information property fields.

`registry_version`

(optional) The registry version of the object.

`labels`

(optional) Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

`is_favorite`

(optional) Specifies whether this object is a favorite or not.

`count_statistics`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_dependent_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_COLLECTION_T Type

A list of dependent object summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of dependent object summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_T Type

The input Operation for which derived entity is to be formed.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The input Operation type.

Allowed values are: 'PROCEDURE', 'API'

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.

`external_key`

(optional) The external key for the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_ENTITY_T Type

The Derive entity object

Syntax
```

```

`dbms_cloud_oci_dataintegration_derived_entity_t`is a subtype of the`dbms_cloud_oci_dataintegration_data_entity_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`ref_data_object`

(optional)

`l_mode`

(optional) Determines whether entity is treated as source or target

Allowed values are: 'IN', 'OUT'

`derived_properties`

(optional) Property-bag (key-value pairs where key is Shape Field resource name and value is object)

### DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_FIELD_T Type

The type representing the derived field concept. Derived fields have an expression to define how to derive the field.

Syntax
```

```

`dbms_cloud_oci_dataintegration_derived_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`expr`

(optional)

`l_type`

(optional) The type of the field.

`is_use_inferred_type`

(optional) Specifies whether to use inferred expression output type as output type of the derived field. Default value of this flag is false.

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DETAILED_DESCRIPTION_T Type

The detailed description of an object.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the published object.

Allowed values are: 'DETAILED_DESCRIPTION'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

`logo`

(optional) Base64 encoded image to represent logo of the object.

`detailed_description`

(optional) Base64 encoded rich text description of the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCOPE_REFERENCE_T Type

The `ScopeReference` class is a base class for any model object that wraps a scope reference to a TypedObject.

Syntax
```

```

Fields

Field Description

`reference_object`

(required) A key or shallow reference to an object. For direct reference, it points to the actual scope object. For BOUND_ENTITY_SHAPE or BOUND_ENTITY_SHAPE_FIELD, it points to the source or target operator. For OCI_FUNCTION_INPUT_SHAPE or OCI_FUNCTION_OUTPUT_SHAPE, it points to the OCI Function object.

`reference_type`

(optional) The reference type for this reference. Set to null for a direct reference, for indirect references set to a type of association such as \"BOUND_ENTITY_SHAPE\". Current known reference type values are \"BOUND_ENTITY_SHAPE\", \"BOUND_ENTITY_SHAPE_FIELD\", \"OCI_FUNCTION_INPUT_SHAPE\", \"OCI_FUNCTION_OUTPUT_SHAPE\"

Allowed values are: 'DIRECT_REF', 'BOUND_ENTITY_SHAPE', 'BOUND_ENTITY_SHAPE_FIELD', 'OCI_FUNCTION_INPUT_SHAPE', 'OCI_FUNCTION_OUTPUT_SHAPE'

`ref_object_name`

(optional) The referenced object name for this reference. Set to the field name if the referenceType is BOUND_ENTITY_SHAPE_FIELD, else set to null.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIRECT_FIELD_MAP_T Type

The information about a field map.

Syntax
```

```

`dbms_cloud_oci_dataintegration_direct_field_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`source_typed_object`

(optional) Deprecated - Reference to a typed object.

`target_typed_object`

(optional) Deprecated - Reference to a typed object.

`source_scope_reference`

(optional)

`target_scope_reference`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIRECT_NAMED_FIELD_MAP_T Type

A named field map.

Syntax
```

```

`dbms_cloud_oci_dataintegration_direct_named_field_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`source_typed_object`

(optional) Deprecated - Reference to a typed object.

`target_typed_object`

(optional) Deprecated - Reference to a typed object

`source_scope_reference`

(optional)

`target_scope_reference`

(optional)

`source_field_name`

(optional) The source field name.

`target_field_name`

(optional) The target field name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_T Type

DIS Application is container for runtime objects.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_T Type

The application summary type contains the audit summary information and the definition of the application.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_dis_application_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_COLLECTION_T Type

This is the collection of application summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of application summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DISTINCT_T Type

The information about the distinct operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_distinct_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_INPUT_FIELD_T Type

The type representing the dynamic field concept. Dynamic fields have a dynamic type handler to define how to generate the field.

Syntax
```

```

`dbms_cloud_oci_dataintegration_dynamic_input_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_TYPE_HANDLER_T Type

This type defines how to derived fields for the dynamic type itself.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The dynamic type handler.

Allowed values are: 'RULE_TYPE_CONFIGS', 'FLATTEN_TYPE_HANDLER'

### DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_TYPE_T Type

The dynamic type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_dynamic_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`type_handler`

(optional)

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_END_OPERATOR_T Type

Represents end of a pipeline

Syntax
```

```

`dbms_cloud_oci_dataintegration_end_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`trigger_rule`

(optional) The merge condition. The conditions are ALL_SUCCESS - All the preceeding operators need to be successful. ALL_FAILED - All the preceeding operators should have failed. ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

Allowed values are: 'ALL_SUCCESS', 'ALL_FAILED', 'ALL_COMPLETE'

### DBMS_CLOUD_OCI_DATAINTEGRATION_ENRICHED_ENTITY_T Type

This is used to specify runtime parameters for data entities such as files that need both the data entity and the format.

Syntax
```

```

Fields

Field Description

`entity`

(optional)

`data_format`

(optional)

`model_type`

(optional) The model type for the entity which is referenced.

`parent_ref`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_T Type

The data entity shape object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The data entity type.

Allowed values are: 'FILE_ENTITY', 'SQL_ENTITY', 'OBJECT_ENTITY'

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_FILE_T Type

The file data entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_entity_shape_from_file_t`is a subtype of the`dbms_cloud_oci_dataintegration_entity_shape_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`types`

(optional)

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'QUEUE', 'STREAM', 'OTHER'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_OBJECT_T Type

The application object entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_entity_shape_from_object_t`is a subtype of the`dbms_cloud_oci_dataintegration_entity_shape_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL', 'OBJECT'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_SQL_T Type

The SQL entity details.

Syntax
```

```

`dbms_cloud_oci_dataintegration_entity_shape_from_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_entity_shape_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`shape`

(optional)

`shape_id`

(optional) The shape ID.

`entity_type`

(optional) The entity type.

Allowed values are: 'TABLE', 'VIEW', 'FILE', 'SQL'

`other_type_label`

(optional) Specifies other type label.

`unique_keys`

(optional) An array of unique keys.

`foreign_keys`

(optional) An array of foreign keys.

`resource_name`

(optional) The resource name.

`data_format`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`sql_query`

(optional) sqlQuery

### DBMS_CLOUD_OCI_DATAINTEGRATION_ERROR_DETAILS_T Type

The details of an error that occured.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A user-friendly error message.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_OBJECT_METADATA_SUMMARY_T Type

Details of the exported object

Syntax
```

```

Fields

Field Description

`key`

(optional) Key of the object

`name`

(optional) Name of the object

`identifier`

(optional) Object identifier

`object_type`

(optional) Object type

`object_version`

(optional) Object version

`aggregator_key`

(optional) Aggregator key

`name_path`

(optional) Object name path

`time_updated_in_millis`

(optional) time at which this object was last updated.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_OBJECT_METADATA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_export_object_metadata_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_T Type

Export metadata object response.

Syntax
```

```

Fields

Field Description

`key`

(optional) Export object request key

`object_keys`

(optional) The list of the objects to be exported

`bucket_name`

(optional) The name of the Object Storage Bucket where the objects will be exported to

`file_name`

(optional) Name of the exported zip file.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`are_references_included`

(optional) Controls if the references will be exported along with the objects

`is_object_overwrite_enabled`

(optional) Flag to control whether to overwrite the object if it is already present at the provided object storage location.

`filters`

(optional) Export multiple objects based on filters.

`status`

(optional) Export Objects request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'QUEUED'

`created_by`

(optional) Name of the user who initiated export request.

`total_exported_object_count`

(optional) Number of objects that are exported.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`error_messages`

(optional) Contains key of the error

`exported_items`

(optional) The array of exported object details.

`referenced_items`

(optional) The array of exported referenced objects.

`name`

(optional) Name of the export request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_T Type

Export metadata object response summary.

Syntax
```

```

Fields

Field Description

`key`

(optional) Export object request key

`object_keys`

(optional) The list of the objects to be exported

`bucket_name`

(optional) The name of the Object Storage Bucket where the objects will be exported to

`file_name`

(optional) Name of the exported zip file.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`are_references_included`

(optional) Controls if the references will be exported along with the objects

`is_object_overwrite_enabled`

(optional) Flag to control whether to overwrite the object if it is already present at the provided object storage location.

`filters`

(optional) Export multiple objects based on filters.

`status`

(optional) Export Objects request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'QUEUED'

`created_by`

(optional) Name of the user who initiated export request.

`total_exported_object_count`

(optional) Number of objects that are exported.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`error_messages`

(optional) Contains key of the error

`exported_items`

(optional) The array of exported object details.

`referenced_items`

(optional) The array of exported referenced objects.

`name`

(optional) Name of the export request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_export_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_COLLECTION_T Type

This is the collection of export object requests.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of export object requests status summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXPRESSION_OPERATOR_T Type

An operator for expressions

Syntax
```

```

`dbms_cloud_oci_dataintegration_expression_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`trigger_rule`

(optional) The merge condition. The conditions are ALL_SUCCESS - All the preceeding operators need to be successful. ALL_FAILED - All the preceeding operators should have failed. ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

Allowed values are: 'ALL_SUCCESS', 'ALL_FAILED', 'ALL_COMPLETE'

`config_provider_delegate`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_T Type

The external published object contains the audit summary information and the definition of the task.

Syntax
```

```

Fields

Field Description

`application_id`

(optional) The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.

`application_compartment_id`

(optional) The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.

`display_name`

(optional) The name of the application.

`resource_configuration`

(optional)

`configuration_details`

(optional)

`status`

(optional) The status of the publishing action to Oracle Cloud Infrastructure Data Flow.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'PUBLISHING'

`error_message`

(optional) The error of the published object in the application.

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects. Other values are reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_T Type

The external publication summary contains the audit summary information and the definition of the external object.

Syntax
```

```

Fields

Field Description

`application_id`

(optional) The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.

`application_compartment_id`

(optional) The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.

`display_name`

(optional) The name of the application.

`resource_configuration`

(optional)

`configuration_details`

(optional)

`status`

(optional) The status of the publishing action to Oracle Cloud Infrastructure Data Flow.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'PUBLISHING'

`error_message`

(optional) The error of the published object in the application.

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects. Other values are reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_external_publication_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_COLLECTION_T Type

This is the collection of external publication summaries. It may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of external publication summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_T Type

The information about external published task validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) Total number of validation messages.

`error_message_count`

(optional) Total number of validation error messages.

`warn_message_count`

(optional) Total number of validation warning messages.

`info_message_count`

(optional) Total number of validation information messages.

`validation_messages`

(optional) Detailed information of the data flow object validation.

`key`

(optional) Objects use a 36 character key as unique ID. It is system generated and cannot be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_T Type

The external publication validation summary contains the validation summary information and the definition of the external object.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) Total number of validation messages.

`error_message_count`

(optional) Total number of validation error messages.

`warn_message_count`

(optional) Total number of validation warning messages.

`info_message_count`

(optional) Total number of validation information messages.

`validation_messages`

(optional) Detailed information of the data flow object validation.

`key`

(optional) Objects use a 36 character key as unique ID. It is system generated and cannot be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_external_publication_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_COLLECTION_T Type

This is the collection of external publication validation summaries. It may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of external publication summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FILTER_T Type

The information about the filter object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_filter_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`filter_condition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUSH_DOWN_OPERATION_T Type

The information about a push down operation.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of operation.

Allowed values are: 'FILTER', 'JOIN', 'SELECT', 'SORT', 'QUERY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_FILTER_PUSH_T Type

The information about a filter operator. The filter operator lets you select certain attributes from the inbound port to continue downstream to the outbound port.

Syntax
```

```

`dbms_cloud_oci_dataintegration_filter_push_t`is a subtype of the`dbms_cloud_oci_dataintegration_push_down_operation_t`type.

Fields

Field Description

`filter_condition`

(optional) The filter condition.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_PROJECTION_PREFERENCES_T Type

The preferences for the flatten operation.

Syntax
```

```

Fields

Field Description

`create_array_index`

(required) Property defining whether to create array indexes in flattened result.

Allowed values are: 'ALLOW', 'DO_NOT_ALLOW'

`retain_all_attributes`

(required) Property defining whether to retain all attributes in flattened result.

Allowed values are: 'ALLOW', 'DO_NOT_ALLOW'

`ignore_null_values`

(required) Property defining whether to ignore null values in flattened result.

Allowed values are: 'ALLOW', 'DO_NOT_ALLOW'

`retain_parent_name_lineage`

(required) Property defining whether to retain parent name lineage.

Allowed values are: 'ALLOW', 'DO_NOT_ALLOW'

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_DETAILS_T Type

Details for the flatten operator.

Syntax
```

```

Fields

Field Description

`flatten_projection_preferences`

(optional)

`flatten_attribute_root`

(optional) The string of flatten attribute column name where the flatten process starts.

`flatten_attribute_path`

(optional) The string of flatten attribute path in flattenAttributeRoot from upper level to leaf/targeted level concatenated with dot(.).

`flatten_columns`

(optional) The array of flatten columns which are the input to flatten.

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_T Type

The information about a flatten object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_flatten_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`flatten_details`

(optional)

`flatten_field`

(optional)

`materialized_flatten_field`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_TYPE_HANDLER_T Type

The flatten type handler.

Syntax
```

```

`dbms_cloud_oci_dataintegration_flatten_type_handler_t`is a subtype of the`dbms_cloud_oci_dataintegration_dynamic_type_handler_t`type.

Fields

Field Description

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`scope`

(optional) Reference key for the typed object.

`flatten_details`

(optional) Contains a key for referencing the flattenDetails information.

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_PORT_T Type

Each operator owns a set of `InputPort` and `OutputPort` objects (can scale to zero), which represent the ports that can be connected to/from the operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_flow_port_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_T Type

The folder type contains the audit summary information and the definition of the folder.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify folder.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the folder.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_DETAILS_T Type

The details including name, description for the folder, which is a container of other folders, tasks and dataflows.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify folder.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the folder.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_T Type

The folder summary type contains the audit summary information and the definition of the folder.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify folder.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the folder.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_folder_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_COLLECTION_T Type

A collection of folder summaries. The collection can be lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of folder summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_CONFIGURATION_DEFINITION_T Type

The configuration details of a configurable object. This contains one or more config param definitions.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

Allowed values are: 'CONFIG_DEFINITION'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`is_contained`

(optional) Specifies whether the configuration is contained or not.

`config_param_defs`

(optional) The parameter configuration details.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OCI_FUNCTION_T Type

The information about the OCI Function.

Syntax
```

```

Fields

Field Description

`function_id`

(optional) Ocid of the OCI Function.

`region_id`

(optional) Region where the OCI Function is deployed.

`fn_config_definition`

(optional)

`input_shape`

(optional)

`output_shape`

(optional)

`model_type`

(optional) The type of the OCI Function object.

Allowed values are: 'OCI_FUNCTION'

`key`

(optional) The key identifying the OCI Function operator object, use this to identiy this instance within the dataflow.

`parent_ref`

(optional)

`model_version`

(optional) The model version of an object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`payload_format`

(optional) The OCI Function payload format.

Allowed values are: 'JSON', 'AVRO', 'JSONBYTES'

`fn_config_def`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_T Type

The Function operator supports users adding a custom OCI Function into the data flow.

Syntax
```

```

`dbms_cloud_oci_dataintegration_function_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`oci_function`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_T Type

The FunctionLibrary type contains the audit summary information and the definition of the FunctionLibrary.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify FunctionLibrary.

`model_type`

(optional) The type of the object.

Allowed values are: 'FUNCTION_LIBRARY'

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the Function Library.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_DETAILS_T Type

The details including name, description for the function library, which is a container for user defined functions.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify FunctionLibrary.

`model_type`

(required) The type of the object.

Allowed values are: 'FUNCTION_LIBRARY'

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the FunctionLibrary.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_T Type

The FunctionLibrary summary type contains the audit summary information and the definition of the Function Library.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify FunctionLibrary.

`model_type`

(optional) The type of the object.

Allowed values are: 'FUNCTION_LIBRARY'

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the Function Library.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_function_library_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_COLLECTION_T Type

A collection of FunctionLibrary summaries. The collection can be lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of FunctionLibrary summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_GENERIC_REST_API_ATTRIBUTES_T Type

Generic rest api specific attributes.

Syntax
```

```

Fields

Field Description

`server_url`

(optional) The server URL serving operation.

### DBMS_CLOUD_OCI_DATAINTEGRATION_GENERIC_REST_CALL_ATTRIBUTE_T Type

Properties to configure reading from a REST data asset / connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_generic_rest_call_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_call_attribute_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_GROUPED_NAME_PATTERN_RULE_T Type

This rule projects fields as a group recognised as name pattern.

Syntax
```

```

`dbms_cloud_oci_dataintegration_grouped_name_pattern_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`name`

(optional) Name of the group.

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`scope`

(optional) Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`is_cascade`

(optional) Specifies whether to cascade or not.

`matching_strategy`

(optional) The pattern matching strategy.

Allowed values are: 'NAME_OR_TAGS', 'TAGS_ONLY', 'NAME_ONLY'

`is_case_sensitive`

(optional) Specifies if the rule is case sensitive.

`rule_type`

(optional) The rule type.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`pattern`

(optional) The rule pattern.

### DBMS_CLOUD_OCI_DATAINTEGRATION_HOURLY_FREQUENCY_DETAILS_T Type

Frequency details model to set hourly frequency

Syntax
```

```

`dbms_cloud_oci_dataintegration_hourly_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`interval`

(optional) This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.

`time`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_OBJECT_METADATA_SUMMARY_T Type

Details of the objects to imported.

Syntax
```

```

Fields

Field Description

`old_key`

(optional) Old key of the object

`new_key`

(optional) New key of the object

`name`

(optional) Name of the object

`identifier`

(optional) Object identifier

`object_type`

(optional) Object type

`object_version`

(optional) Object version

`aggregator_key`

(optional) Aggregator key

`name_path`

(optional) Object name path

`time_updated_in_millis`

(optional) time at which this object was last updated.

`resolution_action`

(optional) Object resolution action

Allowed values are: 'CREATED', 'RETAINED', 'DUPLICATED', 'REPLACED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_OBJECT_METADATA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_import_object_metadata_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_T Type

Import metadata object response.

Syntax
```

```

Fields

Field Description

`key`

(optional) Import object request key

`bucket_name`

(optional) The name of the Object Storage Bucket where the objects will be imported from

`file_name`

(optional) Name of the zip file from which objects will be imported.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`object_key_for_import`

(optional) Key of the object inside which all the objects will be imported

`import_conflict_resolution`

(optional)

`status`

(optional) Import Objects request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'QUEUED'

`created_by`

(optional) Name of the user who initiated import request.

`total_imported_object_count`

(optional) Number of objects that are imported.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`error_messages`

(optional) Contains key of the error

`imported_objects`

(optional) The array of imported object details.

`name`

(optional) Name of the import request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_T Type

Import metadata object response summary.

Syntax
```

```

Fields

Field Description

`key`

(optional) Import object request key

`bucket_name`

(optional) The name of the Object Storage Bucket where the objects will be imported from

`file_name`

(optional) Name of the zip file from which objects will be imported.

`object_storage_tenancy_id`

(optional) Optional parameter to point to object storage tenancy (if using Object Storage of different tenancy)

`object_storage_region`

(optional) Region of the object storage (if using object storage of different region)

`object_key_for_import`

(optional) Key of the object inside which all the objects will be imported

`import_conflict_resolution`

(optional)

`status`

(optional) Import Objects request status.

Allowed values are: 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS', 'TERMINATING', 'TERMINATED', 'QUEUED'

`created_by`

(optional) Name of the user who initiated import request.

`total_imported_object_count`

(optional) Number of objects that are imported.

`time_started_in_millis`

(optional) Time at which the request started getting processed.

`time_ended_in_millis`

(optional) Time at which the request was completely processed.

`error_messages`

(optional) Contains key of the error

`imported_objects`

(optional) The array of imported object details.

`name`

(optional) Name of the import request.

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_import_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_COLLECTION_T Type

This is the collection of import object requests.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of import object requests status summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_DATA_ENTITY_CLAUSE_T Type

Data Entity clause for Incremental Read operation.

Syntax
```

```

Fields

Field Description

`incremental_data_entity_name`

(required) Name of incremental data entity filter.

`incremental_data_entity_value`

(required) Value of incremental data entity filter.

`incremental_comparator`

(required) Incremental comparator symbol.

Allowed values are: 'LESSTHAN', 'GREATERTHAN', 'EQUALS', 'LESSTHANEQUALS', 'GREATERTHANEQUALS', 'STARTSWITH', 'CONTAINS'

### DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_FIELD_CLAUSE_T Type

Field clause for incremental read operation.

Syntax
```

```

Fields

Field Description

`incremental_field_name`

(required) Name of incremental field filter.

`incremental_field_value`

(required) Value of incremental field filter.

`incremental_comparator`

(required) Incremental comparator symbol.

Allowed values are: 'LESSTHAN', 'GREATERTHAN', 'EQUALS', 'LESSTHANEQUALS', 'GREATERTHANEQUALS', 'STARTSWITH', 'CONTAINS'

### DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_FIELD_CLAUSE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_incremental_field_clause_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_DATA_ENTITY_CLAUSE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_incremental_data_entity_clause_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_READ_CONFIG_T Type

Config for incremental read operation.

Syntax
```

```

Fields

Field Description

`last_extracted_field_date`

(optional) List of incremental field clauses.

`last_extracted_data_entity_date`

(optional) List of incremental data entity clauses.

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_FIELD_T Type

The input field for an operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_input_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PROXY_FIELD_T Type

A proxy field to be used as an input field.

Syntax
```

```

`dbms_cloud_oci_dataintegration_input_proxy_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`scope`

(optional) Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a `TypedObject` or a full `TypedObject` definition.

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_INTERSECT_T Type

The information about a intersect object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_intersect_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`intersect_type`

(optional) intersectType

Allowed values are: 'NAME', 'POSITION'

`is_all`

(optional) The information about the intersect all.

### DBMS_CLOUD_OCI_DATAINTEGRATION_JAVA_TYPE_T Type

A java type object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_java_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`java_type_name`

(optional) The java type name.

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_JOIN_T Type

The information about the join operator. The join operator links data from multiple inbound sources.

Syntax
```

```

`dbms_cloud_oci_dataintegration_join_t`is a subtype of the`dbms_cloud_oci_dataintegration_push_down_operation_t`type.

Fields

Field Description

`condition`

(optional) The join condition.

`policy`

(optional) The type of join.

Allowed values are: 'INNER_JOIN', 'LEFT_JOIN', 'RIGHT_JOIN', 'FULL_JOIN'

### DBMS_CLOUD_OCI_DATAINTEGRATION_JOINER_T Type

The information about a joiner object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_joiner_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`join_type`

(optional) joinType

Allowed values are: 'INNER', 'FULL', 'LEFT', 'RIGHT'

`join_condition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_FORMAT_ATTRIBUTE_T Type

The JSON file format attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_json_format_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_format_attribute_t`type.

Fields

Field Description

`encoding`

(optional) The encoding for the file.

`sample_entity_data`

(optional) Sample JSON with all fields of JSON schema specified in it for the JSON data files used in Data Flow, Data Loader or Data Preview and should be specified in Base64 encoded format. Maximum size is 2 MB.

### DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_TEXT_T Type

The JSON type of the formatted text.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The object type.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_RANGE_T Type

The information about key range.

Syntax
```

```

Fields

Field Description

`key`

(optional)

`range`

(optional) The key range.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARTITION_CONFIG_T Type

The information about partition configuration.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of partition configuration.

Allowed values are: 'KEYRANGEPARTITIONCONFIG'

### DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_RANGE_PARTITION_CONFIG_T Type

The information about key range.

Syntax
```

```

`dbms_cloud_oci_dataintegration_key_range_partition_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_partition_config_t`type.

Fields

Field Description

`partition_number`

(optional) The partition number for the key range.

`key_range`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_LAST_RUN_DETAILS_T Type

The last run details for the task run.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify Last run details of a task schedule. On scenarios where reference to the lastRunDetails is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`last_run_time_millis`

(optional) Time in milliseconds for the pervious schedule.

### DBMS_CLOUD_OCI_DATAINTEGRATION_LOOKUP_T Type

The information about the lookup operator. The lookup operator has two input links, a primary input, and a lookup source input. It has an output link, fields of the lookup input are appended to the primary input and projected as the output fields.

Syntax
```

```

`dbms_cloud_oci_dataintegration_lookup_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`lookup_condition`

(optional)

`is_skip_no_match`

(optional) For the rows for which lookup condition does not satisfy, if set to true - do not return those rows of primary Input source and if set to false - create a row with primary input fields values and lookup field values as NULL.

`multi_match_strategy`

(optional) if there are multiple records found in the lookup input what action should be performed. The default value for this field is RETURN_ANY.

Allowed values are: 'RETURN_ANY', 'RETURN_FIRST', 'RETURN_LAST', 'RETURN_ALL', 'RETURN_ERROR'

`null_fill_values`

(optional) this map is used for replacing NULL values in the record. Key is the column name and value is the NULL replacement.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MACRO_FIELD_T Type

The type representing the macro field concept. Macro fields have an expression to define a macro.

Syntax
```

```

`dbms_cloud_oci_dataintegration_macro_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`expr`

(optional)

`l_type`

(optional)

`is_use_source_type`

(optional) Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).

`use_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MACRO_PIVOT_FIELD_T Type

MacroPivotField is used for the PivotField with macro expressions. It can contain the rules according to the macro pattern/attribute added and create new fields according to the PivotKeyValues

Syntax
```

```

Fields

Field Description

`is_use_source_type`

(optional) Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).

`expr`

(optional)

`use_type`

(optional)

`l_type`

(optional)

`column_name_pattern`

(optional) column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MAP_TYPE_T Type

Map type object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_map_type_t`is a subtype of the`dbms_cloud_oci_dataintegration_base_type_t`type.

Fields

Field Description

`key_element_type`

(optional) Seeded type

`value_element_type`

(optional) Seeded type

`contains_null`

(optional) Defines whether null values are allowed.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MERGE_OPERATOR_T Type

Represents the start of a pipeline.

Syntax
```

```

`dbms_cloud_oci_dataintegration_merge_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`trigger_rule`

(optional) The merge condition. The conditions are ALL_SUCCESS - All the preceeding operators need to be successful. ALL_FAILED - All the preceeding operators should have failed. ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed. ONE_SUCCESS - Atleast one of the preceeding operators should have succeeded. ONE_FAILED - Atleast one of the preceeding operators should have failed.

Allowed values are: 'ALL_SUCCESS', 'ALL_FAILED', 'ALL_COMPLETE', 'ONE_SUCCESS', 'ONE_FAILED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_MINUS_T Type

The information about a minus object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_minus_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`minus_type`

(optional) minusType

Allowed values are: 'NAME', 'POSITION'

`is_all`

(optional) The information about the minus all.

### DBMS_CLOUD_OCI_DATAINTEGRATION_NUMBER_TBL Type

Nested table type of number.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_MONTHLY_FREQUENCY_DETAILS_T Type

Frequency Details model for monthly frequency.

Syntax
```

```

`dbms_cloud_oci_dataintegration_monthly_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`interval`

(optional) This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.

`time`

(optional)

`days`

(optional) A list of days of the month to be scheduled. i.e. excute every 2nd,3rd, 10th of the month.

### DBMS_CLOUD_OCI_DATAINTEGRATION_MONTHLY_RULE_FREQUENCY_DETAILS_T Type

Frequency Details model for monthly frequency based on week of month and day of week.

Syntax
```

```

`dbms_cloud_oci_dataintegration_monthly_rule_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`week_of_month`

(optional) This holds the week of the month in which the schedule should be triggered.

Allowed values are: 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'LAST'

`interval`

(optional) This hold the repeatability aspect of a schedule. i.e. in a monhtly frequency, a task can be scheduled for every month, once in two months, once in tree months etc.

`time`

(optional)

`day_of_week`

(optional) This holds the day of the week on which the schedule should be triggered.

Allowed values are: 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_NAME_LIST_RULE_T Type

The name list rule which defines how fields are projected. For example, this may be all fields begining with STR.

Syntax
```

```

`dbms_cloud_oci_dataintegration_name_list_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`scope`

(optional) Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`is_cascade`

(optional) Specifies whether to cascade or not.

`matching_strategy`

(optional) The pattern matching strategy.

Allowed values are: 'NAME_OR_TAGS', 'TAGS_ONLY', 'NAME_ONLY'

`is_case_sensitive`

(optional) Specifies if the rule is case sensitive.

`rule_type`

(optional) The rule type.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`names`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

### DBMS_CLOUD_OCI_DATAINTEGRATION_NAME_PATTERN_RULE_T Type

This rule projects fields by a name pattern, for example it may start with STR_ or end with _DATE. This is defined using a regular expression.

Syntax
```

```

`dbms_cloud_oci_dataintegration_name_pattern_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`scope`

(optional) Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`is_cascade`

(optional) Specifies whether to cascade or not.

`matching_strategy`

(optional) The pattern matching strategy.

Allowed values are: 'NAME_OR_TAGS', 'TAGS_ONLY', 'NAME_ONLY'

`is_case_sensitive`

(optional) Specifies if the rule is case sensitive.

`rule_type`

(optional) The rule type.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`pattern`

(optional) The rule pattern.

### DBMS_CLOUD_OCI_DATAINTEGRATION_NAMED_ENTITY_MAP_T Type

A named field map.

Syntax
```

```

`dbms_cloud_oci_dataintegration_named_entity_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`source_entity`

(optional) The source entity name.

`target_entity`

(optional) The target entity name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_STORAGE_WRITE_ATTRIBUTE_T Type

Properties to configure writing to Object Storage.

Syntax
```

```

`dbms_cloud_oci_dataintegration_object_storage_write_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`write_to_single_file`

(optional) Specifies whether to write output to single-file or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_STORAGE_WRITE_ATTRIBUTES_T Type

Properties to configure writing to Object Storage.

Syntax
```

```

`dbms_cloud_oci_dataintegration_object_storage_write_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`write_to_single_file`

(optional) Specifies whether to write output to single-file or not.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OCI_VAULT_SECRET_CONFIG_T Type

Properties used for specifying OCI vault configuration

Syntax
```

```

`dbms_cloud_oci_dataintegration_oci_vault_secret_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_secret_config_t`type.

Fields

Field Description

`secret_id`

(optional) OCID of the OCI vault secret

### DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_T Type

The operation object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The operation type.

Allowed values are: 'PROCEDURE', 'API'

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_FROM_API_T Type

The API operation object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_operation_from_api_t`is a subtype of the`dbms_cloud_oci_dataintegration_operation_t`type.

Fields

Field Description

`key`

(optional) The operation key, used to identiying this metadata object within the dataflow.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`shape`

(optional)

`name`

(required) The operation name. This value is unique.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`resource_name`

(required) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.

`operation_attributes`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_FROM_PROCEDURE_T Type

The operation object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_operation_from_procedure_t`is a subtype of the`dbms_cloud_oci_dataintegration_operation_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`shape`

(optional)

`name`

(optional) The operation name.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`resource_name`

(optional) The resource name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ADWC_WRITE_ATTRIBUTE_T Type

Properties to configure writing to Oracle Autonomous Data Warehouse Cloud.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_adwc_write_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`bucket_name`

(optional) The bucket name for the attribute.

`staging_file_name`

(optional) The file name for the attribute.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ADWC_WRITE_ATTRIBUTES_T Type

Properties to configure when writing to Oracle Autonomous Data Warehouse Cloud.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_adwc_write_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`bucket_schema`

(optional)

`staging_file_name`

(optional) The file name for the attribute.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ATP_WRITE_ATTRIBUTE_T Type

Properties to configure writing to Oracle Autonomous Transaction Processing.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_atp_write_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`bucket_name`

(optional) The bucket name for the attribute.

`staging_file_name`

(optional) The file name for the attribute.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ATP_WRITE_ATTRIBUTES_T Type

Properties to configure when writing to Oracle Autonomous Data Warehouse Cloud.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_atp_write_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`bucket_schema`

(optional)

`staging_file_name`

(optional) The file name for the attribute.

`staging_data_asset`

(optional)

`staging_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_READ_ATTRIBUTE_T Type

The Oracle read attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_read_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_read_attribute_t`type.

Fields

Field Description

`fetch_size`

(optional) The fetch size for reading.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_READ_ATTRIBUTES_T Type

Properties to configure reading from an Oracle Database.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_read_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_read_attribute_t`type.

Fields

Field Description

`fetch_size`

(optional) The fetch size for reading.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_WRITE_ATTRIBUTE_T Type

The Oracle write attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_write_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`batch_size`

(optional) The batch size for writing.

`is_truncate`

(optional) Specifies whether to truncate.

`isolation_level`

(optional) Specifies the isolation level.

### DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_WRITE_ATTRIBUTES_T Type

Properties to configure when writing to an Oracle Database.

Syntax
```

```

`dbms_cloud_oci_dataintegration_oracle_write_attributes_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_write_attribute_t`type.

Fields

Field Description

`batch_size`

(optional) The batch size for writing.

`is_truncate`

(optional) Specifies whether to truncate.

`isolation_level`

(optional) Specifies the isolation level.

### DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_FIELD_T Type

Output fields of an operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_output_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PARQUET_FORMAT_ATTRIBUTE_T Type

The PARQUET format attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_parquet_format_attribute_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_format_attribute_t`type.

Fields

Field Description

`compression`

(optional) The compression for the file.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_T Type

The patch object contains the audit summary information and the definition of the patch.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`time_patched`

(optional) The date and time the patch was applied, in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`error_messages`

(optional) The errors encountered while applying the patch, if any.

`application_version`

(optional) The application version of the patch.

`patch_type`

(optional) The type of the patch applied or being applied on the application.

Allowed values are: 'PUBLISH', 'REFRESH', 'UNPUBLISH'

`patch_status`

(optional) Status of the patch applied or being applied on the application

Allowed values are: 'QUEUED', 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS'

`dependent_object_metadata`

(optional) List of dependent objects in this patch.

`patch_object_metadata`

(optional) List of objects that are published or unpublished in this patch.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_T Type

This is the patch report summary information.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`name_path`

(optional) The fully qualified path of the published object, which would include its project and folder.

`l_type`

(optional) The type of the object in patch.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`object_version`

(optional) The object version.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`action`

(optional) The patch action indicating if object was created, updated, or deleted.

Allowed values are: 'CREATED', 'DELETED', 'UPDATED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_patch_change_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_COLLECTION_T Type

This is the collection of patch report summaries,. It may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of patch summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_T Type

The patch summary type contains the audit summary information and the definition of the patch.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`time_patched`

(optional) The date and time the patch was applied, in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`error_messages`

(optional) The errors encountered while applying the patch, if any.

`application_version`

(optional) The application version of the patch.

`patch_type`

(optional) The type of the patch applied or being applied on the application.

Allowed values are: 'PUBLISH', 'REFRESH', 'UNPUBLISH'

`patch_status`

(optional) Status of the patch applied or being applied on the application

Allowed values are: 'QUEUED', 'SUCCESSFUL', 'FAILED', 'IN_PROGRESS'

`dependent_object_metadata`

(optional) List of dependent objects in this patch.

`patch_object_metadata`

(optional) List of objects that are published or unpublished in this patch.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_patch_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_COLLECTION_T Type

This is the collection of patch summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of patch summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_T Type

The pipeline summary type contains the audit summary information and the definition of the pipeline.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`model_type`

(optional) The type of the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) A list of nodes attached to the pipeline.

`parameters`

(optional) A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.

`flow_config_values`

(optional)

`variables`

(optional) The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_pipeline_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_COLLECTION_T Type

This is the collection of pipeline summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of pipeline summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_T Type

The information about a pipeline validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the pipeline object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_T Type

The information about a pipeline validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the pipeline object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_pipeline_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_COLLECTION_T Type

A list of pipeline validation summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of validation summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_KEYS_T Type

The type representing the pivot key and pivot value details.

Syntax
```

```

Fields

Field Description

`pivot_axis`

(optional) The pivot axis is the point around which the table will be rotated, and the pivot values will be transposed into columns in the output table.

`pivot_key_value_map`

(optional) Map of alias to pivot key values.

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_T Type

Pivot operator has one input and one output. Pivot operator takes group by columns, a pivot key with values and aggregations. Output is the pivoted table.

Syntax
```

```

`dbms_cloud_oci_dataintegration_pivot_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`group_by_columns`

(optional)

`materialized_group_by_columns`

(optional)

`pivot_keys`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_FIELD_T Type

The type representing the pivot field. Pivot fields have an expression to define a macro and a pattern to generate the column name

Syntax
```

```

`dbms_cloud_oci_dataintegration_pivot_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`expr`

(optional)

`use_type`

(optional)

`l_type`

(optional)

`column_name_pattern`

(optional) column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PRIMARY_KEY_T Type

The primary key object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_primary_key_t`is a subtype of the`dbms_cloud_oci_dataintegration_unique_key_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_T Type

The project type contains the audit summary information and the definition of the project.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify project.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the project.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_DETAILS_T Type

The details including name and description for the project, which is a container of folders, tasks, and dataflows.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify project.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the project.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_T Type

The project summary type contains the audit summary information and the definition of the project.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify project.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the project.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_project_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_COLLECTION_T Type

A collection of project summaries. The collection can be lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of project summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_T Type

The information about the projection object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_projection_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PROXY_FIELD_T Type

A proxy field.

Syntax
```

```

`dbms_cloud_oci_dataintegration_proxy_field_t`is a subtype of the`dbms_cloud_oci_dataintegration_typed_object_t`type.

Fields

Field Description

`scope`

(optional) Deprecated - Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`scope_reference`

(optional)

`l_type`

(optional)

`labels`

(optional) Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_T Type

The information about the published object.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the published object.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_DATA_LOADER_TASK_T Type

The data loader task published object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`data_flow`

(optional)

`conditional_composite_field_map`

(optional)

`is_single_load`

(optional) If true, defines a singular load.

`parallel_load_limit`

(optional) If not a singular load, this defines the number of entities being loaded in parallel at a time for a Data Loader task.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_INTEGRATION_TASK_T Type

The integration task published object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_PIPELINE_TASK_T Type

The pipeline task published object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_from_pipeline_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_T Type

The published obect summary.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the published object.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_PIPELINE_TASK_SUMMARY_T Type

The pipeline task published object summary.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_from_pipeline_task_summary_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_summary_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_published_object_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_COLLECTION_T Type

This is the collection of published object summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of published object summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_FROM_DATA_LOADER_TASK_T Type

The data loader task published object summary.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_summary_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_summary_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_FROM_INTEGRATION_TASK_T Type

The integration task published object summary.

Syntax
```

```

`dbms_cloud_oci_dataintegration_published_object_summary_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_published_object_summary_t`type.

Fields

Field Description

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_QUERY_T Type

A query object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_query_t`is a subtype of the`dbms_cloud_oci_dataintegration_push_down_operation_t`type.

Fields

Field Description

`query`

(optional) A query string.

### DBMS_CLOUD_OCI_DATAINTEGRATION_PUSH_DOWN_OPERATION_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_push_down_operation_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_READ_OPERATION_CONFIG_T Type

The information about the read operation.

Syntax
```

```

`dbms_cloud_oci_dataintegration_read_operation_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_data_operation_config_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`operations`

(optional) An array of operations.

`data_format`

(optional)

`partition_config`

(optional)

`read_attribute`

(optional)

`incremental_read_config`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_child_reference_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_T Type

Reference contains application configuration information.

Syntax
```

```

Fields

Field Description

`key`

(optional) The reference's key, key of the object that is being used by a published object or its dependents.

`name`

(optional) The name of reference object.

`identifier`

(optional) The identifier of reference object.

`identifier_path`

(optional) The identifier path of reference object.

`description`

(optional) The description of reference object.

`l_type`

(optional) The type of reference object.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'SCHEMA', 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'PIPELINE_TASK', 'REST_TASK'

`target_object`

(optional) The new reference object to use instead of the original reference. For example, this can be a data asset reference.

`application_key`

(optional) The application key of the reference object.

`used_by`

(optional) List of published objects where this is used.

`child_references`

(optional) List of references that are dependent on this reference.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_T Type

This is the reference summary information.

Syntax
```

```

Fields

Field Description

`key`

(optional) The reference's key, key of the object that is being used by a published object or its dependents.

`name`

(optional) The name of reference object.

`identifier`

(optional) The identifier of reference object.

`identifier_path`

(optional) The identifier path of reference object.

`description`

(optional) The description of reference object.

`l_type`

(optional) The type of reference object.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'SCHEMA', 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'PIPELINE_TASK', 'REST_TASK'

`target_object`

(optional) The target object referenced. References are made to data assets and child references are made to connections. The type defining this reference is mentioned in the property type.

`aggregator_key`

(optional) The aggregator of reference object.

`used_by`

(optional) List of published objects where this is used.

`child_references`

(optional) List of references that are dependent on this reference.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_reference_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_COLLECTION_T Type

This is the collection of references.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of application summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_FROM_API_T Type

The input procedure object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_referenced_data_object_from_api_t`is a subtype of the`dbms_cloud_oci_dataintegration_referenced_data_object_t`type.

Fields

Field Description

`key`

(optional) The object key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_FROM_PROCEDURE_T Type

The input procedure object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_referenced_data_object_from_procedure_t`is a subtype of the`dbms_cloud_oci_dataintegration_referenced_data_object_t`type.

Fields

Field Description

`key`

(optional) The object key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RENAME_RULE_T Type

Lets you rename an attribute.

Syntax
```

```

`dbms_cloud_oci_dataintegration_rename_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`from_name`

(optional) The attribute name that needs to be renamed.

`to_name`

(optional) The new attribute name.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RESOURCE_PRINCIPAL_AUTH_CONFIG_T Type

Authentication configuration that uses OCI Resource Principal Auth for Generic REST invocation.

Syntax
```

```

`dbms_cloud_oci_dataintegration_resource_principal_auth_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_auth_config_t`type.

Fields

Field Description

`resource_principal_source`

(optional) The OCI resource type that will supply the authentication token

Allowed values are: 'WORKSPACE', 'APPLICATION'

### DBMS_CLOUD_OCI_DATAINTEGRATION_REST_CALL_CONFIG_T Type

The REST API configuration.

Syntax
```

```

Fields

Field Description

`method_type`

(optional) The REST method to use.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`request_headers`

(optional) The headers for the REST call.

`config_values`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_BASED_ENTITY_MAP_T Type

A map of rule patterns.

Syntax
```

```

`dbms_cloud_oci_dataintegration_rule_based_entity_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`map_type`

(optional) mapType

Allowed values are: 'MAPBYNAME', 'MAPBYPATTERN'

`from_pattern`

(optional) The pattern to map from.

`to_pattern`

(optional) The pattern to map to.

`is_java_regex_syntax`

(optional) Specifies whether the rule uses a java regex syntax.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_TYPE_CONFIG_T Type

The rule type config.

Syntax
```

```

`dbms_cloud_oci_dataintegration_rule_type_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_dynamic_type_handler_t`type.

Fields

Field Description

`key`

(optional) The key of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`scope`

(optional) Deprecated - Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a `TypedObject` or a full `TypedObject` definition.

`scope_reference`

(optional)

`is_order_by_rule`

(optional) Specifies whether it is ordered by rule.

`projection_rules`

(optional) The projection rules.

`config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_BASED_FIELD_MAP_T Type

A map of rule patterns.

Syntax
```

```

`dbms_cloud_oci_dataintegration_rule_based_field_map_t`is a subtype of the`dbms_cloud_oci_dataintegration_field_map_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`config_values`

(optional)

`map_type`

(optional) mapType

Allowed values are: 'MAPBYNAME', 'MAPBYPOSITION', 'MAPBYPATTERN'

`from_pattern`

(optional) The pattern to map from.

`to_pattern`

(optional) The pattern to map to.

`is_java_regex_syntax`

(optional) Specifies whether the rule uses a java regex syntax.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`from_rule_config`

(optional)

`to_rule_config`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_T Type

Runtime operator model which holds the runtime metadata of the task operator executed.

Syntax
```

```

Fields

Field Description

`key`

(optional) The RuntimeOperator key.

`task_run_key`

(optional) The TaskRun key.

`start_time_in_millis`

(optional) The runtime operator start time.

`end_time_in_millis`

(optional) The runtime operator end time.

`status`

(optional) Status of RuntimeOperator. This field is deprecated, use RuntimeOperator's executionState field instead.

Allowed values are: 'NOT_STARTED', 'QUEUED', 'RUNNING', 'TERMINATING', 'TERMINATED', 'SUCCESS', 'ERROR'

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`execution_state`

(optional) status

Allowed values are: 'NOT_STARTED', 'RUNNING', 'TERMINATED', 'SUCCESS', 'ERROR', 'SKIPPED', 'UNKNOWN', 'IGNORED'

`parameters`

(optional) A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`operator`

(optional)

`inputs`

(optional) The configuration provider bindings.

`outputs`

(optional) The configuration provider bindings.

`task_type`

(optional) The type of task run.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`config_provider`

(optional)

`operator_type`

(optional) The type of Runtime Operator

Allowed values are: 'BASH_OPERATOR', 'TASK_OPERATOR', 'REST_OPERATOR', 'START_OPERATOR', 'END_OPERATOR', 'EXPRESSION_OPERATOR', 'MERGE_OPERATOR', 'DECISION_OPERATOR', 'LOOP_OPERATOR', 'ACTUAL_END_OPERATOR'

`metrics`

(optional) A map metrics for the task run.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_T Type

The information about RuntimeOperator.

Syntax
```

```

Fields

Field Description

`key`

(optional) The RuntimeOperator key.

`task_run_key`

(optional) The TaskRun key.

`start_time_in_millis`

(optional) The runtime operator start time.

`end_time_in_millis`

(optional) The runtime operator end time.

`status`

(optional) Status of RuntimeOperator. This field is deprecated, use RuntimeOperator's executionState field instead.

Allowed values are: 'NOT_STARTED', 'QUEUED', 'RUNNING', 'TERMINATING', 'TERMINATED', 'SUCCESS', 'ERROR'

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`execution_state`

(optional) status

Allowed values are: 'NOT_STARTED', 'RUNNING', 'TERMINATED', 'SUCCESS', 'ERROR', 'SKIPPED', 'UNKNOWN', 'IGNORED'

`parameters`

(optional) A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`operator`

(optional)

`inputs`

(optional) The configuration provider bindings.

`outputs`

(optional) The configuration provider bindings.

`task_type`

(optional) The type of task run.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`config_provider`

(optional)

`operator_type`

(optional) The type of Runtime Operator

Allowed values are: 'BASH_OPERATOR', 'TASK_OPERATOR', 'REST_OPERATOR', 'START_OPERATOR', 'END_OPERATOR', 'EXPRESSION_OPERATOR', 'MERGE_OPERATOR', 'DECISION_OPERATOR', 'LOOP_OPERATOR', 'ACTUAL_END_OPERATOR'

`metrics`

(optional) A map metrics for the task run.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_runtime_operator_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_COLLECTION_T Type

List of runtimeOperator summaries

Syntax
```

```

Fields

Field Description

`items`

(required) The array of runtimeOperator summaries

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_runtime_operator_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_T Type

Runtime pipeline model which holds the runtime metadata of the task executed.

Syntax
```

```

Fields

Field Description

`pipeline`

(optional)

`runtime_operators`

(optional) A list of RuntimeOperators attached to the RuntimePipeline.

`parent_runtime_operator_key`

(optional) The parent RuntimePipeline's RuntimeOperator key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_T Type

The information about RuntimePipeline.

Syntax
```

```

Fields

Field Description

`pipeline`

(optional)

`runtime_operators`

(optional) A list of RuntimeOperators attached to the RuntimePipeline.

`parent_runtime_operator_key`

(optional) The parent RuntimePipeline's RuntimeOperator key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_runtime_pipeline_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_COLLECTION_T Type

List of runtimePipeline summaries

Syntax
```

```

Fields

Field Description

`items`

(required) The array of runtimePipeline summaries

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_T Type

The schedule summary information.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`frequency_details`

(optional)

`timezone`

(optional) The timezone for the schedule.

`is_daylight_adjustment_enabled`

(optional) A flag to indicate whether daylight adjustment should be considered or not.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_COLLECTION_T Type

A collection of schedule summaries. The collection can be lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Schedule summaries

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_DRIFT_CONFIG_T Type

The configuration for handling schema drift in a Source or Target operator.

Syntax
```

```

Fields

Field Description

`extra_column_handling`

(optional) The setting for how to handle extra columns/fields. NULL_FILLUP means that nulls will be loaded into the target for extra columns.

Allowed values are: 'ALLOW', 'NULL_FILLUP', 'DO_NOT_ALLOW'

`missing_column_handling`

(optional) The setting for how to handle missing columns/fields. NULL_SELECT means that null values will be selected from the source for missing columns.

Allowed values are: 'ALLOW', 'NULL_SELECT', 'DO_NOT_ALLOW'

`data_type_change_handling`

(optional) The setting for how to handle columns/fields with changed data types.

Allowed values are: 'ALLOW', 'DO_CAST_IF_POSSIBLE', 'DO_NOT_ALLOW'

`is_validation_warning_if_allowed`

(optional) If true, display a validation warning for schema changes, even if they are allowed.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_T Type

The schema summary object.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object's type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`resource_name`

(optional) A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.

`description`

(optional) User-defined description for the schema.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`external_key`

(optional) The external key for the object.

`is_has_containers`

(optional) Specifies whether the schema has containers.

`default_connection`

(optional) The default connection key.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_schema_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_COLLECTION_T Type

This is the collection of schema summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of schema summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_FIELD_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_shape_field_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_SELECT_T Type

The information about the select object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_select_t`is a subtype of the`dbms_cloud_oci_dataintegration_push_down_operation_t`type.

Fields

Field Description

`is_distinct`

(optional) Specifies whether the object is distinct.

`select_columns`

(optional) An array of selected columns.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_CLAUSE_T Type

The information about the sort object.

Syntax
```

```

Fields

Field Description

`field`

(optional)

`l_order`

(optional) The sort order.

Allowed values are: 'ASC', 'DESC'

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_CLAUSE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_sort_clause_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_T Type

The information about the sort object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_sort_t`is a subtype of the`dbms_cloud_oci_dataintegration_push_down_operation_t`type.

Fields

Field Description

`sort_clauses`

(optional) The sort clause.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_RULE_T Type

A rule to define the set of fields to sort by, and whether to sort by ascending or descending values.

Syntax
```

```

Fields

Field Description

`wrapped_rule`

(optional)

`is_ascending`

(optional) Specifies if the sort key has ascending order.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_RULE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_sort_key_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_T Type

Sort key contains a set of sort key rules defining sorting algorithm.

Syntax
```

```

Fields

Field Description

`sort_rules`

(optional) The list of sort key rules.

### DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_OPER_T Type

The information about the sort operator.

Syntax
```

```

`dbms_cloud_oci_dataintegration_sort_oper_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`sort_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SOURCE_T Type

The information about the source object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_source_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`entity`

(optional)

`is_read_access`

(optional) Specifies the read access.

`is_copy_fields`

(optional) Specifies the copy fields.

`is_predefined_shape`

(optional) Specifies if this uses a predefined shape.

`schema_drift_config`

(optional)

`fixed_data_shape`

(optional)

`read_operation_config`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_SPLIT_T Type

The information about the split operator. Split operator has one input and many output links. Split operator allows users to take one data set and based on conditions produce many different outputs.

Syntax
```

```

`dbms_cloud_oci_dataintegration_split_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`data_routing_strategy`

(optional) Specify how to handle data that matches a split condition. Either data that matches the first condition should be removed from further processing by other conditions, or all matched data should be evaluated for all conditions.

Allowed values are: 'FIRST', 'ALL'

### DBMS_CLOUD_OCI_DATAINTEGRATION_START_OPERATOR_T Type

Represents the start of a pipeline.

Syntax
```

```

`dbms_cloud_oci_dataintegration_start_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_STRUCTURED_TYPE_T Type

A `StructuredType` object represents a data type that exists in a physical data asset object such as a table column, but is more complex. For example, an Oracle database `OBJECT` type. It can be composed of multiple `DataType` objects.

Syntax
```

```

Fields

Field Description

`schema`

(optional)

`dt_type`

(optional) The data type.

Allowed values are: 'PRIMITIVE', 'STRUCTURED'

`type_system_name`

(optional) The data type system name.

`config_definition`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_WRITE_OPERATION_CONFIG_T Type

The information about the write operation.

Syntax
```

```

`dbms_cloud_oci_dataintegration_write_operation_config_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_data_operation_config_t`type.

Fields

Field Description

`key`

(optional) The object key.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`operations`

(optional) An array of operations.

`data_format`

(optional)

`partition_config`

(optional)

`write_attribute`

(optional)

`write_mode`

(optional) The mode for the write operation.

Allowed values are: 'OVERWRITE', 'APPEND', 'MERGE', 'IGNORE'

`merge_key`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TARGET_T Type

The information about the target operator. The target operator lets you specify the data entity to store the transformed data.

Syntax
```

```

`dbms_cloud_oci_dataintegration_target_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`entity`

(optional)

`is_read_access`

(optional) Specifies the read access.

`is_copy_fields`

(optional) Specifies the copy fields.

`is_predefined_shape`

(optional) Specifies if this uses a predefined shape.

`is_use_same_source_name`

(optional) Specifies if entity name is the same as source.

`target_entity_name_prefix`

(optional) Prefix for the entity Name.

`target_entity_name_suffix`

(optional) Suffix for the entity Name.

`data_property`

(optional) Specifies the data property.

Allowed values are: 'TRUNCATE', 'MERGE', 'BACKUP', 'OVERWRITE', 'APPEND', 'IGNORE'

`schema_drift_config`

(optional)

`fixed_data_shape`

(optional)

`write_operation_config`

(optional)

`load_order`

(optional) A numeric loading order number for the target.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_T Type

The task type contains the audit summary information and the definition of the task.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of the task.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_DATA_LOADER_TASK_DETAILS_T Type

The information about a data flow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_data_loader_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`data_flow`

(optional)

`conditional_composite_field_map`

(optional)

`is_single_load`

(optional) Defines whether Data Loader task is used for single load or multiple

`parallel_load_limit`

(optional) Defines the number of entities being loaded in parallel at a time for a Data Loader task

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_INTEGRATION_TASK_DETAILS_T Type

The information about the integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_integration_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_OCI_DATAFLOW_TASK_DETAILS_T Type

The information about the OCI Dataflow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_oci_dataflow_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`dataflow_application`

(optional)

`driver_shape_details`

(optional)

`executor_shape_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_PIPELINE_TASK_DETAILS_T Type

The information about the pipeline task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_pipeline_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_REST_TASK_DETAILS_T Type

The information about the Generic REST task. The endpoint and cancelEndpoint properties are deprecated, use the properties executeRestCallConfig, cancelRestCallConfig and pollRestCallConfig for execute, cancel and polling of the calls.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_rest_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`auth_details`

(optional)

`auth_config`

(optional)

`endpoint`

(optional)

`method_type`

(optional) The REST method to use. This property is deprecated, use ExecuteRestCallConfig's methodType property instead.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`headers`

(optional) The headers for the REST call. This property is deprecated, use ExecuteRestCallConfig's headers property instead.

`json_data`

(optional) JSON data for payload body. This property is deprecated, use ExecuteRestCallConfig's payload config param instead.

`api_call_mode`

(optional) The REST invocation pattern to use. ASYNC_OCI_WORKREQUEST is being deprecated as well as cancelEndpoint/MethodType.

Allowed values are: 'SYNCHRONOUS', 'ASYNC_OCI_WORKREQUEST', 'ASYNC_GENERIC'

`cancel_endpoint`

(optional)

`cancel_method_type`

(optional) The REST method to use for canceling the original request.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`execute_rest_call_config`

(optional)

`cancel_rest_call_config`

(optional)

`poll_rest_call_config`

(optional)

`typed_expressions`

(optional) List of typed expressions.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_SQL_TASK_DETAILS_T Type

The information about the SQL task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_from_sql_task_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_t`type.

Fields

Field Description

`script`

(optional)

`sql_script_type`

(optional) Indicates whether the task is invoking a custom SQL script or stored procedure.

Allowed values are: 'STORED_PROCEDURE', 'SQL_CODE'

`operation`

(optional) Describes the shape of the execution result

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_OPERATOR_T Type

An operator for task

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_operator_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`retry_attempts`

(optional) The number of retry attempts.

`retry_delay_unit`

(optional) The unit for the retry delay.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`retry_delay`

(optional) The retry delay, the unit for measurement is in the property retry delay unit.

`expected_duration`

(optional) The expected duration for the task run.

`expected_duration_unit`

(optional) The expected duration unit of measure.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`task_type`

(optional) The type of the task referenced in the task property.

Allowed values are: 'PIPELINE_TASK', 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`task`

(optional)

`trigger_rule`

(optional) The merge condition. The conditions are ALL_SUCCESS - All the preceeding operators need to be successful. ALL_FAILED - All the preceeding operators should have failed. ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

Allowed values are: 'ALL_SUCCESS', 'ALL_FAILED', 'ALL_COMPLETE'

`config_provider_delegate`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_T Type

A model that holds Schedule and other information required for scheduling a task.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`schedule_ref`

(optional)

`config_provider_delegate`

(optional)

`is_enabled`

(optional) Whether the schedule is enabled.

`retry_attempts`

(optional) The number of retry attempts.

`retry_delay_unit`

(optional) The unit for the retry delay.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`retry_delay`

(optional) The retry delay, the unit for measurement is in the property retry delay unit.

`start_time_millis`

(optional) The start time in milliseconds.

`end_time_millis`

(optional) The end time in milliseconds.

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`is_backfill_enabled`

(optional) Whether the backfill is enabled

`auth_mode`

(optional) The authorization mode for the task.

Allowed values are: 'OBO', 'RESOURCE_PRINCIPAL', 'USER_CERTIFICATE'

`expected_duration`

(optional) The expected duration of the task execution.

`expected_duration_unit`

(optional) The expected duration unit of the task execution.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`last_run_details`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_T Type

The information about a task run.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`config_provider`

(optional)

`status`

(optional) The status of the task run.

Allowed values are: 'NOT_STARTED', 'QUEUED', 'RUNNING', 'TERMINATING', 'TERMINATED', 'SUCCESS', 'ERROR'

`start_time_millis`

(optional) The start time.

`end_time_millis`

(optional) The end time.

`last_updated`

(optional) The date and time the object was last updated.

`records_written`

(optional) The number of records processed in the task run.

`bytes_processed`

(optional) The number of bytes processed in the task run.

`error_message`

(optional) Contains an error message if status is `ERROR`.

`expected_duration`

(optional) The expected duration for the task run.

`expected_duration_unit`

(optional) The expected duration unit of measure.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`task_key`

(optional) Task Key of the task for which TaskRun is being created. If not specified, the AggregatorKey in RegistryMetadata will be assumed to be the TaskKey

`external_id`

(optional) The external identifier for the task run.

`retry_attempt`

(optional) Holds the particular attempt number.

`task_schedule`

(optional)

`metrics`

(optional) A map of metrics for the run.

`outputs`

(optional) A map of the outputs of the run.

`execution_errors`

(optional) An array of execution errors from the run.

`termination_errors`

(optional) An array of termination errors from the run.

`auth_mode`

(optional) The autorization mode for when the task was executed.

Allowed values are: 'OBO', 'RESOURCE_PRINCIPAL', 'USER_CERTIFICATE'

`opc_request_id`

(optional) The OPC request ID of execution of the task run.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`task_type`

(optional) The type of task run.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`is_log_processing_in_progress`

(optional) This field tells the user if there is any logs being fetched in backend for failure. Applicable only for failed pipeline tasks.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_DETAILS_T Type

The task run object provides information on the execution of a task.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`status`

(optional) status

Allowed values are: 'NOT_STARTED', 'QUEUED', 'RUNNING', 'TERMINATING', 'TERMINATED', 'SUCCESS', 'ERROR'

`start_time_millis`

(optional) The task run start time.

`end_time_millis`

(optional) The task run end time.

`last_updated`

(optional) The date and time the task run was last updated.

`records_written`

(optional) Number of records processed in task run.

`bytes_processed`

(optional) Number of bytes processed in task run.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`task_type`

(optional) The type of the task for the run.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`ref_task_run_id`

(optional) Reference Task Run Id to be used for re-run

`re_run_type`

(optional) Supported re-run types

Allowed values are: 'BEGINNING', 'FAILED', 'STEP'

`step_id`

(optional) Step Id for running from a certain step.

`inputs`

(optional) A map of the configuration provider input bindings of the run.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_DETAILS_T Type

The task lineage object provides information on the lineage information of a task after execution.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`task_name`

(optional) Task name

`task_type`

(optional) Task name

`task_key`

(optional) The object key.

`is_lineage_gen_completed`

(optional) This value is used to track if lineage generation for a task is completed or not.

`task_execution_status`

(optional) The status of the task run.

Allowed values are: 'SUCCESS', 'ERROR', 'TERMINATED'

`flow`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_T Type

The information about TaskRunLineage.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`task_name`

(optional) Task name

`task_type`

(optional) Task name

`task_key`

(optional) The object key.

`is_lineage_gen_completed`

(optional) This value is used to track if lineage generation for a task is completed or not.

`task_execution_status`

(optional) The status of the task run.

Allowed values are: 'SUCCESS', 'ERROR', 'TERMINATED'

`flow`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_task_run_lineage_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_COLLECTION_T Type

List of lineage flows

Syntax
```

```

Fields

Field Description

`items`

(required) The array of lineage flow summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LOG_SUMMARY_T Type

A log message from the execution of a task.

Syntax
```

```

Fields

Field Description

`message`

(optional) A user-friendly log message.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_T Type

The information about a task run.

Syntax
```

```

Fields

Field Description

`key`

(optional) The object key.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`status`

(optional) status

Allowed values are: 'NOT_STARTED', 'QUEUED', 'RUNNING', 'TERMINATING', 'TERMINATED', 'SUCCESS', 'ERROR'

`start_time_millis`

(optional) The task run start time.

`end_time_millis`

(optional) The task run end time.

`last_updated`

(optional) The date and time the task run was last updated.

`records_written`

(optional) Number of records processed in task run.

`bytes_processed`

(optional) Number of bytes processed in task run.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`task_type`

(optional) The type of the task for the run.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`ref_task_run_id`

(optional) Reference Task Run Id to be used for re-run

`re_run_type`

(optional) Supported re-run types

Allowed values are: 'BEGINNING', 'FAILED', 'STEP'

`step_id`

(optional) Step Id for running from a certain step.

`inputs`

(optional) A map of the configuration provider input bindings of the run.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_task_run_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_COLLECTION_T Type

A list of task run summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of task run summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_T Type

The tsk schedule summary information.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`schedule_ref`

(optional)

`config_provider_delegate`

(optional)

`is_enabled`

(optional) Whether the task schedule is enabled.

`number_of_retries`

(optional) The number of retries.

`retry_delay`

(optional) The retry delay, the unit for measurement is in the property retry delay unit.

`retry_delay_unit`

(optional) The unit for the retry delay.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`start_time_millis`

(optional) The start time in milliseconds.

`end_time_millis`

(optional) The end time in milliseconds.

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`is_backfill_enabled`

(optional) Whether the backfill is enabled.

`auth_mode`

(optional) The authorization mode for the task.

Allowed values are: 'OBO', 'RESOURCE_PRINCIPAL', 'USER_CERTIFICATE'

`expected_duration`

(optional) The expected duration of the task execution.

`expected_duration_unit`

(optional) The expected duration unit of the task execution.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`next_run_time_millis`

(optional) The time for next run in milliseconds.

`last_run_details`

(optional)

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_task_schedule_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_COLLECTION_T Type

A collection of TaskSchedule summaries. The collection can be lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of TaskSchedule summaries

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_T Type

The task summary object type contains the audit summary information and the definition of the task summary object.

Syntax
```

```

Fields

Field Description

`model_type`

(optional) The type of task.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(optional) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_task_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_COLLECTION_T Type

This is the collection of task summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of task summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_DATA_LOADER_TASK_T Type

The information about a data flow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`data_flow`

(optional)

`conditional_composite_field_map`

(optional)

`is_single_load`

(optional) Defines whether Data Loader task is used for single load or multiple

`parallel_load_limit`

(optional) Defines the number of entities being loaded in parallel at a time for a Data Loader task

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_INTEGRATION_TASK_T Type

The information about the integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_OCI_DATAFLOW_TASK_T Type

The information about the OCI Dataflow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_oci_dataflow_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`dataflow_application`

(optional)

`driver_shape_details`

(optional)

`executor_shape_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_PIPELINE_TASK_T Type

The information about the pipeline task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_pipeline_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_REST_TASK_T Type

The information about the Generic REST task. The endpoint and cancelEndpoint properties are deprecated, use the properties executeRestCallConfig, cancelRestCallConfig and pollRestCallConfig for execute, cancel and polling of the calls.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_rest_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`auth_details`

(optional)

`auth_config`

(optional)

`endpoint`

(optional)

`method_type`

(optional) The REST method to use. This property is deprecated, use ExecuteRestCallConfig's methodType property instead.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`headers`

(optional) Headers for payload.

`json_data`

(optional) JSON data for payload body. This property is deprecated, use ExecuteRestCallConfig's payload config param instead.

`api_call_mode`

(optional) The REST invocation pattern to use. ASYNC_OCI_WORKREQUEST is being deprecated as well as cancelEndpoint/MethodType.

Allowed values are: 'SYNCHRONOUS', 'ASYNC_OCI_WORKREQUEST', 'ASYNC_GENERIC'

`cancel_endpoint`

(optional)

`cancel_method_type`

(optional) The REST method to use for canceling the original request.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`execute_rest_call_config`

(optional)

`cancel_rest_call_config`

(optional)

`poll_rest_call_config`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_SQL_TASK_T Type

The information about the SQL task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_task_summary_from_sql_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_task_summary_t`type.

Fields

Field Description

`script`

(optional)

`sql_script_type`

(optional) Indicates whether the task is invoking a custom SQL script or stored procedure.

Allowed values are: 'STORED_PROCEDURE', 'SQL_CODE'

`operation`

(optional) Describes the shape of the execution result

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_T Type

The information about task validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) Total number of validation messages.

`error_message_count`

(optional) Total number of validation error messages.

`warn_message_count`

(optional) Total number of validation warning messages.

`info_message_count`

(optional) Total number of validation information messages.

`validation_messages`

(optional) Detailed information of the data flow object validation.

`key`

(optional) Objects use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_T Type

The information about task validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) Total number of validation messages.

`error_message_count`

(optional) Total number of validation error messages.

`warn_message_count`

(optional) Total number of validation warning messages.

`info_message_count`

(optional) Total number of validation information messages.

`validation_messages`

(optional) Detailed information of the data flow object validation.

`key`

(optional) Objects use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_task_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_COLLECTION_T Type

A list of task validation summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of validation summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_T Type

Template application.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_T Type

The application template summary type contains the audit summary information and the definition of the application template.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify application.

`model_type`

(optional) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) The application's version.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`dependent_object_metadata`

(optional) A list of dependent objects in this patch.

`published_object_metadata`

(optional) A list of objects that are published or unpublished in this patch.

`source_application_info`

(optional)

`time_patched`

(optional) The date and time the application was patched, in the timestamp format defined by RFC3339.

`id`

(optional) OCID of the resource that is used to uniquely identify the application

`compartment_id`

(optional) OCID of the compartment that this resource belongs to. Defaults to compartment of the Workspace.

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`time_created`

(optional) The date and time the application was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the application was updated, in the timestamp format defined by RFC3339. example: 2019-08-25T21:10:29.41Z

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_template_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_COLLECTION_T Type

This is the collection of application template summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of application template summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_ELEMENT_T_TBL Type

Nested table type of json_element_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_LIST_RULE_T Type

The type list rule that defines how fields are projected.

Syntax
```

```

`dbms_cloud_oci_dataintegration_type_list_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`scope`

(optional) Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`is_cascade`

(optional) Specifies whether to cascade or not.

`matching_strategy`

(optional) The pattern matching strategy.

Allowed values are: 'NAME_OR_TAGS', 'TAGS_ONLY', 'NAME_ONLY'

`is_case_sensitive`

(optional) Specifies if the rule is case sensitive.

`rule_type`

(optional) The rule type.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`types`

(optional) An arry of types.

### DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_NAME_PATTERN_RULE_T Type

The typed name rule for field projection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_typed_name_pattern_rule_t`is a subtype of the`dbms_cloud_oci_dataintegration_projection_rule_t`type.

Fields

Field Description

`types`

(optional) An array of types.

`is_skip_remaining_rules_on_match`

(optional) Specifies whether to skip remaining rules when a match is found.

`scope`

(optional) Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.

`is_cascade`

(optional) Specifies whether to cascade or not.

`matching_strategy`

(optional) The pattern matching strategy.

Allowed values are: 'NAME_OR_TAGS', 'TAGS_ONLY', 'NAME_ONLY'

`is_case_sensitive`

(optional) Specifies if the rule is case sensitive.

`rule_type`

(optional) The rule type.

Allowed values are: 'INCLUDE', 'EXCLUDE'

`pattern`

(optional) The rule pattern.

`names`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UNION_T Type

The information about a union object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_union_t`is a subtype of the`dbms_cloud_oci_dataintegration_operator_t`type.

Fields

Field Description

`union_type`

(optional) unionType

Allowed values are: 'NAME', 'POSITION'

`is_all`

(optional) The information about the union all.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_DATA_KEY_T Type

The unique key object.

Syntax
```

```

`dbms_cloud_oci_dataintegration_unique_data_key_t`is a subtype of the`dbms_cloud_oci_dataintegration_unique_key_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_APPLICATION_DETAILS_T Type

Properties used in application create operations.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify application.

`model_type`

(required) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) version

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_DETAILS_T Type

Properties used in connection update operations.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the connection.

Allowed values are: 'ORACLE_ADWC_CONNECTION', 'ORACLE_ATP_CONNECTION', 'ORACLE_OBJECT_STORAGE_CONNECTION', 'ORACLEDB_CONNECTION', 'MYSQL_CONNECTION', 'GENERIC_JDBC_CONNECTION', 'BICC_CONNECTION', 'AMAZON_S3_CONNECTION', 'BIP_CONNECTION', 'LAKE_CONNECTION', 'ORACLE_PEOPLESOFT_CONNECTION', 'ORACLE_EBS_CONNECTION', 'ORACLE_SIEBEL_CONNECTION', 'HDFS_CONNECTION', 'MYSQL_HEATWAVE_CONNECTION', 'REST_NO_AUTH_CONNECTION', 'REST_BASIC_AUTH_CONNECTION'

`key`

(required) Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) User-defined description for the connection.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`connection_properties`

(optional) The properties for the connection.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ADWC_T Type

The details to update an Autonomous Data Warehouse data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Data Warehouse instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_AMAZON_S3_T Type

The details to update an Amazon s3 connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`access_key`

(optional)

`secret_key`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ATP_T Type

The details to update an Autonomous Transaction Processing data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`tns_alias`

(optional) The Autonomous Transaction Processing instance service name.

`tns_names`

(optional) Array of service names that are available for selection in the tnsAlias property.

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_BICC_T Type

The details to update a FUSION_APP BICC connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_bicc_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

`default_external_storage`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_BIP_T Type

The details to update a Fusion applications BIP connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_bip_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_HDFS_T Type

The details to update the HDFS data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`hdfs_principal`

(required) The HDFS principal.

`data_node_principal`

(required) The HDFS Data Node principal.

`name_node_principal`

(required) The HDFS Name Node principal.

`realm`

(optional) HDFS Realm name.

`key_distribution_center`

(optional) The HDFS Key Distribution Center.

`key_tab_content`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_JDBC_T Type

The details to update a generic JDBC data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_LAKE_T Type

The details to update a Lake connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_MY_SQL_T Type

The details to update a MYSQL data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type

The details to update a MYSQL HeatWave data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_OBJECT_STORAGE_T Type

The details to update an Oracle Object Storage data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`credential_file_content`

(optional) The credential file content from an Oracle Object Storage wallet.

`user_id`

(optional) The OCI user OCID for the user to connect to.

`finger_print`

(optional) The fingerprint for the user.

`pass_phrase`

(optional) The passphrase for the connection.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_T Type

The details to update an Oracle Database data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The user name for the connection.

`password`

(optional) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_EBS_T Type

The details to update E-Business Suite data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type

The details to update an Oracle PeopleSoft data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_SIEBEL_T Type

The details to update an Oracle Siebel data asset connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(required) The user name for the connection.

`password`

(required) The password for the connection.

`password_secret`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_REST_BASIC_AUTH_T Type

The details to update a basic auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_rest_basic_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

Fields

Field Description

`username`

(required) Username for the connection.

`password_secret`

(required)

`auth_header`

(optional) Optional header name if used other than default header(Authorization).

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_REST_NO_AUTH_T Type

The details to update a no auth rest connection.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_connection_from_rest_no_auth_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_connection_details_t`type.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_COPY_OBJECT_REQUEST_DETAILS_T Type

Properties used in copy object request update operations.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the object.

Allowed values are: 'TERMINATING'

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_DETAILS_T Type

Properties used in data asset update operations.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the data asset.

Allowed values are: 'ORACLE_DATA_ASSET', 'ORACLE_OBJECT_STORAGE_DATA_ASSET', 'ORACLE_ATP_DATA_ASSET', 'ORACLE_ADWC_DATA_ASSET', 'MYSQL_DATA_ASSET', 'GENERIC_JDBC_DATA_ASSET', 'FUSION_APP_DATA_ASSET', 'AMAZON_S3_DATA_ASSET', 'LAKE_DATA_ASSET', 'ORACLE_PEOPLESOFT_DATA_ASSET', 'ORACLE_SIEBEL_DATA_ASSET', 'ORACLE_EBS_DATA_ASSET', 'HDFS_DATA_ASSET', 'MYSQL_HEATWAVE_DATA_ASSET', 'REST_DATA_ASSET'

`key`

(required) Generated key that can be used in API calls to identify data asset.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) The user-defined description of the data asset.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`external_key`

(optional) The external key for the object.

`asset_properties`

(optional) Additional properties for the data asset.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ADWC_T Type

Details for the Autonomous Data Warehouse data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_adwc_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Data Warehouse instance service name.

`driver_class`

(optional) The Autonomous Data Warehouse driver class.

`credential_file_content`

(optional) The credential file content from a Autonomous Data Warehouse wallet.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`region_id`

(optional) The Autonomous Data Warehouse instance region Id.

`tenancy_id`

(optional) The Autonomous Data Warehouse instance tenancy Id.

`compartment_id`

(optional) The Autonomous Data Warehouse instance compartment Id.

`autonomous_db_id`

(optional) Tha Autonomous Database Id

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_AMAZON_S3_T Type

Details for the Amazon s3 data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_amazon_s3_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`l_region`

(optional) The region for Amazon s3

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ATP_T Type

Details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_atp_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`service_name`

(optional) The Autonomous Transaction Processing instance service name.

`driver_class`

(optional) The Autonomous Transaction Processing driver class

`credential_file_content`

(optional) The credential file content from an Autonomous Transaction Processing wallet.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`region_id`

(optional) The Autonomous Data Warehouse instance region Id.

`tenancy_id`

(optional) The Autonomous Data Warehouse instance tenancy Id.

`compartment_id`

(optional) The Autonomous Data Warehouse instance compartment Id.

`autonomous_db_id`

(optional) Tha Autonomous Database Id

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_FUSION_APP_T Type

Details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_fusion_app_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`service_url`

(optional) The service url of the BI Server.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_HDFS_T Type

Details for the HDFS data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_hdfs_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The HDFS hostname.

`port`

(required) The HDFS port.

`protocol`

(required) The HDFS Protocol name.

`validate_certificate`

(optional) Specifies whether certificate validation is needed

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_JDBC_T Type

Details for the Autonomous Transaction Processing data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_jdbc_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`data_asset_type`

(optional) The data asset type for the generic JDBC data asset.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_LAKE_T Type

Details for the Lake data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_lake_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`lake_id`

(required) The Lake Ocid.

`metastore_id`

(optional) The metastoreId for the specified Lake Resource.

`lake_proxy_endpoint`

(optional) The rangerEndpoint for the specified Lake Resource.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_MY_SQL_T Type

Details for the MYSQL data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_my_sql_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The generic JDBC host name.

`port`

(optional) The generic JDBC port number.

`service_name`

(optional) The generic JDBC service name for the database.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type

Details for the MYSQL HeatWave data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_my_sql_heat_wave_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The MySql HeatWave host name.

`port`

(required) The MySql HeatWave port number.

`service_name`

(optional) The MySql HeatWave service name for the database.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_OBJECT_STORAGE_T Type

Details for the Oracle Object storage data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_object_storage_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`oci_region`

(optional) The Oracle Object storage Region ie. us-ashburn-1

`url`

(optional) The Oracle Object storage URL.

`tenancy_id`

(optional) The OCI tenancy OCID.

`namespace`

(optional) The namespace for the specified Oracle Object storage resource. You can find the namespace under Object Storage Settings in the Console.

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_T Type

Details for the Oracle Database data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_oracle_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(optional) The Oracle Database hostname.

`port`

(optional) The Oracle Database port.

`service_name`

(optional) The Oracle Database service name.

`driver_class`

(optional) The Oracle Database driver class.

`sid`

(optional) The Oracle Database SID.

`credential_file_content`

(optional) The credential file content from a wallet for the data asset.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_EBS_T Type

Details for the E-Business Suite data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_oracle_ebs_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle EBS hostname.

`port`

(required) The Oracle EBS port.

`service_name`

(optional) The Oracle EBS service name.

`driver_class`

(optional) The Oracle EBS driver class.

`sid`

(optional) The Oracle EBS SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_T Type

Details for the Oracle PeopleSoft data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_oracle_people_soft_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle PeopleSoft hostname.

`port`

(required) The Oracle PeopleSoft port.

`service_name`

(optional) The Oracle PeopleSoft service name.

`driver_class`

(optional) The Oracle PeopleSoft driver class.

`sid`

(optional) The Oracle PeopleSoft SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_SIEBEL_T Type

Details for the Oracle Siebel data asset type.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_oracle_siebel_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`host`

(required) The Oracle Siebel hostname.

`port`

(required) The Oracle Siebel port.

`service_name`

(optional) The Oracle Siebel service name.

`driver_class`

(optional) The Oracle Siebel driver class.

`sid`

(optional) The Oracle Siebel SID.

`wallet_secret`

(optional)

`wallet_password_secret`

(optional)

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_REST_T Type

Details to update the Rest data asset.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_data_asset_from_rest_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_data_asset_details_t`type.

Fields

Field Description

`base_url`

(required) The base url of the rest server.

`manifest_file_content`

(required) The manifest file content of the rest APIs.

`default_connection`

(required)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_FLOW_DETAILS_T Type

Properties used in data flow update operations.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`nodes`

(optional) An array of nodes.

`parameters`

(optional) An array of parameters.

`description`

(optional) Detailed description for the object.

`flow_config_values`

(optional)

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DETAILED_DESCRIPTION_DETAILS_T Type

Properties used in detailed description update operations.

Syntax
```

```

Fields

Field Description

`logo`

(optional) Base64 encoded image to represent logo of the object.

`detailed_description`

(optional) Base64 encoded rich text description of the object.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DIS_APPLICATION_DETAILS_T Type

Properties used in DIS Application create operations.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify application.

`model_type`

(required) The object type.

`model_version`

(optional) The object's model version.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`application_version`

(optional) version

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`metadata`

(optional)

`display_name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_EXPORT_REQUEST_DETAILS_T Type

Properties used in export object request update operations.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the object.

Allowed values are: 'TERMINATING'

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_EXTERNAL_PUBLICATION_DETAILS_T Type

Properties used to update a published Oracle Cloud Infrastructure Data Flow object.

Syntax
```

```

Fields

Field Description

`application_id`

(optional) The unique OCID of the identifier that is returned after creating the Oracle Cloud Infrastructure Data Flow application.

`application_compartment_id`

(required) The OCID of the compartment where the application is created in the Oracle Cloud Infrastructure Data Flow Service.

`display_name`

(required) The name of the application.

`description`

(optional) The details of the data flow or the application.

`resource_configuration`

(optional)

`configuration_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_FOLDER_DETAILS_T Type

The properties used in folder update operations.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify folder.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the folder.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`parent_ref`

(optional)

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_FUNCTION_LIBRARY_DETAILS_T Type

The properties used in FunctionLibrary update operations.

Syntax
```

```

Fields

Field Description

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the FunctionLibrary.

`category_name`

(optional) The category name.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`model_version`

(optional) The model version of an object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_IMPORT_REQUEST_DETAILS_T Type

Properties used in import object request update operations.

Syntax
```

```

Fields

Field Description

`status`

(optional) The status of the object.

Allowed values are: 'TERMINATING'

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_PIPELINE_DETAILS_T Type

Properties used in pipeline update operations

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.

`model_type`

(required) The type of the object.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(required) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`nodes`

(optional) A list of nodes attached to the pipeline

`parameters`

(optional) A list of additional parameters required in pipeline.

`flow_config_values`

(optional)

`variables`

(optional) The list of variables required in pipeline.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_PROJECT_DETAILS_T Type

The properties used in project update operations.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify project.

`model_type`

(required) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) A user defined description for the project.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`parent_ref`

(optional)

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_DETAIL_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_child_reference_detail_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_REFERENCE_DETAILS_T Type

Application references that need to be updated.

Syntax
```

```

Fields

Field Description

`options`

(optional) A list of options such as `ignoreObjectOnError`.

`target_object`

(optional) The new target object to reference. This can be of type `DataAsset`, `Schema` or `Task`. In case of `DataAsset`, the child references can be of type `Connection`.

`child_references`

(optional) The list of child references that also need to be updated.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_SCHEDULE_DETAILS_T Type

The details for updating a schedule.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify schedule. On scenarios where reference to the schedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(required) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`frequency_details`

(optional)

`timezone`

(optional) The timezone for the schedule.

`is_daylight_adjustment_enabled`

(optional) A flag to indicate whether daylight adjustment should be considered or not.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_DETAILS_T Type

Properties used in task create operations.

Syntax
```

```

Fields

Field Description

`model_type`

(required) The type of the task.

Allowed values are: 'INTEGRATION_TASK', 'DATA_LOADER_TASK', 'PIPELINE_TASK', 'SQL_TASK', 'OCI_DATAFLOW_TASK', 'REST_TASK'

`key`

(required) Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.

`model_version`

(optional) The object's model version.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`identifier`

(optional) Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.

`input_ports`

(optional) An array of input ports.

`output_ports`

(optional) An array of output ports.

`parameters`

(optional) An array of parameters.

`op_config_values`

(optional)

`config_provider_delegate`

(optional)

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_DATA_LOADER_TASK_T Type

The information about the data loader task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_data_loader_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`data_flow`

(optional)

`conditional_composite_field_map`

(optional)

`is_single_load`

(optional) Defines whether Data Loader task is used for single load or multiple

`parallel_load_limit`

(optional) Defines the number of entities being loaded in parallel at a time for a Data Loader task

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_INTEGRATION_TASK_T Type

The information about the integration task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_integration_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`data_flow`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_OCI_DATAFLOW_TASK_T Type

The information about the OCI Dataflow task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_oci_dataflow_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`dataflow_application`

(optional)

`driver_shape_details`

(optional)

`executor_shape_details`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_PIPELINE_TASK_T Type

The information about the pipeline task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_pipeline_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`pipeline`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_REST_TASK_T Type

The information about the Generic REST task. The endpoint and cancelEndpoint properties are deprecated, use the properties executeRestCallConfig, cancelRestCallConfig and pollRestCallConfig for execute, cancel and polling of the calls.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_rest_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`auth_details`

(optional)

`auth_config`

(optional)

`endpoint`

(optional)

`method_type`

(optional) The REST method to use. This property is deprecated, use ExecuteRestCallConfig's methodType property instead.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`headers`

(optional) Headers data for the request.

`additional_properties`

(optional) Header value.

`json_data`

(optional) JSON data for payload body. This property is deprecated, use ExecuteRestCallConfig's payload config param instead.

`api_call_mode`

(optional) The REST invocation pattern to use. ASYNC_OCI_WORKREQUEST is being deprecated as well as cancelEndpoint/MethodType.

Allowed values are: 'SYNCHRONOUS', 'ASYNC_OCI_WORKREQUEST', 'ASYNC_GENERIC'

`cancel_endpoint`

(optional)

`cancel_method_type`

(optional) The REST method to use for canceling the original request.

Allowed values are: 'GET', 'POST', 'PATCH', 'DELETE', 'PUT'

`execute_rest_call_config`

(optional)

`cancel_rest_call_config`

(optional)

`poll_rest_call_config`

(optional)

`typed_expressions`

(optional) List of typed expressions.

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_SQL_TASK_T Type

The information about the SQL task.

Syntax
```

```

`dbms_cloud_oci_dataintegration_update_task_from_sql_task_t`is a subtype of the`dbms_cloud_oci_dataintegration_update_task_details_t`type.

Fields

Field Description

`script`

(optional)

`sql_script_type`

(optional) Indicates whether the task is invoking a custom SQL script or stored procedure.

Allowed values are: 'STORED_PROCEDURE', 'SQL_CODE'

`operation`

(optional) Describes the shape of the execution result

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_RUN_DETAILS_T Type

Properties used in task run update operations.

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the object.

`status`

(optional) The status of the object.

Allowed values are: 'TERMINATING'

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of an object.

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`task_schedule_key`

(optional) Optional task schedule key reference.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_SCHEDULE_DETAILS_T Type

The update task details.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.

`model_version`

(optional) This is a version number that is used by the service to upgrade objects if needed through releases of the service.

`model_type`

(optional) The type of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(required) This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`schedule_ref`

(optional)

`config_provider_delegate`

(optional)

`is_enabled`

(optional) enabled

`number_of_retries`

(optional) The number of retries.

`retry_delay`

(optional) The retry delay, the unit for measurement is in the property retry delay unit.

`retry_delay_unit`

(optional) The unit for the retry delay.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`start_time_millis`

(optional) The start time in milliseconds.

`end_time_millis`

(optional) The end time in milliseconds.

`is_concurrent_allowed`

(optional) Whether the same task can be executed concurrently.

`is_backfill_enabled`

(optional) Whether the backfill is enabled.

`auth_mode`

(optional) The authorization mode for the task.

Allowed values are: 'OBO', 'RESOURCE_PRINCIPAL', 'USER_CERTIFICATE'

`expected_duration`

(optional) The expected duration of the task.

`expected_duration_unit`

(optional) The expected duration of the task.

Allowed values are: 'SECONDS', 'MINUTES', 'HOURS', 'DAYS'

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_USER_DEFINED_FUNCTION_DETAILS_T Type

Properties used in user defined function update operations.

Syntax
```

```

Fields

Field Description

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`model_version`

(optional) The model version of an object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_WORKSPACE_DETAILS_T Type

The information to be updated, the private network can be enabled and VCN and subnet set only when initially it is has been created with it off.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user defined description for the workspace.

`display_name`

(optional) A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_T Type

The user defined function type contains the audit summary information and the definition of the user defined function.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

Allowed values are: 'DIS_USER_DEFINED_FUNCTION'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_DETAILS_T Type

The information about a user defined function.

Syntax
```

```

Fields

Field Description

`key`

(required) Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.

`model_type`

(required) The type of the object.

Allowed values are: 'DIS_USER_DEFINED_FUNCTION'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(required) The version of the object that is used to track changes in the object instance.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`registry_metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_T Type

The user defined function summary type contains the audit summary information and the definition of the user defined function.

Syntax
```

```

Fields

Field Description

`key`

(optional) Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.

`model_type`

(optional) The type of the object.

Allowed values are: 'DIS_USER_DEFINED_FUNCTION'

`model_version`

(optional) The model version of an object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`signatures`

(optional) An array of function signature.

`expr`

(optional)

`description`

(optional) Detailed description for the object.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`metadata`

(optional)

`key_map`

(optional) A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_user_defined_function_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_COLLECTION_T Type

This is the collection of user defined function summaries, it may be a collection of lightweight details or full definitions.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of user defined function summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_T Type

The information about a UserDefinedFunction validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the UserDefinedFunction object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_T Type

The information about a UserDefinedFunction validation.

Syntax
```

```

Fields

Field Description

`total_message_count`

(optional) The total number of validation messages.

`error_message_count`

(optional) The total number of validation error messages.

`warn_message_count`

(optional) The total number of validation warning messages.

`info_message_count`

(optional) The total number of validation information messages.

`validation_messages`

(optional) The detailed information of the UserDefinedFunction object validation.

`key`

(optional) Objects will use a 36 character key as unique ID. It is system generated and cannot be modified.

`model_type`

(optional) The type of the object.

`model_version`

(optional) The model version of the object.

`parent_ref`

(optional)

`name`

(optional) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.

`description`

(optional) Detailed description for the object.

`object_version`

(optional) The version of the object that is used to track changes in the object instance.

`object_status`

(optional) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.

`identifier`

(optional) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.

`metadata`

(optional)

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_user_defined_function_validation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_COLLECTION_T Type

A list of UserDefinedFunction validation summaries.

Syntax
```

```

Fields

Field Description

`items`

(required) The array of validation summaries.

### DBMS_CLOUD_OCI_DATAINTEGRATION_VALIDATION_MESSAGE_T Type

The level, message key, and validation message.

Syntax
```

```

Fields

Field Description

`l_level`

(optional) The total number of validation messages.

`message_key`

(optional) The validation message key.

`validation_message`

(optional) The validation message.

### DBMS_CLOUD_OCI_DATAINTEGRATION_WEEKLY_FREQUENCY_DETAILS_T Type

Frequency Details model for weekly frequency based on day of week.

Syntax
```

```

`dbms_cloud_oci_dataintegration_weekly_frequency_details_t`is a subtype of the`dbms_cloud_oci_dataintegration_abstract_frequency_details_t`type.

Fields

Field Description

`time`

(optional)

`days`

(optional) A list of days of the week to be scheduled. i.e. execute on Monday and Thursday.

Allowed values are: 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_RESOURCE_T Type

The resource that is created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the `IN_PROGRESS` state until work is complete for that resource at which point it will transition to `CREATED`, `UPDATED`, or `DELETED`, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'MOVED', 'IN_PROGRESS', 'FAILED', 'STOPPED', 'STARTED'

`identifier`

(required) The OCID or other unique identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that is used in a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_dataintegration_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_T Type

The API operations used to create and configure Data Integration resources do not take effect immediately. In these cases, the operation spawns an asynchronous workflow to fulfill the request. Work requests provide visibility into the status of these in-progress, long-running asynchronous workflows.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_WORKSPACE', 'UPDATE_WORKSPACE', 'DELETE_WORKSPACE', 'MOVE_WORKSPACE'

`status`

(required) The status of this work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains this work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources that are not in the same compartment, then the system picks a primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The completed percentage of the operation tracked by this work request.

`time_accepted`

(required) The date and time this work request was accepted, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_ERROR_T Type

The error that occured while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured, as listed in[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A user friendly description of the error that occured.

`l_timestamp`

(required) The date and time the error occured, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_LOG_ENTRY_T Type

The log message from executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A user friendly log message.

`l_timestamp`

(required) The date and time the log message was written, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_SUMMARY_T Type

A work request summary object.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_WORKSPACE', 'UPDATE_WORKSPACE', 'DELETE_WORKSPACE', 'MOVE_WORKSPACE'

`status`

(required) The status of this work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The ID of the work request.

`compartment_id`

(required) The OCID of the compartment that contains this work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources that are not in the same compartment, then the system picks a primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The completed percentage of the operation tracked by this work request.

`time_accepted`

(required) The date and time this work request was accepted, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`, in the timestamp format defined by[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORKSPACE_T Type

A workspace is an organizational construct to keep multiple data integration solutions and their resources (data assets, data flows, tasks, and so on) separate from each other, helping you to stay organized. For example, you could have separate workspaces for development, testing, and production.

Syntax
```

```

Fields

Field Description

`vcn_id`

(optional) The OCID of the VCN the subnet is in.

`subnet_id`

(optional) The OCID of the subnet for customer connected databases.

`dns_server_ip`

(optional) The IP of the custom DNS.

`dns_server_zone`

(optional) The DNS zone of the custom DNS to use to resolve names.

`is_private_network_enabled`

(optional) Specifies whether the private network connection is enabled or disabled.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A detailed description for the workspace.

`display_name`

(required) A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.

`compartment_id`

(optional) The OCID of the compartment containing the workspace.

`time_created`

(optional) The date and time the workspace was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the workspace was updated, in the timestamp format defined by[RFC3339](https://tools.ietf.org/html/rfc3339).

`lifecycle_state`

(optional) Lifecycle states for workspaces in Data Integration Service CREATING - The resource is being created and may not be usable until the entire metadata is defined UPDATING - The resource is being updated and may not be usable until all changes are commited DELETING - The resource is being deleted and might require deep cleanup of children. ACTIVE - The resource is valid and available for access INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for administrative reasons DELETED - The resource has been deleted and isn't available FAILED - The resource is in a failed state due to validation or other errors STARTING - The resource is being started and may not be usable until becomes ACTIVE again STOPPING - The resource is in the process of Stopping and may not be usable until it Stops or fails STOPPED - The resource is in Stopped state due to stop operation.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'STARTING', 'STOPPING', 'STOPPED'

`state_message`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.

`id`

(required) A system-generated and immutable identifier assigned to the workspace upon creation.

`endpoint_id`

(optional) OCID of the private endpoint associated with the container/workspace.

`endpoint_name`

(optional) Name of the private endpoint associated with the container/workspace.

`registry_id`

(optional) DCMS Registry ID associated with the container/workspace.

### DBMS_CLOUD_OCI_DATAINTEGRATION_WORKSPACE_SUMMARY_T Type

Summary details of a workspace.

Syntax
```

```

Fields

Field Description

`id`

(optional) A system-generated and immutable identifier assigned to the workspace upon creation.

`description`

(optional) A user defined description for the workspace.

`display_name`

(optional) A user-friendly display name that is changeable. Avoid entering confidential information.

`compartment_id`

(optional) The OCID of the compartment that contains the workspace.

`time_created`

(optional) The date and time the workspace was created, in the timestamp format defined by RFC3339.

`time_updated`

(optional) The date and time the workspace was updated, in the timestamp format defined by RFC3339.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`lifecycle_state`

(optional) The current state of the workspace.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'STARTING', 'STOPPING', 'STOPPED'

`state_message`

(optional) A detailed description about the current state of the workspace. Used to provide actionable information if the workspace is in a failed state.

`endpoint_name`

(optional) Name of the private endpoint associated with the container/workspace. Returns null if there is none.

`endpoint_id`

(optional) DCMS endpoint associated with the container/workspace. Returns null if there is none.

`registry_id`

(optional) DCMS registry associated with the container/workspace. Returns null if there is none.

- [Data Integration Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A41604F4-6460-4703-9810-64387CA5F0F3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6FAB54B7-311D-49B9-B69E-383A18E85C57)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_CALL_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3D479406-0B64-4C80-93E4-7D85124C174D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARENT_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D99A810C-0C43-4F85-A20C-9D99A06EF2D2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BASE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-312E7940-C17F-42BA-9F12-83BF743BA114)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PARAMETER_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-80020D5B-BF27-411F-9E9D-CF09CD09B219)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-81AF1C2D-A0D4-42EA-8234-D11D18A5F769)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-745C7BC4-7832-4FDE-BD98-0FDAFFD7129B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7DACA65A-9BE2-4C97-B39F-F823B6A311B0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_SYSTEM_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3D9046CB-5AA8-4A62-8E03-4A06492735CC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_AGGREGATOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FD3F682F-1F63-4103-9D94-1D710D2A8FB5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AEA8402F-8438-4276-A35B-07F06A89B5DB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1035686F-9BDD-4CAF-BDF2-747C57580C51)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COUNT_STATISTIC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2EFE0DC7-8BAF-4A4D-82BA-0FE3A5E0F284)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6D799483-8D77-4DC5-AA68-9D904F947DF6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EA119ED3-AA9B-489D-BB2E-014ECA7C95D7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_PROPERTY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-09B1F135-BE0A-49AB-AAC6-16FF684541B6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_PROPERTY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9B8E3E3B-AC8F-4773-8ADE-FC74DC20195C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C6BED2DA-4BD3-4D83-8C9F-B4AC1870D2C4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-01441711-17DE-4BA2-9352-E0D9A12C6561)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-53A31F01-A1E8-46D4-A3DA-D2D066E8ED94)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-794E4E11-DF85-400D-8BB9-99D8ABF10499)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_CALL_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E3A32BCE-A4E2-42EA-8DB5-6CDED80C3123)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_DATA_OPERATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-48F13239-AA22-4E17-813E-1ACECDE68899)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PARAMETER_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D2F50237-90EC-4048-91F2-CBF583A8C31B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_VALUES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-064BE527-601E-429B-90CA-BD247BF89737)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4BA6585B-62DA-4516-B484-194BB8537F1C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5C9B2127-16B3-4C61-9D95-30875B4D931B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FORMAT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D0FCE04-6AA6-4285-A584-F1A63EA5B085)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FORMATTED_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-714FA73D-273A-479D-A5F8-5F5C38DD0390)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-954636C2-1BEB-43FD-B7B4-6B566FB0C559)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_READ_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-56776F52-7F04-4FE5-A4AC-383ED4245C5D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ABSTRACT_WRITE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E7246EC0-BDC0-46CC-ACE0-94CA006A67DB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D72EFEE7-0A31-41E2-B03F-CC3528A7628E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-10A397C8-7160-4BEC-9F5E-8DD29F121541)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-637360A6-AC57-4E09-915E-20D9620EB834)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_PROXY_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E56FC51B-2827-44E5-A8A7-3A3EBDE30CF6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MATERIALIZED_COMPOSITE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A1418FFB-A26F-4542-89A1-D16FC4A29D40)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MATERIALIZED_DYNAMIC_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CF8EB6CD-FC60-4342-8EE6-496558ECC021)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PORT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3D22F04B-1F62-49FE-95B7-3C4B180414E9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BAFB5405-CEBE-4BDD-8EFA-A76CE811E2F5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4ACF0048-EE5B-4BA1-BD72-3F7153F33BCD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_AGGREGATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4281EC0A-9E70-44E8-A5C8-3F32DFE59343)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_OBJECT_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B1AA3726-40F7-47ED-80D6-412DD57C9201)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SOURCE_APPLICATION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5B1ABE93-B5B5-49CC-8EA3-7315721DA5C3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_OBJECT_METADATA_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0A21A6F7-FCED-42EB-9856-A0375B56407D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-31859EEB-E505-4676-A80F-7310E56F1BE6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-21DF0C90-C07A-4275-BF6A-CAE9685CACA8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DB3EDB4D-D849-4069-855A-CDAB114518FF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3CFEF21C-CDAF-4F12-8556-EB9790B41F8C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_APPLICATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B4E7FEFE-BE72-4274-BBE1-35ADF79CA854)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ARRAY_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6989EDF2-2CB7-478B-96F9-359DCECEFC5A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_AUTH_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-585E7B46-4D3B-43A3-A1D8-99144D625CCD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_AUTH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0166753D-FF56-461D-96B7-BF8CD77CD75A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_AVRO_FORMAT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-90BF2BAD-7417-44E0-929D-7DC63CD9A808)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTOR_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A380EE6E-EAE3-448E-9383-35276F637853)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B4CDAF00-A82F-4101-A883-EE7783E7E24D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BICC_READ_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52DDF7BC-181A-4020-BE83-A60CA65B4606)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_REPORT_PARAMETER_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1702A112-0E50-4F94-A513-5A69F8F0E88F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_REPORT_PARAMETER_VALUE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1291657E-E364-4FB9-A8D7-2171DA2931AA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_BIP_READ_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-747BB1AC-BFE4-46C8-A69F-B6212BFC529D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CANCEL_REST_CALL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-68BE2033-5441-477A-B7D4-B01526A8A2D2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-160812E6-5203-4B4F-B1B5-DF79C71A7255)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHANGE_DIS_APPLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-53F9EC6E-7E67-4A87-B693-BCB65AB752F0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_USED_BY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-59924BF9-C499-4D1D-9F2E-23C08E3D8973)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_USED_BY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3083B1FA-6B1A-45A0-99BE-124A38C70A50)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7853F9C3-66F8-4AFE-BBD1-152301BA6E85)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7A37CB7A-C224-462B-981E-5C4C17B36EC9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-657E9B80-4F6A-4CB4-A60A-47236F0A2C00)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BA531F12-5FAC-4ADB-A992-D9FBC5FC36BB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EA517D8B-A4FE-48B6-82DC-96AF318FD942)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARAMETER_VALUE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-ABD6FF45-0BE9-4367-A600-F656B29CB152)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_STATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5B27BAA8-E9C1-46E4-A64E-B24E660F6757)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REGISTRY_METADATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5B7D6415-14B3-4886-A241-4D8B7B3028F6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_STATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9244F3D2-930E-4169-B07E-4CE224968343)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_TYPE_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EAFE7A7B-D60D-4226-8984-A4EC10F2EECF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COMPOSITE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3189DF92-263C-4375-9BDC-AB39C6D899A8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COMPRESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C798DED5-C043-4B83-80B7-48BC8976EDDF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-807671A0-CB8D-447F-8C90-B3FB855BCE36)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E3FAEE6F-3D99-4B83-A3AE-AF6F1B1BA8CE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_COMPOSITE_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-113394B2-141F-401B-94BE-01F210D85E81)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_PORT_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FC3E3E24-0CCF-45FA-90A7-8C42CBBE20D0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F252EE3F-20E2-45A2-98A9-1F1DED8B9D41)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPRESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-79E8C88F-7CF9-4803-8F8E-ACB45C657356)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_INPUT_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2C55862E-FDD3-41B1-9A0F-838216787A60)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONDITIONAL_OUTPUT_PORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1BFE0DA7-F02D-4F49-8757-6863BCA7328C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PROVIDER_ABS_T](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9ED1C35C-58BD-476A-9003-5388BE250D7F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIG_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-41E953A2-CA6A-42A2-96E9-C277E6C17FEA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9BE4831C-1B16-462F-84E7-A4971328DD63)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5AB63D23-C746-497B-A75B-C57EA03D91A8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22FCA908-38A0-4987-94E2-1DF98445E3C6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONFIGURED_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9EB03969-FF41-4A6F-9D77-47D03A11D240)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A3B0668B-BD76-4F24-8830-8AC06BD83DF1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SECRET_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-57262FF7-6644-480D-A2DA-E21339BF1A13)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SENSITIVE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7C987541-55C2-4D2B-8A75-60475A4ECCDF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4FDE7E60-EBD9-4FF9-80C3-C1D29D8E764B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ADWC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-77FFB293-ADC7-46F5-9965-E30A7D293FBB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CB4CD2C4-AB68-4A08-9801-DDDD4F806270)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_AMAZON_S3_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DD212FCA-C9D9-4CE7-948E-CFC6E1E31E51)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-00BF615C-0E9D-4823-830E-F42A113DE0E9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ATP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-78BA07D7-1DAE-4455-A2D6-D0B17D6266F3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BICC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4D0279A5-ADB2-46D2-BE8F-2CE3CB8D79E1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BICC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9AB72327-89DC-45B1-AC0F-0E021F73C12C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-17C52C83-A004-4C38-A978-CA5B21AFA840)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_BIP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D04141C4-D88D-4902-82A3-B819446F28B9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8DE57015-A0AD-4605-9FE1-69659E204071)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_HDFS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-51288DB6-D907-45D3-A5FB-8A986C102D86)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-59CC0FDD-4DBD-4866-8343-2691734BECEA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0908D3FC-AAEC-4683-AE01-EFC661DB86ED)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8EC5E454-42EA-43F5-A4EB-EA40FD124596)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_LAKE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1A60885F-C1BA-4616-9795-B413777050C3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CDD2CC34-B802-40EA-968E-D46E03904194)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B56C093A-4D1C-453B-AA7D-4A3114978905)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8294D822-2DCD-4AFF-B70E-BD0469135394)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_MY_SQL_HEAT_WAVE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A0E741C9-08CC-4023-B152-22AED8E3C630)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-66CF6B80-7761-4707-9C73-AFFA1B4276A5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_OBJECT_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0530B181-0EC9-457E-96B4-A95E995655DA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-647C0435-ED0B-41A5-83B4-1F59F44AF940)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-61A4F6FC-CDC0-46F6-9BF9-798A22267249)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5018246E-3F61-4786-AEFD-578C7BDC1E8E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_EBS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CDA881EB-E014-4669-9C5E-B48C7D5ED14F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F78FF8AA-2EA8-4B8C-8CD0-29AA0DCA2803)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-18B32DD6-D644-407E-A4BF-29FF98E8F3BA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C23B2514-69DD-4AEC-91F0-70E09AE8314B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_ORACLE_SIEBEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-760131FE-D3AE-4E7B-878B-4C32B6D5BB11)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_BASIC_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A146C5DD-C987-4DA4-B70F-0E2853EDE040)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_BASIC_AUTH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-28AB896D-924A-416A-AF25-AE8AD2416036)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_NO_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-33E58A2D-A7C9-4E66-BF61-A9AAB3CF0650)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_FROM_REST_NO_AUTH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B2E7D904-B0D3-480E-A054-8673E9A612E7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7DB52536-524D-4A00-A3ED-9382BA5F72F7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-96F33E92-9084-4140-963C-DAC5CCC14FBA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D34EFA05-D79B-413D-955C-3234B59F0CC7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4C04774B-3100-4E53-B92E-3C13389A6D4F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0BC71EDF-51E0-420E-9FF9-8614A04AB80A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_BICC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-949E9E0F-40A6-4335-8F00-D7BCD53AD6D0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_BIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6B360EA8-6B62-4C02-9D06-76AAEC33B5FC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1B987994-CA05-4734-8E4B-834F420BDF28)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-106FF701-B58D-4682-8F73-3753FEB06ED6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D758D569-1D19-406F-B2BB-D1101FA1C93B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-17F9DB02-FAA4-4539-B69A-D8AF4026970C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2998AA46-F0B9-4E3E-9587-332F585D320F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-564C4101-C67D-4153-A827-2ADB3DE20B42)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-328F99E6-1E67-4CD6-BF3B-D81E08ACDA65)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-969CE949-2EA2-456C-8F5A-576707D20EBC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C125E00C-744E-4FD7-ABFF-5EA1E04FDD37)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_REST_BASIC_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4673DBB4-72B8-4F82-B964-E111DE62B626)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_SUMMARY_FROM_REST_NO_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-43F4272E-2EFB-43AD-B669-7EEAC214401A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CC59295C-C6C9-41CD-98A0-2A7D6B5257D4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-63CC560A-C3B0-4E70-8FAD-1A55D033B685)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-098E01B1-3AD9-4499-B0E8-B5E88BA01ECE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7B4E886E-1D66-4C1A-BC31-CB75AB136931)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CONNECTION_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3C29AD3C-B052-4681-A5EC-47CEAA026AF0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_CONFLICT_RESOLUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-ED2B3E48-4B10-43C0-8287-DF313033C4B5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-955A7E3D-1E3D-4F8D-BBC6-80A424AE7589)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_METADATA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B88BEC2B-94CE-4CFC-BB8F-CC0809080869)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-26F0285A-8612-4EE5-B219-583522FB3E71)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D5D543F4-A0A1-4E68-8258-43D91BC69E65)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FAE2EC34-F7A2-4DBF-A182-22BFCF903776)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_COPY_OBJECT_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-497A40C8-2363-47AF-97CA-32F0B7679D28)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_SOURCE_APPLICATION_INFO_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-181D2F8B-0993-4758-BBF3-4223778D659F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-01F45B4E-D27A-419B-8EC6-8B5D1D9B9A1D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONFIG_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-58EE225A-A87B-4CA5-AFCE-2BD04790E3C7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-36BCCF5F-C250-4FE6-AE43-1BE4E32E1957)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D682D2D-D53E-4288-99B6-46555964D709)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-36842ED7-4D60-47A5-A242-9AFEBC222DCB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2E505A7B-25E7-4D3A-AEEB-08E9B60F15D6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_BICC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7786A15E-46B0-44BB-9BE0-5B5C599AD93F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_BIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BCFCB7BB-39AA-49E3-8E37-FC577104B8ED)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-45526D4C-DADC-44D5-B265-9E0C5ADD4A0E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DDD5D7DC-8228-4075-9B0C-583B0B18CA19)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-16AE6119-0580-4546-B500-C0CAC4EFD4D9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-19A96971-50D2-4C79-89DC-52FA8C7D9610)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-740E1B65-724E-41F3-BD3E-725D1511C785)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-604F5BB1-7D9F-4E14-992C-9001004A02B9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-36B8F463-B539-499B-958A-38B7E19A09D6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-239887F2-90F5-49F1-B931-1B36FC309334)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-ABF1F7E6-B82B-482A-94B6-3C7D0BA6202C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F0BF76BD-28FE-4562-9F21-7AFED5E27B22)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_REST_BASIC_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52AA4B8A-CD7A-44C2-9553-F8C714BD9EB2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_FROM_REST_NO_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-08C0C4CE-5263-4E0C-9464-D0F21B4B6EAF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-280E3749-6B9A-4A34-A50A-A05B0AD76FB3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_CONNECTION_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4103086D-7144-4AA6-9D89-7FEC4CC5893F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_COPY_OBJECT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7E3CF6ED-E479-4E8B-A583-71E853EC0031)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D85AF5FB-2131-46E4-A4B9-39DA4CB5FC2D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7ABC7384-A101-4FF2-B33E-C4692AACEAE9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-301D215B-099D-427C-BBE3-C7B397A3E6A8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_FUSION_APP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0C56F991-7CA0-4331-B3B1-DA65496BC8E7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7D6431C3-C140-48CA-9B3D-E5FE5225B427)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F9F22EDA-E99F-4459-AADA-B2B04781CBE5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-25FE6B74-AFCF-489D-9CF7-774AE461718E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E2C115F0-565F-4B7C-9506-20EC71165352)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E562567B-D2FE-4F55-A2F8-8CB7A000C367)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8CE40924-6B7E-41CD-BF1A-2D1C92432675)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AF69A1FB-D1BA-4CC1-AC12-AE76BB9215A6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-68E7FD68-1481-4443-84D8-75F1DE3BEDF6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7980CAB7-85B8-4A18-B29C-55341FF7F013)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-208B032D-FB40-4827-8B66-2F77C7728DB1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_ASSET_FROM_REST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-02EE332C-7F4C-4E76-BBE0-432D4FCD05FD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_LINK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-624E0429-144A-4645-BCDD-9235E06D172C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UI_PROPERTIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3C630B45-0A9C-4128-A945-CBB5BFC2B5B6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-635BD6C1-2BDA-47E9-AB37-E0336CF5EF79)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_LINK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E477B163-C887-4F6D-80C8-4E64642659F4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_NODE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9E94FA68-4027-4197-AA89-C61DDAD5E78A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_NODE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-96814F0D-ADC8-472A-9E38-DF65BC51E091)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_FLOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0D93EC56-3153-466E-9BF3-14B9E5E674A0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_OBJECT_WRAPPER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-97AD7CDB-CAAC-471B-9A2D-F5FEBAC6CBF1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FIELD_MAP_WRAPPER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-79740BB5-B4AF-4E73-A5BF-F5985881C644)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DATA_FLOW_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DBADEFA1-32D6-42E5-82F9-C114700364FF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DETAILED_DESCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-590BB575-4E92-40A6-B5ED-7ABDD7ABC5FB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_DIS_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-29879FE3-9F7A-443A-A14B-42FB0B1FA9A1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FFE8E4F6-2443-48C2-895F-BE61256D8277)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-95FA30C4-B115-4502-ACAE-3BBF93F1BA49)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-184B59FF-4BFF-4C5A-9E51-8E106DA31E31)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_LIBRARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B1FF58BE-D025-4C3E-9A5E-7F92E388B646)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_NATIVE_SHAPE_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A6A9CDE4-00F0-4651-8EB1-8E9AE0F003CD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A99FF499-1BB5-449A-B8B2-2A3A9F8DFFAC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F86C8D3B-914D-4DC9-B2EC-A39698CDA0CA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_ATTRIBUTE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D64149F-391D-4FE1-A5CA-31B6D5FE8BA0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8CC36941-321E-41A0-9009-7449C6680DA4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FB11CCE3-670F-4D78-B0B2-3E89709123E1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOREIGN_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-17DD44D0-9459-4841-8EA1-C2203B5FD15A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FORMAT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7C1D3071-C38C-4A3E-AD65-17E48E0E413D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_KEY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BDDE86BA-D985-4448-95EE-BACBABC4CB26)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOREIGN_KEY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1ED305B3-CCDC-4ED2-BC24-0DFD411785F3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E1F42049-C968-4673-B208-417A4DB46995)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E587D04E-027D-4622-906D-EEF1A9A4A300)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_ENTITY_SHAPE_FROM_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2878B9A7-CA97-40E0-BB8B-E41DE7CEF315)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXPORT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C588C030-4780-42E4-A734-0AEE27B027CA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RESOURCE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A54690DC-8083-478B-B362-4EF95746048F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXTERNAL_PUBLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C7598271-A114-4572-9594-D4352E880861)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_EXTERNAL_PUBLICATION_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F5C0372B-2019-4E32-9050-503E7C76F0BF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_FOLDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-18890369-0FA8-40E2-8B41-AE295563F1BD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_FUNCTION_LIBRARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-241A24C8-5F7C-451B-B97F-9B140249546B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_CONFLICT_RESOLUTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9FA45C06-32DB-4827-878C-229F92C7A230)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_IMPORT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2A11F6B1-7477-4629-A3BC-B1A38E830228)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PATCH_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-97AEA8E1-90C2-4C74-98E0-5C8DBED76749)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ROOT_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-708C2E1E-2A9C-42DF-A4F7-AFCC07A31B1C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_VARIABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2B886FA8-EB6D-478D-B61F-66105866B3A4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_VARIABLE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D9F7F0E8-AFB5-4C8B-A71F-38E8FCFB350F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-27F24CF6-2B94-4538-A84E-7A896332460C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PIPELINE_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AA9D5FF9-73B6-4422-9336-AFCD5E451CB5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-31C8A222-8AB1-4915-8D9D-E41963FEBAD2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1DC6E5DC-EF9E-4C84-9C5A-F208F6152F0C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_PORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F1BB48CC-4283-4208-8851-ABCDC7B0E71A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_PORT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D05187F8-7C5C-435D-A856-4F934D33D057)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2F61D0F2-2074-4F88-AB25-202E170D44EB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1B4988AA-708A-484B-80A7-8D3836A39721)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-380B9AA4-6833-4600-BB57-9582591C6F4F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BE141B4F-C350-4615-9ED0-ADE4C7F0D5E5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATAFLOW_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F3116BFF-2C67-44D3-9E20-924ADC125718)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8B428F7F-EF3D-4A81-808F-19D09D5B6A1D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_OCI_DATAFLOW_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A7025C35-CF48-4727-BFFF-A2E8CE5B79E6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B6D9DC4F-F707-4546-BC84-D8E5AF9877B7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_PIPELINE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9AEBE56F-B49D-4918-A3BB-4690C5876EC5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXECUTE_REST_CALL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6539E3AF-9A5A-4643-BE53-CF8018E6C786)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_POLL_REST_CALL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-386AC20B-21B4-44CE-B9F6-6462D238EA96)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_EXPRESSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A343B6F7-9831-429F-8AAF-C25368913581)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_EXPRESSION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FCA2DC33-A45F-4A88-8D14-28DC95D08428)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_REST_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2408F93B-2F87-4797-AADA-2236EF6D52DD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCRIPT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-49678C8E-0CB4-4AB4-992A-3E0E338CDAD4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_FROM_SQL_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7572E5BA-1E0D-4CD9-A778-1DAA70AC17C1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DA9E1075-663E-4B9E-9817-9FBB184F6EA4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-25D4EBF9-51FD-4A7B-BEA6-B9388C479F34)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-69D66C19-8718-481F-AB6D-2C0A64E8F3B7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FDD60B17-3835-45D8-A95E-55467EE53ADC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-556F2773-E8A5-4154-B7A2-807C9BF1A59D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9C7B5ECE-169A-4EA2-817F-44021958284D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_TASK_VALIDATION_FROM_PIPELINE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-348AAD96-7985-4D34-A877-FF2B277A73DF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_SIGNATURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-781561C9-44ED-48B6-B564-CFB910DF304D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_SIGNATURE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C055872D-CD8F-48C4-BCCF-87D89EE6D9C1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_USER_DEFINED_FUNCTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9B631E64-2866-4922-A664-03A92189827E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_USER_DEFINED_FUNCTION_VALIDATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0054DC57-2CAB-4B1F-B007-7B4C0AC34F5E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CREATE_WORKSPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9B04079B-9F5C-44DE-A2D6-170086C4469D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CSV_FORMAT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6B787CF3-F73D-4CB2-8C43-161A86E9A154)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CUSTOM_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BA4437EB-1450-4360-818C-6287E1837012)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TIME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BCE23891-C98E-42E4-8F88-0C89292775A7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DAILY_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2E96635D-D846-4A9E-BFFA-5E4AC99D3122)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ADWC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-89B67AB9-63C3-41F8-BF7D-40BD86742B95)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6827D9D8-E927-4A00-BEBB-A0476F10A7EA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ATP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22E977DE-7D66-4158-B832-ACC962CAA25A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_FUSION_APP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6903AD43-F5E8-47F1-B7F4-0D910F1C1DA0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_HDFS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A93FE669-6EBE-4E99-A5F0-1EC2DCB3566A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7E8AFAE6-A129-45AE-A181-D5289C959BA7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_LAKE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1C020641-0A50-4DCE-B518-B8EBD1FF4942)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-43B51036-097E-4393-BF93-A62634C6A495)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E7B06372-214C-4158-A5CF-ED179709B50A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_OBJECT_STORAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AB8315E5-2153-449E-B5B5-60BC15DFE475)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-81CC8666-1728-4483-A24A-420A6B5A1BC6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_EBS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-05B39D39-753E-4BDC-9947-E0F47C1585DC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-36FB50E0-4D97-4E92-95E1-F27ECBBF79B9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_ORACLE_SIEBEL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-69B7A123-C17A-4F31-AC9B-5E64D082B454)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_FROM_REST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0FC2FA54-3A11-444A-99E2-AE69663825C8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-64BF421E-73C2-4306-8F68-95A3BE7BE607)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-08242DA4-8659-44E2-BE78-D4CA69A7C382)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1A149F78-480C-4364-8A21-75619A49F08B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0F6FDA12-A91F-48F1-B881-576C5B197E8D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CACB1A69-3837-408F-B578-6FF58F2DAC38)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_FUSION_APP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C6CBCE4E-A710-4DDF-8B14-7D4DF169711A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CFB40267-1A17-4E69-BE0E-34FD989A86A6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F49C95E6-06EA-4829-84F2-B8D03C1A39E4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B17FA733-6145-4E44-883A-12333DF1F682)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-591BDDF8-0BEC-4751-BDB9-DB5E2ACFAC05)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BF5B02F2-E331-45C6-ADE5-8B9BE0CCD257)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3E9E19E5-4C4C-4381-B33C-4443912218E3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FBAEF6E6-8AD2-476F-8E8E-20455A080B39)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-83578F9E-E126-4A69-9C04-7DD8D03ED465)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-61061D96-4B7B-49C9-BF2E-6D3078F9B456)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ASSET_SUMMARY_FROM_REST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-36926ED4-3265-4965-B3B5-966EF386E079)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E4BC5275-FADA-470F-84FA-00DBDC81D9F5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6BC559EE-BEC9-4BDF-9A1A-C7CCCDB4E9AB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_DATA_STORE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7648704B-2AC9-445D-A3B4-5618E3C621C2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_DATA_STORE_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CDBF44BA-AC26-4BB7-AB57-A3788985A7FD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4B90169B-FE2E-4F85-A1D2-65FFD64C2D06)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_FILE_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3AFC372F-C3E6-4666-B447-BAF5320F3348)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-864402CE-777D-48E0-9286-999EDA34B862)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_OBJECT_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-804D58F3-15F1-40BE-98B6-797903BF0D1A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-787F04AC-BB7E-490A-8898-A238C5E2C736)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_SQL_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5FA98344-CD8F-4601-B0DE-05FAA4B75801)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-60F38268-504D-425E-8FF8-6EEE0B9668D0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_TABLE_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9CF2AC60-19CC-43AE-AD7D-DD744EA633FD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_VIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8D682972-1C36-4DD9-88A1-3ABAC7509815)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_FROM_VIEW_ENTITY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-29F9718A-EFD6-43E2-AE74-0CE3E29424BC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DB601A14-2E2C-47BD-AB95-EB2523B4985D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-669570D2-64AD-47CC-B588-4CE1C53D090E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-02946C50-0C70-49AC-9AED-9583EE3CCBFC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_DATA_STORE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-69650983-5155-44D9-8B6C-C5B9B52B4EE6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D641A26-672C-41BF-80F3-DD3D6AB46F54)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E7F01F0A-7525-428F-87EB-C7184FA5ACB2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A9C2D725-2A71-440E-99B6-C3B94742A2B9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_TABLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6B21949C-0E88-4526-AB28-ECCD411A60CB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_ENTITY_SUMMARY_FROM_VIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AC84D83B-0A07-4BBE-832A-DE5CAF2EC4D8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-68698BE3-8E00-4488-8522-E9623227C554)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2370E333-12ED-4AA7-992C-DFC21C009080)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B5356EB5-B8BF-42FF-AC32-ACC8A42AB166)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-943CFE56-E07B-4B43-B25F-6541D2E73996)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-11E43DD9-6D54-4556-B1C7-5E0E6A111070)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F149CE0D-65D0-49F7-8E6F-7474102B2243)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1ED49328-F930-4881-A9B8-6EAC287A8DD3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DATA_FLOW_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C5E9442C-93F7-4570-A339-4CEF9468A80D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DECISION_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8044FCCA-9489-45D1-8EC5-56D11EEF9B89)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DECISION_OUTPUT_PORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22ABDB0B-B2CA-4DCB-BA56-53B12E19E804)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3E2BBBA3-0487-499D-9655-6C75CCDC514E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FB790032-0B00-4151-80A4-DD96737D2EEB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EF9E0346-CFB3-405F-A906-536A02B7539A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DEPENDENT_OBJECT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4EB1A867-DC5E-4C3E-99B6-D031CBCFD4B6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C4250778-B73A-439D-8268-9B2B6A2DC116)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3295BFD3-A084-406F-BA5A-3D22143820BF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DERIVED_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8EA2AE58-DCDC-408A-BDDB-9F1EDD04336B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DETAILED_DESCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E93C5A21-F92D-406B-B94D-3207BDB1CAF8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCOPE_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DEEEB246-59F1-4DE7-BECE-BD3DB82F4FAC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIRECT_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-04553F0F-4FDB-4F49-84A0-696238F25604)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIRECT_NAMED_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9FE832CA-3028-4011-93B8-10FB3E7F1638)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AFFB3F29-5173-4065-966E-98EB075A2C73)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-27190DC5-DBB7-4DB8-9D17-800723430198)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-ED4DC63E-6D8B-4B1B-8680-154D88E1447C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DIS_APPLICATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4F188DF6-8EB1-46D4-8EBD-27746988194E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DISTINCT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-611FE5D2-8E87-456A-B54B-FE78D1097AC5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_INPUT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-46348D31-14FC-44A3-B169-784762C9516F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_TYPE_HANDLER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A0CF9E5A-04F4-4186-919F-7F4C929C19FA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_DYNAMIC_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C1EB0B8E-9901-4218-9047-91575FFBB804)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_END_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BDE33455-9046-45C8-8A0B-CCD76D5D6AFA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ENRICHED_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-93A7F36D-E57A-4761-82AE-503839863AE9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EBBC2D4D-3878-4477-9600-EC3256413C38)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_FILE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-60FB231C-33BB-4439-8AE8-952771C4D61E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D1431A53-B02A-4BBF-82B6-D97325CD9ECE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ENTITY_SHAPE_FROM_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0E92978B-3DE0-4A02-AA6B-3B0045EC322D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ERROR_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1E925E0E-6EBD-4E45-A624-0249D9189BFC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_OBJECT_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52EBAB59-11B7-47F9-8C34-3C71FF5A9C8B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_OBJECT_METADATA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A2C75459-220A-4C12-BD15-5D71650E09FF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B6015D6B-1B76-471B-B8B2-356A6A6C84A2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9D8E0D94-72EB-49BD-B725-C0838C933174)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AF809EFF-52F5-4D71-BC99-A51FE9E32BA2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPORT_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2A566718-2BB4-4419-8D05-6E34361977A6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXPRESSION_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-87EC96E1-5350-410D-A6A7-C790CBCC90D2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7F45951F-4293-4F0D-B983-239C9F3E7899)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2E76184A-7D1E-45B0-A1EB-0CF519266307)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F683B823-C964-4C29-80BA-C529D03AED5A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8E18358E-D391-4808-8F1D-8C1C42F44076)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EADA8B11-E233-4303-820C-EE1CA5D83773)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0F0E2719-21EA-473E-9587-C4A9449F9E54)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EC3BD3A1-D434-4A4A-9EB0-3FBEB7A9FC64)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_EXTERNAL_PUBLICATION_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-73BB99B4-BAED-4307-8FD5-BA87D9B4103A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FILTER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C26515C1-D470-4164-8C46-61135739427C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUSH_DOWN_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22010619-DF50-4FD4-86CF-50BE6F420583)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FILTER_PUSH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BDBBE7AE-D077-4EFE-B49B-6414609FBF2D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_PROJECTION_PREFERENCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5FFEF90E-1F4D-4FE7-943B-55050722DD98)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-37D7D0BF-53D3-4961-87B8-19A82D259EBA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E8C71828-7864-4FE1-926B-B937A0ACF88F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLATTEN_TYPE_HANDLER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A4C71473-FD5A-49FD-8C59-893A0B2B311B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FLOW_PORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4653DFF5-4CEE-42DB-B7CD-88EEB21E38AE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5719A147-EAD9-45C8-8310-9F76B9B551B5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4809478D-98B3-4925-9816-8DB24826048A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4ED320C9-E052-44BD-AEE6-9E14A89D0D44)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-332783DF-D060-4B86-A8F1-F682566A30D1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FOLDER_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9172A394-E0A7-4653-9CA7-F6119B118EDD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_CONFIGURATION_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1E3A2E38-2505-4D90-926D-1BE7B1CF6DDA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OCI_FUNCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A88435CA-96B2-4101-8845-789EC2238D73)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3CC7101C-B282-4EC4-AB10-E6DD6740F935)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8F850332-8F0F-4111-8E5E-D344412B24C1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E0E62533-78A0-4D11-BD1E-0A5FC09748D7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-466890BE-3456-4283-91B1-0EF390482AD1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AE925943-ACD7-4DF1-B21E-F93561FD57F2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_FUNCTION_LIBRARY_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4E72525D-A1AC-45E7-B5E1-0135F2100AF0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_GENERIC_REST_API_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1C992AEE-7D77-4F47-8FFC-01E932F9BFD0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_GENERIC_REST_CALL_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-05DCED35-56AB-474C-8764-610170E3B142)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_GROUPED_NAME_PATTERN_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-20EA0A16-40CA-4529-8D81-79D264A258F2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_HOURLY_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3DD543A8-611B-4783-831C-F1B6F9413F63)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_OBJECT_METADATA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-60D855E2-73D4-4C1C-ACB2-736975C700AF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_OBJECT_METADATA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22335A98-6068-40DB-9F49-7F5F58F58BDC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6E9E8EEC-CB9A-4A9B-95C5-4EE58E1F9C8C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-861433A2-183B-4AD0-98BC-A279B4D328A9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-15ACCAD3-76EB-405E-A4D8-4344323FFFAF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_IMPORT_REQUEST_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-45BC3E50-9897-4146-8236-54DBC0B5D179)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_DATA_ENTITY_CLAUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-498FD924-E159-4599-B931-C78806D58E2E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_FIELD_CLAUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5DB018B0-EAA0-4128-BE2D-44AE8B6B4EDD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_FIELD_CLAUSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-24B1F4C8-00FD-415E-8027-ABD606306822)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_DATA_ENTITY_CLAUSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FAF7C827-66E2-4E6D-A407-BDCB310B858C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INCREMENTAL_READ_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E09ED783-B619-4AB2-AB52-0BDB8CEFE5F2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-330BA701-FF2F-4107-BBAF-5C2844F24C3F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INPUT_PROXY_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-48E4A617-AFC5-401D-B054-EC3FB974735C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_INTERSECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-776A5FFB-EC6A-4308-96A8-C9D6AAD3746C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JAVA_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A5DC2BF6-6E08-4846-A97C-EEDDFC6D4419)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JOIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3F593D14-07B8-470D-9BFD-1FB055060EDC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JOINER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-553A2827-4571-4DEA-9AA7-02E04ECFC4F0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_FORMAT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-74CF197C-6A8E-4338-930C-7F0A3F9E4364)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_TEXT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9B2E7040-37EE-4765-A4E2-D661B4FDF78F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_RANGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A58A27BD-435E-4B17-8C36-92A64B8B7FBA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARTITION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2F21C913-3BD6-4276-A7FA-43B7F9EAE067)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_KEY_RANGE_PARTITION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FB8C1710-906E-462F-9642-F731EE486A87)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_LAST_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-00699870-F5EA-486C-B8F0-3891C098B524)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_LOOKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-85C43546-3E41-4BBC-A025-1C6672E03E1C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MACRO_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-602FD7B4-13FD-41D7-8CDA-7F221EB0665B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MACRO_PIVOT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EE9C97E4-E161-4340-AE4C-A20CDBC7A237)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MAP_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0AE06CF6-3566-4DBB-9569-D85AE649BB40)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MERGE_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-32054AD3-4BD8-4ED7-AF73-5716B2513AE6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MINUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-00A68198-D87B-4BA9-B4FF-E0D337DC7BA3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_NUMBER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-33187F8B-D979-4BD5-9475-BD33F3FA117D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MONTHLY_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-683363FC-AA8F-4904-B9E8-EFB44D19F71A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_MONTHLY_RULE_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-152483AB-DDF6-4FF6-B4F8-55FC1DCAD666)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_NAME_LIST_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-843EC913-84B8-4CA0-9CA3-9FC32AFD1C54)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_NAME_PATTERN_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5298C74A-B62E-4D70-A87E-93381297B941)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_NAMED_ENTITY_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7BC5EDF7-5531-4667-B1DD-5FC485316F61)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_STORAGE_WRITE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-34A4F4C0-3226-45BD-B7B8-A5CBC46F6E37)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OBJECT_STORAGE_WRITE_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F1D2A1CD-B6C9-4040-AA1F-F37276BDC887)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OCI_VAULT_SECRET_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-35C0108F-89A3-4711-9388-27190CB6C2A9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-72157CDA-36BE-49E3-BDC5-799982B55B77)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_FROM_API_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E29C1ADD-4FDE-4F3F-855F-C21E9A1A0D1C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OPERATION_FROM_PROCEDURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B6D1FF1B-08D0-4BF4-9D04-6A79953741D7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ADWC_WRITE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-74E1E2E9-2374-462B-AAD2-09805660239F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ADWC_WRITE_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CA98AEE9-07AE-4447-A012-C038D2632492)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ATP_WRITE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D243369-88BA-476A-88FD-1281400E3B72)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_ATP_WRITE_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A99AA2F6-9BFE-4026-BDCE-BE44FABA072B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_READ_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-93ABF8DA-08CA-46C6-A8AA-1438836C77EA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_READ_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F41F80E6-F748-4456-B496-2CAFD87DF233)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_WRITE_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DFB8BA18-6EF2-4F08-9888-C8BB4C016C2A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_ORACLE_WRITE_ATTRIBUTES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-00D9F857-7EE1-4F00-9E5F-5920F25D7944)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_OUTPUT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-532A5B4E-1645-4C3D-A0CB-3219FEBFD81A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PARQUET_FORMAT_ATTRIBUTE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B34D7C6B-0CA5-4802-B048-346A73FE420B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-26F30305-674E-4123-ABC8-06961360F47F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-67F9F92F-BCF6-4538-B9F4-6E45197CDC9D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-316B47FB-FC3B-43ED-8722-B2CF583D3AC3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_CHANGE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4375325B-9853-499D-A03E-8E33DD701793)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-39C1B728-19D8-419A-B438-1C981FBD6731)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D1BBD467-F606-476E-BE15-677AFC37D382)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PATCH_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0BEADAB4-62F7-455A-8DE8-9BDBE545DEA7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3FC30502-330F-4621-9F34-25E58B173A7F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D194F55-FBED-43F2-A630-4CE5CE27C7EE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2A39C9C3-B4D9-4499-B15F-F232066E6990)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D6FD85D2-ECBB-4941-98BB-28A1912B4AE3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A95A5BCE-203B-439F-8C1F-61D978358B6F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3F9625FA-FA70-4AF0-A892-31303ECFCC1B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIPELINE_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-23071AC0-297F-4D6E-B3CD-FB7E513168C1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_KEYS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8BCC05E7-0744-4BF1-9812-17859CEFE673)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EC93A7D8-4008-47C9-8608-602B95A5BEF7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PIVOT_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EB913D74-DAF5-4F3D-B31F-16B241C2A4A7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PRIMARY_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1D689248-02E1-4FDC-B8AE-199A947FB422)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3C9616B2-A9F6-453F-B57A-08DAC94E008A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F6137B79-8150-426F-B108-4BA78F9B6451)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A351F10F-1452-4FB7-8AE0-4657295C4693)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52EB0668-A25B-4063-B932-85F3728AB37B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-46AC1247-9371-4DC5-88E9-6A270A5EC3A5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROJECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8177AF81-5D30-4331-869D-8827573C9922)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PROXY_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9E6BDA28-6640-4C37-BFCA-4DCC9CCE0545)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E8EAD42B-7433-46AB-9848-97E5737D41B8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1FDA9699-4ED7-4F9F-9BBD-BBA5E1A234ED)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E27340C5-0FE2-4E91-B532-7AE0733DB51E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_PIPELINE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C8F93548-A5C2-4B21-ACD0-9A1B98BB1D2B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-061E33B1-6767-42FD-B281-5D771BB935EC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_FROM_PIPELINE_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F1A9FFD5-C4F9-48BA-9414-1ECA3A9DB038)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-67A53A18-A033-4DD0-A258-7E4C1F2D0DC9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9759D425-5F88-4818-A029-537271836809)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BBD6D3F9-8B69-47E5-ABEC-033206514B7E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUBLISHED_OBJECT_SUMMARY_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9DAD4855-FC79-469E-88ED-D17F285A14E4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_QUERY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F802A490-910A-40A7-A3B6-3258A393D76A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_PUSH_DOWN_OPERATION_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-40205469-688E-4583-B0C5-3BBD006F6A8E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_READ_OPERATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-403FCA95-3A77-43E6-9B45-D8359CBD996A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B79AC6E4-E1C8-4EC7-ADBD-CB191DF7EAD5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9E00641E-AF9E-4C78-8DC4-90BCDAE9F802)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5355A467-723D-48BF-9A29-05C7496079AF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AEC6CFE1-7939-4EE0-B83E-173C59E2CCCA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A3E86457-5895-4F01-BE5B-965527E8420D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_FROM_API_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3F60848A-CAB6-4364-9180-729DD8898566)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REFERENCED_DATA_OBJECT_FROM_PROCEDURE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C215D85C-8919-490F-98FD-4544D78299F2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RENAME_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EFEBB98E-A4CE-4769-B503-DA466495C1F0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RESOURCE_PRINCIPAL_AUTH_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3E76EEB1-1B7F-4E6F-B0DC-A21D1F0A7BC1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_REST_CALL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FA56F206-5DC2-4ED9-B454-432143063F5A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_BASED_ENTITY_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F9F0C1BB-93EF-4912-A070-C2E4EEC9B963)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_TYPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-95F3ABD6-840D-4F3B-AD2A-EA8274A21CC0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RULE_BASED_FIELD_MAP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D9DEFABC-07AF-4CB6-AB1D-EE650A729EAE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AE48F06C-1B33-4388-A70E-8E4228F251D1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-93E6F39D-D5B2-410D-9A52-C5A979AF3FFF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-140A06AE-24B5-4FA6-908C-2E13E921D1E0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-097C0E51-D7BD-4DCD-8FFC-704F754A0E51)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_OPERATOR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F3859A7E-3019-40E1-8DD4-A6F483624D00)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BD8394DB-DB2F-4479-AC6E-C21A51254C80)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-FB2C528E-EE72-4A0E-B73B-F1E43D98108D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0A836E90-232D-45E9-BEF0-88EFBADBF262)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_RUNTIME_PIPELINE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5226028F-2839-48A8-9468-0F4F7BB6B9B7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D3F6D7AF-3CBD-4D85-8FB8-8D36726C2A0B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CF7F87C8-3684-4661-A965-C7E77AE6AEE9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEDULE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AADA1FB0-4ECD-4D9F-85B2-F3E4E0C6ABB4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_DRIFT_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5916B8C3-4AED-412B-B542-2C6755CBA172)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1981FA0F-FF38-4C14-A990-59C08FD0EBA0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A1EA2934-D231-414B-ACE9-55898A17948A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SCHEMA_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EF76C886-1462-4A83-BB8C-8F3F790AC965)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SHAPE_FIELD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-15266E27-13E6-4BD9-A33B-EB84067A1D86)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SELECT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EAC8719B-7B04-4A96-93A6-45ECBF112BB3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_CLAUSE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F854C2E5-0A3A-463D-A6EA-7468E959F396)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_CLAUSE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52E5F1C8-5FDD-4C8C-8559-8AD8C66C0E79)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-75D96613-2D0A-4DDF-B9E4-E1490B112F9D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1F46FEAD-C147-4907-8396-3204E648E537)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1167858B-74DF-4280-B585-09C1F15169A0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A51F06A6-7FE0-4C99-8A65-D340028634B4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SORT_OPER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D41B1521-E8E7-4307-94FF-CDB44B7770C5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8C8C38A1-5290-4630-8857-A85A55121049)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_SPLIT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C01CA43A-4409-433F-B9B5-788DFD37C9E5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_START_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6A554A37-A663-413F-A25B-6870E4286BAF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_STRUCTURED_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-22F02602-E51D-4F33-B20D-734D7EB6D284)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WRITE_OPERATION_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C4EF5170-18A5-43C2-9F5D-BD23BD4AC58C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TARGET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9455200F-8E2D-4C2E-9B16-2029273A2AB3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-39E9A020-6B66-4353-BA40-208301151832)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_DATA_LOADER_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7CFE719F-222B-4BCF-8851-A55E49271D16)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_INTEGRATION_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-76126CF7-7F28-4A6F-9740-DE889E7C9CD8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_OCI_DATAFLOW_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-60B565AE-68F0-4598-BC2F-51F265699290)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_PIPELINE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8F8388E6-0F1B-4656-9F96-3D6D6F5085D4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_REST_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4D78D8CD-59D8-441D-B60D-F282A2A30B4C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_FROM_SQL_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C1192698-5E32-4D1B-8BFE-524EC08A92AA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_OPERATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F27C8194-F927-4F13-A71E-B41CCCFBE0D0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-59D9B405-750A-442C-9D09-3280B4FA737C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5A170A54-562E-492D-8B32-482BC4E13001)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-821986DA-AC07-4714-AA99-3B9A1B86DCAF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A84FCA66-D817-4A10-832D-378135BDC5D3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E2CFD04F-6078-4FDC-A438-D5EEE9C1A55F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-7EC16242-362F-4AAC-8A8E-B0AF3E216CF4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LINEAGE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-52520299-6573-4837-B32E-E8435549E735)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-620FFED4-9480-4C2E-B13B-C2DD89971D91)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5E133FEE-1F12-4900-BC9A-CB648C45C3EF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C28184A5-E0F2-429C-B41E-FD3B94CE79C0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_RUN_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CD2D2ED7-8CA1-45D9-96FF-EA710C639CB1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4DEBA7EA-90CB-4AB2-BC5D-3FABE7964B0D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-27EC60D2-05D6-439A-B3A3-B51ABA7C1F9E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SCHEDULE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B1A6BF40-6413-42D3-BA95-9A7577A17C6B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-29C5B017-0F3E-4B1A-907B-54F2CC98CADF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1F59347D-F8B3-4A39-9188-BC66A5394A36)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-97F8DDB2-EC2A-4E9A-81A9-55A63061E463)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A050A4F4-7EFE-41EE-82FA-B45B7556D830)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-733F28BB-017A-46D9-8ADF-61AD5E661228)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_OCI_DATAFLOW_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D418AD96-83E9-48CB-AEB5-1DAF5662BE42)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_PIPELINE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2022BE14-715F-482C-9380-0403EF75B7F6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_REST_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-15C5D1B8-7EA1-4F50-8281-FC64447EBA5F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_SUMMARY_FROM_SQL_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B15073C5-0144-4DF8-A4D1-43D5B32E0CB4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E20484BA-BFA8-4DE2-948D-BE7EFC81F575)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-04D5BFA5-4EAB-4A88-8E05-A9C8BE2986B3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6A067EE7-9DC1-4D17-B36B-885545F5678C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TASK_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EAC41299-E62E-4BC3-8FC6-D17E90EB5623)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2257ED33-76B5-4198-B6B4-85FF14BE9001)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2D1FCC2C-82C2-4438-BD80-8ABB71C3DA8B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-088B759A-9F25-4B4E-AAFB-A7D6640665FE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TEMPLATE_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-175368FE-CED6-4777-A929-5E9C7503CBD3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_JSON_ELEMENT_T_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-85B6F868-2FD7-4A5E-B103-B252BDC08015)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPE_LIST_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4FC2449F-6E9F-4D24-A2DC-E80DB9DDF587)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_TYPED_NAME_PATTERN_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1EA175F6-89F1-4799-87E6-47B9979BDD01)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UNION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-F4A2A08F-3D36-4C2B-B62F-25267E904770)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UNIQUE_DATA_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6D0EC69C-323B-4B1F-8729-1D8A6D77B493)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-DD481052-EB66-4054-8CEB-1730231AB1FA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9F40E1B5-053C-4F27-A08B-3BCB54F1D2C3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-58E05A0E-71A1-4AD6-8087-4F50F3FF0B6D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2C2CB82B-AEB2-4E8E-A78E-D42E5A3D923A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-0602330C-AB6B-4074-820B-37FA637E74A0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_BICC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2F4DA3E2-0596-4D5C-955F-EFDBBD210FF0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_BIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AA7B104D-E8E8-4C88-A6F5-4392DD013DF0)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-33DC1CE4-B050-4890-B15A-564D519A8A33)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D3999986-736B-4850-9E7C-396BE4646F5A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D56BC210-D22E-4883-A04F-4F278AFEDC36)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-28FAF577-160B-474D-8150-1713496511CF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A4F23CAC-50C4-4ADB-A680-1CAD46F0D016)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-32AA2A79-9FF6-4A91-9146-10CEB3E34E40)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-9FB0368F-9237-44B0-9494-886FAB2DC149)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CC1338DE-AA23-46DD-A98F-1D3C0F5F9EA8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5EA9D2F4-2201-4072-B9B0-B005C32E74D7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-38A216D2-75AC-452F-A856-8C9C4272C1F7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_REST_BASIC_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-312F50CB-1135-4895-A3C3-87ED92AA1EC4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_CONNECTION_FROM_REST_NO_AUTH_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D820497B-B4E1-476D-B86E-245CDA8E2FCB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_COPY_OBJECT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-AD3DEFA7-1FEA-4682-8F02-1F36E65A4716)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-18A01544-DD52-4BBF-8F08-6ED84875A083)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ADWC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5B6D0CD5-3989-4DC4-8C4B-A7A4438A58C2)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_AMAZON_S3_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A61B9B13-6961-42AF-8951-FC8DBF0141FD)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ATP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B79A9C9E-8A5C-404E-8C7E-B40D8C0004BB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_FUSION_APP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8D5DCBAC-C766-483A-A3C2-B0E1B16BA3A8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_HDFS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-685567AB-92E7-48B6-9A2B-EAB10A76E57D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8471442F-B702-42F0-825F-D1BB439D8012)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_LAKE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CA50FA00-0377-4405-8AD5-8C6DBA1D92C8)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4458069D-5046-4602-A153-2334B9A851EE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_MY_SQL_HEAT_WAVE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-90955141-57EE-4A02-A4DA-9D769E3BA102)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_OBJECT_STORAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-4D3451DE-49BA-4497-AFA8-ABB4F88CA03C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-295D2B99-4741-459D-A67F-2DC907B04A53)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_EBS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EB6F4E1B-17CE-47A1-980A-B0B390ED89D5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_PEOPLE_SOFT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-29C808D9-72F9-43CD-894D-D8BE9ED5814B)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_ORACLE_SIEBEL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-638F4A91-D840-40A0-9838-941623BD8BEB)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_ASSET_FROM_REST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-652E670D-6093-4E5E-9521-6480A9B792FE)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DATA_FLOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-63189BF6-7DB1-47C7-955D-1902758FBC5D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DETAILED_DESCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-70385BD2-9DA7-4AE1-90E5-90E3A1F6C5F5)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_DIS_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3A129DF8-2223-4D14-B19C-CCD510E342FC)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_EXPORT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-981927E0-5BB5-452C-91D0-9B17237460D6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_EXTERNAL_PUBLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-08EF6C3F-449E-4555-9EC6-70730573EB74)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_FOLDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8E4135AF-11A2-4CD8-9943-6262106F5D87)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_FUNCTION_LIBRARY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-3D1A1C78-7D7C-40FB-ABF9-3942936113E9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_IMPORT_REQUEST_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-89ED465F-35D2-4B28-A9BE-BF5824F34769)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_PIPELINE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B3D33035-4432-4384-B36B-824DFDAE0C4A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_PROJECT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E6BF6F6D-2EE2-4235-8526-31E0D987807A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_CHILD_REFERENCE_DETAIL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-1B7F3015-EFFF-4CBD-8203-54F22A13B944)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_REFERENCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-EDB49002-4A64-4D26-A1D5-17878BE08E1A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-16F30EEA-2511-467F-9177-5833E9D3F737)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CBD53D5D-9BF9-4B71-A72F-57DF05EE223F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_DATA_LOADER_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-566A86AB-B09A-4D7A-AD0C-791A7784DE6F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_INTEGRATION_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-067FC44D-88F4-48F3-9822-924AF78CAA18)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_OCI_DATAFLOW_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-85CDA18E-CCD6-4E61-A0B5-77ACCC7054CF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_PIPELINE_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E3433707-69B1-4C30-9107-2DE14AB03CC7)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_REST_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CB4257B6-6845-4F70-88D6-36F5D12F9F41)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_FROM_SQL_TASK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2906B84A-D1C9-4303-AA1E-238ECE18DCAF)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2A2CFEE4-C57E-47A8-A1F0-031F68E30CA9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_TASK_SCHEDULE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-E6F98604-A5D0-48EF-B906-F8B024D870A1)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_USER_DEFINED_FUNCTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-6F1D002E-70BE-45F9-9165-B525E5D4194D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_UPDATE_WORKSPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-C62EA0D1-0352-40AA-BA18-AB9D3AFD03F6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-71F23FCE-C10A-4B65-8EE1-583C636E584D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-988332EA-9598-4750-A48B-A21B77B1BEC4)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8A0E30DD-8AD9-43EB-997F-CEBB7738AC6F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-86131B3A-739A-43C9-8D45-1C7FE9B61B7E)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-5DDCB8F6-3280-4D8E-B95E-3C373D70E2E9)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-796FC933-32F0-441B-8C60-F4049673F941)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-06D1E77C-FFD0-406E-8EC9-A410B4E2A949)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-351095EB-B7A1-4007-AFE8-556DC8069391)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_USER_DEFINED_FUNCTION_VALIDATION_SUMMARY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-D1529C73-C15C-4305-82B1-370183F78F0A)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_VALIDATION_MESSAGE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-B6B3615A-474C-4D49-ADE5-D470D23E658C)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WEEKLY_FREQUENCY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8B7FD83C-E121-4B30-994E-04F899B8FC2D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-54774DF2-4730-48C5-922F-EB804B2E967D)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-24B32E96-DA72-44E1-8980-D753134200A6)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-CF5B3261-E05F-4CC0-AAD1-6E897680400F)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-8BE610B2-BE8C-48B1-834C-B2FF25361DE3)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-674C53B8-2C54-4AA1-A21C-D6C825363F64)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-BFDAAF3F-C25D-4708-A975-93441DE584BA)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORKSPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-2161E1A4-C734-4CDF-88DB-3CFECDCADB89)
- [DBMS_CLOUD_OCI_DATAINTEGRATION_WORKSPACE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataintegration_t.html#ADSDK-GUID-A7D45BDA-1566-4DFA-A8DC-F90F2B7FD44B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
