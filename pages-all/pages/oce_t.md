# OCE Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html
- Fetched: 2026-09-05 19:18 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#dcoc-content-body)

## OCE Common Types

### DBMS_CLOUD_OCI_OCE_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_OCE_CHANGE_OCE_INSTANCE_COMPARTMENT_DETAILS_T Type

The information about compartment details.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the OceInstance should be moved.

### DBMS_CLOUD_OCI_OCE_IDENTITY_STRIPE_DETAILS_T Type

Details of the identity stripe used for OceInstance

Syntax
```

```

Fields

Field Description

`service_name`

(required) Name of the Identity Cloud Service instance in My Services to be used. Example: `secondstripe`

`tenancy`

(required) Value of the Identity Cloud Service tenancy. Example: `idcs-8416ebdd0d674f84803f4193cce026e9`

### DBMS_CLOUD_OCI_OCE_CREATE_OCE_INSTANCE_DETAILS_T Type

The information about new OceInstance.

Syntax
```

```

Fields

Field Description

`description`

(optional) OceInstance description

`compartment_id`

(required) Compartment Identifier

`name`

(required) OceInstance Name

`tenancy_id`

(required) Tenancy Identifier

`idcs_access_token`

(required) Identity Cloud Service access token identifying a stripe and service administrator user

`identity_stripe`

(optional)

`tenancy_name`

(required) Tenancy Name

`instance_usage_type`

(optional) Instance type based on its usage

Allowed values are: 'PRIMARY', 'NONPRIMARY'

`add_on_features`

(optional) a list of add-on features for the ocm instance

`object_storage_namespace`

(required) Object Storage Namespace of Tenancy

`admin_email`

(required) Admin Email for Notification

`upgrade_schedule`

(optional) Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version

`waf_primary_domain`

(optional) Web Application Firewall(WAF) primary domain

`instance_access_type`

(optional) Flag indicating whether the instance access is private or public

Allowed values are: 'PUBLIC', 'PRIVATE'

`instance_license_type`

(optional) Flag indicating whether the instance license is new cloud or bring your own license

Allowed values are: 'NEW', 'BYOL', 'PREMIUM', 'STARTER'

`dr_region`

(optional) disaster recovery paired ragion name

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OCE_ERROR_T Type

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

### DBMS_CLOUD_OCI_OCE_OCE_INSTANCE_T Type

Details of OceInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`guid`

(required) Unique GUID identifier that is immutable on creation

`description`

(optional) OceInstance description, can be updated

`compartment_id`

(required) Compartment Identifier

`name`

(required) OceInstance Name

`tenancy_id`

(required) Tenancy Identifier

`idcs_tenancy`

(required) IDCS Tenancy Identifier

`tenancy_name`

(required) Tenancy Name

`upgrade_schedule`

(optional) Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version

Allowed values are: 'UPGRADE_IMMEDIATELY', 'DELAYED_UPGRADE'

`identity_stripe`

(optional)

`instance_usage_type`

(optional) Instance type based on its usage

Allowed values are: 'PRIMARY', 'NONPRIMARY'

`add_on_features`

(optional) a list of add-on features for the ocm instance

`object_storage_namespace`

(required) Object Storage Namespace of tenancy

`admin_email`

(required) Admin Email for Notification

`waf_primary_domain`

(optional) Web Application Firewall(WAF) primary domain

`instance_access_type`

(optional) Flag indicating whether the instance access is private or public

Allowed values are: 'PUBLIC', 'PRIVATE'

`instance_license_type`

(optional) Flag indicating whether the instance license is new cloud or bring your own license

Allowed values are: 'NEW', 'BYOL', 'PREMIUM', 'STARTER'

`time_created`

(optional) The time the the OceInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the OceInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the instance lifecycle.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Details of the current state of the instance lifecycle

Allowed values are: 'STANDBY', 'FAILOVER', 'DOWN', 'PRIMARY'

`dr_region`

(optional) disaster recovery paired ragion name

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

`service`

(optional) SERVICE data. Example: `{\"service\": {\"IDCS\": \"value\"}}`

### DBMS_CLOUD_OCI_OCE_OCE_INSTANCE_SUMMARY_T Type

Summary of the OceInstance.

Syntax
```

```

Fields

Field Description

`id`

(required) Unique identifier that is immutable on creation

`guid`

(required) Unique GUID identifier that is immutable on creation

`description`

(optional) OceInstance description, can be updated

`compartment_id`

(required) Compartment Identifier

`name`

(required) OceInstance Name

`tenancy_id`

(required) Tenancy Identifier

`idcs_tenancy`

(required) IDCS Tenancy Identifier

`tenancy_name`

(required) Tenancy Name

`instance_usage_type`

(optional) Instance type based on its usage

Allowed values are: 'PRIMARY', 'NONPRIMARY'

`add_on_features`

(optional) a list of add-on features for the ocm instance

`object_storage_namespace`

(required) Object Storage Namespace of tenancy

`admin_email`

(required) Admin Email for Notification

`upgrade_schedule`

(optional) Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version

`waf_primary_domain`

(optional) Web Application Firewall(WAF) primary domain

`instance_access_type`

(optional) Flag indicating whether the instance access is private or public

Allowed values are: 'PUBLIC', 'PRIVATE'

`instance_license_type`

(optional) Flag indicating whether the instance license is new cloud or bring your own license

Allowed values are: 'NEW', 'BYOL', 'PREMIUM', 'STARTER'

`time_created`

(optional) The time the the OceInstance was created. An RFC3339 formatted datetime string

`time_updated`

(optional) The time the OceInstance was updated. An RFC3339 formatted datetime string

`lifecycle_state`

(optional) The current state of the instance lifecycle.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`lifecycle_details`

(optional) Details of the current state of the instance lifecycle

Allowed values are: 'STANDBY', 'FAILOVER', 'DOWN', 'PRIMARY'

`dr_region`

(optional) disaster recovery paired ragion name

`state_message`

(optional) An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

`service`

(optional) SERVICE data. Example: `{\"service\": {\"IDCS\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_OCE_UPDATE_OCE_INSTANCE_DETAILS_T Type

The information to be updated.

Syntax
```

```

Fields

Field Description

`description`

(optional) OceInstance description

`waf_primary_domain`

(optional) Web Application Firewall(WAF) primary domain

`instance_license_type`

(optional) Flag indicating whether the instance license is new cloud or bring your own license

Allowed values are: 'NEW', 'BYOL', 'PREMIUM', 'STARTER'

`instance_usage_type`

(optional) Instance type based on its usage

Allowed values are: 'PRIMARY', 'NONPRIMARY'

`add_on_features`

(optional) a list of add-on features for the ocm instance

`lifecycle_details`

(optional) Details of the current state of the instance lifecycle

Allowed values are: 'STANDBY', 'FAILOVER', 'DOWN', 'PRIMARY'

`dr_region`

(optional) disaster recovery paired ragion name

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`defined_tags`

(optional) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

### DBMS_CLOUD_OCI_OCE_WORK_REQUEST_RESOURCE_T Type

A resource created or operated on by a work request.

Syntax
```

```

Fields

Field Description

`entity_type`

(required) The resource type the work request is affects.

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'IN_PROGRESS', 'FAILED'

`identifier`

(required) The identifier of the resource the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata

### DBMS_CLOUD_OCI_OCE_WORKFLOW_STEP_T Type

Workflow step of workflow monitor.

Syntax
```

```

Fields

Field Description

`step_name`

(optional) workflow step name

`status`

(optional) workflow step status

### DBMS_CLOUD_OCI_OCE_WORKFLOW_STEP_TBL Type

Nested table type of dbms_cloud_oci_oce_workflow_step_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCE_WORKFLOW_MONITOR_T Type

The workflow monitor for this work request.

Syntax
```

```

Fields

Field Description

`workflow_name`

(optional) workflow name for this work request

`resource_name`

(optional) resource name for this work request

`workflow_steps`

(optional) Workflow step of workflow monitor.

### DBMS_CLOUD_OCI_OCE_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_oce_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_OCE_WORK_REQUEST_T Type

A description of workrequest status

Syntax
```

```

Fields

Field Description

`operation_type`

(required) type of the work request

Allowed values are: 'CREATE_OCE_INSTANCE', 'UPDATE_OCE_INSTANCE', 'DELETE_OCE_INSTANCE'

`status`

(required) status of current work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`id`

(required) The id of the work request.

`compartment_id`

(required) The ocid of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used

`resources`

(required) The resources affected by this work request.

`workflow_monitor`

(optional)

`percent_complete`

(required) Percentage of the request completed.

`time_accepted`

(required) The date and time the request was created, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_started`

(optional) The date and time the request was started, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339), section 14.29.

`time_finished`

(optional) The date and time the object was finished, as described in[RFC 3339](https://tools.ietf.org/rfc/rfc3339).

### DBMS_CLOUD_OCI_OCE_WORK_REQUEST_ERROR_T Type

An error encountered while executing a work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured. Error codes are listed on (https://docs.us-phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm)

`message`

(required) A human readable description of the issue encountered.

`l_timestamp`

(required) The time the error occured. An RFC3339 formatted datetime string.

### DBMS_CLOUD_OCI_OCE_WORK_REQUEST_LOG_ENTRY_T Type

A log message from the execution of a work request.

Syntax
```

```

Fields

Field Description

`message`

(required) Human-readable log message.

`l_timestamp`

(required) The time the log message was written. An RFC3339 formatted datetime string

- [OCE Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-4DF4155A-9FF9-4EC0-97DB-877217A9CF2A)
- [DBMS_CLOUD_OCI_OCE_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-DB64F799-6721-4748-8488-79D8CF3EE0B7)
- [DBMS_CLOUD_OCI_OCE_CHANGE_OCE_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-6ACFE0D6-D051-4A65-9EFC-98143FB3179F)
- [DBMS_CLOUD_OCI_OCE_IDENTITY_STRIPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-07BE805A-E32E-4C8F-87C2-66EC0E116DF3)
- [DBMS_CLOUD_OCI_OCE_CREATE_OCE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-BA06D927-86B5-4934-897A-B0199753BB6F)
- [DBMS_CLOUD_OCI_OCE_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-D662C800-E34E-4A27-9FA8-EF1DEB9D9901)
- [DBMS_CLOUD_OCI_OCE_OCE_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-DD8A03E5-428F-4099-BC58-1CCFB575A491)
- [DBMS_CLOUD_OCI_OCE_OCE_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-A32B71AF-9A9A-432A-9619-33528B95631A)
- [DBMS_CLOUD_OCI_OCE_UPDATE_OCE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-9E3DC5BB-7B26-4FEA-858B-4610631CAD59)
- [DBMS_CLOUD_OCI_OCE_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-BC15B6D6-2696-4D66-BAE3-9DD43A5B8E8A)
- [DBMS_CLOUD_OCI_OCE_WORKFLOW_STEP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-86E6C608-8285-44A5-A5FD-9A7F10146482)
- [DBMS_CLOUD_OCI_OCE_WORKFLOW_STEP_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-32892988-FD18-467D-A090-9495B3037839)
- [DBMS_CLOUD_OCI_OCE_WORKFLOW_MONITOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-E87B10EC-050A-43F6-BE2C-D0D6229FB410)
- [DBMS_CLOUD_OCI_OCE_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-79475436-9B53-485D-B24F-28ADBF9898BF)
- [DBMS_CLOUD_OCI_OCE_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-2B9BC599-3116-4772-8614-BB4C97B6E97A)
- [DBMS_CLOUD_OCI_OCE_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-D1691850-3869-4CA8-8A82-9F13D15D8441)
- [DBMS_CLOUD_OCI_OCE_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/oce_t.html#ADSDK-GUID-003500FA-8FA7-41F1-AA28-464FD5291ACC)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
