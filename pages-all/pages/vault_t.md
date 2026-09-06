# Vault Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html
- Fetched: 2026-09-05 19:21 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#dcoc-content-body)

## Vault Common Types

### DBMS_CLOUD_OCI_VAULT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_VAULT_SECRET_CONTENT_DETAILS_T Type

The content of the secret and metadata to help identify it.

Syntax
```

```

Fields

Field Description

`content_type`

(required) The base64-encoded content of the secret.

Allowed values are: 'BASE64'

`name`

(optional) Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.

`stage`

(optional) The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system. When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.

Allowed values are: 'CURRENT', 'PENDING'

### DBMS_CLOUD_OCI_VAULT_BASE64_SECRET_CONTENT_DETAILS_T Type

Base64-encoded secret content.

Syntax
```

```

`dbms_cloud_oci_vault_base64_secret_content_details_t`is a subtype of the`dbms_cloud_oci_vault_secret_content_details_t`type.

Fields

Field Description

`content`

(optional) The base64-encoded content of the secret.

### DBMS_CLOUD_OCI_VAULT_CHANGE_SECRET_COMPARTMENT_DETAILS_T Type

Specifies the updated compartment OCID for the secret.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment into which the resource should be moved.

### DBMS_CLOUD_OCI_VAULT_SECRET_RULE_T Type

A rule that you can apply to a secret to enforce certain conditions on the secret's usage and management.

Syntax
```

```

Fields

Field Description

`rule_type`

(required) The type of rule, which either controls when the secret contents expire or whether they can be reused.

Allowed values are: 'SECRET_EXPIRY_RULE', 'SECRET_REUSE_RULE'

### DBMS_CLOUD_OCI_VAULT_SECRET_RULE_TBL Type

Nested table type of dbms_cloud_oci_vault_secret_rule_t.

Syntax
```

```

### DBMS_CLOUD_OCI_VAULT_CREATE_SECRET_DETAILS_T Type

The details of the secret that you want to create.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where you want to create the secret.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A brief description of the secret. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`key_id`

(optional) The OCID of the master encryption key that is used to encrypt the secret. You must specify a symmetric key to encrypt the secret during import to the vault. You cannot encrypt secrets with asymmetric keys. Furthermore, the key must exist in the vault that you specify.

`metadata`

(optional) Additional metadata that you can use to provide context about how to use the secret during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.

`secret_content`

(required)

`secret_name`

(required) A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.

`secret_rules`

(optional) A list of rules to control how the secret is used and managed.

`vault_id`

(required) The OCID of the vault where you want to create the secret.

### DBMS_CLOUD_OCI_VAULT_ERROR_T Type

An error.

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_VAULT_SCHEDULE_SECRET_DELETION_DETAILS_T Type

Details for scheduling the deletion of the specified secret.

Syntax
```

```

Fields

Field Description

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format.

### DBMS_CLOUD_OCI_VAULT_SCHEDULE_SECRET_VERSION_DELETION_DETAILS_T Type

Schedules the deletion of the specified secret version.

Syntax
```

```

Fields

Field Description

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_VAULT_SECRET_T Type

The details of the secret. Secret details do not contain the contents of the secret itself.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where you want to create the secret.

`current_version_number`

(optional) The version number of the secret version that's currently in use.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A brief description of the secret. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`id`

(required) The OCID of the secret.

`key_id`

(optional) The OCID of the master encryption key that is used to encrypt the secret. You must specify a symmetric key to encrypt the secret during import to the vault. You cannot encrypt secrets with asymmetric keys. Furthermore, the key must exist in the vault that you specify.

`lifecycle_details`

(optional) Additional information about the current lifecycle state of the secret.

`lifecycle_state`

(required) The current lifecycle state of the secret.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'SCHEDULING_DELETION', 'PENDING_DELETION', 'CANCELLING_DELETION', 'FAILED'

`metadata`

(optional) Additional metadata that you can use to provide context about how to use the secret or during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.

`secret_name`

(required) The user-friendly name of the secret. Avoid entering confidential information.

`secret_rules`

(optional) A list of rules that control how the secret is used and managed.

`time_created`

(required) A property indicating when the secret was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_current_version_expiry`

(optional) An optional property indicating when the current secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property indicating when to delete the secret, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the vault where the secret exists.

### DBMS_CLOUD_OCI_VAULT_SECRET_EXPIRY_RULE_T Type

A rule that helps enforce the expiration of a secret's contents.

Syntax
```

```

`dbms_cloud_oci_vault_secret_expiry_rule_t`is a subtype of the`dbms_cloud_oci_vault_secret_rule_t`type.

Fields

Field Description

`secret_version_expiry_interval`

(optional) A property indicating how long the secret contents will be considered valid, expressed in[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)format. The secret needs to be updated when the secret content expires. The timer resets after you update the secret contents. The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported. For example, pass `P3D` to have the secret version expire every 3 days.

`time_of_absolute_expiry`

(optional) An optional property indicating the absolute time when this secret will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days. Example: `2019-04-03T21:10:29.600Z`

`is_secret_content_retrieval_blocked_on_expiry`

(optional) A property indicating whether to block retrieval of the secret content, on expiry. The default is false. If the secret has already expired and you would like to retrieve the secret contents, you need to edit the secret rule to disable this property, to allow reading the secret content.

### DBMS_CLOUD_OCI_VAULT_SECRET_REUSE_RULE_T Type

A rule that disallows reuse of previously used secret content by the specified secret.

Syntax
```

```

`dbms_cloud_oci_vault_secret_reuse_rule_t`is a subtype of the`dbms_cloud_oci_vault_secret_rule_t`type.

Fields

Field Description

`is_enforced_on_deleted_secret_versions`

(optional) A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.

### DBMS_CLOUD_OCI_VAULT_SECRET_SUMMARY_T Type

The details of the secret, excluding the contents of the secret.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the secret.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A brief description of the secret.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`key_id`

(optional) The OCID of the master encryption key that is used to encrypt the secret. You must specify a symmetric key to encrypt the secret during import to the vault. You cannot encrypt secrets with asymmetric keys. Furthermore, the key must exist in the vault that you specify.

`id`

(required) The OCID of the secret.

`lifecycle_details`

(optional) Additional information about the secret's current lifecycle state.

`lifecycle_state`

(required) The current lifecycle state of the secret.

Allowed values are: 'CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'DELETED', 'SCHEDULING_DELETION', 'PENDING_DELETION', 'CANCELLING_DELETION', 'FAILED'

`secret_name`

(required) The name of the secret.

`time_created`

(required) A property indicating when the secret was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_current_version_expiry`

(optional) An optional property indicating when the current secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property indicating when to delete the secret, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`vault_id`

(required) The OCID of the Vault in which the secret exists

### DBMS_CLOUD_OCI_VAULT_SECRET_VERSION_T Type

The details of the secret version, excluding the contents of the secret.

Syntax
```

```

Fields

Field Description

`content_type`

(optional) The content type of the secret version's secret contents.

Allowed values are: 'BASE64'

`name`

(optional) The name of the secret version. A name is unique across versions of a secret.

`secret_id`

(optional) The OCID of the secret.

`stages`

(optional) A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`time_created`

(optional) A optional property indicating when the secret version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_current_version_expiry`

(optional) An optional property indicating when the current secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`version_number`

(optional) The version number of the secret.

### DBMS_CLOUD_OCI_VAULT_SECRET_VERSION_SUMMARY_T Type

The secret version summary object, which doesn't include the contents of the secret.

Syntax
```

```

Fields

Field Description

`content_type`

(optional) The content type of the secret version's secret contents.

Allowed values are: 'BASE64'

`name`

(optional) The name of the secret version. A name is unique across versions of a secret.

`secret_id`

(required) The OCID of the secret.

`stages`

(optional) A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`time_created`

(required) A optional property indicating when the secret version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_expiry`

(optional) An optional property indicating when the secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`version_number`

(required) The version number of the secret.

### DBMS_CLOUD_OCI_VAULT_UPDATE_SECRET_DETAILS_T Type

Details for updating a secret.

Syntax
```

```

Fields

Field Description

`current_version_number`

(optional) Details to update the secret version of the specified secret. The secret contents, version number, and rules can't be specified at the same time. Updating the secret contents automatically creates a new secret version.

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`description`

(optional) A brief description of the secret. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`metadata`

(optional) Additional metadata that you can use to provide context about how to use the secret or during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.

`secret_content`

(optional)

`secret_rules`

(optional) A list of rules to control how the secret is used and managed.

- [Vault Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-003130B2-3803-41F7-A588-773FA3EBCF4F)
- [DBMS_CLOUD_OCI_VAULT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-866E0A65-FCF8-4569-A6C9-5660E07C607C)
- [DBMS_CLOUD_OCI_VAULT_SECRET_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-BFBABB60-F99A-454A-B903-8E800BDCA368)
- [DBMS_CLOUD_OCI_VAULT_BASE64_SECRET_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-9963DC01-AF8D-4B9B-892E-8B882D73010B)
- [DBMS_CLOUD_OCI_VAULT_CHANGE_SECRET_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-0E9849E8-F615-4C11-B2FD-1423669963C9)
- [DBMS_CLOUD_OCI_VAULT_SECRET_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-09A2E1E7-C4D1-4A4A-9407-CE2020F7A29E)
- [DBMS_CLOUD_OCI_VAULT_SECRET_RULE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-E5010D5A-D4F0-41AE-8C8D-DC6C98C0D875)
- [DBMS_CLOUD_OCI_VAULT_CREATE_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-93E03BBF-D14F-4DAF-8D0A-91D85A87020A)
- [DBMS_CLOUD_OCI_VAULT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-50EA2132-248E-4DAD-88EB-09901162B391)
- [DBMS_CLOUD_OCI_VAULT_SCHEDULE_SECRET_DELETION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-AC769270-A62C-4EF2-959A-77269F9AC19F)
- [DBMS_CLOUD_OCI_VAULT_SCHEDULE_SECRET_VERSION_DELETION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-AECF6FCD-E95B-42B4-86CD-AB88493B2734)
- [DBMS_CLOUD_OCI_VAULT_SECRET_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-F6FFE5B9-C852-4A81-A844-F987DE2A63DC)
- [DBMS_CLOUD_OCI_VAULT_SECRET_EXPIRY_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-BD020385-E0D9-4777-A38B-C8BC20D1EBB1)
- [DBMS_CLOUD_OCI_VAULT_SECRET_REUSE_RULE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-D627F161-B616-4024-9AE4-26F1DB688ED8)
- [DBMS_CLOUD_OCI_VAULT_SECRET_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-9BBBEB11-6817-4E5D-9529-01B3674C21D0)
- [DBMS_CLOUD_OCI_VAULT_SECRET_VERSION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-0668E2EF-839B-4C72-A753-692F665FD1EC)
- [DBMS_CLOUD_OCI_VAULT_SECRET_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-6FE0F8CB-6B1E-4E6B-AABE-6C5AAFBEAF80)
- [DBMS_CLOUD_OCI_VAULT_UPDATE_SECRET_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/vault_t.html#ADSDK-GUID-BBE25AD0-F5DE-4896-B15B-B7F4048E66F9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
