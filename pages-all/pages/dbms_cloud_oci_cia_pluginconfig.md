# Compute Instance Agent Plugin Config Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_pluginconfig.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_pluginconfig.html#dcoc-content-body)

## Compute Instance Agent Plugin Config Functions

Package: DBMS_CLOUD_OCI_CIA_PLUGINCONFIG

### LIST_INSTANCEAGENT_AVAILABLE_PLUGINS Function

The API to get the list of plugins that are available.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`os_name`

(required) The OS for which the plugin is supported. Examples of OperatingSystemQueryParam:OperatingSystemVersionQueryParam are as follows: 'CentOS' '6.10' , 'CentOS Linux' '7', 'CentOS Linux' '8', 'Oracle Linux Server' '6.10', 'Oracle Linux Server' '8.0', 'Red Hat Enterprise Linux Server' '7.8', 'Windows' '10', 'Windows' '2008ServerR2', 'Windows' '2012ServerR2', 'Windows' '7', 'Windows' '8.1'

`os_version`

(required) The OS version for which the plugin is supported.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for `TIMECREATED` is descending. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The `DISPLAYNAME` sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`name`

(optional) The plugin name

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Compute Instance Agent Plugin Config Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_pluginconfig.html#ADSDK-GUID-B0E9D4C6-E66A-45B2-A9A4-5F5A421D7C62)
- [LIST_INSTANCEAGENT_AVAILABLE_PLUGINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_pluginconfig.html#ADSDK-GUID-85F8B8C4-4B12-43B0-A0F6-98079935913B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
