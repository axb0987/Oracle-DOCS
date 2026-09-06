# Secrets Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html
- Fetched: 2026-09-05 19:19 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#dcoc-content-body)

## Secrets Common Types

### DBMS_CLOUD_OCI_SECRETS_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_CONTENT_DETAILS_T Type

The contents of the secret.

Syntax
```

```

Fields

Field Description

`content_type`

(required) The formatting type of the secret contents.

Allowed values are: 'BASE64'

### DBMS_CLOUD_OCI_SECRETS_BASE64_SECRET_BUNDLE_CONTENT_DETAILS_T Type

The contents of the secret.

Syntax
```

```

`dbms_cloud_oci_secrets_base64_secret_bundle_content_details_t`is a subtype of the`dbms_cloud_oci_secrets_secret_bundle_content_details_t`type.

Fields

Field Description

`content`

(optional) The base64-encoded content of the secret.

### DBMS_CLOUD_OCI_SECRETS_ERROR_T Type

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

### DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_T Type

The contents of the secret, properties of the secret (and secret version), and user-provided contextual metadata for the secret.

Syntax
```

```

Fields

Field Description

`secret_id`

(required) The OCID of the secret.

`time_created`

(optional) The time when the secret bundle was created.

`version_number`

(required) The version number of the secret.

`version_name`

(optional) The name of the secret version. Labels are unique across the different versions of a particular secret.

`secret_bundle_content`

(optional)

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_expiry`

(optional) An optional property indicating when the secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`stages`

(optional) A list of possible rotation states for the secret version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`metadata`

(optional) Customer-provided contextual metadata for the secret.

### DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_VERSION_SUMMARY_T Type

The properties of the secret bundle. (Secret bundle version summary objects do not include the actual contents of the secret.)

Syntax
```

```

Fields

Field Description

`secret_id`

(required) The OCID of the secret.

`time_created`

(optional) The time when the secret bundle was created.

`version_number`

(required) The version number of the secret.

`version_name`

(optional) The version name of the secret bundle, as provided when the secret was created or last rotated.

`time_of_deletion`

(optional) An optional property indicating when to delete the secret version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_expiry`

(optional) An optional property indicating when the secret version will expire, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`stages`

(optional) A list of possible rotation states for the secret bundle.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

- [Secrets Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-9EA13861-3ADE-4C5C-814D-D093AE784B3F)
- [DBMS_CLOUD_OCI_SECRETS_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-50971C07-A156-487C-9910-932BF2C5082E)
- [DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-A605A7B7-906E-42D8-A64B-E336EC076344)
- [DBMS_CLOUD_OCI_SECRETS_BASE64_SECRET_BUNDLE_CONTENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-3E7D9B08-062E-4F08-9A8A-F7C4AA42DFC4)
- [DBMS_CLOUD_OCI_SECRETS_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-FC626DB5-2B61-47F5-A793-46E8AA05C348)
- [DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-705C97C3-2D3A-429F-BBB7-30EF5DF73287)
- [DBMS_CLOUD_OCI_SECRETS_SECRET_BUNDLE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/secrets_t.html#ADSDK-GUID-54329B34-8D6C-43F1-BF88-045B7D8737A9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
