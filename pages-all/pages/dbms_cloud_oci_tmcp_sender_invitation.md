# Tenant Manager Control Plane Sender Invitation Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html
- Fetched: 2026-09-05 19:14 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#dcoc-content-body)

## Tenant Manager Control Plane Sender Invitation Functions

Package: DBMS_CLOUD_OCI_TMCP_SENDER_INVITATION

### CANCEL_SENDER_INVITATION Function

Cancels a sender invitation.

Syntax
```

```

Parameters

Parameter Description

`sender_invitation_id`

(required) OCID of the sender invitation to cancel.

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

### CREATE_SENDER_INVITATION Function

Creates a sender invitation and asynchronously sends the invitation to the recipient.

Syntax
```

```

Parameters

Parameter Description

`create_sender_invitation_details`

(required) Parameters for sender invitation creation.

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

### GET_SENDER_INVITATION Function

Gets information about the sender invitation.

Syntax
```

```

Parameters

Parameter Description

`sender_invitation_id`

(required) OCID of the sender invitation to retrieve.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SENDER_INVITATIONS Function

Return a (paginated) list of sender invitations.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The ID of the compartment in which to list resources.

`recipient_tenancy_id`

(optional) The tenancy that the invitation is addressed to.

`lifecycle_state`

(optional) The lifecycle state of the resource.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'UPDATING', 'FAILED', 'TERMINATED'

`status`

(optional) The status of the sender invitation.

Allowed values are: 'PENDING', 'CANCELED', 'ACCEPTED', 'EXPIRED', 'FAILED'

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`opc_request_id`

(optional) The client request ID for tracing.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`limit`

(optional) The maximum number of items to return.

`sort_by`

(optional) The field to sort by. Only one sort order can be provided. * The default order for timeCreated is descending. * The default order for displayName is ascending. * If no value is specified, timeCreated is the default.

Allowed values are: 'timeCreated', 'displayName'

`sort_order`

(optional) The sort order to use, whether 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://organizations.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SENDER_INVITATION Function

Updates the sender invitation.

Syntax
```

```

Parameters

Parameter Description

`sender_invitation_id`

(required) OCID of the sender invitation to update.

`update_sender_invitation_details`

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

- [Tenant Manager Control Plane Sender Invitation Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-C7DA0ADC-3399-48B3-91F2-8D4D110F5D11)
- [CANCEL_SENDER_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-1E6B78C9-824D-408A-8220-8C3D28D40037)
- [CREATE_SENDER_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-91F7B8E5-A864-4A20-B4E9-2EA80D41C43D)
- [GET_SENDER_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-FD2478FB-AFEC-43C8-8199-9E50E479889A)
- [LIST_SENDER_INVITATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-A73A16B7-A9E9-4C06-9106-E04D48AEB55E)
- [UPDATE_SENDER_INVITATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_tmcp_sender_invitation.html#ADSDK-GUID-C63F2263-644B-4446-AF89-A9C0B5F81C1A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
