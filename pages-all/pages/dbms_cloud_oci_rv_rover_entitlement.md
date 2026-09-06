# Roving Edge Infrastructure Entitlement Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html
- Fetched: 2026-09-05 19:13 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#dcoc-content-body)

## Roving Edge Infrastructure Entitlement Functions

Package: DBMS_CLOUD_OCI_RV_ROVER_ENTITLEMENT

### CHANGE_ROVER_ENTITLEMENT_COMPARTMENT Function

Moves an entitlement into a different compartment.

Syntax
```

```

Parameters

Parameter Description

`rover_entitlement_id`

(required) ID of the rover node or cluster entitlement

`change_rover_entitlement_compartment_details`

(required) CompartmentId of the destination compartment

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_ROVER_ENTITLEMENT Function

Create the Entitlement to use a Rover Device. It requires some offline process of review and signatures before request is granted.

Syntax
```

```

Parameters

Parameter Description

`create_rover_entitlement_details`

(required) Creates a Rover Device Entitlement

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_ROVER_ENTITLEMENT Function

Deletes a rover entitlement

Syntax
```

```

Parameters

Parameter Description

`rover_entitlement_id`

(required) ID of the rover node or cluster entitlement

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_ROVER_ENTITLEMENT Function

Describes the Rover Device Entitlement in detail

Syntax
```

```

Parameters

Parameter Description

`rover_entitlement_id`

(required) ID of the rover node or cluster entitlement

`compartment_id`

(required) The OCID of the compartment in which to list resources.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations. For example, if a resource has been deleted and purged from the system, then a retry of the original creation request might be rejected.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ROVER_ENTITLEMENTS Function

Returns a list of RoverEntitlements.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment in which to list resources.

`id`

(optional) filtering by Rover Device Entitlement id

`display_name`

(optional) A filter to return only resources that match the entire display name given.

`lifecycle_state`

(optional) A filter to return only resources their lifecycleState matches the given lifecycleState.

Allowed values are: 'CREATING', 'UPDATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED'

`limit`

(optional) The maximum number of items to return.

`page`

(optional) The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.

`sort_order`

(optional) The sort order to use, either 'asc' or 'desc'.

Allowed values are: 'ASC', 'DESC'

`sort_by`

(optional) The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Allowed values are: 'timeCreated', 'displayName'

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_ROVER_ENTITLEMENT Function

Updates the RoverEntitlement

Syntax
```

```

Parameters

Parameter Description

`rover_entitlement_id`

(required) ID of the rover node or cluster entitlement

`update_rover_entitlement_details`

(required) The information to be updated.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) The client request ID for tracing.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://rover.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Roving Edge Infrastructure Entitlement Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-8DE33D97-9094-425A-B91D-B7779D6A737E)
- [CHANGE_ROVER_ENTITLEMENT_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-1F5E2FFB-33DF-4202-8078-6438E50E4824)
- [CREATE_ROVER_ENTITLEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-E28D25EA-4790-42BF-8A46-48B7982F62D2)
- [DELETE_ROVER_ENTITLEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-C4AE26CD-8A4F-4E67-9304-6B1E3739F164)
- [GET_ROVER_ENTITLEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-616C29D1-EC09-410D-A489-36C9F2AC8374)
- [LIST_ROVER_ENTITLEMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-B457823A-6D64-447A-B065-91D59AA29329)
- [UPDATE_ROVER_ENTITLEMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_rv_rover_entitlement.html#ADSDK-GUID-A972B091-E4D0-4200-A4B2-7A2D24DD509C)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
