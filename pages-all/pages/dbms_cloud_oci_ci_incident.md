# CIMS Incident Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html
- Fetched: 2026-09-05 19:05 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#dcoc-content-body)

## CIMS Incident Functions

Package: DBMS_CLOUD_OCI_CI_INCIDENT

### CREATE_INCIDENT Function

Operation to create a support ticket.

Syntax
```

```

Parameters

Parameter Description

`create_incident_details`

(required) Incident information

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_CSI_NUMBER Function

Fetches csi number of the user.

Syntax
```

```

Parameters

Parameter Description

`tenant_id`

(required) Tenancy Ocid in oracle cloud Infrastructure

`l_region`

(required) Home region of the customer which is part of oracle cloud infrastructure regions

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_INCIDENT Function

Gets details about the specified support ticket.

Syntax
```

```

Parameters

Parameter Description

`incident_key`

(required) Unique identifier for the support ticket.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`csi`

(optional) The Customer Support Identifier (CSI) associated with the support account.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`compartment_id`

(optional) The OCID of the tenancy.

`problemtype`

(optional) The kind of support request.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STATUS Function

Gets the status of the service.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INCIDENT_RESOURCE_TYPES Function

During support ticket creation, returns the list of all possible products that Oracle Cloud Infrastructure supports.

Syntax
```

```

Parameters

Parameter Description

`problem_type`

(required) The kind of support request.

`compartment_id`

(required) The OCID of the tenancy.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The key to use to sort the returned items.

Allowed values are: 'dateUpdated', 'severity'

`sort_order`

(optional) The order to sort the results in.

Allowed values are: 'ASC', 'DESC'

`name`

(optional) The user-friendly name of the support ticket type.

`csi`

(optional) The Customer Support Identifier (CSI) associated with the support account.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_INCIDENTS Function

Returns the list of support tickets raised by the tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the tenancy.

`csi`

(optional) The Customer Support Identifier (CSI) associated with the support account.

`limit`

(optional) For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The key to use to sort the returned items.

Allowed values are: 'dateUpdated', 'severity'

`sort_order`

(optional) The order to sort the results in.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) The current state of the ticket.

Allowed values are: 'ACTIVE', 'CLOSED'

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`problem_type`

(optional) The kind of support request.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_INCIDENT Function

Updates the specified support ticket's information.

Syntax
```

```

Parameters

Parameter Description

`incident_key`

(required) Unique identifier for the support ticket.

`update_incident_details`

(required) Details about the support ticket being updated.

`csi`

(optional) The Customer Support Identifier (CSI) associated with the support account.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`compartment_id`

(optional) The OCID of the tenancy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### VALIDATE_USER Function

Checks whether the requested user is valid.

Syntax
```

```

Parameters

Parameter Description

`csi`

(optional) The Customer Support Identifier (CSI) associated with the support account.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`problem_type`

(optional) The kind of support request.

Allowed values are: 'LIMIT', 'LEGACY_LIMIT', 'TECH', 'ACCOUNT', 'TAXONOMY'

`ocid`

(optional) User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.

`homeregion`

(optional) The region of the tenancy.

`bearertokentype`

(optional) Token type that determine which cloud provider the request come from.

`bearertoken`

(optional) Token that provided by multi cloud provider, which help to validate the email.

`idtoken`

(optional) IdToken that provided by multi cloud provider, which help to validate the email.

`domainid`

(optional) The OCID of identity domain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://incidentmanagement.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [CIMS Incident Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-EDB26473-7231-4CD2-BE14-17778D1324AF)
- [CREATE_INCIDENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-03E26395-154C-4228-ACC1-119F98A4E765)
- [GET_CSI_NUMBER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-9DDAD826-020E-4C55-8A26-0487DB2B5020)
- [GET_INCIDENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-0EA2622D-D200-45CD-9C30-50B1FCEFEB75)
- [GET_STATUS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-9F09E27C-C1B1-426D-8B64-466CCA6EEAA1)
- [LIST_INCIDENT_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-99A71EBA-A37A-4964-9157-260CE1B6742D)
- [LIST_INCIDENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-E89085F2-E409-436A-8D46-9545593928B5)
- [UPDATE_INCIDENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-29442024-AC22-48A5-91A0-05480ECCCE51)
- [VALIDATE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_ci_incident.html#ADSDK-GUID-EEA6F2E1-D16F-467A-AEC1-FA5ABF14485E)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
