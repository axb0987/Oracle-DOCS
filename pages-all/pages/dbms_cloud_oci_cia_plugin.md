# Compute Instance Agent Plugin Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_plugin.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_plugin.html#dcoc-content-body)

## Compute Instance Agent Plugin Functions

Package: DBMS_CLOUD_OCI_CIA_PLUGIN

### GET_INSTANCE_AGENT_PLUGIN Function

The API to get information for a plugin.

Syntax
```

```

Parameters

Parameter Description

`instanceagent_id`

(required) The OCID of the instance.

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`plugin_name`

(required) The name of the plugin.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://iaas.{region}.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INSTANCE_AGENT_PLUGINS Function

The API to get one or more plugin information.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment.

`instanceagent_id`

(required) The OCID of the instance.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`status`

(optional) The plugin status

Allowed values are: 'RUNNING', 'STOPPED', 'NOT_SUPPORTED', 'INVALID'

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

- [Compute Instance Agent Plugin Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_plugin.html#ADSDK-GUID-084358E8-C085-42B8-92CD-96F6A377BE01)
- [GET_INSTANCE_AGENT_PLUGIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_plugin.html#ADSDK-GUID-3E82A576-D3B0-4607-B380-F9DD3F56E1BC)
- [LIST_INSTANCE_AGENT_PLUGINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_cia_plugin.html#ADSDK-GUID-1213F4B8-F343-40DC-85B1-DB66A4570920)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
