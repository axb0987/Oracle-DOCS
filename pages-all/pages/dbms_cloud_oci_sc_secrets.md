# Secrets Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html#dcoc-content-body)

## Secrets Functions

Package: DBMS_CLOUD_OCI_SC_SECRETS

### GET_SECRET_BUNDLE Function

Gets a secret bundle that matches either the specified `stage`, `secretVersionName`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the secret version marked as `CURRENT` will be returned.

Syntax
```

```

Parameters

Parameter Description

`secret_id`

(required) The OCID of the secret.

`opc_request_id`

(optional) Unique identifier for the request.

`version_number`

(optional) The version number of the secret.

`secret_version_name`

(optional) The name of the secret. (This might be referred to as the name of the secret version. Names are unique across the different versions of a secret.)

`stage`

(optional) The rotation state of the secret version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://secrets.vaults.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_SECRET_BUNDLE_BY_NAME Function

Gets a secret bundle by secret name and vault ID, and secret version that matches either the specified `stage`, `secretVersionName`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the secret version marked as `CURRENT` is returned.

Syntax
```

```

Parameters

Parameter Description

`secret_name`

(required) A user-friendly name for the secret. Secret names are unique within a vault. Secret names are case-sensitive.

`vault_id`

(required) The OCID of the vault that contains the secret.

`opc_request_id`

(optional) Unique identifier for the request.

`version_number`

(optional) The version number of the secret.

`secret_version_name`

(optional) The name of the secret. (This might be referred to as the name of the secret version. Names are unique across the different versions of a secret.)

`stage`

(optional) The rotation state of the secret version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://secrets.vaults.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SECRET_BUNDLE_VERSIONS Function

Lists all secret bundle versions for the specified secret.

Syntax
```

```

Parameters

Parameter Description

`secret_id`

(required) The OCID of the secret.

`opc_request_id`

(optional) Unique identifier for the request.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call. For information about pagination, see[List Pagination](https://docs.oracle.com/#API/Concepts/usingapi.htm#List_Pagination).

`sort_by`

(optional) The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is descending.

Allowed values are: 'VERSION_NUMBER'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://secrets.vaults.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Secrets Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html#ADSDK-GUID-0D27F7BD-3B06-4B2B-BF42-750E584A518C)
- [GET_SECRET_BUNDLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html#ADSDK-GUID-37E39188-AF55-41E0-B419-E4E68A73C9D7)
- [GET_SECRET_BUNDLE_BY_NAME Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html#ADSDK-GUID-CB76978D-CD37-4E26-8376-9DD05304C1EC)
- [LIST_SECRET_BUNDLE_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_sc_secrets.html#ADSDK-GUID-685FEA22-1D6C-4B41-9079-ECFADA07D723)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
