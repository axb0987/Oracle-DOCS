# Data Flow Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#dcoc-content-body)

## Data Flow Common Types

### DBMS_CLOUD_OCI_DATAFLOW_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_LOG_CONFIG_T Type

Logging details of Application logs for Data Flow Run.

Syntax
```

```

Fields

Field Description

`log_group_id`

(required) The log group id for where log objects will be for Data Flow Runs.

`log_id`

(required) The log id of the log object the Application Logs of Data Flow Run will be shipped to.

### DBMS_CLOUD_OCI_DATAFLOW_SHAPE_CONFIG_T Type

This is used to configure the shape of the driver or executor if a flexible shape is used.

Syntax
```

```

Fields

Field Description

`ocpus`

(optional) The total number of OCPUs used for the driver or executors. See[here](https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Shape/)for details.

`memory_in_g_bs`

(optional) The amount of memory used for the driver or executors.

### DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_PARAMETER_T Type

The parameter of an application.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the parameter. It must be a string of one or more word characters (a-z, A-Z, 0-9, _). Examples: \"iterations\", \"input_file\"

`value`

(required) The value of the parameter. It must be a string of 0 or more characters of any kind. Examples: \"\" (empty string), \"10\", \"mydata.xml\", \"${x}\"

### DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_PARAMETER_TBL Type

Nested table type of dbms_cloud_oci_dataflow_application_parameter_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_T Type

A Data Flow application object.

Syntax
```

```

Fields

Field Description

`application_log_config`

(optional)

`archive_uri`

(optional) A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`arguments`

(optional) The arguments passed to the running application as command line arguments. An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code. Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example: `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`

`class_name`

(optional) The class for the application.

`configuration`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description.

`display_name`

(required) A user-friendly name. This name is not necessarily unique.

`driver_shape`

(required) The VM shape for the driver. Sets the driver cores and memory.

`driver_shape_config`

(optional)

`execute`

(optional) The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.

`executor_shape`

(required) The VM shape for the executors. Sets the executor cores and memory.

`executor_shape_config`

(optional)

`file_uri`

(required) An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The application ID.

`language`

(required) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`lifecycle_state`

(required) The current state of this application.

Allowed values are: 'ACTIVE', 'DELETED', 'INACTIVE'

`logs_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`metastore_id`

(optional) The OCID of OCI Hive Metastore.

`num_executors`

(required) The number of executor VMs requested.

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`parameters`

(optional) An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of 0 or more characters of any kind. Example: [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`private_endpoint_id`

(optional) The OCID of a private endpoint.

`spark_version`

(required) The Spark version utilized to run the application.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

`warehouse_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_SUMMARY_T Type

A Data Flow application object used in bulk listings.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. This name is not necessarily unique.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The application ID.

`language`

(required) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`lifecycle_state`

(required) The current state of this application.

Allowed values are: 'ACTIVE', 'DELETED', 'INACTIVE'

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`spark_version`

(required) The Spark version utilized to run the application.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

### DBMS_CLOUD_OCI_DATAFLOW_CHANGE_APPLICATION_COMPARTMENT_DETAILS_T Type

The change application compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

### DBMS_CLOUD_OCI_DATAFLOW_CHANGE_POOL_COMPARTMENT_DETAILS_T Type

The details required to change a pool compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

### DBMS_CLOUD_OCI_DATAFLOW_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

The details required to change a private endpoint compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

### DBMS_CLOUD_OCI_DATAFLOW_CHANGE_RUN_COMPARTMENT_DETAILS_T Type

The change run compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

### DBMS_CLOUD_OCI_DATAFLOW_CHANGE_SQL_ENDPOINT_COMPARTMENT_DETAILS_T Type

Details for changing the compartment of a SQL Endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_APPLICATION_DETAILS_T Type

The create application details.

Syntax
```

```

Fields

Field Description

`archive_uri`

(optional) A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`arguments`

(optional) The arguments passed to the running application as command line arguments. An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code. Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example: `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`

`application_log_config`

(optional)

`class_name`

(optional) The class for the application.

`compartment_id`

(required) The OCID of a compartment.

`configuration`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`driver_shape`

(required) The VM shape for the driver. Sets the driver cores and memory.

`driver_shape_config`

(optional)

`execute`

(optional) The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.

`executor_shape`

(required) The VM shape for the executors. Sets the executor cores and memory.

`executor_shape_config`

(optional)

`file_uri`

(optional) An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`language`

(required) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`logs_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`metastore_id`

(optional) The OCID of OCI Hive Metastore.

`num_executors`

(required) The number of executor VMs requested.

`parameters`

(optional) An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of 0 or more characters of any kind. Example: [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`private_endpoint_id`

(optional) The OCID of a private endpoint.

`spark_version`

(required) The Spark version utilized to run the application.

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

`warehouse_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_POOL_CONFIG_T Type

An object containing the details about the compute shapes and number of compute instances to provison.

Syntax
```

```

Fields

Field Description

`shape`

(optional) The compute shape of the resources you would like to provision.

`shape_config`

(optional)

`l_min`

(optional) Minimum number of compute instances in the pool for a given compute shape.

`l_max`

(optional) Maximum number of compute instances in the pool for a given compute shape.

### DBMS_CLOUD_OCI_DATAFLOW_POOL_SCHEDULE_T Type

Definition of when pool auto start or stop for a given day of a week.

Syntax
```

```

Fields

Field Description

`day_of_week`

(optional) Day of the week SUN-SAT

Allowed values are: 'SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'

`start_time`

(optional) Hour of the day to start or stop pool.

`stop_time`

(optional) Hour of the day to stop the pool.

### DBMS_CLOUD_OCI_DATAFLOW_POOL_CONFIG_TBL Type

Nested table type of dbms_cloud_oci_dataflow_pool_config_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_POOL_SCHEDULE_TBL Type

Nested table type of dbms_cloud_oci_dataflow_pool_schedule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_POOL_DETAILS_T Type

The details required to create a pool.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`configurations`

(required) List of PoolConfig items.

`schedules`

(optional) A list of schedules for pool to auto start and stop.

`idle_timeout_in_minutes`

(optional) Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period. If value not set, pool will not be auto stopped auto.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATAFLOW_SCAN_T Type

Single Client Access Name (SCAN) is the object with a fully-qualified domain name and a port number.

Syntax
```

```

Fields

Field Description

`fqdn`

(optional) A fully-qualified domain name (FQDN).

`port`

(optional) The port number of the FQDN

### DBMS_CLOUD_OCI_DATAFLOW_SCAN_TBL Type

Nested table type of dbms_cloud_oci_dataflow_scan_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_PRIVATE_ENDPOINT_DETAILS_T Type

The details required to create a private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(optional) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`dns_zones`

(required) An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`max_host_count`

(optional) The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256. If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.

`nsg_ids`

(optional) An array of network security group OCIDs.

`scan_details`

(optional) An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as value. [ { fqdn: \"scan1.oracle.com\", port: \"1521\"}, { fqdn: \"scan2.oracle.com\", port: \"1521\" } ]

`subnet_id`

(required) The OCID of a subnet.

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_RUN_DETAILS_T Type

The create run details. The following properties are optional and override the default values set in the associated application: - applicationId - archiveUri - applicationLogConfig - arguments - configuration - definedTags - displayName - driverShape - execute - executorShape - freeformTags - logsBucketUri - metastoreId - numExecutors - parameters - sparkVersion - warehouseBucketUri It is expected that either the applicationId or the execute parameter is specified; but not both. If both or none are set, a Bad Request (HTTP 400) status will be sent as the response. If an appicationId is not specified, then a value for the execute parameter is expected. Using data parsed from the value, a new application will be created and assicated with the new run. See information on the execute parameter for details on the format of this parameter. The optional parameter spark version can only be specified when using the execute parameter. If it is not specified when using the execute parameter, the latest version will be used as default. If the execute parameter is not used, the spark version will be taken from the associated application. If displayName is not specified, it will be derived from the displayName of associated application or set by API using fileUri's application file name. Once a run is created, its properties (except for definedTags and freeformTags) cannot be changed. If the parent application's properties (including definedTags and freeformTags) are updated, the corresponding properties of the run will not update.

Syntax
```

```

Fields

Field Description

`application_log_config`

(optional)

`application_id`

(optional) The OCID of the associated application. If this value is set, then no value for the execute parameter is required. If this value is not set, then a value for the execute parameter is required, and a new application is created and associated with the new run.

`archive_uri`

(optional) A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`arguments`

(optional) The arguments passed to the running application as command line arguments. An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code. Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example: `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`

`compartment_id`

(required) The OCID of a compartment.

`configuration`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name that does not have to be unique. Avoid entering confidential information. If this value is not specified, it will be derived from the associated application's displayName or set by API using fileUri's application file name.

`driver_shape`

(optional) The VM shape for the driver. Sets the driver cores and memory.

`driver_shape_config`

(optional)

`execute`

(optional) The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.

`executor_shape`

(optional) The VM shape for the executors. Sets the executor cores and memory.

`executor_shape_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`logs_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`metastore_id`

(optional) The OCID of OCI Hive Metastore.

`num_executors`

(optional) The number of executor VMs requested.

`parameters`

(optional) An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of 0 or more characters of any kind. Example: [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`spark_version`

(optional) The Spark version utilized to run the application. This value may be set if applicationId is not since the Spark version will be taken from the associated application.

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

`warehouse_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_NETWORK_CONFIGURATION_T Type

The network configuration of a SQL Endpoint.

Syntax
```

```

Fields

Field Description

`network_type`

(required) The type of network configuration.

Allowed values are: 'VCN', 'SECURE_ACCESS'

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_SQL_ENDPOINT_DETAILS_T Type

The information about a new SQL Endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The identifier of the compartment used with the SQL Endpoint.

`display_name`

(required) The SQL Endpoint name, which can be changed.

`description`

(optional) The description of CreateSQLEndpointDetails.

`sql_endpoint_version`

(required) The version of the SQL Endpoint.

`driver_shape`

(required) The shape of the SQL Endpoint driver instance.

`driver_shape_config`

(optional)

`executor_shape`

(required) The shape of the SQL Endpoint worker instance.

`executor_shape_config`

(optional)

`min_executor_count`

(required) The minimum number of executors.

`max_executor_count`

(required) The maximum number of executors.

`metastore_id`

(required) Metastore OCID

`lake_id`

(required) OCI lake OCID

`warehouse_bucket_uri`

(required) The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`spark_advanced_configurations`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`network_configuration`

(required)

### DBMS_CLOUD_OCI_DATAFLOW_CREATE_STATEMENT_DETAILS_T Type

The details required to create a statement.

Syntax
```

```

Fields

Field Description

`code`

(required) The statement code to execute. Example: `println(sc.version)`

### DBMS_CLOUD_OCI_DATAFLOW_ERROR_T Type

The error object.

Syntax
```

```

Fields

Field Description

`code`

(required) The unique code of an error.

`message`

(required) The description of an error.

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_OUTPUT_DATA_T Type

An object representing execution output of a statement.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the `StatementOutputData` like `TEXT_PLAIN`, `TEXT_HTML` or `IMAGE_PNG`.

Allowed values are: 'TEXT_PLAIN', 'TEXT_HTML', 'IMAGE_PNG'

### DBMS_CLOUD_OCI_DATAFLOW_IMAGE_PNG_STATEMENT_OUTPUT_DATA_T Type

The statement output data in png format.

Syntax
```

```

`dbms_cloud_oci_dataflow_image_png_statement_output_data_t`is a subtype of the`dbms_cloud_oci_dataflow_statement_output_data_t`type.

Fields

Field Description

`value`

(required) The statement code execution output in png format.

### DBMS_CLOUD_OCI_DATAFLOW_NODE_COUNT_T Type

An object with a logical shape and count of the number of nodes with that shape.

Syntax
```

```

Fields

Field Description

`logical_shape`

(optional) The compute shape of the nodes that the count is for.

`l_count`

(optional) The node count of this compute shape.

### DBMS_CLOUD_OCI_DATAFLOW_NODE_COUNT_TBL Type

Nested table type of dbms_cloud_oci_dataflow_node_count_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_POOL_METRICS_T Type

A collection of metrics related to a particular pool.

Syntax
```

```

Fields

Field Description

`time_last_started`

(optional) The last time this pool was started.

`time_last_stopped`

(optional) The last time this pool was stopped.

`time_last_used`

(optional) The last time a run used this pool.

`time_last_metrics_updated`

(optional) The last time the mertics were updated for this.

`active_runs_count`

(optional) The number of runs that are currently running that are using this pool.

`actively_used_node_count`

(optional) A count of the nodes that are currently being used for each shape in this pool.

### DBMS_CLOUD_OCI_DATAFLOW_POOL_T Type

A Data Flow pool object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`lifecycle_details`

(optional) The detailed messages about the lifecycle state.

`lifecycle_state`

(required) The current state of this pool.

Allowed values are: 'ACCEPTED', 'SCHEDULED', 'CREATING', 'ACTIVE', 'STOPPING', 'STOPPED', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`pool_metrics`

(optional)

`configurations`

(required) List of PoolConfig items.

`schedules`

(optional) A list of schedules for pool to auto start and stop.

`idle_timeout_in_minutes`

(optional) Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period. If value not set, pool will not be auto stopped auto.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_POOL_SUMMARY_T Type

A pool object used in bulk listings.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`lifecycle_state`

(required) The current state of this pool.

Allowed values are: 'ACCEPTED', 'SCHEDULED', 'CREATING', 'ACTIVE', 'STOPPING', 'STOPPED', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(required) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_POOL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataflow_pool_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_POOL_COLLECTION_T Type

The results of a query for a list of pools. It contains PoolSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of pools.

### DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_T Type

A Data Flow private endpoint object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`dns_zones`

(required) An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a private endpoint.

`lifecycle_details`

(optional) The detailed messages about the lifecycle state.

`lifecycle_state`

(required) The current state of this private endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`max_host_count`

(optional) The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256. If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.

`nsg_ids`

(optional) An array of network security group OCIDs.

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`scan_details`

(optional) An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as value. [ { fqdn: \"scan1.oracle.com\", port: \"1521\"}, { fqdn: \"scan2.oracle.com\", port: \"1521\" } ]

`subnet_id`

(required) The OCID of a subnet.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_SUMMARY_T Type

A Data Flow private endpoint object used in bulk listings.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(required) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`dns_zones`

(required) An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of a private endpoint.

`lifecycle_state`

(required) The current state of this private endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'FAILED'

`max_host_count`

(optional) The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256. If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.

`nsg_ids`

(optional) An array of network security group OCIDs.

`owner_principal_id`

(required) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`scan_details`

(optional) An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as value. [ { fqdn: \"scan1.oracle.com\", port: \"1521\"}, { fqdn: \"scan2.oracle.com\", port: \"1521\" } ]

`subnet_id`

(required) The OCID of a subnet.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataflow_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_COLLECTION_T Type

The results of a query for a list of private endpoints. It contains PrivateEndpointSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of private endpoints.

### DBMS_CLOUD_OCI_DATAFLOW_RUN_T Type

A run object.

Syntax
```

```

Fields

Field Description

`archive_uri`

(optional) A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`arguments`

(optional) The arguments passed to the running application as command line arguments. An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code. Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example: `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`

`application_id`

(required) The application ID.

`application_log_config`

(optional)

`class_name`

(optional) The class for the application.

`compartment_id`

(required) The OCID of a compartment.

`configuration`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`data_read_in_bytes`

(optional) The data read by the run in bytes.

`data_written_in_bytes`

(optional) The data written by the run in bytes.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. This name is not necessarily unique.

`driver_shape`

(required) The VM shape for the driver. Sets the driver cores and memory.

`driver_shape_config`

(optional)

`execute`

(optional) The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.

`executor_shape`

(required) The VM shape for the executors. Sets the executor cores and memory.

`executor_shape_config`

(optional)

`file_uri`

(required) An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The ID of a run.

`language`

(required) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`lifecycle_details`

(optional) The detailed messages about the lifecycle state.

`lifecycle_state`

(required) The current state of this run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'FAILED', 'SUCCEEDED', 'STOPPING', 'STOPPED'

`logs_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`metastore_id`

(optional) The OCID of OCI Hive Metastore.

`num_executors`

(required) The number of executor VMs requested.

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`owner_principal_id`

(optional) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`parameters`

(optional) An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of 0 or more characters of any kind. Example: [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`private_endpoint_dns_zones`

(optional) An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`

`private_endpoint_max_host_count`

(optional) The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256. If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.

`private_endpoint_nsg_ids`

(optional) An array of network security group OCIDs.

`private_endpoint_id`

(optional) The OCID of a private endpoint.

`private_endpoint_subnet_id`

(optional) The OCID of a subnet.

`run_duration_in_milliseconds`

(optional) The duration of the run in milliseconds.

`spark_version`

(required) The Spark version utilized to run the application.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`total_o_cpu`

(optional) The total number of oCPU requested by the run.

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

`warehouse_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_RUN_LOG_SUMMARY_T Type

A summary of a log associated with a particular run.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the log. Example: spark_driver_stderr_20190917T114000Z.log.gz

`run_id`

(required) The runId associated with the log.

`size_in_bytes`

(optional) The size of the object in bytes.

`source`

(required) The source of the log such as driver and executor.

Allowed values are: 'APPLICATION', 'DRIVER', 'EXECUTOR'

`time_created`

(optional) The date and time the object was created, as described in[RFC 2616](https://tools.ietf.org/rfc/rfc2616), section 14.29.

`l_type`

(required) The type of log such as stdout and stderr.

Allowed values are: 'STDERR', 'STDOUT'

### DBMS_CLOUD_OCI_DATAFLOW_RUN_SUMMARY_T Type

A summary of the run.

Syntax
```

```

Fields

Field Description

`application_id`

(required) The application ID.

`compartment_id`

(required) The OCID of a compartment.

`data_read_in_bytes`

(optional) The data read by the run in bytes.

`data_written_in_bytes`

(optional) The data written by the run in bytes.

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`display_name`

(optional) A user-friendly name. This name is not necessarily unique.

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The ID of a run.

`language`

(required) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`lifecycle_details`

(optional) The detailed messages about the lifecycle state.

`lifecycle_state`

(required) The current state of this run.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'FAILED', 'SUCCEEDED', 'STOPPING', 'STOPPED'

`opc_request_id`

(optional) Unique Oracle assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`owner_principal_id`

(optional) The OCID of the user who created the resource.

`owner_user_name`

(optional) The username of the user who created the resource. If the username of the owner does not exist, `null` will be returned and the caller should refer to the ownerPrincipalId value instead.

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`run_duration_in_milliseconds`

(optional) The duration of the run in milliseconds.

`total_o_cpu`

(optional) The total number of oCPU requested by the run.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_updated`

(required) The date and time the resource was updated, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`l_type`

(optional) The Spark application processing type.

Allowed values are: 'BATCH', 'STREAMING', 'SESSION'

### DBMS_CLOUD_OCI_DATAFLOW_SECURE_ACCESS_CONTROL_RULE_T Type

The access control rule for SECURE_ACCESS network type selection.

Syntax
```

```

Fields

Field Description

`ip_notation`

(required) The type of IP notation.

Allowed values are: 'IP_ADDRESS', 'CIDR', 'VCN', 'VCN_OCID'

`value`

(required) The associated value of the selected IP notation.

`vcn_ips`

(optional) A comma-separated IP or CIDR address for VCN OCID IP notation selection.

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_T Type

The description of a SQL Endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The provision identifier that is immutable on creation.

`display_name`

(required) The SQL Endpoint name, which can be changed.

`compartment_id`

(required) The OCID of a compartment.

`jdbc_endpoint_url`

(optional) The JDBC URL field. For example, jdbc:spark://{serviceFQDN}:443/default;SparkServerType=DFI

`time_created`

(optional) The time the Sql Endpoint was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Sql Endpoint was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Sql Endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) A message describing the reason why the resource is in it's current state. Helps bubble up errors in state changes. For example, it can be used to provide actionable information for a resource in the Failed state.

`sql_endpoint_version`

(required) The version of SQL Endpoint.

`driver_shape`

(required) The shape of the SQL Endpoint driver instance.

`driver_shape_config`

(optional)

`executor_shape`

(required) The shape of the SQL Endpoint executor instance.

`executor_shape_config`

(optional)

`min_executor_count`

(required) The minimum number of executors.

`max_executor_count`

(required) The maximum number of executors.

`metastore_id`

(required) The OCID of OCI Hive Metastore.

`lake_id`

(required) The OCID of OCI Lake.

`warehouse_bucket_uri`

(required) The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html

`description`

(required) The description of the SQL Endpoint.

`last_accepted_request_token`

(optional) This token is used by Splat, and indicates that the service accepts the request, and that the request is currently being processed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`spark_advanced_configurations`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SUMMARY_T Type

A summary of the Sql Endpoint.

Syntax
```

```

Fields

Field Description

`id`

(required) The provision identifier that is immutable on creation.

`display_name`

(required) The SQL Endpoint name, which can be changed.

`compartment_id`

(required) The OCID of a compartment.

`jdbc_endpoint_url`

(optional) The JDBC URL field. For example, jdbc:spark://{serviceFQDN}:443/default;SparkServerType=DFI

`time_created`

(optional) The time the Sql Endpoint was created. An RFC3339 formatted datetime string.

`time_updated`

(optional) The time the Sql Endpoint was updated. An RFC3339 formatted datetime string.

`lifecycle_state`

(optional) The current state of the Sql Endpoint.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`state_message`

(optional) A message describing the reason why the resource is in it's current state. Helps bubble up errors in state changes. For example, it can be used to provide actionable information for a resource in the Failed state.

`sql_endpoint_version`

(required) The version of SQL Endpoint.

`driver_shape`

(required) The shape of the SQL Endpoint driver instance.

`driver_shape_config`

(optional)

`executor_shape`

(required) The shape of the SQL Endpoint executor instance.

`executor_shape_config`

(optional)

`min_executor_count`

(required) The minimum number of executors.

`max_executor_count`

(required) The maximum number of executors.

`owner_principal_id`

(optional) The OCID of the user who created the resource.

`metastore_id`

(required) The OCID of OCI Hive Metastore.

`lake_id`

(required) The OCID of OCI Lake.

`warehouse_bucket_uri`

(required) The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html

`description`

(required) The description of the SQL Endpoint.

`last_accepted_request_token`

(optional) This token is used by Splat, and indicates that the service accepts the request, and that the request is currently being processed.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`spark_advanced_configurations`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`network_configuration`

(optional)

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataflow_sql_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_COLLECTION_T Type

The results of a Sql Endpoint search. It contains the objects in a SqlEndpointSummary.

Syntax
```

```

Fields

Field Description

`items`

(required) The collection of SqlEndpointSummary objects.

### DBMS_CLOUD_OCI_DATAFLOW_SECURE_ACCESS_CONTROL_RULE_TBL Type

Nested table type of dbms_cloud_oci_dataflow_secure_access_control_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SECURE_ACCESS_CONFIG_T Type

Access control rules for secure access selection.

Syntax
```

```

`dbms_cloud_oci_dataflow_sql_endpoint_secure_access_config_t`is a subtype of the`dbms_cloud_oci_dataflow_sql_endpoint_network_configuration_t`type.

Fields

Field Description

`access_control_rules`

(optional) A list of SecureAccessControlRule's to which access is limited to

`public_endpoint_ip`

(optional) Ip Address of public endpoint

### DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_VCN_CONFIG_T Type

The VCN configuration for VCN network type selection.

Syntax
```

```

`dbms_cloud_oci_dataflow_sql_endpoint_vcn_config_t`is a subtype of the`dbms_cloud_oci_dataflow_sql_endpoint_network_configuration_t`type.

Fields

Field Description

`vcn_id`

(required) The VCN OCID.

`subnet_id`

(required) The VCN Subnet OCID.

`host_name_prefix`

(optional) The host name prefix.

`nsg_ids`

(optional) The OCIDs of Network Security Groups (NSGs).

`private_endpoint_ip`

(optional) Ip Address of private endpoint

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_OUTPUT_T Type

The execution output of a statement.

Syntax
```

```

Fields

Field Description

`data`

(optional)

`status`

(optional) Status of the statement output.

Allowed values are: 'OK', 'ERROR'

`error_name`

(optional) The name of the error in the statement output.

`error_value`

(optional) The value of the error in the statement output.

`traceback`

(optional) The traceback of the statement output.

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_T Type

A statement object.

Syntax
```

```

Fields

Field Description

`id`

(required) The statement ID.

`code`

(required) The statement code to execute. Example: `println(sc.version)`

`lifecycle_state`

(required) The current state of this statement.

Allowed values are: 'ACCEPTED', 'CANCELLING', 'CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED'

`output`

(optional)

`progress`

(optional) The execution progress.

`run_id`

(optional) The ID of a run.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_completed`

(optional) The date and time a statement execution was completed, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-05-31T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_SUMMARY_T Type

Summary of the statement.

Syntax
```

```

Fields

Field Description

`id`

(required) The statement ID.

`lifecycle_state`

(required) The current state of this statement.

Allowed values are: 'ACCEPTED', 'CANCELLING', 'CANCELLED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED'

`run_id`

(optional) The ID of a run.

`time_created`

(required) The date and time the resource was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2018-04-03T21:10:29.600Z`

`time_completed`

(optional) The date and time a statement execution was completed, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2022-05-31T21:10:29.600Z`

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataflow_statement_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_COLLECTION_T Type

The results of a query for a list of statements of a Session Run. It contains StatementSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of statements for a Session Run.

### DBMS_CLOUD_OCI_DATAFLOW_TEXT_HTML_STATEMENT_OUTPUT_DATA_T Type

The statement output data in html format.

Syntax
```

```

`dbms_cloud_oci_dataflow_text_html_statement_output_data_t`is a subtype of the`dbms_cloud_oci_dataflow_statement_output_data_t`type.

Fields

Field Description

`value`

(required) The statement code execution output in html format.

### DBMS_CLOUD_OCI_DATAFLOW_TEXT_PLAIN_STATEMENT_OUTPUT_DATA_T Type

The statement output data in text format.

Syntax
```

```

`dbms_cloud_oci_dataflow_text_plain_statement_output_data_t`is a subtype of the`dbms_cloud_oci_dataflow_statement_output_data_t`type.

Fields

Field Description

`value`

(required) The statement code execution output in text format.

### DBMS_CLOUD_OCI_DATAFLOW_UPDATE_APPLICATION_DETAILS_T Type

The update application details.

Syntax
```

```

Fields

Field Description

`class_name`

(optional) The class for the application.

`file_uri`

(optional) An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`spark_version`

(optional) The Spark version utilized to run the application.

`language`

(optional) The Spark language.

Allowed values are: 'SCALA', 'JAVA', 'PYTHON', 'SQL'

`application_log_config`

(optional)

`archive_uri`

(optional) A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`arguments`

(optional) The arguments passed to the running application as command line arguments. An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code. Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example: `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`

`configuration`

(optional) The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(optional) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`driver_shape`

(optional) The VM shape for the driver. Sets the driver cores and memory.

`driver_shape_config`

(optional)

`execute`

(optional) The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.

`executor_shape`

(optional) The VM shape for the executors. Sets the executor cores and memory.

`executor_shape_config`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`logs_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`metastore_id`

(optional) The OCID of OCI Hive Metastore.

`num_executors`

(optional) The number of executor VMs requested.

`parameters`

(optional) An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of 0 or more characters of any kind. Example: [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

`pool_id`

(optional) The OCID of a pool. Unique Id to indentify a dataflow pool resource.

`private_endpoint_id`

(optional) The OCID of a private endpoint.

`warehouse_bucket_uri`

(optional) An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_UPDATE_POOL_DETAILS_T Type

The details required to update a given pool with ```poolId```.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`configurations`

(optional) List of PoolConfig items.

`schedules`

(optional) A list of schedules for pool to auto start and stop.

`idle_timeout_in_minutes`

(optional) Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period. If value not set, pool will not be auto stopped auto.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_DATAFLOW_UPDATE_PRIVATE_ENDPOINT_DETAILS_T Type

The details required to update a private endpoint.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A user-friendly description. Avoid entering confidential information.

`display_name`

(optional) A user-friendly name. It does not have to be unique. Avoid entering confidential information.

`dns_zones`

(optional) An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`max_host_count`

(optional) The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256. If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.

`nsg_ids`

(optional) An array of network security group OCIDs.

`scan_details`

(optional) An array of fqdn/port pairs used to create private endpoint. Each object is a simple key-value pair with FQDN as key and port number as value. [ { fqdn: \"scan1.oracle.com\", port: \"1521\"}, { fqdn: \"scan2.oracle.com\", port: \"1521\" } ]

### DBMS_CLOUD_OCI_DATAFLOW_UPDATE_RUN_DETAILS_T Type

The update run details. Only a limited set of properties of a run can be updated.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`max_duration_in_minutes`

(optional) The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated once it reaches this duration from the time it transitions to `IN_PROGRESS` state.

`idle_timeout_in_minutes`

(optional) The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period. Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)

### DBMS_CLOUD_OCI_DATAFLOW_UPDATE_SQL_ENDPOINT_DETAILS_T Type

Currently only the tags of a SQL Endpoint can be updated.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_RESOURCE_T Type

A resource related to a Data Flow work request.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'INPROGRESS', 'RELATED'

`id`

(optional) The id of a work request resource object.

`resource_id`

(required) The id of the releated resource. See resourceType to identity the specific type of resource.

`resource_type`

(required) The type of resource. See resourceId for the id of the specific resource.

`resource_uri`

(optional) The URI path that the user can use to get access to the resource metadata

`work_requestid`

(optional) The OCID of a work request.

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_dataflow_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_T Type

A Data Flow work request object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`id`

(required) The OCID of a work request.

`operation`

(required) The operation related to this work request.

Allowed values are: 'CREATE_PRIVATE_ENDPOINT', 'UPDATE_PRIVATE_ENDPOINT', 'DELETE_PRIVATE_ENDPOINT', 'MOVE_PRIVATE_ENDPOINT'

`percent_complete`

(required) Percentage of the request completed.

`resources`

(required) The resources affected by this work request.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'CANCELLED', 'CANCELLING', 'FAILED', 'INPROGRESS', 'SUCCEEDED'

`time_accepted`

(optional) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_SUMMARY_T Type

A Data Flow work request summary object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of a compartment.

`id`

(required) The OCID of a work request.

`operation`

(required) The operation related to this work request.

Allowed values are: 'CREATE_PRIVATE_ENDPOINT', 'UPDATE_PRIVATE_ENDPOINT', 'DELETE_PRIVATE_ENDPOINT', 'MOVE_PRIVATE_ENDPOINT'

`percent_complete`

(required) Percentage of the request completed.

`resources`

(optional) The resources affected by this work request.

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'CANCELLED', 'CANCELLING', 'FAILED', 'INPROGRESS', 'SUCCEEDED'

`time_accepted`

(optional) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_dataflow_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_COLLECTION_T Type

Results of a query for a list of work requests. Contains WorkRequestSummary items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work requests

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_T Type

A Data Flow work request error object.

Syntax
```

```

Fields

Field Description

`code`

(required) A Machine-usable code for the error that occured.

`id`

(optional) The id of a work request error.

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

`work_requestid`

(optional) The OCID of a work request.

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_dataflow_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_COLLECTION_T Type

Results of a query for a list of work request errors. Contains WorkRequestError items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request errors.

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_T Type

A Data Flow work request log object.

Syntax
```

```

Fields

Field Description

`id`

(optional) The id of a work request log.

`message`

(required) A human readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

`work_requestid`

(optional) The OCID of a work request.

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_TBL Type

Nested table type of dbms_cloud_oci_dataflow_work_request_log_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_COLLECTION_T Type

Results of a query for a list of work request logs. Contains WorkRequestLog items.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of work request logs.

- [Data Flow Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-C9B7448A-3B54-42CD-9A6B-86E40626E821)
- [DBMS_CLOUD_OCI_DATAFLOW_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-3B1ECF57-9CAC-4872-8B2C-6AD82CAB0393)
- [DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_LOG_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-E1970966-3217-4C35-835E-5650C9146CFA)
- [DBMS_CLOUD_OCI_DATAFLOW_SHAPE_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-40291DFB-12AF-449F-9B98-3CA022CEDF4A)
- [DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_PARAMETER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-B1050B80-25F0-4E6D-83CA-433E3FCD9C1F)
- [DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_PARAMETER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-45553181-0593-466B-B342-13A22D91782A)
- [DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-A9C90DC5-1694-4E98-9143-391C4EF3B50F)
- [DBMS_CLOUD_OCI_DATAFLOW_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-AE1B1A2B-6A60-41D1-866B-EFAB69EF13E4)
- [DBMS_CLOUD_OCI_DATAFLOW_CHANGE_APPLICATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-6A7F2E34-C727-4E91-AF49-4530C47F1FD3)
- [DBMS_CLOUD_OCI_DATAFLOW_CHANGE_POOL_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-92AADD97-DFA0-4D22-972A-FB197719218B)
- [DBMS_CLOUD_OCI_DATAFLOW_CHANGE_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-6D2D6C30-1C9F-461D-87CC-479E2225A298)
- [DBMS_CLOUD_OCI_DATAFLOW_CHANGE_RUN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-FC9D6023-2CD3-4400-8452-90088EFE9BCA)
- [DBMS_CLOUD_OCI_DATAFLOW_CHANGE_SQL_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-7ED9E996-6702-422D-BB59-9EE2B00C00BE)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-9C3E5174-DA73-410C-9451-8A74D6409741)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-6E3F6FC6-35DF-42C4-8A06-56D6A3791A1A)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_SCHEDULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-E175F2C5-50C5-4AED-9838-5740C4AAAF55)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_CONFIG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-34C3CDB4-86C7-4DED-89B1-96C7AF3AE633)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_SCHEDULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-0EBC9672-72B5-4128-ADAB-B96D04305ABE)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-C7942596-8434-48F4-BD47-69DF2DCF82B6)
- [DBMS_CLOUD_OCI_DATAFLOW_SCAN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-F8F70B9C-BD4F-49C1-918E-66DD8F592F5B)
- [DBMS_CLOUD_OCI_DATAFLOW_SCAN_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-4F3482F4-4166-4FFF-8765-30E1ABE687AD)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-E2343FC1-760B-4F80-80E3-E4AEA583085D)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-7DAD926B-9CFF-4CD4-9321-B91D2DD370C5)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_NETWORK_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-ABFDF1ED-C68A-4A14-8594-5DBA22701917)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_SQL_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-423E4E6E-7F5A-4AE5-A461-D99D152E317F)
- [DBMS_CLOUD_OCI_DATAFLOW_CREATE_STATEMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-C41112CD-68D2-412D-B150-24D6930E414F)
- [DBMS_CLOUD_OCI_DATAFLOW_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-AAE5193D-3D7D-4E03-938B-9DAB07E30503)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_OUTPUT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-4A47B209-7E6F-4D2D-B887-B88ADBD11265)
- [DBMS_CLOUD_OCI_DATAFLOW_IMAGE_PNG_STATEMENT_OUTPUT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-2FCC176D-CFEA-4C78-B23D-4155B08A9C0A)
- [DBMS_CLOUD_OCI_DATAFLOW_NODE_COUNT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-BD581F02-9129-4C37-B79F-C445522ED276)
- [DBMS_CLOUD_OCI_DATAFLOW_NODE_COUNT_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-D8F8E118-2FA4-40F3-A3CE-2099664F9ED3)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_METRICS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-37EB7D29-8984-4BDF-BBC8-0CBEE22E3E7F)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-94BAB9D8-0051-423B-8BA2-CFC07D847FD2)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-789E22CE-04C1-4B7C-8998-894FB67B3D12)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-A833B76D-31FE-493F-AF60-876790453712)
- [DBMS_CLOUD_OCI_DATAFLOW_POOL_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-F50C104C-E953-4B4E-80A1-D539E95E056B)
- [DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-8DE17BBA-EE76-4C13-8D17-85182154CABC)
- [DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-B6E77C7E-FF7A-4FC3-99AB-F0E5F9D7C0E2)
- [DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-FF6341A5-54F0-4CCA-8A23-B946624CE751)
- [DBMS_CLOUD_OCI_DATAFLOW_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-9AA19037-F979-4A1C-A93C-FBC73225B67C)
- [DBMS_CLOUD_OCI_DATAFLOW_RUN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-507D541F-237A-419A-9574-53E28206BE61)
- [DBMS_CLOUD_OCI_DATAFLOW_RUN_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-3AE95F1D-304F-4736-884D-11FD6AFD27CF)
- [DBMS_CLOUD_OCI_DATAFLOW_RUN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-A2F30883-63E8-4DD2-AC3F-F79B334C2E3D)
- [DBMS_CLOUD_OCI_DATAFLOW_SECURE_ACCESS_CONTROL_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-F5AFE1C7-B430-4F41-B8B9-C82FA43B7F67)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-01C409C2-80F5-4409-814F-DF208C33E0E1)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-E0A51C16-194D-4620-AD06-3DF127F597DD)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-34E5F363-07FC-4F16-AC11-8EB030DF98CF)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-644F9657-D910-4791-8162-EFD96AA6E310)
- [DBMS_CLOUD_OCI_DATAFLOW_SECURE_ACCESS_CONTROL_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-90C3022A-497C-4A23-9AE3-1008D1499706)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_SECURE_ACCESS_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-5721312B-F0D6-4AAB-A0A6-D4716C2B23C6)
- [DBMS_CLOUD_OCI_DATAFLOW_SQL_ENDPOINT_VCN_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-014853ED-A5EF-46AA-8214-E5237C0EA299)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_OUTPUT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-753A7725-A56C-4968-BB51-F3618C7B471D)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-CA84A35C-9C6C-484F-AA53-4A7311AE0254)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-887CC31F-1C6D-4426-9651-DE1711E9EB51)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-DE5B5151-83F4-4321-9DD6-9F81F8BDC74B)
- [DBMS_CLOUD_OCI_DATAFLOW_STATEMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-8FE27640-95C1-49F1-A192-ED2AEA440BC0)
- [DBMS_CLOUD_OCI_DATAFLOW_TEXT_HTML_STATEMENT_OUTPUT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-C5B21C32-C282-4995-A23F-52AA82B208A7)
- [DBMS_CLOUD_OCI_DATAFLOW_TEXT_PLAIN_STATEMENT_OUTPUT_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-4769407F-BC09-427F-BB6C-1C8654E97342)
- [DBMS_CLOUD_OCI_DATAFLOW_UPDATE_APPLICATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-97C5AE70-7758-4A30-9A97-7CAD38D64C71)
- [DBMS_CLOUD_OCI_DATAFLOW_UPDATE_POOL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-785EE934-2670-4267-8728-86CFB618DB5C)
- [DBMS_CLOUD_OCI_DATAFLOW_UPDATE_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-29DF0C3B-511C-45C7-97DB-41741C74A8EF)
- [DBMS_CLOUD_OCI_DATAFLOW_UPDATE_RUN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-B5FE526A-9285-4FE3-87A8-B929C00D4E44)
- [DBMS_CLOUD_OCI_DATAFLOW_UPDATE_SQL_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-7CDE9D91-7AA7-4EA4-8F5A-4ED9EFC7467F)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-8E71CCBE-78FB-4AAD-9C6E-8C8AE6EDE1AB)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-3962C7BE-F793-4962-90B2-D34CB9DEABBF)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-8BC23A78-552A-4F1D-850D-01B89D43E8D2)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-C866A7E5-B928-4C03-AA18-F9F5A8592A96)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-DDD1A09A-D071-4AC7-ABEB-072E15827F57)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-80288446-93ED-49D8-9037-7AA015474F21)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-44888A01-1688-4DB7-8D50-4D2C08CFFE0A)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-00D22C9E-6D36-444A-B88C-6311FA685E29)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-41E04564-9FFB-4DC0-9075-8E8F3AA8B578)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-940BE7C3-6172-4DA8-9D7E-690441513B7A)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-DE732483-081F-4BB6-98CC-6C4C4697A158)
- [DBMS_CLOUD_OCI_DATAFLOW_WORK_REQUEST_LOG_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dataflow_t.html#ADSDK-GUID-6B73A597-654D-4B6C-ABD7-46EF81D5C0F1)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
