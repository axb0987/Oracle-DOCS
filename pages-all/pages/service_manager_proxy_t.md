# Service Manager Proxy Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html
- Fetched: 2026-09-05 19:20 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#dcoc-content-body)

## Service Manager Proxy Common Types

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_ERROR_ENTITY_T Type

The model for the error entity.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error.

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_DEFINITION_T Type

Details for a service definition.

Syntax
```

```

Fields

Field Description

`l_type`

(required) The service definition type. For example, a service definition type \"RGBUOROMS\" would be for the service \"Oracle Retail Order Management Cloud Service\".

`display_name`

(required) Display name of the service. For example, \"Oracle Retail Order Management Cloud Service\".

`short_display_name`

(required) Short display name of the service. For example, \"Retail Order Management\".

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_END_POINT_OVERVIEW_T Type

An overview of service environment endpoints.

Syntax
```

```

Fields

Field Description

`environment_type`

(required) Service environment endpoint type.

Allowed values are: 'INSTANCE_URL_PROD', 'INSTANCE_URL_TEST', 'INSTANCE_URL_DEV', 'OTHER'

`url`

(required) Service environment instance URL.

`description`

(optional) Description of the environment link

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_END_POINT_OVERVIEW_TBL Type

Nested table type of dbms_cloud_oci_service_manager_proxy_service_environment_end_point_overview_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_T Type

Detailed information about a service environment. **Note:** Service URL formats may vary from the provided example.

Syntax
```

```

Fields

Field Description

`id`

(required) Unqiue identifier for the entitlement related to the environment. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`subscription_id`

(required) The unique subscription ID associated with the service environment ID. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`status`

(required) Status of the entitlement registration for the service.

Allowed values are: 'INITIALIZED', 'BEGIN_ACTIVATION', 'ACTIVE', 'BEGIN_SOFT_TERMINATION', 'SOFT_TERMINATED', 'BEGIN_TERMINATION', 'CANCELED', 'TERMINATED', 'BEGIN_DISABLING', 'BEGIN_ENABLING', 'BEGIN_MIGRATION', 'DISABLED', 'BEGIN_SUSPENSION', 'BEGIN_RESUMPTION', 'SUSPENDED', 'BEGIN_LOCK_RELOCATION', 'LOCKED_RELOCATION', 'BEGIN_RELOCATION', 'RELOCATED', 'BEGIN_UNLOCK_RELOCATION', 'UNLOCKED_RELOCATION', 'FAILED_LOCK_RELOCATION', 'FAILED_ACTIVATION', 'FAILED_MIGRATION', 'ACCESS_DISABLED', 'BEGIN_DISABLING_ACCESS', 'BEGIN_ENABLING_ACCESS', 'TRA_UNKNOWN'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment.

`service_definition`

(required)

`console_url`

(optional) The URL for the console.

`service_environment_endpoints`

(optional) Array of service environment end points.

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_SUMMARY_T Type

Summary of service environment details.

Syntax
```

```

Fields

Field Description

`id`

(required) Unqiue identifier for the entitlement related to the environment. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`subscription_id`

(required) The unique subscription ID associated with the service environment ID. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`status`

(required) Status of the entitlement registration for the service.

Allowed values are: 'INITIALIZED', 'BEGIN_ACTIVATION', 'ACTIVE', 'BEGIN_SOFT_TERMINATION', 'SOFT_TERMINATED', 'BEGIN_TERMINATION', 'CANCELED', 'TERMINATED', 'BEGIN_DISABLING', 'BEGIN_ENABLING', 'BEGIN_MIGRATION', 'DISABLED', 'BEGIN_SUSPENSION', 'BEGIN_RESUMPTION', 'SUSPENDED', 'BEGIN_LOCK_RELOCATION', 'LOCKED_RELOCATION', 'BEGIN_RELOCATION', 'RELOCATED', 'BEGIN_UNLOCK_RELOCATION', 'UNLOCKED_RELOCATION', 'FAILED_LOCK_RELOCATION', 'FAILED_ACTIVATION', 'FAILED_MIGRATION', 'ACCESS_DISABLED', 'BEGIN_DISABLING_ACCESS', 'BEGIN_ENABLING_ACCESS', 'TRA_UNKNOWN'

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment.

`service_definition`

(required)

`console_url`

(optional) The URL for the console.

`service_environment_endpoints`

(optional) Array of service environment end points.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"CostCenter\": \"42\"}`

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_service_manager_proxy_service_environment_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_COLLECTION_T Type

Collection of service environments. **Note:** Service URL formats may vary from the provided example.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of items.

- [Service Manager Proxy Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-82778E06-7EFF-4899-800C-C61AA6FAF508)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-683724D9-5278-4BCF-B4CA-24BAE036A5F1)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_ERROR_ENTITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-02295543-25D1-4247-9361-7C9BC65D6DBD)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_DEFINITION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-07945DA6-54BE-4C48-928B-C167DF7D8BE4)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_END_POINT_OVERVIEW_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-8F3DE1D9-B6C4-4E24-9A30-E319C0BC4425)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_END_POINT_OVERVIEW_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-C0370EB8-A325-4F26-B0C4-774F53FED276)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-11CAA99D-7A66-4949-A4FA-DD6A31D67C95)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-E7D401A4-A3B5-4264-A574-E98AF90AE916)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-11BD8BD8-93E6-410E-BD8D-96727647A10A)
- [DBMS_CLOUD_OCI_SERVICE_MANAGER_PROXY_SERVICE_ENVIRONMENT_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/service_manager_proxy_t.html#ADSDK-GUID-36C5387A-392B-406E-8674-D46A5F43A892)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
