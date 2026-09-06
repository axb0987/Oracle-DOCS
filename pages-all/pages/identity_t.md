# Identity Common Types
- Source: https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html
- Fetched: 2026-09-05 19:17 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#dcoc-content-body)

## Identity Common Types

### DBMS_CLOUD_OCI_IDENTITY_VARCHAR2_TBL Type

Nested table type of varchar2(32767).

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_ADD_LOCK_DETAILS_T Type

Request payload to add lock to the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

### DBMS_CLOUD_OCI_IDENTITY_ADD_USER_TO_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`user_id`

(required) The OCID of the user.

`group_id`

(required) The OCID of the group.

### DBMS_CLOUD_OCI_IDENTITY_ALLOWED_DOMAIN_LICENSE_TYPE_SUMMARY_T Type

(For tenancies that support identity domains) The 'AllowedDomainLicenseTypeSummary' object contains information about the license type of the identity domain.

Syntax
```

```

Fields

Field Description

`name`

(required) The license type name. Example: \"Oracle Apps Premium\"

`license_type`

(required) The license type identifier. Example: \"oracle-apps-premium\"

`description`

(required) The license type description.

### DBMS_CLOUD_OCI_IDENTITY_API_KEY_T Type

A PEM-format RSA credential for securing requests to the Oracle Cloud Infrastructure REST API. Also known as an *API signing key*. Specifically, this is the public key from the key pair. The private key remains with the user calling the API. For information about generating a key pair in the required PEM format, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). **Important:** This is **not** the SSH key for accessing compute instances. Each user can have a maximum of three API signing keys. For more information about user credentials, see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/Concepts/usercredentials.htm).

Syntax
```

```

Fields

Field Description

`key_id`

(optional) An Oracle-assigned identifier for the key, in this format: TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.

`key_value`

(optional) The key's value.

`fingerprint`

(optional) The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).

`user_id`

(optional) The OCID of the user the key belongs to.

`time_created`

(optional) Date and time the `ApiKey` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The API key's current state. After creating an `ApiKey` object, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_AUTH_TOKEN_T Type

An `AuthToken` is an Oracle-generated token string that you can use to authenticate with third-party APIs that do not support Oracle Cloud Infrastructure's signature-based authentication. For example, use an `AuthToken` to authenticate with a Swift client with the Object Storage Service. The auth token is associated with the user's Console login. Auth tokens never expire. A user can have up to two auth tokens at a time. **Note:** The token is always an Oracle-generated string; you can't change it to a string of your choice. For more information, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm).

Syntax
```

```

Fields

Field Description

`token`

(optional) The auth token. The value is available only in the response for `CreateAuthToken`, and not for `ListAuthTokens` or `UpdateAuthToken`.

`id`

(optional) The OCID of the auth token.

`user_id`

(optional) The OCID of the user the auth token belongs to.

`description`

(optional) The description you assign to the auth token. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`time_created`

(optional) Date and time the `AuthToken` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this auth token will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The token's current state. After creating an auth token, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_PASSWORD_POLICY_T Type

Password policy, currently set for the given compartment.

Syntax
```

```

Fields

Field Description

`minimum_password_length`

(optional) Minimum password length required.

`is_uppercase_characters_required`

(optional) At least one uppercase character required.

`is_lowercase_characters_required`

(optional) At least one lower case character required.

`is_numeric_characters_required`

(optional) At least one numeric character required.

`is_special_characters_required`

(optional) At least one special character required.

`is_username_containment_allowed`

(optional) User name is allowed to be part of the password.

### DBMS_CLOUD_OCI_IDENTITY_NETWORK_POLICY_T Type

Network policy, which consists of a list of network source IDs.

Syntax
```

```

Fields

Field Description

`network_source_ids`

(optional) Network Source ids

### DBMS_CLOUD_OCI_IDENTITY_AUTHENTICATION_POLICY_T Type

Authentication policy, currently set for the given compartment.

Syntax
```

```

Fields

Field Description

`password_policy`

(optional)

`compartment_id`

(optional) Compartment OCID.

`network_policy`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_AVAILABILITY_DOMAIN_T Type

One or more isolated, fault-tolerant Oracle data centers that host cloud resources such as instances, volumes, and subnets. A region contains several Availability Domains. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the Availability Domain.

`id`

(optional) The OCID of the Availability Domain.

`compartment_id`

(optional) The OCID of the tenancy.

### DBMS_CLOUD_OCI_IDENTITY_BASE_TAG_DEFINITION_VALIDATOR_T Type

Validates a definedTag value. Each validator performs validation steps in addition to the standard validation for definedTag values. For more information, see[Limits on Tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm#limits). If you define a validator after a value has been set for a defined tag, then any updates that attempt to change the value must pass the additional validation defined by the current rule. Previously set values (even those that would fail the current validation) are not updated. You can still update other attributes to resources that contain a non-valid defined tag. To clear the validator call UpdateTag with[DefaultTagDefinitionValidator](https://docs.oracle.com/iaas/api/#/en/identity/latest/datatypes/DefaultTagDefinitionValidator).

Syntax
```

```

Fields

Field Description

`validator_type`

(required) Specifies the type of validation: a static value (no validation) or a list.

Allowed values are: 'ENUM', 'DEFAULT'

### DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_T Type

The bulk action resource entity.

Syntax
```

```

Fields

Field Description

`identifier`

(required) The resource OCID.

`entity_type`

(required) The resource-type. To get the list of supported resource-types use`LIST_BULK_ACTION_RESOURCE_TYPES`Function.

`metadata`

(optional) Additional information that helps to identity the resource for bulk action. The APIs to delete and move most resource types only require the resource identifier (ocid). But some resource-types require additional identifying information. This information is provided in the resource's public API document. It is also available through the`LIST_BULK_ACTION_RESOURCE_TYPES`Function. **Example**: The APIs to delete or move the `buckets` resource-type require `namespaceName` and `bucketName` to identify the resource, as shown in the APIs,`DELETE_BUCKET`Function and`UPDATE_BUCKET`Function. To add a bucket for bulk actions, specify `namespaceName` and `bucketName` in the metadata property as shown in this example { \"identifier\": \"&lt;OCID_of_bucket&gt;\" \"entityType\": \"bucket\", \"metadata\": { \"namespaceName\": \"sampleNamespace\", \"bucketName\": \"sampleBucket\" } }

### DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_T Type

Syntax
```

```

Fields

Field Description

`name`

(required) The unique name of the resource-type.

`metadata_keys`

(optional) List of metadata keys required to identify a specific resource. Some resource-types require information besides an OCID to identify a specific resource. For example, the resource-type `buckets` requires metadataKeys`DELETE_BUCKET`Function.

### DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_TBL Type

Nested table type of dbms_cloud_oci_identity_bulk_action_resource_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_COLLECTION_T Type

Collection of resource-types supported by a compartment bulk action.

Syntax
```

```

Fields

Field Description

`items`

(required) Collection of the resource-types supported by a compartment bulk action.

### DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_identity_bulk_action_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_BULK_DELETE_RESOURCES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`resources`

(required) The resources to be deleted.

### DBMS_CLOUD_OCI_IDENTITY_BULK_DELETE_TAGS_DETAILS_T Type

Properties for deleting tags in bulk

Syntax
```

```

Fields

Field Description

`tag_definition_ids`

(required) The OCIDs of the tag definitions to delete

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_OPERATION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`operation_type`

(required) An enum-like description of the type of operation. * `ADD_WHERE_ABSENT` adds a defined tag only if the tag does not already exist on the resource. * `SET_WHERE_PRESENT` updates the value for a defined tag only if the tag is present on the resource. * `ADD_OR_SET` combines the first two operations to add a defined tag if it does not already exist on the resource or update the value for a defined tag only if the tag is present on the resource. * `REMOVE` removes the defined tag from the resource. The tag is removed from the resource regardless of the tag value.

Allowed values are: 'ADD_WHERE_ABSENT', 'SET_WHERE_PRESENT', 'ADD_OR_SET', 'REMOVE'

`defined_tags`

(required) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_RESOURCE_T Type

Syntax
```

```

Fields

Field Description

`id`

(required) The unique OCID of the resource.

`resource_type`

(required) The type of resource. See`LIST_BULK_EDIT_TAGS_RESOURCE_TYPES`Function.

`metadata`

(optional) Additional information that identifies the resource for bulk editing of tags. This information is provided in the resource's API documentation.

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_identity_bulk_edit_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_OPERATION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_identity_bulk_edit_operation_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the bulk tag edit request is submitted.

`resources`

(required) The resources to be updated.

`bulk_edit_operations`

(required) The operations associated with the request to bulk edit tags.

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_T Type

Syntax
```

```

Fields

Field Description

`resource_type`

(required) The unique name of the resource type.

`metadata_keys`

(optional) The metadata keys required to identify the resource. For example, for a bucket, the value of `metadataKeys` will be[\"namespaceName\", \"bucketName\"]. This information will match the API documentation. See [UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket)and[DeleteBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/DeleteBucket).

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_TBL Type

Nested table type of dbms_cloud_oci_identity_bulk_edit_tags_resource_type_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_COLLECTION_T Type

The list of resource types that support bulk editing of tags.

Syntax
```

```

Fields

Field Description

`items`

(required) The collection of resource types that support bulk editing of tags.

### DBMS_CLOUD_OCI_IDENTITY_BULK_MOVE_RESOURCES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`resources`

(required) The resources to be moved.

`target_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment into which to move the resources.

### DBMS_CLOUD_OCI_IDENTITY_CHANGE_DOMAIN_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment into which to move the identity domain.

### DBMS_CLOUD_OCI_IDENTITY_CHANGE_DOMAIN_LICENSE_TYPE_DETAILS_T Type

(For tenancies that support identity domains) Details for updating the license type of the identity domain.

Syntax
```

```

Fields

Field Description

`license_type`

(optional) The license type of the identity domain.

### DBMS_CLOUD_OCI_IDENTITY_CHANGE_TAG_NAMESPACE_COMPARTMENT_DETAIL_T Type

Details of the compartment the resource is being moved to.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The Oracle Cloud ID (OCID) of the destination compartment.

### DBMS_CLOUD_OCI_IDENTITY_CHANGE_TAS_DOMAIN_LICENSE_TYPE_DETAILS_T Type

(For tenancies that support identity domains) Update the identity domain license type.

Syntax
```

```

Fields

Field Description

`license_type`

(optional) The license type of the identity domain.

### DBMS_CLOUD_OCI_IDENTITY_COMPARTMENT_T Type

A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of IAM Service policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. For more information, see[Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). To place a resource in a compartment, simply specify the compartment ID in the \"Create\" request object when initially creating the resource. For example, to launch an instance into a particular compartment, specify that compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one compartment to another. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the compartment.

`compartment_id`

(required) The OCID of the parent compartment containing the compartment.

`name`

(required) The name you assign to the compartment during creation. The name must be unique across all compartments in the parent. Avoid entering confidential information.

`description`

(required) The description you assign to the compartment. Does not have to be unique, and it's changeable.

`time_created`

(required) Date and time the compartment was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`is_accessible`

(optional) Indicates whether or not the compartment is accessible for the user making the request. Returns true when the user has INSPECT permissions directly on a resource in the compartment or indirectly (permissions can be on a resource in a subcompartment).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_API_KEY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`key`

(required) The public key. Must be an RSA key in PEM format.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_AUTH_TOKEN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(required) The description you assign to the auth token during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the parent compartment containing the compartment.

`name`

(required) The name you assign to the compartment during creation. The name must be unique across all compartments in the parent compartment. Avoid entering confidential information.

`description`

(required) The description you assign to the compartment during creation. Does not have to be unique, and it's changeable.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_CUSTOMER_SECRET_KEY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(required) The name you assign to the secret key during creation. Does not have to be unique, and it's changeable.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_DB_CREDENTIAL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`password`

(required) The password for the DB credentials during creation.

`description`

(required) The description you assign to the DB credentials during creation. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_DOMAIN_DETAILS_T Type

(For tenancies that support identity domains) Details for creating an identity domain.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the identity domain is created.

`display_name`

(required) The mutable display name of the identity domain.

`description`

(required) The identity domain description. You can have an empty description.

`home_region`

(required) The region's name identifier. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names. Example: `us-phoenix-1`

`license_type`

(required) The license type of the identity domain.

`is_hidden_on_login`

(optional) Indicates whether the identity domain is hidden on the sign-in screen or not.

`admin_first_name`

(optional) The administrator's first name.

`admin_last_name`

(optional) The administrator's last name.

`admin_user_name`

(optional) The administrator's user name.

`admin_email`

(optional) The administrator's email address.

`is_notification_bypassed`

(optional) Indicates whether or not the administrator user created in the IDCS stripe would like to receive notifications like a welcome email. This field is required only if admin information is provided. This field is otherwise optional.

`is_primary_email_required`

(optional) Optional field to indicate whether users in the identity domain are required to have a primary email address or not. The default is true.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_DYNAMIC_GROUP_DETAILS_T Type

Properties for creating a dynamic group.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the group.

`name`

(required) The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`matching_rule`

(required) The matching rule to dynamically match an instance certificate to this dynamic group. For rule syntax, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).

`description`

(required) The description you assign to the group during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the group.

`name`

(required) The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`description`

(required) The description you assign to the group during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_IDENTITY_PROVIDER_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of your tenancy.

`name`

(required) The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed.

`description`

(required) The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable.

`product_type`

(required) The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS). Example: `IDCS`

Allowed values are: 'IDCS', 'ADFS'

`protocol`

(required) The protocol used for federation. Example: `SAML2`

Allowed values are: 'SAML2', 'ADFS'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_IDP_GROUP_MAPPING_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`idp_group_name`

(required) The name of the IdP group you want to map.

`group_id`

(required) The OCID of the IAM Service`GROUP`Type you want to map to the IdP group.

### DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_VIRTUAL_SOURCE_LIST_T Type

Syntax
```

```

Fields

Field Description

`vcn_id`

(optional)

`ip_ranges`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_VIRTUAL_SOURCE_LIST_TBL Type

Nested table type of dbms_cloud_oci_identity_network_sources_virtual_source_list_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_CREATE_NETWORK_SOURCE_DETAILS_T Type

Properties for creating a network source object.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy (root compartment) containing the network source object.

`name`

(required) The name you assign to the network source during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`public_source_list`

(optional) A list of allowed public IP addresses and CIDR ranges.

`virtual_source_list`

(optional) A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

`services`

(optional) -- The services attribute has no effect and is reserved for use by Oracle. --

`description`

(required) The description you assign to the network source during creation. Does not have to be unique, and it's changeable.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_FULLY_QUALIFIED_SCOPE_T Type

Syntax
```

```

Fields

Field Description

`audience`

(required) Audience for the given scope context.

`scope`

(required) Allowed permission scope for the given context.

### DBMS_CLOUD_OCI_IDENTITY_FULLY_QUALIFIED_SCOPE_TBL Type

Nested table type of dbms_cloud_oci_identity_fully_qualified_scope_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_CREATE_O_AUTH2_CLIENT_CREDENTIAL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`name`

(required) Name of the oauth credential to help user differentiate them.

`description`

(required) Description of the oauth credential to help user differentiate them.

`scopes`

(required) Allowed scopes for the given oauth credential.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_POLICY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment containing the policy (either the tenancy or another compartment).

`name`

(required) The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed.

`statements`

(required) An array of policy statements written in the policy language. See[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

`description`

(required) The description you assign to the policy during creation. Does not have to be unique, and it's changeable.

`version_date`

(optional) The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_REGION_SUBSCRIPTION_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`region_key`

(required) The regions's key. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported 3-letter region codes. Example: `PHX`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_SAML2_IDENTITY_PROVIDER_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_identity_create_saml2_identity_provider_details_t`is a subtype of the`dbms_cloud_oci_identity_create_identity_provider_details_t`type.

Fields

Field Description

`metadata_url`

(required) The URL for retrieving the identity provider's metadata, which contains information required for federating.

`metadata`

(required) The XML that contains the information required for federating.

`freeform_attributes`

(optional) Extra name value pairs associated with this identity provider. Example: `{\"clientId\": \"app_sf3kdjf3\"}`

### DBMS_CLOUD_OCI_IDENTITY_CREATE_SMTP_CREDENTIAL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(required) The description you assign to the SMTP credentials during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_SWIFT_PASSWORD_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(required) The description you assign to the Swift password during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_ADD_LOCK_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_identity_add_lock_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_DEFAULT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.

`tag_definition_id`

(required) The OCID of the tag definition. The tag default will always assign a default value for this tag definition.

`value`

(required) The default value for the tag definition. This will be applied to all new resources created in the compartment.

`is_required`

(optional) If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. Example: `false`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`name`

(required) The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.

`description`

(required) The description you assign to the tag during creation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_cost_tracking`

(optional) Indicates whether the tag is enabled for cost tracking.

`validator`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_NAMESPACE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the tag namespace.

`name`

(required) The name you assign to the tag namespace during creation. It must be unique across all tag namespaces in the tenancy and cannot be changed.

`description`

(required) The description you assign to the tag namespace during creation.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_CREATE_USER_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the tenancy containing the user.

`name`

(required) The name you assign to the user during creation. This is the user's login for the Console. The name must be unique across all users in the tenancy and cannot be changed.

`description`

(required) The description you assign to the user during creation. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`email`

(optional) The email you assign to the user during creation. The email must be unique across all users in the tenancy. (For tenancies that support identity domains) You must provide an email for each user.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_CUSTOMER_SECRET_KEY_T Type

A `CustomerSecretKey` is an Oracle-provided key for using the Object Storage Service's[Amazon S3 compatible API](https://docs.oracle.com/iaas/Content/Object/Tasks/s3compatibleapi.htm). The key consists of a secret key/access key pair. A user can have up to two secret keys at a time. **Note:** The secret key is always an Oracle-generated string; you can't change it to a string of your choice. For more information, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm).

Syntax
```

```

Fields

Field Description

`key`

(optional) The secret key.

`id`

(optional) The access key portion of the key pair.

`user_id`

(optional) The OCID of the user the password belongs to.

`display_name`

(optional) The display name you assign to the secret key. Does not have to be unique, and it's changeable.

`time_created`

(optional) Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this password will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_CUSTOMER_SECRET_KEY_SUMMARY_T Type

As the name suggests, a `CustomerSecretKeySummary` object contains information about a `CustomerSecretKey`. A `CustomerSecretKey` is an Oracle-provided key for using the Object Storage Service's Amazon S3 compatible API.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the secret key.

`user_id`

(optional) The OCID of the user the password belongs to.

`display_name`

(optional) The displayName you assign to the secret key. Does not have to be unique, and it's changeable.

`time_created`

(optional) Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this password will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_DB_CREDENTIAL_T Type

Database credentials are needed for onboarding cloud database to identity. The DB credentials are used for DB authentication with the service.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the DB credential.

`user_id`

(optional) The OCID of the user the DB credential belongs to.

`time_created`

(optional) Date and time the `DbCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'DELETED'

`lifecycle_details`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_DB_CREDENTIAL_SUMMARY_T Type

As the name suggests, an `DbCredentialSummary` object contains information about an `DbCredential`. The DB credential is used for DB authentication with the [DB Service].

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the DB credential.

`user_id`

(optional) The OCID of the user the DB credential belongs to.

`description`

(optional) The description you assign to the DB credential. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`time_created`

(optional) Date and time the `DbCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

### DBMS_CLOUD_OCI_IDENTITY_DEFAULT_TAG_DEFINITION_VALIDATOR_T Type

Use this validator to clear any existing validator on the tag key definition with the UpdateTag operation. Using this `validatorType` is the same as not setting any value on the validator field. The resultant value for `validatorType` returned in the response body is `null`.

Syntax
```

```

`dbms_cloud_oci_identity_default_tag_definition_validator_t`is a subtype of the`dbms_cloud_oci_identity_base_tag_definition_validator_t`type.

### DBMS_CLOUD_OCI_IDENTITY_REPLICATED_REGION_DETAILS_T Type

(For tenancies that support identity domains) Properties for a region where a replica for the identity domain exists.

Syntax
```

```

Fields

Field Description

`l_region`

(optional) A REPLICATION_ENABLED region, e.g. us-ashburn-1. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names.

`url`

(optional) Region-agnostic identity domain URL.

`regional_url`

(optional) Region-specific identity domain URL.

`state`

(optional) The IDCS-replicated region state.

Allowed values are: 'ENABLING_REPLICATION', 'REPLICATION_ENABLED', 'DISABLING_REPLICATION', 'REPLICATION_DISABLED', 'DELETED'

### DBMS_CLOUD_OCI_IDENTITY_REPLICATED_REGION_DETAILS_TBL Type

Nested table type of dbms_cloud_oci_identity_replicated_region_details_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DOMAIN_T Type

(For tenancies that support identity domains) Properties for an identity domain. An identity domain is used to manage users and groups, integration standards, external identities, and secure application integration through Oracle Single Sign-on (SSO) configuration.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the identity domain.

`compartment_id`

(required) The OCID of the compartment containing the identity domain.

`display_name`

(required) The mutable display name of the identity domain.

`description`

(required) The identity domain description. You can have an empty description.

`url`

(required) Region-agnostic identity domain URL.

`home_region_url`

(required) Region-specific identity domain URL.

`home_region`

(required) The home region for the identity domain. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names. Example: `us-phoenix-1`

`replica_regions`

(required) The regions where replicas of the identity domain exist.

`l_type`

(required) The type of the domain.

Allowed values are: 'DEFAULT', 'SECONDARY'

`license_type`

(required) The license type of the identity domain.

`is_hidden_on_login`

(required) Indicates whether the identity domain is hidden on the sign-in screen or not.

`time_created`

(required) Date and time the identity domain was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'INACTIVE'

`lifecycle_details`

(optional) Any additional details about the current state of the identity domain.

Allowed values are: 'DEACTIVATING', 'ACTIVATING', 'UPDATING'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_STATES_T Type

(For tenancies that support identity domains) The identity domain replication log for all identity domains for a given region.

Syntax
```

```

Fields

Field Description

`domain_id`

(required) The OCID of the identity domain.

`state`

(required) The IDCS-replicated region state.

Allowed values are: 'ENABLING_REPLICATION', 'REPLICATION_ENABLED', 'DISABLING_REPLICATION', 'REPLICATION_DISABLED', 'DELETED'

`replica_region`

(required) The replica region for the identity domain.

### DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_STATES_TBL Type

Nested table type of dbms_cloud_oci_identity_domain_replication_states_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_T Type

(For tenancies that support identity domains) Identity domain replication states.

Syntax
```

```

Fields

Field Description

`opc_water_mark`

(required) The version number indicating the value of kievTxnId, starting from which the identity domain replication events need to be returned.

`txn_seq_number`

(required) A custom value defining the order of records with the same kievTxnId.

`domain_replication_states`

(required) The identity domain's replication state.

### DBMS_CLOUD_OCI_IDENTITY_DOMAIN_SUMMARY_T Type

(For tenancies that support identity domains) As the name suggests, a `DomainSummary` object contains information about a `Domain`.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the identity domain.

`compartment_id`

(required) The OCID of the compartment containing the identity domain.

`display_name`

(required) The mutable display name of the identity domain.

`description`

(required) The identity domain description. You can have an empty description.

`url`

(required) Region-agnostic identity domain URL.

`home_region_url`

(required) Region-specific identity domain URL.

`home_region`

(required) The home region for the identity domain.

`replica_regions`

(required) The regions where replicas of the identity domain exist.

`l_type`

(required) The type of the identity domain.

Allowed values are: 'DEFAULT', 'SECONDARY'

`license_type`

(required) The license type of the identity domain.

`is_hidden_on_login`

(required) Indicates whether the identity domain is hidden on the sign-in screen or not.

`time_created`

(required) Date and time the identity domain was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state.

Allowed values are: 'CREATING', 'ACTIVE', 'DELETING', 'INACTIVE'

`lifecycle_details`

(optional) Any additional details about the current state of the identity domain.

Allowed values are: 'DEACTIVATING', 'ACTIVATING', 'UPDATING'

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_DYNAMIC_GROUP_T Type

A dynamic group defines a matching rule. Every bare metal or virtual machine instance is deployed with an instance certificate. The certificate contains metadata about the instance. This includes the instance OCID and the compartment OCID, along with a few other optional properties. When an API call is made using this instance certificate as the authenticator, the certificate can be matched to one or multiple dynamic groups. The instance can then get access to the API based on the permissions granted in policies written for the dynamic groups. This works like regular user/group membership. But in that case, the membership is a static relationship, whereas in a dynamic group, the membership of an instance certificate to a dynamic group is determined during runtime. For more information, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the group.

`compartment_id`

(required) The OCID of the tenancy containing the group.

`name`

(required) The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`description`

(required) The description you assign to the group. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`matching_rule`

(required) A rule string that defines which instance certificates will be matched. For syntax, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).

`time_created`

(required) Date and time the group was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_ENABLE_REPLICATION_TO_REGION_DETAILS_T Type

(For tenancies that support identity domains) Identity domain replication request packet.

Syntax
```

```

Fields

Field Description

`replica_region`

(optional) A region to which you want identity domain replication to occur. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names. Example: `us-phoenix-1`

### DBMS_CLOUD_OCI_IDENTITY_ENUM_TAG_DEFINITION_VALIDATOR_T Type

Used to validate the value set for a defined tag and contains the list of allowable `values`. You must specify at least one valid value in the `values` array. You can't have blank or or empty strings (`\"\"`). Duplicate values are not allowed.

Syntax
```

```

`dbms_cloud_oci_identity_enum_tag_definition_validator_t`is a subtype of the`dbms_cloud_oci_identity_base_tag_definition_validator_t`type.

Fields

Field Description

`l_values`

(optional) The list of allowed values for a definedTag value.

### DBMS_CLOUD_OCI_IDENTITY_ERROR_T Type

Syntax
```

```

Fields

Field Description

`code`

(required) A short error code that defines the error, meant for programmatic parsing. See[API Errors](https://docs.oracle.com/iaas/Content/API/References/apierrors.htm).

`message`

(required) A human-readable error string.

### DBMS_CLOUD_OCI_IDENTITY_FAULT_DOMAIN_T Type

A Fault Domain is a logical grouping of hardware and infrastructure within an Availability Domain that can become unavailable in its entirety either due to hardware failure such as Top-of-rack (TOR) switch failure or due to planned software maintenance such as security updates that reboot your instances.

Syntax
```

```

Fields

Field Description

`name`

(optional) The name of the Fault Domain.

`id`

(optional) The OCID of the Fault Domain.

`compartment_id`

(optional) The OCID of the compartment. Currently only tenancy (root) compartment can be provided.

`availability_domain`

(optional) The name of the availabilityDomain where the Fault Domain belongs.

### DBMS_CLOUD_OCI_IDENTITY_GROUP_T Type

A collection of users who all need the same type of access to a particular set of resources or compartment. If you're federating with an identity provider (IdP), you need to create mappings between the groups defined in the IdP and groups you define in the IAM service. For more information, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). Also see`IDENTITY_PROVIDER`Type and`IDP_GROUP_MAPPING`Type. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the group.

`compartment_id`

(required) The OCID of the tenancy containing the group.

`name`

(required) The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.

`description`

(required) The description you assign to the group. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`time_created`

(required) Date and time the group was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_RESOURCE_T Type

(For tenancies that support identity domains) A IAM work request resource entry.

Syntax
```

```

Fields

Field Description

`action_type`

(required) The way in which this resource is affected by the work tracked in the work request. A resource being created, updated, or deleted will remain in the IN_PROGRESS state until work is complete for that resource at which point it will transition to CREATED, UPDATED, or DELETED, respectively.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS'

`entity_type`

(required) The resource type the work request is affects.

`identifier`

(required) An OCID of the resource that the work request affects.

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_identity_iam_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_T Type

(For tenancies that support identity domains) An IAM work request object that allows users to track the status of asynchronous API requests.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) The asynchronous operation tracked by this IAM work request.

Allowed values are: 'CREATE_DOMAIN', 'REPLICATE_DOMAIN_TO_REGION', 'UPDATE_DOMAIN', 'ACTIVATE_DOMAIN', 'DEACTIVATE_DOMAIN', 'DELETE_DOMAIN', 'CHANGE_COMPARTMENT_FOR_DOMAIN', 'CHANGE_LICENSE_TYPE_FOR_DOMAIN'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(optional) The OCID of the compartment containing this IAM work request.

`resources`

(optional) The resources this work request affects.

`percent_complete`

(optional) How much progress the operation has made.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_ERROR_SUMMARY_T Type

(For tenancies that support identity domains) An error encountered while executing an operation that is tracked by a IAM work request.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

`l_timestamp`

(required) The date and time the error occurred.

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_LOG_SUMMARY_T Type

(For tenancies that support identity domains) The log entity for a IAM work request.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable error string.

`l_timestamp`

(optional) Date and time the log was written, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_SUMMARY_T Type

(For tenancies that support identity domains) The IAM work request summary. Tracks the status of asynchronous operations.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) The asynchronous operation tracked by this IAM work request.

Allowed values are: 'CREATE_DOMAIN', 'REPLICATE_DOMAIN_TO_REGION', 'UPDATE_DOMAIN', 'ACTIVATE_DOMAIN', 'DEACTIVATE_DOMAIN', 'DELETE_DOMAIN', 'CHANGE_COMPARTMENT_FOR_DOMAIN', 'CHANGE_LICENSE_TYPE_FOR_DOMAIN'

`status`

(required) The status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`compartment_id`

(optional) The OCID of the compartment containing this IAM work request.

`resources`

(optional) The resources this work request affects.

`percent_complete`

(optional) How much progress the operation has made.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_IDENTITY_PROVIDER_T Type

The resulting base object when you add an identity provider to your tenancy. A`SAML2_IDENTITY_PROVIDER`Type is a specific type of `IdentityProvider` that supports the SAML 2.0 protocol. Each `IdentityProvider` object has its own OCID. For more information, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the `IdentityProvider`.

`compartment_id`

(required) The OCID of the tenancy containing the `IdentityProvider`.

`name`

(required) The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed. This is the name federated users see when choosing which identity provider to use when signing in to the Oracle Cloud Infrastructure Console.

`description`

(required) The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable.

`product_type`

(required) The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS). Allowed values are: - `ADFS` - `IDCS` Example: `IDCS`

`time_created`

(required) Date and time the `IdentityProvider` was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The current state. After creating an `IdentityProvider`, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`protocol`

(required) The protocol used for federation. Allowed value: `SAML2`. Example: `SAML2`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_IDENTITY_PROVIDER_GROUP_SUMMARY_T Type

A group created in an identity provider that can be mapped to a group in OCI

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the `IdentityProviderGroup`.

`identity_provider_id`

(optional) The OCID of the `IdentityProvider` this group belongs to.

`display_name`

(optional) Display name of the group

`name`

(optional) Display name of the group

`external_identifier`

(optional) Identifier of the group in the identity provider

`time_created`

(optional) Date and time the `IdentityProviderGroup` was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_modified`

(optional) Date and time the `IdentityProviderGroup` was last modified, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_IDP_GROUP_MAPPING_T Type

A mapping between a single group defined by the identity provider (IdP) you're federating with and a single IAM Service`GROUP`Type in Oracle Cloud Infrastructure. For more information about group mappings and what they're for, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). A given IdP group can be mapped to zero, one, or multiple IAM Service groups, and vice versa. But each `IdPGroupMapping` object is between only a single IdP group and IAM Service group. Each `IdPGroupMapping` object has its own OCID. **Note:** Any users who are in more than 50 IdP groups cannot be authenticated to use the Oracle Cloud Infrastructure Console.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the `IdpGroupMapping`.

`idp_id`

(required) The OCID of the `IdentityProvider` this mapping belongs to.

`idp_group_name`

(required) The name of the IdP group that is mapped to the IAM Service group.

`group_id`

(required) The OCID of the IAM Service group that is mapped to the IdP group.

`compartment_id`

(required) The OCID of the tenancy containing the `IdentityProvider`.

`time_created`

(required) Date and time the mapping was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The mapping's current state. After creating a mapping object, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_IMPORT_STANDARD_TAGS_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment where the bulk create request is submitted and where the tag namespaces will be created.

`standard_tag_namespace_name`

(required) The name of standard tag namespace that will be imported in bulk

### DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_DEVICE_T Type

Users can enable multi-factor authentication (MFA) for their own user accounts. After MFA is enabled, the user is prompted for a time-based one-time password (TOTP) to authenticate before they can sign in to the Console. To enable multi-factor authentication, the user must register a mobile device with a TOTP authenticator app installed. The registration process creates the `MfaTotpDevice` object. The registration process requires interaction with the Console and cannot be completed programmatically. For more information, see[Managing Multi-Factor Authentication](https://docs.oracle.com/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the MFA TOTP device.

`seed`

(required) The seed for the MFA TOTP device (Base32 encoded).

`user_id`

(required) The OCID of the user the MFA TOTP device belongs to.

`time_created`

(required) Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this MFA TOTP device will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The MFA TOTP device's current state. After creating the MFA TOTP device, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState. Allowed values are: - 1 - SUSPENDED - 2 - DISABLED - 4 - BLOCKED - 8 - LOCKED

`is_activated`

(required) Flag to indicate if the MFA TOTP device has been activated.

### DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_DEVICE_SUMMARY_T Type

As the name suggests, a `MfaTotpDeviceSummary` object contains information about a `MfaTotpDevice`.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the MFA TOTP Device.

`user_id`

(required) The OCID of the user the MFA TOTP device belongs to.

`time_created`

(required) Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this MFA TOTP device will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The MFA TOTP device's current state.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState. Allowed values are: - 1 - SUSPENDED - 2 - DISABLED - 4 - BLOCKED - 8 - LOCKED

`is_activated`

(required) Flag to indicate if the MFA TOTP device has been activated

### DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_TOKEN_T Type

Totp token for MFA

Syntax
```

```

Fields

Field Description

`totp_token`

(optional) The Totp token for MFA.

### DBMS_CLOUD_OCI_IDENTITY_MOVE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`target_compartment_id`

(required) The[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)of the destination compartment into which to move the compartment.

### DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_T Type

A network source specifies a list of source IP addresses that are allowed to make authorization requests. Use the network source in policy statements to restrict access to only requests that come from the specified IPs. For more information, see[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the network source.

`compartment_id`

(required) The OCID of the tenancy containing the network source. The tenancy is the root compartment.

`name`

(required) The name you assign to the network source during creation. The name must be unique across the tenancy and cannot be changed.

`description`

(required) The description you assign to the network source. Does not have to be unique, and it's changeable.

`public_source_list`

(optional) A list of allowed public IPs and CIDR ranges.

`virtual_source_list`

(optional) A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

`services`

(optional) -- The services attribute has no effect and is reserved for use by Oracle. --

`time_created`

(required) Date and time the network source was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The network source object's current state. After creating a network source, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_SUMMARY_T Type

A network source specifies a list of source IP addresses that are allowed to make authorization requests. Use the network source in policy statements to restrict access to only requests that come from the specified IPs. For more information, see[Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the network source.

`compartment_id`

(required) The OCID of the tenancy (root compartment) containing the network source.

`name`

(required) The name you assign to the network source during creation. The name must be unique across the tenancy and cannot be changed.

`description`

(required) The description you assign to the network source. Does not have to be unique, and it's changeable.

`public_source_list`

(optional) A list of allowed public IP addresses and CIDR ranges.

`virtual_source_list`

(optional) A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

`services`

(optional) -- The services attribute has no effect and is reserved for use by Oracle. --

`lifecycle_state`

(required) The network source object's current state. After creating a network source, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

`time_created`

(required) Date and time the network source was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_O_AUTH2_CLIENT_CREDENTIAL_T Type

User can define Oauth clients in IAM, then use it to generate a token to grant access to app resources.

Syntax
```

```

Fields

Field Description

`scopes`

(optional) Allowed scopes for the given oauth credential.

`password`

(optional) Returned during create and update with password reset requests.

`user_id`

(optional) The OCID of the user the Oauth credential belongs to.

`expires_on`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`id`

(optional) The OCID of the Oauth credential.

`compartment_id`

(optional) The OCID of the compartment containing the Oauth credential.

`name`

(optional) The name of the Oauth credential.

`description`

(optional) The description of the Oauth credential.

`lifecycle_state`

(optional) The credential's current state. After creating a Oauth credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`time_created`

(optional) Date and time the `OAuth2ClientCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_O_AUTH2_CLIENT_CREDENTIAL_SUMMARY_T Type

User can define Oauth clients in IAM, then use it to generate a token to grant access to app resources.

Syntax
```

```

Fields

Field Description

`scopes`

(optional) Allowed scopes for the given oauth credential.

`user_id`

(optional) The OCID of the user the Oauth credential belongs to.

`expires_on`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`id`

(optional) The OCID of the Oauth credential.

`compartment_id`

(optional) The OCID of the compartment containing the Oauth credential.

`name`

(optional) The name of the Oauth credential.

`description`

(optional) The description of the Oauth credential.

`lifecycle_state`

(optional) The credential's current state. After creating a Oauth credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`time_created`

(optional) Date and time the `OAuth2ClientCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_POLICY_T Type

A document that specifies the type of access a group has to the resources in a compartment. If you're new to policies, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). The word \"policy\" is used by people in different ways: * An individual statement written in the policy language * A collection of statements in a single, named \"policy\" document (which has an Oracle Cloud ID (OCID) assigned to it) * The overall body of policies your organization uses to control access to resources To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the policy.

`compartment_id`

(required) The OCID of the compartment containing the policy (either the tenancy or another compartment).

`name`

(required) The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed.

`statements`

(required) An array of one or more policy statements written in the policy language.

`description`

(required) The description you assign to the policy. Does not have to be unique, and it's changeable.

`time_created`

(required) Date and time the policy was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

`version_date`

(optional) The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_REGION_T Type

A localized geographic area, such as Phoenix, AZ. Oracle Cloud Infrastructure is hosted in regions and Availability Domains. A region is composed of several Availability Domains. An Availability Domain is one or more data centers located within a region. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm).

Syntax
```

```

Fields

Field Description

`key`

(optional) The key of the region. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported 3-letter region codes. Example: `PHX`

`name`

(optional) The name of the region. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names. Example: `us-phoenix-1`

### DBMS_CLOUD_OCI_IDENTITY_REGION_SUBSCRIPTION_T Type

An object that represents your tenancy's access to a particular region (i.e., a subscription), the status of that access, and whether that region is the home region. For more information, see[Managing Regions](https://docs.oracle.com/iaas/Content/Identity/regions/managingregions.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm).

Syntax
```

```

Fields

Field Description

`region_key`

(required) The region's key. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported 3-letter region codes. Example: `PHX`

`region_name`

(required) The region's name. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm)for the full list of supported region names. Example: `us-phoenix-1`

`status`

(required) The region subscription status.

Allowed values are: 'READY', 'IN_PROGRESS'

`is_home_region`

(required) Indicates if the region is the home region or not.

### DBMS_CLOUD_OCI_IDENTITY_REMOVE_LOCK_DETAILS_T Type

Request payload to remove lock to the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

### DBMS_CLOUD_OCI_IDENTITY_RESOURCE_LOCK_T Type

Resource locks are used to prevent certain APIs from being called for the resource. A full lock prevents both updating the resource and deleting the resource. A delete lock prevents deleting the resource.

Syntax
```

```

Fields

Field Description

`l_type`

(required) Type of the lock.

Allowed values are: 'FULL', 'DELETE'

`related_resource_id`

(optional) The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.

`message`

(optional) A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.

`time_created`

(optional) When the lock was created.

`is_active`

(optional) Indicates if the lock is active or not. For example, if there are mutliple FULL locks, the first-created FULL lock will be effective.

### DBMS_CLOUD_OCI_IDENTITY_SAML2_IDENTITY_PROVIDER_T Type

A special type of`IDENTITY_PROVIDER`Type that supports the SAML 2.0 protocol. For more information, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm).

Syntax
```

```

`dbms_cloud_oci_identity_saml2_identity_provider_t`is a subtype of the`dbms_cloud_oci_identity_identity_provider_t`type.

Fields

Field Description

`metadata_url`

(required) The URL for retrieving the identity provider's metadata, which contains information required for federating.

`metadata`

(optional) The XML that contains the information required for federating Identity with SAML2 Identity Provider.

`signing_certificate`

(required) The identity provider's signing certificate used by the IAM Service to validate the SAML2 token.

`redirect_url`

(required) The URL to redirect federated users to for authentication with the identity provider.

`freeform_attributes`

(optional) Extra name value pairs associated with this identity provider. Example: `{\"clientId\": \"app_sf3kdjf3\"}`

### DBMS_CLOUD_OCI_IDENTITY_SCIM_CLIENT_CREDENTIALS_T Type

The OAuth2 client credentials.

Syntax
```

```

Fields

Field Description

`client_id`

(optional) The client identifier.

`client_secret`

(optional) The client secret.

### DBMS_CLOUD_OCI_IDENTITY_SMTP_CREDENTIAL_T Type

Simple Mail Transfer Protocol (SMTP) credentials are needed to send email through Email Delivery. The SMTP credentials are used for SMTP authentication with the service. The credentials never expire. A user can have up to 2 SMTP credentials at a time. **Note:** The credential set is always an Oracle-generated SMTP user name and password pair; you cannot designate the SMTP user name or the SMTP password. For more information, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm#SMTP).

Syntax
```

```

Fields

Field Description

`username`

(optional) The SMTP user name.

`password`

(optional) The SMTP password.

`id`

(optional) The OCID of the SMTP credential.

`user_id`

(optional) The OCID of the user the SMTP credential belongs to.

`description`

(optional) The description you assign to the SMTP credential. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`time_created`

(optional) Date and time the `SmtpCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The credential's current state. After creating a SMTP credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_SMTP_CREDENTIAL_SUMMARY_T Type

As the name suggests, an `SmtpCredentialSummary` object contains information about an `SmtpCredential`. The SMTP credential is used for SMTP authentication with the[Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).

Syntax
```

```

Fields

Field Description

`username`

(optional) The SMTP user name.

`id`

(optional) The OCID of the SMTP credential.

`user_id`

(optional) The OCID of the user the SMTP credential belongs to.

`description`

(optional) The description you assign to the SMTP credential. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`time_created`

(optional) Date and time the `SmtpCredential` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_expires`

(optional) Date and time when this credential will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The credential's current state. After creating a SMTP credential, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_DEFINITION_TEMPLATE_T Type

The template of the tag definition. This object includes necessary details to create the provided standard tag definition.

Syntax
```

```

Fields

Field Description

`description`

(required) The default description of the tag namespace that users can use to create the tag definition

`tag_definition_name`

(required) The name of this standard tag definition

`l_type`

(required) The type of tag definition. Enum or string.

Allowed values are: 'ENUM', 'STRING'

`possible_values`

(optional) List of possible values. An optional parameter that will be present if the type of definition is enum.

`is_cost_tracking`

(required) Is the tag a cost tracking tag. Default will be false as cost tracking tags have been deprecated

`enum_mutability`

(optional) The mutability of the possible values list for enum tags. This will default to IMMUTABLE for string value tags

Allowed values are: 'IMMUTABLE', 'MUTABLE', 'APPENDABLE'

### DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_DEFINITION_TEMPLATE_TBL Type

Nested table type of dbms_cloud_oci_identity_standard_tag_definition_template_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_NAMESPACE_TEMPLATE_T Type

The template of the standard tag namespace. This object includes necessary details to create the provided standard tag namespace.

Syntax
```

```

Fields

Field Description

`description`

(required) The default description of the tag namespace that users can use to create the tag namespace

`standard_tag_namespace_name`

(required) The reserved name of this standard tag namespace

`tag_definition_templates`

(required) The template of the tag definition. This object includes necessary details to create the provided standard tag definition.

`status`

(required) The status of the standard tag namespace

### DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_NAMESPACE_TEMPLATE_SUMMARY_T Type

The template of the standard tag namespace. This object includes necessary details to create the provided standard tag namespace.

Syntax
```

```

Fields

Field Description

`description`

(required) The default description of the tag namespace that users can use to create the tag namespace

`standard_tag_namespace_name`

(required) The reserved name of this standard tag namespace

`status`

(required) The status of the standard tag namespace

### DBMS_CLOUD_OCI_IDENTITY_SWIFT_PASSWORD_T Type

**Deprecated. Use`AUTH_TOKEN`Type instead.** Swift is the OpenStack object storage service. A `SwiftPassword` is an Oracle-provided password for using a Swift client with the Object Storage Service. This password is associated with the user's Console login. Swift passwords never expire. A user can have up to two Swift passwords at a time. **Note:** The password is always an Oracle-generated string; you can't change it to a string of your choice. For more information, see[Managing User Credentials](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

Syntax
```

```

Fields

Field Description

`password`

(optional) The Swift password. The value is available only in the response for `CreateSwiftPassword`, and not for `ListSwiftPasswords` or `UpdateSwiftPassword`.

`id`

(optional) The OCID of the Swift password.

`user_id`

(optional) The OCID of the user the password belongs to.

`description`

(optional) The description you assign to the Swift password. Does not have to be unique, and it's changeable.

`time_created`

(optional) Date and time the `SwiftPassword` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`expires_on`

(optional) Date and time when this password will expire, in the format defined by RFC3339. Null if it never expires. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The password's current state. After creating a password, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_TAG_T Type

A tag definition that belongs to a specific tag namespace. \"Defined tags\" must be set up in your tenancy before you can apply them to resources. For more information, see[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`compartment_id`

(required) The OCID of the compartment that contains the tag definition.

`tag_namespace_id`

(required) The OCID of the namespace that contains the tag definition.

`tag_namespace_name`

(required) The name of the tag namespace that contains the tag definition.

`id`

(required) The OCID of the tag definition.

`name`

(required) The name assigned to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.

`description`

(required) The description you assign to the tag.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_retired`

(required) Indicates whether the tag is retired. See[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`lifecycle_state`

(optional) The tag's current state. After creating a tag, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tag, make sure its `lifecycleState` is INACTIVE before using it. If you delete a tag, you cannot delete another tag until the deleted tag's `lifecycleState` changes from DELETING to DELETED.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) Date and time the tag was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`is_cost_tracking`

(optional) Indicates whether the tag is enabled for cost tracking.

`validator`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_RESOURCE_LOCK_TBL Type

Nested table type of dbms_cloud_oci_identity_resource_lock_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_TAG_DEFAULT_T Type

Tag defaults let you specify a default tag (tagnamespace.tag=\"value\") to apply to all resource types in a specified compartment. The tag default is applied at the time the resource is created. Resources that exist in the compartment before you create the tag default are not tagged. The `TagDefault` object specifies the tag and compartment details. Tag defaults are inherited by child compartments. This means that if you set a tag default on the root compartment for a tenancy, all resources that are created in the tenancy are tagged. For more information about using tag defaults, see[Managing Tag Defaults](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagdefaults.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the tag default.

`compartment_id`

(required) The OCID of the compartment. The tag default applies to all new resources that get created in the compartment. Resources that existed before the tag default was created are not tagged.

`tag_namespace_id`

(required) The OCID of the tag namespace that contains the tag definition.

`tag_definition_id`

(required) The OCID of the tag definition. The tag default will always assign a default value for this tag definition.

`tag_definition_name`

(required) The name used in the tag definition. This field is informational in the context of the tag default.

`value`

(required) The default value for the tag definition. This will be applied to all resources created in the compartment.

`time_created`

(required) Date and time the `TagDefault` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.

Allowed values are: 'ACTIVE'

`is_required`

(required) If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. Example: `false`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_TAG_DEFAULT_SUMMARY_T Type

Summary information for the specified tag default.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the tag default.

`compartment_id`

(required) The OCID of the compartment. The tag default will apply to all new resources that are created in the compartment.

`tag_namespace_id`

(required) The OCID of the tag namespace that contains the tag definition.

`tag_definition_id`

(required) The OCID of the tag definition. The tag default will always assign a default value for this tag definition.

`tag_definition_name`

(required) The name used in the tag definition. This field is informational in the context of the tag default.

`value`

(required) The default value for the tag definition. This will be applied to all new resources created in the compartment.

`time_created`

(required) Date and time the `TagDefault` object was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The tag default's current state. After creating a `TagDefault`, make sure its `lifecycleState` is ACTIVE before using it.

Allowed values are: 'ACTIVE'

`is_required`

(required) If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. Example: `false`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_TAG_NAMESPACE_T Type

A managed container for defined tags. A tag namespace is unique in a tenancy. For more information, see[Managing Tags and Tag Namespaces](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the tag namespace.

`compartment_id`

(required) The OCID of the compartment that contains the tag namespace.

`name`

(required) The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.

`description`

(required) The description you assign to the tag namespace.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_retired`

(required) Whether the tag namespace is retired. See[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`lifecycle_state`

(optional) The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.

Allowed values are: 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`time_created`

(required) Date and time the tagNamespace was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_TAG_NAMESPACE_SUMMARY_T Type

A container for defined tags.

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the tag namespace.

`compartment_id`

(optional) The OCID of the compartment that contains the tag namespace.

`name`

(optional) The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.

`description`

(optional) The description you assign to the tag namespace.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_retired`

(optional) Whether the tag namespace is retired. For more information, see[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`lifecycle_state`

(optional) The tagnamespace's current state. After creating a tagnamespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tagnamespace, make sure its `lifecycleState` is INACTIVE before using it.

`time_created`

(optional) Date and time the tag namespace was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`locks`

(optional) Locks associated with this resource.

### DBMS_CLOUD_OCI_IDENTITY_TAG_SUMMARY_T Type

A tag definition that belongs to a specific tag namespace.

Syntax
```

```

Fields

Field Description

`compartment_id`

(optional) The OCID of the compartment that contains the tag definition.

`id`

(optional) The OCID of the tag definition.

`name`

(optional) The name assigned to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.

`description`

(optional) The description you assign to the tag.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_retired`

(optional) Whether the tag is retired. See[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`lifecycle_state`

(optional) The tag's current state. After creating a tag, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tag, make sure its `lifecycleState` is INACTIVE before using it. If you delete a tag, you cannot delete another tag until the deleted tag's `lifecycleState` changes from DELETING to DELETED.

`time_created`

(optional) Date and time the tag was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`is_cost_tracking`

(optional) Indicates whether the tag is enabled for cost tracking.

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_RESOURCE_T Type

The resource entity.

Syntax
```

```

Fields

Field Description

`identifier`

(required) The resource identifier the work request affects.

`entity_type`

(required) The resource type the work request is affects.

`action_type`

(required) The way in which this resource was affected by the work tracked by the work request.

Allowed values are: 'CREATED', 'UPDATED', 'DELETED', 'RELATED', 'IN_PROGRESS', 'FAILED'

`entity_uri`

(optional) The URI path that the user can do a GET on to access the resource metadata.

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_RESOURCE_TBL Type

Nested table type of dbms_cloud_oci_identity_work_request_resource_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_T Type

The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) An enum-like description of the type of work the work request is doing.

Allowed values are: 'DELETE_TAG_DEFINITION', 'DELETE_NON_EMPTY_TAG_NAMESPACE', 'BULK_DELETE_TAG_DEFINITION', 'BULK_EDIT_OF_TAGS', 'IMPORT_STANDARD_TAGS'

`compartment_id`

(optional) The OCID of the compartment that contains the work request.

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'PARTIALLY_SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(optional) The resources this work request affects.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`percent_complete`

(optional) How much progress the operation has made.

### DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_ERROR_SUMMARY_T Type

The error entity.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

`l_timestamp`

(optional) Date and time the error happened, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_LOG_SUMMARY_T Type

The log entity.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable error string.

`l_timestamp`

(optional) Date and time the log was written, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_SUMMARY_T Type

The work request summary. Tracks the status of the asynchronous operation.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) An enum-like description of the type of work the work request is doing.

Allowed values are: 'DELETE_TAG_DEFINITION', 'DELETE_NON_EMPTY_TAG_NAMESPACE', 'BULK_DELETE_TAG_DEFINITION', 'BULK_EDIT_OF_TAGS', 'IMPORT_STANDARD_TAGS'

`compartment_id`

(optional) The OCID of the compartment that contains the work request.

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'PARTIALLY_SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(optional) The resources this work request affects.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`percent_complete`

(optional) How much progress the operation has made.

### DBMS_CLOUD_OCI_IDENTITY_TENANCY_T Type

The root compartment that contains all of your organization's compartments and other Oracle Cloud Infrastructure cloud resources. When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for your company, which is a secure and isolated partition where you can create, organize, and administer your cloud resources. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm).

Syntax
```

```

Fields

Field Description

`id`

(optional) The OCID of the tenancy.

`name`

(optional) The name of the tenancy.

`description`

(optional) The description of the tenancy.

`home_region_key`

(optional) The region key for the tenancy's home region. For the full list of supported regions, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Example: `PHX`

`upi_idcs_compatibility_layer_endpoint`

(optional) Url which refers to the UPI IDCS compatibility layer endpoint configured for this Tenant's home region.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UI_PASSWORD_T Type

A text password that enables a user to sign in to the Console, the user interface for interacting with Oracle Cloud Infrastructure. For more information about user credentials, see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm).

Syntax
```

```

Fields

Field Description

`password`

(optional) The user's password for the Console.

`user_id`

(optional) The OCID of the user.

`time_created`

(optional) Date and time the password was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The password's current state. After creating a password, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_UI_PASSWORD_INFORMATION_T Type

Information about the UIPassword, which is a text password that enables a user to sign in to the Console, the user interface for interacting with Oracle Cloud Infrastructure. For more information about user credentials, see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/Concepts/usercredentials.htm).

Syntax
```

```

Fields

Field Description

`user_id`

(optional) The OCID of the user.

`time_created`

(optional) Date and time the password was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(optional) The password's current state. After creating a password, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_AUTH_TOKEN_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the auth token. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_AUTHENTICATION_POLICY_DETAILS_T Type

Update request for authentication policy, describes set of validation rules and their parameters to be updated.

Syntax
```

```

Fields

Field Description

`password_policy`

(optional)

`network_policy`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_COMPARTMENT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the compartment. Does not have to be unique, and it's changeable.

`name`

(optional) The new name you assign to the compartment. The name must be unique across all compartments in the parent compartment. Avoid entering confidential information.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_CUSTOMER_SECRET_KEY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`display_name`

(optional) The description you assign to the secret key. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_DOMAIN_DETAILS_T Type

(For tenancies that support identity domains) Update identity domain details.

Syntax
```

```

Fields

Field Description

`description`

(optional) The identity domain description. You can have an empty description.

`display_name`

(optional) The mutable display name of the identity domain.

`is_hidden_on_login`

(optional) Indicates whether the identity domain is hidden on the sign-in screen or not.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_DYNAMIC_GROUP_DETAILS_T Type

Properties for updating a dynamic group.

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the dynamic group. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`matching_rule`

(optional) The matching rule to dynamically match an instance certificate to this dynamic group. For rule syntax, see[Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_GROUP_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the group. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_IDENTITY_PROVIDER_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`protocol`

(required) The protocol used for federation. Example: `SAML2`

Allowed values are: 'SAML2'

`description`

(optional) The description you assign to the `IdentityProvider`. Does not have to be unique, and it's changeable.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_IDP_GROUP_MAPPING_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`idp_group_name`

(optional) The idp group name.

`group_id`

(optional) The OCID of the group.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_NETWORK_SOURCE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the network source. Does not have to be unique, and it's changeable.

`public_source_list`

(optional) A list of allowed public IP addresses and CIDR ranges.

`virtual_source_list`

(optional) A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

`services`

(optional) -- The services attribute has no effect and is reserved for use by Oracle. --

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_O_AUTH2_CLIENT_CREDENTIAL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(required) Description of the oauth credential to help user differentiate them.

`scopes`

(required) Allowed scopes for the given oauth credential.

`is_reset_password`

(optional) Indicate if the password to be reset or not in the update.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_POLICY_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the policy. Does not have to be unique, and it's changeable.

`statements`

(optional) An array of policy statements written in the policy language. See[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).

`version_date`

(optional) The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_SAML2_IDENTITY_PROVIDER_DETAILS_T Type

Syntax
```

```

`dbms_cloud_oci_identity_update_saml2_identity_provider_details_t`is a subtype of the`dbms_cloud_oci_identity_update_identity_provider_details_t`type.

Fields

Field Description

`metadata_url`

(optional) The URL for retrieving the identity provider's metadata, which contains information required for federating.

`metadata`

(optional) The XML that contains the information required for federating.

`freeform_attributes`

(optional) Extra name value pairs associated with this identity provider. Example: `{\"clientId\": \"app_sf3kdjf3\"}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_SMTP_CREDENTIAL_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the SMTP credential. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_STATE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`blocked`

(optional) Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_SWIFT_PASSWORD_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the Swift password. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_DEFAULT_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`value`

(required) The default value for the tag definition. This will be applied to all resources created in the Compartment.

`is_required`

(optional) If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked. * If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. Example: `false`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the tag during creation.

`is_retired`

(optional) Whether the tag is retired. See[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`is_cost_tracking`

(optional) Indicates whether the tag is enabled for cost tracking.

`validator`

(optional)

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_NAMESPACE_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the tag namespace.

`is_retired`

(optional) Whether the tag namespace is retired. See[Retiring Key Definitions and Namespace Definitions](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_USER_CAPABILITIES_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`can_use_console_password`

(optional) Indicates if the user can log in to the console.

`can_use_api_keys`

(optional) Indicates if the user can use API keys.

`can_use_auth_tokens`

(optional) Indicates if the user can use SWIFT passwords / auth tokens.

`can_use_smtp_credentials`

(optional) Indicates if the user can use SMTP passwords.

`can_use_db_credentials`

(optional) Indicates if the user can use DB passwords.

`can_use_customer_secret_keys`

(optional) Indicates if the user can use SigV4 symmetric keys.

`can_use_o_auth2_client_credentials`

(optional) Indicates if the user can use OAuth2 credentials and tokens.

### DBMS_CLOUD_OCI_IDENTITY_UPDATE_USER_DETAILS_T Type

Syntax
```

```

Fields

Field Description

`description`

(optional) The description you assign to the user. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`email`

(optional) The email you assign to the user during creation. The email must be unique across all users in the tenancy. (For tenancies that support identity domains) You must provide an email for each user.

`db_user_name`

(optional) DB username of the DB credential. Has to be unique across the tenancy.

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

### DBMS_CLOUD_OCI_IDENTITY_USER_CAPABILITIES_T Type

Properties indicating how the user is allowed to authenticate.

Syntax
```

```

Fields

Field Description

`can_use_console_password`

(optional) Indicates if the user can log in to the console.

`can_use_api_keys`

(optional) Indicates if the user can use API keys.

`can_use_auth_tokens`

(optional) Indicates if the user can use SWIFT passwords / auth tokens.

`can_use_smtp_credentials`

(optional) Indicates if the user can use SMTP passwords.

`can_use_db_credentials`

(optional) Indicates if the user can use DB passwords.

`can_use_customer_secret_keys`

(optional) Indicates if the user can use SigV4 symmetric keys.

`can_use_o_auth2_client_credentials`

(optional) Indicates if the user can use OAuth2 credentials and tokens.

### DBMS_CLOUD_OCI_IDENTITY_USER_T Type

An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure resources. Users might need to launch instances, manage remote disks, work with your cloud network, etc. Users have one or more IAM Service credentials (`API_KEY`Type,`UI_PASSWORD`Type,`SWIFT_PASSWORD`Type and`AUTH_TOKEN`Type). For more information, see[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm)). End users of your application are not typically IAM Service users, but for tenancies that have identity domains, they might be. These users are created directly within the Oracle Cloud Infrastructure system, via the IAM service. They are different from *federated users*, who authenticate themselves to the Oracle Cloud Infrastructure Console via an identity provider. For more information, see[Identity Providers and Federation](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm). To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see[Get Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm). **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the user.

`compartment_id`

(required) The OCID of the tenancy containing the user.

`name`

(required) The name you assign to the user during creation. This is the user's login for the Console. The name must be unique across all users in the tenancy and cannot be changed.

`description`

(required) The description you assign to the user. Does not have to be unique, and it's changeable. (For tenancies that support identity domains) You can have an empty description.

`email`

(optional) The email address you assign to the user. The email address must be unique across all users in the tenancy. (For tenancies that support identity domains) The email address is required unless the requirement is disabled at the tenancy level.

`email_verified`

(optional) Whether the email address has been validated.

`db_user_name`

(optional) DB username of the DB credential. Has to be unique across the tenancy.

`identity_provider_id`

(optional) The OCID of the `IdentityProvider` this user belongs to.

`external_identifier`

(optional) Identifier of the user in the identity provider

`time_created`

(required) Date and time the user was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user is inactive: - bit 0: SUSPENDED (reserved for future use) - bit 1: DISABLED (reserved for future use) - bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)

`freeform_tags`

(optional) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Department\": \"Finance\"}`

`defined_tags`

(optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

`capabilities`

(optional)

`is_mfa_activated`

(required) Flag indicates if MFA has been activated for the user.

`last_successful_login_time`

(optional) The date and time of when the user most recently logged in the format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`). If there is no login history, this field is null. For illustrative purposes, suppose we have a user who has logged in at July 1st, 2020 at 1200 PST and logged out 30 minutes later. They then login again on July 2nd, 2020 at 1500 PST. Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`. Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.

`previous_successful_login_time`

(optional) The date and time of when the user most recently logged in the format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`). If there is no login history, this field is null. For illustrative purposes, suppose we have a user who has logged in at July 1st, 2020 at 1200 PST and logged out 30 minutes later. They then login again on July 2nd, 2020 at 1500 PST. Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`. Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.

### DBMS_CLOUD_OCI_IDENTITY_USER_GROUP_MEMBERSHIP_T Type

An object that represents the membership of a user in a group. When you add a user to a group, the result is a `UserGroupMembership` with its own OCID. To remove a user from a group, you delete the `UserGroupMembership` object.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the membership.

`compartment_id`

(required) The OCID of the tenancy containing the user, group, and membership object.

`group_id`

(required) The OCID of the group.

`user_id`

(required) The OCID of the user.

`time_created`

(required) Date and time the membership was created, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`lifecycle_state`

(required) The membership's current state. After creating a membership object, make sure its `lifecycleState` changes from CREATING to ACTIVE before using it.

Allowed values are: 'CREATING', 'ACTIVE', 'INACTIVE', 'DELETING', 'DELETED'

`inactive_status`

(optional) The detailed status of INACTIVE lifecycleState.

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_ERROR_T Type

The error entity.

Syntax
```

```

Fields

Field Description

`code`

(required) A machine-usable code for the error that occured.

`message`

(required) A human-readable error string.

`l_timestamp`

(optional) Date and time the error happened, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_LOG_ENTRY_T Type

The log entity.

Syntax
```

```

Fields

Field Description

`message`

(required) A human-readable error string.

`l_timestamp`

(optional) Date and time the log was written, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_ERROR_TBL Type

Nested table type of dbms_cloud_oci_identity_work_request_error_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_LOG_ENTRY_TBL Type

Nested table type of dbms_cloud_oci_identity_work_request_log_entry_t.

Syntax
```

```

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_T Type

The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) An enum-like description of the type of work the work request is doing.

Allowed values are: 'DELETE_COMPARTMENT', 'DELETE_TAG_DEFINITION'

`compartment_id`

(optional) The OCID of the compartment that contains the work request.

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(optional) The resources this work request affects.

`errors`

(optional) The errors for work request.

`logs`

(optional) The logs for work request.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`percent_complete`

(optional) How much progress the operation has made.

### DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_SUMMARY_T Type

The work request summary. Tracks the status of the asynchronous operation.

Syntax
```

```

Fields

Field Description

`id`

(required) The OCID of the work request.

`operation_type`

(required) An enum-like description of the type of work the work request is doing.

Allowed values are: 'DELETE_COMPARTMENT', 'DELETE_TAG_DEFINITION'

`compartment_id`

(optional) The OCID of the compartment that contains the work request.

`status`

(required) The current status of the work request.

Allowed values are: 'ACCEPTED', 'IN_PROGRESS', 'FAILED', 'SUCCEEDED', 'CANCELING', 'CANCELED'

`resources`

(optional) The resources this work request affects.

`errors`

(optional) The errors for work request.

`time_accepted`

(optional) Date and time the work was accepted, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_started`

(optional) Date and time the work started, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`time_finished`

(optional) Date and time the work completed, in the format defined by RFC3339. Example: `2016-08-25T21:10:29.600Z`

`percent_complete`

(optional) How much progress the operation has made.

- [Identity Common Types](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-CEB4FE6C-50BB-4BAF-8B3F-B757EE48D2F8)
- [DBMS_CLOUD_OCI_IDENTITY_VARCHAR2_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-77B0A778-9287-4283-AD65-F0DAD559251C)
- [DBMS_CLOUD_OCI_IDENTITY_ADD_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-3EFBEA36-22F0-46D4-B7A7-42B7C36DB89A)
- [DBMS_CLOUD_OCI_IDENTITY_ADD_USER_TO_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-AF6324A4-7513-4FDC-8262-C8363C15F860)
- [DBMS_CLOUD_OCI_IDENTITY_ALLOWED_DOMAIN_LICENSE_TYPE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2FCC8370-73DD-44C0-906F-4EE55645F610)
- [DBMS_CLOUD_OCI_IDENTITY_API_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-8AFA56B8-2E09-46F0-BB9C-273C35BE3378)
- [DBMS_CLOUD_OCI_IDENTITY_AUTH_TOKEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-087C873B-75C3-4010-BB29-D21E0CE80E8F)
- [DBMS_CLOUD_OCI_IDENTITY_PASSWORD_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-BF631898-442E-40F8-9E4D-A62BE2BAD0C4)
- [DBMS_CLOUD_OCI_IDENTITY_NETWORK_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-88667C23-0655-4518-84DC-266BC5FB4B4A)
- [DBMS_CLOUD_OCI_IDENTITY_AUTHENTICATION_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5818E542-60BD-46C7-8CA3-EF24AE30C4F8)
- [DBMS_CLOUD_OCI_IDENTITY_AVAILABILITY_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E5F8EB82-BA7F-4DB8-BA3C-ED98F5B62B2D)
- [DBMS_CLOUD_OCI_IDENTITY_BASE_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-57CA70D8-ECC8-4602-B0FE-FCD2C25CAB67)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-331E3752-6054-418B-B502-75F6D575889B)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2F14A363-A312-4EDC-A0F2-095EC3E1F0BF)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4A127A88-895F-4DC7-9D17-120BCBFEC262)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D7BCE83C-FD6B-41DB-A9A7-0827227A372E)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_ACTION_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-0B8E5493-4DBB-46F8-A53C-18537675CFD1)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_DELETE_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7DC3F9AE-4976-4F95-94B1-97081C105C05)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_DELETE_TAGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-23506BC6-D849-49A1-A159-27D0F36D9A80)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_OPERATION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E99B1D92-81C3-400D-8D24-27DD4509602D)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-44EFA4B8-A449-456A-9CAC-14179ADA9C45)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-90C65436-4810-4C7E-9906-3E87E68A5BAA)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_OPERATION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2A185524-FA66-4D7E-9559-6D0D32B2A070)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-F6655A38-C9E4-4803-8479-8ABC579A484A)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-DD0A898E-322D-4811-AE43-EC47D0304739)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5E656D98-395B-43BC-A95A-8E3B4857C042)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_EDIT_TAGS_RESOURCE_TYPE_COLLECTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-203778C0-4166-4245-BE70-7E0F477D56C8)
- [DBMS_CLOUD_OCI_IDENTITY_BULK_MOVE_RESOURCES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-FA243232-6211-410A-B154-E08ADC843E69)
- [DBMS_CLOUD_OCI_IDENTITY_CHANGE_DOMAIN_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-B2369503-0CC5-4469-B1D0-1EBC1005566E)
- [DBMS_CLOUD_OCI_IDENTITY_CHANGE_DOMAIN_LICENSE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-19BEFB74-BDA4-48F1-A2B8-89C991E290EF)
- [DBMS_CLOUD_OCI_IDENTITY_CHANGE_TAG_NAMESPACE_COMPARTMENT_DETAIL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-CA99F089-43EA-4585-8B49-806582FC0795)
- [DBMS_CLOUD_OCI_IDENTITY_CHANGE_TAS_DOMAIN_LICENSE_TYPE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C4D44F11-6EF9-4173-AD72-3B058073D865)
- [DBMS_CLOUD_OCI_IDENTITY_COMPARTMENT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-46F1FEA9-4842-467E-AF0E-E7024DDC44DA)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_API_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-9324D92A-3747-4991-87EF-66CA3E41ABD1)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_AUTH_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D0094964-29D9-4901-AFC5-6B78D5FFF2F7)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-200972C3-CDD1-4D06-B6AF-8E8BEE25E4C4)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_CUSTOMER_SECRET_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5AE5AEE6-39F9-4861-98E3-A81004DC0860)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_DB_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-BD14BDB1-257C-47DC-88A8-FAD94E30243D)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C4FCA2FA-6E38-4875-B12E-4CD37DF3AABD)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_DYNAMIC_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-EC38936D-915D-4836-923A-508166677B11)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-0308930A-5CB1-4067-8493-E986E747B14C)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_IDENTITY_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7145B3C7-5016-4B8E-9A7E-39B17A27F5F1)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_IDP_GROUP_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-30A728E2-4803-423D-A237-1AAABE36DDBE)
- [DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_VIRTUAL_SOURCE_LIST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-EAE3D86D-D7D4-4BD7-8C8D-956A0AF30824)
- [DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_VIRTUAL_SOURCE_LIST_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-950E38E9-5213-49C1-BB5C-B1ADBFDA711B)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_NETWORK_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2E2D4297-E27B-4205-8FD2-A4E49D23AF04)
- [DBMS_CLOUD_OCI_IDENTITY_FULLY_QUALIFIED_SCOPE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D66C2EF3-246C-4BEF-86C2-8C66033F94CB)
- [DBMS_CLOUD_OCI_IDENTITY_FULLY_QUALIFIED_SCOPE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-74092EB6-E7FF-47A9-B8AB-1970F0B158EC)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_O_AUTH2_CLIENT_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-279DCB47-DF7F-4C41-A830-3BC3B04A20CB)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-08450D69-A3A5-42D5-A5DD-B9192FEA5DA9)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_REGION_SUBSCRIPTION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C2F7A7E8-6622-4547-9D9D-0D36CFCD5A5F)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_SAML2_IDENTITY_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-577509F5-0DB7-4540-8A92-D22DE6383693)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_SMTP_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-705190F4-464E-43F1-9F16-01555ADDE2F0)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_SWIFT_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-91687AD2-8BA6-4F28-99A2-74E5863016A9)
- [DBMS_CLOUD_OCI_IDENTITY_ADD_LOCK_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-F22D6926-7258-4EC2-944B-45E7629B5864)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_DEFAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-1955638B-8E26-450F-B784-437D15E0F9BE)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-9F33E1FB-40B1-4E96-A22E-77B533AE7173)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_TAG_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-36479A2B-487E-499F-A6F7-D26C6DADCF86)
- [DBMS_CLOUD_OCI_IDENTITY_CREATE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-A4BBFB61-554D-4793-9752-8FAC2DDDE1A9)
- [DBMS_CLOUD_OCI_IDENTITY_CUSTOMER_SECRET_KEY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-53C0C71E-CA6F-4154-A929-6DA2D929797B)
- [DBMS_CLOUD_OCI_IDENTITY_CUSTOMER_SECRET_KEY_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-09C46925-959D-4CC3-B9C2-631AEF077DEF)
- [DBMS_CLOUD_OCI_IDENTITY_DB_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-119AECD3-F4A4-40E8-959D-1E5E594F87B9)
- [DBMS_CLOUD_OCI_IDENTITY_DB_CREDENTIAL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-93A82A1F-9968-4DA1-9DD0-B21A53FDFD6A)
- [DBMS_CLOUD_OCI_IDENTITY_DEFAULT_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2327484B-BCCD-4413-8106-12202E98DCFE)
- [DBMS_CLOUD_OCI_IDENTITY_REPLICATED_REGION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-A1857290-D0A8-4108-8560-76C201398F08)
- [DBMS_CLOUD_OCI_IDENTITY_REPLICATED_REGION_DETAILS_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7365798F-E113-4EDC-95AE-D630EFF75B5B)
- [DBMS_CLOUD_OCI_IDENTITY_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-79F7C337-52A7-4A71-9DDB-BFC3B73F50C4)
- [DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_STATES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-AD76FAFA-9402-4048-BDAC-EB7A84B765BB)
- [DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_STATES_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-ABDC44D7-E933-4E2D-8620-269901131478)
- [DBMS_CLOUD_OCI_IDENTITY_DOMAIN_REPLICATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-55A00894-F310-4F09-ACF8-9F3E0F25951A)
- [DBMS_CLOUD_OCI_IDENTITY_DOMAIN_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5AAB3F7F-1BF8-4B26-A99A-0987511B778B)
- [DBMS_CLOUD_OCI_IDENTITY_DYNAMIC_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-305E57E3-040E-4C04-86D1-EFC8DF67739C)
- [DBMS_CLOUD_OCI_IDENTITY_ENABLE_REPLICATION_TO_REGION_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E7F8CFA0-7917-470A-B11B-621496644390)
- [DBMS_CLOUD_OCI_IDENTITY_ENUM_TAG_DEFINITION_VALIDATOR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-155F4DEC-2E32-45EA-B08E-A00AB9A49158)
- [DBMS_CLOUD_OCI_IDENTITY_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-A4E26511-0960-4AFE-A8C9-0CF7645E0EDC)
- [DBMS_CLOUD_OCI_IDENTITY_FAULT_DOMAIN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4D033F1E-FA0C-4F00-B3BD-4F3285516BE6)
- [DBMS_CLOUD_OCI_IDENTITY_GROUP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4B290D77-8BCE-4A26-9E28-F9B4BE094129)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-F6C4CB52-A5BC-43E5-8D5A-0E69585F1B00)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-16802CBA-832B-4251-B295-258AD549A5B2)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-BD1030A7-D815-4D89-8156-7935DEC47D07)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_ERROR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-36C42E3F-8910-4F79-80E4-D7995C4824E9)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-04AA4460-9FCF-42D7-BA4C-97798F329836)
- [DBMS_CLOUD_OCI_IDENTITY_IAM_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5BF5BC41-2CAB-4BCD-B839-D0A5F4854381)
- [DBMS_CLOUD_OCI_IDENTITY_IDENTITY_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-EC56EDB4-0F9C-4FDE-8687-3072AABDBC53)
- [DBMS_CLOUD_OCI_IDENTITY_IDENTITY_PROVIDER_GROUP_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D3AE3B3F-3652-4FBC-A46E-6D281AEC55A3)
- [DBMS_CLOUD_OCI_IDENTITY_IDP_GROUP_MAPPING_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-DD72E65F-2DFD-44C4-A91B-7C406A28952C)
- [DBMS_CLOUD_OCI_IDENTITY_IMPORT_STANDARD_TAGS_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-1B45C4F6-615B-4D9B-B523-7024BF074E6F)
- [DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_DEVICE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-74E6A0DF-5553-48C8-9814-A7A19464415B)
- [DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_DEVICE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-A9DFC287-8E2F-4AA8-9529-1EE64D0E1D1C)
- [DBMS_CLOUD_OCI_IDENTITY_MFA_TOTP_TOKEN_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-70872C29-62DC-45DD-A22A-DD2E942905CB)
- [DBMS_CLOUD_OCI_IDENTITY_MOVE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-86F76858-D2AF-41E1-BEB0-9EEBFFB4F51E)
- [DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E3DB44B2-2A88-4AA3-9083-B0C1D8818A3A)
- [DBMS_CLOUD_OCI_IDENTITY_NETWORK_SOURCES_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-DC01984B-4F8A-4E4A-AA27-DE4309C3FE3B)
- [DBMS_CLOUD_OCI_IDENTITY_O_AUTH2_CLIENT_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E37C45FA-F8DC-4CB1-9960-23FA74EFEB55)
- [DBMS_CLOUD_OCI_IDENTITY_O_AUTH2_CLIENT_CREDENTIAL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D069AA01-D5FD-43D1-90DD-AD3B428E6F20)
- [DBMS_CLOUD_OCI_IDENTITY_POLICY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E89C1721-9988-471F-A7EA-99121B4C6FA1)
- [DBMS_CLOUD_OCI_IDENTITY_REGION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-ECB2BAE4-629A-472B-9B19-BD35F5FECB46)
- [DBMS_CLOUD_OCI_IDENTITY_REGION_SUBSCRIPTION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-9B6074D0-33D1-4371-B4B2-25C973F97D06)
- [DBMS_CLOUD_OCI_IDENTITY_REMOVE_LOCK_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2AC0B66C-0A8F-4790-A4D7-EE24D4089ECB)
- [DBMS_CLOUD_OCI_IDENTITY_RESOURCE_LOCK_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-429D5FAA-BE94-42DC-A094-7B2C436C996E)
- [DBMS_CLOUD_OCI_IDENTITY_SAML2_IDENTITY_PROVIDER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-97CE5A32-D796-46D9-BD32-71B534AEB91E)
- [DBMS_CLOUD_OCI_IDENTITY_SCIM_CLIENT_CREDENTIALS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C0249515-DC27-4EDB-B64F-568A89CBBC01)
- [DBMS_CLOUD_OCI_IDENTITY_SMTP_CREDENTIAL_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-6535F9CF-3F5E-45DE-B664-2D6CC2B31AC5)
- [DBMS_CLOUD_OCI_IDENTITY_SMTP_CREDENTIAL_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-AB0105FF-FEB8-439E-8471-06DAAB95B604)
- [DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_DEFINITION_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-89E20E12-8746-47E6-9D7C-10D1D939A7F0)
- [DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_DEFINITION_TEMPLATE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-BF12C87F-5581-4528-9777-6BEC16D2FA26)
- [DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_NAMESPACE_TEMPLATE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7A67D06E-56F1-47B4-80C3-8BC4B2705664)
- [DBMS_CLOUD_OCI_IDENTITY_STANDARD_TAG_NAMESPACE_TEMPLATE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2B16A413-F00F-4E8D-9A2C-F93452DE16E8)
- [DBMS_CLOUD_OCI_IDENTITY_SWIFT_PASSWORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-012059C6-3FFE-4C7E-95E3-6E638C017EE3)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E0427F28-57DB-408F-A2A8-A49BCEA1FFAE)
- [DBMS_CLOUD_OCI_IDENTITY_RESOURCE_LOCK_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-DD8F3817-1FEA-4D20-9663-1010210B52AA)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_DEFAULT_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7EC0E977-6E54-49AA-8BA8-4D0F06916A94)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_DEFAULT_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-E5DA3D43-B439-4B7C-B484-AB52A20C46D1)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_NAMESPACE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-90F90498-A755-4D45-841C-B3ADEA508319)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_NAMESPACE_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-F19B91F5-AA00-4C8C-AFF7-A3652091DA82)
- [DBMS_CLOUD_OCI_IDENTITY_TAG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5BF932F2-1915-479D-BFBD-D65AC0CA812B)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_RESOURCE_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-585BA51E-9597-4CC7-AE8D-9F1AA6862425)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_RESOURCE_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-EED22089-095A-4315-B037-520773C7793A)
- [DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-B75A0975-BE67-4347-8E29-65B110FAB701)
- [DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_ERROR_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-3082E47E-A742-454D-9ABB-279B6F4DFD5E)
- [DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_LOG_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-EEF68F97-41A0-4179-8BBE-01416B87B0DD)
- [DBMS_CLOUD_OCI_IDENTITY_TAGGING_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4B8EED3F-9A2F-426C-838C-1F2648EA2663)
- [DBMS_CLOUD_OCI_IDENTITY_TENANCY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-204017CB-1C73-47F9-A4F6-B82707E5D748)
- [DBMS_CLOUD_OCI_IDENTITY_UI_PASSWORD_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-0E078821-D0BB-4C52-9327-8769512882D1)
- [DBMS_CLOUD_OCI_IDENTITY_UI_PASSWORD_INFORMATION_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C2FC7755-361E-4B2E-BDC7-8CFD42A8C903)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_AUTH_TOKEN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-FD5196AA-9D58-4ABD-AD0A-83B0BD5E4E12)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_AUTHENTICATION_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-89B74B80-5BD2-4415-A4EF-B208C572BC3C)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_COMPARTMENT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5C4C7D7F-4AB8-4148-BC63-A974FB14148F)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_CUSTOMER_SECRET_KEY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-1C2CB79C-7C8A-4AEC-A319-A811A69A2023)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_DOMAIN_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2A5D76BB-A460-4084-A1CE-9845F293A251)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_DYNAMIC_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-570B3F60-93F5-40D8-878E-39D8DE69E209)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_GROUP_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-9287BF0B-33B3-4906-8273-9804D42C2891)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_IDENTITY_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-B1A17C12-EFE7-46B9-A6A6-2B4DF033ECE3)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_IDP_GROUP_MAPPING_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-1F767903-BE72-4F49-B894-2772569E82BC)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_NETWORK_SOURCE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2D32917F-8ABB-4F9B-96DE-323F8E589BB8)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_O_AUTH2_CLIENT_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-5455C46E-E88E-4051-BF30-29BB0946A9BF)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_POLICY_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4784D6EB-FA99-4B7C-86CB-9BB095578A98)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_SAML2_IDENTITY_PROVIDER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2CAB294B-119D-480A-857B-7DED687EE085)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_SMTP_CREDENTIAL_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7F303407-85FC-442E-9518-71E9AC3F38A1)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_STATE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-BBE19AB1-3EC1-4B94-BF4E-D5D4B759740B)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_SWIFT_PASSWORD_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-CF540843-2836-4FD3-8755-D46ABAC568FD)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_DEFAULT_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7238C2AA-A1F9-4848-A652-D8332E04B9B4)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-0E9AE2AC-2D5F-47C5-9C6D-F2E024E1750A)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_TAG_NAMESPACE_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-CF4D0259-871D-485B-922E-DA04722724EA)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_USER_CAPABILITIES_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-C443A71B-C11E-4D49-8E9F-2CF9AB08F238)
- [DBMS_CLOUD_OCI_IDENTITY_UPDATE_USER_DETAILS_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-D34DB5EB-EFE2-4AF9-A40F-05A1785E44E8)
- [DBMS_CLOUD_OCI_IDENTITY_USER_CAPABILITIES_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-CE289487-7EE1-4757-A554-3C7EAE359CFE)
- [DBMS_CLOUD_OCI_IDENTITY_USER_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-71F99FB1-3405-4393-9C34-0D5980BE687F)
- [DBMS_CLOUD_OCI_IDENTITY_USER_GROUP_MEMBERSHIP_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-9CAB8648-ECAB-4162-BE47-AAE82DC5F461)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_ERROR_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-FB973ABF-A213-4988-9FB4-951C0428CC86)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_LOG_ENTRY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-2E6C9637-F3D8-497E-ABC4-77CF599EB5A8)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_ERROR_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-7C1A8CF4-CBFF-4A2B-8171-9BDFBF20E04B)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_LOG_ENTRY_TBL Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-3EC16B97-0894-474C-B025-CDE0319B2DD4)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-48E731EB-5D27-4324-98A2-752C5018EDFB)
- [DBMS_CLOUD_OCI_IDENTITY_WORK_REQUEST_SUMMARY_T Type](https://docs.oracle.com/iaas/Content/pl-sql-sdk/doc/identity_t.html#ADSDK-GUID-4753FED1-CDDA-4D8D-9586-92A5197DD58A)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
