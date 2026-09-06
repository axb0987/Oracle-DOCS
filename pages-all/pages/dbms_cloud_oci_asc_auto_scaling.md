# Autoscaling Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html
- Fetched: 2026-09-05 19:04 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#dcoc-content-body)

## Autoscaling Functions

Package: DBMS_CLOUD_OCI_ASC_AUTO_SCALING

### CHANGE_AUTO_SCALING_CONFIGURATION_COMPARTMENT Function

Moves an autoscaling configuration into a different compartment within the same tenancy. For information about moving resources between compartments, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes). When you move an autoscaling configuration to a different compartment, associated resources such as instance pools are not moved.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`change_compartment_details`

(required) Request to change the compartment of given autoscaling configuration.

`opc_request_id`

(optional)

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTO_SCALING_CONFIGURATION Function

Creates an autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`create_auto_scaling_configuration_details`

(required) Creation details for an autoscaling configuration.

`opc_request_id`

(optional)

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTO_SCALING_POLICY Function

Creates an autoscaling policy for the specified autoscaling configuration. You can create the following types of autoscaling policies: - **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold. An autoscaling configuration can either have multiple schedule-based autoscaling policies, or one threshold-based autoscaling policy.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`create_auto_scaling_policy_details`

(required) Creation details for an autoscaling policy.

`opc_request_id`

(optional)

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTO_SCALING_CONFIGURATION Function

Deletes an autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTO_SCALING_POLICY Function

Deletes an autoscaling policy for the specified autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`auto_scaling_policy_id`

(required) The ID of the autoscaling policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTO_SCALING_CONFIGURATION Function

Gets information about the specified autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`opc_request_id`

(optional)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTO_SCALING_POLICY Function

Gets information about the specified autoscaling policy in the specified autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`auto_scaling_policy_id`

(required) The ID of the autoscaling policy.

`opc_request_id`

(optional)

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTO_SCALING_CONFIGURATIONS Function

Lists autoscaling configurations in the specifed compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the compartment containing the resource. Use tenancyId to search in the root compartment.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`opc_request_id`

(optional)

`limit`

(optional) For list pagination. The maximum number of items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTO_SCALING_POLICIES Function

Lists the autoscaling policies in the specified autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`display_name`

(optional) A filter to return only resources that match the given display name exactly.

`opc_request_id`

(optional)

`limit`

(optional) For list pagination. The maximum number of items to return in a paginated \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`page`

(optional) For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see[List Pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'TIMECREATED', 'DISPLAYNAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTO_SCALING_CONFIGURATION Function

Updates certain fields on the specified autoscaling configuration, such as the name, the cooldown period, and whether the autoscaling configuration is enabled.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`update_auto_scaling_configuration_details`

(required) Update details for an autoscaling configuration.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional)

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTO_SCALING_POLICY Function

Updates an autoscaling policy in the specified autoscaling configuration.

Syntax
```

```

Parameters

Parameter Description

`auto_scaling_configuration_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the autoscaling configuration.

`auto_scaling_policy_id`

(required) The ID of the autoscaling policy.

`update_auto_scaling_policy_details`

(required) Update details for an autoscaling policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional)

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (for example, if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://autoscaling.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Autoscaling Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-8D504E76-2253-4C76-A7F5-D75588BBBB0D)
- [CHANGE_AUTO_SCALING_CONFIGURATION_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-DC8A1961-FBF5-4560-BAE9-000B39272583)
- [CREATE_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-479AA5AF-D8F6-4305-9D42-F655376D73AF)
- [CREATE_AUTO_SCALING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-856EAE24-3008-43F3-9B41-46F62D08C370)
- [DELETE_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-5393A073-C8FF-4C72-9965-DE5B7556BF25)
- [DELETE_AUTO_SCALING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-E0E6E439-BCEA-4FAB-85EF-6833122D65BF)
- [GET_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-980E51C1-9A7D-4D8B-8F9A-655760920D09)
- [GET_AUTO_SCALING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-2E254994-F499-4B09-85C8-E6840D86F1DF)
- [LIST_AUTO_SCALING_CONFIGURATIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-980FA0D3-D2B5-4AEE-9A6A-C810487367C4)
- [LIST_AUTO_SCALING_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-BAA5A71D-ACE2-48D0-BBF3-77CF5704414C)
- [UPDATE_AUTO_SCALING_CONFIGURATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-D0EE238D-C3E5-47CC-B6DC-1679C6048EBC)
- [UPDATE_AUTO_SCALING_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_asc_auto_scaling.html#ADSDK-GUID-31111B9C-E8EB-4F14-B005-E35BFCF819E9)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
