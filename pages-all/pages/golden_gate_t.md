# Golden Gate Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#dcoc-content-body)

## Golden Gate Common Types

### DBMS_CLOUD_OCI_GOLDEN_GATE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_INGRESS_IP_DETAILS_T Type

Private Endpoint IP Addresses created in the customer's subnet. GoldenGate service will use these ingress IP addresses to send all specific requests initiated from the service. These are typically used for accessing customer resources.

Syntax
```

```

Fields

Field Description

`ingress_ip`

(required) A Private Endpoint IPv4 or IPv6 Address created in the customer's subnet.

### DBMS_CLOUD_OCI_GOLDEN_GATE_INGRESS_IP_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_ingress_ip_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_T Type

Represents the metadata description of a connection used by deployments in the same compartment.

Syntax
```

```

Fields

Field Description

`connection_type`

(required) The connection type.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection being referenced.

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`lifecycle_state`

(required) Possible lifecycle states for connection.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(required) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`ingress_ips`

(optional) List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp. Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`routing_method`

(optional) Controls the network traffic direction to the target: SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets. SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

Allowed values are: 'SHARED_SERVICE_ENDPOINT', 'SHARED_DEPLOYMENT_ENDPOINT', 'DEDICATED_ENDPOINT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_KINESIS_CONNECTION_T Type

Represents the metadata of a Amazon Kinesis Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_kinesis_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Kinesis technology type.

Allowed values are: 'AMAZON_KINESIS'

`access_key_id`

(required) Access key ID to access the Amazon Kinesis.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_SUMMARY_T Type

Summary of the Connection.

Syntax
```

```

Fields

Field Description

`connection_type`

(required) The connection type.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection being referenced.

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`lifecycle_state`

(required) Possible lifecycle states for connection.

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(required) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`ingress_ips`

(optional) List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp. Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`routing_method`

(optional) Controls the network traffic direction to the target: SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets. SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

Allowed values are: 'SHARED_SERVICE_ENDPOINT', 'SHARED_DEPLOYMENT_ENDPOINT', 'DEDICATED_ENDPOINT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_KINESIS_CONNECTION_SUMMARY_T Type

Summary of the Amazon Kinesis Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_kinesis_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Kinesis technology type.

`access_key_id`

(required) Access key ID to access the Amazon Kinesis.

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_REDSHIFT_CONNECTION_T Type

Represents the metadata of a Amazon Redshift Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_redshift_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Redshift technology type.

Allowed values are: 'AMAZON_REDSHIFT'

`connection_url`

(required) Connection URL. e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_REDSHIFT_CONNECTION_SUMMARY_T Type

Summary of the Amazon Redshift Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_redshift_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Redshift technology type.

`connection_url`

(required) Connection URL. e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_S3_CONNECTION_T Type

Represents the metadata of a Amazon S3 Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_s3_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon S3 technology type.

Allowed values are: 'AMAZON_S3'

`access_key_id`

(required) Access key ID to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

### DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_S3_CONNECTION_SUMMARY_T Type

Summary of the Amazon S3 Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_amazon_s3_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon S3 technology type.

`access_key_id`

(required) Access key ID to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

### DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_T Type

Represents the metadata of a Azure Data Lake Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_azure_data_lake_storage_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Data Lake Storage technology type.

Allowed values are: 'AZURE_DATA_LAKE_STORAGE'

`authentication_type`

(required) Used authentication mechanism to access Azure Data Lake Storage.

Allowed values are: 'SHARED_KEY', 'SHARED_ACCESS_SIGNATURE', 'AZURE_ACTIVE_DIRECTORY'

`account_name`

(required) Sets the Azure storage account name.

`azure_tenant_id`

(optional) Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 14593954-d337-4a61-a364-9f758c64f97f

`client_id`

(optional) Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d

`endpoint`

(optional) Azure Storage service endpoint. e.g: https://test.blob.core.windows.net

### DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_SUMMARY_T Type

Summary of the Azure Data Lake Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_azure_data_lake_storage_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Data Lake Storage technology type.

`authentication_type`

(required) Used authentication mechanism to access Azure Data Lake Storage.

`account_name`

(required) Sets the Azure storage account name.

`azure_tenant_id`

(optional) Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 14593954-d337-4a61-a364-9f758c64f97f

`client_id`

(optional) Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d

`endpoint`

(optional) Azure Storage service endpoint. e.g: https://test.blob.core.windows.net

### DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_SYNAPSE_CONNECTION_T Type

Represents the metadata of a Azure Synapse Analytics Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_azure_synapse_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Synapse Analytics technology type.

Allowed values are: 'AZURE_SYNAPSE_ANALYTICS'

`connection_string`

(required) JDBC connection string. e.g.: 'jdbc:sqlserver://&lt;synapse-workspace&gt;.sql.azuresynapse.net:1433;database=&lt;db-name&gt;;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_SYNAPSE_CONNECTION_SUMMARY_T Type

Summary of the Azure Synapse Analytics Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_azure_synapse_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Synapse Analytics technology type.

`connection_string`

(required) JDBC connection string. e.g.: 'jdbc:sqlserver://&lt;synapse-workspace&gt;.sql.azuresynapse.net:1433;database=&lt;db-name&gt;;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_DEPLOYMENT_BACKUP_DETAILS_T Type

The information about the Cancel for a DeploymentBackup.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment backup cancel

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about canceling.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deploymentUpgrade cancel.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about snooze canceling.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deploymentUpgrade cancel snooze.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_T Type

Certificate data.

Syntax
```

```

Fields

Field Description

`key`

(required) The identifier key (unique name in the scope of the deployment) of the certificate being referenced. It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`certificate_content`

(required) A PEM-encoded SSL certificate.

`issuer`

(required) The Certificate issuer.

`is_self_signed`

(required) Indicates if the certificate is self signed.

`md5_hash`

(required) The Certificate md5Hash.

`public_key`

(required) The Certificate public key.

`public_key_algorithm`

(required) The Certificate public key algorithm.

`public_key_size`

(required) The Certificate public key size.

`serial`

(required) The Certificate serial.

`subject`

(required) The Certificate subject.

`time_valid_from`

(required) The time the certificate is valid from. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_valid_to`

(required) The time the certificate is valid to. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`version`

(required) The Certificate version.

`sha1_hash`

(required) The Certificate sha1 hash.

`authority_key_id`

(required) The Certificate authority key id.

`is_ca`

(required) Indicates if the certificate is ca.

`subject_key_id`

(required) The Certificate subject key id.

`lifecycle_state`

(required) Possible certificate lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_SUMMARY_T Type

Summary of the Certificates.

Syntax
```

```

Fields

Field Description

`key`

(required) The identifier key (unique name in the scope of the deployment) of the certificate being referenced. It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`lifecycle_state`

(required) Possible certificate lifecycle states.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`subject`

(required) The Certificate subject.

`is_self_signed`

(required) Indicates if the certificate is self signed.

`time_valid_to`

(required) The time the certificate is valid to. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_certificate_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_COLLECTION_T Type

A list of Certificates.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Certificates.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_CONNECTION_COMPARTMENT_DETAILS_T Type

The new compartment for a Connection.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DATABASE_REGISTRATION_COMPARTMENT_DETAILS_T Type

The new compartment for a DatabaseRegistration.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DEPLOYMENT_BACKUP_COMPARTMENT_DETAILS_T Type

The new compartment for a DeploymentBackup.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DEPLOYMENT_COMPARTMENT_DETAILS_T Type

The new compartment for a Deployment.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_COLLECT_DEPLOYMENT_DIAGNOSTIC_DETAILS_T Type

Details for collecting deployment diagnostic

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(required) Name of the bucket where the object is to be uploaded in the object storage

`diagnostic_name_prefix`

(required) Prefix of the diagnostic collected and uploaded to object storage

`time_diagnostic_start`

(optional) The time from which the diagnostic collection should collect the logs. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_diagnostic_end`

(optional) The time until which the diagnostic collection should collect the logs. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_T Type

Represents the metadata description of a connection assignment. Before you can use a connection as a GoldenGate source or target, you must assign it to a deployment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection assignment being referenced.

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`alias_name`

(optional) Credential store alias.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`lifecycle_state`

(required) Possible lifecycle states for connection assignments.

Allowed values are: 'CREATING', 'ACTIVE', 'FAILED', 'UPDATING', 'DELETING'

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(required) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_SUMMARY_T Type

Summary of the Connection Assignment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection assignment being referenced.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`alias_name`

(required) Credential store alias.

`lifecycle_state`

(required) Possible lifecycle states for connection assignments.

`time_created`

(required) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(required) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_connection_assignment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_COLLECTION_T Type

List of connection summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Connection Assignment summaries.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_connection_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_COLLECTION_T Type

List of connection summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Connection summaries.

### DBMS_CLOUD_OCI_GOLDEN_GATE_COPY_DEPLOYMENT_BACKUP_DETAILS_T Type

The information about the copy for a Deployment Backup.

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(required) Name of the bucket where the object is to be uploaded in the object storage

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CONNECTION_DETAILS_T Type

The information about a new Connection.

Syntax
```

```

Fields

Field Description

`connection_type`

(required) The connection type.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`routing_method`

(optional) Controls the network traffic direction to the target: SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets. SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

Allowed values are: 'SHARED_SERVICE_ENDPOINT', 'SHARED_DEPLOYMENT_ENDPOINT', 'DEDICATED_ENDPOINT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_KINESIS_CONNECTION_DETAILS_T Type

The information about a new Amazon Kinesis Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_amazon_kinesis_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Kinesis technology type.

`access_key_id`

(required) Access key ID to access the Amazon Kinesis.

`secret_access_key`

(required) Secret access key to access the Amazon Kinesis.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_REDSHIFT_CONNECTION_DETAILS_T Type

The information about a new Amazon Redshift Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_amazon_redshift_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon Redshift technology type.

`connection_url`

(required) Connection URL. e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_S3_CONNECTION_DETAILS_T Type

The information about a new Amazon S3 Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_amazon_s3_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Amazon S3 technology type.

`access_key_id`

(required) Access key ID to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

`secret_access_key`

(required) Secret access key to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_DETAILS_T Type

The information about a new Azure Data Lake Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_azure_data_lake_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Data Lake Storage technology type.

`authentication_type`

(required) Used authentication mechanism to access Azure Data Lake Storage.

`account_name`

(required) Sets the Azure storage account name.

`account_key`

(optional) Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'. e.g.: pa3WbhVATzj56xD4DH1VjOUhApRGEGHvOo58eQJVWIzX+j8j4CUVFcTjpIqDSRaSa1Wo2LbWY5at+AStEgLOIQ==

`sas_token`

(optional) Credential that uses a shared access signature (SAS) to authenticate to an Azure Service. This property is required when 'authenticationType' is set to 'SHARED_ACCESS_SIGNATURE'. e.g.: ?sv=2020-06-08&amp;ss=bfqt&amp;srt=sco&amp;sp=rwdlacupyx&amp;se=2020-09-10T20:27:28Z&amp;st=2022-08-05T12:27:28Z&amp;spr=https&amp;sig=C1IgHsiLBmTSStYkXXGLTP8it0xBrArcgCqOsZbXwIQ%3D

`azure_tenant_id`

(optional) Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 14593954-d337-4a61-a364-9f758c64f97f

`client_id`

(optional) Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d

`client_secret`

(optional) Azure client secret (aka application password) for authentication. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: dO29Q~F5-VwnA.lZdd11xFF_t5NAXCaGwDl9NbT1

`endpoint`

(optional) Azure Storage service endpoint. e.g: https://test.blob.core.windows.net

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AZURE_SYNAPSE_CONNECTION_DETAILS_T Type

The information about a new Azure Synapse Analytics Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_azure_synapse_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Azure Synapse Analytics technology type.

`connection_string`

(required) JDBC connection string. e.g.: 'jdbc:sqlserver://&lt;synapse-workspace&gt;.sql.azuresynapse.net:1433;database=&lt;db-name&gt;;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CERTIFICATE_DETAILS_T Type

The information about a new Certificates.

Syntax
```

```

Fields

Field Description

`key`

(required) The identifier key (unique name in the scope of the deployment) of the certificate being referenced. It must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`certificate_content`

(required) A PEM-encoded SSL certificate.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CONNECTION_ASSIGNMENT_DETAILS_T Type

The information about a new Connection Assignment.

Syntax
```

```

Fields

Field Description

`connection_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the connection being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DATABASE_REGISTRATION_DETAILS_T Type

The information about a new DatabaseRegistration.

Syntax
```

```

Fields

Field Description

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`fqdn`

(required) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`ip_address`

(optional) The private IP address in the customer's VCN of the customer's endpoint, typically a database.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

Allowed values are: 'DIRECT', 'REDIRECT'

`wallet`

(optional) The wallet contents Oracle GoldenGate uses to make connections to a database. This attribute is expected to be base64 encoded.

`alias_name`

(required) Credential store alias.

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`secret_compartment_id`

(optional) The OCID of the compartment where the GoldenGate Secret will be created. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DEPLOYMENT_BACKUP_DETAILS_T Type

The information about a new DeploymentBackup.

Syntax
```

```

Fields

Field Description

`display_name`

(required) An object's Display Name.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`namespace_name`

(required) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(required) Name of the bucket where the object is to be uploaded in the object storage

`object_name`

(required) Name of the object to be uploaded to object storage

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_OGG_DEPLOYMENT_DETAILS_T Type

Deployment Data for creating an OggDeployment

Syntax
```

```

Fields

Field Description

`deployment_name`

(required) The name given to the GoldenGate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`credential_store`

(optional) The type of credential store for OGG.

Allowed values are: 'GOLDENGATE', 'IAM'

`identity_domain_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Identity Domain when IAM credential store is used.

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the deployment password is stored.

`admin_username`

(optional) The GoldenGate deployment console username.

`admin_password`

(optional) The password associated with the GoldenGate deployment console username. The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric, and 1 special character. Special characters such as '$', '^', or '?' are not allowed. This field will be deprecated and replaced by \"passwordSecretId\".

`certificate`

(optional) A PEM-encoded SSL certificate.

`key`

(optional) A PEM-encoded private key.

`ogg_version`

(optional) Version of OGG

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MAINTENANCE_WINDOW_DETAILS_T Type

Defines the maintenance window for create operation, when automatic actions can be performed.

Syntax
```

```

Fields

Field Description

`day`

(required) Days of the week.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

`start_hour`

(required) Start hour for maintenance period. Hour is in UTC.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MAINTENANCE_CONFIGURATION_DETAILS_T Type

Defines the maintenance configuration for create operation.

Syntax
```

```

Fields

Field Description

`is_interim_release_auto_upgrade_enabled`

(optional) By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interimReleaseUpgradePeriodInDays too.

`interim_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.

`bundle_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.

`major_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default.

`security_patch_upgrade_period_in_days`

(optional) Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DEPLOYMENT_DETAILS_T Type

The information about a new Deployment.

Syntax
```

```

Fields

Field Description

`display_name`

(required) An object's Display Name.

`license_model`

(required) The Oracle license model that applies to a Deployment.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`deployment_backup_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup being referenced.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet of the deployment's private endpoint.

`load_balancer_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a public subnet in the customer tenancy. Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy. For backward compatiblity this is an optional property for now, but it will become mandatory (for public deployments only) after October 1, 2024.

`fqdn`

(optional) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`is_public`

(optional) True if this object is publicly available.

`cpu_core_count`

(required) The Minimum number of OCPUs to be made available for this Deployment.

`is_auto_scaling_enabled`

(required) Indicates if auto scaling is enabled for the Deployment's CPU core count.

`deployment_type`

(required) The type of deployment, which can be any one of the Allowed values. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes. Its use is discouraged in favor of 'DATABASE_ORACLE'.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`ogg_data`

(optional)

`maintenance_window`

(optional)

`maintenance_configuration`

(optional)

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ELASTICSEARCH_CONNECTION_DETAILS_T Type

The information about a new Elasticsearch Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_elasticsearch_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Elasticsearch technology type.

`servers`

(required) Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Used for establishing the initial connection to the Elasticsearch cluster. Example: `\"server1.example.com:4000,server2.example.com:4000\"`

`security_protocol`

(required) Security protocol for Elasticsearch.

`authentication_type`

(required) Authentication type for Elasticsearch.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`fingerprint`

(optional) Fingerprint required by TLS security protocol. Eg.: '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GENERIC_CONNECTION_DETAILS_T Type

The information about a new Generic Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_generic_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Generic technology type.

`host`

(required) Host and port separated by colon. Example: `\"server.example.com:1234\"` For multiple hosts, provide a comma separated list. Example: `\"server1.example.com:1000,server1.example.com:2000\"`

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOLDEN_GATE_CONNECTION_DETAILS_T Type

The information about a new GoldenGate Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_golden_gate_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The GoldenGate technology type.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username credential existing in the Oracle GoldenGate used to be connected to.

`password`

(optional) The password used to connect to the Oracle GoldenGate accessed trough this connection.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOOGLE_BIG_QUERY_CONNECTION_DETAILS_T Type

The information about a new Google BigQuery Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_google_big_query_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Google BigQuery technology type.

`service_account_key_file`

(required) The base64 encoded content of the service account key file containing the credentials required to use Google BigQuery.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOOGLE_CLOUD_STORAGE_CONNECTION_DETAILS_T Type

The information about a new Google Cloud Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_google_cloud_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Google Cloud Storage technology type.

`service_account_key_file`

(required) The base64 encoded content of the service account key file containing the credentials required to use Google Cloud Storage.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_HDFS_CONNECTION_DETAILS_T Type

The information about a new Hadoop Distributed File System Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_hdfs_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Hadoop Distributed File System technology type.

`core_site_xml`

(required) The base64 encoded content of the Hadoop Distributed File System configuration file (core-site.xml).

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_JAVA_MESSAGE_SERVICE_CONNECTION_DETAILS_T Type

The information about a new Java Message Service Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_java_message_service_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Java Message Service technology type.

`should_use_jndi`

(required) If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.

`jndi_connection_factory`

(optional) The Connection Factory can be looked up using this name. e.g.: 'ConnectionFactory'

`jndi_provider_url`

(optional) The URL that Java Message Service will use to contact the JNDI provider. e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'

`jndi_initial_context_factory`

(optional) The implementation of javax.naming.spi.InitialContextFactory interface that the client uses to obtain initial naming context. e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'

`jndi_security_principal`

(optional) Specifies the identity of the principal (user) to be authenticated. e.g.: 'admin2'

`jndi_security_credentials`

(optional) The password associated to the principal.

`connection_url`

(optional) Connectin URL of the Java Message Service, specifying the protocol, host, and port. e.g.: 'mq://myjms.host.domain:7676'

`connection_factory`

(optional) The of Java class implementing javax.jms.ConnectionFactory interface supplied by the Java Message Service provider. e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'

`username`

(optional) The username Oracle GoldenGate uses to connect to the Java Message Service. This username must already exist and be available by the Java Message Service to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated Java Message Service.

`security_protocol`

(optional) Security protocol for Java Message Service. If not provided, default is PLAIN. Optional until 2024-06-27, in the release after it will be made required.

`authentication_type`

(optional) Authentication type for Java Message Service. If not provided, default is NONE. Optional until 2024-06-27, in the release after it will be made required.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_BOOTSTRAP_SERVER_T Type

Represents a Kafka bootstrap server with host name, optional port defaults to 9092, and an optional private ip.

Syntax
```

```

Fields

Field Description

`host`

(required) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_BOOTSTRAP_SERVER_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_kafka_bootstrap_server_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_KAFKA_CONNECTION_DETAILS_T Type

The information about a new Kafka Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_kafka_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka technology type.

`stream_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream pool being referenced.

`bootstrap_servers`

(optional) Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

`security_protocol`

(optional) Security Type for Kafka.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided.

`consumer_properties`

(optional) The base64 encoded content of the consumer.properties file.

`producer_properties`

(optional) The base64 encoded content of the producer.properties file.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_DETAILS_T Type

The information about a new Kafka (e.g. Confluent) Schema Registry Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_kafka_schema_registry_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka (e.g. Confluent) Schema Registry technology type.

`url`

(required) Kafka Schema Registry URL.

`authentication_type`

(required) Used authentication mechanism to access Schema Registry.

`username`

(optional) The username to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`password`

(optional) The password to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside the KeyStore. In case it differs from the KeyStore password, it should be provided.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_NAME_VALUE_PAIR_T Type

A name-value pair representing an attribute entry usable in a list of attributes.

Syntax
```

```

Fields

Field Description

`name`

(required) The name of the property entry.

`value`

(required) The value of the property entry.

### DBMS_CLOUD_OCI_GOLDEN_GATE_NAME_VALUE_PAIR_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_name_value_pair_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MICROSOFT_SQLSERVER_CONNECTION_DETAILS_T Type

The information about a new Microsoft SQL Server Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_microsoft_sqlserver_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Microsoft SQL Server technology type.

`database_name`

(required) The name of the database.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`username`

(required) The username Oracle GoldenGate uses to connect to the Microsoft SQL Server. This username must already exist and be available by the Microsoft SQL Server to be connected to.

`password`

(required) The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security Type for Microsoft SQL Server.

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1-way SSL).

`should_validate_server_certificate`

(optional) If set to true, the driver validates the certificate that is sent by the database server.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MONGO_DB_CONNECTION_DETAILS_T Type

The information about a new MongoDB Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_mongo_db_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The MongoDB technology type.

`connection_string`

(optional) MongoDB connection string. e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'

`username`

(optional) The username Oracle GoldenGate uses to connect to the database. This username must already exist and be available by the database to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated database.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Autonomous Json Database.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MYSQL_CONNECTION_DETAILS_T Type

The information about a new MySQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_mysql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The MySQL technology type.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`database_name`

(required) The name of the database.

`security_protocol`

(required) Security Type for MySQL.

`ssl_mode`

(optional) SSL modes for MySQL.

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1 and 2-way SSL).

`ssl_crl`

(optional) The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA). Note: This is an optional property and only applicable if TLS/MTLS option is selected.

`ssl_cert`

(optional) Client Certificate - The base64 encoded content of a .pem or .crt file. containing the client public key (for 2-way SSL).

`ssl_key`

(optional) Client Key – The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL).

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_OCI_OBJECT_STORAGE_CONNECTION_DETAILS_T Type

The information about a new OCI Object Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_oci_object_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The OCI Object Storage technology type.

`tenancy_id`

(optional) The OCID of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(optional) The OCID of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.

`private_key_file`

(required) The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.

`private_key_passphrase`

(optional) The passphrase of the private key.

`public_key_fingerprint`

(required) The fingerprint of the API Key of the user specified by the userId.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ORACLE_CONNECTION_DETAILS_T Type

The information about a new Oracle Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_oracle_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle technology type.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`wallet`

(optional) The wallet contents Oracle GoldenGate uses to make connections to a database. This attribute is expected to be base64 encoded.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ORACLE_NOSQL_CONNECTION_DETAILS_T Type

The information about a new Oracle NoSQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_oracle_nosql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle NoSQL technology type.

`tenancy_id`

(optional) The OCID of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(optional) The OCID of the OCI user who will access the Oracle NoSQL database. The user must have write access to the table they want to connect to.

`private_key_file`

(required) The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.

`private_key_passphrase`

(optional) The passphrase of the private key.

`public_key_fingerprint`

(required) The fingerprint of the API Key of the user specified by the userId.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_POSTGRESQL_CONNECTION_DETAILS_T Type

The information about a new PostgreSQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_postgresql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The PostgreSQL technology type.

`database_name`

(required) The name of the database.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(required) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security protocol for PostgreSQL.

`ssl_mode`

(optional) SSL modes for PostgreSQL.

`ssl_ca`

(optional) The base64 encoded certificate of the trusted certificate authorities (Trusted CA) for PostgreSQL. The supported file formats are .pem and .crt.

`ssl_crl`

(optional) The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).

`ssl_cert`

(optional) The base64 encoded certificate of the PostgreSQL server. The supported file formats are .pem and .crt.

`ssl_key`

(optional) The base64 encoded private key of the PostgreSQL server. The supported file formats are .pem and .crt.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_REDIS_CONNECTION_DETAILS_T Type

The information about a new Redis Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_redis_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Redis technology type.

`servers`

(required) Comma separated list of Redis server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 6379. Used for establishing the initial connection to the Redis cluster. Example: `\"server1.example.com:6379,server2.example.com:6379\"`

`security_protocol`

(required) Security protocol for Redis.

`authentication_type`

(required) Authenticationentication type for the Redis database.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

### DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_SNOWFLAKE_CONNECTION_DETAILS_T Type

The information about a new Snowflake Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_create_snowflake_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_create_connection_details_t`type.

Fields

Field Description

`technology_type`

(required) The Snowflake technology type.

`connection_url`

(required) JDBC connection URL. e.g.: 'jdbc:snowflake://&lt;account_name&gt;.snowflakecomputing.com/?warehouse=&lt;warehouse-name&gt;&amp;db=&lt;db-name&gt;'

`authentication_type`

(required) Used authentication mechanism to access Snowflake.

`username`

(optional) The username Oracle GoldenGate uses to connect to Snowflake. This username must already exist and be available by Snowflake platform to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect to Snowflake platform.

`private_key_file`

(optional) The base64 encoded content of private key file in PEM format.

`private_key_passphrase`

(optional) Password if the private key file is encrypted.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_T Type

Represents the metadata description of a database used by deployments in the same compartment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the databaseRegistration being referenced.

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`fqdn`

(required) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`ip_address`

(required) The private IP address in the customer's VCN of the customer's endpoint, typically a database.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

`rce_private_ip`

(optional) A Private Endpoint IP address created in the customer's subnet. A customer database can expect network traffic initiated by GoldenGate Service from this IP address. It can also send network traffic to this IP address, typically in response to requests from GoldenGate Service. The customer may use this IP address in Security Lists or Network Security Groups (NSG) as needed.

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

Allowed values are: 'DIRECT', 'REDIRECT'

`alias_name`

(required) Credential store alias.

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`secret_compartment_id`

(optional) The OCID of the compartment where the GoldenGate Secret will be created. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`secret_id`

(optional) The OCID of the customer's GoldenGate Service Secret. If provided, it references a key that customers will be required to ensure the policies are established to permit GoldenGate to use this Secret.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_SUMMARY_T Type

Summary of the DatabaseRegistration.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the databaseRegistration being referenced.

`display_name`

(required) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`fqdn`

(required) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

Allowed values are: 'DIRECT', 'REDIRECT'

`alias_name`

(optional) Credential store alias.

`secret_id`

(optional) The OCID of the customer's GoldenGate Service Secret. If provided, it references a key that customers will be required to ensure the policies are established to permit GoldenGate to use this Secret.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_database_registration_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_COLLECTION_T Type

A list of DatabaseRegistrations.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of DatabaseRegistration summaries.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_DEPLOYMENT_BACKUP_DETAILS_T Type

Definition of the additional attributes for default deployment backup cancel.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_cancel_deployment_backup_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_cancel_deployment_backup_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_DEPLOYMENT_UPGRADE_DETAILS_T Type

Definition of the additional attributes for default deployment upgrade cancel.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_cancel_deployment_upgrade_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_cancel_deployment_upgrade_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type

Definition of the additional attributes for default deployment upgrade cancel snooze.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_cancel_snooze_deployment_upgrade_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_cancel_snooze_deployment_upgrade_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLET_EXISTS_DETAILS_T Type

The information to check if a wallet is present in the Deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment for wallet

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_DEPLOYMENT_WALLET_EXISTS_DETAILS_T Type

Definition of the additional attributes for default check of a wallet in deployment .

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_deployment_wallet_exists_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_deployment_wallet_exists_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_RESTORE_DEPLOYMENT_DETAILS_T Type

The information about the Restore for a Deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment restore.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_RESTORE_DEPLOYMENT_DETAILS_T Type

Definition of the additional attributes for default deployment restore.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_restore_deployment_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_restore_deployment_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ROLLBACK_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about the rollback of an upgrade.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deploymentUpgrade rollback.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_ROLLBACK_DEPLOYMENT_UPGRADE_DETAILS_T Type

Definition of the additional attributes for default upgrade rollback.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_rollback_deployment_upgrade_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_rollback_deployment_upgrade_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about the snooze for a deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deploymentUpgrade snooze.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type

Definition of the additional attributes for default deployment upgrade snooze.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_snooze_deployment_upgrade_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_snooze_deployment_upgrade_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_START_DEPLOYMENT_DETAILS_T Type

The information about the Start for a Deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment start

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_START_DEPLOYMENT_DETAILS_T Type

Definition of the additional attributes for default deployment start.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_start_deployment_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_start_deployment_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_STOP_DEPLOYMENT_DETAILS_T Type

The information about the Stop for a Deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment stop

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_STOP_DEPLOYMENT_DETAILS_T Type

Definition of the additional attributes for default deployment stop.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_stop_deployment_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_stop_deployment_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_DETAILS_T Type

The information about testing the assigned connection.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of the test of the assigned connection.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_TEST_CONNECTION_ASSIGNMENT_DETAILS_T Type

Definition of the additional attributes for default test of assigned connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_test_connection_assignment_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_test_connection_assignment_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about the upgrade for a deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment start.

Allowed values are: 'DEFAULT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_UPGRADE_DEPLOYMENT_UPGRADE_DETAILS_T Type

Definition of the additional attributes for default deployment upgrade.

Syntax
```

```

`dbms_cloud_oci_golden_gate_default_upgrade_deployment_upgrade_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_upgrade_deployment_upgrade_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_OGG_DEPLOYMENT_T Type

Deployment Data for an OggDeployment

Syntax
```

```

Fields

Field Description

`deployment_name`

(required) The name given to the GoldenGate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.

`admin_username`

(required) The GoldenGate deployment console username.

`ogg_version`

(optional) Version of OGG

`certificate`

(optional) A PEM-encoded SSL certificate.

`credential_store`

(optional) The type of credential store for OGG.

Allowed values are: 'GOLDENGATE', 'IAM'

`identity_domain_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Identity Domain when IAM credential store is used.

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the deployment password is stored.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_DIAGNOSTIC_DATA_T Type

Information regarding the deployment diagnostic collection

Syntax
```

```

Fields

Field Description

`namespace_name`

(required) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(required) Name of the bucket where the object is to be uploaded in the object storage

`object_name`

(required) Name of the diagnostic collected and uploaded to object storage

`diagnostic_state`

(required) The state of the deployment diagnostic collection.

Allowed values are: 'IN_PROGRESS', 'SUCCEEDED', 'FAILED'

`time_diagnostic_start`

(optional) The time from which the diagnostic collection should collect the logs. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_diagnostic_end`

(optional) The time until which the diagnostic collection should collect the logs. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MAINTENANCE_WINDOW_T Type

Defines the maintenance window, when automatic actions can be performed.

Syntax
```

```

Fields

Field Description

`day`

(required) Days of the week.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

`start_hour`

(required) Start hour for maintenance period. Hour is in UTC.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MAINTENANCE_CONFIGURATION_T Type

Attributes for configuring automatic deployment maintenance.

Syntax
```

```

Fields

Field Description

`is_interim_release_auto_upgrade_enabled`

(required) By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interimReleaseUpgradePeriodInDays too.

`interim_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.

`bundle_release_upgrade_period_in_days`

(required) Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.

`major_release_upgrade_period_in_days`

(required) Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default.

`security_patch_upgrade_period_in_days`

(required) Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_T Type

A container for your OCI GoldenGate resources, such as the OCI GoldenGate deployment console.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`deployment_backup_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup being referenced.

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_sub_state`

(optional) Possible GGS lifecycle sub-states.

Allowed values are: 'RECOVERING', 'STARTING', 'STOPPING', 'MOVING', 'UPGRADING', 'RESTORING', 'BACKUP_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`is_healthy`

(optional) True if all of the aggregate resources are working correctly.

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet of the deployment's private endpoint.

`load_balancer_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a public subnet in the customer tenancy. Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy. For backward compatiblity this is an optional property for now, but it will become mandatory (for public deployments only) after October 1, 2024.

`load_balancer_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the loadbalancer in the customer's subnet. The loadbalancer of the public deployment created in the customer subnet.

`fqdn`

(optional) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`license_model`

(required) The Oracle license model that applies to a Deployment.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`cpu_core_count`

(required) The Minimum number of OCPUs to be made available for this Deployment.

`is_auto_scaling_enabled`

(required) Indicates if auto scaling is enabled for the Deployment's CPU core count.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`is_public`

(optional) True if this object is publicly available.

`public_ip_address`

(optional) The public IP address representing the access point for the Deployment.

`private_ip_address`

(optional) The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.

`deployment_url`

(optional) The URL of a resource.

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`is_latest_version`

(optional) Indicates if the resource is the the latest available version.

`time_upgrade_required`

(optional) Note: Deprecated: Use timeOfNextMaintenance instead, or related upgrade records to check, when deployment will be forced to upgrade to a newer version. Old description: The date the existing version in use will no longer be considered as usable and an upgrade will be required. This date is typically 6 months after the version was released for use by GGS. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`storage_utilization_in_bytes`

(optional) The amount of storage being utilized (in bytes)

`is_storage_utilization_limit_exceeded`

(optional) Indicator will be true if the amount of storage being utilized exceeds the allowable storage utilization limit. Exceeding the limit may be an indication of a misconfiguration of the deployment's GoldenGate service.

`deployment_type`

(required) The type of deployment, which can be any one of the Allowed values. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes. Its use is discouraged in favor of 'DATABASE_ORACLE'.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`ogg_data`

(optional)

`deployment_diagnostic_data`

(optional)

`maintenance_window`

(optional)

`time_of_next_maintenance`

(optional) The time of next maintenance schedule. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`next_maintenance_action_type`

(optional) Type of the next maintenance.

Allowed values are: 'UPGRADE'

`next_maintenance_description`

(optional) Description of the next maintenance.

`maintenance_configuration`

(optional)

`time_ogg_version_supported_until`

(optional) The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`ingress_ips`

(optional) List of ingress IP addresses from where the GoldenGate deployment connects to this connection's privateIp. Customers may optionally set up ingress security rules to restrict traffic from these IP addresses.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_T Type

A backup of the current state of the GoldenGate deployment. Can be used to restore a deployment, or create a new deployment with that state as the starting deployment state.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`display_name`

(optional) An object's Display Name.

`is_automatic`

(optional) True if this object is automatically created

`lifecycle_state`

(required) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`time_of_backup`

(optional) The time of the resource backup. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_backup_finished`

(optional) The time of the resource backup finish. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`size_in_bytes`

(optional) The size of the backup stored in object storage (in bytes)

`backup_type`

(optional) Possible Deployment backup types.

Allowed values are: 'INCREMENTAL', 'FULL'

`ogg_version`

(required) Version of OGG

`namespace_name`

(optional) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(optional) Name of the bucket where the object is to be uploaded in the object storage

`object_name`

(optional) Name of the object to be uploaded to object storage

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_SUMMARY_T Type

The summary of the Backup.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the backup being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`display_name`

(optional) An object's Display Name.

`is_automatic`

(optional) True if this object is automatically created

`lifecycle_state`

(required) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`time_of_backup`

(optional) The time of the resource backup. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_backup_finished`

(optional) The time of the resource backup finish. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`size_in_bytes`

(optional) The size of the backup stored in object storage (in bytes)

`backup_type`

(optional) Possible Deployment backup types.

Allowed values are: 'INCREMENTAL', 'FULL'

`ogg_version`

(required) Version of OGG

`namespace_name`

(optional) Name of namespace that serves as a container for all of your buckets

`bucket_name`

(optional) Name of the bucket where the object is to be uploaded in the object storage

`object_name`

(optional) Name of the object to be uploaded to object storage

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_backup_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_COLLECTION_T Type

A list of DeploymentBackups.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of DeploymentBackups.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_SUMMARY_T Type

Summary of the Deployment.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_sub_state`

(optional) Possible GGS lifecycle sub-states.

Allowed values are: 'RECOVERING', 'STARTING', 'STOPPING', 'MOVING', 'UPGRADING', 'RESTORING', 'BACKUP_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`subnet_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet of the deployment's private endpoint.

`load_balancer_subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of a public subnet in the customer tenancy. Can be provided only for public deployments. If provided, the loadbalancer will be created in this subnet instead of the service tenancy. For backward compatiblity this is an optional property for now, but it will become mandatory (for public deployments only) after October 1, 2024.

`load_balancer_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the loadbalancer in the customer's subnet. The loadbalancer of the public deployment created in the customer subnet.

`license_model`

(required) The Oracle license model that applies to a Deployment.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`fqdn`

(optional) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`cpu_core_count`

(optional) The Minimum number of OCPUs to be made available for this Deployment.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling is enabled for the Deployment's CPU core count.

`is_public`

(optional) True if this object is publicly available.

`public_ip_address`

(optional) The public IP address representing the access point for the Deployment.

`private_ip_address`

(optional) The private IP address in the customer's VCN representing the access point for the associated endpoint service in the GoldenGate service VCN.

`deployment_url`

(optional) The URL of a resource.

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`is_latest_version`

(optional) Indicates if the resource is the the latest available version.

`time_upgrade_required`

(optional) Note: Deprecated: Use timeOfNextMaintenance instead, or related upgrade records to check, when deployment will be forced to upgrade to a newer version. Old description: The date the existing version in use will no longer be considered as usable and an upgrade will be required. This date is typically 6 months after the version was released for use by GGS. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`deployment_type`

(optional) The type of deployment, which can be any one of the Allowed values. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes. Its use is discouraged in favor of 'DATABASE_ORACLE'.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`storage_utilization_in_bytes`

(optional) The amount of storage being utilized (in bytes)

`is_storage_utilization_limit_exceeded`

(optional) Indicator will be true if the amount of storage being utilized exceeds the allowable storage utilization limit. Exceeding the limit may be an indication of a misconfiguration of the deployment's GoldenGate service.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_COLLECTION_T Type

A list of Deployments.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Deployment summaries.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MESSAGE_SUMMARY_T Type

Deployment message Summary.

Syntax
```

```

Fields

Field Description

`id`

(required) The deployment Message Id.

`deployment_message`

(required) The deployment Message in plain text with optional HTML anchor tags.

`deployment_message_status`

(required) The deployment Message Status.

Allowed values are: 'INFO', 'WARNING', 'ERROR'

### DBMS_CLOUD_OCI_GOLDEN_GATE_MESSAGE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_message_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_MESSAGE_COLLECTION_T Type

A list of DeploymentMessages.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of DeploymentMessages.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_SUMMARY_T Type

The meta-data specific on particular deployment type represented by deploymentType field.

Syntax
```

```

Fields

Field Description

`category`

(required) The deployment category defines the broad separation of the deployment type into three categories. Currently the separation is 'DATA_REPLICATION', 'STREAM_ANALYTICS' and 'DATA_TRANSFORMS'.

Allowed values are: 'DATA_REPLICATION', 'STREAM_ANALYTICS', 'DATA_TRANSFORMS'

`display_name`

(required) An object's Display Name.

`deployment_type`

(required) The type of deployment, which can be any one of the Allowed values. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes. Its use is discouraged in favor of 'DATABASE_ORACLE'.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`connection_types`

(optional) An array of connectionTypes.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`source_technologies`

(optional) List of the supported technologies generally. The value is a freeform text string generally consisting of a description of the technology and optionally the speific version(s) support. For example, [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]

`target_technologies`

(optional) List of the supported technologies generally. The value is a freeform text string generally consisting of a description of the technology and optionally the speific version(s) support. For example, [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]

`ogg_version`

(optional) Version of OGG

`supported_technologies_url`

(optional) The URL to the webpage listing the supported technologies.

`default_username`

(optional) The default admin username used by deployment.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_type_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_COLLECTION_T Type

The list of DeploymentTypeDescriptor objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of DeploymentTypeSummary

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_T Type

A container for your OCI GoldenGate Upgrade information.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment upgrade being referenced.

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`deployment_upgrade_type`

(required) The type of the deployment upgrade: MANUAL or AUTOMATIC

Allowed values are: 'MANUAL', 'AUTOMATIC'

`time_started`

(optional) The date and time the request was started. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_finished`

(optional) The date and time the request was finished. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`ogg_version`

(optional) Version of OGG

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_sub_state`

(optional) Possible GGS lifecycle sub-states.

Allowed values are: 'RECOVERING', 'STARTING', 'STOPPING', 'MOVING', 'UPGRADING', 'RESTORING', 'BACKUP_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`previous_ogg_version`

(optional) Version of OGG

`time_schedule`

(optional) The time of upgrade schedule. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`is_snoozed`

(optional) Indicates if upgrade notifications are snoozed or not.

`time_snoozed_until`

(optional) The time the upgrade notifications are snoozed until. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_released`

(optional) The time the resource was released. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`release_type`

(optional) The type of release.

Allowed values are: 'MAJOR', 'BUNDLE', 'MINOR'

`is_security_fix`

(optional) Indicates if OGG release contains security fix.

`is_rollback_allowed`

(optional) Indicates if rollback is allowed. In practice only the last upgrade can be rolled back. - Manual upgrade is allowed to rollback only until the old version isn't deprecated yet. - Automatic upgrade by default is not allowed, unless a serious issue does not justify.

`time_ogg_version_supported_until`

(optional) The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`is_cancel_allowed`

(optional) Indicates if cancel is allowed. Scheduled upgrade can be cancelled only if target version is not forced by service, otherwise only reschedule allowed.

`is_reschedule_allowed`

(optional) Indicates if reschedule is allowed. Upgrade can be rescheduled postponed until the end of the service defined auto-upgrade period.

`time_schedule_max`

(optional) Indicates the latest time until the deployment upgrade could be rescheduled. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_SUMMARY_T Type

Summary of the Deployment Upgrade.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment being referenced.

`deployment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`deployment_upgrade_type`

(required) The type of the deployment upgrade: MANUAL or AUTOMATIC

Allowed values are: 'MANUAL', 'AUTOMATIC'

`time_started`

(optional) The date and time the request was started. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_finished`

(optional) The date and time the request was finished. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`ogg_version`

(optional) Version of OGG

`time_created`

(optional) The time the resource was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`lifecycle_state`

(optional) Possible lifecycle states.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED', 'FAILED', 'NEEDS_ATTENTION', 'IN_PROGRESS', 'CANCELING', 'CANCELED', 'SUCCEEDED', 'WAITING'

`lifecycle_sub_state`

(optional) Possible GGS lifecycle sub-states.

Allowed values are: 'RECOVERING', 'STARTING', 'STOPPING', 'MOVING', 'UPGRADING', 'RESTORING', 'BACKUP_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS'

`lifecycle_details`

(optional) Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`

`previous_ogg_version`

(optional) Version of OGG

`time_schedule`

(optional) The time of upgrade schedule. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`is_snoozed`

(optional) Indicates if upgrade notifications are snoozed or not.

`time_snoozed_until`

(optional) The time the upgrade notifications are snoozed until. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_released`

(optional) The time the resource was released. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`release_type`

(optional) The type of release.

Allowed values are: 'MAJOR', 'BUNDLE', 'MINOR'

`is_security_fix`

(optional) Indicates if OGG release contains security fix.

`is_rollback_allowed`

(optional) Indicates if rollback is allowed. In practice only the last upgrade can be rolled back. - Manual upgrade is allowed to rollback only until the old version isn't deprecated yet. - Automatic upgrade by default is not allowed, unless a serious issue does not justify.

`time_ogg_version_supported_until`

(optional) The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`is_cancel_allowed`

(optional) Indicates if cancel is allowed. Scheduled upgrade can be cancelled only if target version is not forced by service, otherwise only reschedule allowed.

`is_reschedule_allowed`

(optional) Indicates if reschedule is allowed. Upgrade can be rescheduled postponed until the end of the service defined auto-upgrade period.

`time_schedule_max`

(optional) Indicates the latest time until the deployment upgrade could be rescheduled. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_upgrade_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_COLLECTION_T Type

A list of Deployment Upgrades.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of Deployment Upgrade summaries.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_SUMMARY_T Type

The summary data of a specific deployment version.

Syntax
```

```

Fields

Field Description

`ogg_version`

(required) Version of OGG

`deployment_type`

(required) The type of deployment, which can be any one of the Allowed values. NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes. Its use is discouraged in favor of 'DATABASE_ORACLE'.

Allowed values are: 'OGG', 'DATABASE_ORACLE', 'BIGDATA', 'DATABASE_MICROSOFT_SQLSERVER', 'DATABASE_MYSQL', 'DATABASE_POSTGRESQL', 'DATABASE_DB2ZOS', 'GGSA', 'DATA_TRANSFORMS'

`time_released`

(optional) The time the resource was released. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`release_type`

(optional) The type of release.

Allowed values are: 'MAJOR', 'BUNDLE', 'MINOR'

`is_security_fix`

(optional) Indicates if OGG release contains security fix.

`time_supported_until`

(optional) The time until OGG version is supported. After this date has passed OGG version will not be available anymore. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_COLLECTION_T Type

The list of DeploymentVersionSummary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) Array of DeploymentVersionSummary.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLET_EXISTS_RESPONSE_DETAILS_T Type

Indicates whether the wallet exists in the deployment container

Syntax
```

```

Fields

Field Description

`is_ogg_wallet_exists`

(required) Indicates if the wallet is present in the deployment container

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_SUMMARY_T Type

Summary of the deployment wallets operations.

Syntax
```

```

Fields

Field Description

`wallet_operation_id`

(required) The UUID of the wallet operation performed by the customer. If provided, this will reference a key which the customer can use to query or search a particular wallet operation

`wallet_secret_id`

(required) The OCID of the customer's GoldenGate Service Secret. If provided, it references a key that customers will be required to ensure the policies are established to permit GoldenGate to use this Secret.

`deployment_wallet_operation_type`

(required) The operation type of the deployment wallet.

Allowed values are: 'EXPORT', 'IMPORT'

`deployment_wallet_operation_status`

(required) The status of the deployment wallet.

Allowed values are: 'EXPORTING', 'EXPORTED', 'IMPORTED', 'IMPORTING', 'FAILED'

`time_started`

(required) The date and time the request was started. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_completed`

(optional) The date and time the request was finished. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_deployment_wallets_operation_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_COLLECTION_T Type

A list of deployment wallets operations.

Syntax
```

```

Fields

Field Description

`items`

(required) An array of DeploymentWallets operations.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ELASTICSEARCH_CONNECTION_T Type

Represents the metadata of a Elasticsearch Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_elasticsearch_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Elasticsearch technology type.

Allowed values are: 'ELASTICSEARCH'

`servers`

(required) Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Used for establishing the initial connection to the Elasticsearch cluster. Example: `\"server1.example.com:4000,server2.example.com:4000\"`

`security_protocol`

(required) Security protocol for Elasticsearch

Allowed values are: 'PLAIN', 'TLS'

`authentication_type`

(required) Authentication type for Elasticsearch.

Allowed values are: 'NONE', 'BASIC'

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ELASTICSEARCH_CONNECTION_SUMMARY_T Type

Summary of the Elasticsearch Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_elasticsearch_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Elasticsearch technology type.

`servers`

(required) Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Used for establishing the initial connection to the Elasticsearch cluster. Example: `\"server1.example.com:4000,server2.example.com:4000\"`

`security_protocol`

(required) Security protocol for Elasticsearch.

`authentication_type`

(required) Authentication type for Elasticsearch.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ERROR_T Type

Error information.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_GOLDEN_GATE_EXPORT_DEPLOYMENT_WALLET_DETAILS_T Type

Metadata required to export wallet from deployment

Syntax
```

```

Fields

Field Description

`vault_id`

(required) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`master_encryption_key_id`

(required) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`secret_name`

(required) Name of the secret with which secret is shown in vault

`description`

(optional) Metadata about this specific object.

### DBMS_CLOUD_OCI_GOLDEN_GATE_GENERIC_CONNECTION_T Type

Represents the metadata of a Generic Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_generic_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Generic technology type.

Allowed values are: 'GENERIC'

`host`

(required) Host and port separated by colon. Example: `\"server.example.com:1234\"` For multiple hosts, provide a comma separated list. Example: `\"server1.example.com:1000,server1.example.com:2000\"`

### DBMS_CLOUD_OCI_GOLDEN_GATE_GENERIC_CONNECTION_SUMMARY_T Type

Summary of the Generic Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_generic_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Generic technology type.

`host`

(required) Host and port separated by colon. Example: `\"server.example.com:1234\"` For multiple hosts, provide a comma separated list. Example: `\"server1.example.com:1000,server1.example.com:2000\"`

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOLDEN_GATE_CONNECTION_T Type

Represents the metadata of a GoldenGate Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_golden_gate_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The GoldenGate technology type.

Allowed values are: 'GOLDENGATE'

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username credential existing in the Oracle GoldenGate used to be connected to.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOLDEN_GATE_CONNECTION_SUMMARY_T Type

Summary of the GoldenGate Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_golden_gate_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The GoldenGate technology type.

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username credential existing in the Oracle GoldenGate used to be connected to.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_BIG_QUERY_CONNECTION_T Type

Represents the metadata of a Google BigQuery Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_google_big_query_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Google BigQuery technology type.

Allowed values are: 'GOOGLE_BIGQUERY'

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_BIG_QUERY_CONNECTION_SUMMARY_T Type

Summary of the Google BigQuery Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_google_big_query_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Google BigQuery technology type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_CLOUD_STORAGE_CONNECTION_T Type

Represents the metadata of a Google Cloud Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_google_cloud_storage_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Google Cloud Storage technology type.

Allowed values are: 'GOOGLE_CLOUD_STORAGE'

### DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_CLOUD_STORAGE_CONNECTION_SUMMARY_T Type

Summary of the Google Cloud Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_google_cloud_storage_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Google Cloud Storage technology type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_HDFS_CONNECTION_T Type

Represents the metadata of a Hadoop Distributed File System Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_hdfs_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Hadoop Distributed File System technology type.

Allowed values are: 'HDFS'

### DBMS_CLOUD_OCI_GOLDEN_GATE_HDFS_CONNECTION_SUMMARY_T Type

Summary of the Hadoop Distributed File System Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_hdfs_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Hadoop Distributed File System technology type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_IMPORT_DEPLOYMENT_WALLET_DETAILS_T Type

Metadata required to import wallet to deployment

Syntax
```

```

Fields

Field Description

`vault_id`

(required) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`new_wallet_secret_id`

(required) The OCID of the customer's GoldenGate Service Secret. If provided, it references a key that customers will be required to ensure the policies are established to permit GoldenGate to use this Secret.

`wallet_backup_secret_name`

(optional) Name of the secret with which secret is shown in vault

`master_encryption_key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`description`

(optional) Metadata about this specific object.

### DBMS_CLOUD_OCI_GOLDEN_GATE_JAVA_MESSAGE_SERVICE_CONNECTION_T Type

Represents the metadata of a Java Message Service Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_java_message_service_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Java Message Service technology type.

Allowed values are: 'ORACLE_WEBLOGIC_JMS'

`should_use_jndi`

(required) If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.

`jndi_connection_factory`

(optional) The Connection Factory can be looked up using this name. e.g.: 'ConnectionFactory'

`jndi_provider_url`

(optional) The URL that Java Message Service will use to contact the JNDI provider. e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'

`jndi_initial_context_factory`

(optional) The implementation of javax.naming.spi.InitialContextFactory interface that the client uses to obtain initial naming context. e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'

`jndi_security_principal`

(optional) Specifies the identity of the principal (user) to be authenticated. e.g.: 'admin2'

`connection_url`

(optional) Connectin URL of the Java Message Service, specifying the protocol, host, and port. e.g.: 'mq://myjms.host.domain:7676'

`connection_factory`

(optional) The of Java class implementing javax.jms.ConnectionFactory interface supplied by the Java Message Service provider. e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'

`security_protocol`

(optional) Security protocol for Java Message Service. If not provided, default is PLAIN. Optional until 2024-06-27, in the release after it will be made required.

Allowed values are: 'PLAIN', 'TLS', 'MTLS'

`authentication_type`

(optional) Authentication type for Java Message Service. If not provided, default is NONE. Optional until 2024-06-27, in the release after it will be made required.

Allowed values are: 'NONE', 'BASIC'

`username`

(optional) The username Oracle GoldenGate uses to connect to the Java Message Service. This username must already exist and be available by the Java Message Service to be connected to.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_JAVA_MESSAGE_SERVICE_CONNECTION_SUMMARY_T Type

Summary of the Java Message Service Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_java_message_service_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Java Message Service technology type.

`should_use_jndi`

(required) If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.

`jndi_connection_factory`

(optional) The Connection Factory can be looked up using this name. e.g.: 'ConnectionFactory'

`jndi_provider_url`

(optional) The URL that Java Message Service will use to contact the JNDI provider. e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'

`jndi_initial_context_factory`

(optional) The implementation of javax.naming.spi.InitialContextFactory interface that the client uses to obtain initial naming context. e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'

`jndi_security_principal`

(optional) Specifies the identity of the principal (user) to be authenticated. e.g.: 'admin2'

`connection_url`

(optional) Connectin URL of the Java Message Service, specifying the protocol, host, and port. e.g.: 'mq://myjms.host.domain:7676'

`connection_factory`

(optional) The of Java class implementing javax.jms.ConnectionFactory interface supplied by the Java Message Service provider. e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'

`security_protocol`

(optional) Security protocol for Java Message Service. If not provided, default is PLAIN. Optional until 2024-06-27, in the release after it will be made required.

`authentication_type`

(optional) Authentication type for Java Message Service. If not provided, default is NONE. Optional until 2024-06-27, in the release after it will be made required.

`username`

(optional) The username Oracle GoldenGate uses to connect to the Java Message Service. This username must already exist and be available by the Java Message Service to be connected to.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_CONNECTION_T Type

Represents the metadata of a Kafka Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_kafka_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka technology type.

Allowed values are: 'APACHE_KAFKA', 'AZURE_EVENT_HUBS', 'CONFLUENT_KAFKA', 'OCI_STREAMING'

`stream_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream pool being referenced.

`bootstrap_servers`

(optional) Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

`security_protocol`

(optional) Kafka security protocol.

Allowed values are: 'SSL', 'SASL_SSL', 'PLAINTEXT', 'SASL_PLAINTEXT'

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_CONNECTION_SUMMARY_T Type

Summary of the Kafka Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_kafka_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka technology type.

`stream_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream pool being referenced.

`bootstrap_servers`

(optional) Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

`security_protocol`

(optional) Security Type for Kafka.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_T Type

Represents the metadata of a Kafka (e.g. Confluent) Schema Registry Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_kafka_schema_registry_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka (e.g. Confluent) Schema Registry technology type.

Allowed values are: 'CONFLUENT_SCHEMA_REGISTRY'

`url`

(required) Kafka Schema Registry URL.

`authentication_type`

(required) Used authentication mechanism to access Schema Registry.

Allowed values are: 'NONE', 'BASIC', 'MUTUAL'

`username`

(optional) The username to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_SUMMARY_T Type

Summary of the Kafka (e.g. Confluent) Schema Registry Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_kafka_schema_registry_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Kafka (e.g. Confluent) Schema Registry technology type.

`url`

(required) Kafka Schema Registry URL.

`authentication_type`

(required) Used authentication mechanism to access Schema Registry.

`username`

(optional) The username to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MICROSOFT_SQLSERVER_CONNECTION_T Type

Represents the metadata of a Microsoft SQL Server Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_microsoft_sqlserver_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Microsoft SQL Server technology type.

Allowed values are: 'AMAZON_RDS_SQLSERVER', 'AZURE_SQLSERVER_MANAGED_INSTANCE', 'AZURE_SQLSERVER_NON_MANAGED_INSTANCE', 'GOOGLE_CLOUD_SQL_SQLSERVER', 'MICROSOFT_SQLSERVER'

`username`

(required) The username Oracle GoldenGate uses to connect to the Microsoft SQL Server. This username must already exist and be available by the Microsoft SQL Server to be connected to.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`database_name`

(required) The name of the database.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security Protocol for Microsoft SQL Server.

Allowed values are: 'PLAIN', 'TLS'

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1-way SSL).

`should_validate_server_certificate`

(optional) If set to true, the driver validates the certificate that is sent by the database server.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MICROSOFT_SQLSERVER_CONNECTION_SUMMARY_T Type

Summary of the Microsoft SQL Server Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_microsoft_sqlserver_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Microsoft SQL Server technology type.

`database_name`

(required) The name of the database.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`username`

(required) The username Oracle GoldenGate uses to connect to the Microsoft SQL Server. This username must already exist and be available by the Microsoft SQL Server to be connected to.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security Type for Microsoft SQL Server.

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1-way SSL).

`should_validate_server_certificate`

(optional) If set to true, the driver validates the certificate that is sent by the database server.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MONGO_DB_CONNECTION_T Type

Represents the metadata of a MongoDB Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_mongo_db_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The MongoDB technology type.

Allowed values are: 'MONGODB', 'OCI_AUTONOMOUS_JSON_DATABASE', 'AZURE_COSMOS_DB_FOR_MONGODB'

`connection_string`

(optional) MongoDB connection string. e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'

`username`

(optional) The username Oracle GoldenGate uses to connect to the database. This username must already exist and be available by the database to be connected to.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Autonomous Json Database.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MONGO_DB_CONNECTION_SUMMARY_T Type

Summary of the MongoDB Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_mongo_db_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The MongoDB technology type.

`connection_string`

(optional) MongoDB connection string. e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'

`username`

(optional) The username Oracle GoldenGate uses to connect to the database. This username must already exist and be available by the database to be connected to.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Autonomous Json Database.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MYSQL_CONNECTION_T Type

Represents the metadata of a MySQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_mysql_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The MySQL technology type.

Allowed values are: 'AMAZON_AURORA_MYSQL', 'AMAZON_RDS_MARIADB', 'AMAZON_RDS_MYSQL', 'AZURE_MYSQL', 'GOOGLE_CLOUD_SQL_MYSQL', 'MARIADB', 'MYSQL_SERVER', 'OCI_MYSQL', 'SINGLESTOREDB', 'SINGLESTOREDB_CLOUD'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`database_name`

(optional) The name of the database.

`security_protocol`

(required) Security Protocol for MySQL.

Allowed values are: 'PLAIN', 'TLS', 'MTLS'

`ssl_mode`

(optional) SSL modes for MySQL.

Allowed values are: 'DISABLED', 'PREFERRED', 'REQUIRED', 'VERIFY_CA', 'VERIFY_IDENTITY'

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_MYSQL_CONNECTION_SUMMARY_T Type

Summary of the MySQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_mysql_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The MySQL technology type.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`database_name`

(optional) The name of the database.

`security_protocol`

(required) Security Type for MySQL.

`ssl_mode`

(optional) SSL modes for MySQL.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_OCI_OBJECT_STORAGE_CONNECTION_T Type

Represents the metadata of an OCI Object Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oci_object_storage_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The OCI Object Storage technology type.

Allowed values are: 'OCI_OBJECT_STORAGE'

`tenancy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_OCI_OBJECT_STORAGE_CONNECTION_SUMMARY_T Type

Summary of the OCI Object Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oci_object_storage_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The OCI Object Storage technology type.

`tenancy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_CONNECTION_T Type

Represents the metadata of an Oracle Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oracle_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle technology type.

Allowed values are: 'AMAZON_RDS_ORACLE', 'OCI_AUTONOMOUS_DATABASE', 'ORACLE_DATABASE', 'ORACLE_EXADATA'

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

Allowed values are: 'DIRECT', 'REDIRECT'

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_CONNECTION_SUMMARY_T Type

Summary of the Oracle Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oracle_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle technology type.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_NOSQL_CONNECTION_T Type

Represents the metadata of an Oracle NoSQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oracle_nosql_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle NoSQL technology type.

Allowed values are: 'ORACLE_NOSQL'

`tenancy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI user who will access the Oracle NoSQL database. The user must have write access to the table they want to connect to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_NOSQL_CONNECTION_SUMMARY_T Type

Summary of the Oracle NoSQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_oracle_nosql_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Oracle NoSQL technology type.

`tenancy_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the OCI user who will access the Oracle NoSQL database. The user must have write access to the table they want to connect to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_POSTGRESQL_CONNECTION_T Type

Represents the metadata of a PostgreSQL Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_postgresql_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The PostgreSQL technology type.

Allowed values are: 'POSTGRESQL_SERVER', 'AMAZON_AURORA_POSTGRESQL', 'AMAZON_RDS_POSTGRESQL', 'AZURE_POSTGRESQL', 'GOOGLE_CLOUD_SQL_POSTGRESQL'

`database_name`

(required) The name of the database.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security protocol for PostgreSQL.

Allowed values are: 'PLAIN', 'TLS', 'MTLS'

`ssl_mode`

(optional) SSL mode for PostgreSQL.

Allowed values are: 'PREFER', 'REQUIRE', 'VERIFY_CA', 'VERIFY_FULL'

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_POSTGRESQL_CONNECTION_SUMMARY_T Type

Summary of the PostgreSQL Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_postgresql_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The PostgreSQL technology type.

`database_name`

(required) The name of the database.

`host`

(required) The name or address of a host.

`port`

(required) The port of an endpoint usually specified for a connection.

`username`

(required) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(required) Security protocol for PostgreSQL.

`ssl_mode`

(optional) SSL modes for PostgreSQL.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_REDIS_CONNECTION_T Type

Represents the metadata of a Redis Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_redis_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Redis technology type.

Allowed values are: 'REDIS'

`servers`

(required) Comma separated list of Redis server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 6379. Used for establishing the initial connection to the Redis cluster. Example: `\"server1.example.com:6379,server2.example.com:6379\"`

`security_protocol`

(required) Security protocol for Redis

Allowed values are: 'PLAIN', 'TLS', 'MTLS'

`authentication_type`

(required) Authentication type for Redis.

Allowed values are: 'NONE', 'BASIC'

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_REDIS_CONNECTION_SUMMARY_T Type

Summary of the Redis Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_redis_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Redis technology type.

`servers`

(required) Comma separated list of Redis server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 6379. Used for establishing the initial connection to the Redis cluster. Example: `\"server1.example.com:6379,server2.example.com:6379\"`

`security_protocol`

(required) Security protocol for Redis.

`authentication_type`

(required) Authenticationentication type for the Redis database.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

### DBMS_CLOUD_OCI_GOLDEN_GATE_RESCHEDULE_DEPLOYMENT_UPGRADE_DETAILS_T Type

The information about canceling.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deploymentUpgrade reschedule.

Allowed values are: 'RESCHEDULE_TO_DATE'

### DBMS_CLOUD_OCI_GOLDEN_GATE_RESCHEDULE_DEPLOYMENT_UPGRADE_TO_DATE_DETAILS_T Type

Definition of the additional attributes for default deployment upgrade cancel.

Syntax
```

```

`dbms_cloud_oci_golden_gate_reschedule_deployment_upgrade_to_date_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_reschedule_deployment_upgrade_details_t`type.

Fields

Field Description

`time_schedule`

(required) The time of upgrade schedule. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_SNOWFLAKE_CONNECTION_T Type

Represents the metadata of a Snowflake Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_snowflake_connection_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_t`type.

Fields

Field Description

`technology_type`

(required) The Snowflake technology type.

Allowed values are: 'SNOWFLAKE'

`connection_url`

(required) JDBC connection URL. e.g.: 'jdbc:snowflake://&lt;account_name&gt;.snowflakecomputing.com/?warehouse=&lt;warehouse-name&gt;&amp;db=&lt;db-name&gt;'

`authentication_type`

(required) Used authentication mechanism to access Snowflake.

Allowed values are: 'BASIC', 'KEY_PAIR'

`username`

(optional) The username Oracle GoldenGate uses to connect to Snowflake. This username must already exist and be available by Snowflake platform to be connected to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_SNOWFLAKE_CONNECTION_SUMMARY_T Type

Summary of the Snowflake Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_snowflake_connection_summary_t`is a subtype of the`dbms_cloud_oci_golden_gate_connection_summary_t`type.

Fields

Field Description

`technology_type`

(required) The Snowflake technology type.

`connection_url`

(required) JDBC connection URL. e.g.: 'jdbc:snowflake://&lt;account_name&gt;.snowflakecomputing.com/?warehouse=&lt;warehouse-name&gt;&amp;db=&lt;db-name&gt;'

`authentication_type`

(required) Used authentication mechanism to access Snowflake.

`username`

(optional) The username Oracle GoldenGate uses to connect to Snowflake. This username must already exist and be available by Snowflake platform to be connected to.

### DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_ERROR_T Type

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

`issue`

(optional) The text describing the root cause of the reported issue.

`action`

(optional) The text describing the action required to fix the issue.

### DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_RESULT_T Type

The result of the connectivity test performed between the GoldenGate deployment and the associated database / service.

Syntax
```

```

Fields

Field Description

`result_type`

(required) Type of the result (i.e. Success, Failure or Timeout).

Allowed values are: 'SUCCEEDED', 'FAILED', 'TIMED_OUT'

`error`

(optional)

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_SUMMARY_T Type

Summary of the TrailFiles.

Syntax
```

```

Fields

Field Description

`trail_file_id`

(required) The TrailFile Id.

`display_name`

(optional) An object's Display Name.

`size_in_bytes`

(optional) The size of the backup stored in object storage (in bytes)

`time_last_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`number_of_sequences`

(optional) Number of sequences for a specific trail file

`min_sequence_number`

(optional) Minimum sequence number

`max_sequence_number`

(optional) Maximum sequence number

`producer`

(optional) Producer Process Name if any.

`consumers`

(optional) array of consumer process names

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_trail_file_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_COLLECTION_T Type

A list of TrailFiles.

Syntax
```

```

Fields

Field Description

`time_last_fetched`

(required) The time the data was last fetched from the deployment. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`items`

(required) An array of TrailFiles.

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_SUMMARY_T Type

Summary of the TrailSequences.

Syntax
```

```

Fields

Field Description

`sequence_id`

(required) Sequence Id

`display_name`

(optional) An object's Display Name.

`size_in_bytes`

(optional) The size of the backup stored in object storage (in bytes)

`time_last_updated`

(optional) The time the resource was last updated. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_trail_sequence_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_COLLECTION_T Type

A list of TrailSequences.

Syntax
```

```

Fields

Field Description

`time_last_fetched`

(required) The time the data was last fetched from the deployment. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`items`

(required) An array of TrailSequences.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_CONNECTION_DETAILS_T Type

The information to update a Connection.

Syntax
```

```

Fields

Field Description

`connection_type`

(optional) The connection type.

Allowed values are: 'GOLDENGATE', 'KAFKA', 'KAFKA_SCHEMA_REGISTRY', 'MYSQL', 'JAVA_MESSAGE_SERVICE', 'MICROSOFT_SQLSERVER', 'OCI_OBJECT_STORAGE', 'ORACLE', 'AZURE_DATA_LAKE_STORAGE', 'POSTGRESQL', 'AZURE_SYNAPSE_ANALYTICS', 'SNOWFLAKE', 'AMAZON_S3', 'HDFS', 'ORACLE_NOSQL', 'MONGODB', 'AMAZON_KINESIS', 'AMAZON_REDSHIFT', 'REDIS', 'ELASTICSEARCH', 'GENERIC', 'GOOGLE_CLOUD_STORAGE', 'GOOGLE_BIGQUERY'

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`vault_id`

(optional) Refers to the customer's vault OCID. If provided, it references a vault where GoldenGate can manage secrets. Customers must add policies to permit GoldenGate to manage secrets contained within this vault.

`key_id`

(optional) Refers to the customer's master key OCID. If provided, it references a key to manage secrets. Customers must add policies to permit GoldenGate to use this key.

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the target subnet of the dedicated connection.

`routing_method`

(optional) Controls the network traffic direction to the target: SHARED_SERVICE_ENDPOINT: Traffic flows through the Goldengate Service's network to public hosts. Cannot be used for private targets. SHARED_DEPLOYMENT_ENDPOINT: Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. DEDICATED_ENDPOINT: A dedicated private endpoint is created in the target VCN subnet for the connection. The subnetId is required when DEDICATED_ENDPOINT networking is selected.

Allowed values are: 'SHARED_SERVICE_ENDPOINT', 'SHARED_DEPLOYMENT_ENDPOINT', 'DEDICATED_ENDPOINT'

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_KINESIS_CONNECTION_DETAILS_T Type

The information to update a the Amazon Kinesis Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_amazon_kinesis_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`access_key_id`

(optional) Access key ID to access the Amazon Kinesis.

`secret_access_key`

(optional) Secret access key to access the Amazon Kinesis.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_REDSHIFT_CONNECTION_DETAILS_T Type

The information to update a the Amazon Redshift Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_amazon_redshift_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`connection_url`

(optional) Connection URL. e.g.: 'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_S3_CONNECTION_DETAILS_T Type

The information to update a the Amazon S3 Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_amazon_s3_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`access_key_id`

(optional) Access key ID to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

`secret_access_key`

(optional) Secret access key to access the Amazon S3 bucket. e.g.: \"this-is-not-the-secret\"

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_DETAILS_T Type

The information to update a Azure Data Lake Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_azure_data_lake_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`authentication_type`

(optional) Used authentication mechanism to access Azure Data Lake Storage.

`account_name`

(optional) Sets the Azure storage account name.

`account_key`

(optional) Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'. e.g.: pa3WbhVATzj56xD4DH1VjOUhApRGEGHvOo58eQJVWIzX+j8j4CUVFcTjpIqDSRaSa1Wo2LbWY5at+AStEgLOIQ==

`sas_token`

(optional) Credential that uses a shared access signature (SAS) to authenticate to an Azure Service. This property is required when 'authenticationType' is set to 'SHARED_ACCESS_SIGNATURE'. e.g.: ?sv=2020-06-08&amp;ss=bfqt&amp;srt=sco&amp;sp=rwdlacupyx&amp;se=2020-09-10T20:27:28Z&amp;st=2022-08-05T12:27:28Z&amp;spr=https&amp;sig=C1IgHsiLBmTSStYkXXGLTP8it0xBrArcgCqOsZbXwIQ%3D

`azure_tenant_id`

(optional) Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 14593954-d337-4a61-a364-9f758c64f97f

`client_id`

(optional) Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d

`client_secret`

(optional) Azure client secret (aka application password) for authentication. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'. e.g.: dO29Q~F5-VwnA.lZdd11xFF_t5NAXCaGwDl9NbT1

`endpoint`

(optional) Azure Storage service endpoint. e.g: https://test.blob.core.windows.net

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AZURE_SYNAPSE_CONNECTION_DETAILS_T Type

The information to update a Azure Synapse Analytics Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_azure_synapse_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`connection_string`

(optional) JDBC connection string. e.g.: 'jdbc:sqlserver://&lt;synapse-workspace&gt;.sql.azuresynapse.net:1433;database=&lt;db-name&gt;;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DATABASE_REGISTRATION_DETAILS_T Type

The information to update a DatabaseRegistration.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) An object's Display Name.

`description`

(optional) Metadata about this specific object.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`fqdn`

(optional) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

Allowed values are: 'DIRECT', 'REDIRECT'

`wallet`

(optional) The wallet contents Oracle GoldenGate uses to make connections to a database. This attribute is expected to be base64 encoded.

`alias_name`

(optional) Credential store alias.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DEPLOYMENT_BACKUP_DETAILS_T Type

The information to use to update a Deployment Backup.

Syntax
```

```

Fields

Field Description

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_OGG_DEPLOYMENT_DETAILS_T Type

Deployment Details for updating an OggDeployment

Syntax
```

```

Fields

Field Description

`credential_store`

(optional) The type of credential store for OGG.

Allowed values are: 'GOLDENGATE', 'IAM'

`identity_domain_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Identity Domain when IAM credential store is used.

`password_secret_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Secret where the deployment password is stored.

`admin_username`

(optional) The GoldenGate deployment console username.

`admin_password`

(optional) The password associated with the GoldenGate deployment console username. The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric, and 1 special character. Special characters such as '$', '^', or '?' are not allowed. This field will be deprecated and replaced by \"passwordSecretId\".

`certificate`

(optional) A PEM-encoded SSL certificate.

`key`

(optional) A PEM-encoded private key.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MAINTENANCE_WINDOW_DETAILS_T Type

Defines the maintenance window for update operation, when automatic actions can be performed.

Syntax
```

```

Fields

Field Description

`day`

(required) Days of the week.

Allowed values are: 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'

`start_hour`

(required) Start hour for maintenance period. Hour is in UTC.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MAINTENANCE_CONFIGURATION_DETAILS_T Type

Defines the maintenance configuration for update operation.

Syntax
```

```

Fields

Field Description

`is_interim_release_auto_upgrade_enabled`

(optional) By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interimReleaseUpgradePeriodInDays too.

`interim_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.

`bundle_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.

`major_release_upgrade_period_in_days`

(optional) Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default.

`security_patch_upgrade_period_in_days`

(optional) Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DEPLOYMENT_DETAILS_T Type

The information to use to update a Deployment.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) An object's Display Name.

`license_model`

(optional) The Oracle license model that applies to a Deployment.

Allowed values are: 'LICENSE_INCLUDED', 'BRING_YOUR_OWN_LICENSE'

`description`

(optional) Metadata about this specific object.

`freeform_tags`

(optional) A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Tags defined for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`nsg_ids`

(optional) An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.

`subnet_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the subnet of the deployment's private endpoint.

`is_public`

(optional) True if this object is publicly available.

`fqdn`

(optional) A three-label Fully Qualified Domain Name (FQDN) for a resource.

`cpu_core_count`

(optional) The Minimum number of OCPUs to be made available for this Deployment.

`is_auto_scaling_enabled`

(optional) Indicates if auto scaling is enabled for the Deployment's CPU core count.

`ogg_data`

(optional)

`maintenance_window`

(optional)

`maintenance_configuration`

(optional)

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ELASTICSEARCH_CONNECTION_DETAILS_T Type

The information to update a Elasticsearch Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_elasticsearch_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`servers`

(optional) Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Used for establishing the initial connection to the Elasticsearch cluster. Example: `\"server1.example.com:4000,server2.example.com:4000\"`

`security_protocol`

(optional) Security protocol for Elasticsearch.

`authentication_type`

(optional) Authentication type for Elasticsearch.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`fingerprint`

(optional) Fingerprint required by TLS security protocol. Eg.: '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GENERIC_CONNECTION_DETAILS_T Type

The information to update a Generic Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_generic_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`host`

(optional) Host and port separated by colon. Example: `\"server.example.com:1234\"` For multiple hosts, provide a comma separated list. Example: `\"server1.example.com:1000,server1.example.com:2000\"`

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOLDEN_GATE_CONNECTION_DETAILS_T Type

The information to update a GoldenGate Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_golden_gate_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`deployment_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the deployment being referenced.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username credential existing in the Oracle GoldenGate used to be connected to.

`password`

(optional) The password used to connect to the Oracle GoldenGate accessed trough this connection.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOOGLE_BIG_QUERY_CONNECTION_DETAILS_T Type

The information to update a the Google BigQuery Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_google_big_query_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`service_account_key_file`

(optional) The base64 encoded content of the service account key file containing the credentials required to use Google BigQuery.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOOGLE_CLOUD_STORAGE_CONNECTION_DETAILS_T Type

The information to update a the Google Cloud Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_google_cloud_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`service_account_key_file`

(optional) The base64 encoded content of the service account key file containing the credentials required to use Google Cloud Storage.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_HDFS_CONNECTION_DETAILS_T Type

The information to update a Hadoop Distributed File System Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_hdfs_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`core_site_xml`

(optional) The base64 encoded content of the Hadoop Distributed File System configuration file (core-site.xml).

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_JAVA_MESSAGE_SERVICE_CONNECTION_DETAILS_T Type

The information to update a Java Message Service Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_java_message_service_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`should_use_jndi`

(optional) If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.

`jndi_connection_factory`

(optional) The Connection Factory can be looked up using this name. e.g.: 'ConnectionFactory'

`jndi_provider_url`

(optional) The URL that Java Message Service will use to contact the JNDI provider. e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'

`jndi_initial_context_factory`

(optional) The implementation of javax.naming.spi.InitialContextFactory interface that the client uses to obtain initial naming context. e.g.: 'org.apache.activemq.jndi.ActiveMQInitialContextFactory'

`jndi_security_principal`

(optional) Specifies the identity of the principal (user) to be authenticated. e.g.: 'admin2'

`jndi_security_credentials`

(optional) The password associated to the principal.

`connection_url`

(optional) Connectin URL of the Java Message Service, specifying the protocol, host, and port. e.g.: 'mq://myjms.host.domain:7676'

`connection_factory`

(optional) The of Java class implementing javax.jms.ConnectionFactory interface supplied by the Java Message Service provider. e.g.: 'com.stc.jmsjca.core.JConnectionFactoryXA'

`username`

(optional) The username Oracle GoldenGate uses to connect to the Java Message Service. This username must already exist and be available by the Java Message Service to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated Java Message Service.

`security_protocol`

(optional) Security protocol for Java Message Service. If not provided, default is PLAIN. Optional until 2024-06-27, in the release after it will be made required.

`authentication_type`

(optional) Authentication type for Java Message Service. If not provided, default is NONE. Optional until 2024-06-27, in the release after it will be made required.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_KAFKA_CONNECTION_DETAILS_T Type

The information to update a Kafka Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_kafka_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`stream_pool_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the stream pool being referenced.

`bootstrap_servers`

(optional) Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: `\"server1.example.com:9092,server2.example.com:9092\"`

`security_protocol`

(optional) Security Type for Kafka.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided.

`consumer_properties`

(optional) The base64 encoded content of the consumer.properties file.

`producer_properties`

(optional) The base64 encoded content of the producer.properties file.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_DETAILS_T Type

The information to update Kafka (e.g. Confluent) Schema Registry Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_kafka_schema_registry_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`url`

(optional) Kafka Schema Registry URL.

`authentication_type`

(optional) Used authentication mechanism to access Schema Registry.

`username`

(optional) The username to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`password`

(optional) The password to access Schema Registry using basic authentation. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

`ssl_key_password`

(optional) The password for the cert inside the KeyStore. In case it differs from the KeyStore password, it should be provided.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MICROSOFT_SQLSERVER_CONNECTION_DETAILS_T Type

The information to update a Microsoft SQL Server Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_microsoft_sqlserver_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`database_name`

(optional) The name of the database.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username Oracle GoldenGate uses to connect to the Microsoft SQL Server. This username must already exist and be available by the Microsoft SQL Server to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(optional) Security Type for Microsoft SQL Server.

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1-way SSL).

`should_validate_server_certificate`

(optional) If set to true, the driver validates the certificate that is sent by the database server.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MONGO_DB_CONNECTION_DETAILS_T Type

The information to update a MongoDB Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_mongo_db_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`connection_string`

(optional) MongoDB connection string. e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'

`username`

(optional) The username Oracle GoldenGate uses to connect to the database. This username must already exist and be available by the database to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated database.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the Oracle Autonomous Json Database.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MYSQL_CONNECTION_DETAILS_T Type

The information to update a MySQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_mysql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`database_name`

(optional) The name of the database.

`security_protocol`

(optional) Security Type for MySQL.

`ssl_mode`

(optional) SSL modes for MySQL.

`ssl_ca`

(optional) Database Certificate - The base64 encoded content of a .pem or .crt file. containing the server public key (for 1 and 2-way SSL).

`ssl_crl`

(optional) The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA). Note: This is an optional property and only applicable if TLS/MTLS option is selected.

`ssl_cert`

(optional) Client Certificate - The base64 encoded content of a .pem or .crt file. containing the client public key (for 2-way SSL).

`ssl_key`

(optional) Client Key – The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL).

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`db_system_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database system being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_OCI_OBJECT_STORAGE_CONNECTION_DETAILS_T Type

The information to update a OCI Object Storage Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_oci_object_storage_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`tenancy_id`

(optional) The OCID of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(optional) The OCID of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.

`private_key_file`

(optional) The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.

`private_key_passphrase`

(optional) The passphrase of the private key.

`public_key_fingerprint`

(optional) The fingerprint of the API Key of the user specified by the userId.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ORACLE_CONNECTION_DETAILS_T Type

The information to update an Oracle Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_oracle_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`connection_string`

(optional) Connect descriptor or Easy Connect Naming method used to connect to a database.

`wallet`

(optional) The wallet contents Oracle GoldenGate uses to make connections to a database. This attribute is expected to be base64 encoded.

`session_mode`

(optional) The mode of the database connection session to be established by the data client. 'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database. Connection to a RAC database involves a redirection received from the SCAN listeners to the database node to connect to. By default the mode would be DIRECT.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

`database_id`

(optional) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the database being referenced.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ORACLE_NOSQL_CONNECTION_DETAILS_T Type

The information to update a Oracle NoSQL Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_oracle_nosql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`tenancy_id`

(optional) The OCID of the related OCI tenancy.

`l_region`

(optional) The name of the region. e.g.: us-ashburn-1

`user_id`

(optional) The OCID of the OCI user who will access the Oracle NoSQL database. The user must have write access to the table they want to connect to.

`private_key_file`

(optional) The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.

`private_key_passphrase`

(optional) The passphrase of the private key.

`public_key_fingerprint`

(optional) The fingerprint of the API Key of the user specified by the userId.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_POSTGRESQL_CONNECTION_DETAILS_T Type

The information to update a PostgreSQL Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_postgresql_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`database_name`

(optional) The name of the database.

`host`

(optional) The name or address of a host.

`port`

(optional) The port of an endpoint usually specified for a connection.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`additional_attributes`

(optional) An array of name-value pair attribute entries. Used as additional parameters in connection string.

`security_protocol`

(optional) Security protocol for PostgreSQL.

`ssl_mode`

(optional) SSL modes for PostgreSQL.

`ssl_ca`

(optional) The base64 encoded certificate of the trusted certificate authorities (Trusted CA) for PostgreSQL. The supported file formats are .pem and .crt.

`ssl_crl`

(optional) The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).

`ssl_cert`

(optional) The base64 encoded certificate of the PostgreSQL server. The supported file formats are .pem and .crt.

`ssl_key`

(optional) The base64 encoded private key of the PostgreSQL server. The supported file formats are .pem and .crt.

`private_ip`

(optional) Deprecated: this field will be removed in future versions. Either specify the private IP in the connectionString or host field, or make sure the host name is resolvable in the target VCN. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_REDIS_CONNECTION_DETAILS_T Type

The information to update a Redis Database Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_redis_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`servers`

(optional) Comma separated list of Redis server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 6379. Used for establishing the initial connection to the Redis cluster. Example: `\"server1.example.com:6379,server2.example.com:6379\"`

`security_protocol`

(optional) Security protocol for Redis.

`authentication_type`

(optional) Authenticationentication type for the Redis database.

`username`

(optional) The username Oracle GoldenGate uses to connect the associated system of the given technology. This username must already exist and be available by the system/application to be connected to and must conform to the case sensitivty requirments defined in it.

`password`

(optional) The password Oracle GoldenGate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on.

`trust_store`

(optional) The base64 encoded content of the TrustStore file.

`trust_store_password`

(optional) The TrustStore password.

`key_store`

(optional) The base64 encoded content of the KeyStore file.

`key_store_password`

(optional) The KeyStore password.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_SNOWFLAKE_CONNECTION_DETAILS_T Type

The information to update a Snowflake Connection.

Syntax
```

```

`dbms_cloud_oci_golden_gate_update_snowflake_connection_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_update_connection_details_t`type.

Fields

Field Description

`connection_url`

(optional) JDBC connection URL. e.g.: 'jdbc:snowflake://&lt;account_name&gt;.snowflakecomputing.com/?warehouse=&lt;warehouse-name&gt;&amp;db=&lt;db-name&gt;'

`authentication_type`

(optional) Used authentication mechanism to access Snowflake.

`username`

(optional) The username Oracle GoldenGate uses to connect to Snowflake. This username must already exist and be available by Snowflake platform to be connected to.

`password`

(optional) The password Oracle GoldenGate uses to connect to Snowflake platform.

`private_key_file`

(optional) The base64 encoded content of private key file in PEM format.

`private_key_passphrase`

(optional) Password if the private key file is encrypted.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_DETAILS_T Type

The information about the Upgrade for a Deployment.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The type of a deployment upgrade

Allowed values are: 'CURRENT_RELEASE', 'SPECIFIC_RELEASE'

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_CURRENT_RELEASE_DETAILS_T Type

Definition of the additional attributes for a Current Release upgrade.

Syntax
```

```

`dbms_cloud_oci_golden_gate_upgrade_deployment_current_release_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_upgrade_deployment_details_t`type.

### DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_SPECIFIC_RELEASE_DETAILS_T Type

Definition of the additional attributes for a Specific Release upgrade.

Syntax
```

```

`dbms_cloud_oci_golden_gate_upgrade_deployment_specific_release_details_t`is a subtype of the`dbms_cloud_oci_golden_gate_upgrade_deployment_details_t`type.

Fields

Field Description

`ogg_version`

(required) Version of OGG

### DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. When you create, update, or delete a resource, it remains in the IN_PROGRESS state until work is complete for that resource. It then transitions to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'RELATED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that you perform a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_golden_gate_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_T Type

The API operations that create and configure GoldenGate resources do not take effect immediately. In these cases, the operation spawns an asynchronous workflow to fulfill the request. Work requests provide visibility into the status of these in-progress, long-running asynchronous workflows.

Syntax
```

```

Fields

Field Description

`operation_type`

(required) The work request's operation type.

Allowed values are: 'GOLDENGATE_DATABASE_REGISTRATION_CREATE', 'GOLDENGATE_DATABASE_REGISTRATION_UPDATE', 'GOLDENGATE_DATABASE_REGISTRATION_DELETE', 'GOLDENGATE_DATABASE_REGISTRATION_MOVE', 'GOLDENGATE_DEPLOYMENT_CREATE', 'GOLDENGATE_DEPLOYMENT_UPDATE', 'GOLDENGATE_DEPLOYMENT_DELETE', 'GOLDENGATE_DEPLOYMENT_MOVE', 'GOLDENGATE_DEPLOYMENT_RESTORE', 'GOLDENGATE_DEPLOYMENT_START', 'GOLDENGATE_DEPLOYMENT_STOP', 'GOLDENGATE_DEPLOYMENT_UPGRADE', 'GOLDENGATE_DEPLOYMENT_BACKUP_CREATE', 'GOLDENGATE_DEPLOYMENT_BACKUP_DELETE', 'GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL', 'GOLDENGATE_DEPLOYMENT_BACKUP_COPY', 'GOLDENGATE_CONNECTION_CREATE', 'GOLDENGATE_CONNECTION_UPDATE', 'GOLDENGATE_CONNECTION_DELETE', 'GOLDENGATE_CONNECTION_MOVE', 'GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE', 'GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE', 'GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT', 'GOLDENGATE_DEPLOYMENT_WALLET_EXPORT', 'GOLDENGATE_DEPLOYMENT_WALLET_IMPORT', 'GOLDENGATE_DEPLOYMENT_UPGRADE_UPGRADE', 'GOLDENGATE_DEPLOYMENT_UPGRADE_ROLLBACK', 'GOLDENGATE_DEPLOYMENT_UPGRADE_SNOOZE', 'GOLDENGATE_DEPLOYMENT_CERTIFICATE_CREATE', 'GOLDENGATE_DEPLOYMENT_CERTIFICATE_DELETE'

`status`

(required) Status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.

`resources`

(required) The resources affected by this work request.

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_started`

(optional) The date and time the request was started. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

`time_finished`

(optional) The date and time the request was finished. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm).

`message`

(required) A human-readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

### DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. The format is defined by[RFC3339](https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.

- [Golden Gate Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-197E4544-9D5B-4E14-96C6-F9CC8E3A547E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6DC121B7-49DC-40F3-80DC-644B276AE9AC)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_INGRESS_IP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-42833DC8-6329-42C6-AC20-F9BB39534B3B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_INGRESS_IP_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C9DCD9CD-0F0C-498F-81D6-C19B33A9E9A8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-D244260F-F282-4B75-83DB-873A60E9299B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_KINESIS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E0E4AE62-06B1-4E53-B18D-DECFBFB9D806)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-8248C52A-AB73-4E96-B49D-BA20C1095927)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_KINESIS_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4080371B-9C8E-4C65-A6BD-BE653E7B8376)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_REDSHIFT_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-D4AC7D5F-F396-4D4B-BE1C-8164BDDA8859)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_REDSHIFT_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-50141697-8B78-4A88-AA0B-8D5BC349AC5A)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_S3_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-D2E3D180-B0F3-467F-9377-DD7E8F916E44)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AMAZON_S3_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-88FD7419-D4EF-4A22-AAC1-AF9AA94E8836)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-9FAEB14F-CFE5-447C-9610-FE66EE9B08FB)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-58BCBC44-BF4B-4854-8DB4-8B29864BFA3F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_SYNAPSE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FA42E60F-AB23-4269-8D43-7429A8FF1341)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_AZURE_SYNAPSE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AEBE2B28-7309-45B3-863C-B8C91AF27162)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_DEPLOYMENT_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-CDDE83CF-3161-4BDE-B0A5-B09EAA96D9FE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-089A551F-7DCD-4B34-8D4B-99AB26DC60B7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CANCEL_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-761A50AB-D5CA-4AFC-ACE1-79665104B85F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AC9E0043-222E-4826-8575-DAE375EFAF19)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4B0EF954-079C-4402-ACFD-2C17EBB5DD67)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-DEC6475A-D22B-40C1-9A53-B8C06A1AB830)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CERTIFICATE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3EC16DC4-671D-4617-BB12-8B20A2DA2FDF)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_CONNECTION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-942640BA-FF99-47C5-8001-355B5EC85CC3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DATABASE_REGISTRATION_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E76F3436-DF1D-4DA4-B823-FFBB9827F3E3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DEPLOYMENT_BACKUP_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A41606CE-1014-4E1B-A630-B96A1E1DE602)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CHANGE_DEPLOYMENT_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-24000F3B-BD5A-43BC-814F-C10E2CBC0953)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_COLLECT_DEPLOYMENT_DIAGNOSTIC_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-62F980E7-0735-4399-89CB-C4A2956CFA16)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-D355203C-249E-43F2-A8DE-433808E532EA)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-808CA283-8507-439A-8819-79F7086D155C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F735623B-DF2A-45F4-9025-CBFDB3A42BEF)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_ASSIGNMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3CD88BB4-6375-4CF0-82D2-3187808AA690)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FDCA119B-4965-431B-926C-0BFA934124F2)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CONNECTION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AF1977AD-E3E5-42CC-8936-349DC8743F63)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_COPY_DEPLOYMENT_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-CD79DAD8-D4E2-491F-BA9F-EDB74BC7AEE1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-56EE1CCA-C541-4602-BD43-C8C38051BE5F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_KINESIS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-ED7B2FF7-F096-4ADD-B182-5C99783F0A8F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_REDSHIFT_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0E2A8E05-E4C1-40D4-A860-376D8C167635)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AMAZON_S3_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1FF13B21-4729-4B59-B70B-C09287C424AD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-53B10BE2-7BC0-4B4D-B640-3ADCCB925C44)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_AZURE_SYNAPSE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4495A506-7AC4-48BF-A3F7-43C03F739129)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CERTIFICATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6345395C-B898-487A-9FED-661D15FE98B8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_CONNECTION_ASSIGNMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1DE206F3-3DFB-45AA-B7B4-8E5B4B4E69DC)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DATABASE_REGISTRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-03255367-AA12-40F1-9DF7-0C89E816C55D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DEPLOYMENT_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-D2B83557-565D-492B-A158-1C325B9569C8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_OGG_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-ECED6080-9007-4EAA-90AE-0FBEF7C163BD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MAINTENANCE_WINDOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-51C246DA-92F4-43CC-8824-794D85F50E34)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MAINTENANCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-388EC51F-D570-4726-B585-90C79112DF4B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-BDBB5526-43E3-41FB-9025-D5A235319694)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ELASTICSEARCH_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AD0E88F0-2622-472B-A413-86333FFE435E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GENERIC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-9400DA40-0D17-48CF-BC65-06B70020922D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOLDEN_GATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-53091341-1385-40F8-A30A-54C26E02D7ED)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOOGLE_BIG_QUERY_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-630790CB-CFBE-4A7B-A0F0-06A607FC680C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_GOOGLE_CLOUD_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FB9FD9A2-F9D4-4A36-89DA-34384E7DD213)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_HDFS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A79B1F2B-5551-4F22-8C07-6407494588BD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_JAVA_MESSAGE_SERVICE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5710FA3C-9047-42C2-81E1-D2836FD147E8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_BOOTSTRAP_SERVER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-39D94F3E-7510-4EEE-922D-681812C3BFEE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_BOOTSTRAP_SERVER_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-37F0A322-BCD6-4C8F-BE36-9E098CF39E02)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_KAFKA_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-8571F751-8935-48D6-86AF-58504DBA6D0D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1EC954B3-5C7A-4595-90BE-63A283CE9976)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_NAME_VALUE_PAIR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4B66CCBB-D891-4EED-B636-1489C08DA57B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_NAME_VALUE_PAIR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4F76DAC9-A947-4405-94F6-7D1A3991272F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MICROSOFT_SQLSERVER_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A84ACE1F-D20F-4FA6-946E-0BC403F77EC9)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MONGO_DB_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3533A485-EF6C-4450-BF6D-762D0C1DC7E7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_MYSQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-43129ED5-A651-4C90-A36E-AEDD66639075)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_OCI_OBJECT_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-9BBC7E7E-4457-485E-A61C-B161AC9F2B5D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ORACLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7444D66C-3610-414B-AF75-4A6426122076)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_ORACLE_NOSQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-BCD5C9CB-2B33-4EA4-8E0E-7975F1328F0C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_POSTGRESQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5C2F88DA-D309-41D5-B7B5-252C345FDEF3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_REDIS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-2D1F04C8-70F4-4443-8842-8187B8E3B104)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_CREATE_SNOWFLAKE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B07D282C-BC18-4869-B220-FE5833111017)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-748F6894-C911-4165-9E57-B702B918C499)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-56C8C042-8E5E-4E28-95CA-F194C5C9FAE8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-34EB34A2-4CD1-4A5A-AC20-7ABD0D2AC53D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DATABASE_REGISTRATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B7BB222D-DD96-4DEE-ABC7-21F8B4DC3491)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_DEPLOYMENT_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C90C6D30-C2CB-4E66-8D5A-02D52DCBFCD3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-09974E39-F1B2-4F5B-974A-76B0DFFBED84)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_CANCEL_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E7F9BC67-9959-43A0-9370-CED290D8B770)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLET_EXISTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-29572CDF-5B8F-475B-8262-4AACFFBF60C8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_DEPLOYMENT_WALLET_EXISTS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E9BDA951-FF9C-40D3-8E12-79BF9232E2A5)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_RESTORE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FF5F194F-3DB1-437F-B27D-CB7C07A8DDEB)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_RESTORE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B8487211-B5D0-4203-8CBF-B0A40B21AA2D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ROLLBACK_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-94079DAF-7DD9-4F4C-ADE1-E0ED084BBBEE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_ROLLBACK_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5AC9C057-7E12-433C-AA29-92B224A3EDAF)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7E724043-7CF8-4803-A886-41D9E4DF3073)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_SNOOZE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7EB9B86D-E8E5-4195-89AA-DD21918EA109)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_START_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B01020BD-9CD0-4A2B-BF5A-221AFAAD9E6E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_START_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5BA50A64-A31E-4682-B117-7C5E03F3C7C6)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_STOP_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-655F1891-665F-478A-86A0-47CCF556516F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_STOP_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1D5D088B-002E-4C20-B2ED-6F0AEC514F63)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A101DA80-4C1D-48EB-98A3-A8EDB8E0D01E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_TEST_CONNECTION_ASSIGNMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-441383E0-9184-4009-BFB4-2BA06E74CEDD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-35B79628-53D1-4DBE-AF5F-947EBD7773D7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEFAULT_UPGRADE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6FB32C5C-1836-41E8-8AD6-C1752BB9FFA2)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_OGG_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-8E10C6FF-55DC-4494-B3C3-4AE50BE4D42E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_DIAGNOSTIC_DATA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-05077345-7803-4A36-97CA-950787948B70)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MAINTENANCE_WINDOW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-01B815CC-1666-46EA-99DC-2E50096B990F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MAINTENANCE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-51A8795D-F64A-436B-9D53-37D1E76141BB)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-163EFD29-82A3-41BE-915E-A530ABD40284)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E6CE94F0-9DEE-4437-98A1-36FA248A36F9)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6D4CCACC-6986-49CB-9448-986C89A67CBC)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0B163773-3A31-446D-9200-D7B444D342C6)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_BACKUP_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-50AC91D5-65AB-4309-BC71-528847C184D0)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-DC702283-535A-42DC-AAAA-908E83074261)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C082AE13-EA39-48F7-B06B-69572149B641)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-679D1B4A-1DFC-439D-B9A9-82F525AD7998)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MESSAGE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AB8E1C1C-CD56-4738-B904-C0F61C4129AE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MESSAGE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4A962567-0927-4579-8964-E958C3B39250)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_MESSAGE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C63FDD7E-A42D-4475-8942-702CC8405F39)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5FEF8FDB-81A7-4F5E-AB39-F0B748DB7998)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-999E03CB-40BD-411D-BF9D-EE2FE2BC65DA)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-52D6199F-B582-4221-B608-522A07682B68)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-DDF941A3-FFC0-4FF6-9A11-936DBE243B2F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F61E980C-5305-46F9-9291-F8208FC1361E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-56DB16F8-80D7-41DC-8DF5-4CDCEC0B1EAB)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_UPGRADE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-BCF8CD16-1567-40CE-8C6A-CAF0D77DAA83)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6C3EF1B6-78D0-4499-8F68-A4076726F6D1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E589C76E-903C-45A1-A283-5292ECE23C34)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-96FA6DF8-7B8F-40D3-8AC5-DDEFC084C60B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLET_EXISTS_RESPONSE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-058E38A3-2A5A-4911-B952-82C57816E80F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3A232008-D46B-40E9-9ED5-CFAD7FDCE346)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C4FF0295-38FA-4120-8488-BA4635A1B91A)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_DEPLOYMENT_WALLETS_OPERATION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B9304093-3FF4-41C4-BD02-1B127AE41068)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ELASTICSEARCH_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-DD9FB0B9-C177-4ADB-B6DD-F3F9592F40DD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ELASTICSEARCH_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C448BF39-DA47-4482-92A5-8175F8CB0C03)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-E02F39C6-7298-4742-B5D3-242F13083A24)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_EXPORT_DEPLOYMENT_WALLET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1E45D7F7-A8A6-4641-AB99-A323B33FB3A2)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GENERIC_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0E300A1B-0E97-41BB-B3CE-1980DB0186B1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GENERIC_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F9F2CAC7-8F52-49E2-ACBE-6505C6925D77)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOLDEN_GATE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-347F257D-BF17-483B-9408-3B94EC85F854)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOLDEN_GATE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0B6A223B-CAE0-4F0B-8297-9B1F29B0EA9E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_BIG_QUERY_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FE920E89-D6E7-4E71-B947-1247B6F934C1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_BIG_QUERY_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A3153047-950D-47C4-99FE-31DAE6DDF16B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_CLOUD_STORAGE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-70E055CF-60B0-4108-8600-AFB781B43241)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_GOOGLE_CLOUD_STORAGE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FC4BBC6D-D564-4B69-B5ED-4156BB4BF03C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_HDFS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A8F6070C-70BB-419D-9B02-BD8DD6139A3A)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_HDFS_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-57868473-59D9-4171-9570-124BAE5DEB43)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_IMPORT_DEPLOYMENT_WALLET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-74F9B235-7828-4BE4-89B2-50EE21768662)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_JAVA_MESSAGE_SERVICE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-EC493051-91D4-49E6-B740-850E26A53222)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_JAVA_MESSAGE_SERVICE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B3EC0987-D3B5-4CD6-8ACD-4E7C3381BB85)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-AC4534CA-3662-45EB-BDB5-A61820F5FA1F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-DFE9322C-A420-4F5E-BBE0-30337E6C3DA0)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-8D92BA27-284D-4B05-8482-759C49B1D90F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A0194234-AB99-4332-A893-8E6466F17A6C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MICROSOFT_SQLSERVER_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C7BBDAE6-2944-422C-B28B-9EEEE85A5543)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MICROSOFT_SQLSERVER_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-387D9699-AACC-4AA7-8F7A-E85D29BAA736)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MONGO_DB_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-6465E1DE-9BCA-40DA-A3F4-D419EB4F3AF7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MONGO_DB_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-44FC857E-E828-4A0E-9541-8118143DE6E8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MYSQL_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3DED9984-AB59-4035-A4B8-6C8FCBC1D6CC)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_MYSQL_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-044C09FF-E369-4ED9-B369-4F5F51894D4E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_OCI_OBJECT_STORAGE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-53301E7B-7D5F-4151-99A6-8946AC5455D9)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_OCI_OBJECT_STORAGE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-25ABB5D4-047C-4353-B967-9D9F757F97D1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3575EF37-D666-4BD8-8BD4-CEC14DB31A86)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-17AACDCA-29D7-4A07-90FF-B6E6B3BE53CD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_NOSQL_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3CEF672A-FD3D-4473-9E98-52C3429BD783)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_ORACLE_NOSQL_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-34B95F41-4301-46F7-9584-23BCDDB78C7D)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_POSTGRESQL_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-CA0942AF-EFCD-4D8D-8C3D-DFD9D5A9883F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_POSTGRESQL_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-00EB4FE6-FD45-4C8F-B258-D659353680F1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_REDIS_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F68600A0-624F-475B-B8A5-5762974B9C59)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_REDIS_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B355AC1F-0229-4E0C-B34B-89C65AFD2E48)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_RESCHEDULE_DEPLOYMENT_UPGRADE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7F971208-DB4E-47C1-84BF-E8CE663F5A88)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_RESCHEDULE_DEPLOYMENT_UPGRADE_TO_DATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-02F099F5-6FB7-41BB-B558-9D41EC3321B1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_SNOWFLAKE_CONNECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3B10D860-CA3B-4954-AE51-57A2097FE2B1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_SNOWFLAKE_CONNECTION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0DDBA9A8-1AD6-4134-B381-3B8B936AD4FF)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-2D8BF096-392F-4D5A-B088-57AD5787D030)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TEST_CONNECTION_ASSIGNMENT_RESULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-868B1CB4-6664-4ED2-9A8F-BD06C616B5A8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A3CE2145-E6DE-4FF5-82CB-37ACCC153B1F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-279343A3-8941-4C09-ADA6-474A092C2FDD)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_FILE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C6212D5C-37A5-4856-A8E1-E48CFDBA3D61)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-01703338-E126-4BCC-B47F-3FCDBD60E8A1)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C6E92D55-9CE0-48D9-8542-C29A7D2C925A)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_TRAIL_SEQUENCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-39FA0C8D-04E8-47AA-A92C-0C7B8D5D61AC)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F2021ECE-33A9-4696-A238-FD1832D5694C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_KINESIS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-2A33D0A0-3815-4AC1-A294-70ED83EF3068)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_REDSHIFT_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-38203CBF-8E98-41F6-B07A-2DB41CB6FF0F)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AMAZON_S3_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-C903B50C-A58A-4BB7-AB1B-AD65A7124008)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AZURE_DATA_LAKE_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F32432AD-154C-41B8-AD24-C7D6450A1DE4)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_AZURE_SYNAPSE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5E131B29-6002-43A0-9AF1-795CC65E22E7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DATABASE_REGISTRATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A77FE987-4903-4DD3-B798-DDE446625475)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DEPLOYMENT_BACKUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1B97B2ED-F66F-42DD-9EBE-905975FDA169)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_OGG_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-39E19B40-5569-42EA-A327-9E3B2D09BE74)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MAINTENANCE_WINDOW_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-3D152A8C-4EAE-4BDF-8572-124CA057017C)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MAINTENANCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-05457A49-0C9F-4159-82A4-CF7E004B03E7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-FEB155A7-9EAC-417C-9CAE-F9AED1C261A7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ELASTICSEARCH_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F06342C5-4516-43E7-B532-848706A5C8FE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GENERIC_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-900B92C2-6FD4-4010-AB9B-2120CE2F679B)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOLDEN_GATE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-CFFD21EE-3ECA-46B3-819C-115214FCE645)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOOGLE_BIG_QUERY_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1A976E66-8B14-4887-92B8-003C879963E8)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_GOOGLE_CLOUD_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-51CC258F-9EBC-4B45-9881-547E66B3DC0E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_HDFS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F5283A9D-92CC-4147-A154-0651D97019F6)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_JAVA_MESSAGE_SERVICE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-BF495A38-2C0E-4D7B-8866-F61792BDD2F3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_KAFKA_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-9F0286D6-BCEA-490C-B71C-E0F4E1BE028E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_KAFKA_SCHEMA_REGISTRY_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A9E24600-59A8-49EA-91BD-CC053DF4B55A)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MICROSOFT_SQLSERVER_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-82DB11AB-4BB9-4485-9A98-4F51A6235FCE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MONGO_DB_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B41FF74B-8A1B-4F9D-9972-E14A8917393E)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_MYSQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-19517098-6CB7-4AA4-A01A-285C9AF259C7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_OCI_OBJECT_STORAGE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A269970B-E0ED-4A4A-95E3-66276C854DD2)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ORACLE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-B6FE029A-48EB-45F6-869E-8E5079AB45E3)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_ORACLE_NOSQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-4321117E-BF49-4C67-8208-05A8B51C8023)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_POSTGRESQL_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-54305BBE-8307-4618-A8FC-7FBD416969FE)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_REDIS_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-1E601152-C50B-4235-B4E5-AC2E4D792CC7)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPDATE_SNOWFLAKE_CONNECTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-5D14041D-DCF6-431B-B170-9562F8AD28B2)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7108EB62-EED8-4C33-B2B5-73BA761C3E98)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_CURRENT_RELEASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-904EF394-FA3B-405A-B5DB-E3C20E92D674)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_UPGRADE_DEPLOYMENT_SPECIFIC_RELEASE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-28A50965-5E8A-498A-827D-960E3563F513)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F578F262-C99C-42A9-8E7B-AC5EFB163D49)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-0E20A1A7-8897-4034-9B38-879584E3D126)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-7664225E-B0D6-465B-90DC-C5B35DE6F273)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-F49FE11F-9681-4E09-A7EC-15245FF9EDD4)
- [DBMS_CLOUD_OCI_GOLDEN_GATE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/golden_gate_t.html#ADSDK-GUID-A8563838-4620-421D-9F95-5C5936072B70)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
