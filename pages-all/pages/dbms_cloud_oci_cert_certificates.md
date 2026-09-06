# Certificates Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#dcoc-content-body)

## Certificates Functions

Package: DBMS_CLOUD_OCI_CERT_CERTIFICATES

### GET_CA_BUNDLE Function

Gets a ca-bundle bundle.

Syntax
```

```

Parameters

Parameter Description

`ca_bundle_id`

(required) The OCID of the CA bundle.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://certificates.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CERTIFICATE_AUTHORITY_BUNDLE Function

Gets a certificate authority bundle that matches either the specified `stage`, `name`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the certificate authority version marked as `CURRENT` will be returned.

Syntax
```

```

Parameters

Parameter Description

`certificate_authority_id`

(required) The OCID of the certificate authority (CA).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`version_number`

(optional) The version number of the certificate authority (CA).

`certificate_authority_version_name`

(optional) The name of the certificate authority (CA). (This might be referred to as the name of the CA version, as every CA consists of at least one version.) Names are unique across versions of a given CA.

`stage`

(optional) The rotation state of the certificate version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://certificates.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CERTIFICATE_BUNDLE Function

Gets a certificate bundle that matches either the specified `stage`, `versionName`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the certificate version marked as `CURRENT` will be returned. By default, the private key is not included in the query result, and a CertificateBundlePublicOnly is returned. If the private key is needed, use the CertificateBundleTypeQueryParam parameter to get a CertificateBundleWithPrivateKey response.

Syntax
```

```

Parameters

Parameter Description

`certificate_id`

(required) The OCID of the certificate.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`version_number`

(optional) The version number of the certificate. The default value is 0, which means that this query parameter is ignored.

`certificate_version_name`

(optional) The name of the certificate. (This might be referred to as the name of the certificate version, as every certificate consists of at least one version.) Names are unique across versions of a given certificate.

`stage`

(optional) The rotation state of the certificate version.

Allowed values are: 'CURRENT', 'PENDING', 'LATEST', 'PREVIOUS', 'DEPRECATED'

`certificate_bundle_type`

(optional) The type of certificate bundle. By default, the private key fields are not returned. When querying for certificate bundles, to return results with certificate contents, the private key in PEM format, and the private key passphrase, specify the value of this parameter as `CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`.

Allowed values are: 'CERTIFICATE_CONTENT_PUBLIC_ONLY', 'CERTIFICATE_CONTENT_WITH_PRIVATE_KEY'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://certificates.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CERTIFICATE_AUTHORITY_BUNDLE_VERSIONS Function

Lists all certificate authority bundle versions for the specified certificate authority.

Syntax
```

```

Parameters

Parameter Description

`certificate_authority_id`

(required) The OCID of the certificate authority (CA).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is ascending.

Allowed values are: 'VERSION_NUMBER'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://certificates.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CERTIFICATE_BUNDLE_VERSIONS Function

Lists all certificate bundle versions for the specified certificate.

Syntax
```

```

Parameters

Parameter Description

`certificate_id`

(required) The OCID of the certificate.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`sort_by`

(optional) The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is ascending.

Allowed values are: 'VERSION_NUMBER'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`).

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://certificates.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Certificates Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-C1442D2D-C62C-4DA1-A395-AE2B7050BD75)
- [GET_CA_BUNDLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-942C5652-FFB8-4C3F-89BC-6D50C540B7FD)
- [GET_CERTIFICATE_AUTHORITY_BUNDLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-9AC0890F-20F5-43AC-9884-685EB1029694)
- [GET_CERTIFICATE_BUNDLE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-ADFAD318-B703-4CDA-8DFE-0F45F6E38D09)
- [LIST_CERTIFICATE_AUTHORITY_BUNDLE_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-B40E48B2-0ECF-442E-9AB6-F91AE0242AB5)
- [LIST_CERTIFICATE_BUNDLE_VERSIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cert_certificates.html#ADSDK-GUID-FA549CF7-E3B5-4F27-BB2B-F5CD70523CFE)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
