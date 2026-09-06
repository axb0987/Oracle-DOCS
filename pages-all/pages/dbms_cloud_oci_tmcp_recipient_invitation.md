# Tenant Manager Control Plane Recipient Invitation Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#dcoc-content-body)

## Tenant Manager Control Plane Recipient Invitation Functions

Package: DBMS_CLOUD_OCI_TMCP_RECIPIENT_INVITATION

### ACCEPT_RECIPIENT_INVITATION Function

Accepts a recipient invitation.

Syntax
```

```

Parameters

Parameter Description

`recipient_invitation_id`

(required) OCID of recipient invitation to accept.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request, so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request will be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_RECIPIENT_INVITATION Function

Gets information about the recipient invitation.

Syntax
```

```

Parameters

Parameter Description

`recipient_invitation_id`

(required) OCID of the recipient invitation to retrieve.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IGNORE_RECIPIENT_INVITATION Function

Ignores a recipient invitation.

Syntax
```

```

Parameters

Parameter Description

`recipient_invitation_id`

(required) OCID of recipient invitation to ignore.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request, so it can be retried in case of a timeout or server error, without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request will be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_RECIPIENT_INVITATIONS Function

Return a (paginated) list of recipient invitations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`sender_tenancy_id`

(optional) The tenancy that sent the invitation.

`lifecycle_state`

(optional) The lifecycle state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(optional) The status of the recipient invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'IGNORED', 'EXPIRED', 'FAILED'

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_RECIPIENT_INVITATION Function

Updates the recipient invitation.

Syntax
```

```

Parameters

Parameter Description

`recipient_invitation_id`

(required) OCID of the recipient invitation to update.

`update_recipient_invitation_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Tenant Manager Control Plane Recipient Invitation Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-8B872F2E-66A9-45C6-A083-81D8C34AFD6E)
- [ACCEPT_RECIPIENT_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-8F2BB0B1-0D0F-41CB-AF1F-EF0350B7CCA5)
- [GET_RECIPIENT_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-9AF5DC37-2DBA-4311-8F29-B500F4E046BF)
- [IGNORE_RECIPIENT_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-80FD4C98-863F-4726-9FF4-9CECF3E3330F)
- [LIST_RECIPIENT_INVITATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-5FC507F8-F6DC-4BB7-9163-BD20649FD8AE)
- [UPDATE_RECIPIENT_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_recipient_invitation.html#ADSDK-GUID-6B3280F8-59D7-42A2-B4F4-A07654241274)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
