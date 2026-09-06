# Identity Functions
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html
- Fetched: 2026-09-05 19:08 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#dcoc-content-body)

## Identity Functions

Package: DBMS_CLOUD_OCI_ID_IDENTITY

### ACTIVATE_DOMAIN Function

(For tenancies that support identity domains) Activates a deactivated identity domain. You can only activate identity domains that your user account is not a part of. After you send the request, the `lifecycleDetails` of the identity domain is set to ACTIVATING. When the operation completes, the `lifecycleDetails` is set to null and the `lifecycleState` of the identity domain is set to ACTIVE. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ACTIVATE_MFA_TOTP_DEVICE Function

Activates the specified MFA TOTP device for the user. Activation requires manual interaction with the Console.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`mfa_totp_device_id`

(required) The OCID of the MFA TOTP device.

`mfa_totp_token`

(required) MFA TOTP token

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_TAG_DEFAULT_LOCK Function

Add a resource lock to a tag default.

Syntax
```

```

Parameters

Parameter Description

`tag_default_id`

(required) The OCID of the tag default.

`add_lock_details`

(required) Lock that is going to be added to resource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_TAG_NAMESPACE_LOCK Function

Add a resource lock to a tag namespace.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`add_lock_details`

(required) Lock that is going to be added to resource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ADD_USER_TO_GROUP Function

Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`add_user_to_group_details`

(required) Request object for adding a user to a group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ASSEMBLE_EFFECTIVE_TAG_SET Function

Assembles tag defaults in the specified compartment and any parent compartments to determine the tags to apply. Tag defaults from parent compartments do not override tag defaults referencing the same tag in a compartment lower down the hierarchy. This set of tag defaults includes all tag defaults from the current compartment back to the root compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_DELETE_RESOURCES Function

Deletes multiple resources in the compartment. All resources must be in the same compartment. You must have the appropriate permissions to delete the resources in the request. This API can only be invoked from the tenancy's[home region](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm#Home). This operation creates a`WORK_REQUEST`Type. Use the`GET_WORK_REQUEST`Function API to monitor the status of the bulk action.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`bulk_delete_resources_details`

(required) Request object for bulk delete resources in a compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_DELETE_TAGS Function

Deletes the specified tag key definitions. This operation triggers a process that removes the tags from all resources in your tenancy. The tag key definitions must be within the same tag namespace. The following actions happen immediately: * If the tag is a cost-tracking tag, the tag no longer counts against your 10 cost-tracking tags limit, even if you do not disable the tag before running this operation. * If the tag is used with dynamic groups, the rules that contain the tag are no longer evaluated against the tag. After you start this operation, the state of the tag changes to DELETING, and tag removal from resources begins. This process can take up to 48 hours depending on the number of resources that are tagged and the regions in which those resources reside. When all tags have been removed, the state changes to DELETED. You cannot restore a deleted tag. After the tag state changes to DELETED, you can use the same tag name again. After you start this operation, you cannot start either the`DELETE_TAG`Function or the`CASCADE_DELETE_TAG_NAMESPACE`Function operation until this process completes. In order to delete tags, you must first retire the tags. Use`UPDATE_TAG`Function to retire a tag.

Syntax
```

```

Parameters

Parameter Description

`bulk_delete_tags_details`

(required) Request object for deleting tags in bulk.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_EDIT_TAGS Function

Edits the specified list of tag key definitions for the selected resources. This operation triggers a process that edits the tags on all selected resources. The possible actions are: * Add a defined tag when the tag does not already exist on the resource. * Update the value for a defined tag when the tag is present on the resource. * Add a defined tag when it does not already exist on the resource or update the value for a defined tag when the tag is present on the resource. * Remove a defined tag from a resource. The tag is removed from the resource regardless of the tag value. See`BULK_EDIT_OPERATION_DETAILS`Function for more information. The edits can include a combination of operations and tag sets. However, multiple operations cannot apply to one key definition in the same request. For example, if one request adds `tag set-1` to a resource and sets a tag value to `tag set-2`, `tag set-1` and `tag set-2` cannot have any common tag definitions.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`bulk_edit_tags_details`

(optional) The request object for bulk editing tags on resources in the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### BULK_MOVE_RESOURCES Function

Moves multiple resources from one compartment to another. All resources must be in the same compartment. This API can only be invoked from the tenancy's[home region](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm#Home). To move resources, you must have the appropriate permissions to move the resource in both the source and target compartments. This operation creates a`WORK_REQUEST`Type. Use the`GET_WORK_REQUEST`Function API to monitor the status of the bulk action.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`bulk_move_resources_details`

(required) Request object for bulk move resources in the compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CASCADE_DELETE_TAG_NAMESPACE Function

Deletes the specified tag namespace. This operation triggers a process that removes all of the tags defined in the specified tag namespace from all resources in your tenancy and then deletes the tag namespace. After you start the delete operation: * New tag key definitions cannot be created under the namespace. * The state of the tag namespace changes to DELETING. * Tag removal from the resources begins. This process can take up to 48 hours depending on the number of tag definitions in the namespace, the number of resources that are tagged, and the locations of the regions in which those resources reside. After all tags are removed, the state changes to DELETED. You cannot restore a deleted tag namespace. After the deleted tag namespace changes its state to DELETED, you can use the name of the deleted tag namespace again. After you start this operation, you cannot start either the`DELETE_TAG`Function or the`BULK_DELETE_TAGS`Function operation until this process completes. To delete a tag namespace, you must first retire it. Use`UPDATE_TAG_NAMESPACE`Function to retire a tag namespace.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DOMAIN_COMPARTMENT Function

(For tenancies that support identity domains) Moves the identity domain to a different compartment in the tenancy. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`change_domain_compartment_details`

(required) The request object for moving the identity domain to a different compartment.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_DOMAIN_LICENSE_TYPE Function

(For tenancies that support identity domains) Changes the license type of the given identity domain. The identity domain's `lifecycleState` must be set to ACTIVE and the requested `licenseType` must be allowed. To retrieve the allowed `licenseType` for the identity domain, use`LIST_ALLOWED_DOMAIN_LICENSE_TYPES`Function. After you send your request, the `lifecycleDetails` of this identity domain is set to UPDATING. When the update of the identity domain completes, then the `lifecycleDetails` is set to null. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`change_domain_license_type_details`

(required) The request object for an update to the license type of the identity domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CHANGE_TAG_NAMESPACE_COMPARTMENT Function

Moves the specified tag namespace to the specified compartment within the same tenancy. To move the tag namespace, you must have the manage tag-namespaces permission on both compartments. For more information about IAM policies, see[Details for IAM](https://docs.oracle.com/iaas/Content/Identity/policyreference/iampolicyreference.htm). Moving a tag namespace moves all the tag key definitions contained in the tag namespace.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`change_tag_namespace_compartment_detail`

(required) Request object for changing the compartment of a tag namespace.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_AUTH_TOKEN Function

Creates a new auth token for the specified user. For information about what auth tokens are for, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm). You must specify a *description* for the auth token (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_AUTH_TOKEN`Function. Every user has permission to create an auth token for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create an auth token for any user, including themselves.

Syntax
```

```

Parameters

Parameter Description

`create_auth_token_details`

(required) Request object for creating a new auth token.

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_COMPARTMENT Function

Creates a new compartment in the specified compartment. Specify the parent compartment's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the compartment, which must be unique across all compartments in your tenancy. You can use this name or the OCID when writing policies that apply to the compartment. For more information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm). You must also specify a *description* for the compartment (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_COMPARTMENT`Function. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`create_compartment_details`

(required) Request object for creating a new compartment.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_CUSTOMER_SECRET_KEY Function

Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3 compatible API. The secret key consists of an Access Key/Secret Key pair. For information, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm). You must specify a *description* for the secret key (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_CUSTOMER_SECRET_KEY`Function. Every user has permission to create a secret key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a secret key for any user, including themselves.

Syntax
```

```

Parameters

Parameter Description

`create_customer_secret_key_details`

(required) Request object for creating a new secret key.

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DB_CREDENTIAL Function

Creates a new DB credential for the specified user.

Syntax
```

```

Parameters

Parameter Description

`create_db_credential_details`

(required) Request object for creating a new DB credential with the user.

`user_id`

(required) The OCID of the user.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DOMAIN Function

(For tenancies that support identity domains) Creates a new identity domain in the tenancy with the identity domain home in `homeRegion`. After you send your request, the temporary `lifecycleState` of this identity domain is set to CREATING and `lifecycleDetails` to UPDATING. When creation of the identity domain completes, this identity domain's `lifecycleState` is set to ACTIVE and `lifecycleDetails` to null. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. After creating an `identity domain`, first make sure its `lifecycleState` changes from CREATING to ACTIVE before you use it.

Syntax
```

```

Parameters

Parameter Description

`create_domain_details`

(required) The request object for creating a new identity domain.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_DYNAMIC_GROUP Function

Creates a new dynamic group in your tenancy. You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the dynamic group, which must be unique across all dynamic groups in your tenancy, and cannot be changed. Note that this name has to be also unique across all groups in your tenancy. You can use this name or the OCID when writing policies that apply to the dynamic group. For more information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm). You must also specify a *description* for the dynamic group (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_DYNAMIC_GROUP`Function. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`create_dynamic_group_details`

(required) Request object for creating a new dynamic group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_GROUP Function

Creates a new group in your tenancy. You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the group, which must be unique across all groups in your tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm). You must also specify a *description* for the group (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_GROUP`Function. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. After creating the group, you need to put users in it and write policies for it. See`ADD_USER_TO_GROUP`Function and`CREATE_POLICY`Function.

Syntax
```

```

Parameters

Parameter Description

`create_group_details`

(required) Request object for creating a new group.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IDENTITY_PROVIDER Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Creates a new identity provider in your tenancy. For more information, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the `IdentityProvider`, which must be unique across all `IdentityProvider` objects in your tenancy and cannot be changed. You must also specify a *description* for the `IdentityProvider` (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_IDENTITY_PROVIDER`Function. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`create_identity_provider_details`

(required) Request object for creating a new SAML2 identity provider.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_IDP_GROUP_MAPPING Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Creates a single mapping between an IdP group and an IAM Service`GROUP`Type.

Syntax
```

```

Parameters

Parameter Description

`create_idp_group_mapping_details`

(required) Add a mapping from an SAML2.0 identity provider group to a BMC group.

`identity_provider_id`

(required) The OCID of the identity provider.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_MFA_TOTP_DEVICE Function

Creates a new MFA TOTP device for the user. A user can have one MFA TOTP device.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_NETWORK_SOURCE Function

Creates a new network source in your tenancy. You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the network source, which must be unique across all network sources in your tenancy, and cannot be changed. You can use this name or the OCID when writing policies that apply to the network source. For more information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm). You must also specify a *description* for the network source (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_NETWORK_SOURCE`Function. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. After your network resource is created, you can use it in policy to restrict access to only requests made from an allowed IP address specified in your network source. For more information, see[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).

Syntax
```

```

Parameters

Parameter Description

`create_network_source_details`

(required) Request object for creating a new network source.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_O_AUTH_CLIENT_CREDENTIAL Function

Creates Oauth token for the user

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`create_o_auth2_client_credential_details`

(required) Request object containing the information required to generate an Oauth token.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_OR_RESET_UI_PASSWORD Function

Creates a new Console one-time password for the specified user. For more information about user credentials, see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm). Use this operation after creating a new user, or if a user forgets their password. The new one-time password is returned to you in the response, and you must securely deliver it to the user. They'll be prompted to change this password the next time they sign in to the Console. If they don't change it within 7 days, the password will expire and you'll need to create a new one-time password for the user. (For tenancies that support identity domains) Resetting a user's password generates a reset password email with a link that the user must follow to reset their password. If the user does not reset their password before the link expires, you'll need to reset the user's password again. **Note:** The user's Console login is the unique name you specified when you created the user (see`CREATE_USER`Function).

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_POLICY Function

Creates a new policy in the specified compartment (either the tenancy or another of your compartments). If you're new to policies, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). You must specify a *name* for the policy, which must be unique across all policies in your tenancy and cannot be changed. You must also specify a *description* for the policy (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_POLICY`Function. You must specify one or more policy statements in the statements array. For information about writing policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. New policies take effect typically within 10 seconds.

Syntax
```

```

Parameters

Parameter Description

`create_policy_details`

(required) Request object for creating a new policy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_REGION_SUBSCRIPTION Function

Creates a subscription to a region for a tenancy.

Syntax
```

```

Parameters

Parameter Description

`create_region_subscription_details`

(required) Request object for activate a new region.

`tenancy_id`

(required) The OCID of the tenancy.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SMTP_CREDENTIAL Function

Creates a new SMTP credential for the specified user. An SMTP credential has an SMTP user name and an SMTP password. You must specify a *description* for the SMTP credential (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_SMTP_CREDENTIAL`Function.

Syntax
```

```

Parameters

Parameter Description

`create_smtp_credential_details`

(required) Request object for creating a new SMTP credential with the user.

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_SWIFT_PASSWORD Function

**Deprecated. Use`CREATE_AUTH_TOKEN`Function instead.** Creates a new Swift password for the specified user. For information about what Swift passwords are for, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm). You must specify a *description* for the Swift password (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_SWIFT_PASSWORD`Function. Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a Swift password for any user, including themselves.

Syntax
```

```

Parameters

Parameter Description

`create_swift_password_details`

(required) Request object for creating a new swift password.

`user_id`

(required) The OCID of the user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TAG Function

Creates a new tag in the specified tag namespace. The tag requires either the OCID or the name of the tag namespace that will contain this tag definition. You must specify a *name* for the tag, which must be unique across all tags in the tag namespace and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters. Names are case insensitive. That means, for example, \"myTag\" and \"mytag\" are not allowed in the same namespace. If you specify a name that's already in use in the tag namespace, a 409 error is returned. The tag must have a *description*. It does not have to be unique, and you can change it with`UPDATE_TAG`Function. The tag must have a value type, which is specified with a validator. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. Lists are validiated. * If no `validator` is set, the user applying the tag to a resource can type in a static value or leave the tag value empty. * If a `validator` is set, the user applying the tag to a resource must select from a list of values that you supply with`ENUM_TAG_DEFINITION_VALIDATOR`Function.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`create_tag_details`

(required) Request object for creating a new tag in the specified tag namespace.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TAG_DEFAULT Function

Creates a new tag default in the specified compartment for the specified tag definition. If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

Syntax
```

```

Parameters

Parameter Description

`create_tag_default_details`

(required) Request object for creating a new tag default.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_TAG_NAMESPACE Function

Creates a new tag namespace in the specified compartment. You must specify the compartment ID in the request object (remember that the tenancy is simply the root compartment). You must also specify a *name* for the namespace, which must be unique across all namespaces in your tenancy and cannot be changed. The name can contain any ASCII character except the space (_) or period (.). Names are case insensitive. That means, for example, \"myNamespace\" and \"mynamespace\" are not allowed in the same tenancy. Once you created a namespace, you cannot change the name. If you specify a name that's already in use in the tenancy, a 409 error is returned. You must also specify a *description* for the namespace. It does not have to be unique, and you can change it with`UPDATE_TAG_NAMESPACE`Function.

Syntax
```

```

Parameters

Parameter Description

`create_tag_namespace_details`

(required) Request object for creating a new tag namespace.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### CREATE_USER Function

Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other IAM Service components, see[Overview of IAM](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm). You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). You must also specify a *name* for the user, which must be unique across all users in your tenancy and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods, underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error. This name will be the user's login to the Console. You might want to pick a name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses. If you delete a user and then create a new user with the same name, they'll be considered different users because they have different OCIDs. You must also specify a *description* for the user (although it can be an empty string). It does not have to be unique, and you can change it anytime with`UPDATE_USER`Function. You can use the field to provide the user's full name, a description, a nickname, or other information to generally identify the user. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. A new user has no permissions until you place the user in one or more groups (see`ADD_USER_TO_GROUP`Function). If the user needs to access the Console, you need to provide the user a password (see`CREATE_OR_RESET_UI_PASSWORD`Function). If the user needs to access the Oracle Cloud Infrastructure REST API, you need to upload a public API signing key for that user (see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm)and also`UPLOAD_API_KEY`Function). **Important:** Make sure to inform the new user which compartment(s) they have access to.

Syntax
```

```

Parameters

Parameter Description

`create_user_details`

(required) Request object for creating a new user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DEACTIVATE_DOMAIN Function

(For tenancies that support identity domains) Deactivates the specified identity domain. Identity domains must be in an ACTIVE `lifecycleState` and have no active apps present in the domain or underlying Identity Cloud Service stripe. You cannot deactivate the default identity domain. After you send your request, the `lifecycleDetails` of this identity domain is set to DEACTIVATING. When the operation completes, then the `lifecycleDetails` is set to null and the `lifecycleState` is set to INACTIVE. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_API_KEY Function

Deletes the specified API signing key for the specified user. Every user has permission to use this operation to delete a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to delete a key for any user, including themselves.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`fingerprint`

(required) The key's fingerprint.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_AUTH_TOKEN Function

Deletes the specified auth token for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`auth_token_id`

(required) The OCID of the auth token.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_COMPARTMENT Function

Deletes the specified compartment. The compartment must be empty.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_CUSTOMER_SECRET_KEY Function

Deletes the specified secret key for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`customer_secret_key_id`

(required) The access token of the secret key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DB_CREDENTIAL Function

Deletes the specified DB credential for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`db_credential_id`

(required) The OCID of the DB credential.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DOMAIN Function

(For tenancies that support identity domains) Deletes an identity domain. The identity domain must have no active apps present in the underlying IDCS stripe. You must also deactivate the identity domain, rendering the `lifecycleState` of the identity domain INACTIVE. Furthermore, as the authenticated user performing the operation, you cannot be a member of the identity domain you are deleting. Lastly, you cannot delete the default identity domain. A tenancy must always have at least the default identity domain. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_DYNAMIC_GROUP Function

Deletes the specified dynamic group.

Syntax
```

```

Parameters

Parameter Description

`dynamic_group_id`

(required) The OCID of the dynamic group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_GROUP Function

Deletes the specified group. The group must be empty.

Syntax
```

```

Parameters

Parameter Description

`group_id`

(required) The OCID of the group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IDENTITY_PROVIDER Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Deletes the specified identity provider. The identity provider must not have any group mappings (see`IDP_GROUP_MAPPING`Type).

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_IDP_GROUP_MAPPING Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Deletes the specified group mapping.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`mapping_id`

(required) The OCID of the group mapping.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_MFA_TOTP_DEVICE Function

Deletes the specified MFA TOTP device for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`mfa_totp_device_id`

(required) The OCID of the MFA TOTP device.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_NETWORK_SOURCE Function

Deletes the specified network source.

Syntax
```

```

Parameters

Parameter Description

`network_source_id`

(required) The OCID of the network source.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_O_AUTH_CLIENT_CREDENTIAL Function

Delete Oauth token for the user

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`oauth2_client_credential_id`

(required) The ID of the Oauth credential.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_POLICY Function

Deletes the specified policy. The deletion takes effect typically within 10 seconds.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SMTP_CREDENTIAL Function

Deletes the specified SMTP credential for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`smtp_credential_id`

(required) The OCID of the SMTP credential.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_SWIFT_PASSWORD Function

**Deprecated. Use`DELETE_AUTH_TOKEN`Function instead.** Deletes the specified Swift password for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`swift_password_id`

(required) The OCID of the Swift password.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TAG Function

Deletes the specified tag definition. This operation triggers a process that removes the tag from all resources in your tenancy. These things happen immediately: * If the tag was a cost-tracking tag, it no longer counts against your 10 cost-tracking tags limit, whether you first disabled it or not. * If the tag was used with dynamic groups, none of the rules that contain the tag will be evaluated against the tag. When you start the delete operation, the state of the tag changes to DELETING and tag removal from resources begins. This can take up to 48 hours depending on the number of resources that were tagged as well as the regions in which those resources reside. When all tags have been removed, the state changes to DELETED. You cannot restore a deleted tag. Once the deleted tag changes its state to DELETED, you can use the same tag name again. After you start this operation, you cannot start either the`BULK_DELETE_TAGS`Function or the`CASCADE_DELETE_TAG_NAMESPACE`Function operation until this process completes. To delete a tag, you must first retire it. Use`UPDATE_TAG`Function to retire a tag.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`tag_name`

(required) The name of the tag.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TAG_DEFAULT Function

Deletes the the specified tag default.

Syntax
```

```

Parameters

Parameter Description

`tag_default_id`

(required) The OCID of the tag default.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_TAG_NAMESPACE Function

Deletes the specified tag namespace. Only an empty tag namespace can be deleted with this operation. To use this operation to delete a tag namespace that contains tag definitions, first delete all of its tag definitions. Use`CASCADE_DELETE_TAG_NAMESPACE`Function to delete a tag namespace along with all of the tag definitions contained within that namespace. Use`DELETE_TAG`Function to delete a tag definition.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### DELETE_USER Function

Deletes the specified user. The user must not be in any groups.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### ENABLE_REPLICATION_TO_REGION Function

(For tenancies that support identity domains) Replicates the identity domain to a new region (provided that the region is the tenancy home region or other region that the tenancy subscribes to). You can only replicate identity domains that are in an ACTIVE `lifecycleState` and not currently updating or already replicating. You also can only trigger the replication of secondary identity domains. The default identity domain is automatically replicated to all regions that the tenancy subscribes to. After you send the request, the `state` of the identity domain in the replica region is set to ENABLING_REPLICATION. When the operation completes, the `state` is set to REPLICATION_ENABLED. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`enable_replication_to_region_details`

(required) The request object for replicating the identity domain to another region.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GENERATE_TOTP_SEED Function

Generate seed for the MFA TOTP device.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`mfa_totp_device_id`

(required) The OCID of the MFA TOTP device.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_AUTHENTICATION_POLICY Function

Gets the authentication policy for the given tenancy. You must specify your tenant's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_COMPARTMENT Function

Gets the specified compartment's information. This operation does not return a list of all the resources inside the compartment. There is no single API operation that does that. Compartments can contain multiple types of resources (instances, block storage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for each resource type and specify the compartment's OCID as a query parameter in the request. For example, call the`LIST_INSTANCES`Function operation in the Cloud Compute Service or the`LIST_VOLUMES`Function operation in Cloud Block Storage.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DOMAIN Function

(For tenancies that support identity domains) Gets the specified identity domain's information.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_DYNAMIC_GROUP Function

Gets the specified dynamic group's information.

Syntax
```

```

Parameters

Parameter Description

`dynamic_group_id`

(required) The OCID of the dynamic group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_GROUP Function

Gets the specified group's information. This operation does not return a list of all the users in the group. To do that, use`LIST_USER_GROUP_MEMBERSHIPS`Function and provide the group's OCID as a query parameter in the request.

Syntax
```

```

Parameters

Parameter Description

`group_id`

(required) The OCID of the group.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IAM_WORK_REQUEST Function

Gets the details of a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service.

Syntax
```

```

Parameters

Parameter Description

`iam_work_request_id`

(required) The OCID of the IAM work request.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IDENTITY_PROVIDER Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Gets the specified identity provider's information.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_IDP_GROUP_MAPPING Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Gets the specified group mapping.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`mapping_id`

(required) The OCID of the group mapping.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_MFA_TOTP_DEVICE Function

Get the specified MFA TOTP device for the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`mfa_totp_device_id`

(required) The OCID of the MFA TOTP device.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_NETWORK_SOURCE Function

Gets the specified network source's information.

Syntax
```

```

Parameters

Parameter Description

`network_source_id`

(required) The OCID of the network source.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_POLICY Function

Gets the specified policy's information.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the policy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_STANDARD_TAG_TEMPLATE Function

Retrieve the standard tag namespace template given the standard tag namespace name.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`standard_tag_namespace_name`

(required) The name of the standard tag namespace tempate that is requested

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TAG Function

Gets the specified tag's information.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`tag_name`

(required) The name of the tag.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TAG_DEFAULT Function

Retrieves the specified tag default.

Syntax
```

```

Parameters

Parameter Description

`tag_default_id`

(required) The OCID of the tag default.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TAG_NAMESPACE Function

Gets the specified tag namespace's information.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TAGGING_WORK_REQUEST Function

Gets details on a specified work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in tagging service.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_TENANCY Function

Get the specified tenancy's information.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER Function

Gets the specified user's information.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_GROUP_MEMBERSHIP Function

Gets the specified UserGroupMembership's information.

Syntax
```

```

Parameters

Parameter Description

`user_group_membership_id`

(required) The OCID of the userGroupMembership.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_USER_UI_PASSWORD_INFORMATION Function

Gets the specified user's console password information. The returned object contains the user's OCID, but not the password itself. The actual password is returned only when created or reset.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### GET_WORK_REQUEST Function

Gets details on a specified work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the compartment service.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### IMPORT_STANDARD_TAGS Function

OCI will release Tag Namespaces that our customers can import. These Tag Namespaces will provide Tags for our customers and Partners to provide consistency and enable data reporting.

Syntax
```

```

Parameters

Parameter Description

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`import_standard_tags_details`

(optional) The request object for creating or updating standard tag namespace.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_ALLOWED_DOMAIN_LICENSE_TYPES Function

(For tenancies that support identity domains) Lists the license types for identity domains supported by Oracle Cloud Infrastructure. (License types are also referred to as domain types.) If `currentLicenseTypeName` is provided, then the request returns license types that the identity domain with the specified license type name can change to. Otherwise, the request returns all valid license types currently supported.

Syntax
```

```

Parameters

Parameter Description

`current_license_type_name`

(optional) The license type of the identity domain.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_API_KEYS Function

Lists the API signing keys for the specified user. A user can have a maximum of three keys. Every user has permission to use this API call for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AUTH_TOKENS Function

Lists the auth tokens for the specified user. The returned object contains the token's OCID, but not the token itself. The actual token is returned only upon creation.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_AVAILABILITY_DOMAINS Function

Lists the availability domains in your tenancy. Specify the OCID of either the tenancy or another of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five). Note that the order of the results returned can change if availability domains are added or removed; therefore, do not create a dependency on the list order.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BULK_ACTION_RESOURCE_TYPES Function

Lists the resource-types supported by compartment bulk actions. Use this API to help you provide the correct resource-type information to the`BULK_DELETE_RESOURCES`Function and`BULK_MOVE_RESOURCES`Function operations. The returned list of resource-types provides the appropriate resource-type names to use with the bulk action operations along with the type of identifying information you'll need to provide for each resource-type. Most resource-types just require an[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)to identify a specific resource, but some resource-types, such as buckets, require you to provide other identifying information.

Syntax
```

```

Parameters

Parameter Description

`bulk_action_type`

(required) The type of bulk action.

Allowed values are: 'BULK_MOVE_RESOURCES', 'BULK_DELETE_RESOURCES'

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_BULK_EDIT_TAGS_RESOURCE_TYPES Function

Lists the resource types that support bulk tag editing.

Syntax
```

```

Parameters

Parameter Description

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COMPARTMENTS Function

Lists the compartments in a specified compartment. The members of the list returned depends on the values set for several parameters. With the exception of the tenancy (root compartment), the ListCompartments operation returns only the first-level child compartments in the parent compartment specified in `compartmentId`. The list does not include any subcompartments of the child compartments (grandchildren). The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (the resource can be in a subcompartment). The parameter `compartmentIdInSubtree` applies only when you perform ListCompartments on the tenancy (root compartment). When set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ANY. See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`access_level`

(optional) Valid values are `ANY` and `ACCESSIBLE`. Default is `ANY`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). For the compartments on which the user indirectly has INSPECT permissions, a restricted set of fields is returned. When set to `ANY` permissions are not checked.

Allowed values are: 'ANY', 'ACCESSIBLE'

`compartment_id_in_subtree`

(optional) Default is false. Can only be set to true when performing ListCompartments on the tenancy (root compartment). When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_COST_TRACKING_TAGS Function

Lists all the tags enabled for cost-tracking in the specified tenancy. For information about cost-tracking tags, see[Using Cost-tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_CUSTOMER_SECRET_KEYS Function

Lists the secret keys for the specified user. The returned object contains the secret key's OCID, but not the secret key itself. The actual secret key is returned only upon creation.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DB_CREDENTIALS Function

Lists the DB credentials for the specified user. The returned object contains the credential's OCID

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DOMAINS Function

(For tenancies that support identity domains) Lists all identity domains within a tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`display_name`

(optional) The mutable display name of the identity domain.

`url`

(optional) The region-agnostic identity domain URL.

`home_region_url`

(optional) The region-specific identity domain URL.

`l_type`

(optional) The identity domain type.

`license_type`

(optional) The license type of the identity domain.

`is_hidden_on_login`

(optional) Indicates whether or not the identity domain is visible at the sign-in screen.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_DYNAMIC_GROUPS Function

Lists the dynamic groups in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_FAULT_DOMAINS Function

Lists the Fault Domains in your tenancy. Specify the OCID of either the tenancy or another of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`availability_domain`

(required) The name of the availabilityDomain.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_GROUPS Function

Lists the groups in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IAM_WORK_REQUEST_ERRORS Function

Gets error details for a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service.

Syntax
```

```

Parameters

Parameter Description

`iam_work_request_id`

(required) The OCID of the IAM work request.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IAM_WORK_REQUEST_LOGS Function

Gets logs for a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service.

Syntax
```

```

Parameters

Parameter Description

`iam_work_request_id`

(required) The OCID of the IAM work request.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IAM_WORK_REQUESTS Function

Lists the IAM work requests in compartment. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`resource_identifier`

(optional) The identifier of the resource the work request affects.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IDENTITY_PROVIDER_GROUPS Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Lists the identity provider groups.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IDENTITY_PROVIDERS Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Lists all the identity providers in your tenancy. You must specify the identity provider type (e.g., `SAML2` for identity providers using the SAML2.0 protocol). You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`protocol`

(required) The protocol used for federation.

Allowed values are: 'SAML2'

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_IDP_GROUP_MAPPINGS Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Lists the group mappings for the specified identity provider.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_MFA_TOTP_DEVICES Function

Lists the MFA TOTP devices for the specified user. The returned object contains the device's OCID, but not the seed. The seed is returned only upon creation or when the IAM service regenerates the MFA seed for the device.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_NETWORK_SOURCES Function

Lists the network sources in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_O_AUTH_CLIENT_CREDENTIALS Function

List of Oauth tokens for the user

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_POLICIES Function

Lists the policies in the specified compartment (either the tenancy or another of your compartments). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five). To determine which policies apply to a particular group or compartment, you must view the individual statements inside all your policies. There isn't a way to automatically obtain that information via the API.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REGION_SUBSCRIPTIONS Function

Lists the region subscriptions for the specified tenancy.

Syntax
```

```

Parameters

Parameter Description

`tenancy_id`

(required) The OCID of the tenancy.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_REGIONS Function

Lists all the regions offered by Oracle Cloud Infrastructure.

Syntax
```

```

Parameters

Parameter Description

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SMTP_CREDENTIALS Function

Lists the SMTP credentials for the specified user. The returned object contains the credential's OCID, the SMTP user name but not the SMTP password. The SMTP password is returned only upon creation.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_STANDARD_TAG_NAMESPACES Function

Lists available standard tag namespaces that users can create.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_SWIFT_PASSWORDS Function

**Deprecated. Use`LIST_AUTH_TOKENS`Function instead.** Lists the Swift passwords for the specified user. The returned object contains the password's OCID, but not the password itself. The actual password is returned only upon creation.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAG_DEFAULTS Function

Lists the tag defaults for tag definitions in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`id`

(optional) A filter to only return resources that match the specified OCID exactly.

`compartment_id`

(optional) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`tag_definition_id`

(optional) The OCID of the tag definition.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAG_NAMESPACES Function

Lists the tag namespaces in the specified compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`include_subcompartments`

(optional) An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAGGING_WORK_REQUEST_ERRORS Function

Gets the errors for a work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAGGING_WORK_REQUEST_LOGS Function

Gets the logs for a work request.

Syntax
```

```

Parameters

Parameter Description

`work_request_id`

(required) The OCID of the work request.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAGGING_WORK_REQUESTS Function

Lists the tagging work requests in compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`resource_identifier`

(optional) The identifier of the resource the work request affects.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_TAGS Function

Lists the tag definitions in the specified tag namespace.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USER_GROUP_MEMBERSHIPS Function

Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (see[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five)). You must also then filter the list in one of these ways: - You can limit the results to just the memberships for a given user by specifying a `userId`. - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`. - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group. If the answer is no, the response is an empty list. - Although`userId` and `groupId` are not individually required, you must set one of them.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`user_id`

(optional) The OCID of the user.

`group_id`

(optional) The OCID of the group.

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_USERS Function

Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`identity_provider_id`

(optional) The id of the identity provider.

`external_identifier`

(optional) The id of a user in the identity provider.

`name`

(optional) A filter to only return resources that match the given name exactly.

`sort_by`

(optional) The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive. **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.

Allowed values are: 'TIMECREATED', 'NAME'

`sort_order`

(optional) The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.

Allowed values are: 'ASC', 'DESC'

`lifecycle_state`

(optional) A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### LIST_WORK_REQUESTS Function

Lists the work requests in compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment (remember that the tenancy is simply the root compartment).

`page`

(optional) The value of the `opc-next-page` response header from the previous \"List\" call.

`limit`

(optional) The maximum number of items to return in a paginated \"List\" call.

`resource_identifier`

(optional) The identifier of the resource the work request affects.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### MOVE_COMPARTMENT Function

Move the compartment to a different parent compartment in the same tenancy. When you move a compartment, all its contents (subcompartments and resources) are moved with it. Note that the `CompartmentId` that you specify in the path is the compartment that you want to move. **IMPORTANT**: After you move a compartment to a new parent compartment, the access policies of the new parent take effect and the policies of the previous parent no longer apply. Ensure that you are aware of the implications for the compartment contents before you move it. For more information, see[Moving a Compartment](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm#MoveCompartment).

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`move_compartment_details`

(required) Request object for moving a compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RECOVER_COMPARTMENT Function

Recover the compartment from DELETED state to ACTIVE state.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_TAG_DEFAULT_LOCK Function

Remove a resource lock from a tag default.

Syntax
```

```

Parameters

Parameter Description

`tag_default_id`

(required) The OCID of the tag default.

`remove_lock_details`

(required) Lock that is going to be removed from resource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_TAG_NAMESPACE_LOCK Function

Remove a resource lock from a tag namespace.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`remove_lock_details`

(required) Lock that is going to be removed from resource

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### REMOVE_USER_FROM_GROUP Function

Removes a user from a group by deleting the corresponding `UserGroupMembership`.

Syntax
```

```

Parameters

Parameter Description

`user_group_membership_id`

(required) The OCID of the userGroupMembership.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### RESET_IDP_SCIM_CLIENT Function

Resets the OAuth2 client credentials for the SCIM client associated with this identity provider.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTH_TOKEN Function

Updates the specified auth token's description.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`auth_token_id`

(required) The OCID of the auth token.

`update_auth_token_details`

(required) Request object for updating an auth token.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_AUTHENTICATION_POLICY Function

Updates authentication policy for the specified tenancy.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`update_authentication_policy_details`

(required) Request object for updating the authentication policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_COMPARTMENT Function

Updates the specified compartment's description or name. You can't update the root compartment.

Syntax
```

```

Parameters

Parameter Description

`compartment_id`

(required) The OCID of the compartment.

`update_compartment_details`

(required) Request object for updating a compartment.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_CUSTOMER_SECRET_KEY Function

Updates the specified secret key's description.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`customer_secret_key_id`

(required) The access token of the secret key.

`update_customer_secret_key_details`

(required) Request object for updating a secret key.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DOMAIN Function

(For tenancies that support identity domains) Updates identity domain information and the associated Identity Cloud Service (IDCS) stripe. To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

Syntax
```

```

Parameters

Parameter Description

`domain_id`

(required) The OCID of the identity domain.

`update_domain_details`

(required) Request object for updating the identity domain.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_DYNAMIC_GROUP Function

Updates the specified dynamic group.

Syntax
```

```

Parameters

Parameter Description

`dynamic_group_id`

(required) The OCID of the dynamic group.

`update_dynamic_group_details`

(required) Request object for updating an dynamic group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_GROUP Function

Updates the specified group.

Syntax
```

```

Parameters

Parameter Description

`group_id`

(required) The OCID of the group.

`update_group_details`

(required) Request object for updating a group.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IDENTITY_PROVIDER Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Updates the specified identity provider.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`update_identity_provider_details`

(required) Request object for updating a identity provider.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_IDP_GROUP_MAPPING Function

**Deprecated.** For more information, see[Deprecated IAM Service APIs](https://docs.oracle.com/iaas/Content/Identity/Reference/deprecatediamapis.htm). Updates the specified group mapping.

Syntax
```

```

Parameters

Parameter Description

`identity_provider_id`

(required) The OCID of the identity provider.

`mapping_id`

(required) The OCID of the group mapping.

`update_idp_group_mapping_details`

(required) Request object for updating an identity provider group mapping

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_NETWORK_SOURCE Function

Updates the specified network source.

Syntax
```

```

Parameters

Parameter Description

`network_source_id`

(required) The OCID of the network source.

`update_network_source_details`

(required) Request object for updating a network source.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_O_AUTH_CLIENT_CREDENTIAL Function

Updates Oauth token for the user

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`oauth2_client_credential_id`

(required) The ID of the Oauth credential.

`update_o_auth2_client_credential_details`

(required) Request object containing the information required to generate an Oauth token.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_POLICY Function

Updates the specified policy. You can update the description or the policy statements themselves. Policy changes take effect typically within 10 seconds.

Syntax
```

```

Parameters

Parameter Description

`policy_id`

(required) The OCID of the policy.

`update_policy_details`

(required) Request object for updating a policy.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SMTP_CREDENTIAL Function

Updates the specified SMTP credential's description.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`smtp_credential_id`

(required) The OCID of the SMTP credential.

`update_smtp_credential_details`

(required) Request object for updating a SMTP credential.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_SWIFT_PASSWORD Function

**Deprecated. Use`UPDATE_AUTH_TOKEN`Function instead.** Updates the specified Swift password's description.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`swift_password_id`

(required) The OCID of the Swift password.

`update_swift_password_details`

(required) Request object for updating a Swift password.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TAG Function

Updates the specified tag definition. Setting `validator` determines the value type. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. On update, any values in a list that were previously set do not change, but new values must pass validation. Values already applied to a resource do not change. You cannot remove list values that appear in a TagDefault. To remove a list value that appears in a TagDefault, first update the TagDefault to use a different value.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`tag_name`

(required) The name of the tag.

`update_tag_details`

(required) Request object for updating a tag.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TAG_DEFAULT Function

Updates the specified tag default. If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

Syntax
```

```

Parameters

Parameter Description

`tag_default_id`

(required) The OCID of the tag default.

`update_tag_default_details`

(required) Request object for updating a tag default.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`opc_request_id`

(optional) Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_TAG_NAMESPACE Function

Updates the the specified tag namespace. You can't update the namespace name. Updating `isRetired` to 'true' retires the namespace and all the tag definitions in the namespace. Reactivating a namespace (changing `isRetired` from 'true' to 'false') does not reactivate tag definitions. To reactivate the tag definitions, you must reactivate each one individually *after* you reactivate the namespace, using`UPDATE_TAG`Function. For more information about retiring tag namespaces, see[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys). You can't add a namespace with the same name as a retired namespace in the same tenancy.

Syntax
```

```

Parameters

Parameter Description

`tag_namespace_id`

(required) The OCID of the tag namespace.

`update_tag_namespace_details`

(required) Request object for updating a namespace.

`is_lock_override`

(optional) Whether to override locks (if any exist).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USER Function

Updates the description of the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`update_user_details`

(required) Request object for updating a user.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USER_CAPABILITIES Function

Updates the capabilities of the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`update_user_capabilities_details`

(required) Request object for updating user capabilities.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPDATE_USER_STATE Function

Updates the state of the specified user.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`update_state_details`

(required) Request object for updating a user state.

`if_match`

(optional) For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

### UPLOAD_API_KEY Function

Uploads an API signing key for the specified user. Every user has permission to use this operation to upload a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to upload a key for any user, including themselves. **Important:** Even though you have permission to upload an API key, you might not yet have permission to do much else. If you try calling an operation unrelated to your own credential management (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error, check with an administrator to confirm which IAM Service group(s) you're in and what access you have. Also confirm you're working in the correct compartment. After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

Syntax
```

```

Parameters

Parameter Description

`user_id`

(required) The OCID of the user.

`create_api_key_details`

(required) Request object for uploading an API key for a user.

`opc_retry_token`

(optional) A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations (e.g., if a resource has been deleted and purged from the system, then a retry of the original creation request may be rejected).

`region`

(optional) OCI region id. e.g us-phoenix-1 for US West (Phoenix).

`endpoint`

(optional) The endpoint of the service to call using this function. e.g https://identity.{region}.oci.{secondLevelDomain}.If both endpoint and region are given, then endpoint takes precedence.

`credential_name`

(optional) The name of the credential for authenticating with the corresponding cloud native API.

- [Identity Functions](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-FDDF201B-7B79-43CF-9011-004D7FADCD03)
- [ACTIVATE_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-82CCC884-B9C2-469B-87AC-FAAD00E65EFF)
- [ACTIVATE_MFA_TOTP_DEVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-CCA719AF-7D8F-42F2-A9DC-8CD55E8C5EF0)
- [ADD_TAG_DEFAULT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-79CA5400-A217-4675-A5D1-53C280A33DAB)
- [ADD_TAG_NAMESPACE_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6641DA60-4CE0-4862-85B2-E23B1BAAB5EA)
- [ADD_USER_TO_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2A06260A-86D1-4AF8-B017-22DD646307CB)
- [ASSEMBLE_EFFECTIVE_TAG_SET Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9D817038-097B-4BB1-881B-0AE12F7FC9BA)
- [BULK_DELETE_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-10B39E55-10E8-4C35-88E4-DF294087BEB7)
- [BULK_DELETE_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-391405ED-7972-4DCC-924A-E6B28FB2293D)
- [BULK_EDIT_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-559045A8-D3A1-4D48-A5F5-5385DE1C0DE3)
- [BULK_MOVE_RESOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-66F065E1-CB7D-465E-B090-A611B351E702)
- [CASCADE_DELETE_TAG_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2EA24E1B-94D0-449A-A915-98F7FD9BBDC6)
- [CHANGE_DOMAIN_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-CF8B1BE2-64C7-469B-AEEC-23F1CE8AE592)
- [CHANGE_DOMAIN_LICENSE_TYPE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-A45E696A-5D04-48FD-9821-FB037165C65D)
- [CHANGE_TAG_NAMESPACE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-48641B63-5B45-4B57-B5F8-1A1764CAE65D)
- [CREATE_AUTH_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-B32E16B1-01E3-4A3E-AF75-BEBC106C117B)
- [CREATE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-BBBB1907-BB8E-4E85-88ED-461A4FA5446B)
- [CREATE_CUSTOMER_SECRET_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-28A6B871-F6E0-48AB-A4C9-D1DB3DEF040A)
- [CREATE_DB_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6E8B2B87-4852-488F-A2C4-AEFA9DF540A0)
- [CREATE_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-00A93792-6D50-4D78-A1B4-4AA47F2CCC4D)
- [CREATE_DYNAMIC_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-DCE21950-4D72-4DC6-8C37-509C4B16C1EF)
- [CREATE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-7DCFD523-BC77-462B-AD04-48B1709E31F5)
- [CREATE_IDENTITY_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-22329DB1-318E-4581-B884-BC96D7D9056F)
- [CREATE_IDP_GROUP_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4FD279B1-1E5D-4CBB-A09E-583AE0F9E355)
- [CREATE_MFA_TOTP_DEVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-37ED4484-F746-49F2-991B-D5D1575D554E)
- [CREATE_NETWORK_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-55DB63B9-34FD-4E9F-809C-39755AB4F9A3)
- [CREATE_O_AUTH_CLIENT_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-84953F67-97AD-46C1-A220-07875378934D)
- [CREATE_OR_RESET_UI_PASSWORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-22A089A6-75EF-435B-910E-429B6F717858)
- [CREATE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-16E9620E-20ED-4602-B830-D3C8D6713F58)
- [CREATE_REGION_SUBSCRIPTION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9025F9CC-18FE-41A7-BEC1-339D51C12498)
- [CREATE_SMTP_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-42F73B8B-F73A-4CCB-B709-121BCF7B4CB2)
- [CREATE_SWIFT_PASSWORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-7F39EEB2-8CF3-4CAA-A8DB-964605CACFE4)
- [CREATE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5503EAFE-22B6-40AD-8731-CB2F27F1D355)
- [CREATE_TAG_DEFAULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-BEBF6A71-6D24-4CB1-A48C-4D4803B5D084)
- [CREATE_TAG_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-7957909F-A0F9-4CF8-9F57-A2B71CCBB1D6)
- [CREATE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-585B8B44-A661-435E-A62E-1D1CDEEFC55B)
- [DEACTIVATE_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-B1D1BA0D-E4AC-43FF-B936-60FC79A80418)
- [DELETE_API_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-8BD7933A-B185-4E40-9FAA-4F4B9EC08EB6)
- [DELETE_AUTH_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-DC257D76-BDDE-431B-BD00-0B4972F0A470)
- [DELETE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-ACA13A2E-2226-40CB-932A-5F3B19376FE7)
- [DELETE_CUSTOMER_SECRET_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C0A0CD97-4C84-4211-AB1B-949872D47F2A)
- [DELETE_DB_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5DC05FC2-3449-429E-9CFC-BAE840B09D03)
- [DELETE_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-915E3FC8-B283-4209-B0B9-4C366B0E5333)
- [DELETE_DYNAMIC_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9E18E7D0-D470-4FD0-9889-77752B461F4B)
- [DELETE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9D7CC0ED-54C2-4E11-B635-5345927BBDD4)
- [DELETE_IDENTITY_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9A2FA8B6-B3E2-47B2-8217-58D9A9219112)
- [DELETE_IDP_GROUP_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-56CF367E-1F93-4400-B0CA-9A6905FD3A99)
- [DELETE_MFA_TOTP_DEVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-0AB01210-FA17-472B-8605-137468132534)
- [DELETE_NETWORK_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-A3F18414-436F-40D1-83B0-C221C3C55D3C)
- [DELETE_O_AUTH_CLIENT_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-E11979AE-E6AA-4B40-8A8F-50282ED2489B)
- [DELETE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4C93696E-A612-4191-A7BC-841E4EDBF7B4)
- [DELETE_SMTP_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-F55D0D64-F250-45C9-9B09-0069BD5D7A55)
- [DELETE_SWIFT_PASSWORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-94801413-78AE-47DC-926E-A6267552CA5B)
- [DELETE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-E006E6DB-E171-4786-A812-2DB4177C906E)
- [DELETE_TAG_DEFAULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-7508F305-F237-4FB5-9605-D26AAB92341D)
- [DELETE_TAG_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-74D7638B-27CE-4DE9-9852-9ED6C5FB381C)
- [DELETE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-AF3A1C87-D9C8-439F-8CC9-6511D9494374)
- [ENABLE_REPLICATION_TO_REGION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1305F489-3719-4A75-9C19-F1BBE753AC55)
- [GENERATE_TOTP_SEED Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-52D9051D-05BE-4B09-8ECF-7C49CCC1872A)
- [GET_AUTHENTICATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-E3DD25D2-389F-4156-B903-DDB32266EC9C)
- [GET_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2EE683C0-A95C-40F5-9612-0A5D54881CF2)
- [GET_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-FC34EFF6-7829-424E-95A2-806185DF8E70)
- [GET_DYNAMIC_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-324AD32D-7363-4159-B98B-0F44500F0F4C)
- [GET_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C2CAC906-80E4-4B74-92CF-690914E8CDC5)
- [GET_IAM_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-D55FD7D4-9271-4857-BD84-950A2F831020)
- [GET_IDENTITY_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-8E223DDC-E457-47B2-8CD1-39CC7FB10954)
- [GET_IDP_GROUP_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2D80D6B8-6A63-4151-824A-8A3C8CE43F2C)
- [GET_MFA_TOTP_DEVICE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-48209519-5405-45CE-B84E-9829FF01458A)
- [GET_NETWORK_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6C8FEA05-270B-4E8D-89D9-74941E0622B4)
- [GET_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2DCD257F-145A-41DA-9F32-CE195D3603DA)
- [GET_STANDARD_TAG_TEMPLATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-87D33DBC-0EDB-46A1-8A80-F2CE6AF8F8B2)
- [GET_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-3C259FF2-CBEB-4201-A6C0-C013DAAD7357)
- [GET_TAG_DEFAULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1E81127F-DFB2-4015-BA0E-1346F7434F45)
- [GET_TAG_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5C506A7D-AFDB-45A0-8A97-5ECEA2267FFD)
- [GET_TAGGING_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-A66CBF28-E7A8-4DA6-B29D-0BBB6C1E829E)
- [GET_TENANCY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-99E76900-5068-4468-B44F-03578A19DF48)
- [GET_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-E33EE7A1-17F1-4238-9519-9A7DC0ADAC51)
- [GET_USER_GROUP_MEMBERSHIP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-3E0FD3DC-6BFC-4F2A-B955-A9820D03B1F4)
- [GET_USER_UI_PASSWORD_INFORMATION Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-18030F05-DBF7-4C24-931F-A3C614D27BF3)
- [GET_WORK_REQUEST Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-EDCE9568-60F2-4859-93B3-7ED5EC766CBF)
- [IMPORT_STANDARD_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-DEC5B755-7753-4B63-A563-A8850BC68130)
- [LIST_ALLOWED_DOMAIN_LICENSE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-33264FC1-05F9-4112-ACC8-C5865AD53166)
- [LIST_API_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-DC690CA9-5FC8-4C36-85A2-9C9C0843591B)
- [LIST_AUTH_TOKENS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4590FFFE-6B23-4218-8BBC-02A594CA5F03)
- [LIST_AVAILABILITY_DOMAINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-E4F6114C-256C-43DD-9A48-0E0B79319154)
- [LIST_BULK_ACTION_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-F6E4851E-35CD-436D-A540-19BF6D0E50DD)
- [LIST_BULK_EDIT_TAGS_RESOURCE_TYPES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-BC41CB57-6B2F-441A-A7C2-EE47136F2699)
- [LIST_COMPARTMENTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-33B9DB49-34E2-4B19-B397-656A8923482C)
- [LIST_COST_TRACKING_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-B7EE8B88-32DD-4163-B8AB-7C7D7CFA4153)
- [LIST_CUSTOMER_SECRET_KEYS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2B982E6C-275D-45E0-A08B-AA19C5BAC59B)
- [LIST_DB_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1C2960CE-AB97-4F5F-ADC8-4828336945C9)
- [LIST_DOMAINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-8AE53632-97B7-436C-817E-E3CE93019914)
- [LIST_DYNAMIC_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-CE186049-625E-47CF-B1EC-B7D34378FCDF)
- [LIST_FAULT_DOMAINS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5D12428C-4D8D-4B5A-9E94-08A9072E16EC)
- [LIST_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-96570BC7-FD28-4F73-BA72-32293457BC5B)
- [LIST_IAM_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-7FD7BC05-2244-45E8-9866-82EBC0C7413D)
- [LIST_IAM_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5A1C1B6C-581D-4F63-912A-11592043422B)
- [LIST_IAM_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-68CF9F03-DC68-4B07-AB26-601BCBE72A5A)
- [LIST_IDENTITY_PROVIDER_GROUPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-3BC33301-608F-4C49-95E7-642672299255)
- [LIST_IDENTITY_PROVIDERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-F938FE8C-8B78-46CB-AAAE-7AD08D02680A)
- [LIST_IDP_GROUP_MAPPINGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4DBCA519-9722-4437-8F00-767AB625A22D)
- [LIST_MFA_TOTP_DEVICES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C4503D7C-D278-480A-BCF2-8CFD3CA9D41F)
- [LIST_NETWORK_SOURCES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-04628E2D-808D-41C5-A4D6-20370B289D40)
- [LIST_O_AUTH_CLIENT_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-91FD42F9-CC94-408C-B6A7-EAF4FB6700D7)
- [LIST_POLICIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-23A1B519-13C7-4A65-9B58-51BB48023A58)
- [LIST_REGION_SUBSCRIPTIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-DD8C2E12-949B-493D-BF55-B5B54E056084)
- [LIST_REGIONS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-73A41499-818F-4181-8B64-0865D2DB9DEB)
- [LIST_SMTP_CREDENTIALS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-D8579F03-BB82-42AD-97F6-CEFF63595E48)
- [LIST_STANDARD_TAG_NAMESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C926DF21-8AC1-4F48-AB90-A735316F28E4)
- [LIST_SWIFT_PASSWORDS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1194EB5D-7E37-4AD6-BABF-B2F9A14DC674)
- [LIST_TAG_DEFAULTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-95FFF997-8AF3-44A0-A01F-EEAFCA07D6E7)
- [LIST_TAG_NAMESPACES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-399B6EA3-D599-4C84-AB22-A3ADF70DDFF4)
- [LIST_TAGGING_WORK_REQUEST_ERRORS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-0C2330DF-8E99-4235-847F-A988FF087F78)
- [LIST_TAGGING_WORK_REQUEST_LOGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C6CB48A5-7387-4113-AEC4-A3146E9E4A1F)
- [LIST_TAGGING_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-97276FBF-8BDA-47C4-A78B-0E2F4393F5FD)
- [LIST_TAGS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-13466842-1D32-414F-BB7A-EE2A99035A5D)
- [LIST_USER_GROUP_MEMBERSHIPS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-861A18A4-85A3-4EF0-9C42-9C34FFAD6AAE)
- [LIST_USERS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1C56DFE4-0FD9-47FC-92C5-72BA96C14603)
- [LIST_WORK_REQUESTS Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-FC2444AF-51A7-4DF5-9BCC-0CE6B19014C2)
- [MOVE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4F9EF690-A255-40FE-8188-B16CD88F9627)
- [RECOVER_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-CEFC1183-A728-4897-8080-592F4A218683)
- [REMOVE_TAG_DEFAULT_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-80A54C41-11E3-42F9-ABBC-B3DFEC94DAB4)
- [REMOVE_TAG_NAMESPACE_LOCK Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-FCE691CE-4CB3-46B5-A2A1-4768236AA0FA)
- [REMOVE_USER_FROM_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-79FB0A4D-032E-4475-A9AB-C5E5FCD36F59)
- [RESET_IDP_SCIM_CLIENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-66300BC0-0F83-4480-BCC5-F1C9B9C1AA04)
- [UPDATE_AUTH_TOKEN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1E5B0A73-DE9B-4373-A44F-2BB0ADD6A1EB)
- [UPDATE_AUTHENTICATION_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-4528B97D-33B1-4646-B3E5-3D756F3F11C2)
- [UPDATE_COMPARTMENT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6D306F83-AD04-47A1-B864-C9EE1494FFAA)
- [UPDATE_CUSTOMER_SECRET_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-3E9FDFF1-1FC2-4DBC-8788-0D6FE5CA71BE)
- [UPDATE_DOMAIN Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6614BD5A-766C-445D-B897-C3FC11E5114E)
- [UPDATE_DYNAMIC_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-57FEE14C-150B-44C0-BA1B-F0B449A7E9D8)
- [UPDATE_GROUP Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2EA22CB7-BAF1-4E45-8E15-68C16BA28AFD)
- [UPDATE_IDENTITY_PROVIDER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-064AA854-EA14-4B2D-92C6-719C70420375)
- [UPDATE_IDP_GROUP_MAPPING Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-D05B3F10-7983-44F7-AC6A-D9ED52A9E9BA)
- [UPDATE_NETWORK_SOURCE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-2A543CB1-DA76-482A-B77C-A9D31A1D68E3)
- [UPDATE_O_AUTH_CLIENT_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-5653486D-D0C6-446B-9A1E-EC5ED98C87BC)
- [UPDATE_POLICY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-55BE19CE-5D65-4852-B0E0-470E22665782)
- [UPDATE_SMTP_CREDENTIAL Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1230EA68-346F-4B5C-9732-5E973C04C37A)
- [UPDATE_SWIFT_PASSWORD Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-1A2AA036-9CBC-4869-8A37-7738CC51C819)
- [UPDATE_TAG Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-C28C7AB3-C270-4EF5-992C-8CB91DC443A8)
- [UPDATE_TAG_DEFAULT Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-9D01006D-B37F-43C1-A0BF-92BDAB6CE340)
- [UPDATE_TAG_NAMESPACE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-178690A0-53DB-42C9-A3B3-6780753724B3)
- [UPDATE_USER Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-604034CF-B6A8-4A8B-A641-31D1BE4829BB)
- [UPDATE_USER_CAPABILITIES Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-D0DC002D-DEDF-401D-BE8B-686459BE5249)
- [UPDATE_USER_STATE Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-8AE0132D-33C9-4580-82F1-74FE5CF14F6B)
- [UPLOAD_API_KEY Function](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/dbms_cloud_oci_id_identity.html#ADSDK-GUID-6ED98774-BE7F-4398-9EBC-7D84EE9293D8)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
