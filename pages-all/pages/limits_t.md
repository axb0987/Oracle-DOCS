# Limits Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#dcoc-content-body)

## Limits Common Types

### DBMS_CLOUD_OCI_LIMITS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_LIMITS_ADD_LOCK_DETAILS_T Type

Request payload to add lock to the resource. The FULL lock type allows no modifications (delete, create, update). The DELETE lock type allows all modifications, but delete is not allowed.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Lock type.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.

`message`

(optional) A message added by the lock creator. The message typically gives an indication of why the resource is locked.

### DBMS_CLOUD_OCI_LIMITS_ADD_LOCK_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_limits_add_lock_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LIMITS_CREATE_QUOTA_DETAILS_T Type

Request object for create quota operation.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the resource this quota applies to.

`description`

(required) The description you assign to the quota.

`name`

(required) The name you assign to the quota during creation. The name must be unique across all quotas in the tenancy and cannot be changed.

`statements`

(required) An array of quota statements written in the declarative quota statement language.

`locks`

(optional) Locks associated with this resource.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_LIMITS_ERROR_T Type

Generic error object.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_LIMITS_LIMIT_DEFINITION_SUMMARY_T Type

The metadata specific to a resource limit definition.

Syntax
```

```

Fields

Field Description

`name`

(optional) The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.

`service_name`

(optional) The service name of the limit.

`description`

(optional) The limit description.

`scope_type`

(optional) Reflects the scope of the resource limit, whether Global (across all regions), regional, or availability domain-specific.

Allowed values are: 'GLOBAL', 'REGION', 'AD'

`are_quotas_supported`

(optional) If true, quota policies can be created on top of this resource limit.

`is_resource_availability_supported`

(optional) Reflects whether or not the GetResourceAvailability API is supported for this limit. If not, the API returns an empty JSON response.

`is_deprecated`

(optional) Indicates if the limit has been deprecated.

`is_eligible_for_limit_increase`

(optional) Indicates if the customer can request a limit increase for this resource.

`is_dynamic`

(optional) The limit for this resource has a dynamic value that is based on consumption across all OCI services.

### DBMS_CLOUD_OCI_LIMITS_LIMIT_VALUE_SUMMARY_T Type

The value of a specific resource limit.

Syntax
```

```

Fields

Field Description

`name`

(optional) The resource limit name. To be used for writing policies (in case of quotas) or other programmatic calls.

`scope_type`

(optional) The scope type of the limit.

Allowed values are: 'GLOBAL', 'REGION', 'AD'

`availability_domain`

(optional) If present, the returned value is only specific to this availability domain.

`value`

(optional) The resource limit value.

### DBMS_CLOUD_OCI_LIMITS_RESOURCE_LOCK_T Type

Resource locks prevent certain APIs from being called for the resource. A full lock prevents both updating and deleting the resource. A lock delete prevents deleting the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Lock type.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The resource ID that is locking this resource. Indicates that deleting this resource removes the lock.

`message`

(optional) A message added by the lock creator. The message typically gives an indication of why the resource is locked.

`time_created`

(optional) Indicates when the lock was created, in the format defined by RFC 3339.

### DBMS_CLOUD_OCI_LIMITS_RESOURCE_LOCK_TBL Type

Nested table type of dbms_cloud_oci_limits_resource_lock_t.

Syntax
```

```

### DBMS_CLOUD_OCI_LIMITS_QUOTA_T Type

Quotas are applied on top of the service limits and inherited through the nested compartment hierarchy. Quotas allow compartment admins to limit resource consumption and set boundaries around acceptable resource use. The term \"quota\" can be interpreted as the following: * An individual statement written in the declarative language. * A collection of statements in a single, named \"quota\" object (which has an Oracle Cloud ID (OCID) assigned to it). * The overall body of quotas your organization uses to control access to resources.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the quota.

`compartment_id`

(required) The OCID of the compartment containing the resource this quota applies to.

`name`

(required) The name you assign to the quota during creation. The name must be unique across all quotas in the tenancy and cannot be changed.

`statements`

(required) An array of one or more quota statements written in the declarative quota statement language.

`locks`

(optional) Locks associated with this resource.

`description`

(required) The description you assign to the quota.

`time_created`

(required) Date and time the quota was created, in the format defined by RFC 3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The quota's current state. After creating a quota, make sure its `lifecycleState` is set to ACTIVE before using it.

Allowed values are: 'ACTIVE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_LIMITS_QUOTA_SUMMARY_T Type

Consists of a subset of all the properties of the corresponding quota, and is recommended to be used in cases requiring security of quota details, and for slightly better API performance.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the quota.

`compartment_id`

(required) The OCID of the compartment containing the resource this quota applies to.

`name`

(required) The name you assign to the quota during creation. The name must be unique across all quotas in the tenancy and cannot be changed.

`description`

(required) The description you assign to the quota.

`time_created`

(required) Date and time the quota was created, in the format defined by RFC 3339. Example: `2016-08-25T21:10:29.600Z`

`locks`

(optional) Locks associated with this resource.

`lifecycle_state`

(optional) The quota's current state. After creating a quota, make sure its `lifecycleState` is set to ACTIVE before using it.

Allowed values are: 'ACTIVE'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_LIMITS_REMOVE_LOCK_DETAILS_T Type

Request payload to remove the resource lock.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Lock type.

Allowed values are: 'FULL', 'DELETE'

### DBMS_CLOUD_OCI_LIMITS_RESOURCE_AVAILABILITY_T Type

The availability of a given resource limit, based on the usage, tenant service limits, and quotas set for the tenancy. Note: We cannot guarantee this data for all the limits. In such cases, these fields will be empty.

Syntax
```

```

Fields

Field Description

`used`

(optional) The current usage in the given compartment. To support resources with fractional counts, the field rounds up to the nearest integer.

`available`

(optional) The count of available resources. To support resources with fractional counts, the field rounds down to the nearest integer.

`fractional_usage`

(optional) The current most accurate usage in the given compartment.

`fractional_availability`

(optional) The most accurate count of available resources.

`effective_quota_value`

(optional) The effective quota value for the given compartment. This field is only present if there is a current quota policy affecting the current resource in the target region or availability domain.

### DBMS_CLOUD_OCI_LIMITS_SERVICE_SUMMARY_T Type

A specific OCI service supported by resource limits.

Syntax
```

```

Fields

Field Description

`name`

(optional) The service name. Use this when calling other APIs.

`description`

(optional) The friendly service name.

### DBMS_CLOUD_OCI_LIMITS_UPDATE_QUOTA_DETAILS_T Type

Request object for update quota operation.

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the quota.

`statements`

(optional) An array of quota statements written in the declarative quota statement language.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

- [Limits Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-C40126BD-FCC9-49EE-BE38-4AC268C1A39D)
- [DBMS_CLOUD_OCI_LIMITS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-417046A8-0299-4C31-8C1B-41FD9E83BDA6)
- [DBMS_CLOUD_OCI_LIMITS_ADD_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-06337043-C5F5-4DD2-AAE7-8CB3031724EE)
- [DBMS_CLOUD_OCI_LIMITS_ADD_LOCK_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-8DFB6812-CE50-4EF5-816C-222EABA2A6DD)
- [DBMS_CLOUD_OCI_LIMITS_CREATE_QUOTA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-DB8E7552-502C-4482-AC81-A77984DEFF36)
- [DBMS_CLOUD_OCI_LIMITS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-8B32BB7C-2E51-4E02-9F31-88F1D7D84056)
- [DBMS_CLOUD_OCI_LIMITS_LIMIT_DEFINITION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-A00BF479-55FD-4394-B97C-E56D3B89CB1A)
- [DBMS_CLOUD_OCI_LIMITS_LIMIT_VALUE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-1BD37364-35D2-4DC9-9420-30CD3DA8B651)
- [DBMS_CLOUD_OCI_LIMITS_RESOURCE_LOCK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-249B317B-B731-47AE-AC49-59E7962B8FC3)
- [DBMS_CLOUD_OCI_LIMITS_RESOURCE_LOCK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-CCD39EB1-946B-4222-85DC-1CC1C23A98BE)
- [DBMS_CLOUD_OCI_LIMITS_QUOTA_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-F8BE70DA-A153-48ED-9F01-F235AEA4601D)
- [DBMS_CLOUD_OCI_LIMITS_QUOTA_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-5BC8D5C0-DC99-4C44-A598-32127B8836C1)
- [DBMS_CLOUD_OCI_LIMITS_REMOVE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-0A12A193-BF6D-4F00-B23F-FCAFF217B953)
- [DBMS_CLOUD_OCI_LIMITS_RESOURCE_AVAILABILITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-5AFCC132-C0FC-4EDE-A068-7A7A6AE389A9)
- [DBMS_CLOUD_OCI_LIMITS_SERVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-7EB2E5C3-979B-4C80-A905-914001B84C63)
- [DBMS_CLOUD_OCI_LIMITS_UPDATE_QUOTA_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/limits_t.html#ADSDK-GUID-B467BABE-6BA1-41CC-BC39-99924CCA8946)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
