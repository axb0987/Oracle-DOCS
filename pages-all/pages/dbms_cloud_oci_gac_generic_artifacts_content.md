# Generic Artifacts Content Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html#dcoc-content-body)

## Generic Artifacts Content Functions

Package: DBMS_CLOUD_OCI_GAC_GENERIC_ARTIFACTS_CONTENT

### GET_GENERIC_ARTIFACT_CONTENT Function

Gets the specified artifact's content.

Syntax
```

```

Parameters

Parameter Description

`artifact_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the artifact. Example: `ocid1.genericartifact.oc1..exampleuniqueID`

`opc_request_id`

(optional) Unique Oracle-assigned[request ID](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx` If you contact Oracle about a request, provide this request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://generic.artifacts.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GENERIC_ARTIFACT_CONTENT_BY_PATH Function

Gets the content of an artifact with a specified `artifactPath` and `version`.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository. Example: `ocid1.repository.oc1..exampleuniqueID`

`artifact_path`

(required) A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version. Example: `project01/my-web-app/artifact-abc`

`version`

(required) A user-defined string to describe the artifact version. Example: `1.1.2` or `1.2-beta-2`

`opc_request_id`

(optional) Unique Oracle-assigned[request ID](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx` If you contact Oracle about a request, provide this request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://generic.artifacts.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### PUT_GENERIC_ARTIFACT_CONTENT_BY_PATH Function

Uploads an artifact. Provide `artifactPath`, `version` and content. Avoid entering confidential information when you define the path and version.

Syntax
```

```

Parameters

Parameter Description

`repository_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the repository. Example: `ocid1.repository.oc1..exampleuniqueID`

`artifact_path`

(required) A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version. Example: `project01/my-web-app/artifact-abc`

`version`

(required) A user-defined string to describe the artifact version. Example: `1.1.2` or `1.2-beta-2`

`generic_artifact_content_body`

(required) Uploads an artifact. Provide artifact path, version and content. Avoid entering confidential information when you define the path and version.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource. The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

`opc_request_id`

(optional) Unique Oracle-assigned[request ID](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx` If you contact Oracle about a request, provide this request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://generic.artifacts.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Generic Artifacts Content Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html#ADSDK-GUID-C33A0C2B-7493-44AE-919A-C8C002A84C8C)
- [GET_GENERIC_ARTIFACT_CONTENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html#ADSDK-GUID-96233A48-87C5-4BB6-A2F8-9968A0A3AA98)
- [GET_GENERIC_ARTIFACT_CONTENT_BY_PATH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html#ADSDK-GUID-ED869843-4747-4B7F-B775-CED9A3F1D3E5)
- [PUT_GENERIC_ARTIFACT_CONTENT_BY_PATH Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_gac_generic_artifacts_content.html#ADSDK-GUID-D7911980-DEE3-4CC5-8160-5F01B8186154)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
