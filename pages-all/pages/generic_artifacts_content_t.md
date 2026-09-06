# Generic Artifacts Content Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html
- Fetched: 2026-09-05 19:16 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html#dcoc-content-body)

## Generic Artifacts Content Common Types

### DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_GENERIC_ARTIFACT_T Type

The metadata of the artifact.

Syntax
```

```

Fields

Field Description

`id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the artifact. Example: `ocid1.genericartifact.oc1..exampleuniqueID`

`display_name`

(required) The artifact name with the format of `&lt;artifact-path&gt;:&lt;artifact-version&gt;`. The artifact name is truncated to a maximum length of 255. Example: `project01/my-web-app/artifact-abc:1.0.0`

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository's compartment.

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository.

`artifact_path`

(required) A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version. Example: `project01/my-web-app/artifact-abc`

`version`

(required) A user-defined string to describe the artifact version. Example: `1.1.0` or `1.2-beta-2`

`sha256`

(required) The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.

`size_in_bytes`

(required) The size of the artifact in bytes.

`lifecycle_state`

(required) The current state of the artifact.

Allowed values are: 'AVAILABLE', 'DELETING', 'DELETED'

`freeform_tags`

(required) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`time_created`

(required) An RFC 3339 timestamp indicating when the repository was created.

- [Generic Artifacts Content Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html#ADSDK-GUID-4636BA7D-0E0C-42F8-AB84-30CF0BF4A9C1)
- [DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html#ADSDK-GUID-7BA9A3CF-B88E-4FD0-B758-9ECDDEB54C8A)
- [DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html#ADSDK-GUID-C02F050F-B314-4F21-ADE3-A1D96F7A89CE)
- [DBMS_CLOUD_OCI_GENERIC_ARTIFACTS_CONTENT_GENERIC_ARTIFACT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/generic_artifacts_content_t.html#ADSDK-GUID-F747EEB6-CC49-488F-9641-B289C9223648)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
