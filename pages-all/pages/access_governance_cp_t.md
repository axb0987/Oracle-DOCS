# Access Governance CP Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#dcoc-content-body)

## Access Governance CP Common Types

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_CHANGE_GOVERNANCE_INSTANCE_COMPARTMENT_DETAILS_T Type

The details of a GovernanceInstance to be updated for a compartment change.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the GovernanceInstance resides.

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_CREATE_GOVERNANCE_INSTANCE_DETAILS_T Type

The details about a new GovernanceInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name for the GovernanceInstance.

`description`

(optional) The description of the GovernanceInstance.

`license_type`

(required) The licenseType being used.

Allowed values are: 'NEW_LICENSE', 'BRING_YOUR_OWN_LICENSE', 'AG_ORACLE_WORKLOADS', 'AG_OCI'

`tenancy_namespace`

(required) The namespace for tenancy object storage.

`compartment_id`

(required) The OCID of the compartment where the GovernanceInstance resides.

`idcs_access_token`

(required) IDCS access token identifying a stripe and service administrator user.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_ERROR_T Type

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

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_T Type

The details of a GovenanceInstance.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique OCID of the GovernanceInstance.

`display_name`

(required) The name for the GovernanceInstance.

`compartment_id`

(required) The OCID of the compartment where the GovernanceInstance resides.

`time_created`

(required) The time the the GovernanceInstance was created in an RFC3339 formatted datetime string.

`time_updated`

(optional) The time the GovernanceInstance was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the GovernanceInstance.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`description`

(optional) The description of the GovernanceInstance.

`license_type`

(optional) The licenseType being used.

Allowed values are: 'NEW_LICENSE', 'BRING_YOUR_OWN_LICENSE', 'AG_ORACLE_WORKLOADS', 'AG_OCI'

`tenancy_namespace`

(optional) The namespace for tenancy object storage.

`instance_url`

(optional) The access URL of the GovernanceInstance.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_SUMMARY_T Type

The summary of an GovernanceInstance.

Syntax
```

```

Fields

Field Description

`id`

(optional) The unique OCID of the GovernanceInstance.

`display_name`

(required) The name for the GovernanceInstance.

`description`

(optional) The description of the GovernanceInstance.

`compartment_id`

(required) The OCID of the compartment where the GovernanceInstance resides.

`time_created`

(required) The time the the GovernanceInstance was created in an RFC3339 formatted datetime string.

`time_updated`

(optional) The time the GovernanceInstance was updated in an RFC3339 formatted datetime string.

`lifecycle_state`

(required) The current state of the GovernanceInstance.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'NEEDS_ATTENTION'

`license_type`

(optional) The licenseType being used.

Allowed values are: 'NEW_LICENSE', 'BRING_YOUR_OWN_LICENSE', 'AG_ORACLE_WORKLOADS', 'AG_OCI'

`instance_url`

(optional) The access URL of the GovernanceInstance.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

`system_tags`

(optional) Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_access_governance_cp_governance_instance_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_COLLECTION_T Type

Results of a GovernanceInstance search.

Syntax
```

```

Fields

Field Description

`items`

(required) List of GovernanceInstances.

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_SENDER_CONFIG_T Type

The sender information for email notifications sent by GovernanceInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The sender's displayName.

`email`

(optional) The sender's email.

`is_verified`

(optional) Whether or not the sender's email has been verified.

`time_verify_response_expiry`

(optional) The time when the verify response needs to be received by.

`is_inbox_configured`

(optional) Whether the sender email has inbox configured to receive emails.

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_CONFIGURATION_T Type

The tenancy-wide configuration for GovernanceInstances.

Syntax
```

```

Fields

Field Description

`sender_info`

(required)

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_SENDER_CONFIG_T Type

Update to a sender information for email notifications sent by GovernanceInstance.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The sender's displayName.

`email`

(required) The sender's email.

`is_inbox_configured`

(required) Whether the sender email has inbox configured to receive emails.

`is_resend_notification_email`

(optional) Whether there is a need to resend the verification email.

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_GOVERNANCE_INSTANCE_CONFIGURATION_DETAILS_T Type

The details of a tenancy-wide configuration for GovernanceInstances to be updated.

Syntax
```

```

Fields

Field Description

`sender_info`

(optional)

### DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_GOVERNANCE_INSTANCE_DETAILS_T Type

The details of a GovernanceInstance to be updated.

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The name for the GovernanceInstance.

`description`

(optional) The description of the GovernanceInstance.

`license_type`

(optional) The licenseType being used.

Allowed values are: 'NEW_LICENSE', 'BRING_YOUR_OWN_LICENSE', 'AG_ORACLE_WORKLOADS', 'AG_OCI'

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

`freeform_tags`

(optional) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`

- [Access Governance CP Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-DDCEF78D-309B-4B01-83AE-F96C5B7BEF24)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-867A03B4-E9AD-419E-9F0B-F50914DD7736)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_CHANGE_GOVERNANCE_INSTANCE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-EC778822-0C1E-4C03-B4C7-83D9BD3C8661)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_CREATE_GOVERNANCE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-50CC4D1D-0DE2-4F5C-9961-5D235D3A5902)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-10D173C5-99AF-4035-83DE-926E18356052)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-3B84BBF2-9854-41A9-81D8-6F31F8D2EF00)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-F4B06D90-2383-4D32-B505-B83BE499CEA6)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-0D64328D-F0D2-4981-B467-B4F00EDF9D58)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-D1AF1A06-CC72-4649-BEAF-93891A397B00)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_SENDER_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-11C047D6-B6D5-4185-B51D-F8A374063F50)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_GOVERNANCE_INSTANCE_CONFIGURATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-5B1F1335-9387-40F3-A112-F5B08DE94B86)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_SENDER_CONFIG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-50E00001-3580-4ED7-A9E2-3D367867DEEF)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_GOVERNANCE_INSTANCE_CONFIGURATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-4499DF91-869C-417F-82D8-F90C491A93A8)
- [DBMS_CLOUD_OCI_ACCESS_GOVERNANCE_CP_UPDATE_GOVERNANCE_INSTANCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/access_governance_cp_t.html#ADSDK-GUID-D03127A4-6DF7-4471-9AA7-E338D88702BA)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
