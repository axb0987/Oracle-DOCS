# Application Migration Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#dcoc-content-body)

## Application Migration Common Types

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_AUTHORIZATION_DETAILS_T Type

Details of the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. It also contains access credentials.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the source environment from which you are migrating applications to Oracle Cloud Infrastructure.

Allowed values are: 'OCIC', 'INTERNAL_COMPUTE', 'OCC', 'OCIC_IDCS', 'IMPORT'

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CHANGE_COMPARTMENT_DETAILS_T Type

Moves the resource to the specified compartment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the resource to.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_RESOURCE_FIELD_T Type

Resource object that can be used to pass details about any list of resources associated with Migrations. The List of resources are added to ConfigurationField to add the capability to pass lists of resources of any type and group.

Syntax
```

```

Fields

Field Description

`name`

(optional) The display name of the resource field.

`l_group`

(optional) The name of the group to which this field belongs to.

`l_type`

(required) The type of the resource field.

`value`

(required) The value of the field.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_RESOURCE_FIELD_TBL Type

Nested table type of dbms_cloud_oci_application_migration_resource_field_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CONFIGURATION_FIELD_T Type

Provide configuration information about the application in the target environment. Application Migration migrates the application to the target environment only after you provide this information. The information that you must provide varies depending on the type of application that you are migrating.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the configuration field.

`l_group`

(optional) The name of the group to which this field belongs, if any.

`l_type`

(optional) The type of the configuration field.

`value`

(optional) The value of the field.

`description`

(optional) Help text to guide the user in setting the configuration value.

`resource_list`

(optional) A list of resources associated with a specific configuration object.

`is_required`

(optional) Indicates whether or not the field is required (defaults to `true`).

`is_mutable`

(optional) Indicates whether or not the field may be modified (defaults to `true`).

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_DISCOVERY_DETAILS_T Type

Base model for different application discovery requirements.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of application that you want to migrate.

Allowed values are: 'JCS', 'SOACS', 'OIC', 'OAC', 'ICS', 'PCS'

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CREATE_MIGRATION_DETAILS_T Type

While creating a migration, specify the source and the application that you want migrate. Each migration moves a single application from a specified source to a specified Oracle Cloud Infrastructure tenancy. If required, provide the credentials of the application administrator in the source environment. Application Migration uses this information to access the application, as well as discover application artifacts, such as the complete domain configuration along with data sources and other dependencies. You must also assign a name and provide a description for the migration. This helps you to identify the appropriate source environment when you have multiple sources defined. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the source.

`display_name`

(optional) User-friendly name of the application. This will be the name of the migrated application in Oracle Cloud Infrastructure.

`description`

(optional) Description of the application that you are migrating.

`source_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`application_name`

(required) Name of the application that you want to migrate from the source environment.

`discovery_details`

(required)

`pre_created_target_database_type`

(optional) The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.

Allowed values are: 'DATABASE_SYSTEM', 'NOT_SET'

`is_selective_migration`

(optional) If set to `true`, Application Migration migrates the application resources selectively depending on the source.

`service_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`application_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_DETAILS_T Type

Specify one of the following values depending for the 'type' attribute based on the application that you want to migrate. Specify `OCIC` if you want to migrate Oracle Java Cloud Service, Oracle Analytics Cloud - Classic, Oracle Integration, and Oracle SOA Cloud Service applications from Oracle Cloud Infrastructure - Classic. Specify `INTERNAL_COMPUTE` if you have a traditional Oracle Cloud Infrastructure - Classic account and you want to migrate Oracle Process Cloud Service or Oracle Integration Cloud Service applications. Specify `OCC` if you want to migrate applications from Oracle Cloud@Customer.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of source environment.

Allowed values are: 'OCIC', 'INTERNAL_COMPUTE', 'OCC', 'OCIC_IDCS', 'IMPORT'

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CREATE_SOURCE_DETAILS_T Type

The configuration details for creating a source. When you create a source, provide the required information to let Application Migration access the source environment. You must also assign a name and provide a description for the source. This helps you to identify the appropriate source environment when you have multiple sources defined. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the source.

`display_name`

(optional) Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`description`

(optional) Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`source_details`

(required)

`authorization_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_ERROR_T Type

Error that occurs during the execution of a request. It contains an error code and message which you can use to troubleshoot an API request failure.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. For more information, see[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A user-friendly error string.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_ICS_DISCOVERY_DETAILS_T Type

Credentials to access the Oracle Integration Cloud Service application in the source environment. Application Migration connects to the application in the source environment with the supplied credentials.

Syntax
```

```

`dbms_cloud_oci_application_migration_ics_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`service_instance_user`

(required) Application administrator username to access the Oracle Integration Cloud Service application in the source environment.

`service_instance_password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_IMPORT_MANIFEST_T Type

Manifest describing details about an import source

Syntax
```

```

Fields

Field Description

`version`

(optional) the version of the export tool that was used to generate the manifest

`export_type`

(optional) the type of application that the export tool was executed against to generate this manifest

`export_details`

(optional) application specific details as parsed from various sources of the application that was exported

`l_timestamp`

(optional) when this manifest was generated

`md5`

(optional) the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest

`signature`

(optional) a sha1 hash of all the fields of this manifest (excluding the signature)

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_IMPORT_SOURCE_DETAILS_T Type

/ Basic details about the source, import manifest and object storage bucket as well as object name of the archive that should be used during import

Syntax
```

```

`dbms_cloud_oci_application_migration_import_source_details_t`is a subtype of the`dbms_cloud_oci_application_migration_source_details_t`type.

Fields

Field Description

`manifest`

(required)

`namespace`

(required) the object storage namespace where the bucket and uploaded object resides

`bucket`

(required) the bucket wherein the export archive exists in object storage

`object_name`

(required) the name of the archive as it exists in object storage

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_INTERNAL_AUTHORIZATION_DETAILS_T Type

Credentials to access Oracle Cloud Infrastructure - Classic, which is the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_internal_authorization_details_t`is a subtype of the`dbms_cloud_oci_application_migration_authorization_details_t`type.

Fields

Field Description

`username`

(required) User with Compute Operations role in Oracle Cloud Infrastructure - Classic.

`password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_INTERNAL_SOURCE_DETAILS_T Type

Details about the Oracle Cloud Infrastructure - Classic account, the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_internal_source_details_t`is a subtype of the`dbms_cloud_oci_application_migration_source_details_t`type.

Fields

Field Description

`account_name`

(required) The identity domain ID of your traditional Oracle Cloud Infrastructure - Classic account.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_JCS_DISCOVERY_DETAILS_T Type

Credentials to access the Oracle Java Cloud Service application in the source environment. When you create and update a migration, Application Migration connects to the application in the source environment with the supplied credentials and exports the domain configuration.

Syntax
```

```

`dbms_cloud_oci_application_migration_jcs_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`weblogic_user`

(required) WebLogic administrator username for the Oracle Java Cloud Service application in the source environment.

`weblogic_password`

(required) The password of the WebLogic administrator for the Oracle Java Cloud Service application in the source environment.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_MIGRATION_T Type

The properties that define a migration. A migration represents the end-to-end workflow of moving an application from a source environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure. For more information, see[Manage Migrations](https://docs.oracle.com/iaas/application-migration/manage_migrations.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the migration.

`display_name`

(optional) User-friendly name of the migration.

`description`

(optional) Description of the migration.

`time_created`

(optional) The date and time at which the migration was created, in the format defined by RFC3339.

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source with which this migration is associated.

`application_name`

(optional) Name of the application which is being migrated. This is the name of the application in the source environment.

`application_type`

(optional) The type of application being migrated.

Allowed values are: 'JCS', 'SOACS', 'OIC', 'OAC', 'ICS', 'PCS'

`pre_created_target_database_type`

(optional) The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.

Allowed values are: 'DATABASE_SYSTEM', 'NOT_SET'

`is_selective_migration`

(optional) If set to `true`, Application Migration migrates only the application resources that you specify. If set to `false`, Application Migration migrates the entire application. When you migrate the entire application, all the application resources are migrated to the target environment. You can selectively migrate resources only for the Oracle Integration Cloud and Oracle Integration Cloud Service applications.

`service_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`application_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`lifecycle_state`

(optional) The current state of the migration.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'SUCCEEDED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) Details about the current lifecycle state of the migration.

`migration_state`

(optional) The current state of the overall migration process.

Allowed values are: 'DISCOVERING_APPLICATION', 'DISCOVERY_FAILED', 'MISSING_CONFIG_VALUES', 'READY', 'MIGRATING', 'MIGRATION_FAILED', 'MIGRATION_SUCCEEDED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_MIGRATION_SUMMARY_T Type

Details about the migration. Each migration moves a single application from a specified source to Oracle Cloud Infrastructure.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the migration.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the migration.

`display_name`

(optional) User-friendly name of the migration.

`description`

(optional) Description of the migration.

`time_created`

(optional) The date and time at which the migration was created, in the format defined by RFC3339.

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`application_name`

(optional) Name of the application which is being migrated from the source environment.

`application_type`

(optional) The type of application being migrated.

Allowed values are: 'JCS', 'SOACS', 'OIC', 'OAC', 'ICS', 'PCS'

`lifecycle_state`

(optional) The current state of the migration.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'SUCCEEDED', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) Details about the current lifecycle state.

`migration_state`

(optional) The current state of the overall migration process.

Allowed values are: 'DISCOVERING_APPLICATION', 'DISCOVERY_FAILED', 'MISSING_CONFIG_VALUES', 'READY', 'MIGRATING', 'MIGRATION_FAILED', 'MIGRATION_SUCCEEDED'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OAC_DISCOVERY_DETAILS_T Type

Details about the Oracle Analytics Cloud - Classic application in the source environment.

Syntax
```

```

`dbms_cloud_oci_application_migration_oac_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`service_instance_user`

(required) This field is currently not supported. You must enter a value, such as &lt;code&gt;unused&lt;/code&gt;. However, the value that you enter is ignored.

`service_instance_password`

(required) This field is currently not supported. You must enter a value, such as &lt;code&gt;unused&lt;/code&gt;. However, the value that you enter is ignored.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCC_AUTHORIZATION_DETAILS_T Type

Credentials to access Oracle Cloud@Customer, which is the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_occ_authorization_details_t`is a subtype of the`dbms_cloud_oci_application_migration_authorization_details_t`type.

Fields

Field Description

`username`

(required) User with Compute Operations role in Oracle Cloud@Customer.

`password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCC_SOURCE_DETAILS_T Type

Details about the Oracle Cloud@Customer account, the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_occ_source_details_t`is a subtype of the`dbms_cloud_oci_application_migration_source_details_t`type.

Fields

Field Description

`compute_account`

(required) If you are using an Oracle Cloud@Customer account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud@Customer Compute service entitlement, then enter 567890123.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_AUTHORIZATION_DETAILS_T Type

Credentials to access Oracle Cloud Infrastructure - Classic, which is the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_ocic_authorization_details_t`is a subtype of the`dbms_cloud_oci_application_migration_authorization_details_t`type.

Fields

Field Description

`username`

(required) User with Compute Operations role in Oracle Cloud Infrastructure - Classic.

`password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_AUTHORIZATION_TOKEN_DETAILS_T Type

Auth Token and endpoint to access Oracle Cloud Infrastructure - Classic, which is the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_ocic_authorization_token_details_t`is a subtype of the`dbms_cloud_oci_application_migration_authorization_details_t`type.

Fields

Field Description

`client_app_url`

(required) AuthClient app url resource that the accesstoken is for.

`access_token`

(required) AccessToken to access the app endpoint.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_SOURCE_DETAILS_T Type

Details about the Oracle Cloud Infrastructure Classic account, the source environment from which you want to migrate the application.

Syntax
```

```

`dbms_cloud_oci_application_migration_ocic_source_details_t`is a subtype of the`dbms_cloud_oci_application_migration_source_details_t`type.

Fields

Field Description

`l_region`

(required) The Oracle Cloud Infrastructure - Classic region from which you want to migrate your applications. For example, uscom-east-1 or uscom-central-1.

`compute_account`

(required) If you are using an Oracle Cloud Infrastructure - Classic account with Identity Cloud Service (IDCS), enter the service instance ID. For example, if Compute-567890123 is the account name of your Oracle Cloud Infrastructure Classic Compute service entitlement, then enter 567890123. If you are using a traditional Oracle Cloud Infrastructure - Classic account, enter your identity domain ID.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OIC_DISCOVERY_DETAILS_T Type

Credentials to access the Oracle Integration application in the source environment. Application Migration connects to the application in the source environment with the supplied credentials.

Syntax
```

```

`dbms_cloud_oci_application_migration_oic_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`service_instance_user`

(required) Application administrator username to access the Oracle Integration Classic instance in the source environment.

`service_instance_password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_PCS_DISCOVERY_DETAILS_T Type

Credentials to access the Oracle Process Cloud Service application in the source environment. Application Migration connects to the application in the source environment with the supplied credentials.

Syntax
```

```

`dbms_cloud_oci_application_migration_pcs_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`service_instance_user`

(required) Application administrator username to access the Oracle Process Cloud Service application in the source environment.

`service_instance_password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOACS_DISCOVERY_DETAILS_T Type

Credentials to access the Oracle SOA Cloud Service application in the source environment. When you create and update a migration, Application Migration connects to the application in the source environment with the supplied credentials and exports the domain configuration.

Syntax
```

```

`dbms_cloud_oci_application_migration_soacs_discovery_details_t`is a subtype of the`dbms_cloud_oci_application_migration_discovery_details_t`type.

Fields

Field Description

`weblogic_user`

(required) WebLogic administrator username for the Oracle SOA Cloud Service application in the source environment.

`weblogic_password`

(required) Password for this user.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_T Type

The properties that define a source. Source refers to the source environment from which you migrate an application to Oracle Cloud Infrastructure. For more information, see[Manage Sources](https://docs.oracle.com/iaas/application-migration/manage_sources.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the source.

`display_name`

(optional) Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`description`

(optional) Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`time_created`

(optional) The date and time at which the source was created, in the format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the source.

Allowed values are: 'CREATING', 'DELETING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETED'

`lifecycle_details`

(optional) Details about the current lifecycle state of the source.

`source_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_APPLICATION_T Type

Details about an application running in the source environment that you can migrate to Oracle Cloud Infrastructure.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the application.

`l_type`

(optional) The type of application.

Allowed values are: 'JCS', 'SOACS', 'OIC', 'OAC', 'ICS', 'PCS'

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source to which the application belongs.

`version`

(optional) The version of the application.

`state`

(optional) The current state of the application.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_APPLICATION_SUMMARY_T Type

The properties that define an application, that is running in the source environment and which can be migrated to Oracle Cloud Infrastructure.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the application.

`l_type`

(optional) The type of the application.

Allowed values are: 'JCS', 'SOACS', 'OIC', 'OAC', 'ICS', 'PCS'

`source_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source to which the application belongs.

`version`

(optional) The version of the application.

`state`

(optional) The current state of the application.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_SUMMARY_T Type

Details of the source. In Application Migration, a source refers to the environment from which the application is migrated to Oracle Cloud Infrastructure.

Syntax
```

```

Fields

Field Description

`id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the source.

`l_type`

(optional) The type of source environment.

Allowed values are: 'OCIC', 'INTERNAL_COMPUTE', 'OCC', 'OCIC_IDCS', 'IMPORT'

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the source.

`display_name`

(optional) Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`description`

(optional) Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`time_created`

(optional) The date and time at which the source was created, in the format defined by RFC3339.

`lifecycle_state`

(optional) The current state of the source.

Allowed values are: 'CREATING', 'DELETING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETED'

`lifecycle_details`

(optional) Details about the current lifecycle state of the source.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_UPDATE_MIGRATION_DETAILS_T Type

Provide configuration information about the application in the target environment. Application Migration migrates the application to the target environment only after you provide this information. The information that you must provide varies depending on the type of application that you are migrating. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) User-friendly name of the migration.

`description`

(optional) Description of the migration.

`discovery_details`

(optional)

`is_selective_migration`

(optional) If set to `true`, Application Migration migrates the application resources selectively depending on the source.

`service_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`application_config`

(optional) Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_UPDATE_SOURCE_DETAILS_T Type

You can update the authorization details to access the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. You can also update the description and tags of a source.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`description`

(optional) Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.

`source_details`

(optional)

`authorization_details`

(optional)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_RESOURCE_T Type

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

(required) The resource type that the work request affects, source or migration.

`identifier`

(required) An[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)or other unique identifier for the resource.

`entity_uri`

(optional) The URI path that you can use for a GET request to access the resource metadata.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_application_migration_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_SOURCE', 'UPDATE_SOURCE', 'DELETE_SOURCE', 'CREATE_MIGRATION', 'UPDATE_MIGRATION', 'DELETE_MIGRATION', 'AUTHORIZE_SOURCE', 'DISCOVER_APPLICATION', 'MIGRATE_APPLICATION', 'CHANGE_SOURCE_COMPARTMENT', 'CHANGE_MIGRATION_COMPARTMENT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) The percentage completion of the operation relative to the total amount of work that is tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_ERROR_T Type

An error encountered while executing an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A user-friendly error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_LOG_ENTRY_T Type

A log message about the execution of an operation that is tracked by a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A user-friendly log message.

`l_timestamp`

(required) The time the log message was written.

### DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_SOURCE', 'UPDATE_SOURCE', 'DELETE_SOURCE', 'CREATE_MIGRATION', 'UPDATE_MIGRATION', 'DELETE_MIGRATION', 'AUTHORIZE_SOURCE', 'DISCOVER_APPLICATION', 'MIGRATE_APPLICATION', 'CHANGE_SOURCE_COMPARTMENT', 'CHANGE_MIGRATION_COMPARTMENT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing this work request.

`percent_complete`

(required) The percentage completion of the operation tracked by this work request.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

- [Application Migration Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-5EA9486F-F35C-4E1A-B533-DFDBE041E8F1)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-3009571E-1703-45A0-B2E9-396F54C5087A)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_AUTHORIZATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-B962EDD5-D3AB-4326-9D2D-E1F3DEEE5F1B)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CHANGE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-CCCF9BA2-D02A-4EB2-AF54-A4B5466035FC)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_RESOURCE_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-05DF7945-82C8-4913-AD3D-3D9970DF51D7)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_RESOURCE_FIELD_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-C3E9BD73-08D4-4990-8E30-825C0227A4EB)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CONFIGURATION_FIELD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-904BF7B4-B66A-4BD1-9FAB-F418C2A86555)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-5BEAFA91-E143-4AF6-A6BA-41CE7C97DBBA)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CREATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-4DFE4AD3-A778-4B54-9A73-A27D727B9CC2)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-E9B9ACBA-573C-489B-947A-119A6A7143B4)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_CREATE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-C041933C-B8FE-4DB8-8BFD-4B595F3112E4)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-B726DC03-B1CB-4283-BCF7-1662EFCADD99)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_ICS_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-C463C49D-0A49-4C6F-996F-D4791813A1F0)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_IMPORT_MANIFEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-EBC842A7-F21C-4E20-A4E9-623A1569EEC6)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_IMPORT_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-1D391620-4783-4B6C-9422-22B18AE928D7)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_INTERNAL_AUTHORIZATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-6697F961-1C8D-412B-92F5-FC8485DB439D)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_INTERNAL_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-7FC0D587-51C5-468C-9173-09DD4A83311A)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_JCS_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-7CCECDAA-0FA1-4396-B982-7FD344BF6DC4)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_MIGRATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-32E5788A-8342-4E77-9D9E-2C96F9EFAB32)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_MIGRATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-70E47592-69EC-4200-87A1-F33E5A87E9C3)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OAC_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-6B74E2EB-480C-4041-A4D5-39BC3B7C585B)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCC_AUTHORIZATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-B4D489AA-7A21-46CE-B940-72E38293370D)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCC_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-8D5F5232-B890-40E7-A72F-EF7EC8469671)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_AUTHORIZATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-A66B1073-A5E7-4B40-BCC8-64DFBC92402F)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_AUTHORIZATION_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-02F22FB8-5381-426A-8F19-59AC959473AE)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OCIC_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-A59CE161-A604-48CD-BAB5-C0253A3F3F51)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_OIC_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-C5C3C0A5-7621-40D1-9692-9E5F7B84B9F7)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_PCS_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-43BB98EA-7318-46AE-B30D-039C429C2029)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOACS_DISCOVERY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-79B00D8B-D6DE-4A4E-BED9-C4EE222A9B63)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-5298B27B-3E0C-4CA8-A516-3F2C6D65AF77)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_APPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-1002C6DE-674F-4315-A130-1F97E92AA89E)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_APPLICATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-7B8E1436-1868-42F1-B29A-A9EAB1978B3C)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_SOURCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-7D4CD7E0-9C40-4757-8C96-DF0F7D617D35)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_UPDATE_MIGRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-8FFC9D32-661A-4CA8-8D89-DF129567E1D0)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_UPDATE_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-D15C7A9B-2892-464A-A0B4-41088E1C5D51)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-5E45539B-0730-475A-9CEE-5047DBEBF1DE)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-A36BA138-22E6-49EF-B23A-7424E8CBE4B0)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-CE8EAA66-98E2-4A7E-AB5E-85FD36CE0B74)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-7889BE7A-5DD8-4CA4-9039-6B4B2688CBD3)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-A35B54FE-EC0F-4C7A-B8A3-7DB5E1858A0E)
- [DBMS_CLOUD_OCI_APPLICATION_MIGRATION_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/application_migration_t.html#ADSDK-GUID-03A6E900-A969-4915-87D9-D2B1D8375ED9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
