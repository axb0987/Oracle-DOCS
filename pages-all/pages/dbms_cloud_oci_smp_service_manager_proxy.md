# Service Manager Proxy Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smp_service_manager_proxy.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smp_service_manager_proxy.html#dcoc-content-body)

## Service Manager Proxy Functions

Package: DBMS_CLOUD_OCI_SMP_SERVICE_MANAGER_PROXY

### GET_SERVICE_ENVIRONMENT Function

Get the detailed information for a specific service environment.

Syntax
```

```

Parameters

Parameter Description

`service_environment_id`

(required) The unique identifier associated with the service environment. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://smproxy.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SERVICE_ENVIRONMENTS Function

List the details of Software as a Service (SaaS) environments provisioned by Service Manager. Information includes the service instance endpoints and service definition details.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)for the compartment.

`service_environment_id`

(optional) The unique identifier associated with the service environment. **Note:** Not an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

`service_environment_type`

(optional) The environment's service definition type. For example, \"RGBUOROMS\" is the service definition type for \"Oracle Retail Order Management Cloud Service\".

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. ID is default ordered as ascending.

Allowed values are: 'ID'

`sort_order`

(optional) The sort order to use, either `ASC` or `DESC`.

Allowed values are: 'ASC', 'DESC'

`display_name`

(optional) The display name of the resource.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://smproxy.{region}.ocs.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Service Manager Proxy Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smp_service_manager_proxy.html#ADSDK-GUID-EC6C68A1-E778-42CD-BF4E-8D3ED4CEDF92)
- [GET_SERVICE_ENVIRONMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smp_service_manager_proxy.html#ADSDK-GUID-2BA43601-84DD-4E92-9B0F-CD15A632BD93)
- [LIST_SERVICE_ENVIRONMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_smp_service_manager_proxy.html#ADSDK-GUID-B10453C0-1A26-40FD-865D-4A0D36C18ADC)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
