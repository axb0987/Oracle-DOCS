# Database Tools Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html
- Fetched: 2026-09-05 19:02 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#dcoc-content-body)

## Database Tools Common Types

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_ADD_RESOURCE_LOCK_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CHANGE_DATABASE_TOOLS_CONNECTION_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the `DatabaseToolsConnection` to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the `DatabaseToolsConnection` to.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CHANGE_DATABASE_TOOLS_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type

Contains the details for the compartment to move the Database Tools private endpoint to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment to move the `DatabaseConnectionProfile` to.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_RESOURCE_LOCK_T Type

Resource locks are used to prevent certain APIs from being called for the resource. A full lock prevents both updating the resource and deleting the resource. A delete lock prevents deleting the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_RESOURCE_LOCK_TBL Type

Nested table type of dbms_cloud_oci_database_tools_resource_lock_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type

Details for the new Database Tools connection.

Syntax
```

```

Fields

Field Description

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools connection.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`locks`

(optional) Locks associated with this resource.

`l_type`

(required) The DatabaseToolsConnection type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

`runtime_support`

(optional) Specifies whether this connection is supported by the Database Tools Runtime.

Allowed values are: 'SUPPORTED', 'UNSUPPORTED'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_DETAILS_T Type

The user password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the user password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_DETAILS_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_DETAILS_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_DETAILS_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO', 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_generic_jdbc_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_DETAILS_T Type

Details of the new Database Tools connection for a Generic JDBC database system.

Syntax
```

```

`dbms_cloud_oci_database_tools_create_database_tools_connection_generic_jdbc_details_t`is a subtype of the`dbms_cloud_oci_database_tools_create_database_tools_connection_details_t`type.

Fields

Field Description

`url`

(required) The JDBC URL used to connect to the Generic JDBC database system.

`user_name`

(required) The user name.

`user_password`

(required)

`advanced_properties`

(optional) The advanced connection properties key-value pair.

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'MYSQLDBSYSTEM'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_DETAILS_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_DETAILS_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_DETAILS_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_my_sql_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type

Details of the new Database Tools connection for a MySQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_create_database_tools_connection_my_sql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_create_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the MySQL Server.

`user_name`

(required) The user name.

`user_password`

(required)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'AUTONOMOUSDATABASE', 'DATABASE', 'PLUGGABLEDATABASE'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_DETAILS_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_DETAILS_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_DETAILS_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_DETAILS_T Type

The proxy client information.

Syntax
```

```

Fields

Field Description

`proxy_authentication_type`

(required) The proxy authentication type.

Allowed values are: 'USER_NAME', 'NO_PROXY'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type

Details of the new Database Tools connection for an Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_tools_create_database_tools_connection_oracle_database_details_t`is a subtype of the`dbms_cloud_oci_database_tools_create_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connect descriptor or Easy Connect Naming method use to connect to the database.

`user_name`

(required) The database user name.

`user_password`

(required)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `oracle.net.ssl_server_dn_match`).

`key_stores`

(optional) Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

`proxy_client`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'POSTGRESQLDBSYSTEM'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_DETAILS_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_DETAILS_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_DETAILS_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_postgresql_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type

Details of the new Database Tools connection for a PostgreSQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_create_database_tools_connection_postgresql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_create_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the PostgreSQL Server.

`user_name`

(required) The user name.

`user_password`

(required)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT_DETAILS_T Type

The details for the new Database Tools private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools private endpoint.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`locks`

(optional) Locks associated with this resource.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the Database Tools private endpoint.

`endpoint_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `DatabaseToolsEndpointService`.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that the private endpoint belongs to.

`private_endpoint_ip`

(optional) The private IP address that represents the access point for the associated endpoint service.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the private endpoint's VNIC belongs to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_T Type

Description of the Database Tools connection.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools connection.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools connection.

`lifecycle_state`

(required) The current state of the Database Tools connection.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, this message can be used to provide actionable information for a resource in the Failed state.

`time_created`

(required) The time the Database Tools connection was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the DatabaseToolsConnection was updated. An RFC3339 formatted datetime string.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`locks`

(optional) Locks associated with this resource.

`l_type`

(required) The Database Tools connection type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

`runtime_support`

(required) Specifies whether this connection is supported by the Database Tools Runtime.

Allowed values are: 'SUPPORTED', 'UNSUPPORTED'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_SUMMARY_T Type

Summary of the Database Tools connection.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `DatabaseToolsConnection`.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools connection.

`lifecycle_state`

(required) The current state of the Database Tools connection.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`time_created`

(required) The time the Database Tools connection was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the Database Tools connection was updated. An RFC3339 formatted datetime string.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`locks`

(optional) Locks associated with this resource.

`l_type`

(required) The Database Tools connection type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

`runtime_support`

(required) Specifies whether this connection is supported by the Database Tools Runtime.

Allowed values are: 'SUPPORTED', 'UNSUPPORTED'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_COLLECTION_T Type

List of `DatabaseToolsConnectionSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of `DatabaseToolsConnectionSummary` items.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_T Type

The user password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the user password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO', 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_generic_jdbc_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_T Type

Database Tools connection of a Generic JDBC database system.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_generic_jdbc_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_t`type.

Fields

Field Description

`url`

(required) The JDBC URL used to connect to the Generic JDBC database system.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair.

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SUMMARY_T Type

The user password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the user password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_SUMMARY_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_SUMMARY_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_SUMMARY_T Type

The summary of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO', 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_generic_jdbc_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_SUMMARY_T Type

DatabaseToolsConnectionSummary of a Generic JDBC database system.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_generic_jdbc_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_summary_t`type.

Fields

Field Description

`url`

(required) The JDBC URL used to connect to the Generic JDBC database system.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair.

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_T Type

A related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'MYSQLDBSYSTEM'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_my_sql_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_MY_SQL_T Type

Database Tools connection of a MySQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_my_sql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the MySQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (for example, `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_SUMMARY_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_SUMMARY_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_SUMMARY_T Type

The key store secrets.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_my_sql_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_MY_SQL_SUMMARY_T Type

DatabaseToolsConnectionSummary of a MySQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_my_sql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_summary_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the MySQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `DatabaseToolsPrivateEndpoint` used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_T Type

A related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'AUTONOMOUSDATABASE', 'DATABASE', 'PLUGGABLEDATABASE'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_T Type

The proxy client information.

Syntax
```

```

Fields

Field Description

`proxy_authentication_type`

(required) The proxy authentication type.

Allowed values are: 'USER_NAME', 'NO_PROXY'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_T Type

Database Tools connection of an Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connect descriptor or Easy Connect Naming method used to connect to the database.

`user_name`

(optional) The database user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (for example, `oracle.net.ssl_server_dn_match`).

`key_stores`

(optional) The Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

`proxy_client`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_T Type

Represents blank proxy client information.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_no_proxy_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_DETAILS_T Type

Represents blank proxy client information.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_no_proxy_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_SUMMARY_T Type

The proxy client information.

Syntax
```

```

Fields

Field Description

`proxy_authentication_type`

(required) The proxy authentication type.

Allowed values are: 'USER_NAME', 'NO_PROXY'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_SUMMARY_T Type

Represents blank proxy client information.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_no_proxy_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_summary_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_T Type

Proxy client information for user name based proxy authentication.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_user_name_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_t`type.

Fields

Field Description

`user_name`

(required) The user name.

`user_password`

(optional)

`roles`

(optional) A list of database roles for the client. These roles are enabled if the proxy is authorized to use the roles on behalf of the client.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_DETAILS_T Type

Proxy client information for user name based proxy authentication.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_user_name_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_details_t`type.

Fields

Field Description

`user_name`

(required) The user name.

`user_password`

(optional)

`roles`

(optional) A list of database roles for the client. These roles are enabled if the proxy is authorized to use the roles on behalf of the client.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_SUMMARY_T Type

Proxy client information for user name based proxy authentication.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_user_name_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_proxy_client_summary_t`type.

Fields

Field Description

`user_name`

(required) The user name.

`user_password`

(optional)

`roles`

(optional) A list of database roles for the client. These roles are enabled if the proxy is authorized to use the roles on behalf of the client.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SUMMARY_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SUMMARY_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_SUMMARY_T Type

The key store secrets.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'JAVA_KEY_STORE', 'JAVA_TRUST_STORE', 'PKCS12', 'SSO'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_SUMMARY_T Type

DatabaseToolsConnectionSummary of an Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_oracle_database_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_summary_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connect descriptor or Easy Connect Naming method used to connect to the database.

`user_name`

(optional) The database user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `oracle.net.ssl_server_dn_match`).

`key_stores`

(optional) Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `DatabaseToolsPrivateEndpoint` used to access the database in the customer VCN.

`proxy_client`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_T Type

A related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource entity type.

Allowed values are: 'POSTGRESQLDBSYSTEM'

`identifier`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_T Type

The details of the key store.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_postgresql_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_POSTGRESQL_T Type

Database Tools connection of a PostgreSQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_postgresql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the PostgreSQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (for example, `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_SUMMARY_T Type

The key store content.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store content.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_SUMMARY_T Type

The key store password.

Syntax
```

```

Fields

Field Description

`value_type`

(required) The value type of the key store password.

Allowed values are: 'SECRETID'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_SUMMARY_T Type

The key store secrets.

Syntax
```

```

Fields

Field Description

`key_store_type`

(optional) The key store type.

Allowed values are: 'CLIENT_CERTIFICATE_PEM', 'CLIENT_PRIVATE_KEY_PEM', 'CA_CERTIFICATE_PEM'

`key_store_content`

(optional)

`key_store_password`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_key_store_postgresql_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_POSTGRESQL_SUMMARY_T Type

DatabaseToolsConnectionSummary of a PostgreSQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_connection_postgresql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_connection_summary_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(required) The connection string used to connect to the PostgreSQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the `DatabaseToolsPrivateEndpoint` used to access the database in the customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_T Type

Description of Database Tools Endpoint Service.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools Endpoint Service.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`name`

(optional) A unique, non-changeable resource name.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools Endpoint Service.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(required) The time the Database Tools Endpoint Service was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Database Tools Endpoint Service was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(required) The current state of the Database Tools Endpoint Service.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`description`

(optional) A description of the Database Tools Endpoint Service.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_SUMMARY_T Type

Summary of the Database Tools Endpoint Service.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools Endpoint Service.

`display_name`

(required) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`name`

(optional) A unique, non-changeable resource name.

`compartment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools Endpoint Service.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`time_created`

(optional) The time the Database Tools Endpoint Service was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the Database Tools Endpoint Service was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the Database Tools Endpoint Service.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`description`

(optional) A description of the Database Tools Endpoint Service.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_endpoint_service_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_COLLECTION_T Type

List of `DatabaseToolsEndpointServiceSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of `DatabaseToolsEndpointServiceSummary` items.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_DETAILS_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_generic_jdbc_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_generic_jdbc_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_DETAILS_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_generic_jdbc_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_generic_jdbc_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_SUMMARY_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_generic_jdbc_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_generic_jdbc_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_my_sql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_my_sql_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_DETAILS_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_my_sql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_my_sql_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_SUMMARY_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_my_sql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_my_sql_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_postgresql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_postgresql_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_DETAILS_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_postgresql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_postgresql_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_SUMMARY_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_postgresql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_postgresql_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_SUMMARY_T Type

The key store content.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_content_secret_id_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_content_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_DETAILS_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_generic_jdbc_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_generic_jdbc_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_DETAILS_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_generic_jdbc_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_generic_jdbc_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_SUMMARY_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_generic_jdbc_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_generic_jdbc_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_my_sql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_my_sql_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_DETAILS_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_my_sql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_my_sql_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_SUMMARY_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_my_sql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_my_sql_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_postgresql_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_postgresql_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_DETAILS_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_postgresql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_postgresql_details_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_SUMMARY_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_postgresql_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_postgresql_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_SUMMARY_T Type

The key store password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_key_store_password_secret_id_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_key_store_password_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the key store password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTIONS_SOURCE_IP_T Type

Source IP information for reverse connection configuration.

Syntax
```

```

Fields

Field Description

`source_ip`

(optional) The IP address in the customer's VCN to be used as the source IP for reverse connection packets traveling from the customer's VCN to the service's VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTIONS_SOURCE_IP_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_private_endpoint_reverse_connections_source_ip_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTION_CONFIGURATION_T Type

Reverse connection configuration details of the private endpoint.

Syntax
```

```

Fields

Field Description

`reverse_connections_source_ips`

(optional) A list of IP addresses in the customer VCN to be used as the source IPs for reverse connection packets traveling from the service's VCN to the customer's VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_T Type

Description of Database Tools private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the Database Tools private endpoint.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`locks`

(optional) Locks associated with this resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the Database Tools private endpoint.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint.

`endpoint_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools Endpoint Service.

`time_created`

(required) The time the Database Tools private endpoint was created. An RFC3339 formatted datetime string

`time_updated`

(required) The time the Database Tools private endpoint was updated. An RFC3339 formatted datetime string

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN that the private endpoint belongs to.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that the private endpoint belongs to.

`private_endpoint_vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint's VNIC.

`private_endpoint_ip`

(optional) The private IP address that represents the access point for the associated endpoint service.

`endpoint_fqdn`

(optional) Then FQDN to use for the private endpoint.

`additional_fqdns`

(optional) A list of additional FQDNs that can be also be used for the private endpoint.

`lifecycle_state`

(required) The current state of the Database Tools private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the private endpoint's VNIC belongs to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`reverse_connection_configuration`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_SUMMARY_T Type

Summary of the Database Tools private endpoint.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the private endpoint.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`locks`

(optional) Locks associated with this resource.

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the Database Tools private endpoint.

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools private endpoint.

`endpoint_service_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Database Tools Endpoint Service.

`time_created`

(required) The time the Database Tools private endpoint was created. An RFC3339 formatted datetime string.

`time_updated`

(required) The time the Database Tools private endpoint was updated. An RFC3339 formatted datetime string.

`vcn_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the VCN that the private endpoint belongs to.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet that the private endpoint belongs to.

`private_endpoint_vnic_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the private endpoint's VNIC.

`private_endpoint_ip`

(optional) The private IP address that represents the access point for the associated endpoint service.

`endpoint_fqdn`

(optional) Then FQDN to use for the private endpoint.

`additional_fqdns`

(optional) A list of additional FQDNs that can be also be used for the private endpoint.

`lifecycle_state`

(required) The current state of the Database Tools private endpoint.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED', 'INACTIVE'

`lifecycle_details`

(optional) A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the private endpoint's VNIC belongs to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

`reverse_connection_configuration`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_database_tools_private_endpoint_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_COLLECTION_T Type

List of `DatabaseToolsPrivateEndpointSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of `DatabaseToolsPrivateEndpointSummary` items.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_T Type

The user password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_user_password_secret_id_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_user_password_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_DETAILS_T Type

The user password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_user_password_secret_id_details_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_user_password_details_t`type.

Fields

Field Description

`secret_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_SUMMARY_T Type

The user password.

Syntax
```

```

`dbms_cloud_oci_database_tools_database_tools_user_password_secret_id_summary_t`is a subtype of the`dbms_cloud_oci_database_tools_database_tools_user_password_summary_t`type.

Fields

Field Description

`secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the secret containing the user password.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_ERROR_T Type

Error Information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_REMOVE_RESOURCE_LOCK_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The id of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`l_type`

(required) The `DatabaseToolsConnection` type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_DETAILS_T Type

The update details for a Database Tools Generic JDBC database system connection.

Syntax
```

```

`dbms_cloud_oci_database_tools_update_database_tools_connection_generic_jdbc_details_t`is a subtype of the`dbms_cloud_oci_database_tools_update_database_tools_connection_details_t`type.

Fields

Field Description

`url`

(optional) The JDBC URL used to connect to the Generic JDBC database system.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair.

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(optional) The resource entity type.

Allowed values are: 'MYSQLDBSYSTEM'

`identifier`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type

The update details for a Database Tools MySQL Server connection.

Syntax
```

```

`dbms_cloud_oci_database_tools_update_database_tools_connection_my_sql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_update_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(optional) The connection string used to connect to the MySQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(optional) The resource entity type.

Allowed values are: 'AUTONOMOUSDATABASE', 'DATABASE', 'PLUGGABLEDATABASE'

`identifier`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type

The update details for a Database Tools Oracle Database connection.

Syntax
```

```

`dbms_cloud_oci_database_tools_update_database_tools_connection_oracle_database_details_t`is a subtype of the`dbms_cloud_oci_database_tools_update_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(optional) The connect descriptor or Easy Connect Naming method used to connect to the database.

`user_name`

(optional) The database user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `oracle.net.ssl_server_dn_match`).

`key_stores`

(optional) Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

`proxy_client`

(optional)

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_DETAILS_T Type

The related resource

Syntax
```

```

Fields

Field Description

`entity_type`

(optional) The resource entity type.

Allowed values are: 'POSTGRESQLDBSYSTEM'

`identifier`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related resource.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type

The update details for a Database Tools PostgreSQL Server connection.

Syntax
```

```

`dbms_cloud_oci_database_tools_update_database_tools_connection_postgresql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_update_database_tools_connection_details_t`type.

Fields

Field Description

`related_resource`

(optional)

`connection_string`

(optional) The connection string used to connect to the PostgreSQL Server.

`user_name`

(optional) The user name.

`user_password`

(optional)

`advanced_properties`

(optional) The advanced connection properties key-value pair (e.g., `sslMode`).

`key_stores`

(optional) The CA certificate to verify the server's certificate and the client private key and associated certificate required for client authentication.

`private_endpoint_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`display_name`

(optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`description`

(optional) A description of the Database Tools private endpoint.

`nsg_ids`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the network security groups that the private endpoint's VNIC belongs to. For more information about NSGs, see`NETWORK_SECURITY_GROUP`Type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type

Connection validation details.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The `DatabaseToolsConnection` type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type

Connection validation details for the MySQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_my_sql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_RESULT_T Type

Connection validation result.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The Database Tools connection type.

Allowed values are: 'ORACLE_DATABASE', 'MYSQL', 'POSTGRESQL', 'GENERIC_JDBC'

`code`

(required) A short code that defines the result of the validation, meant for programmatic parsing. The value OK indicates that the validation was successful.

`message`

(required) A human-readable message that describes the result of the validation.

`cause`

(optional) A human-readable message that describes possible causes for the validation error.

`action`

(optional) A human-readable message that suggests a remedial action to resolve the validation error.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_RESULT_T Type

Connection validaton result for the MySQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_my_sql_result_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_result_t`type.

Fields

Field Description

`database_name`

(optional) The database name.

`database_version`

(required) The database version.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type

Connection validation details for the Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_oracle_database_details_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_RESULT_T Type

Connection validaton result for the Oracle Database.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_oracle_database_result_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_result_t`type.

Fields

Field Description

`database_name`

(optional) The database name.

`database_version`

(required) The database version.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type

Connection validation details for the PostgreSQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_postgresql_details_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_details_t`type.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_RESULT_T Type

Connection validaton result for the PostgreSQL Server.

Syntax
```

```

`dbms_cloud_oci_database_tools_validate_database_tools_connection_postgresql_result_t`is a subtype of the`dbms_cloud_oci_database_tools_validate_database_tools_connection_result_t`type.

Fields

Field Description

`database_name`

(optional) The database name.

`database_version`

(required) The database version.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can use for a GET operation to access the resource metadata.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_database_tools_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_T Type

An asynchronous work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_DATABASE_TOOLS_CONNECTION', 'UPDATE_DATABASE_TOOLS_CONNECTION', 'DELETE_DATABASE_TOOLS_CONNECTION', 'CREATE_DATABASE_TOOLS_SERVICE_INSTANCE', 'UPDATE_DATABASE_TOOLS_SERVICE_INSTANCE', 'DELETE_DATABASE_TOOLS_SERVICE_INSTANCE', 'CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT', 'UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT', 'DELETE_DATABASE_TOOLS_PRIVATE_ENDPOINT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'WAITING'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_SUMMARY_T Type

A summary of the status of a work request.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The asynchronous operation tracked by this work request.

Allowed values are: 'CREATE_DATABASE_TOOLS_CONNECTION', 'UPDATE_DATABASE_TOOLS_CONNECTION', 'DELETE_DATABASE_TOOLS_CONNECTION', 'CREATE_DATABASE_TOOLS_SERVICE_INSTANCE', 'UPDATE_DATABASE_TOOLS_SERVICE_INSTANCE', 'DELETE_DATABASE_TOOLS_SERVICE_INSTANCE', 'CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT', 'UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT', 'DELETE_DATABASE_TOOLS_PRIVATE_ENDPOINT'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED', 'WAITING'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the work request.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment that contains the work request.

`resources`

(optional) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the work request was created, in the format defined by RFC3339.

`time_started`

(optional) The date and time the work request transitioned from `ACCEPTED` to `IN_PROGRESS`, in the format defined by RFC3339.

`time_finished`

(optional) The date and time the work request reached a terminal state, either `FAILED` or `SUCCEEDED`. Format is defined by RFC3339.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_work_request_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_COLLECTION_T Type

List of `WorkRequestSummary` items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of `WorkRequestSummary` items.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.cloud.oracle.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_database_tools_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_COLLECTION_T Type

List of WorkRequestError items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of Work Request Error items.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_database_tools_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type

List of work request log items.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of work request log items.

- [Database Tools Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-2C1BE110-2F77-4721-A840-9B707B4F43D1)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-9367AF14-1984-4F30-BB90-8E57727AC459)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_ADD_RESOURCE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-14328C33-4AB1-4E04-A058-36C6D86F0445)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CHANGE_DATABASE_TOOLS_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-49F93012-5DC3-4629-BA8B-0162C1BDA5FA)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CHANGE_DATABASE_TOOLS_PRIVATE_ENDPOINT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D42B2043-FF82-4D65-9CA7-992EB18DFFFC)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_RESOURCE_LOCK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F8AC21D7-C89C-4D80-B404-B0C8DF427BE8)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_RESOURCE_LOCK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-83F85A65-B627-403C-B4A5-0F493172DEE3)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-28B36253-4CDA-48BC-8C65-B41B243E8D6B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-58836C08-D4AA-4D91-ABA4-E2CD8CDFE456)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-32F63237-1E70-4EC8-8BB9-641A45BE6BF0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C6426737-51EE-4E93-AB41-B06C01A0CB78)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-3ACF8BAB-9E50-4661-AEED-C9848B298E1E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-AC9FC44E-7098-410C-9459-8008DB3C02E9)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-A6FA5C44-052D-433F-9CBC-AEF26312C558)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-799F868F-C5C2-4488-AD17-B1A7A0EE6705)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-93E3CD64-9A58-435F-856E-759434E5D30F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-7104B114-70D4-4F8D-AAD9-2D588CE0649D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-920915BA-8195-4987-8371-A6CE9BA2FFF8)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-17B5FB75-C446-41F3-BB51-031891C67CE6)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-0DC50946-D7ED-4FC8-BD3F-CA8D611DC740)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-033C6D7D-E07F-4492-8C9A-8AE16BEEAB5D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D7DCF7DA-AB4F-4660-98EF-99DD51A4300B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-80FF6DAA-8EFA-46D8-ABC5-836D745B9B8C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-85026F10-5160-4DF9-9668-73FBA1855112)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-71375055-CD17-445B-BDE8-36C2F97E93EE)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-335A2AD0-BBF8-4EBA-AC15-702FD82B1DD5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-29B92950-1B2F-441C-A0B7-454F61AE6C35)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-581CBE6C-F6CF-435B-8EB5-8F54D4101D7E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-2E0A78E7-191B-405E-9380-00E21D23E22C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-5F28B914-2B30-4E03-B650-C9721342E68E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-379A7646-9190-47D2-BE13-B165DAF493DB)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C454FCB0-F96B-4A7B-8B42-CC402799451A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F9C08750-BD51-4A71-8521-4D48615E4ECD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_CREATE_DATABASE_TOOLS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-11F68597-985B-4FB8-9162-FAB00717BCC1)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-9826F6C6-8BD2-490A-B661-E60972F36D19)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-FE38A891-30EA-4A3D-8DE9-9D878752CE10)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-40D69C16-FEA8-4B34-AD64-BD0079A073FC)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-ECE14346-6CF0-4F75-A92D-E15D0FB6C4A7)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-84507F1B-77A8-4386-A447-4BA894BDD106)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-961DCB69-3224-4B04-A400-4400D37CFA73)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-5D4A7E84-D8DF-4152-A4BE-6DBE8126128F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C9916AA9-34C0-479C-A7F5-AD6B185C702F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F10BE9B6-B587-4F26-9066-705F377C0382)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-60F3F50C-D7F8-4F89-AEC2-FC2E3550C93C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C1F35551-3837-41D1-A3EB-5ED49701970A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-30278F5A-8E8D-4E42-8C88-B3D63B6B6DC0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-B0162082-708E-4B33-90E9-46231D0CCC9A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D834DF7D-4EDC-4B57-8921-78389B873EF4)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_GENERIC_JDBC_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-9CD0B4F5-BD4A-4FD5-9E3C-B35C1F84040B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-E856F9BE-C812-4192-BBBD-403238DC6DE1)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-B3EF68EE-46A5-40EB-B270-6157FE332F26)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-77565CB8-CA82-4B29-9374-BF9412046C60)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-80C7488E-2A0D-4BB5-AEC1-6D0EC0726F0D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D2C8C699-C3D3-461A-AFEE-13D1BE5AB9D0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F5527038-029D-4D90-AA02-2E2335E4B6FB)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-1CA66BE0-2423-43E9-9E7D-039F12456ADD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-654965A8-D4A5-41A3-B7A5-3926AC8CC8CA)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-67416047-87F7-4139-9D15-004B7CC3703B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-16B8E9B0-8B0A-4FEF-8EE3-67495A5A0978)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_MY_SQL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-4289E565-B4A6-4B4D-9984-93D42BB41154)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-66325CB7-F72C-4404-9167-DACD5C45C58F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-105A7CE1-2A50-42AA-8E69-8835F5FDDC27)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-3CA44AAD-8592-4983-8DAD-488B1EA9334E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-DCA6E5E6-0EFE-440F-A153-C6899E3D57DD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D037730D-F7BE-4788-91EC-7911274ADFA4)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-22E66A74-CAA7-4E6C-B117-9EACBD5D131A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-8F52CFBD-932A-4B08-BECF-ADB9CFCD94F3)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D7F514E7-42D3-4126-844C-CBAA46ADE300)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-1F6929F1-130E-4C5B-A2C4-CA61198E7E7D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-58602032-F5A5-40E4-90E3-757B79434ED5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-1913607C-7E95-43B5-9036-D153E9809F70)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_NO_PROXY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-9BCD1AB8-9B5A-45F7-9C7B-0F54A4CDA5CB)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-A380B25E-5D66-4D2C-9B4B-871B81A0876C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-A2AF524B-462A-469C-A782-32D0E4EB13EE)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_PROXY_CLIENT_USER_NAME_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-2F3641EC-6331-4B18-A98B-0826765FEA71)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-277B2C91-98D1-4978-8991-13F745DCBCE7)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-813BF945-BF7C-4FAD-9F56-379F5924D274)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-88EC50C7-778E-438F-8FAB-4C80CD354678)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BB9D8144-2B48-451A-B7B4-9533096C5773)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-4CC45657-D835-431F-B1D6-358AF4D34D09)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-496AECE9-150C-415B-9D2E-A23A859753B5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-7BF9CFE3-CC2C-4DCB-9F2B-940EC8B476F5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-E3CEBC67-A897-44CE-A5D0-923CA2B75B92)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-B68E4A14-3E31-42F5-ABCE-0F18D189F3F1)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-22BBB653-BA59-401D-9C26-889E52DD1568)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BB3B75B1-ECF3-4165-80FB-03D7A6F42DDD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-8E6256F0-8F29-4F5E-890A-6AE713EA1348)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-B54B3C2D-F6BA-4437-AA76-3DC2DB88229D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-DD25BC31-070B-4302-99DB-CDB157650700)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_POSTGRESQL_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F34C1423-7A45-493A-9FE4-15DD26374B7A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_CONNECTION_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-842A81C5-2B33-4905-9195-4FC3AB1021D2)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BF6B78B8-5819-4C6F-9F80-78A327B202F2)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-20886344-CCB7-4D8F-9888-013EA1013B97)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-EB9AFA80-8673-4A69-8205-7FA268AF3087)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_ENDPOINT_SERVICE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-ED79E1BC-57DC-4211-856D-75517BB80B17)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-6E5EE0D9-8084-4E4B-B801-B6B83CE29A2C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-7DDC6381-5701-41C0-A57D-3228A80707D0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-ED7179DF-3085-4EE6-8A01-BB6C125C65AD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C9BDA9B1-3A15-45C2-8851-55E9B22BB775)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-ABDAF0F6-D1C0-4CD4-976A-F5952D1E8D67)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BAD460D7-CC02-4D58-8F7F-BC34CD838264)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BDCEB687-4A7A-4936-82D5-53F9929F74B4)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-6FD49843-D628-4518-8087-CC6B60B75D19)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-E0797CBD-FB79-4034-AFC0-A22E02DEDED6)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-0BA3A0FC-2F01-4DC4-B146-6D9AA21658E0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C3044845-D9D7-45C9-BD17-EC2EA30D664D)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_CONTENT_SECRET_ID_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-986A3D40-130D-41A8-A639-592C5416AA10)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D8240C44-CAF6-4EF1-A08D-0EC652E7B4D2)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-663B8FC9-4A25-40DD-B7A3-B6F054E60E5B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-15FC25D3-7D3C-47B3-BAB3-5D605A20C5DD)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-DA64E9D0-A28A-4D2C-929A-94B33CAEE54E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_GENERIC_JDBC_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-A6663597-B0FC-498B-B47C-12BF2868F692)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-4FC6CA74-C334-4985-BDFE-3A6E9CCBC64F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-AF6CAC04-8E67-456A-8E0A-4605BEE2C092)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_MY_SQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-ED927F47-7B93-4AFA-9500-D21AE4963FA2)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-A12BC315-0C86-4EF3-8E0F-F0084E57A9C9)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-76833632-9201-454E-991B-7120BCF24C29)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_POSTGRESQL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BE340557-A9E6-4814-BE4A-ADF56D6ABEC5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_KEY_STORE_PASSWORD_SECRET_ID_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-DF90FD6B-8A43-4E77-BE41-63C6F1DDFDC2)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTIONS_SOURCE_IP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-25CEED20-07DD-4B95-B930-7E26EEEB789A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTIONS_SOURCE_IP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-50C12296-ACEA-4A16-AFCA-5BBE2B0D3D93)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_REVERSE_CONNECTION_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-FA3B41BE-B658-48AB-AB5D-51E06FD2AD4A)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-5D4B7034-E3BA-4683-9880-5D4E1EC6D23E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-DE9DCE03-FDA3-48BC-A1FC-AA22B4DADD38)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-2A51AFE2-6918-43A5-BE00-B4A4CBDE86CE)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_PRIVATE_ENDPOINT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-250007A6-7EA8-4C33-8994-C7A6498C4579)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-3450F29E-BA82-4D6D-9865-8D3F1C53C3E6)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-B2D94AD8-A27E-4C14-A67E-AFEA7DB23D39)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_DATABASE_TOOLS_USER_PASSWORD_SECRET_ID_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-8E58170B-C208-41CF-B6C9-919C2D3BD859)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-FE6BEA16-CC5A-45CB-9F28-8C7CD9AE762B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_REMOVE_RESOURCE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-88926396-014E-410B-AC8F-C34DB29AAF33)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-BBBF8416-DC65-4C1C-8133-4C0E0A510AF0)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_GENERIC_JDBC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-D25AF95D-E9DA-43E6-A24D-17B883D6CD0B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-902EEC00-BF57-420C-8A45-D80949E271DB)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-5FD2A4E2-F4E9-4AE3-941C-4CD1E44A4891)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-0C9B5C56-9FDC-45AE-946D-4CA3C8321EB1)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-6D4DD150-B230-466E-94D9-782D0C8EAB04)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_RELATED_RESOURCE_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-13E8099D-0ED8-4F5A-B8EF-8CFC1507A869)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-5E683939-2686-4A2D-9BFD-8BF4AD8F4A6C)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_UPDATE_DATABASE_TOOLS_PRIVATE_ENDPOINT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-8312E92E-43F4-4509-AFCE-34F15811A835)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F062AA70-D9FA-4F7F-B5D3-69EB62A066B9)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-42F46AD0-B0A8-47CD-AE72-0369F26F0AE5)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-C83CD67C-1B39-4E27-A627-2340496B0966)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_MY_SQL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-73B12C6F-47AF-4445-B485-A6EE1E95B652)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-8E475CDF-9C35-4B77-B366-89099281DF13)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_ORACLE_DATABASE_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-76F9A50D-806D-42BF-AF81-FD6157667AEB)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-854FA8B0-09B1-4180-98B4-DA4751FD23E3)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_VALIDATE_DATABASE_TOOLS_CONNECTION_POSTGRESQL_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-57FCB776-4710-4F5C-B073-82E2EEB997CE)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-63674365-8D2F-4B1D-B0BD-F18EBC2DDDAA)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F39D1096-44A9-421C-B9C9-2494D2A3DD70)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-04D9576D-D34D-4CC0-BB71-DA8782104E8B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-111D8739-A001-4311-B3A9-E21AF7E5FE02)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-94CE07DB-1DFE-43DF-AAA9-D2D04C1A144F)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-CE343A81-965A-4121-8C34-6D9B45B9A5D8)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-3AB3D1CD-BD53-4998-A3BE-9C14818DF6F9)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-9BE932CA-3FB6-45A9-8941-C925E315D26B)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_ERROR_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-F3EC90EC-E8A2-409B-8443-011CD1B4661E)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-96669C67-1848-436C-9EB5-B605A40AA085)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-2D837481-B02F-4622-8097-452B98F149D3)
- [DBMS_CLOUD_OCI_DATABASE_TOOLS_WORK_REQUEST_LOG_ENTRY_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/database_tools_t.html#ADSDK-GUID-43BB69E5-78F5-454C-9A81-339EB5A194AF)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
