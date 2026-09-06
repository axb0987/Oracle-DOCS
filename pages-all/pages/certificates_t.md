# Certificates Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html
- Fetched: 2026-09-05 19:01 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#dcoc-content-body)

## Certificates Common Types

### DBMS_CLOUD_OCI_CERTIFICATES_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_CERTIFICATES_CA_BUNDLE_T Type

The contents of the CA bundle (root and intermediate certificates), properties of the CA bundle, and user-provided contextual metadata for the CA bundle.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the CA bundle.

`name`

(required) A user-friendly name for the CA bundle. Names are unique within a compartment. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.

`ca_bundle_pem`

(required) Certificates (in PEM format) in the CA bundle. Can be of arbitrary length.

### DBMS_CLOUD_OCI_CERTIFICATES_VALIDITY_T Type

An object that describes a period of time during which an entity is valid.

Syntax
```

```

Fields

Field Description

`time_of_validity_not_before`

(required) The date on which the certificate validity period begins, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`time_of_validity_not_after`

(required) The date on which the certificate validity period ends, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

### DBMS_CLOUD_OCI_CERTIFICATES_REVOCATION_STATUS_T Type

The current revocation status of the certificate or certificate authority (CA).

Syntax
```

```

Fields

Field Description

`time_revoked`

(required) The time when the certificate or CA was revoked.

`revocation_reason`

(required) The reason that the certificate or CA was revoked.

Allowed values are: 'UNSPECIFIED', 'KEY_COMPROMISE', 'CA_COMPROMISE', 'AFFILIATION_CHANGED', 'SUPERSEDED', 'CESSATION_OF_OPERATION', 'PRIVILEGE_WITHDRAWN', 'AA_COMPROMISE'

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_T Type

The contents of the certificate, properties of the certificate (and certificate version), and user-provided contextual metadata for the certificate.

Syntax
```

```

Fields

Field Description

`certificate_authority_id`

(required) The OCID of the certificate authority (CA).

`certificate_authority_name`

(required) The name of the CA.

`serial_number`

(required) A unique certificate identifier used in certificate revocation tracking, formatted as octets. Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`

`certificate_pem`

(required) The certificate (in PEM format) for this CA version.

`cert_chain_pem`

(optional) The certificate chain (in PEM format) for this CA version.

`version_name`

(optional) The name of the CA.

`time_created`

(required) A property indicating when the CA was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`version_number`

(required) The version number of the CA.

`validity`

(required)

`stages`

(required) A list of rotation states for this CA.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED', 'FAILED'

`revocation_status`

(optional)

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_SUMMARY_T Type

The properties of a version of a bundle for a certificate authority (CA). Certificate authority bundle version summary objects do not include the actual contents of the certificate.

Syntax
```

```

Fields

Field Description

`certificate_authority_id`

(required) The OCID of the certificate authority (CA).

`serial_number`

(optional) A unique certificate identifier used in certificate revocation tracking, formatted as octets. Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`

`time_created`

(required) An optional property indicating when the CA version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`version_number`

(required) The version number of the CA.

`version_name`

(optional) The name of the CA version. When this value is not null, the name is unique across CA versions for a given CA.

`certificate_authority_name`

(required) The name of the CA.

`time_of_deletion`

(optional) An optional property indicating when to delete the CA version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`validity`

(optional)

`stages`

(required) A list of rotation states for this CA version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED', 'FAILED'

`revocation_status`

(optional)

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_certificates_certificate_authority_bundle_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_COLLECTION_T Type

The results of a certificate authority (CA) version search. Results contain CA version summary objects and other data.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of CA version summary objects.

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_T Type

The contents of the certificate, properties of the certificate (and certificate version), and user-provided contextual metadata for the certificate.

Syntax
```

```

Fields

Field Description

`certificate_bundle_type`

(required) The type of certificate bundle, which indicates whether the private key fields are included.

Allowed values are: 'CERTIFICATE_CONTENT_PUBLIC_ONLY', 'CERTIFICATE_CONTENT_WITH_PRIVATE_KEY'

`certificate_id`

(required) The OCID of the certificate.

`certificate_name`

(required) The name of the certificate.

`version_number`

(required) The version number of the certificate.

`serial_number`

(required) A unique certificate identifier used in certificate revocation tracking, formatted as octets. Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`

`certificate_pem`

(optional) The certificate in PEM format.

`cert_chain_pem`

(optional) The certificate chain (in PEM format) for the certificate bundle.

`time_created`

(required) An optional property indicating when the certificate version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`validity`

(required)

`version_name`

(optional) The name of the certificate version.

`stages`

(required) A list of rotation states for the certificate bundle.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED', 'FAILED'

`revocation_status`

(optional)

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_PUBLIC_ONLY_T Type

A certificate bundle, not including the private key.

Syntax
```

```

`dbms_cloud_oci_certificates_certificate_bundle_public_only_t`is a subtype of the`dbms_cloud_oci_certificates_certificate_bundle_t`type.

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_SUMMARY_T Type

The properties of the certificate bundle. Certificate bundle version summary objects do not include the actual contents of the certificate.

Syntax
```

```

Fields

Field Description

`certificate_id`

(required) The OCID of the certificate.

`serial_number`

(optional) A unique certificate identifier used in certificate revocation tracking, formatted as octets. Example: `03 AC FC FA CC B3 CB 02 B8 F8 DE F5 85 E7 7B FF`

`version_name`

(optional) The name of the certificate version.

`certificate_name`

(required) The name of the certificate.

`version_number`

(required) The version number of the certificate.

`time_created`

(required) An optional property indicating when the certificate version was created, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`validity`

(optional)

`time_of_deletion`

(optional) An optional property indicating when to delete the certificate version, expressed in[RFC 3339](https://tools.ietf.org/html/rfc3339)timestamp format. Example: `2019-04-03T21:10:29.600Z`

`stages`

(required) A list of rotation states for this certificate bundle version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED', 'FAILED'

`revocation_status`

(optional)

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_SUMMARY_TBL Type

Nested table type of dbms_cloud_oci_certificates_certificate_bundle_version_summary_t.

Syntax
```

```

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_COLLECTION_T Type

The results of a certificate bundle versions search. Results contain certificate bundle version summary objects.

Syntax
```

```

Fields

Field Description

`items`

(required) A list of certificate bundle version summary objects.

### DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_WITH_PRIVATE_KEY_T Type

A certificate bundle, including the private key.

Syntax
```

```

`dbms_cloud_oci_certificates_certificate_bundle_with_private_key_t`is a subtype of the`dbms_cloud_oci_certificates_certificate_bundle_t`type.

Fields

Field Description

`private_key_pem`

(required) The private key (in PEM format) for the certificate.

`private_key_pem_passphrase`

(optional) An optional passphrase for the private key.

### DBMS_CLOUD_OCI_CERTIFICATES_ERROR_T Type

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

- [Certificates Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-ADA8F5A7-CEF0-4AA9-A54A-05354C8EA1A8)
- [DBMS_CLOUD_OCI_CERTIFICATES_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-6AAF3EC8-7007-4C53-B086-187E0893E46E)
- [DBMS_CLOUD_OCI_CERTIFICATES_CA_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-B358F863-3203-4FE9-9741-B927DE00BE86)
- [DBMS_CLOUD_OCI_CERTIFICATES_VALIDITY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-16E368C9-CFA1-4F64-A9E0-2519CE02BA39)
- [DBMS_CLOUD_OCI_CERTIFICATES_REVOCATION_STATUS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-0847210C-B358-43CA-AEB6-B60E92702ADD)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-711F3ED0-CAEE-4F87-AAC2-7A8639767B27)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-D350031E-F0F2-4C74-BE08-D4A8BD2D52BD)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-BE4BD208-5CD1-4E01-9400-AFDEF4304A19)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_AUTHORITY_BUNDLE_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-65344F58-97B0-4CE3-B7E3-F427EC59E76B)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-14219236-FC50-4AA1-89D8-E45F54A76337)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_PUBLIC_ONLY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-157C5A21-E5C3-4A5A-9E31-83D0EEE9341E)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-B678FA11-CD00-4FBD-BF57-CAE24FEBFF07)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_SUMMARY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-CA212CAC-BF21-4559-9453-002960AD2598)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_VERSION_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-F2CB0711-D3F1-448B-B67F-0B749E8F5745)
- [DBMS_CLOUD_OCI_CERTIFICATES_CERTIFICATE_BUNDLE_WITH_PRIVATE_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-0913B3F9-39B9-42AD-B79F-1B5CDA9B3B46)
- [DBMS_CLOUD_OCI_CERTIFICATES_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/certificates_t.html#ADSDK-GUID-27C37369-F6D4-4FD3-B6AA-C5CF363CC838)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
